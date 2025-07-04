import os
from tqdm import tqdm
from rich import print
from pathlib import Path
from openai import OpenAI
from dotenv import set_key
from config import ENV_PATH

# === OpenAI Vectorstore Functions ===
def create_openAI_vectorstore():
    """
    Create an OpenAI vectorstore and write its ID to .env.
    """    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Create vectorstore
    vector_store = client.vector_stores.create(name="aima_files")

    # Save vectorestore ID to .env
    set_key(str(ENV_PATH), "VECTORSTORE_ID", vector_store.id)
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
    changed_files: list[str],
    vectorstore_id: str
    ):
    """
    Upload markdown files to an existing OpenAI vectorstore.
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))    
    md_files = [Path(f"{upload_dir}/{file}") for file in changed_files]

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
