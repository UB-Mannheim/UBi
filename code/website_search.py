import html

import requests
from bs4 import BeautifulSoup


def search_ub_website(query: str, max_results: int = 5) -> str:
    url = f"https://www.bib.uni-mannheim.de/suche/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "Die Websuche ist derzeit nicht verfügbar."
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.select("div.uma-search-result")

    entries = []
    for result in results[:max_results]:
        title = result.select_one(".uma-search-result-title h3")
        link = result.find("a", href=True)
        preview = result.select_one(".uma-search-result-preview-text")
        if title and link:
            preview_text = html.unescape(preview.text.strip()) if preview else ""
            entries.append(f"- **[{title.text.strip()}](https://www.bib.uni-mannheim.de{link['href']})**\n  {preview_text[:200]}...")
    return "\n\n".join(entries) if entries else "Keine passenden Ergebnisse auf der Website gefunden."
