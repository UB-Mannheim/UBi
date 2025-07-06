from ast import main
import os
import re
import datetime
import shutil
from pathlib import Path
from tqdm import tqdm
from rich import print
from urllib.parse import urlparse
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from config import ENV_PATH, DATA_DIR

# === Load Configuration ===
load_dotenv(ENV_PATH)
TEMP_DIR = f"../data/markdown"

# === Helper Funtions ===
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
        
def write_markdown(
    url,
    content,
    output_dir: str = TEMP_DIR,
    ):
    """
    Write markdown for a URL only if content is new or changed.
    Returns the filename if written/changed, else None.
    """
    # Ensure output_dir exists
    ensure_dir(output_dir)
    
    # Format filename and path
    url_path = urlparse(url).path.split('/')
    filename = '_'.join([part for part in url_path if part])
    file_path = Path(output_dir).joinpath(f"{filename}.md")
    
    # Collect markdown content
    new_content = ''
    for el in content:
        if el.startswith('#'):
            new_content += '\n\n' + el + '\n\n'
        else:
            new_content += el + '\n'

    # Check if file exists and content is unchanged
    if file_path.exists():
        old_content = file_path.read_text(encoding='utf-8')
        if old_content == new_content:
            return None  # No change

    # Write new/changed content
    file_path.write_text(new_content, encoding='utf-8')
    return file_path.name

# === Post-Processing ===
PROMPT_POSTPROCESSING = """You are an expert for preparing markdown documents for Retrieval-Augmented Generation (RAG). 
Perform the following tasks on the provided documents that are sourced from the website of the Universitätsbibliothek Mannheim:
1. Clean the structure, improve headings, embed links using markdown syntax. Do not add content to the markdown page itself. Simply refine it.
2. Add a YAML header (without markdown wrapping!) by using this template:
---
title: title of document
source_url: URL of document
category: one of these categories: [Benutzung, Öffnungszeiten, Standorte, Services, Medien, Projekte]
tags: [a list of precise, descriptive]
language: de, en or other language tags
---
3. Chunk content into semantic blocks of 100–300 words. Remove redundancy and make the file suitable for semantic search or chatbot use.
4. Return the processed markdown file.

# Example Output
---
title: Deutscher Reichsanzeiger und Preußischer Staatsanzeiger
source_url: https://www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum/datenangebot-des-fdz/deutscher-reichsanzeiger-und-preussischer-staatsanzeiger/
category:
tags: [Forschungsdatenzentrum, Datenangebot des FDZ, Deutscher Reichsanziger und Preussischer Staatsanzeiger, Zeitungen]
language: de
---

# First Heading of Markdown Page
The content of the markdown page..."""


def process_markdown_files_with_llm(
    input_dir: str,
    output_dir: str,
    model_name: str = "gpt-4o-mini-2024-07-18",
    only_files: list | None = None
    ):
    """
    Post-process markdown files with LLM and add YAML header.
    If only_files is provided, only process those files.
    """
    # Backup output_dir if it exists
    if output_dir:
        backup_dir_with_timestamp(output_dir)
        
    # Check for updated files
    if only_files is not None:
        input_files = [Path(input_dir)/f for f in only_files if (Path(input_dir)/f).exists()]
    else:
        input_files = list(Path(input_dir).glob('*.md'))

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize the LLM (LangChain wrapper for OpenAI Chat API)
    llm = ChatOpenAI(
        model=model_name,
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
    )

    print(f"[bold][Processing Markdown Files with {model_name}]")
    
    for file_path in tqdm(input_files, desc="LLM Processing"):
        content = file_path.read_text(encoding="utf-8")
        try:
            # LLM interaction
            response = llm.invoke([
                {
                    "role": "system",
                    "content": PROMPT_POSTPROCESSING
                },
                {
                    "role": "user",
                    "content": content
                }
            ])

            # Write to output
            output_file = output_path / file_path.name
            output_file.write_text(response.content, encoding="utf-8")

        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")
            
