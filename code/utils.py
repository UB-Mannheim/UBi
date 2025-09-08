import datetime
import hashlib
import json
import shutil
from urllib.parse import urlparse
import yaml
from pathlib import Path
from rich import print


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
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
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


def write_hashes_for_directory(directory, hash_file="md_hashes.json"):
    """
    Write hashes of all .md files to a JSON file in a "snapshot" folder
    of directory.
    """
    hash_dict = {}
    for file in Path(directory).glob("*.md"):
        hash_dict[file.name] = compute_file_hash(file)

    # Create hash_subfolder
    snapshot_dir = Path(directory) / "snapshot"
    ensure_dir(snapshot_dir)

    # Write hash_snapshot json
    hash_path = snapshot_dir / hash_file
    with open(hash_path, "w") as f:
        json.dump(hash_dict, f, indent=2)

    print(f"[bold green]Hash snapshot written to {hash_path}")


def load_hash_snapshot(directory, hash_file="md_hashes.json") -> dict:
    """
    Load the hash snapshot from a JSON file in the given directory.
    Returns a dict of filename to hash, or an empty dict if not found.
    """
    hash_file_path = Path(directory) / "snapshot" / hash_file
    if hash_file_path.exists():
        with open(hash_file_path, "r") as f:
            return json.load(f)
    return {}


def get_current_hashes(directory) -> dict:
    """
    Return a dict of {filename: hash} for all .md files in the given directory.
    """
    hashes = {}
    for file in Path(directory).glob("*.md"):
        hashes[file.name] = compute_file_hash(file)
    return hashes


