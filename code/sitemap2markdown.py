import re
import requests
import xml.etree.ElementTree as ET
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from urllib.parse import urlparse, urljoin
from tqdm import tqdm
import os
from langchain_openai import ChatOpenAI

OUTPUT_DIR = "../data/markdown"
OUTPUT_DIR_PROCESSED = "../data/markdown_processed"
txt_filename='../data/urls.txt' # file with URLs

def ensure_dir(dir) -> None:
    path = Path(dir)
    if not path.exists():
        path.mkdir(parents=True)
        

def crawl_all_urls(sitemap_url, filters: list, txt_filename: str = txt_filename, save_to_disk: bool = True):
    """
    Fetches and filters URLs from an XML sitemap.

    Args:
        sitemap_url (str): The URL of the XML sitemap to crawl.
        filters (list): A list of strings to filter out URLs containing any of these substrings.
        txt_filename (str, optional): The name of the file to save the filtered URLs. Defaults to txt_filename.
        save_to_disk (bool, optional): Whether to save the filtered URLs to disk. Defaults to True.

    Returns:
        list: A list of filtered URLs if `save_to_disk` is True, otherwise an empty list.

    Raises:
        requests.exceptions.RequestException: If there is an error fetching the XML sitemap.
        ET.ParseError: If there is an error parsing the XML sitemap.
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
        clean_urls = list(set([url for url in urls_clean if url.startswith('http')]))
        clean_urls = sorted([url for url in clean_urls if not any(filter in url for filter in filters)])
        
        if save_to_disk:
            ensure_dir(Path(txt_filename).parent)
            with open(txt_filename, 'w', encoding='utf-8') as file:
                for url in clean_urls:
                    file.write(url + '\n')
        return clean_urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the XML: {e}")
    except ET.ParseError as e:
        print(f"Error parsing the XML: {e}")


def find_specified_tags(tag: Tag, tag_list: list[str], tags_to_exclude: list[str],
                        class_list: list[str], classes_to_exclude: list[str], url: str) -> list:
    """
    Extracts and formats specified HTML tags and their contents from a BeautifulSoup tag object.

    This function searches through the descendants of a given BeautifulSoup tag object,
    extracting and formatting content from tags specified in `tag_list` and classes specified
    in `class_list`. The extracted content is returned in Markdown format, with special handling
    for URLs, emails, and other specific tag types.

    Args:
        tag (BeautifulSoup.Tag): The root tag to search within.
        tag_list (list): A list of tag names (e.g., ['h1', 'p', 'li']) to match and extract.
        class_list (list): A list of class names (e.g., ['teaser-link', 'uma-address-position']) 
                           to match and extract.
        url (str): The base URL of the page being processed, used to construct absolute URLs 
                   from relative URLs.

    Returns:
        list: A list of strings containing the extracted and formatted content in Markdown format.
    """
    def get_a_href(element):
        a_tags = element.find_all('a')
        element_text_md = element.text
        
        for a_tag in a_tags:
            # Match absolute URLs 
            if a_tag['href'].startswith('http'):
                href_text = a_tag.text
                href_url = a_tag['href']
                href_md = f"{href_text} ({href_url})"
                element_text_md = element_text_md.replace(a_tag.text, href_md)
                
            # Match relative URLs
            elif a_tag['href'].startswith('/'):
                href_text = a_tag.text
                href_url_part = a_tag['href']
                if url.startswith('https://www.uni'):
                    href_url_md = f"{href_text} (https://www.uni-mannheim.de{href_url_part})"
                elif url.startswith('https://www.bib'):
                    href_url_md = f"{href_text} (https://www.bib.uni-mannheim.de{href_url_part})"
                element_text_md = element_text_md.replace(a_tag.text, href_url_md)
                
            # If no URL was found return element.text
            else:
                element_text_md = element.text
        return element_text_md
            
    def get_email(element):
        email_tag = element.find('a', href='#')
        email = ''.join(email_tag.stripped_strings) if email_tag else None
        if email:
            email = re.sub(r'mail-', '@', email)
            return email
        else:
            return None
        
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
    
    
    matched_tags = []
    
    for element in tag.descendants:
        if element.name and (element.name in tag_list or any(cls in element.get('class', []) for cls in class_list)):
            
            # Check if a certain parent tag is present and skip processing if so                        
            skip_element = False
            for parent in element.parents:
                if parent.name in tags_to_exclude:
                    for cls in parent.get('class', []):
                        if cls in classes_to_exclude:
                            skip_element = True
                            break
                if skip_element:
                    break
            if skip_element:
                continue
                        
            element_text = element.text.strip()
            
            # Handle headings h1 - h3 differently from h4 - h6
            if element.name == 'h1':
                matched_tags.append(f'# {element_text} ({url})')
            elif element.name in ['h2', 'h3']:
                matched_tags.append(f'## {element_text}')
            elif element.name == 'h4':
                profile_link = element.find_next('a', href=True)
                if profile_link and profile_link['href'].startswith(('/', 'http')):
                    matched_tags.append(f"### {element_text} ({urljoin(url, profile_link['href'])})")
                else:
                    matched_tags.append(f'### {element_text}')
            elif element.name == 'h5':
                matched_tags.append(f'### {element_text}')
            elif element.name in ['h6']:
                matched_tags.append(f'### {element_text}')
                
            # Handle <p> and <b> tags and href
            if element.name in ['p', 'b'] and not any(parent.name == 'td' for parent in element.parents): 
                
                # Check if element is a part of a block quote
                if element.parent and 'testimonial-text' in element.parent.get('class', []):
                    if element.find_all('a'):
                        element_text_with_href = get_a_href(element)
                        matched_tags.append(f"> {element_text_with_href}")
                    else:
                        matched_tags.append(f"> {element.text.strip()}")
                        
                # Check for <br> tags and replace them with a line break
                if element.find_all('br'):
                    for br in element.find_all('br'):
                        br.replace_with('\n') 
                
                # Check for <strong> tags
                if element.find_all('strong'):
                    for el in element.find_all('strong'):
                        bold_text = f"**{el.text.strip()}**"
                        el.replace_with(bold_text)
                        
                # Look for links
                if element.find_all('a'):
                    matched_tags.append(get_a_href(element))
                else:
                    matched_tags.append(element.text.strip())
                    
            # Handle div class "teaser_link" (button for forwarding to another URL)
            if 'teaser-link' in element.get('class', []):
                matched_tags.append(get_a_href(element))
            
            # Handle <ul> tags
            if element.name == 'ul' and not element.has_attr('class'):
                li_elements = element.find_all('li')
                
                li_elements_clean = []
                for li in li_elements:
                    if li.find_all('a'):
                        li_elements_clean.append(f'* {get_a_href(li)}')
                    else:
                        li_elements_clean.append(f'* {li.text}')

                matched_tags.append('\n' + '\n'.join(li for li in li_elements_clean) + '\n')
                
            # Handle tables <tbody>
            if element.name == 'tbody':
                markdown_table = ''
                rows = element.find_all('tr')
                for row in rows:
                    cells = row.find_all(['th', 'td'])  # Include both th and td elements
                    row_content = "| " + " | ".join(cell.get_text(strip=True) for cell in cells) + " |"
                    markdown_table += row_content + "\n"

                    # Add a header separator row after the first row if it contains headers
                    if row.find('th') and rows.index(row) == 0:
                        header_sep = "| " + " | ".join(['---'] * len(cells)) + " |"
                        markdown_table += header_sep + "\n"
                    elif row.find('th') == None and rows.index(row) == 0:
                        header_sep = "| " + " | ".join(['---'] * len(cells)) + " |"
                        markdown_table += header_sep + "\n"
                        
                matched_tags.append(markdown_table)
        
            # Handle "icon" class
            if 'icon' in element.get('class', []):
                footer_phrases = [
                    'Öffnungs­zeiten',
                    'Freie Sitzplätze',
                    'Auskunft und Beratung',
                    'Chat Mo–Fr'
                ]

                icon_text = element.get_text(strip=True)
    
                # Skip if it's any of the known footer icons
                if any(phrase in icon_text for phrase in footer_phrases):
                    continue

                matched_tags.append(f"* {get_a_href(element)}")
        
            # KONTAKT CONTENT
            # Handle classes → position, contact details, address, profile 
            if 'uma-address-position' in element.get('class', []):
                matched_tags.append(element_text)
                  
            elif 'uma-address-details' in element.get('class', []):
                element_temp = element_text.split('\n')
                element_temp = [el.strip() for el in element_temp]
                element_temp = ', '.join([el for el in element_temp if len(el) > 1])
                matched_tags.append(f'\nKontaktinformationen:\n\n* Adresse: {element_temp}')
                
            elif 'uma-address-contact' in element.get('class', []):
                # Get telephone number
                tel_tag = element.find('a', href=lambda x: x and x.startswith('tel:'))
                telephone = tel_tag.text if tel_tag else None
                if telephone:
                    matched_tags.append(f'* Telefon: {telephone}') 
                
                # Get Email
                email = get_email(element)
                if email:
                    matched_tags.append(f'* E-Mail: {email}') 
                    
                # Get ORCID-ID
                orcid_tag = element.find('a', href=lambda x: x and 'orcid.org' in x)
                orcid = orcid_tag.text if orcid_tag else None
                if orcid:
                    matched_tags.append(f'* ORCID-ID: {orcid} ({orcid_tag.get("href")})') 
                
            # Check if profile button exists and load additional profile information
            elif 'button' in element.get('class', []):
                profile_url = urljoin(url, element.get('href'))
                profile_tasks = []

                # Check for page
                response = requests.get(profile_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Find "Aufgaben" heading
                    header = soup.find('h2')
                    if header and header.text.strip() == 'Aufgaben':  
                        ul = header.find_next('ul')
                        if ul:
                            li_elements = ul.find_all('li')
                            profile_tasks = [li.text.strip() for li in li_elements]
                        
                if profile_tasks:
                    matched_tags.append("\nAufgaben:\n\n" + "\n".join(f"* {task}" for task in profile_tasks))
              
    clean_tags = final_check(matched_tags)
    return clean_tags


def postprocess_markdown_files(folder: str, verbose: bool = False) -> None:
    # Get markdown filepaths from folder
    filepaths = sorted(list(Path(folder).glob('*.md')))

    # Lists and filters for the processing steps below
    heading_filters = ['Neuigkeit', 'News', 'Aktuelles']
    seen_contact_blocks = []

    for file in filepaths:
        # Read markdown
        with open(Path(file), 'r', encoding='utf-8') as file_in:
            raw_data = file_in.read()
            split_data = raw_data.split('\n\n\n')
            split_data = [line.strip() for line in split_data]

        # Clean redundant "Kontakt" block information
        clean_content_blocks, seen_contact_blocks = clean_kontakt_block(split_data, seen_contact_blocks)

        # Skip markdown files that contain only a single h1 heading without any content
        if len(clean_content_blocks) <= 1:
            continue

        clean_content_blocks_final = []

        for idx, block in enumerate(clean_content_blocks):
            # Remove soft hyphes (unicode "U+00AD" → "\xad")
            block = block.replace('\xad', '')

            # Remove trailing "Kontakt" heading
            if (idx + 1) == len(clean_content_blocks) and re.search(r'#+.*[Kk]ontakt\b', block):
                continue

            # Remove "News" headings as news content parts are not crawled
            elif any(filter in block for filter in heading_filters) and (idx + 1) <= len(clean_content_blocks):
                if clean_content_blocks[idx + 1].startswith('#'):
                    continue

            # Remove trailing . in headings as it is not markdown conform
            elif block.startswith('#') and block.endswith('.'):
                block = block[:-1]

            clean_content_blocks_final.append(block)

        if verbose:
            print(f"split_data from {file}:\n{split_data}\n")
            print(f"clean_content_blocks:\n{clean_content_blocks_final}\n")

        # Write cleaned content in  to markdown
        write_postprocessed_markdown(clean_content_blocks_final, file)


def clean_kontakt_block(split_data: list[str], seen_contact_blocks: list[str]) -> tuple[list, list]:
    # List for cleaned content
    clean_content_blocks = []

    # Flag to mark if "Kontakt" content block was detected
    inside_contact_block = False

    # Iterate over content blocks
    for block in split_data:
        if inside_contact_block:
            if block in seen_contact_blocks:
                continue
            else:
                seen_contact_blocks.append(block)
                clean_content_blocks.append(block)
        elif re.search(r'#+.*[Kk]ontakt\b', block):
            inside_contact_block = True
            clean_content_blocks.append(block)
        else:
            clean_content_blocks.append(block)

    return clean_content_blocks, seen_contact_blocks


def write_postprocessed_markdown(content: list[str], filepath: str) -> None:
    filepath = Path(filepath)
    processed_folder = Path(f"{filepath.parent}_processed")

    if not processed_folder.exists():
        processed_folder.mkdir(parents=True)
    new_filepath = processed_folder.joinpath(filepath.name)

    # Remove leading/trailing whitespace and filter out empty blocks
    cleaned_blocks = [block.strip() for block in content if block.strip()]

    with open(new_filepath, 'w', encoding='utf-8') as markdown_file:
        markdown_file.write('\n'.join(cleaned_blocks))


def write_markdown(url, content, output_dir: str = OUTPUT_DIR, single_file: bool = False):
    # Check if output_dir exists, else create it
    ensure_dir(output_dir)
    
    url_path = urlparse(url).path.split('/')
    filename = '_'.join([part for part in url_path if part])
    
    if single_file:
        # Write single markdown file with all content
        with open(Path(output_dir).joinpath('content_all_pages.md'), 'w', encoding='utf-8') as file:
            for el in content:
                for line in el:
                    if line.startswith('#'):
                        markdown_file.write('\n\n' + line + '\n\n')
                    else:
                        markdown_file.write(line + '\n')
                file.write('\n')
    else:
        # Write one markdown for each URL
        with open(f"{Path(output_dir).joinpath(filename)}.md", 'w', encoding='utf-8') as markdown_file:
            for el in content:
                if el.startswith('#'):
                    markdown_file.write('\n\n' + el + '\n\n')
                else:
                    markdown_file.write(el + '\n')

   
def process_urls(urls: list, single_file: bool = False, verbose: bool = False,
                 postprocess: bool = False, output_dir: str = ''):
    """
    Processes a list of URLs by fetching their content and extracting specific HTML tags and classes. The extracted content can be saved into individual or a single markdown file.
    
    Parameters:
    urls (list): A list of URLs to process.
    single_file (bool, optional): If True, all extracted content will be saved in a single markdown file. 
                                  Defaults to False.
    verbose (bool, optional): If True, prints the URL being processed and additional logs. Defaults to False.
    
    Returns:
    None
    """
    content_all_pages = []
    
    for url in tqdm(urls): 
        if verbose:
            print(f'Processing {url} ...')
            
        response = requests.get(url)
        content_single_page = []
        
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # List of tag names and class names to match
                tags_to_find = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'b', 'a', 'ul', 'tbody', 'strong']
                classes_to_find = ['uma-address-position', 'uma-address-details', 'uma-address-contact', 'button',
                                'icon', 'teaser-link']
                
                # List of tag names and class names to exclude
                # These tags will be ignorerd to exclude fast changing content parts like "news" items 
                tags_to_exclude = ['div']
                classes_to_exclude = ['news', 'hide-for-large', 'gallery-slider-item', 'gallery-full-screen-slider-text-item']
                
                # Get main <div class="page content"> and ignore footer tag
                page_content = soup.find('div', id='page-content')
                page_content_tags = find_specified_tags(tag=page_content, 
                                                        tag_list=tags_to_find, 
                                                        tags_to_exclude=tags_to_exclude,
                                                        class_list=classes_to_find,
                                                        classes_to_exclude=classes_to_exclude,
                                                        url=url)
                
                # Add page content to list
                content_single_page.extend(page_content_tags)
                
                # Append single page content to list with all other page content
                content_all_pages.append(content_single_page)
        
                # Save markdown file
                write_markdown(url, content_single_page, output_dir)
            
        except Exception as e:
            print(f'Error ({e}) while processing {url}. Continuing ...')
    
    if single_file:
        write_markdown(url, content_all_pages, output_dir, single_file=True)
        
    if postprocess:
        postprocess_markdown_files(output_dir, verbose)

def process_markdown_files_with_llm(input_dir: str, output_dir: str, model_name: str = "gpt-4o-mini-2024-07-18"):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Initialize the LLM (LangChain wrapper for OpenAI Chat API)
    llm = ChatOpenAI(
        model_name=model_name,
        temperature=0,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
    )

    # Prompt to guide markdown cleanup for RAG
    system_prompt = """You are a helpful assistant that prepares markdown documents for Retrieval-Augmented Generation (RAG).
