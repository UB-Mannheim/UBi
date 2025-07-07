import os
import re
import datetime
import shutil
import backoff
import asyncio
import time
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

# === Helper Functions ===
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

def extract_content_after_yaml_header(content: str) -> str:
    """
    Extract content after YAML header (after second '---').
    
    Args:
        content: Markdown content with YAML header
        
    Returns:
        Content after YAML header
    """
    lines = content.split('\n')
    content_start = 0
    yaml_end_count = 0
    
    for i, line in enumerate(lines):
        if line.strip() == '---':
            yaml_end_count += 1
            if yaml_end_count == 2:
                content_start = i + 1
                break
    
    return '\n'.join(lines[content_start:]).strip()

def adjust_heading_hierarchy(content: str, demote_levels: int = 1) -> str:
    """
    Adjust heading hierarchy by demoting headings by specified number of levels.
    
    Args:
        content: Markdown content
        demote_levels: Number of levels to demote (default: 1)
        
    Returns:
        Content with adjusted heading hierarchy
    """
    def demote_heading(match):
        """Add demote_levels number of # to the heading"""
        hashes = match.group(1)
        new_hashes = '#' * (len(hashes) + demote_levels)
        return f'{new_hashes} '
    
    # Use a single regex to match all headings and demote them properly
    return re.sub(r'^(#{1,6}) ', demote_heading, content, flags=re.MULTILINE)

def url_to_filename(url: str) -> str:
    """
    Convert URL to filename by removing domain and replacing slashes 
    with underscores.
    """
    url_path = url.replace('https://www.bib.uni-mannheim.de/', '')
    return url_path.replace('/', '_').rstrip('_') + '.md'

def safe_remove_file(file_path: Path, processed_files: set | None = None) -> bool:
    """
    Safely remove a file and optionally track it in a set.
    
    Args:
        file_path: Path to file to remove
        processed_files: Optional set to track processed files
        
    Returns:
        True if successful, False otherwise
    """
    try:
        file_path.unlink()
        if processed_files is not None:
            processed_files.add(file_path.name)
        print(f"[bold blue]Removed {file_path.name} after successful merge.")
        return True
    except Exception as e:
        print(f"[bold yellow]Warning: Could not remove {file_path.name}: {e}")
        return False

def create_llm_messages(system_prompt: str, user_content: str) -> list:
    """
    Create standardized LLM messages for system and user content.
    
    Args:
        system_prompt: System prompt content
        user_content: User content
        
    Returns:
        List of message dictionaries
    """
    return [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_content
        }
    ]

def find_section_position(content_lines: list, section_heading: str) -> int:
    """
    Find the position of a section heading in content lines.
    
    Args:
        content_lines: List of content lines
        section_heading: Section heading to find
        
    Returns:
        Index of section heading, -1 if not found
    """
    for i, line in enumerate(content_lines):
        if line.strip() == section_heading:
            return i
    return -1

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
tags: [a list of precise, descriptive keywords]
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

@backoff.on_exception(backoff.expo, Exception, max_tries=3)
async def process_single_file_async(llm, file_path, output_path, prompt):
    """
    Process a single markdown file with retry logic.
    """
    content = file_path.read_text(encoding="utf-8")
    
    # LLM interaction
    messages = create_llm_messages(prompt, content)
    response = await llm.ainvoke(messages)

    # Write to output
    output_file = output_path / file_path.name
    output_file.write_text(response.content, encoding="utf-8")
    return file_path.name

