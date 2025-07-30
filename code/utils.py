import json
import shutil
import hashlib
import datetime
from rich import print
from pathlib import Path

def ensure_dir(dir) -> None:
    path = Path(dir)
    if not path.exists():
        path.mkdir(parents=True)

def is_valid_json(json_string):
    """
    Check if json_string is valid JSON.
    """
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError as e:
        print(f"... Invalid JSON: {e}")
        return False

def backup_dir_with_timestamp(dir_path):
    """
    If dir_path exists, copy it to dir_path_backup_YYYYmmdd.
    """
    path = Path(dir_path)
    if path.exists() and path.is_dir():
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_dir = path.parent / "backups"
        if not backup_dir.exists():
            backup_dir.mkdir(exist_ok=True, parents=True)
        backup_path = backup_dir / f"{path.name}_backup_{timestamp}"
        shutil.copytree(path, backup_path)
        print(f"[bold cyan][BACKUP] {dir_path} -> {backup_path} ... Done.")

def compute_file_hash(file_path):
    """
    Compute SHA256 hash of a file.
    """
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def write_hashes_for_directory(
    directory,
    hash_file="md_hashes.json"
    ):
    """
    Write hashes of all .md files to a JSON file in a "snapshot" folder
    of directory.
    """
    hash_dict = {}
    for file in Path(directory).glob("*.md"):
        hash_dict[file.name] = compute_file_hash(file)

    # Create hash_subfolder
    snapshot_dir =  Path(directory) / "snapshot"
    ensure_dir(snapshot_dir)

    # Write hash_snapshot json
    hash_path = snapshot_dir / hash_file
    with open(hash_path, "w") as f:
        json.dump(hash_dict, f, indent=2)

    print(f"[bold green]Hash snapshot written to {hash_path}")

def load_hash_snapshot(
    directory,
    hash_file="md_hashes.json"
    ) -> dict:
    """
    Load the hash snapshot from a JSON file in the given directory.
    Returns a dict of filename to hash, or an empty dict if not found.
    """
    hash_file_path = Path(directory) / "snapshot" / hash_file
    if hash_file_path.exists():
        with open(hash_file_path, "r") as f:
            return json.load(f)
    return {}

def get_current_hashes(
    directory
    ) -> dict:
    """
    Return a dict of {filename: hash} for all .md files in the given directory.
    """
    hashes = {}
    for file in Path(directory).glob("*.md"):
        hashes[file.name] = compute_file_hash(file)
    return hashes

def get_new_or_modified_files_by_hash(
    directory,
    hash_file="md_hashes.json",
    return_path_objects: bool = False
    ) -> list[str] | list[Path]:
    """
    Detect new or modified .md files by comparing current file hashes with a
    previous snapshot.

    Args:
        directory: Path to directory containing .md files to check
        hash_file: Name of JSON file containing previous hash snapshot
                    (default: "md_hashes.json")
        return_path_objects: If True, return Path objects; if False, return
                    filenames as strings

    Returns:
        List of filenames or Path objects for files that are new or have
        changed since the snapshot

    Note:
        Files are considered "new or modified" if they don't exist in the
        snapshot or have different hashes. The snapshot is expected to be
        in a "snapshot" subdirectory of the target directory.
    """
    old_hashes = load_hash_snapshot(directory, hash_file=hash_file)
    current_hashes = get_current_hashes(directory)

    if return_path_objects:
        return [(Path(directory) / fname).resolve() for fname, h in current_hashes.items() if old_hashes.get(fname) != h]
    else:
        return [fname for fname, h in current_hashes.items() if old_hashes.get(fname) != h]
