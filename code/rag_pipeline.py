import chromadb.config
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from config import DATA_DIR, PERSIST_DIR, CHUNK_SIZE, CHUNK_OVERLAP
from operator import itemgetter
import datetime
import os
from conversation_memory import create_conversation_context
from language_detection import detect_language_and_get_name


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


async def create_rag_chain():
    embedding_model = OpenAIEmbeddings(
        model="text-embedding-ada-002",
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )
    model_name = "openai_ada"
    persist_path = PERSIST_DIR / f"{model_name}_c{CHUNK_SIZE}_o{CHUNK_OVERLAP}_ub"

    if persist_path.exists():
        vectorstore = Chroma(
            persist_directory=str(persist_path),
            embedding_function=embedding_model,
            client_settings=chromadb.config.Settings(
                anonymized_telemetry=False
            )
        )
    else:
        files = sorted(DATA_DIR.glob("*.md"))
        all_docs = []
        for file in files:
            all_docs.extend(UnstructuredMarkdownLoader(str(file)).load())

        chunks = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP).split_documents(all_docs)
        vectorstore = Chroma.from_documents(
            chunks,
            embedding=embedding_model,
            persist_directory=str(persist_path),
            client_settings=chromadb.config.Settings(
                anonymized_telemetry=False
            )
        )

    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
    prompt = hub.pull("rlm/rag-prompt")
    today = datetime.datetime.now().strftime('%B %d, %Y %H:%M:%S')

    prompt.messages[0].prompt.template = f"""Du bist der virtuelle Assistent der Universitätsbibliothek Mannheim.
Freundlich, kompetent und unterstützend beantwortest du Fragen zur Nutzung der Bibliothek,
zu Services, Recherchemöglichkeiten und mehr.
**Regeln:**
1. Nutze nur die bereitgestellten Daten.
2. Keine externen Inhalte, wenn Kontext fehlt.
3. Antworten max. 500 Zeichen lang.
4. Wenn du etwas nicht weißt, verweise auf den UB-Chat (Mo–Fr, 10–18 Uhr): https://www2.bib.uni-mannheim.de/mibew/index.php/chat?locale=de
5. Keine Annahmen, Erfindungen oder Fantasie-URLs.
6. Keine Buchempfehlungen – verweise stattdessen auf die Primo-Suche: https://primo.bib.uni-mannheim.de
7. Keine Paperempfehlungen - verweise stattdessen auf die MADOC-Suche: https://madoc.bib.uni-mannheim.de
8. Keine Datenempfehlungen - verweise stattdessen auf die MADATA-Suche: https://madata.bib.uni-mannheim.de
9. Antworte immer in der Sprache: {{language}}.
10. Heute ist {today}. Nutze das für aktuelle Fragen (z. B. Öffnungszeiten). Verweise auf: https://www.bib.uni-mannheim.de/oeffnungszeiten

**Konversationsverlauf:**
{{conversation_context}}

Frage: {{question}}
Kontext: {{context}}
Antwort:"""

    llm = ChatOpenAI(model_name="gpt-4o-mini-2024-07-18", temperature=0, streaming=True, openai_api_key=os.getenv("OPENAI_API_KEY"))

    return (
        {
            "context": itemgetter("question") | retriever | format_docs,
            "question": itemgetter("question"),
            "conversation_context": itemgetter("conversation_context"),
            "language": itemgetter("language")
        }
        | prompt
        | llm
        | StrOutputParser()
    )
