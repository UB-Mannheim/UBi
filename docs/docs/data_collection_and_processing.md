# Data Collection and Processing Pipeline

`Version 1.1`

This document describes the **data collection** and **data processing** pipeline used to gather and structure content from the [University Library Mannheim](https://www.bib.uni-mannheim.de/) website.

## Table of Contents

1. [Overview](#overview)
    - [Configuration](#configuration)
    - [YAML Header for Custom Documents](#yaml-header-for-custom-documents)
    - [Pipeline Steps](#pipeline-steps)
    - [Full Pipeline Example](#full-pipeline-example)
2. [Step 1: Data Collection — crawler.py](#step-1-data-collection--crawlerpy)
    - [URL Discovery](#url-discovery)
    - [Content Extraction](#content-extraction)
    - [Output and Change Detection](#output-and-change-detection)
    - [CLI Reference](#cli-reference)
3. [Step 2: Data Processing — markdown_processing.py](#step-2-data-processing--markdown_processingpy)
    - [LLM-Based Processing](#llm-based-processing)
    - [Additional Post-Processing](#additional-post-processing)
    - [Custom Documents Sync](#custom-documents-sync)
    - [Hash Snapshot](#hash-snapshot)
    - [CLI Reference](#cli-reference-1)
4. [Data Flow](#data-flow)

## Overview

The pipeline consists of two main steps with **hash-based file tracking** to detect website updates and changes to custom documents (i.e., internal documents not part of the library's website). **Both** steps must be run sequentially to ensure the hash-based tracking works correctly.

### Configuration

Four variables in `code/config.py` are essential for the pipeline:

```python
URLS_TO_CRAWL = Path("../data/urls.txt")
CRAWL_DIR = Path("../data/markdown")
CUSTOM_DOCS_DIR = Path("../data/custom_docs")
DATA_DIR = Path("../data/markdown_processed")
```

| Variable | Description |
|---|---|
| `URLS_TO_CRAWL` | Path to a text file containing URLs to crawl (one per line). If this file does not exist on disk, the crawler falls back to the XML sitemap. |
| `CRAWL_DIR` | Directory where raw crawled markdown files are saved. |
| `CUSTOM_DOCS_DIR` | Directory for custom markdown files not part of the library's website. Files must be `.md` format with a valid YAML header (see [below](#yaml-header-for-custom-documents)). |
| `DATA_DIR` | Directory where final post-processed markdown files are saved — these files serve as the chatbot's knowledge base. |

### YAML Header for Custom Documents

All markdown files in `CUSTOM_DOCS_DIR` **must** contain a valid YAML header. During LLM post-processing, YAML headers are automatically added to crawled pages. However, custom documents skip LLM processing to preserve their original content and structure, so the header must be added manually.

It is **mandatory** to provide `source_url_de` and `source_url_en`, as the chatbot injects at least one URL in every response. Missing URLs may lead to hallucinated links.

#### Example YAML Header

```yaml
---
title: Nutzungsbedingungen für den UBi (KI-Chatbot) der Universitätsbibliothek Mannheim
source_url_de: https://chat.bib.uni-mannheim.de/public/docs/ubi_policy.pdf
source_url_en: https://chat.bib.uni-mannheim.de/public/docs/ubi_policy.pdf
category: Services
tags: ['Nutzungsbedingungen UBi', 'KI-Chatbot der Universitätsbibliothek Mannheim', 'UBi', 'Serviceangebot', 'Rechtliches']
language: de
---
```

### Pipeline Steps

1. **Data Collection** (`code/crawler.py`): Crawls the library website, extracts content from HTML pages, and saves the results as raw markdown files in `CRAWL_DIR`.
2. **Data Processing** (`code/markdown_processing.py`): Performs LLM-based post-processing (content structuring, cleaning, YAML header injection) on new or changed files, runs additional domain-specific post-processing on `DATA_DIR`, syncs custom documents from `CUSTOM_DOCS_DIR` to `DATA_DIR`, and writes hash snapshots for change tracking.

Both scripts provide `click` CLI interfaces with configurable options (see the respective [crawler CLI](#cli-reference) and [processing CLI](#cli-reference-1) sections).

#### Important Note

When `crawler.py` runs again after an initial crawl, it compares the newly crawled content against existing files in `CRAWL_DIR`. Only pages with actual content changes or previously uncrawled URLs produce updated files. Subsequently, `markdown_processing.py` uses hash-based comparison to identify which files in `CRAWL_DIR` have changed since the last processing run, and only processes those.

### Full Pipeline Example

Make sure the virtual environment is active.

```bash
cd code

# Step 1: Crawl all URLs
python crawler.py

# Step 2: Post-process crawled files and sync custom docs
python markdown_processing.py
```

## Step 1: Data Collection — `crawler.py`

When `crawler.py` runs, it first creates a timestamped backup of `CRAWL_DIR` in `../data/backups/`.

### URL Discovery

- **Primary source**: A text file at `URLS_TO_CRAWL` (default: `../data/urls.txt`) containing one URL per line.
- **Fallback**: If the file does not exist on disk, the [XML sitemap](https://www.bib.uni-mannheim.de/xml-sitemap/) is fetched asynchronously via `aiohttp` and the discovered URLs are saved to `URLS_TO_CRAWL` for future runs.
- **Filtering**: URLs matching specific patterns are excluded (social media, portals, events, blog posts, etc.).

### Content Extraction

The crawler extracts content from the `<div id="page-content">` section of each page, targeting specific HTML elements and CSS classes while ignoring headers, footers, and navigation.

#### Targeted HTML Elements

| Category | Elements |
|---|---|
| Headings | `h1`, `h2`, `h3`, `h4`, `h5`, `h6` |
| Text | `p`, `b`, `strong` |
| Lists | `ul`, `ol` |
| Tables | `tbody`, `table` |
| Links | `a` |

#### Targeted CSS Classes

| Category | Classes |
|---|---|
| Address blocks | `uma-address-position`, `uma-address-details`, `uma-address-contact` |
| Navigation / UI | `button`, `icon`, `teaser-link` |
| Content | `accordion-content`, `contenttable` |

#### Exclusion Rules

| Type | Values |
|---|---|
| Tags | `div` (when parent has an excluded class) |
| Classes | `news`, `hide-for-large`, `gallery-slider-item`, `gallery-full-screen-slider-text-item` |

#### Content Processing Features

- **Link resolution**: Relative URLs are converted to absolute URLs.
- **English URL extraction**: The English page URL is parsed from `<div class="language-selector">` and stored as `<en_url>` metadata for the LLM post-processing step.
- **Email parsing**: Obfuscated email addresses are decoded. Two obfuscation methods are handled: the legacy method (`mail-` → `@`) and the current method using `<span class="commat"></span>` (replaced with `@`) combined with a hidden `<span style="display:none">mail-</span>` decoy (removed).
- **Address formatting**: Structured parsing of `uma-address-*` contact blocks (name, position, street, phone, email, ORCID).
- **Table conversion**: HTML tables are converted to markdown table format.
- **Profile integration**: For elements with class `button`, linked profile pages are fetched and "Aufgaben" (tasks) sections are extracted and appended.
- **Soft hyphen removal**: Invisible characters (soft hyphens, zero-width spaces, non-breaking spaces, etc.) are cleaned from crawled text.

### Output and Change Detection

- Raw markdown files are saved to `CRAWL_DIR` (default: `../data/markdown/`).
- Filenames are generated from the URL path structure (e.g., `https://www.bib.uni-mannheim.de/foo/bar/` → `foo_bar.md`).
- **Content comparison**: Before writing a file, the crawler compares the newly crawled content against the existing file on disk. Only files with actual changes are overwritten.
- **404 handling**: If a previously crawled URL returns HTTP 404, the corresponding local markdown files in both `CRAWL_DIR` and `DATA_DIR` are deleted automatically.
- After crawling completes, hash-based comparison against the stored snapshot identifies and reports all changed files.

### CLI Reference

```bash
Usage: crawler.py [OPTIONS]

  Main crawling function.

Options:
  -q, --quiet           Only print errors to stdout. Suppresses progress bars
                        and info messages.
  -w, --write-snapshot  Only write file hashes for CRAWL_DIR and exit.
  --help                Show this message and exit.
```

- `-w, --write-snapshot`: Manually writes a hash snapshot to `CRAWL_DIR/snapshot/md_hashes.json` for the current files without crawling.

## Step 2: Data Processing — `markdown_processing.py`

After Step 1, `markdown_processing.py` handles post-processing of the crawled markdown files using OpenAI's API. It also syncs custom documents from `CUSTOM_DOCS_DIR` to `DATA_DIR`.

Before LLM processing begins, a timestamped backup of `DATA_DIR` is created in `../data/backups/`.

### LLM-Based Processing

| Setting | Value |
|---|---|
| **Model** | OpenAI GPT (default: `gpt-4.1-2025-04-14`) |
| **Temperature** | `0` (deterministic output) |
| **Concurrency** | Async processing with semaphore (max 3 concurrent requests) |
| **Rate limiting** | Configurable delay between API requests |
| **Fallback** | Sequential processing if async batch processing fails |

**What the LLM does for each file:**

- Adds a structured YAML header with metadata (title, URLs, category, tags, language).
- Eliminates redundant content while preserving all unique information.
- Structures and cleans the markdown for optimal semantic search.
- Fixes link formatting and heading hierarchy.
- Validates and formats the output markdown using `mdformat`.

**File selection** (default behavior, no CLI flags): Only files in `CRAWL_DIR` that are new or modified since the last hash snapshot are processed. Alternatively, specific files or an entire input directory can be passed via the `-f` or `-i` CLI options.

### Additional Post-Processing

After LLM processing, domain-specific post-processing merges and augments certain pages in `DATA_DIR`:

#### 1. "Standorte" (Locations)

- Groups location files (`standorte*.md`) by base name.
- Finds linked "Ansprechpersonen" (contact) pages.
- Appends contact information to the shortest file in each group.
- Removes the merged contact files after successful integration.

#### 2. "Direktion" (Management)

- Augments the leadership page (`*direktion.md`).
- Updates title and profile descriptions for consistency.

#### 3. "Semesterapparat" (Course Reserves)

- Merges the application form page (`*semesterapparat_antrag*.md`) into the main semesterapparat page.
- Inserts the merged content before the "Kontakt" section if present, otherwise appends it.
- Removes the application file after merging.

#### 4. "Shibboleth" (Authentication)

- Appends Shibboleth access information to the e-resources page (`*e-books-e-journals-und-datenbanken.md`).
- Preserves the "Kontakt" section at the end.
- Removes the Shibboleth file after merging.

### Custom Documents Sync

After all post-processing is complete, custom documents from `CUSTOM_DOCS_DIR` are synced to `DATA_DIR`:

- Only **new or modified** files (detected via hash comparison against `CUSTOM_DOCS_DIR/snapshot/md_hashes.json`) are copied.
- Custom documents are **not** processed by the LLM — they are copied as-is to preserve their manually curated content.
- After syncing, a hash snapshot is written to `CUSTOM_DOCS_DIR/snapshot/md_hashes.json`.

### Hash Snapshot

At the end of processing (enabled by default, controlled by `--write-snapshot`), a hash snapshot is written to `CRAWL_DIR/snapshot/md_hashes.json`. This JSON file stores SHA256 hashes of all `.md` files and is used in future runs to identify which files have changed.

### CLI Reference

```bash
Usage: markdown_processing.py [OPTIONS]

  CLI for post-processing markdown files.

Options:
  -i, --input-dir TEXT            Input directory containing markdown files to
                                  process (Default: CRAWL_DIR).
  -f, --files TEXT                Specific markdown files to process. Can be
                                  used multiple times. (e.g., -f file1.md -f
                                  file2.md)
  -m, --model-name TEXT           Model name for LLM postprocessing. (Default:
                                  gpt-4.1-2025-04-14)
  -t, --temperature INTEGER       LLM temperature for post-processing.
                                  (Default: 0)
  -llm, --llm-processing / --no-llm-processing
                                  Run LLM post-processing on markdown files.
                                  (Default: True)
  -add, --additional-processing / --no-additional-processing
                                  Run additional post-processing on markdown
                                  files. (Default: True)
  -format, --format-markdown / --no-format-markdown
                                  Run only markdown formatting for all files
                                  in input_dir. (Default: False)
  -w, --write-snapshot / --no-write-snapshot
                                  Write a hash snapshot to input_dir.
                                  (Default: True)
  -q, --quiet                     Only print errors to stdout. Suppresses
                                  progress bars and info messages. (Default:
                                  True)
  --help                          Show this message and exit.
```

## Data Flow

```text
                          ┌──────────────────────────┐
                          │      URL Source          │
                          │  urls.txt or XML Sitemap │
                          └───────────┬──────────────┘
                                      │
                    ══════════════════════════════════════
                    ║          Step 1: crawler.py         ║
                    ══════════════════════════════════════
                                      │
                        Backup CRAWL_DIR → ../data/backups/
                                      │
                        Crawl HTML pages & extract content
                                      │
                        Content-based change detection
                        (only write new/changed files)
                                      │
                                      ▼
          ┌───────────────────────────────────────────────────┐
          │                      CRAWL_DIR                    │
          │                 ../data/markdown/                 │
          │   (raw markdown files + snapshot/md_hashes.json)  │
          └───────────────────────┬───────────────────────────┘
                                  │
                    ══════════════════════════════════════
                    ║    Step 2: markdown_processing.py   ║
                    ══════════════════════════════════════
                                  │
                    Hash-based change detection against
                    CRAWL_DIR/snapshot/md_hashes.json
                    (only process new/changed files)
                                  │
                    Backup DATA_DIR → ../data/backups/
                                  │
                    LLM post-processing
                    (YAML header, content cleanup,
                     deduplication, mdformat)
                                  │
                    Write results to DATA_DIR
                                  │
                    Additional post-processing on DATA_DIR
                    ├── Standorte: merge contact pages
                    ├── Direktion: augment leadership page
                    ├── Semesterapparat: merge application form
                    └── Shibboleth: merge auth info
                                  │
                                  │     ┌──────────────────────────────┐
                                  │     │      CUSTOM_DOCS_DIR         │
                                  │     │   ../data/custom_docs/       │
                                  │     │  (manually curated .md files │
                                  │     │ + snapshot/md_hashes.json)   │
                                  │     └──────────────┬───────────────┘
                                  │                    │
                                  │     Hash-based change detection
                                  │     Copy new/changed files (no LLM)
                                  │                    │
                                  ▼                    ▼
          ┌───────────────────────────────────────────────────┐
          │                    DATA_DIR                       │
          │           ../data/markdown_processed/             │
          │                                                   │
          │   Final knowledge base for the chatbot            │
          │   (LLM-processed crawled files + custom docs)     │
          └───────────────────────────────────────────────────┘
```
