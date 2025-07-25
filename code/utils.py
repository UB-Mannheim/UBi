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

def init_ui_config_from_template(config_file="public/ui_config.json"):
    """
    Initialize ui_config.json from template if it doesn't exist.
    
    Args:
        config_file (str): Path to the config file
    """
    config_path = Path(config_file)
    template_path = Path("./ui_config.template.json")
    # If config doesn't exist but template does, copy from template
    if not config_path.exists() and template_path.exists():
        with open(template_path, 'r', encoding='utf-8') as f:
            template_data = json.load(f)
        
        # Ensure directory exists
        ensure_dir(config_path.parent)
        
        # Write config file
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(template_data, f, indent=2, ensure_ascii=False)
        
        print(f"[green]Initialized {config_file} from template[/green]")
        return template_data
    
    return None
        
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
        
def update_ui_config(data_updates=None, config_file="public/ui_config.json"):
    """
    Update or create the public/ui_config.json file with new data.
    
    Args:
        data_updates (dict): Dictionary of data to update/add to the JSON file
    """
    data_file = Path(config_file)
    public_dir = data_file.parent
    ensure_dir(public_dir)
    # Load existing data or create new with default config
    if data_file.exists():
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {}
    else:
        data = {}
    
    # Update with new data if provided
    if data_updates:
        data.update(data_updates)
    
    # Write back to file
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    return data


def get_ui_config(config_file="public/ui_config.json"):
    """
    Read the public/ui_config.json file.
    
    Returns:
        dict: Data from the JSON file, or empty dict if file doesn't exist
    """
    data_file = Path(config_file)
    
    if data_file.exists():
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}


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
    
    # Update public ui_config.json with last_updated timestamp
    update_ui_config({"last_updated": datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})
    
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
    # Load hash snapshot
    if hash_file_path.exists():
        # Set last_updated in ui_config.json if not set
        ui_config = get_ui_config()
        if ui_config.get("last_updated") is None:
            last_modified_timestamp = hash_file_path.stat().st_mtime
            last_modified_datetime = datetime.datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M')
            update_ui_config({"last_updated": last_modified_datetime})
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
    hash_file="md_hashes.json"
    ) -> list[str]:
    """
    Compare current file hashes for directory with an older hash snapshot
    defined in hash_file and return a list with all filenames that are
    either new or updated.
    """
    old_hashes = load_hash_snapshot(directory, hash_file=hash_file)
    current_hashes = get_current_hashes(directory)
    return [fname for fname, h in current_hashes.items() if old_hashes.get(fname) != h]
