import asyncio
import os
import re
import time
import mdformat
from pathlib import Path
from typing import Optional

import backoff
import click
import utils
from config import CRAWL_DIR, DATA_DIR
from langchain_openai import ChatOpenAI
from prompts import PROMPT_POST_PROCESSING
from rich import print
from tqdm import tqdm


# === Processing Functions ===
def extract_content_after_yaml_header(content: str) -> str:
    """
    Extract content after YAML header (after second '---').

    Args:
        content: Markdown content with YAML header

    Returns:
        Content after YAML header
    """
    lines = content.split("\n")
    content_start = 0
    yaml_end_count = 0

    for i, line in enumerate(lines):
        if line.strip() == "---":
            yaml_end_count += 1
            if yaml_end_count == 2:
                content_start = i + 1
                break

    return "\n".join(lines[content_start:]).strip()


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
        new_hashes = "#" * (len(hashes) + demote_levels)
        return f"{new_hashes} "

    # Use a single regex to match all headings and demote them properly
    return re.sub(r"^(#{1,6}) ", demote_heading, content, flags=re.MULTILINE)


def url_to_filename(url: str) -> str:
    """
    Convert URL to filename by removing domain and replacing slashes
    with underscores.
    """
    url_path = url.replace("https://www.bib.uni-mannheim.de/", "")
    return url_path.replace("/", "_").rstrip("_") + ".md"


def safe_remove_file(
    file_path: Path, processed_files: set | None = None
) -> bool:
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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content},
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


def validate_and_format_markdown(content: str) -> str:
    """
    Ensure correct markdown formatting.
    """
    # Get YAML header
    yaml_data = utils.parse_yaml_header(md_data=content)

    # Remove YAML header from content
    pattern = r"^---\s*\n.*?\n---\s*\n"
    markdown_raw = re.sub(pattern, "", content, flags=re.MULTILINE | re.DOTALL)

    # Format markdown
    markdown_clean = mdformat.text(markdown_raw)

    # Remove trailing \ from line endings
    markdown_clean = re.sub(
        r"\\\s*(?=\n|$)", "", markdown_clean, flags=re.MULTILINE
    )

    # Combine YAML header and clean markdown
    body = "\n".join(f"{k}: {v}" for k, v in yaml_data.items())
    markdown_final = f"---\n{body}\n---\n\n{markdown_clean}"

    return markdown_final


def run_markdown_formatting(input_dir: str):
    """
    Run markdown formatting for the input_dir and save the formatted
    files to the same directory.
    """
    # Ensure directory exists
    input_path = Path(input_dir)
    if not input_path.exists() or not input_path.is_dir():
        print(
            f"[bold yellow]Directory not found or not a directory: {input_dir}"
        )
        return

    # Load all .md from input_dir
    files_to_process = list(Path(input_dir).glob("*.md"))
    if not files_to_process:
        print(f"[bold yellow]No .md files found in {input_dir}.")
        return

    print(
        f"[bold][Formatting Markdown] {len(files_to_process)} file(s) in {input_dir}"
    )

    count = 0
    for file_path in tqdm(files_to_process, desc="Formatting"):
        try:
            raw_content = file_path.read_text(encoding="utf-8")
            formatted_content = validate_and_format_markdown(raw_content)
            file_path.write_text(formatted_content, encoding="utf-8")
            count += 1
        except Exception as e:
            print(f"❌ Error formatting {file_path.name}: {e}")

    print(
        f"[bold green]Formatted {count}/{len(files_to_process)} file(s) in {input_dir}"
    )