Clean the structure, improve headings, embed links using markdown syntax, add YAML frontmatter with title, source_url, tags (if inferable), and language (de).
Chunk content into semantic blocks of 100–300 words. Remove redundancy and make the file suitable for semantic search or chatbot use.
"""

    for file_path in input_path.glob("*.md"):
        print(f"🔄 Processing {file_path.name}...")
        content = file_path.read_text(encoding="utf-8")

        try:
            # LLM interaction
            response = llm.invoke([
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": content}
            ])

            # Write to output
            output_file = output_path / file_path.name
            output_file.write_text(response.content, encoding="utf-8")
            print(f"✅ Saved: {output_file.name}")

        except Exception as e:
            print(f"❌ Error processing {file_path.name}: {e}")

if __name__ == "__main__":
    file_path = Path(txt_filename)
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = crawl_all_urls(
            sitemap_url='https://www.bib.uni-mannheim.de/xml-sitemap/',
            filters=[
                'twitter', 'youtube', 'google', 'facebook', 'instagram',
                'primo', 'absolventum', 'portal2', 'blog'
            ],
            save_to_disk=True,
            txt_filename=txt_filename
        )
    # Saves one .md for each URL
    # Some URLs will not be processed as they do not follow the standard style guide uni-mannheim.de
    process_urls(
        urls=urls,
        single_file=False,
        verbose=True,
        output_dir=OUTPUT_DIR,
    )
    process_markdown_files_with_llm(OUTPUT_DIR, OUTPUT_DIR_PROCESSED)