def get_new_or_modified_files_by_hash(
    directory, hash_file="md_hashes.json", return_path_objects: bool = False
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
        return [
            (Path(directory) / fname).resolve()
            for fname, h in current_hashes.items()
            if old_hashes.get(fname) != h
        ]
    else:
        return [
            fname
            for fname, h in current_hashes.items()
            if old_hashes.get(fname) != h
        ]


def extract_openai_response_data(response_obj):
    """
    Extract file search chunk and LLM usage data from an OpenAI LLM call.
    """
    # Initialize results containers
    results_data = []
    usage_data = {}

    # Extract Result objects from the file search tool call
    if hasattr(response_obj, "output") and len(response_obj.output) > 0:
        # Find the file search tool call in the output
        for output_item in response_obj.output:
            if (
                hasattr(output_item, "type")
                and output_item.type == "file_search_call"
                and hasattr(output_item, "results")
            ):
                for result in output_item.results:
                    result_info = {
                        "file_id": result.file_id,
                        "filename": result.filename,
                        "score": result.score,
                        "text": result.text,
                    }
                    results_data.append(result_info)
                break

    # Extract ResponseUsage data
    if hasattr(response_obj, "usage"):
        usage_data = {
            "input_tokens": response_obj.usage.input_tokens,
            "output_tokens": response_obj.usage.output_tokens,
            "total_tokens": response_obj.usage.total_tokens,
        }

    return results_data, usage_data


def print_openai_extracted_data(results_data, usage_data):
    """
    Print the extracted data in a formatted way
    """
    print("=" * 40)
    print("RETRIEVED VECTORESTORE DOCS / CHUNKS")
    print("=" * 40)

    # Print Results data
    print(f"\nRESULTS ({len(results_data)} items):")
    print("-" * 40)

    for i, result in enumerate(results_data, 1):
        print(f"[bold]\nResult {i}:")
        print(f"  [bold]File ID[/]: {result['file_id']}")
        print(f"  [bold]Filename[/]: {result['filename']}")
        print(f"  [bold]Score[/]: {result['score']}")
        print(f"  [bold]Text[/]: [green]{result['text']}[/]")
        print()
        print("=" * 40)
        print()

    # Print Usage data
    print("\n[bold]RESPONSE USAGE:")
    print("-" * 40)
    print(f"[bold]Input Tokens[/]: {usage_data.get('input_tokens', 'N/A')}")
    print(f"[bold]Output Tokens[/]: {usage_data.get('output_tokens', 'N/A')}")
    print(f"[bold]Total Tokens[/]: {usage_data.get('total_tokens', 'N/A')}")


def escape_colons_in_yaml_values(line: str) -> str:
    """
    Escape colons in YAML values to prevent parsing errors.
    Only escapes colons that appear after the first colon (key: value).
    """
    if ":" not in line:
        return line

    # Split on first colon to separate key and value
    parts = line.split(":", 1)
    if len(parts) != 2:
        return line

    key, value = parts

    # If value is quoted, don't escape colons inside quotes
    if value.strip().startswith('"') and value.strip().endswith('"'):
        return line
    if value.strip().startswith("'") and value.strip().endswith("'"):
        return line

    # If value is a list (starts with [), don't escape colons inside brackets
    if value.strip().startswith("["):
        return line

    # Escape colons in the value part by wrapping in quotes
    if (
        ":" in value
        and not value.strip().startswith('"')
        and not value.strip().startswith("'")
    ):
        # Wrap the entire value in quotes to escape colons
        escaped_value = f'"{value.strip()}"'
        return f"{key}: {escaped_value}"

    return line


def parse_yaml_header(md_data: str | Path) -> dict:
    """
    Parse the YAML header from either:
    - a markdown file path (str | Path), or
    - a raw markdown string containing a YAML front matter block.

    The function auto-detects whether the input string refers to an existing
    file path; if it does, the file is read. Otherwise, the input is treated
    as raw markdown content. Colons in values are made robust via
    `escape_colons_in_yaml_values`.

    Example YAML Header:
    ---
    title: Datenangebot des Forschungsdatenzentrums (FDZ)
    source_url: https://www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum/datenangebot-des-fdz/
    category: Projekte
    tags: [Forschungsdatenzentrum, Datenbanken, Wirtschafts- und Sozialwissenschaften, Unternehmensdaten, Digitalisierung, Knowledge Graph, Open Data]
    language: de
    ---
    """
    try:
        # Filepath
        if isinstance(md_data, Path):
            with open(md_data, "r", encoding="utf-8") as f:
                content = f.read()

        # Raw string
        elif isinstance(md_data, str):
            raw_str = md_data
            # Check for raw string with YAML header
            if "\n" in raw_str or raw_str.lstrip().startswith("---"):
                content = raw_str
            else:
                try:
                    potential_path = Path(raw_str)
                    if potential_path.exists():
                        with open(potential_path, "r", encoding="utf-8") as f:
                            content = f.read()
                    else:
                        content = raw_str
                except OSError:
                    content = raw_str

        # Check if content starts with YAML header
        if not content.startswith("---"):
            return {}

        # Find the end of YAML header and escape colons in values
        lines = content.split("\n")
        yaml_lines = []
        in_yaml = False

        for line in lines:
            if line.strip() == "---":
                if not in_yaml:
                    in_yaml = True
                else:
                    break
            elif in_yaml:
                processed_line = escape_colons_in_yaml_values(line)
                yaml_lines.append(processed_line)

        if not yaml_lines:
            return {}

        # Join YAML lines and parse
        yaml_content = "\n".join(yaml_lines)
        yaml_data = yaml.safe_load(yaml_content)

        return yaml_data if yaml_data else {}

    except Exception as e:
        print(f"Error parsing YAML header: {e}")
        return {}


def get_markdown_filepath_for_url(url: str, output_dir: str) -> Path:
    """
    Construct a markdown filepath for a URL.
    """
    url_path = urlparse(url).path.split("/")
    filename = "_".join([part for part in url_path if part])
    return Path(output_dir).joinpath(f"{filename}.md")


def delete_filepath(filepath: Path | str) -> None:
    """
    Delete a file locally.
    """
    if not isinstance(filepath, Path):
        filepath = Path(filepath)

    # Delete filepath
    try:
        # Files and symlinks (including symlinks to directories)
        if filepath.is_file() or filepath.is_symlink():
            filepath.unlink(missing_ok=True)
            return
    except Exception as e:
        print(f"[bold red]Failed to delete {filepath}: {e}")
