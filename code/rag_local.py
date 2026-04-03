import datetime
import logging
import os
import re
import yaml
from operator import itemgetter

import chromadb.config
from config import CHUNK_OVERLAP, CHUNK_SIZE, DATA_DIR, PERSIST_DIR
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from prompts import BASE_SYSTEM_PROMPT
from rich import print


def format_docs(docs):
    formatted = []
    for doc in docs:
        content = doc.page_content

        # Inject source URLs if available in metadata
        source_de = doc.metadata.get('source_url_de', '')
        source_en = doc.metadata.get('source_url_en', '')

        if source_de or source_en:
            content += "\n\n---\n**Available Source URLs:**"
            if source_de:
                content += f"\n- German: {source_de}"
            if source_en:
                content += f"\n- English: {source_en}"

        formatted.append(content)
    return "\n\n".join(formatted)


async def create_rag_chain(debug=False):
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
    use_ollama = not openai_api_key or openai_api_key == "sk-"

    if use_ollama:
        try:
            from langchain_ollama import ChatOllama, OllamaEmbeddings
        except ImportError as exc:
            raise ImportError(
                "langchain-ollama is required when OPENAI_API_KEY is not set. "
                "Install it with: pip install langchain-ollama"
            ) from exc

        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        ollama_chat_model = os.getenv("OLLAMA_CHAT_MODEL", "llama3.2")
        ollama_embedding_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")

        embedding_model = OllamaEmbeddings(
            model=ollama_embedding_model,
            base_url=ollama_base_url,
        )
        model_name = f"ollama_{re.sub(r'[^a-zA-Z0-9_-]', '_', ollama_embedding_model)}"
        persist_path = (
            PERSIST_DIR / f"{model_name}_c{CHUNK_SIZE}_o{CHUNK_OVERLAP}_ub"
        )
    else:
        embedding_model = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            openai_api_key=openai_api_key,
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
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract YAML frontmatter and preserve as metadata.
            # Use a regex that only matches '---' at the very start of the file,
            # followed by a closing '---' on its own line, to avoid false splits
            # on horizontal rules or code blocks.
            frontmatter_match = re.match(
                r'\A---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL
            )
            if frontmatter_match:
                try:
                    metadata = yaml.safe_load(frontmatter_match.group(1)) or {}
                except yaml.YAMLError:
                    logging.warning("Failed to parse YAML frontmatter in %s", file)
                    metadata = {}
                text_content = frontmatter_match.group(2).strip()
            else:
                metadata = {}
                text_content = content

            all_docs.append(Document(page_content=text_content, metadata=metadata))

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

**CRITICAL INSTRUCTION**:
- You MUST respond in the language specified in the "Response Language" field below
- Match your response language to the detected query language
- Provide links appropriate for the response language

**URL Formatting Rules:**
- If source URLs are provided in the context (marked as "Available Source URLs"):
  - For English responses: Use the English source URL if available
  - For German responses: Use the German source URL if available
  - NEVER invent or guess URLs
  - NEVER mix German text with English URLs or vice versa
- Link text MUST match the response language:
  - English response → English link text (e.g., "Learn more", "Contact", "Details")
  - German response → German link text (e.g., "Weitere Informationen", "Kontakt", "Details")

**Response Language:** {{language}}

**Conversation History:**
{{conversation_context}}

**Question:** {{question}}

**Context:** {{context}}

**Answer:**"""

    if use_ollama:
        llm = ChatOllama(
            # format="json",
            model=ollama_chat_model,
            base_url=ollama_base_url,
            temperature=0,
        )
    else:
        llm = ChatOpenAI(
            model_name="gpt-4o-mini-2024-07-18",
            temperature=0,
            streaming=True,
            openai_api_key=openai_api_key,
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
