import datetime
import os
from operator import itemgetter

import chromadb.config
from config import CHUNK_OVERLAP, CHUNK_SIZE, DATA_DIR, PERSIST_DIR
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from prompts import BASE_SYSTEM_PROMPT
from rich import print


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


async def create_rag_chain(debug=False):
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )
    model_name = "openai_ada"
    persist_path = (
        PERSIST_DIR / f"{model_name}_c{CHUNK_SIZE}_o{CHUNK_OVERLAP}_ub"
    )

    if persist_path.exists():
        vectorstore = Chroma(
            persist_directory=str(persist_path),
            embedding_function=embedding_model,
            client_settings=chromadb.config.Settings(
                anonymized_telemetry=False
            ),
        )
    else:
        files = sorted(DATA_DIR.glob("*.md"))
        all_docs = []
        for file in files:
            all_docs.extend(UnstructuredMarkdownLoader(str(file)).load())

        chunks = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        ).split_documents(all_docs)
        vectorstore = Chroma.from_documents(
            chunks,
            embedding=embedding_model,
            persist_directory=str(persist_path),
            client_settings=chromadb.config.Settings(
                anonymized_telemetry=False
            ),
        )

    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 4}
    )
    prompt = hub.pull("rlm/rag-prompt")
    today = datetime.datetime.now().strftime("%B %d, %Y %H:%M:%S")
    prompt.messages[
        0
    ].prompt.template = f"""{BASE_SYSTEM_PROMPT.format(today=today)}
**Konversationsverlauf:**
{{conversation_context}}

Frage: {{question}}
Kontext: {{context}}
Antwort:"""

    llm = ChatOpenAI(
        model_name="gpt-4o-mini-2024-07-18",
        temperature=0,
        streaming=True,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    def log_prompt(prompt):
        if debug:
            print(
                f"\n[bold yellow]Prompt sent to LLM:[/bold yellow]\n{prompt}\n"
            )
        return prompt

    return (
        {
            "context": itemgetter("question") | retriever | format_docs,
            "question": itemgetter("question"),
            "conversation_context": itemgetter("conversation_context"),
            "language": itemgetter("language"),
        }
        | prompt
        | log_prompt  # Log the prompt before sending to LLM
        | llm
        | StrOutputParser()
    )