def clean_soft_hyphens(text: str) -> str:
    """
    Remove soft hyphens and invisible width modifiers that may appear
    in crawled text. Also normalize non-breaking spaces to regular spaces.
    """
    # Characters to remove
    SOFT_HYPHEN = "\u00ad"  # SHY
    ZERO_WIDTH_SPACE = "\u200b"
    ZERO_WIDTH_NON_JOINER = "\u200c"
    ZERO_WIDTH_JOINER = "\u200d"
    ZERO_WIDTH_NBSP = "\ufeff"
    WORD_JOINER = "\u2060"

    if not text:
        return text

    # Normalize NBSP to regular space
    cleaned = text.replace("\u00a0", " ")

    # Strip invisible/soft characters
    for ch in (
        SOFT_HYPHEN,
        ZERO_WIDTH_SPACE,
        ZERO_WIDTH_NON_JOINER,
        ZERO_WIDTH_JOINER,
        ZERO_WIDTH_NBSP,
        WORD_JOINER,
    ):
        cleaned = cleaned.replace(ch, "")
    return cleaned


def write_markdown_from_url(
    url,
    content: list[str],
    output_dir: str = CRAWL_DIR,
) -> Optional[Path]:
    """
    Write markdown for a URL only if content is new or changed.
    Returns the filename if written/changed, else None.
    """
    # Ensure output_dir exists
    utils.ensure_dir(output_dir)

    # Format filename and path
    file_path = utils.get_markdown_filepath_for_url(url, output_dir)

    new_content = ""
    for el in content:
        # Clean el (a string) from all soft hyphens
        cleaned_el = clean_soft_hyphens(el)

        if cleaned_el.startswith("#"):
            new_content += "\n\n" + cleaned_el + "\n\n"
        else:
            new_content += cleaned_el + "\n"

    # Check if file exists and content is unchanged
    if file_path.exists():
        old_content = file_path.read_text(encoding="utf-8")
        if old_content == new_content:
            return None  # No change

    # Write new/changed content
    file_path.write_text(new_content, encoding="utf-8")
    return file_path.name


@backoff.on_exception(backoff.expo, Exception, max_tries=3)
async def process_single_file_async(
    llm: ChatOpenAI, file_path, output_path, prompt
):
    """
    Process a single markdown file with retry logic.
    """
    content = file_path.read_text(encoding="utf-8")

    print(f"[bold]Processing {file_path} ...")

    # LLM interaction
    messages = create_llm_messages(prompt, content)
    response = await llm.ainvoke(messages)

    # Validate and format markdown
    clean_response = validate_and_format_markdown(response.content)

    # Write to output
    output_file = output_path / file_path.name
    output_file.write_text(clean_response, encoding="utf-8")
    return file_path.name


def process_markdown_files_with_llm(
    input_dir: str,
    output_dir: str,
    model_name: str = "gpt-4.1-2025-04-14",
    temperature: float = 0,
    files_to_process: list | None = None,
    max_concurrent: int = 3,
    delay_between_requests: float = 0.5,
):
    """
    Post-process markdown files with LLM and add YAML header.
    If files_to_process is provided, only process those files.

    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to write processed files
        model_name: OpenAI model to use
        files_to_process: List of specific files to process
        max_concurrent: Maximum concurrent API requests
        delay_between_requests: Delay between requests in seconds
    """
    # Backup output_dir if it exists
    if output_dir:
        utils.backup_dir_with_timestamp(output_dir)

    # Check for updated files
    if files_to_process is not None:
        input_files = [f for f in files_to_process if f.exists()]
        if len(input_files) != len(files_to_process):
            missing_files = [f for f in files_to_process if not f.exists()]
            for missing_file in missing_files:
                print(f"[bold yellow]Warning: File not found: {missing_file}")
    else:
        input_files = list(Path(input_dir).glob("*.md"))

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize the LLM
    llm = ChatOpenAI(
        model=model_name,
        temperature=temperature,
        api_key=os.getenv("OPENAI_API_KEY"),
        max_retries=2,
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
                        llm, file_path, output_path, PROMPT_POST_PROCESSING
                    )
                    # Add delay between requests to respect rate limits
                    if delay_between_requests > 0:
                        await asyncio.sleep(delay_between_requests)
                    return result
                except Exception as e:
                    print(f"❌ Error processing {file_path.name}: {e}")
                    return None

        # Create tasks for all files
        tasks = [
            process_with_semaphore(file_path) for file_path in input_files
        ]

        # Process with progress bar
        completed = 0
        for coro in tqdm(
            asyncio.as_completed(tasks),
            total=len(tasks),
            desc="LLM Processing",
        ):
            result = await coro
            if result:
                completed += 1

        return completed

    # Run the async processing
    try:
        completed_count = asyncio.run(process_files_async())
        print(
            f"[bold green]Successfully processed {completed_count}/{len(input_files)} files"
        )
    except Exception as e:
        print(f"[bold red]Error during batch processing: {e}")
        # Fallback to sequential processing
        print("[bold yellow]Falling back to sequential processing...")
        process_markdown_files_sequential(llm, input_files, output_path)


