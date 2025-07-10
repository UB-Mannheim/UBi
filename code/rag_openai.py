import os
import asyncio
import utils
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
        remote_file_id = vectorstore_filenames[filename]
        try:
            await asyncio.to_thread(client.vector_stores.files.delete,
                vector_store_id=str(vectorstore_id),
                file_id=remote_file_id
            )
            print(f"[bold]Deleted {filename} from vectorstore.")
            await asyncio.to_thread(client.files.delete, file_id=remote_file_id)
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
        if filename in vectorstore_filenames:
            vectorstore_file_id = vectorstore_filenames[filename]
            
            # Delete the file that gets replaced in the vectorstore first
            try:
                # Unlink file from vectorstore
                await asyncio.to_thread(client.vector_stores.files.delete,
                    vector_store_id=str(vectorstore_id),
                    file_id=vectorstore_file_id
                    )
                # Delete file from vectorstore
                print(f"[bold]Deleting old {filename} from vectorstore ...")
                await asyncio.to_thread(
                    client.files.delete,
                    file_id=vectorstore_file_id
                    )
            except Exception as e:
                print(f"[bold]Error deleting {filename} from vectorstore: {e}")

        # File Upload
        try:
            # Upload the updated local file to vectorstore
            print(f"[bold]Uploading updated {filename} to vectorstore ...")
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
        pbar_up.update(1)
    await asyncio.gather(*(upload_file(md_file) for md_file in md_files))
    pbar_up.close()

async def get_vectorstore_filenames(
    client: OpenAI,
    vectorstore_id: str
    ) -> dict:
    """
    Async helper to retrieve a dict mapping filename to file_id for all files
    in the vectorstore.
    """
    vector_store_files = await asyncio.to_thread(get_all_vectorstore_files, client, vectorstore_id)
    if vector_store_files:
        async def retrieve_file(f):
            file_obj = await asyncio.to_thread(client.files.retrieve, f.id)
            return (file_obj.filename, f.id)
        results = await asyncio.gather(*(retrieve_file(f) for f in vector_store_files))
        return dict(results)
    else:
        return {}

async def async_sync_files_with_vectorstore(
    upload_dir: Path,
    files_to_upload: list[str],
    vectorstore_id: str,
    vectorstore_filenames: dict = {},
    ):
    """
    Async upload markdown files to an existing OpenAI vectorstore.
    Also, delete files from the vectorstore that are not in files_to_upload.
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))    
    md_files = [Path(f"{upload_dir}/{file}") for file in files_to_upload]

    # Only fetch vectorstore files if not provided (empty dict)
    if not vectorstore_filenames:
        print(f"[bold]Retrieving filenames from vectorstore ...")
        vectorstore_filenames = await get_vectorstore_filenames(client, vectorstore_id)
        print(f"[bold]{len(vectorstore_filenames)} files in vectorstore: {vectorstore_id}")
    else:
        print(f"[bold]{len(vectorstore_filenames)} files in vectorstore: {vectorstore_id}")

    # Get all local markdowns in upload_dir
    all_local_files_set = set([f.name for f in upload_dir.glob('*.md')])
    
    # Create a set of unique filenames currently in the vectorstore
    vectorstore_filenames_set = set(vectorstore_filenames.keys())
    
    # Delete files in vectorstore if they are not present in local files anymore
    files_to_delete = vectorstore_filenames_set - all_local_files_set
    
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
    Create or load an OpenAI vectorstore and upload only files from
    DATA_DIR that were updated (hash comparison with md_hashes.json).
    """
    # Load config from .env
    load_dotenv(str(ENV_PATH))
    USE_OPENAI_VECTORSTORE = True if os.getenv("USE_OPENAI_VECTORSTORE") == "True" else False
    if not USE_OPENAI_VECTORSTORE:
        print("[bold]Aborting: OpenAI vectorstore is disabled in .env")
        return
    OPENAI_VECTORSTORE_ID = os.getenv("OPENAI_VECTORSTORE_ID")

    try:
        if not OPENAI_VECTORSTORE_ID:
            # Create a new OpenAI vectorstore
            print("[bold]No OPENAI_VECTORSTORE_ID found. Creating new OpenAI vectorstore...")
            vectorstore = create_openAI_vectorstore()
            print(f"[bold]Created new vectorstore with ID: {vectorstore.id}")

            # Reload .env and OPENAI_VECTORSTORE_ID after creation
            load_dotenv(str(ENV_PATH))
            OPENAI_VECTORSTORE_ID = os.getenv("OPENAI_VECTORSTORE_ID")

            # Get all files from DATA_DIR for upload
            files_to_upload = [f.name for f in DATA_DIR.glob('*.md')]
            files_to_delete = set()
            vectorstore_filenames = {}
        else:
            print(f"[bold]Using OpenAI vectorstore: {OPENAI_VECTORSTORE_ID}")
            print(f"[bold]Syncing local files to vectorstore ...")

            client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

            # Check for updated files in DATA_DIR
            files_to_upload = utils.get_new_or_modified_files_by_hash(
                directory=DATA_DIR
                )

            # Check for deleted files in DATA_DIR
            vectorstore_filenames = asyncio.run(get_vectorstore_filenames(
                client,
                str(OPENAI_VECTORSTORE_ID))
                )
            vectorstore_filenames_set = set(vectorstore_filenames.keys())
            all_local_files_set = set([f.name for f in DATA_DIR.glob('*.md')])
            files_to_delete = vectorstore_filenames_set - all_local_files_set

            print(f"[bold]{len(vectorstore_filenames)} files in vectorstore: {OPENAI_VECTORSTORE_ID}")

        # Only skip if there are truly no changes (no upload, no delete)
        if files_to_upload or files_to_delete:
            if files_to_upload:
                print(f"[bold]Uploading {len(files_to_upload)} changed/new files to vectorstore ...")
            if files_to_delete:
                print(f"[bold]Deleting {len(files_to_delete)} files from vectorstore ...")

            # Sync (will handle both upload and delete)
            asyncio.run(async_sync_files_with_vectorstore(
                upload_dir=DATA_DIR,
                files_to_upload=files_to_upload,
                vectorstore_id=str(OPENAI_VECTORSTORE_ID),
                vectorstore_filenames=vectorstore_filenames
            ))

            # Write hash snapshot
            utils.write_hashes_for_directory(DATA_DIR)
        else:
            print("[bold green]No changes detected in DATA_DIR since last sync. Skipping vectorstore upload.")
    except Exception as e:
        print(f'Error: {e}')
