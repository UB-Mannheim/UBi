import asyncio
import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv, set_key
from openai import OpenAI
from tqdm import tqdm

import utils
from config import DATA_DIR, ENV_PATH


# === OpenAI Vectorstore Functions ===
def create_openAI_vectorstore():
    """
    Create an OpenAI vectorstore and write its ID to .env.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
                vector_store_id=str(vectorstore_id), limit=100, after=after
            )
        else:
            response = client.vector_stores.files.list(
                vector_store_id=str(vectorstore_id), limit=100
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
    files_to_delete: set,
):
    """
    Async delete files from vectorstore and OpenAI storage, with progress bar.
    """
    pbar_del = tqdm(
        total=len(files_to_delete), desc="Deleting files", leave=False
    )

    async def delete_file(filename):
        remote_file_id = vectorstore_filenames[filename]["file_id"]
        try:
            await asyncio.to_thread(
                client.vector_stores.files.delete,
                vector_store_id=str(vectorstore_id),
                file_id=remote_file_id,
            )
            utils.print_info(f"[bold]Deleted {filename} from vectorstore.")
            await asyncio.to_thread(
                client.files.delete, file_id=remote_file_id
            )
        except Exception as e:
            utils.print_err(
                f"[bold]Error deleting {filename} from vectorstore/OpenAI storage: {e}"
            )
        pbar_del.update(1)

    await asyncio.gather(
        *(delete_file(filename) for filename in files_to_delete)
    )
    pbar_del.close()


async def async_upload_files_to_vectorstore(
    client: OpenAI,
    vectorstore_id: str,
    vectorstore_filenames: dict,
    md_files: list,
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
                await asyncio.to_thread(
                    client.vector_stores.files.delete,
                    vector_store_id=str(vectorstore_id),
                    file_id=vectorstore_file_id,
                )
                # Delete file from vectorstore
                utils.print_info(f"[bold]Deleting old {filename} from vectorstore ...")
                await asyncio.to_thread(
                    client.files.delete, file_id=vectorstore_file_id
                )
            except Exception as e:
                utils.print_err(f"[bold]Error deleting {filename} from vectorstore: {e}")

        # File Upload
        try:
            # Parse YAML header for attributes
            yaml_data = utils.parse_yaml_header(md_file) or {}

            # Persist local filename in vectorstore attributes for health checks
            yaml_data["local_filename"] = filename

            # Upload the updated local file to vectorstore
            utils.print_info(f"[bold]Uploading updated {filename} to vectorstore ...")
            with open(md_file, "rb") as f:
                uploaded_file = await asyncio.to_thread(
                    client.files.create, file=f, purpose="user_data"
                )

            # Link uploaded file to vectorstore
            await asyncio.to_thread(
                client.vector_stores.files.create,
                vector_store_id=str(vectorstore_id),
                file_id=uploaded_file.id,
                attributes=yaml_data,
            )
        except Exception as e:
            utils.print_err(f"Error uploading {filename}: {e}")
        pbar_up.update(1)

    await asyncio.gather(*(upload_file(md_file) for md_file in md_files))
    pbar_up.close()


async def get_vectorstore_fileids_and_metadata(
    client: OpenAI, vectorstore_id: str
) -> dict[str, dict[str, object]]:
    """
    Async helper to retrieve a dict mapping filename to a dict containing
    file_id and attributes for all files in the vectorstore.

    If missing/corrupted files are found (status_code == 404), they get flag
    with the prefix "missing:" in "filename" as well as file_missing == True.
    """
    vector_store_files = await asyncio.to_thread(
        get_all_vectorstore_files, client, vectorstore_id
    )
    if vector_store_files:

        async def retrieve_file(f):
            missing_file = False
            error = None
            attributes = f.attributes or {}
            original_filename = attributes.get("local_filename")
            try:
                file_obj = await asyncio.to_thread(client.files.retrieve, f.id)
                filename = file_obj.filename
            except Exception as e:
                if getattr(e, "status_code", None) == 404:
                    filename = f"missing:{f.id}"
                    missing_file = True
                    error = str(e)
                    utils.print_err(
                        f"[bold yellow]Vectorstore file {f.id} is missing in OpenAI Files API (404). Marked for unlink."
                    )
                else:
                    raise

            payload = {
                "file_id": f.id,
                "attributes": attributes,
                "status": f.status,
                "file_missing": missing_file,
            }
            if original_filename:
                payload["original_filename"] = original_filename
            if error:
                payload["error"] = error

            return (
                filename,
                payload,
            )

        results = await asyncio.gather(
            *(retrieve_file(f) for f in vector_store_files)
        )
        return dict(results)
    else:
        return {}


def list_vectorstore_files(as_json: bool = False) -> None:
    """
    Debug helper: list all files currently in the OpenAI vectorstore
    (filename + file_id). Intended to be invoked from the CLI.
    """
    from rich.console import Console
    from rich.table import Table

    load_dotenv(str(ENV_PATH))
    vectorstore_id = os.getenv("OPENAI_VECTORSTORE_ID")
    if not vectorstore_id:
        utils.print_err("[bold]No OPENAI_VECTORSTORE_ID found in .env")
        return

    # Retrieve files in vectorestore
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore_filenames = asyncio.run(
        get_vectorstore_fileids_and_metadata(client, str(vectorstore_id))
    )

    # Print as JSON
    if as_json:
        import json

        payload = {
            (idx + 1): {
                "vectorstore_filename": filename,
                "vectorstore_fileid": info.get("file_id"),
                "vectorstore_file_status": info.get("status"),
                "original_filename": info.get("original_filename"),
                "missing": str(info.get("file_missing")),
            }
            for idx, (filename, info) in enumerate(vectorstore_filenames.items())
        }
        print(json.dumps(payload, indent=2))
        return

    # Print as rich CLI table
    table = Table(
        title=f"Vectorstore {vectorstore_id} ({len(vectorstore_filenames)} files)"
    )
    table.add_column("vectorstore_filename", overflow="fold")
    table.add_column("vectorstore_fileid", overflow="fold")
    table.add_column("vectorstore_file_status", overflow="fold")
    table.add_column("original_filename", overflow="fold")
    table.add_column("missing_file?", overflow="fold")
    for filename in sorted(vectorstore_filenames):
        table.add_row(
            filename,
            vectorstore_filenames[filename].get("file_id"),
            vectorstore_filenames[filename].get("status"),
            vectorstore_filenames[filename].get("original_filename"),
            str(vectorstore_filenames[filename].get("file_missing")),
        )
    Console().print(table)


async def async_sync_files_with_vectorstore(
    upload_dir: Path,
    files_to_upload: list[str],
    files_to_delete: set | None,
    vectorstore_id: str,
    vectorstore_filenames: dict = {},
):
    """
    Async upload markdown files to an existing OpenAI vectorstore.
    Also, delete files from the vectorstore that are not in files_to_upload.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    md_files = [Path(f"{upload_dir}/{file}") for file in files_to_upload]

    # Only fetch vectorstore files if not provided (empty dict)
    if not vectorstore_filenames:
        utils.print_info("[bold]Retrieving filenames from vectorstore ...")
        vectorstore_filenames = await get_vectorstore_fileids_and_metadata(
            client, vectorstore_id
        )

    # Delete files
    if files_to_delete:
        await async_delete_files_from_vectorstore(
            client, vectorstore_id, vectorstore_filenames, files_to_delete
        )

    # Upload new or updated files to vectorstore
    utils.print_info(f"🔄 Uploading {len(md_files)} files to OpenAI vectorstore ...")
    await async_upload_files_to_vectorstore(
        client, vectorstore_id, vectorstore_filenames, md_files
    )
    utils.print_info("✅ Finished.")