def process_markdown_files_sequential(llm, input_files, output_path):
    """
    Fallback sequential processing if async fails.
    """
    for file_path in tqdm(input_files, desc="LLM Processing"):
        try:
            print(f"[bold]Processing {file_path} ...")
            content = file_path.read_text(encoding="utf-8")

            # LLM interaction
            messages = create_llm_messages(PROMPT_POST_PROCESSING, content)
            response = llm.invoke(messages)

            # Validate and format markdown
            clean_response = validate_and_format_markdown(response.content)

            # Write to output
            output_file = output_path / file_path.name
            output_file.write_text(clean_response, encoding="utf-8")

            # Add delay between requests (reduced for better performance)
            time.sleep(0.2)

        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")


def process_standorte(data_path: Path, verbose: bool = False):
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
        print("[bold][Processing Standorte Contacts]")

    # Group files by their base name (e.g., "bb-a3", "bb-a5" ...)
    file_groups = {}
    for file_path in standorte_files:
        # Extract base name by removing "standorte_" prefix and suffixes after "_"
        stem = file_path.stem
        if stem.startswith("standorte_"):
            base_name = stem[10:]  # Remove "standorte_" prefix
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
            contact_link_pattern = r"\[.*?Ansprechpersonen.*?\]\((https://www\.bib\.uni-mannheim\.de/[^)]+)\)"
            matches = re.findall(contact_link_pattern, content, re.IGNORECASE)

            if not matches and verbose:
                print(
                    f"[bold yellow]No 'Ansprechpersonen' found in {shortest_file.name}"
                )
                continue

            if verbose:
                print(
                    f"[bold]Found {len(matches)} contact links in {shortest_file.name}"
                )

            for contact_url in matches:
                # Convert URL to filename
                contact_filename = url_to_filename(contact_url)
                contact_file_path = data_path / contact_filename

                # Skip if this contact file has already been processed
                if contact_filename in processed_contacts:
                    if verbose:
                        print(
                            f"[bold yellow]Skipping {contact_filename} - already processed"
                        )
                        continue

                if contact_file_path.exists():
                    if verbose:
                        print(
                            f"[bold]Appending content from {contact_filename}"
                        )

                    # Read contact content
                    contact_content = contact_file_path.read_text(
                        encoding="utf-8"
                    )

                    # Extract content after YAML header and skip first # heading
                    contact_content_body = extract_content_after_yaml_header(
                        content=contact_content
                    )
                    if contact_content_body:
                        # Skip the first heading (usually # heading)
                        lines = contact_content_body.split("\n")
                        if lines and lines[0].startswith("# "):
                            contact_content_body = "\n".join(lines[2:]).strip()

                    if contact_content_body:
                        # Adjust heading hierarchy in contact content (demote by two levels)
                        adjusted_content = adjust_heading_hierarchy(
                            content=contact_content_body, demote_levels=2
                        )

                        # Append contact content to original file
                        separator = "\n\n### Weitere Ansprechpersonen\n\n"
                        new_content = content + separator + adjusted_content

                        # Write back to file
                        shortest_file.write_text(new_content, encoding="utf-8")
                        processed_count += 1
                        print(
                            f"[bold green]Appended contact information to {shortest_file.name}"
                        )

                        # Remove the contact file after successful merge
                        safe_remove_file(contact_file_path, processed_contacts)

                        print(
                            f"[bold green]Done. Processed {processed_count} contact files."
                        )
                    else:
                        if verbose:
                            print(
                                f"[bold red]Error: No content found in {contact_filename}"
                            )
                else:
                    if verbose:
                        print(
                            f"[bold red]Contact file not found: {contact_filename}"
                        )

        except Exception as e:
            print(f"[bold red]Error processing {shortest_file.name}: {e}")


