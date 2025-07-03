import os
import re
import requests
import shutil
import datetime
import xml.etree.ElementTree as ET
from rich import print
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from urllib.parse import urlparse, urljoin
from tqdm import tqdm
from openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import set_key, load_dotenv
from config import (
    ENV_PATH,
    URLS_TO_CRAWL,
    DATA_DIR,
    USE_OPENAI_VECTORSTORE
)

# === Load Configuration ===
load_dotenv(ENV_PATH)
TEMP_DIR = f"../data/markdown"
VECTORSTORE_ID = os.getenv("VECTORSTORE_ID")

# === Prompts ===
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
        print(f"[bold]===\n[Backup Markdown Folder]")
        print(f"[bold]{dir_path} -> {backup_path}\n===")
        
# === Crawler Funtions ===
def crawl_urls(
    sitemap_url: str,
    filters: list[str], 
    url_filename: str = str(URLS_TO_CRAWL), 
    save_to_disk: bool = True
    ) -> list[str] | None:
    """
    Fetches and filters URLs from an XML sitemap.
    """ 
    try:
        # Fetch the XML content from the URL
        response = requests.get(sitemap_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        xml_content = response.content

        # Parse the XML content directly from bytes
        root = ET.fromstring(xml_content)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        # Find the loc tag and get its text
        urls = root.findall('.//ns:loc', namespace)
        urls_clean = [url.text for url in urls]
        
        # Clean and filter urls
        clean_urls = list(set([url for url in urls_clean if url and url.startswith('http')]))
        clean_urls = sorted([url for url in clean_urls if not any(filter in url for filter in filters)])
        
        if save_to_disk:
            ensure_dir(Path(url_filename).parent)
            with open(url_filename, 'w', encoding='utf-8') as file:
                for url in clean_urls:
                    file.write(url + '\n')
        return clean_urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the XML: {e}")
    except ET.ParseError as e:
        print(f"Error parsing the XML: {e}")

def parse_uma_address_details(element):
    """
    Helper function for parsing HTML address details block.
    """
    lines = []
    # Street address
    street_div = element.find('div', class_='uma-address-street-address')
    if street_div:
        # Replace <br> with newlines, get text, strip, and join lines
        for br in street_div.find_all('br'):
            br.replace_with('\n')
        address = street_div.get_text(separator='\n').strip()
        address = ', '.join([line.strip() for line in address.split('\n') if line.strip()])
        lines.append(f"* Adresse: {address}")

    # Contact info
    contact_div = element.find('div', class_='uma-address-contact')
    if contact_div:
        contact_lines = []
        current_label = None
        for child in contact_div.children:
            if getattr(child, 'name', None) == 'strong':
                current_label = child.get_text(strip=True).replace(':', '')
            elif getattr(child, 'name', None) == 'a':
                href = child.get('href', '')
                text = child.get_text(strip=True)
                if current_label == 'Web':
                    contact_lines.append(f"* Web: [{text}]({href})")
                current_label = None
        lines.extend(contact_lines)
    return lines

def parse_email(element):
    """
    Helper function to parse e-mail addresses.
    """
    if not isinstance(element, Tag):
        return None
    email_tag = element.find('a', href='#')
    email = ''.join(email_tag.stripped_strings) if email_tag else None
    if email:
        email = re.sub(r'mail-', '@', email)
        return email
    else:
        return None

def parse_table(table_element):
    """
    Parse <tbody> to markdown
    """
    markdown_table = ''
        
    rows = table_element.find_all('tr')
    for row in rows:
        cells = row.find_all(['th', 'td'])
        row_content = "| " + " | ".join(cell.get_text(strip=True) for cell in cells) + " |"
        markdown_table += row_content + "\n"
        # Add header separator after first row
        if row.find('th') and rows.index(row) == 0:
            header_sep = "| " + " | ".join(['---'] * len(cells)) + " |"
            markdown_table += header_sep + "\n"
        elif not row.find('th') and rows.index(row) == 0:
            header_sep = "| " + " | ".join(['---'] * len(cells)) + " |"
            markdown_table += header_sep + "\n"
    return markdown_table

def find_specified_tags(
    tag: Tag,
    tag_list: list[str],
    tags_to_exclude: list[str],
    class_list: list[str],
    classes_to_exclude: list[str],
    url: str
) -> list:
    """
    Extracts and formats specified HTML tags and their contents from a BeautifulSoup tag object.
    Preserves the reading order of the HTML.
    """
    def parse_a_href(element):
        """
        Helper function to parse <a href> elements.
        """
        a_tags = element.find_all('a') if isinstance(element, Tag) else []
        element_text_md = element.get_text() if isinstance(element, Tag) else str(element)
        
        for a_tag in a_tags:
            href = a_tag.get('href') if isinstance(a_tag, Tag) else None
            if not (isinstance(href, str) and href):
                continue
            href_text = a_tag.get_text() if isinstance(a_tag, Tag) else str(a_tag)
            
            # Match absolute URLs
            if href.startswith('http'):
                href_md = f"{href_text} ({href})"
                element_text_md = element_text_md.replace(href_text, href_md)
                
            # Match relative URLs
            elif href.startswith('/'):
                if url.startswith('https://www.uni'):
                    href_url_md = f"{href_text} (https://www.uni-mannheim.de{href})"
                elif url.startswith('https://www.bib'):
                    href_url_md = f"{href_text} (https://www.bib.uni-mannheim.de{href})"
                else:
                    href_url_md = f"{href_text} ({href})"
                element_text_md = element_text_md.replace(href_text, href_url_md)
            else:
                element_text_md = element.get_text() if isinstance(element, Tag) else str(element)
        return element_text_md

    def final_check(matched_tags):
        clean_tags = []
        for tag in matched_tags:
            if '/ Bild:' in tag:
                continue
            elif 'mail-' in tag:
                new_tag = re.sub(r'mail-', '@', tag)
                clean_tags.append(new_tag)
            else:
                clean_tags.append(tag)
        return clean_tags

    def has_excluded_parent(element):
        for parent in getattr(element, 'parents', []):
            if not isinstance(parent, Tag):
                continue
            if parent.name in tags_to_exclude:
                parent_classes = []
                if element.parent and isinstance(element.parent, Tag):
                    parent_classes = element.parent.get('class') or []
                    parent_classes = [str(cls) for cls in parent_classes]
                if any(cls in classes_to_exclude for cls in parent_classes):
                    return True
        return False

    # Parse HTML
    matched_tags = []
    for element in tag.find_all(True, recursive=True):
        if not isinstance(element, Tag):
            continue
        
        tag_match = element.name in tag_list
        class_attr = element.get('class') or []
        class_attr = [str(cls) for cls in class_attr]
        class_match = any(cls in class_list for cls in class_attr)
        
        if not (tag_match or class_match):
            continue
        
        if has_excluded_parent(element):
            continue
        
        element_text = element.get_text(strip=True)
        
        # H1
        if element.name == 'h1':
            matched_tags.append(f'# {element_text} ({url})')
        
        # H2, H3
        elif element.name in ['h2', 'h3']:
            matched_tags.append(f'## {element_text}')
            
        # H4
        elif element.name == 'h4':
            profile_link = element.find('a', href=True)
            href = profile_link.get('href') if isinstance(profile_link, Tag) else None
            if isinstance(href, str) and (href.startswith('/') or href.startswith('http')):
                matched_tags.append(f"### {element_text} ({urljoin(url, str(href))})")
            else:
                matched_tags.append(f'### {element_text}')
                
        # H5
        elif element.name == 'h5':
            teaser_link = element.find('a', href=True)
            href = teaser_link.get('href') if isinstance(teaser_link, Tag) else None
            if isinstance(href, str) and (href.startswith('/') or href.startswith('http')):
                matched_tags.append(f"### {element_text} ({urljoin(url, str(href))})")
            else:
                matched_tags.append(f'### {element_text}')
                
        # H6
        elif element.name == 'h6':
            matched_tags.append(f'### {element_text}')
            
        # <p>, <b>
        elif element.name in ['p', 'b'] and not any(isinstance(parent, Tag) and parent.name == 'td' for parent in getattr(element, 'parents', [])):
            parent_classes = []
            if element.parent and isinstance(element.parent, Tag):
                parent_classes = element.parent.get('class') or []
                parent_classes = [str(cls) for cls in parent_classes]
            if parent_classes and 'testimonial-text' in parent_classes:
                if isinstance(element, Tag) and element.find_all('a'):
                    element_text_with_href = parse_a_href(element)
                    matched_tags.append(f"> {element_text_with_href}")
                else:
                    matched_tags.append(f"> {element_text}")
            else:
                text = element_text
                if isinstance(element, Tag):
                    for strong in element.find_all('strong'):
                        strong_text = f"**{strong.get_text(strip=True)}**"
                        text = text.replace(strong.get_text(strip=True), strong_text)
                    if element.find_all('a'):
                        matched_tags.append(parse_a_href(element))
                    else:
                        matched_tags.append(text)
                else:
                    matched_tags.append(text)
                    
        # class: teaser-link
        elif 'teaser-link' in class_attr:
            matched_tags.append(parse_a_href(element))
            
        # <ul>
        elif element.name == 'ul' and not element.has_attr('class'):
            li_elements = element.find_all('li', recursive=False) if isinstance(element, Tag) else []
            li_elements_clean = []
            for li in li_elements:
                if not isinstance(li, Tag):
                    continue
                if isinstance(li, Tag) and li.find_all('a'):
                    li_elements_clean.append(f'* {parse_a_href(li)}')
                else:
                    li_elements_clean.append(f'* {li.get_text(strip=True)}')
            matched_tags.append('\n' + '\n'.join(li_elements_clean) + '\n')
            
        # <tbody>
        elif element.name == 'tbody':
            matched_tags.append(parse_table(element))
            
        # class: icon
        elif 'icon' in class_attr:
            footer_phrases = [
                'Öffnungs­zeiten',
                'Freie Sitzplätze',
                'Auskunft und Beratung',
                'Chat Mo–Fr'
            ]
            icon_text = element.get_text(strip=True)
            if any(phrase in icon_text for phrase in footer_phrases):
                continue
            matched_tags.append(f"* {parse_a_href(element)}")
            
        # Address block
        elif 'uma-address-position' in class_attr:
            matched_tags.append(element_text)
        elif 'uma-address-details' in class_attr:
            lines = parse_uma_address_details(element)
            matched_tags.extend(lines)
        elif 'uma-address-contact' in class_attr:
            tel_tag = element.find('a', href=lambda x: isinstance(x, str) and x.startswith('tel:')) if isinstance(element, Tag) else None
            telephone = tel_tag.get_text(strip=True) if (tel_tag and isinstance(tel_tag, Tag)) else None
            if telephone:
                matched_tags.append(f'* Telefon: {telephone}')
            email = parse_email(element)
            if email:
                matched_tags.append(f'* E-Mail: {email}')
            orcid_tag = element.find('a', href=lambda x: isinstance(x, str) and 'orcid.org' in x) if isinstance(element, Tag) else None
            orcid = orcid_tag.get_text(strip=True) if (orcid_tag and isinstance(orcid_tag, Tag)) else None
            orcid_href = orcid_tag.get('href') if (orcid_tag and isinstance(orcid_tag, Tag) and isinstance(orcid_tag.get('href'), str)) else None
            if orcid and orcid_href:
                matched_tags.append(f'* ORCID-ID: {orcid} ({orcid_href})')
                
        # class: button
        elif 'button' in class_attr:
            href_val = element.get('href')
            profile_url = str(href_val) if isinstance(href_val, str) else None
            if profile_url:
                profile_url = urljoin(url, profile_url)
                profile_tasks = []
                try:
                    response = requests.get(profile_url)
                    if response.status_code == 200:
                        soup = BeautifulSoup(response.content, 'html.parser')
                        header = soup.find('h2')
                        if header and header.get_text(strip=True) == 'Aufgaben':
                            ul = header.find_next('ul')
                            if ul:
                                li_elements = ul.find_all('li')
                                profile_tasks = [li.get_text(strip=True) for li in li_elements if isinstance(li, Tag)]
                except Exception:
                    pass
                if profile_tasks:
                    matched_tags.append("\nAufgaben:\n\n" + "\n".join(f"* {task}" for task in profile_tasks))
    clean_tags = final_check(matched_tags)
    return clean_tags

def write_markdown(
    url,
    content,
    output_dir: str = TEMP_DIR,
    ):
    """
    Write markdown for a URL only if content is new or changed.
    Returns the filename if written/changed, else None.
    """
    ensure_dir(output_dir)
    url_path = urlparse(url).path.split('/')
    filename = '_'.join([part for part in url_path if part])
    file_path = Path(output_dir).joinpath(f"{filename}.md")
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

def process_urls(
    urls: list[str],
    verbose: bool = False,
    output_dir: str = ''
    ):
    """
    Processes a list of URLs by fetching their content and extracting specific
    HTML tags and classes. The extracted content can be saved into individual
    or a single markdown file. Returns a list of changed/new filenames.
    """
    # Backup output_dir if it exists
    if output_dir:
        backup_dir_with_timestamp(output_dir)
        
    changed_files = []
    for url in tqdm(urls): 
        if verbose:
            print(f'Crawling {url} ...')
            
        response = requests.get(url)
        content_single_page = []
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # List of tag names to match
            tags_to_find = [
                'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                'p', 'b', 'a', 'ul', 'tbody', 'table', 'strong'
            ]
            
            # List of class names to match
            classes_to_find = [
                'uma-address-position', 'uma-address-details',
                'uma-address-contact', 'button', 'icon',
                'teaser-link', 'contenttable'
            ]
            
            # List of tags to ignore
            tags_to_exclude = ['div']
            
            # List of classes to ignore
            classes_to_exclude = [
                'news', 'hide-for-large', 'gallery-slider-item', 
                'gallery-full-screen-slider-text-item'
            ]
            
            # Get main <div class="page content"> and ignore footer tag
            page_content = soup.find('div', id='page-content')
            if page_content is None:
                print("ERROR: page_content not found! Skipping URL ...")
                continue
            
            page_content_tags = find_specified_tags(
                tag=page_content, 
                tag_list=tags_to_find, 
                tags_to_exclude=tags_to_exclude,
                class_list=classes_to_find,
                classes_to_exclude=classes_to_exclude,
                url=url
            )
            
            # Add page content to list
            content_single_page.extend(page_content_tags)
            
            # Save markdown file only if changed/new
            written_file = write_markdown(url, content_single_page, output_dir)
            if written_file:
                changed_files.append(written_file)
                
    return changed_files

def process_markdown_files_with_llm(
    input_dir: str,
    output_dir: str,
    model_name: str = "gpt-4o-mini-2024-07-18",
    only_files: list = None
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

    print(f"[bold]===\n[Processing Markdown Files with {model_name}]\n===")
    
    for file_path in tqdm(input_files):
        print(f"Processing {file_path.name}...")
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
            
def create_openAI_vectorstore():
    """
    Create an OpenAI vectorstore and write its ID to .env.
    """    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    # Create vectorstore
    vector_store = client.vector_stores.create(name="aima_files")

    # Save vectorestore ID to .env
    set_key(str(ENV_PATH), "VECTORSTORE_ID", vector_store.id)
    return vector_store

def retrieve_openAI_vectorstore(id):
    """
    Retrieve an existing OpenAI vectorstore.
    """    
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    vector_store = client.vector_stores.retrieve(vector_store_id=id)
    return vector_store

def upload_files_to_openAI_vectorstore(upload_dir):
    """
    Upload markdown files to an existing OpenAI vectorstore.
    """
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    # Load markdown files
    md_files = list(Path(upload_dir).glob('*.md'))
    
    # Check if vectorstore contains files first
    vector_store_files = client.vector_stores.files.list(
        vector_store_id=str(VECTORSTORE_ID)
    )
    if len(vector_store_files.data) > 1:
        print('VECTORSTORE contains files. Aborting to avoid overwriting.')
        return
    
    # Upload files to vectorstore
    print(f"🔄 Uploading {len(md_files)} to OpenAI vectorstore.")
    for md_file in tqdm(md_files):
        try:
            # Upload file
            uploaded_file = client.files.create(
                file=open(md_file, "rb"),
                purpose="user_data"
            )
            
            # Link file to vector_store
            client.vector_stores.files.create(
                vector_store_id=str(VECTORSTORE_ID),
                file_id=uploaded_file.id
            )
        except Exception as e:
            print(f"Error: {e}")
    print(f"✅ Finished.")

if __name__ == "__main__":
    file_path = URLS_TO_CRAWL
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = crawl_urls(
            sitemap_url='https://www.bib.uni-mannheim.de/xml-sitemap/',
            filters=[
                'twitter',
                'youtube',
                'google',
                'facebook',
                'instagram',
                'primo',
                'absolventum',
                'portal2',
                'blog',
                'auskunft-und-beratung',
                'beschaeftigte-von-a-bis-z',
                'aktuelles/events',
                'ausstellungen-und-veranstaltungen',
                'anmeldung-fuer-schulen',
                'fuehrungen',
            ],
            save_to_disk=True,
            url_filename=str(URLS_TO_CRAWL)
        )
        
    if urls:
        # Download and parse each HTML page to markdown, get changed files
        changed_files = process_urls(
            urls=urls,
            verbose=True,
            output_dir=TEMP_DIR,
        )
        
        # Post-process only changed markdown with LLM
        if changed_files:
            process_markdown_files_with_llm(
                input_dir=TEMP_DIR,
                output_dir=str(DATA_DIR),
                model_name='gpt-4.1-mini-2025-04-14',
                only_files=changed_files
            )
        else:
            print("[bold]No markdown files changed, skipping LLM postprocessing.")
        
        # OpenAI vectorstore option
        if USE_OPENAI_VECTORSTORE:
            try:
                if VECTORSTORE_ID:
                    vector_store = retrieve_openAI_vectorstore(VECTORSTORE_ID)
                else:
                    vector_store = create_openAI_vectorstore()

                # Reload .env
                load_dotenv(str(ENV_PATH))
                print(f"⬆️ Uploading new files to OpenAI vectorstore: {VECTORSTORE_ID}")

                # Upload markdown to vectorstore
                if vector_store:
                    upload_files_to_openAI_vectorstore(DATA_DIR)
                    
            except Exception as e:
                print(f'Error: {e}')