def process_markdown_files_with_llm(
    input_dir: str,
    output_dir: str,
    model_name: str = "gpt-4o-mini-2024-07-18",
    only_files: list | None = None,
    max_concurrent: int = 3,
    delay_between_requests: float = 0.5
    ):
    """
    Post-process markdown files with LLM and add YAML header.
    If only_files is provided, only process those files.
    
    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to write processed files
        model_name: OpenAI model to use
        only_files: List of specific files to process
        max_concurrent: Maximum concurrent API requests
        delay_between_requests: Delay between requests in seconds
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

    # Initialize the LLM
    llm = ChatOpenAI(
        model=model_name,
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        max_retries=2
    )

    print(f"[bold][Processing Markdown Files with {model_name}]")
    
    # For single file or small batches, use sequential processing to avoid async overhead
    if len(input_files) <= 2:
        process_markdown_files_sequential(llm, input_files, output_path)
        return
    
    async def process_files_async():
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def process_with_semaphore(file_path):
            async with semaphore:
                try:
                    result = await process_single_file_async(
                        llm,
                        file_path,
                        output_path,
                        PROMPT_POSTPROCESSING
                    )
                    # Add delay between requests to respect rate limits
                    if delay_between_requests > 0:
                        await asyncio.sleep(delay_between_requests)
                    return result
                except Exception as e:
                    print(f"❌ Error processing {file_path.name}: {e}")
                    return None
        
        # Create tasks for all files
        tasks = [process_with_semaphore(file_path) for file_path in input_files]
        
        # Process with progress bar
        completed = 0
        for coro in tqdm(
            asyncio.as_completed(tasks),
            total=len(tasks),
            desc="LLM Processing"
            ):
            result = await coro
            if result:
                completed += 1
        
        return completed
    
    # Run the async processing
    try:
        completed_count = asyncio.run(process_files_async())
        print(f"[bold green]Successfully processed {completed_count}/{len(input_files)} files")
    except Exception as e:
        print(f"[bold red]Error during batch processing: {e}")
        # Fallback to sequential processing
        print("[bold yellow]Falling back to sequential processing...")
        process_markdown_files_sequential(llm, input_files, output_path)

def process_markdown_files_sequential(llm, input_files, output_path):
    """Fallback sequential processing if async fails."""
    for file_path in tqdm(input_files, desc="LLM Processing"):
        try:
            content = file_path.read_text(encoding="utf-8")
            
            # LLM interaction
            messages = create_llm_messages(PROMPT_POSTPROCESSING, content)
            response = llm.invoke(messages)

            # Write to output
            output_file = output_path / file_path.name
            output_file.write_text(response.content, encoding="utf-8")
            
            # Add delay between requests (reduced for better performance)
            time.sleep(0.2)

        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")

def process_standorte(
    data_path: Path,
    verbose: bool = False
    ):
    """
    Post-processing function that finds standorte markdown files and appends
    related contact information from linked pages.
    Groups files by base name and only appends contacts to the shortest file in each group.
    """
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
                contact_filename = url_to_filename(contact_url)
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
                    
                    # Extract content after YAML header and skip first # heading
                    contact_content_body = extract_content_after_yaml_header(
                        content=contact_content
                        )
                    if contact_content_body:
                        # Skip the first heading (usually # heading)
                        lines = contact_content_body.split('\n')
                        if lines and lines[0].startswith('# '):
                            contact_content_body = '\n'.join(lines[2:]).strip()
                    
                    if contact_content_body:
                        # Adjust heading hierarchy in contact content (demote by two levels)
                        adjusted_content = adjust_heading_hierarchy(
                            content=contact_content_body,
                            demote_levels=2
                            )
                        
                        # Append contact content to original file
                        separator = "\n\n### Weitere Ansprechpersonen\n\n"
                        new_content = content + separator + adjusted_content
                        
                        # Write back to file
                        shortest_file.write_text(new_content, encoding="utf-8")
                        processed_count += 1
                        print(f"[bold green]Appended contact information to {shortest_file.name}")
                        
                        # Remove the contact file after successful merge
                        safe_remove_file(contact_file_path, processed_contacts)
                    else:
                        if verbose:
                            print(f"[bold red]Error: No content found in {contact_filename}")
                else:
                    if verbose:
                        print(f"[bold red]Contact file not found: {contact_filename}")
                    
        except Exception as e:
            print(f"[bold red]Error processing {shortest_file.name}: {e}")
    
    print(f"[bold green]Done. Processed {processed_count} contact files.")
    
def process_direktion(
    data_path: Path,
    verbose: bool = False
    ):
    """
    Augemnt "ihre-ub_ansprechpersonen_direktion.md"
    """
    # Find "direktion" markdown
    direktion_md = list(data_path.glob("*direktion.md"))
    if not direktion_md:
        print(f"[bold ]No '*direktion.md' for processing.")
        return
    
    try:
        md_data = direktion_md[0].read_text(encoding='utf-8')
                
        # Augment the # heading    
        heading_match = re.search(r"^# .*$", md_data, re.MULTILINE)
        if heading_match:
            old_string = heading_match.group(0)
            new_string = "# Direktion und Leitung der Universitätsbibliothek Mannheim"
            md_data = re.sub(re.escape(old_string), new_string, md_data)
        
        # Augment the profile description
        profile_match = re.search(
            r"^Direktorin der Universitätsbibliothek\s*$",
            md_data,
            re.MULTILINE
            )
        if profile_match:
            old_string = profile_match.group(0)
            new_string = "Direktorin und Leiterin der Universitätsbibliothek"
            md_data = re.sub(re.escape(old_string), new_string, md_data)
        
        # Write augmented file
        direktion_md[0].write_text(md_data, encoding='utf-8')
        
    except Exception as e:
        print(f"[bold red]Error processing Direktionen files: {e}")
    
    print(f"[bold green]Done. Augmented 'Direktion' markdown page.")
    
def process_semesterapparat(
    data_path: Path,
    verbose: bool = False
    ):
    """
    Post-processing function that finds the semesterapparat application file 
    and appends its content to the parent semesterapparat file.
    """
    # Find the parent semesterapparat file
    semesterapparat_files = list(data_path.glob("*semesterapparat.md"))
    semesterapparat_files = [f for f in semesterapparat_files if "antrag" not in f.name]
    
    if not semesterapparat_files:
        print("[bold]No parent semesterapparat file found for processing.")
        return
    
    parent_file = semesterapparat_files[0]
    
    # Find the application file
    antrag_files = list(data_path.glob("*semesterapparat_antrag*.md"))
    
    if not antrag_files:
        print("[bold]No semesterapparat application file found for processing.")
        return
    
    antrag_file = antrag_files[0]
    
    if verbose:
        print(f"[bold][Processing Semesterapparat Application]")
        print(f"[bold]Parent file: {parent_file.name}")
        print(f"[bold]Application file: {antrag_file.name}")
    
    try:
        # Read parent file content
        parent_content = parent_file.read_text(encoding="utf-8")
        parent_lines = parent_content.split('\n')
        
        # Find the "## Kontakt" section
        kontakt_start = find_section_position(parent_lines, "## Kontakt")
        
        # Read application file content
        antrag_content = antrag_file.read_text(encoding="utf-8")
        
        # Extract content after YAML header from application file
        antrag_content_body = extract_content_after_yaml_header(antrag_content)
        
        if antrag_content_body:
            # Adjust heading hierarchy in application content (demote by one level)
            adjusted_content = adjust_heading_hierarchy(
                content=antrag_content_body,
                demote_levels=1
                )
            
            # Construct new content
            separator = "\n## Antrag auf Einrichtung eines Semesterapparats\n\n"
            
            if kontakt_start >= 0:
                # If Kontakt section exists, insert before it
                before_kontakt = '\n'.join(parent_lines[:kontakt_start])
                kontakt_section = '\n'.join(parent_lines[kontakt_start:])
                new_content = before_kontakt + separator + adjusted_content + "\n\n" + kontakt_section
            else:
                # If no Kontakt section, just append to the end
                new_content = parent_content + separator + adjusted_content
            
            # Write back to parent file
            parent_file.write_text(new_content, encoding="utf-8")
            print(f"[bold green]Appended application information to {parent_file.name}")
            
            # Remove the application file after successful merge
            safe_remove_file(antrag_file)
        else:
            if verbose:
                print(f"[bold red]Error: No content found in {antrag_file.name}")
                
    except Exception as e:
        print(f"[bold red]Error processing semesterapparat files: {e}")
    
    print(f"[bold green]Done. Processed semesterapparat application file.")

def process_shibboleth(
    data_path: Path,
    verbose: bool = False
    ):
    """
    Appends the content from the shibboleth markdown file to the parent 
    e-books-e-journals-und-datenbanken.md file, placing the parent's Kontakt section at the end.
    """
    # Find the parent file
    parent_files = list(data_path.glob("*medien_hinweise-zu-e-books-e-journals-und-datenbanken.md"))
    if not parent_files:
        print("[bold]No parent e-books-e-journals-und-datenbanken file found for processing.")
        return
    parent_file = parent_files[0]

    # Find the shibboleth file
    shib_files = list(data_path.glob("*medien_hinweise-zu-e-books-e-journals-und-datenbanken_shibboleth.md"))
    if not shib_files:
        print("[bold]No shibboleth file found for processing.")
        return
    shib_file = shib_files[0]

    if verbose:
        print(f"[bold][Processing Shibboleth Append]")
        print(f"[bold]Parent file: {parent_file.name}")
        print(f"[bold]Shibboleth file: {shib_file.name}")

    try:
        # Read parent file content
        parent_content = parent_file.read_text(encoding="utf-8")
        parent_lines = parent_content.split('\n')

        # Find the '## Kontakt' section
        kontakt_start = find_section_position(parent_lines, "## Kontakt")

        # Read shibboleth file content
        shib_content = shib_file.read_text(encoding="utf-8")
        shib_content_body = extract_content_after_yaml_header(shib_content)

        if shib_content_body:
            # Adjust heading hierarchy in shibboleth content (demote by one level)
            adjusted_content = adjust_heading_hierarchy(
                content=shib_content_body,
                demote_levels=1
            )

            separator = "\n\n## Shibboleth-Zugang zu digitalen Medien\n\n"

            if kontakt_start >= 0:
                before_kontakt = '\n'.join(parent_lines[:kontakt_start])
                kontakt_section = '\n'.join(parent_lines[kontakt_start:])
                new_content = before_kontakt + separator + adjusted_content + "\n\n" + kontakt_section
            else:
                new_content = parent_content + separator + adjusted_content

            parent_file.write_text(new_content, encoding="utf-8")
            print(f"[bold green]Appended shibboleth information to {parent_file.name}")

            # Remove the shibboleth file after successful merge
            safe_remove_file(shib_file)
        else:
            if verbose:
                print(f"[bold red]Error: No content found in {shib_file.name}")

    except Exception as e:
        print(f"[bold red]Error processing shibboleth files: {e}")

    print(f"[bold green]Done. Processed shibboleth file.")

def post_process(
    data_dir: str = str(DATA_DIR),
    verbose: bool = False
    ):
    """
    Additional post-processing for already LLM processed markdown files.
    """
    data_path = Path(data_dir)
    if not data_path.exists():
        print(f"[bold red]Data directory {data_dir} does not exist!")
        return

    # Process "standorte" files
    process_standorte(data_path=data_path, verbose=verbose)

    # Augment "direktion" markdown
    process_direktion(data_path=data_path, verbose=verbose)
    
    # Process "semesterapparat" application file
    process_semesterapparat(data_path=data_path, verbose=verbose)

    # Process shibboleth file
    process_shibboleth(data_path=data_path, verbose=verbose)
