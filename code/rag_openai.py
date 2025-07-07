import os
import asyncio
from tqdm import tqdm
from rich import print
from pathlib import Path
from openai import OpenAI
from dotenv import set_key, load_dotenv
from config import ENV_PATH, DATA_DIR

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

def get_all_vectorstore_files(client: OpenAI, vectorstore_id: str):
    """
    Get all files linked to the OpenAI vectorstore.
    """
    all_files = []
    after = None
    while True:
        if after is not None:
            response = client.vector_stores.files.list(
                vector_store_id=str(vectorstore_id),
                limit=100,
                after=after
            )
        else:
            response = client.vector_stores.files.list(
                vector_store_id=str(vectorstore_id),
                limit=100
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

async def async_delete_files_from_vectorstore(
    client: OpenAI,
    vectorstore_id: str,
    vectorstore_filenames: dict,
    files_to_delete: set
    ):
    """
    Async delete files from vectorstore and OpenAI storage, with progress bar.
    """
    pbar_del = tqdm(total=len(files_to_delete), desc="Deleting files", leave=False)
    async def delete_file(filename):
        remote_file_id, _ = vectorstore_filenames[filename]
        try:
            await asyncio.to_thread(client.vector_stores.files.delete,
                vector_store_id=str(vectorstore_id),
                file_id=remote_file_id
            )
            print(f"[bold]Deleted {filename} from vectorstore.")
            await asyncio.to_thread(client.files.delete, file_id=remote_file_id)
            print(f"[bold]Deleted {filename} from OpenAI storage.")
        except Exception as e:
            print(f"[bold]Error deleting {filename} from vectorstore/OpenAI storage: {e}")
        pbar_del.update(1)
    await asyncio.gather(*(delete_file(filename) for filename in files_to_delete))
    pbar_del.close()

async def async_upload_files_to_vectorstore(
    client: OpenAI,
    vectorstore_id: str,
    vectorstore_filenames: dict,
    md_files: list
    ):
    """
    Async upload new or updated files to vectorstore, with progress bar.
    """
    pbar_up = tqdm(total=len(md_files), desc="Uploading files", leave=False)
    async def upload_file(md_file):
        filename = md_file.name
        local_byte_size = os.path.getsize(md_file)
        upload_needed = True

        if filename in vectorstore_filenames:
            remote_file_id, remote_byte_size = vectorstore_filenames[filename]
            if local_byte_size == remote_byte_size:
                upload_needed = False
            else:
                try:
                    # Unlink file from vectorstore
                    await asyncio.to_thread(client.vector_stores.files.delete,
                        vector_store_id=str(vectorstore_id),
                        file_id=remote_file_id
                    )
                    # Delete file from OpenAI storage
                    print(f"[bold]Deleting old {filename} from vectorstore ...")
                    await asyncio.to_thread(client.files.delete, file_id=remote_file_id)
                except Exception as e:
                    print(f"[bold]Error deleting {filename} from vectorstore: {e}")
        if upload_needed:
            try:
                with open(md_file, "rb") as f:
                    uploaded_file = await asyncio.to_thread(
                        client.files.create,
                        file=f,
                        purpose="user_data"
                        )
                # Link uploaded file to vectorstore
                await asyncio.to_thread(client.vector_stores.files.create,
                    vector_store_id=str(vectorstore_id),
                    file_id=uploaded_file.id
                )
            except Exception as e:
                print(f"Error uploading {filename}: {e}")
        else:
            print(f"[bold]Skipping Upload: [blue]{filename}[/blue] is unchanged (byte size matches).")
        pbar_up.update(1)
    await asyncio.gather(*(upload_file(md_file) for md_file in md_files))
    pbar_up.close()

async def async_sync_files_with_vectorstore(
    upload_dir: Path,
    files_to_upload: list[str],
    vectorstore_id: str
    ):
    """
    Async upload markdown files to an existing OpenAI vectorstore.
    Only upload if the file is new or its byte size differs from the one 
    in the vectorstore. Also, delete files from the vectorstore that are 
    not in files_to_upload.
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))    
    md_files = [Path(f"{upload_dir}/{file}") for file in files_to_upload]

    # Get all files in the vectorstore (with pagination)
    vector_store_files = await asyncio.to_thread(
        get_all_vectorstore_files,
        client,
        vectorstore_id
        )
    print(f"[bold]{len(vector_store_files)} files in vectorstore: {vectorstore_id}")

    # Build a dict: filename -> (file_id, byte_size)
    if len(vector_store_files) >= 1:
        print(f"[bold]Retrieving filenames and byte sizes from vectorstore ...")
        async def retrieve_file(f):
            file_obj = await asyncio.to_thread(client.files.retrieve, f.id)
            return (file_obj.filename, (f.id, file_obj.bytes))
        results = await asyncio.gather(*(retrieve_file(f) for f in vector_store_files))
        vectorstore_filenames = dict(results)
    else:
        vectorstore_filenames = {}

    # Delete files in vectorstore that are not in files_to_upload
    files_to_upload_set = set([Path(f).name for f in files_to_upload])
    vectorstore_filenames_set = set(vectorstore_filenames.keys())
    files_to_delete = vectorstore_filenames_set - files_to_upload_set
    if files_to_delete:
        await async_delete_files_from_vectorstore(
            client,
            vectorstore_id,
            vectorstore_filenames,
            files_to_delete
            )

    # Upload new or updated files to vectorstore
    print(f"🔄 Uploading {len(md_files)} files to OpenAI vectorstore ...")
    await async_upload_files_to_vectorstore(
        client,
        vectorstore_id,
        vectorstore_filenames,
        md_files
        )
    print(f"✅ Finished.")

def initialize_vectorstore():
    """
    Create or load an OpenAI vectorstore and upload all files from
    DATA_DIR to it if they were updated previously.
    """
    # Load config from .env
    load_dotenv(str(ENV_PATH))
    USE_OPENAI_VECTORSTORE = True if os.getenv("USE_OPENAI_VECTORSTORE") == "True" else False
    if not USE_OPENAI_VECTORSTORE:
        print("[bold]Aborting: OpenAI vectorstore is disabled in .env")
        return
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
            asyncio.run(async_sync_files_with_vectorstore(
                upload_dir=DATA_DIR,
                files_to_upload=all_md_files,
                vectorstore_id=str(OPENAI_VECTORSTORE_ID)
            ))
            
            # Reset DATA_DIR_UPDATED
            set_key(ENV_PATH, "DATA_DIR_UPDATED", "False")
            
    except Exception as e:
        print(f'Error: {e}')