def process_direktion(data_path: Path, verbose: bool = False):
    """
    Augemnt "ihre-ub_ansprechpersonen_direktion.md"
    """
    # Find "direktion" markdown
    direktion_md = list(data_path.glob("*direktion.md"))
    if not direktion_md:
        print("[bold ]No '*direktion.md' for processing.")
        return

    try:
        md_data = direktion_md[0].read_text(encoding="utf-8")

        # Augment the # heading
        heading_match = re.search(r"^# .*$", md_data, re.MULTILINE)
        if heading_match:
            old_string = heading_match.group(0)
            new_string = (
                "# Direktion und Leitung der Universitätsbibliothek Mannheim"
            )
            md_data = re.sub(re.escape(old_string), new_string, md_data)

        # Augment the profile description
        profile_match = re.search(
            r"^Direktorin der Universitätsbibliothek\s*$",
            md_data,
            re.MULTILINE,
        )
        if profile_match:
            old_string = profile_match.group(0)
            new_string = "Direktorin und Leiterin der Universitätsbibliothek"
            md_data = re.sub(re.escape(old_string), new_string, md_data)

        # Write augmented file
        direktion_md[0].write_text(md_data, encoding="utf-8")

        print("[bold green]Done. Augmented 'Direktion' markdown page.")

    except Exception as e:
        print(f"[bold red]Error processing Direktionen files: {e}")


def process_semesterapparat(data_path: Path, verbose: bool = False):
    """
    Post-processing function that finds the semesterapparat application file
    and appends its content to the parent semesterapparat file.
    """
    # Find the parent semesterapparat file
    semesterapparat_files = list(data_path.glob("*semesterapparat.md"))
    semesterapparat_files = [
        f for f in semesterapparat_files if "antrag" not in f.name
    ]

    if not semesterapparat_files:
        print("[bold]No parent semesterapparat file found for processing.")
        return

    parent_file = semesterapparat_files[0]

    # Find the application file
    antrag_files = list(data_path.glob("*semesterapparat_antrag*.md"))

    if not antrag_files:
        return

    antrag_file = antrag_files[0]

    if verbose:
        print("[bold][Processing Semesterapparat Application]")
        print(f"[bold]Parent file: {parent_file.name}")
        print(f"[bold]Application file: {antrag_file.name}")

    try:
        # Read parent file content
        parent_content = parent_file.read_text(encoding="utf-8")
        parent_lines = parent_content.split("\n")

        # Find the "## Kontakt" section
        kontakt_start = find_section_position(parent_lines, "## Kontakt")

        # Read application file content
        antrag_content = antrag_file.read_text(encoding="utf-8")

        # Extract content after YAML header from application file
        antrag_content_body = extract_content_after_yaml_header(antrag_content)

        if antrag_content_body:
            # Adjust heading hierarchy in application content (demote by one level)
            adjusted_content = adjust_heading_hierarchy(
                content=antrag_content_body, demote_levels=1
            )

            # Construct new content
            separator = (
                "\n## Antrag auf Einrichtung eines Semesterapparats\n\n"
            )

            if kontakt_start >= 0:
                # If Kontakt section exists, insert before it
                before_kontakt = "\n".join(parent_lines[:kontakt_start])
                kontakt_section = "\n".join(parent_lines[kontakt_start:])
                new_content = (
                    before_kontakt
                    + separator
                    + adjusted_content
                    + "\n\n"
                    + kontakt_section
                )
            else:
                # If no Kontakt section, just append to the end
                new_content = parent_content + separator + adjusted_content

            # Write back to parent file
            parent_file.write_text(new_content, encoding="utf-8")
            print(
                f"[bold green]Appended application information to {parent_file.name}"
            )

            # Remove the application file after successful merge
            safe_remove_file(antrag_file)

            print(
                "[bold green]Done. Processed semesterapparat application file."
            )
        else:
            if verbose:
                print(
                    f"[bold red]Error: No content found in {antrag_file.name}"
                )

    except Exception as e:
        print(f"[bold red]Error processing semesterapparat files: {e}")


