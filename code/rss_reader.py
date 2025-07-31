import feedparser
from config import RSS_URL


def get_rss_items():
    feed = feedparser.parse(RSS_URL)
    if not feed.entries:
        return []
    return [
        (
            entry.title,
            entry.link,
            [tag["term"] for tag in entry.tags]
        )
        for entry in feed.entries[:7]
        if hasattr(entry, "tags") and any(tag["term"] == "Topmeldungen" for tag in entry.tags)
    ]
