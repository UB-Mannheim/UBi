from pathlib import Path

ENV_PATH = Path("../.env")
URLS_TO_CRAWL = Path("../data/urls.txt")
CRAWL_DIR = Path("../data/markdown")
DATA_DIR = Path("../data/markdown_processed")
PERSIST_DIR = Path("../data/vectorstore")
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 0
RSS_URL = "https://blog.bib.uni-mannheim.de/Aktuelles/?feed=rss2&cat=4"
DB_PATH = "../data/feedback.db"

# Session Memory Configuration
SESSION_MEMORY_CONFIG = {
    "max_turns": 10,  # Maximum conversation turns to remember
    "max_tokens": 4000,  # Maximum tokens in memory
    "context_window": 5,  # Recent turns to include in context
}

# Rate Limiting Configuration
RATE_LIMIT_CONFIG = {
    "max_chars_per_request": 500,  # Maximum characters per request
    "max_chars_per_session": 5000,  # Maximum characters per session
    "max_turns_per_session": 24,  # Maximum turns per session
    "max_requests_per_minute": 12,  # Maximum requests per minute
    "rate_limit_window": 60,  # Rate limit window in seconds
    "global_max_requests": 1, #1000,  # Global maximum requests
    "global_rate_limit_window": 600,  # Global rate limit window in seconds (10 minutes)
    "global_block_duration": 3600,  # Duration to block requests if limit exceeded (1 hour)
    "admin_passphrase": "DEFCON 5",  # Passphrase to unlock global block
}
