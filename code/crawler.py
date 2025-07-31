import asyncio
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

import aiohttp
import click
import requests
import utils
from bs4 import BeautifulSoup, Tag
from config import CRAWL_DIR, URLS_TO_CRAWL
from dotenv import load_dotenv
from markdown_processing import write_markdown
from rich import print
from tqdm import tqdm


# === Crawler Funtions ===
async def crawl_urls(
    sitemap_url: str,
    filters: list[str],
    url_filename: str = str(URLS_TO_CRAWL),
    save_to_disk: bool = True
    ) -> list[str] | None:
    """
    Fetches and filters URLs from an XML sitemap asynchronously.
    """
    try:
        # Fetch the XML content from the URL asynchronously
        async with aiohttp.ClientSession() as session:
            async with session.get(sitemap_url) as response:
                response.raise_for_status()
                xml_content = await response.read()

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
            utils.ensure_dir(Path(url_filename).parent)
            with open(url_filename, 'w', encoding='utf-8') as file:
                for url in clean_urls:
                    file.write(url + '\n')
        return clean_urls
    except aiohttp.ClientError as e:
        print(f"Error fetching the XML: {e}")
    except ET.ParseError as e:
        print(f"Error parsing the XML: {e}")

def parse_english_url(element) -> list[str]:
    """
    Parse english URL string from <div class="language-selector">
    """
    url_tag_en = element.find('a', attrs={'lang': 'en'})
    if url_tag_en:
        base_url = 'https://www.bib.uni-mannheim.de'
        url_part = url_tag_en.get('href')
        markdown_string = f"<en_url>{base_url + url_part}</en_url>"
        return [markdown_string]
    else:
        return ['']

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

    def li_to_markdown(li: Tag) -> str:
        if li.find_all('a'):
            return f'* {parse_a_href(li)}'
        else:
            return f'* {li.get_text(strip=True)}'

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

        # class: accordion-content
        elif 'accordion-content' in class_attr:
            # Find the first <ul> inside this element (even if it has a class)
            ul = element.find('ul')
            if ul and isinstance(ul, Tag):
                li_elements = ul.find_all('li', recursive=False)
                li_elements_clean = []
                for li in li_elements:
                    if not isinstance(li, Tag):
                        continue
                    li_elements_clean.append(li_to_markdown(li))
                matched_tags.append('\n' + '\n'.join(li_elements_clean) + '\n')
            else:
                # fallback: just get the text
                matched_tags.append(element.get_text(strip=True))

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
                            if ul and isinstance(ul, Tag):
                                li_elements = ul.find_all('li')
                                profile_tasks = [li.get_text(strip=True) for li in li_elements if isinstance(li, Tag)]
                except Exception:
                    pass
                if profile_tasks:
                    matched_tags.append("\nAufgaben:\n\n" + "\n".join(f"* {task}" for task in profile_tasks))
    clean_tags = final_check(matched_tags)
    return clean_tags

def process_urls(
    urls: list[str],
    output_dir: str = ''
    ):
    """
    Processes a list of URLs by fetching their content and extracting specific
    HTML tags and classes. The extracted content can be saved into individual
    or a single markdown file. Returns a list of changed/new filenames.
    """
    # Backup output_dir if it exists
    if output_dir:
        utils.backup_dir_with_timestamp(output_dir)

    changed_files = []
    for url in tqdm(urls, desc="Crawling URLs"):
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
                'teaser-link', 'contenttable', 'accordion-content'
            ]

            # List of tags to ignore
            tags_to_exclude = ['div']

            # List of classes to ignore
            classes_to_exclude = [
                'news', 'hide-for-large', 'gallery-slider-item',
                'gallery-full-screen-slider-text-item'
            ]

            # Parse <div class="language-selector"> to get English URL
            div_language_selector = soup.find(
                'div',
                attrs={'class': 'language-selector'}
            )
            if div_language_selector:
                english_url_markdown = parse_english_url(div_language_selector)
                content_single_page.extend(english_url_markdown)

            # Get main <div class="page content"> and ignore footer tag
            page_content = soup.find('div', id='page-content')
            if page_content is None:
                print(f"[bold]Error: page_content not found! Skipping {url} ...")
                continue

            page_content_tags = find_specified_tags(
                tag=page_content,
                tag_list=tags_to_find,
                tags_to_exclude=tags_to_exclude,
                class_list=classes_to_find,
                classes_to_exclude=classes_to_exclude,
                url=url
            ) if isinstance(page_content, Tag) else []

            # Add page content to list
            content_single_page.extend(page_content_tags)

            # Save markdown file only if changed/new
            written_file = write_markdown(url, content_single_page, output_dir)
            if written_file:
                changed_files.append(written_file)

    return changed_files

@click.command()
@click.option(
    '--write-hashes-only/--no-write-hashes-only', '-w',
    default=False,
    help='Only write file hashes for CRAWL_DIR and exit.'
    )
def main(write_hashes_only) -> Optional[list[str] | list[Path]]:
    """
    Main crawling function.
    """
    # Write hashes only and exit
    if write_hashes_only:
        utils.write_hashes_for_directory(CRAWL_DIR)
        return

    # Crawl URLs
    file_path = URLS_TO_CRAWL
    if file_path.exists():
        print(f"[bold]Using {str(URLS_TO_CRAWL)} to crawl URLs.")
        with file_path.open("r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        sitemap_url = 'https://www.bib.uni-mannheim.de/xml-sitemap/'
        print(f"[bold]Crawling all URLs from {sitemap_url}")
        urls = asyncio.run(crawl_urls(
            sitemap_url=sitemap_url,
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
        ))
    if urls:
        process_urls(
            urls=urls,
            output_dir=CRAWL_DIR,
        )
    else:
        print("[bold red]No URLs found to crawl. Exiting.")
        return

    # Hash-based file change detection in CRAWL_DIR
    changed_files = utils.get_new_or_modified_files_by_hash(CRAWL_DIR)

    if changed_files:
        changed_files_str = '\n'.join(str(f) for f in changed_files)
        print(f"[bold green]{len(changed_files)} changed file(s) detected in {CRAWL_DIR}:")
        print(f"[bold green]{changed_files_str}")
        return changed_files
    else:
        print("[bold]No markdown files changed.")

if __name__ == "__main__":
    main()
