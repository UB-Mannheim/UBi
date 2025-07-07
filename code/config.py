from pathlib import Path

ENV_PATH = Path("../.env")
DATA_DIR = Path("../data/markdown_processed")
URLS_TO_CRAWL = Path("../data/urls.txt")
PERSIST_DIR = Path("../data/vectorstore")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 0
RSS_URL = "https://blog.bib.uni-mannheim.de/Aktuelles/?feed=rss2&cat=4"
DB_PATH = "../data/feedback.db"

# Session Memory Configuration
SESSION_MEMORY_CONFIG = {
    "max_turns": 10,           # Maximum conversation turns to remember
    "max_tokens": 4000,        # Maximum tokens in memory
    "context_window": 5,       # Recent turns to include in context
}