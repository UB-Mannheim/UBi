import feedparser
from config import RSS_URL

def get_rss_items():
    feed = feedparser.parse(RSS_URL)
    if not feed.entries:
        return []
    return [(entry.title, entry.link) for entry in feed.entries[:7]]
