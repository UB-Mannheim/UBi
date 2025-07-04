import os
from tqdm import tqdm
from rich import print
from pathlib import Path
from openai import OpenAI
from dotenv import set_key, load_dotenv
from config import (
    ENV_PATH,
    DATA_DIR,
    USE_OPENAI_VECTORSTORE
)

# === OpenAI Vectorstore Functions ===
def create_openAI_vectorstore():
    """
    Create an OpenAI vectorstore and write its ID to .env.
    """    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Create vectorstore
    vector_store = client.vector_stores.create(name="aima_files")

    # Save vectorestore ID to .env
    set_key(str(ENV_PATH), "OPENAI_VECTORSTORE_ID", vector_store.id)
    return vector_store

def retrieve_openAI_vectorstore(id):
    """
    Retrieve an existing OpenAI vectorstore.
    """    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    vector_store = client.vector_stores.retrieve(vector_store_id=id)
    return vector_store

def get_all_vectorstore_files(client: OpenAI, vectorstore_id: str):
    """
    Get all files linked to the OpenAI vectorstore.
    """
    all_files = []
    after = None
    while True:
        response = client.vector_stores.files.list(
            vector_store_id=str(vectorstore_id),
            limit=100,
            after=after
        )
        files = list(response)
        if not files:
            break
        all_files.extend(files)
        # The API returns files in order; use the last file's id as the next 'after'
        after = files[-1].id
        if len(files) < 100:
            break
    return all_files

def upload_files_to_openAI_vectorstore(
    upload_dir: Path,
    files_to_upload: list[str],
    vectorstore_id: str
    ):
    """
    Upload markdown files to an existing OpenAI vectorstore.
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))    
    md_files = [Path(f"{upload_dir}/{file}") for file in files_to_upload]

    # Get all files in the vectorstore (with pagination)
    vector_store_files = get_all_vectorstore_files(client, vectorstore_id)
    print(f"[bold]{len(vector_store_files)} files in vectorstore: {vectorstore_id}")

    # Build a set of filenames already in the vectorstore
    if len(vector_store_files) >= 1:
        print(f"[bold]Retrieving filenames from vectorstore ...")
        vectorstore_filenames = {client.files.retrieve(f.id).filename: f.id for f in tqdm(vector_store_files)}
    else:
        vectorstore_filenames = {}

    print(f"🔄 Uploading {len(md_files)} files to OpenAI vectorstore ...")
    
    for md_file in tqdm(md_files):
        filename = md_file.name
        
        # If file exists in vectorstore, unlink and delete it first
        if filename in vectorstore_filenames:
            try:
                # Unlink file from vectorstore
                client.vector_stores.files.delete(
                    vector_store_id=str(vectorstore_id),
                    file_id=vectorstore_filenames[filename]
                )
                # Delete file from OpenAI storage
                print(f"Deleting old {filename} from vectorstore ...")
                client.files.delete(
                    file_id=vectorstore_filenames[filename]
                )
            except Exception as e:
                print(f"Error deleting {filename} from vectorstore: {e}")

        # Upload the file
        try:
            with open(md_file, "rb") as f:
                uploaded_file = client.files.create(
                    file=f,
                    purpose="user_data"
                )
                
            # Link uploaded file to vectorstore
            client.vector_stores.files.create(
                vector_store_id=str(vectorstore_id),
                file_id=uploaded_file.id
            )
        except Exception as e:
            print(f"Error uploading {filename}: {e}")

    print(f"✅ Finished.")

def initialize_vectorstore():
    """
    Create or load an OpenAI vectorstore and upload all files from
    DATA_DIR to it if they were updated previously.
    """
    if not USE_OPENAI_VECTORSTORE:
        print("Aborting: OpenAI vectorstore is disabled in config.py")
        return

    # Load config from .env
    load_dotenv(str(ENV_PATH))
    OPENAI_VECTORSTORE_ID = os.getenv("OPENAI_VECTORSTORE_ID")
    DATA_DIR_UPDATED = True if os.getenv("DATA_DIR_UPDATED") == "True" else False

    vectorstore_created = False
    try:
        if not OPENAI_VECTORSTORE_ID:
            # Create an OpenAI vectorstore
            print("[bold]No OPENAI_VECTORSTORE_ID found. Creating new OpenAI vectorstore...")
            vectorstore = create_openAI_vectorstore()
            print(f"[bold]Created new vectorstore with ID: {vectorstore.id}")
            vectorstore_created = True

            # Reload .env and OPENAI_VECTORSTORE_ID after creation
            load_dotenv(str(ENV_PATH))
            OPENAI_VECTORSTORE_ID = os.getenv("OPENAI_VECTORSTORE_ID")

        # If vectorstore was created or DATA_DIR_UPDATED upload files
        if vectorstore_created or DATA_DIR_UPDATED:
            print(f"[bold]Using OpenAI vectorstore: {OPENAI_VECTORSTORE_ID}")
            all_md_files = [f.name for f in Path(DATA_DIR).glob('*.md')]
            upload_files_to_openAI_vectorstore(
                upload_dir=DATA_DIR,
                files_to_upload=all_md_files,
                vectorstore_id=str(OPENAI_VECTORSTORE_ID)
            )
    except Exception as e:
        print(f'Error: {e}')
