import datetime
import logging
import os
import re
import uuid
from operator import itemgetter
from pathlib import Path

import chromadb.config
import yaml
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich import print

import config
from prompts import BASE_SYSTEM_PROMPT
from vectorstore_incremental import FileIndexManager

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", config.CHUNK_OVERLAP))
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", config.CHUNK_SIZE))
DATA_DIR = os.getenv("DATA_DIR", config.DATA_DIR)
PERSIST_DIR = config.PERSIST_DIR

def _parse_frontmatter(file: Path, content: str):
    """Extract YAML frontmatter and return (metadata, text_content).

    Uses a regex that only matches '---' at the very start of the file,
    followed by a closing '---' on its own line, to avoid false splits
    on horizontal rules or code blocks.  Metadata values that are lists
    are converted to lists of strings; other non-primitive values are
    coerced to strings for ChromaDB compatibility.
    """
    frontmatter_match = re.match(
        r'\A---\r?\n(.*?)\r?\n---\r?\n(.*)', content, re.DOTALL
    )
    if frontmatter_match:
        try:
            raw_metadata = yaml.safe_load(frontmatter_match.group(1)) or {}
            # Sanitize metadata for ChromaDB compatibility
            metadata = {}
            for key, value in raw_metadata.items():
                if isinstance(value, list):
                    metadata[key] = [str(item) for item in value]
                elif isinstance(value, (str, int, float, bool)):
                    metadata[key] = value
                elif value is not None:
                    metadata[key] = str(value)
        except yaml.YAMLError:
            logging.warning("Failed to parse YAML frontmatter in %s", file)
            metadata = {}
        text_content = frontmatter_match.group(2).strip()
    else:
        metadata = {}
        text_content = content
    return metadata, text_content


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
    ollama_embedding_model = os.getenv("OLLAMA_EMBEDDING_MODEL")
    openai_api_key = os.getenv("OPENAI_API_KEY", "").strip()
    use_ollama = not openai_api_key or openai_api_key == "sk-"

    if ollama_embedding_model:
        try:
            from langchain_ollama import ChatOllama, OllamaEmbeddings
        except ImportError as exc:
            raise ImportError(
                "langchain-ollama is required when OPENAI_API_KEY is not set. "
                "Install it with: pip install langchain-ollama"
            ) from exc

        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        ollama_chat_model = os.getenv("OLLAMA_CHAT_MODEL", "llama3.2")

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

    # Determine if we should do incremental update
    incremental = os.getenv("VECTORSTORE_INCREMENTAL", "true").lower() == "true"

    if persist_path.exists():
        # Load existing vectorstore
        vectorstore = Chroma(
            persist_directory=str(persist_path),
            embedding_function=embedding_model,
            client_settings=chromadb.config.Settings(
                anonymized_telemetry=False
            ),
        )

        # Check if incremental update is enabled and config hasn't changed
        if incremental:
            file_index = FileIndexManager(persist_path)

            # Check if configuration changed (chunk size, overlap, model)
            if file_index.config_changed(
                CHUNK_SIZE, CHUNK_OVERLAP,
                ollama_embedding_model if ollama_embedding_model else "text-embedding-ada-002"
            ):
                if debug:
                    print("[yellow]⚠️  Configuration changed, full rebuild required[/yellow]")
                incremental = False
            else:
                # Detect file changes
                files = sorted(DATA_DIR.glob("*.md"))
                new_or_modified, unchanged, deleted = file_index.detect_changes(files)

                if debug:
                    print("[cyan]📊 Incremental update:[/cyan]")
                    print(f"  - New/Modified: {len(new_or_modified)}")
                    print(f"  - Unchanged: {len(unchanged)}")
                    print(f"  - Deleted: {len(deleted)}")

                # Delete removed files from vectorstore
                for deleted_path in deleted:
                    chunk_ids = file_index.remove_file_entry(deleted_path)
                    if chunk_ids:
                        try:
                            vectorstore._collection.delete(ids=chunk_ids)
                            if debug:
                                print(f"[red]🗑️  Deleted: {Path(deleted_path).name}[/red]")
                        except Exception as e:
                            if debug:
                                print(f"[yellow]⚠️  Could not delete {Path(deleted_path).name}: {e}[/yellow]")

                # Process new/modified files
                if new_or_modified:
                    for file in new_or_modified:
                        # Delete old chunks if file was modified
                        path_str = str(file.resolve())
                        old_chunk_ids = file_index.get_chunk_ids_for_file(path_str)
                        if old_chunk_ids:
                            try:
                                vectorstore._collection.delete(ids=old_chunk_ids)
                            except Exception:
                                pass

                        # Process file
                        with open(file, 'r', encoding='utf-8') as f:
                            content = f.read()

                        metadata, text_content = _parse_frontmatter(file, content)

                        # Create document and split into chunks
                        doc = Document(page_content=text_content, metadata=metadata)
                        chunks = RecursiveCharacterTextSplitter(
                            chunk_size=CHUNK_SIZE,
                            chunk_overlap=CHUNK_OVERLAP
                        ).split_documents([doc])

                        # Generate unique IDs for chunks
                        chunk_ids = [str(uuid.uuid4()) for _ in chunks]

                        # Add chunks to vectorstore
                        vectorstore.add_documents(chunks, ids=chunk_ids)

                        # Update file index
                        file_index.update_file_entry(file, chunk_ids)

                        if debug:
                            print(f"[green]✅ Updated: {file.name} ({len(chunks)} chunks)[/green]")

                    # Save updated index
                    file_index.save_index()

                    if debug:
                        print("[bold green]✅ Incremental update complete[/bold green]")
                else:
                    if debug:
                        print("[bold green]✅ No changes detected[/bold green]")
        else:
            if debug:
                print("[yellow]Incremental updates disabled, using existing vectorstore[/yellow]")

    else:
        # First time build - create vectorstore from scratch
        files = sorted(DATA_DIR.glob("*.md"))
        all_docs = []
        file_to_chunks = {}

        for file in files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()

            metadata, text_content = _parse_frontmatter(file, content)
            all_docs.append(Document(page_content=text_content, metadata=metadata))
            file_to_chunks[str(file.resolve())] = []

        # Split documents per file to track chunk ownership, then build vectorstore
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
        )
        all_chunks = []
        chunk_ids = []
        for doc_idx, doc in enumerate(all_docs):
            file_path = str(files[doc_idx].resolve())
            doc_chunks = splitter.split_documents([doc])
            ids = [str(uuid.uuid4()) for _ in doc_chunks]
            all_chunks.extend(doc_chunks)
            chunk_ids.extend(ids)
            file_to_chunks[file_path] = ids

        vectorstore = Chroma.from_documents(
            all_chunks,
            embedding=embedding_model,
            persist_directory=str(persist_path),
            ids=chunk_ids,
            client_settings=chromadb.config.Settings(
                anonymized_telemetry=False
            ),
        )

        # Create and save file index
        file_index = FileIndexManager(persist_path)
        for file in files:
            path_str = str(file.resolve())
            file_index.update_file_entry(file, file_to_chunks[path_str])
        file_index.update_config(
            CHUNK_SIZE,
            CHUNK_OVERLAP,
            ollama_embedding_model if ollama_embedding_model else "text-embedding-ada-002"
        )
        file_index.save_index()

        if debug:
            print(f"[bold green]✅ Vector store created with {len(files)} files[/bold green]")

    retriever = vectorstore.as_retriever(
        search_type="similarity", search_kwargs={"k": 20}
    )
    today = datetime.datetime.now().strftime("%B %d, %Y %H:%M:%S")
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "human",
                f"""{BASE_SYSTEM_PROMPT.format(today=today)}
**Konversationsverlauf:**
{{conversation_context}}

Frage: {{question}}
Kontext: {{context}}
Antwort:""",
            )
        ]
    )

    if use_ollama:
        llm = ChatOllama(
            # format="json",
            model=ollama_chat_model,
            base_url=ollama_base_url,
            temperature=0,
        )
    else:
        llm = ChatOpenAI(
            model_name=os.getenv("CHAT_MODEL", "gpt-4o-mini-2024-07-18"),
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