def process_shibboleth(data_path: Path, verbose: bool = False):
    """
    Appends the content from the shibboleth markdown file to the parent
    e-books-e-journals-und-datenbanken.md file, placing the parent's
    Kontakt section at the end.
    """
    # Find the parent file
    parent_files = list(
        data_path.glob(
            "*medien_hinweise-zu-e-books-e-journals-und-datenbanken.md"
        )
    )
    if not parent_files:
        print(
            "[bold]No parent e-books-e-journals-und-datenbanken file found for processing."
        )
        return
    parent_file = parent_files[0]

    # Find the shibboleth file
    shib_files = list(
        data_path.glob(
            "*medien_hinweise-zu-e-books-e-journals-und-datenbanken_shibboleth.md"
        )
    )
    if not shib_files:
        return

    shib_file = shib_files[0]

    if verbose:
        print("[bold][Processing Shibboleth Append]")
        print(f"[bold]Parent file: {parent_file.name}")
        print(f"[bold]Shibboleth file: {shib_file.name}")

    try:
        # Read parent file content
        parent_content = parent_file.read_text(encoding="utf-8")
        parent_lines = parent_content.split("\n")

        # Find the '## Kontakt' section
        kontakt_start = find_section_position(parent_lines, "## Kontakt")

        # Read shibboleth file content
        shib_content = shib_file.read_text(encoding="utf-8")
        shib_content_body = extract_content_after_yaml_header(shib_content)

        if shib_content_body:
            # Adjust heading hierarchy in shibboleth content (demote by one level)
            adjusted_content = adjust_heading_hierarchy(
                content=shib_content_body, demote_levels=1
            )

            separator = "\n\n## Shibboleth-Zugang zu digitalen Medien\n\n"

            if kontakt_start >= 0:
                before_kontakt = "\n".join(parent_lines[:kontakt_start])
                kontakt_section = "\n".join(parent_lines[kontakt_start:])
                new_content = (
                    before_kontakt
                    + separator
                    + adjusted_content
                    + "\n\n"
                    + kontakt_section
                )
            else:
                new_content = parent_content + separator + adjusted_content

            parent_file.write_text(new_content, encoding="utf-8")
            print(
                f"[bold green]Appended shibboleth information to {parent_file.name}"
            )

            # Remove the shibboleth file after successful merge
            safe_remove_file(shib_file)

            print("[bold green]Done. Processed shibboleth file.")
        else:
            if verbose:
                print(f"[bold red]Error: No content found in {shib_file.name}")

    except Exception as e:
        print(f"[bold red]Error processing shibboleth files: {e}")


