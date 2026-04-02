import json
import httpx
from typing import Optional

VUFIND_BASE = "https://disco.bib.uni-mannheim.de/vufind"  # Adjust to your VuFind URL

async def search_catalog(query: dict | str, limit: int = 5) -> Optional[str]:
    """Search the VuFind catalog and return formatted Markdown text.

    The ``query`` parameter can be either:
    - A dict with VuFind API parameters (``lookfor``, ``type``, optional ``filter``)
    - A JSON string that can be parsed into a dict
    - A plain search string
    """
    try:
        # Parse structured VuFind parameters
        if isinstance(query, dict):
            # Direct dict object (new format from router)
            params_json = query
            lookfor = params_json.get("lookfor", "")
            search_type = params_json.get("type", "AllFields")
            filters = params_json.get("filter", [])
        elif isinstance(query, str):
            # Try parsing as JSON string, fall back to plain string
            try:
                params_json = json.loads(query)
                lookfor = params_json.get("lookfor", query)
                search_type = params_json.get("type", "AllFields")
                filters = params_json.get("filter", [])
            except (json.JSONDecodeError, TypeError):
                # Plain search string
                lookfor = query
                search_type = "AllFields"
                filters = []
        else:
            # Fallback
            lookfor = str(query)
            search_type = "AllFields"
            filters = []

        params = {
            "lookfor": lookfor,
            "type":    search_type,
            "limit":   limit,
            "field[]": ["title", "author", "publishDate", "id", "format"],
        }
        if filters:
            params["filter[]"] = filters

        async with httpx.AsyncClient(timeout=8.0) as client:
            resp = await client.get(
                f"{VUFIND_BASE}/api/v1/search",
                params=params,
            )
        records = resp.json().get("records", [])
        if not records:
            return None

        lines = []
        for r in records:
            title  = r.get("title", "No title")
            author = r.get("author", "")
            year   = (r.get("publishDate") or [""])[0]
            fmt    = (r.get("format")      or [""])[0]
            url    = f"{VUFIND_BASE}/Record/{r.get('id', '')}"
            meta   = " · ".join(filter(None, [author, year, fmt]))
            lines.append(f"- **{title}**  \n  {meta}  \n  {url}")

        return "\n\n".join(lines)
    except Exception:
        return None
