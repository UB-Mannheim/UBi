# Data Collection and Processing Pipeline

This README describes the **data collection** and **data processing** pipeline used to gather and structure content from the [University Library Mannheim](https://www.bib.uni-mannheim.de/) website.

## Overview

The pipeline consists of two steps with **hash-based** file tracking to keep track of website updates. **Both** pipeline steps must be run to ensure the hash-based file tracking works correctly.

### Prerequisites

Two variables in `code/config.py` are essential for data collection and processing:

```python
CRAWL_DIR = Path("../data/markdown")
DATA_DIR = Path("../data/markdown_processed")
```

- `CRAWL_DIR`: directory where the crawled website are saved as markdown files
- `DATA_DIR`: directory where the post-processed markdown files are saved that are used as the knowledge base for the chatbot

### Processing steps

1. **Data Collection** (`code/crawler.py`): Handles the web crawling and HTML extraction. Returns markdown files.
2. **Data Processing** (`code/markdown_processing.py`): LLM-based post-processing of the crawled markdown files (content structuring, cleaning and YAML header injection). After the data processing is finished a **hash snapshot** is written to `CRAWL_DIR`.

Both python scripts come with `click` CLI interfaces to adjust different parameters (see below).

### Note

If `crawler.py` is run again, it checks if there are any changes to the already processed markdown files in `CRAWL_DIR` (meaning the website was changed) or if there are new URLs that weren't previously crawled. Only those website with updates / changes will then be available for data processing.

### Full pipeline example

Make sure `venv` is active.

```bash
cd code

# Crawl all URLs in ../data/urls.txt
python crawler.py

# Post-process all crawled URLs
python markdown_processing.py
```

## Step 1: Data Collection → `crawler.py`

If `crawler.py` is run a backup of the current `CRAWL_DIR` will be created in `../data/backups`.

### URL Discovery

- **Crawled URLs**: The website's [XML sitemap](`https://www.bib.uni-mannheim.de/xml-sitemap/`) is used for crawling if no `URLS_TO_CRAWL` path is defined in `code/config.py`
- **Method**: Asynchronous HTTP requests using `aiohttp`
- **Filtering**: Excludes URLs containing specific patterns (social media, portals, events, etc.)

### Content Extraction

The crawler extracts content from specific HTML elements and CSS classes and avoids other parts of the website (e.g. footer and header sections):

#### Targeted HTML Elements

- Headings: `h1`, `h2`, `h3`, `h4`, `h5`, `h6`
- Text content: `p`, `b`, `strong`
- Lists: `ul`, `li`
- Tables: `tbody`, `table`
- Links: `a`

#### Targeted CSS Classes

- Address information: `uma-address-position`, `uma-address-details`, `uma-address-contact`
- Navigation: `button`, `icon`, `teaser-link`
- Content: `accordion-content`, `contenttable`

#### Exclusion Rules

- Tags: `div` (when in excluded contexts)
- Classes: `news`, `hide-for-large`, `gallery-slider-item`, `gallery-full-screen-slider-text-item`

### Content Processing Features

- **Link Resolution**: Converts relative URLs to absolute URLs
- **Email Parsing**: Handles obfuscated email addresses (`mail-` → `@`)
- **Address Formatting**: Structured parsing of contact information
- **Table Conversion**: Converts HTML tables to Markdown format
- **Profile Integration**: Fetches additional content from linked profile pages

### Output

- Raw markdown files are saved to `../data/markdown/`
- Filename generation based on URL path structure
- Change detection using hash-based comparison

### Usage

#### Command Line Interface

```bash
Usage: crawler.py [OPTIONS]

  Main crawling function.

Options:
  -w, --write-hashes-only / --no-write-hashes-only
                                  Only write file hashes for CRAWL_DIR and
                                  exit.
  --help                          Show this message and exit.
```

- `-w, --write-hashes-only`: Manually write a hash snapshot to `CRAWL_DIR` for the current files in `CRAWL_DIR`

## Step 2: Data Processing → `markdown_processing.py`

After step 1 was completed successfully `code/markdown_processing.py` will handle the post-processing of the crawled website using OpenAI's API.

### LLM-Based Processing

- **Model**: OpenAI GPT models (default: `gpt-4.1-mini-2025-04-14`)
- **Processing**: Concurrent async processing with rate limiting
- **Input**: Raw markdown from step 1
- **Output**: Structured markdown with YAML headers

### Processing Features

- **YAML Header Addition**: Adds metadata headers to markdown files
- **Content Structuring**: LLM-based content organization and formatting
- **Heading Hierarchy**: Automatic adjustment of heading levels

### Post-Processing Operations

#### 1. "Standorte" Processing

- Groups location markdowns (Standorte) by base name
- Appends contact information from linked pages
- Merges related content and removes duplicate files

#### 2. "Direktion"  Enhancement

- Augments leadership page content
- Updates titles and descriptions for consistency

#### 3. "Semesterapparat" Integration

- Merges application forms with main semesterapparat pages
- Maintains proper section ordering

#### 4. "Shibboleth" Content Integration

- Appends Shibboleth access information to e-resources pages
- Preserves contact sections at the end

### Usage

#### Command Line Interface

```bash
Usage: markdown_processing.py [OPTIONS]

  CLI for post-processing markdown files.

Options:
  -i, --input-dir TEXT            Input directory containing markdown files to
                                  process (default: CRAWL_DIR).
  -f, --files TEXT                Specific markdown files to process. Can be
                                  used multiple times. (e.g., -f file1.md -f
                                  file2.md)
  -m, --model-name TEXT           Model name for LLM postprocessing. (default:
                                  gpt-4o-mini-2024-07-18)
  -llm, --llm-processing / --no-llm-processing
                                  Run LLM post-processing on markdown files.
                                  (default: True)
  -add, --additional-processing / --no-additional-processing
                                  Run additional post-processing on markdown
                                  files. (default: True)
  -v, --verbose / --no-verbose    Enable verbose output during post-
                                  processing. (default: False)
  --help                          Show this message and exit.
```

## Data Flow

```
XML Sitemap → URL Filtering → HTML Crawling → Content Extraction → Raw Markdown
                                                                    ↓
Final Markdown ← Post-Processing ← LLM Processing ← YAML Headers ← Structured Content
```