def process_standorte_contacts(
    data_dir: str = str(DATA_DIR),
    verbose: bool = False
    ):
    """
    Post-processing function that finds standorte markdown files and appends
    related contact information from linked pages.
    Groups files by base name and only appends contacts to the shortest file in each group.
    """
    data_path = Path(data_dir)
    if not data_path.exists():
        print(f"[bold red]Data directory {data_dir} does not exist!")
        return
    
    # Find all markdown files starting with "standorte"
    standorte_files = list(data_path.glob("standorte*.md"))
    
    if not standorte_files:
        print("[bold]No standorte files found for contact processing.")
        return
    
    if verbose:
        print(f"[bold][Processing Standorte Contacts]")
    
    # Group files by their base name (e.g., "bb-a3", "bb-a5" ...)
    file_groups = {}
    for file_path in standorte_files:
        # Extract base name by removing "standorte_" prefix and suffixes after "_"
        stem = file_path.stem
        if stem.startswith("standorte_"):
            base_name = stem[10:] # Remove "standorte_" prefix
            # Remove suffixes after "_" (e.g., "_testverfahren-psychologie")
            if "_" in base_name:
                base_name = base_name.split("_")[0]
            if base_name not in file_groups:
                file_groups[base_name] = []
            file_groups[base_name].append(file_path)
    
    processed_count = 0
    processed_contacts = set()
    
    # Process each group - find the shortest file and append contacts to it
    for base_name, group_files in file_groups.items():
        if not group_files:
            continue
            
        # Find the shortest file in this group
        shortest_file = min(group_files, key=lambda f: len(f.stem))
        
        try:
            content = shortest_file.read_text(encoding="utf-8")
            
            # Check for "Ansprechpersonen" in markdown link format
            contact_link_pattern = r'\[.*?Ansprechpersonen.*?\]\((https://www\.bib\.uni-mannheim\.de/[^)]+)\)'
            matches = re.findall(contact_link_pattern, content, re.IGNORECASE)
            
            if not matches and verbose:
                print(f"[bold yellow]No 'Ansprechpersonen' found in {shortest_file.name}")
                continue
            
            if verbose:
                print(f"[bold]Found {len(matches)} contact links in {shortest_file.name}")
            
            for contact_url in matches:
                # Convert URL to filename
                url_path = contact_url.replace('https://www.bib.uni-mannheim.de/', '')
                contact_filename = url_path.replace('/', '_').rstrip('_') + '.md'
                contact_file_path = data_path / contact_filename
                
                # Skip if this contact file has already been processed
                if contact_filename in processed_contacts:
                    if verbose:
                        print(f"[bold yellow]Skipping {contact_filename} - already processed")
                        continue
                
                if contact_file_path.exists():
                    if verbose:
                        print(f"[bold]Appending content from {contact_filename}")
                    
                    # Read contact content
                    contact_content = contact_file_path.read_text(encoding="utf-8")
                    
                    # Extract content after YAML header
                    lines = contact_content.split('\n')
                    content_start = 0
                    yaml_end_count = 0
                    
                    for i, line in enumerate(lines):
                        if line.strip() == '---':
                            yaml_end_count += 1
                            if yaml_end_count == 2:
                                content_start = i + 1
                                break
                    
                    # Get content after YAML header and skip first # heading
                    contact_content_body = '\n'.join(lines[content_start + 2:]).strip()
                    
                    if contact_content_body:
                        # Adjust heading hierarchy in contact content (demote by one level)
                        adjusted_content = contact_content_body
                        adjusted_content = re.sub(
                            r'^### ',
                            '###### ',
                            adjusted_content,
                            flags=re.MULTILINE
                            )
                        adjusted_content = re.sub(
                            r'^## ',
                            '##### ',
                            adjusted_content,
                            flags=re.MULTILINE
                            )
                        # Append contact content to original file
                        separator = "\n\n### Weitere Ansprechpersonen\n\n"
                        new_content = content + separator + adjusted_content
                        
                        # Write back to file
                        shortest_file.write_text(new_content, encoding="utf-8")
                        processed_count += 1
                        print(f"[bold green]Appended contact information to {shortest_file.name}")
                        
                        # Remove the contact file after successful merge
                        try:
                            contact_file_path.unlink()
                            processed_contacts.add(contact_filename) # Mark as processed
                            print(f"[bold blue]Removed {contact_filename} after successful merge.")
                        except Exception as e:
                            print(f"[bold yellow]Warning: Could not remove {contact_filename}: {e}")
                    else:
                        if verbose:
                            print(f"[bold red]Error: No content found in {contact_filename}")
                else:
                    if verbose:
                        print(f"[bold red]Contact file not found: {contact_filename}")
                    
        except Exception as e:
            print(f"[bold red]Error processing {shortest_file.name}: {e}")
    
    print(f"[bold green]Done. Processed {processed_count} contact files.")
