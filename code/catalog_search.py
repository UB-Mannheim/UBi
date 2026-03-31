import httpx
from typing import Optional

VUFIND_BASE = "https://disco.bib.uni-mannheim.de/vufind"  # Ihre VuFind-URL anpassen

async def search_catalog(query: str, limit: int = 5) -> Optional[str]:
    """Sucht im VuFind-Katalog und gibt formatierten Markdown-Text zurück."""
    try:
        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.get(
                f"{VUFIND_BASE}/api/v1/search",
                params={
                    "lookfor": query,
                    "type":    "AllFields",
                    "limit":   limit,
                    "field[]": ["title", "author", "publishDate", "id", "format"],
                }
            )
        records = resp.json().get("records", [])
        if not records:
            return None

        lines = []
        for r in records:
            title  = r.get("title", "Kein Titel")
            author = r.get("author", "")
            year   = (r.get("publishDate") or [""])[0]
            fmt    = (r.get("format")      or [""])[0]
            url    = f"{VUFIND_BASE}/Record/{r.get('id', '')}"
            meta   = " · ".join(filter(None, [author, year, fmt]))
            lines.append(f"- **{title}**  \n  {meta}  \n  {url}")

        return "\n\n".join(lines)
    except Exception:
        return None
