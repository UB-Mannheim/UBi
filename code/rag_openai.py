import os
import asyncio
import yaml
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
        remote_file_id = vectorstore_filenames[filename]["file_id"]
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

def escape_colons_in_yaml_values(line: str) -> str:
    """
    Escape colons in YAML values to prevent parsing errors.
    Only escapes colons that appear after the first colon (key: value).
    """
    if ':' not in line:
        return line

    # Split on first colon to separate key and value
    parts = line.split(':', 1)
    if len(parts) != 2:
        return line

    key, value = parts

    # If value is quoted, don't escape colons inside quotes
    if value.strip().startswith('"') and value.strip().endswith('"'):
        return line
    if value.strip().startswith("'") and value.strip().endswith("'"):
        return line

    # If value is a list (starts with [), don't escape colons inside brackets
    if value.strip().startswith('['):
        return line

    # Escape colons in the value part by wrapping in quotes
    if ':' in value and not value.strip().startswith('"') and not value.strip().startswith("'"):
        # Wrap the entire value in quotes to escape colons
        escaped_value = f'"{value.strip()}"'
        return f"{key}: {escaped_value}"

    return line

def parse_yaml_header(md_file) -> dict:
    """
    Parse the YAML header of a processed markdown file and return a
    dictionary. Escape ":" in values to make the parsing robust.

    Example YAML Header:
    ---
    title: Datenangebot des Forschungsdatenzentrums (FDZ)
    source_url: https://www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum/datenangebot-des-fdz/
    category: Projekte
    tags: [Forschungsdatenzentrum, Datenbanken, Wirtschafts- und Sozialwissenschaften, Unternehmensdaten, Digitalisierung, Knowledge Graph, Open Data]
    language: de
    ---

    Example return:
    yaml_data = {
        'title': 'Datenangebot des Forschungsdatenzentrums (FDZ)',
        'source_url': 'https://www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum/datenangebot-des-fdz/',
        'category': 'Projekte',
        'tags': ['Forschungsdatenzentrum', 'Datenbanken', 'Wirtschafts- und Sozialwissenschaften', 'Unternehmensdaten', 'Digitalisierung', 'Knowledge Graph', 'Open Data'],
        'language': 'de'
    }
    """
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if file starts with YAML header
        if not content.startswith('---'):
            return {}

        # Find the end of YAML header and escape colons in values
        lines = content.split('\n')
        yaml_lines = []
        in_yaml = False

        for line in lines:
            if line.strip() == '---':
                if not in_yaml:
                    in_yaml = True
                else:
                    break
            elif in_yaml:
                # Escape colons in values to prevent YAML parsing errors
                processed_line = escape_colons_in_yaml_values(line)
                yaml_lines.append(processed_line)

        if not yaml_lines:
            return {}

        # Join YAML lines and parse
        yaml_content = '\n'.join(yaml_lines)
        yaml_data = yaml.safe_load(yaml_content)

        return yaml_data if yaml_data else {}

    except Exception as e:
        print(f"Error parsing YAML header for {md_file}: {e}")
        return {}

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
            vectorstore_file_id = vectorstore_filenames[filename]["file_id"]

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
            # Parse YAML header for attributes
            yaml_data = parse_yaml_header(md_file)

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
                file_id=uploaded_file.id,
                attributes=yaml_data if yaml_data else None
                )
        except Exception as e:
            print(f"Error uploading {filename}: {e}")
        pbar_up.update(1)
    await asyncio.gather(*(upload_file(md_file) for md_file in md_files))
    pbar_up.close()

async def get_vectorstore_fileids_and_metadata(
    client: OpenAI,
    vectorstore_id: str
    ) -> dict[str, dict[str, object]]:
    """
    Async helper to retrieve a dict mapping filename to a dict containing
    file_id and attributes for all files in the vectorstore.
    """
    vector_store_files = await asyncio.to_thread(get_all_vectorstore_files, client, vectorstore_id)
    if vector_store_files:
        async def retrieve_file(f):
            file_obj = await asyncio.to_thread(client.files.retrieve, f.id)
            return (file_obj.filename, {"file_id": f.id, "attributes": f.attributes})
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
        vectorstore_filenames = await get_vectorstore_fileids_and_metadata(
            client,
            vectorstore_id
            )

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

async def check_and_reupload_if_attributes_empty(
    client: OpenAI,
    vectorstore_id: str,
    upload_dir: Path,
    vectorstore_filenames: dict | None = None
    ) -> tuple[bool, dict]:
    """
    Check if any files in the vectorstore have empty attributes.
    If so, reupload all files to ensure attributes are properly set.

    Args:
        client: OpenAI client instance
        vectorstore_id: ID of the vectorstore
        upload_dir: Directory containing files to upload
        vectorstore_filenames: Optional pre-fetched vectorstore metadata to avoid duplicate API calls

    Returns:
        tuple[bool, dict]: (True if reupload was performed, vectorstore_filenames dict)
    """
    print("[bold]Checking vectorstore file attributes...")

    # Get all files from vectorstore with their metadata if not provided
    if vectorstore_filenames is None:
        vectorstore_filenames = await get_vectorstore_fileids_and_metadata(
            client,
            vectorstore_id
        )

    if not vectorstore_filenames:
        print("[bold]No files found in vectorstore. Nothing to check.")
        return False, {}

    # Check if any files have empty attributes
    files_with_empty_attributes = []
    for filename, file_info in vectorstore_filenames.items():
        attributes = file_info.get("attributes")
        if attributes is None or attributes == {}:
            files_with_empty_attributes.append(filename)

    if files_with_empty_attributes:
        print(f"[bold yellow]Found {len(files_with_empty_attributes)} files with empty attributes:")
        for filename in files_with_empty_attributes[:5]:  # Show first 5
            print(f"  - {filename}")
        if len(files_with_empty_attributes) > 5:
            print(f"  ... and {len(files_with_empty_attributes) - 5} more")

        print("[bold]Reuploading all files to set attributes correctly...")

        # Get all local markdown files
        all_local_files = [f.name for f in upload_dir.glob('*.md')]

        # Reupload all files
        await async_sync_files_with_vectorstore(
            upload_dir=upload_dir,
            files_to_upload=all_local_files,
            vectorstore_id=vectorstore_id,
            vectorstore_filenames=vectorstore_filenames
            )

        print("[bold green]✅ All files reuploaded with proper attributes.")
        return True, vectorstore_filenames
    else:
        print("[bold green]✅ All vectorstore files have proper attributes.")
        return False, vectorstore_filenames

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

            # Get vectorstore files with metadata
            vectorstore_filenames = asyncio.run(get_vectorstore_fileids_and_metadata(
                client,
                str(OPENAI_VECTORSTORE_ID))
                )

            # Check if vectorstore file attributes are empty and reupload if needed
            reupload_performed, vectorstore_filenames = asyncio.run(check_and_reupload_if_attributes_empty(
                client,
                str(OPENAI_VECTORSTORE_ID),
                DATA_DIR,
                vectorstore_filenames
            ))
            if reupload_performed:
                # If reupload was performed, write hash snapshot and return
                utils.write_hashes_for_directory(DATA_DIR)
                return

            # Check for updated files in DATA_DIR
            files_to_upload = utils.get_new_or_modified_files_by_hash(
                directory=DATA_DIR
                )

            # Check for deleted files
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

            # === Vectorstore Syncronization === (will handle both upload and delete)
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
