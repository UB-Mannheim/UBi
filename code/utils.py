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
        
def backup_dir_with_timestamp(dir_path):
    """
    If dir_path exists, copy it to dir_path_backup_YYYYmmdd.
    """
    path = Path(dir_path)
    if path.exists() and path.is_dir():
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = path.parent / f"{path.name}_backup_{timestamp}"
        shutil.copytree(path, backup_path)
        print(f"[bold][BACKUP] {dir_path} -> {backup_path}\nDone.")
        
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
    Write hashes of all .md files in directory to a JSON file.
    """
    hash_dict = {}
    for file in Path(directory).glob("*.md"):
        hash_dict[file.name] = compute_file_hash(file)
    hash_path = Path(directory) / hash_file
    with open(hash_path, "w") as f:
        json.dump(hash_dict, f, indent=2)
    print(f"[bold green]Hash snapshot written to {hash_path}")
    
def data_dir_has_updates(
    data_dir: Path,
    hash_file_name: str = "md_hashes.json"
    ) -> bool:
    """
    Check if any .md file in data_dir has a different hash than in 
    hash_file_name, or if there are new/deleted files. Returns True 
    if updated, added, or deleted.
    """
    hash_file_path = data_dir / hash_file_name
    
    if not hash_file_path.exists():
        return True
    
    # Get old hashes from json
    with open(hash_file_path, "r") as f:
        old_hashes = json.load(f)
        
    # Current hashes
    current_hashes = {}
    for file in data_dir.glob("*.md"):
        current_hashes[file.name] = compute_file_hash(file)
        
    # Check for new or deleted files
    if set(current_hashes.keys()) != set(old_hashes.keys()):
        return True
    
    # Check for changed hashes
    for fname, h in current_hashes.items():
        if old_hashes.get(fname) != h:
            return True
        
    return False

def load_hash_snapshot(
    directory,
    hash_file="md_hashes.json"
    ) -> dict:
    """
    Load the hash snapshot from a JSON file in the given directory.
    Returns a dict of filename to hash, or an empty dict if not found.
    """
    hash_file_path = Path(directory) / hash_file
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