def additional_post_processing(
    data_dir: str = str(DATA_DIR), verbose: bool = False
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

    # Process "shibboleth" file
    process_shibboleth(data_path=data_path, verbose=verbose)


@click.command()
@click.option(
    "--input-dir",
    "-i",
    default=None,
    help="Input directory containing markdown files to process (default: CRAWL_DIR).",
)
@click.option(
    "--files",
    "-f",
    multiple=True,
    help="Specific markdown files to process. Can be used multiple times. (e.g., -f file1.md -f file2.md)",
)
@click.option(
    "--model-name",
    "-m",
    default="gpt-4.1-2025-04-14",
    help="Model name for LLM postprocessing. (default: gpt-4.1-2025-04-14)",
)
@click.option(
    "--temperature",
    "-t",
    default=0,
    help="LLM temperature for post-processing. (default: 0)",
)
@click.option(
    "--llm-processing/--no-llm-processing",
    "-llm",
    default=True,
    help="Run LLM post-processing on markdown files. (default: True)",
)
@click.option(
    "--additional-processing/--no-additional-processing",
    "-add",
    default=True,
    help="Run additional post-processing on markdown files. (default: True)",
)
@click.option(
    "--format-markdown/--no-format-markdown",
    "-format",
    default=False,
    help="Run only markdown formatting for all files in input_dir. (default: False)",
)
@click.option(
    "--write-snapshot/--no-write-snapshot",
    "-snapshot",
    default=True,
    help="Write a hash snapshot to input_dir. (default: True)",
)
@click.option(
    "--verbose/--no-verbose",
    "-v",
    default=False,
    help="Enable verbose output during post-processing. (default: False)",
)
def run_post_processing(
    input_dir: str,
    files: tuple,
    model_name: str,
    temperature: float,
    llm_processing: bool,
    additional_processing: bool,
    format_markdown: bool,
    write_snapshot: bool,
    verbose: bool,
):
    """
    CLI for post-processing markdown files.
    """
    # Determine which files to process
    files_to_process = []

    # Specific files option
    if files:
        # If input_dir is not specified, use CRAWL_DIR as default
        if not input_dir:
            input_dir = CRAWL_DIR

        # Resolve all files to absolute paths
        for f in files:
            # If file path contains directory separators, treat as full path
            if "/" in str(f) or "\\" in str(f):
                # Try to resolve relative to current directory first
                file_path = Path(f).resolve()
                if not file_path.exists():
                    # If not found, try relative to project root
                    file_path = (Path.cwd().parent / f).resolve()
            else:
                # Otherwise, treat as relative to input_dir
                file_path = (Path(input_dir) / f).resolve()

            if file_path.exists():
                files_to_process.append(file_path)
            else:
                print(f"[bold yellow]Warning: File not found: {f}")

        print(
            f"[bold]Processing {len(files_to_process)} markdown file(s):\n{', '.join(str(f) for f in files_to_process)}"
        )

    # input_dir option
    elif input_dir:
        files_to_process = list(Path(input_dir).glob("*.md"))
        print(
            f"[bold]Processing {len(files_to_process)} markdown files in {input_dir}."
        )

    # Hash snapshot (default fallback)
    else:
        input_dir = CRAWL_DIR
        files_to_process = utils.get_new_or_modified_files_by_hash(
            input_dir, return_path_objects=True
        )

    if not files_to_process:
        print("[bold yellow]No files to process. Exiting.")
        return

    # Post-processing with LLM
    if llm_processing:
        process_markdown_files_with_llm(
            input_dir=input_dir,
            output_dir=str(DATA_DIR),
            files_to_process=files_to_process,
            model_name=model_name,
            temperature=temperature,
        )

    # Additional post-processing
    if additional_processing:
        additional_post_processing(data_dir=str(DATA_DIR), verbose=verbose)

    # Markdown formatting only
    if format_markdown:
        if not input_dir:
            print(
                "[bold yellow]Please provide an input_dir for markdown formatting."
            )
            return
        run_markdown_formatting(input_dir=input_dir)

    # Update hash snapshot after processing
    if write_snapshot:
        utils.write_hashes_for_directory(input_dir)


if __name__ == "__main__":
    run_post_processing()