async def check_and_reupload_if_attributes_empty(
    client: OpenAI,
    vectorstore_id: str,
    upload_dir: Path,
    vectorstore_filenames: dict | None = None,
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
    utils.print_info("[bold]Checking vectorstore file attributes...")

    # Get all files from vectorstore with their metadata if not provided
    if vectorstore_filenames is None:
        vectorstore_filenames = await get_vectorstore_fileids_and_metadata(
            client, vectorstore_id
        )

    if not vectorstore_filenames:
        utils.print_err("[bold]No files found in vectorstore. Nothing to check.")
        return False, {}

    # Check if any files have empty attributes
    files_with_empty_attributes = []
    for filename, file_info in vectorstore_filenames.items():
        attributes = file_info.get("attributes")
        if attributes is None or attributes == {}:
            files_with_empty_attributes.append(filename)

    if files_with_empty_attributes:
        utils.print_info(
            f"[bold yellow]Found {len(files_with_empty_attributes)} files with empty attributes:"
        )
        for filename in files_with_empty_attributes[:5]:  # Show first 5
            utils.print_info(f"  - {filename}")
        if len(files_with_empty_attributes) > 5:
            utils.print_info(f"  ... and {len(files_with_empty_attributes) - 5} more")

        utils.print_info("[bold]Reuploading all files to set attributes correctly...")

        # Get all local markdown files
        all_local_files = [f.name for f in upload_dir.glob("*.md")]

        # Reupload all files
        await async_sync_files_with_vectorstore(
            upload_dir=upload_dir,
            files_to_upload=all_local_files,
            files_to_delete=None,
            vectorstore_id=vectorstore_id,
            vectorstore_filenames=vectorstore_filenames,
        )

        utils.print_info("[bold green]✅ All files reuploaded with proper attributes.")
        return True, vectorstore_filenames
    else:
        utils.print_info("[bold green]✅ All vectorstore files have proper attributes.")
        return False, vectorstore_filenames


def collect_all_files_to_upload(
    vectorstore_filenames: dict[str, dict],
    all_local_files_set: set,
    files_to_upload: list[str] | set[str],
) -> list:
    """
    Collect all files that should be uploaded or reuploaded to the vectorstore.

    The function checks if the vectorstore returned files with an attribute
    "file_missing" == True. Those files result in a status 404 when called
    by their file_id and or most likely corrupted, meaning the vectorstore
    contains a metadata entry for this file_id but no actually .md file.

    The function collects those corrupted filenames, checks if they exist
    in all_local_files_set (a set of all currently available .mds in DATA_DIR)
    and when they do, adds them to files_to_upload.
    """
    healthy_vectorstore_filenames = {
        name
        for name, info in vectorstore_filenames.items()
        if not info.get("file_missing")
    }
    corrupted_local_files_to_reupload = {
        info["original_filename"]
        for info in vectorstore_filenames.values()
        if info.get("file_missing")
        and info.get("original_filename")
        and info["original_filename"] in all_local_files_set
        and info["original_filename"] not in healthy_vectorstore_filenames
    }
    if corrupted_local_files_to_reupload:
        utils.print_info(
            f"[bold yellow]Reuploading {len(corrupted_local_files_to_reupload)} "
            "locally-identified corrupted files ..."
        )
        files_to_upload = sorted(
            set(files_to_upload) | corrupted_local_files_to_reupload
        )
    return files_to_upload


def initialize_vectorstore():
    """
    Create or load an OpenAI vectorstore and upload only files from
    DATA_DIR that were updated (hash comparison with md_hashes.json).
    """
    # Load config from .env
    load_dotenv(str(ENV_PATH))
    USE_OPENAI_VECTORSTORE = (
        True if os.getenv("USE_OPENAI_VECTORSTORE") == "True" else False
    )
    if not USE_OPENAI_VECTORSTORE:
        utils.print_err("[bold]Aborting: OpenAI vectorstore is disabled in .env")
        return
    OPENAI_VECTORSTORE_ID = os.getenv("OPENAI_VECTORSTORE_ID")

    try:
        if not OPENAI_VECTORSTORE_ID:
            # Create a new OpenAI vectorstore
            utils.print_info(
                "[bold]No OPENAI_VECTORSTORE_ID found. Creating new OpenAI vectorstore..."
            )
            vectorstore = create_openAI_vectorstore()
            utils.print_info(f"[bold]Created new vectorstore with ID: {vectorstore.id}")

            # Reload .env and OPENAI_VECTORSTORE_ID after creation
            load_dotenv(str(ENV_PATH))
            OPENAI_VECTORSTORE_ID = os.getenv("OPENAI_VECTORSTORE_ID")

            # Get all files from DATA_DIR for upload
            files_to_upload = [f.name for f in DATA_DIR.glob("*.md")]
            files_to_delete = set()
            vectorstore_filenames = {}
        else:
            utils.print_info(f"[bold]Using OpenAI vectorstore: {OPENAI_VECTORSTORE_ID}")
            utils.print_info("[bold]Syncing local files to vectorstore ...")

            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            # Get vectorstore files with metadata
            vectorstore_filenames = asyncio.run(
                get_vectorstore_fileids_and_metadata(
                    client, str(OPENAI_VECTORSTORE_ID)
                )
            )

            # Check if vectorstore file attributes are empty and reupload if needed
            reupload_performed, vectorstore_filenames = asyncio.run(
                check_and_reupload_if_attributes_empty(
                    client,
                    str(OPENAI_VECTORSTORE_ID),
                    DATA_DIR,
                    vectorstore_filenames,
                )
            )
            if reupload_performed:
                # If reupload was performed, write hash snapshot and return
                utils.write_hashes_for_directory(DATA_DIR)
                utils.write_dynamic_ui_var(
                    "last_updated", date.today().strftime("%Y-%m-%d")
                )
                return

            # === File Collection for Vectorstore Synchronization ===
            # 1. Check for updated files in DATA_DIR by hash comparison
            files_to_upload = utils.get_new_or_modified_files_by_hash(
                directory=DATA_DIR
            )

            # 2. Check for locally deleted files that need to be cleaned from the vs
            vectorstore_filenames_set = set(vectorstore_filenames.keys())
            all_local_files_set = set([f.name for f in DATA_DIR.glob("*.md")])
            files_to_delete = vectorstore_filenames_set - all_local_files_set

            # 3. Check for missing files in the vs that ne to be reuploaded
            missing_vectorstore_files = all_local_files_set - vectorstore_filenames_set
            files_to_upload = set(files_to_upload) | missing_vectorstore_files

            # 4. Collect all files for upload (updated, new and corrupted files)
            files_to_upload = collect_all_files_to_upload(
                vectorstore_filenames=vectorstore_filenames,
                all_local_files_set=all_local_files_set,
                files_to_upload=files_to_upload
            )

            utils.print_info(
                f"[bold]{len(vectorstore_filenames)} files in vectorstore: {OPENAI_VECTORSTORE_ID}"
            )

        # Only skip if there are truly no changes (no upload, no delete)
        if files_to_upload or files_to_delete:
            if files_to_upload:
                utils.print_info(
                    f"[bold]Uploading {len(files_to_upload)} changed/new files to vectorstore ..."
                )
            if files_to_delete:
                utils.print_info(
                    f"[bold]Deleting {len(files_to_delete)} files from vectorstore ..."
                )

            # === Vectorstore Syncronization === (will handle both upload and delete)
            asyncio.run(
                async_sync_files_with_vectorstore(
                    upload_dir=DATA_DIR,
                    files_to_upload=files_to_upload,
                    files_to_delete=files_to_delete,
                    vectorstore_id=str(OPENAI_VECTORSTORE_ID),
                    vectorstore_filenames=vectorstore_filenames,
                )
            )

            # Write hash snapshot
            utils.write_hashes_for_directory(DATA_DIR)
            utils.write_dynamic_ui_var(
                "last_updated", date.today().strftime("%Y-%m-%d")
            )
        else:
            utils.print_info(
                "[bold green]No changes detected in DATA_DIR since last sync. Skipping vectorstore upload."
            )
            # If no changes, update the timestamp to the last data check time
            try:
                # Corrected path to the hash file
                utils.print_info("[bold]Updating last_updated timestamp from md_hashes.json ...")
                snapshot_path = Path(DATA_DIR) / "snapshot" / "md_hashes.json"
                if snapshot_path.exists():
                    last_mod_time = date.fromtimestamp(snapshot_path.stat().st_mtime)
                    utils.write_dynamic_ui_var("last_updated", last_mod_time.strftime("%Y-%m-%d"))
            except Exception as e:
                utils.print_err(f"Warning: Could not update timestamp from md_hashes.json: {e}")

    except Exception as e:
        utils.print_err(f"Error: {e}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="OpenAI vectorstore utilities")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_list = subparsers.add_parser(
        "list-files",
        help="List all files currently in the vectorstore (debug)",
    )
    p_list.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()
    if args.command == "list-files":
        list_vectorstore_files(as_json=args.json)
