import json
import os

from langchain_openai import ChatOpenAI
from tqdm import tqdm

# Initialize ChatOpenAI LLM
llm = ChatOpenAI(
    model_name="gpt-4o-mini-2024-07-18",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
)


# Build a single-prompt to generate all Q&A from markdown
def generate_qa_from_markdown(md_text):
    prompt = f'''
Du bist ein hilfsbereiter Assistent. Deine Aufgabe ist es, aus dem folgenden Markdown-Inhalt strukturierte Frage-Antwort-Paare zu generieren.

Anweisungen:
- Identifiziere zu jedem Abschnitt (beginnend mit "###") genau ein Thema.
- Erstelle pro Thema genau eine präzise Frage und eine ausführliche, sachliche Antwort.
- Wenn im Titel des Abschnitts eine URL angegeben ist, verwende diese als Quelle am Ende der Antwort.
- Wenn keine URL vorhanden ist, verwende stattdessen die erste im Dokument gefundene URL.
- Hänge an jede Antwort am Ende die Quelle im Format "Quelle: URL" an.
- Am Ende sollen deine generierten Fragen und Antworten den gesamten Inhalt des Eingabetextes vollständig abdecken.

Markdown-Inhalt:
"""
{md_text}
"""

Antwort nur im folgenden JSON-Format:
[
  {{
    "question": "Deine Frage?",
    "answer": "Deine ausführliche Antwort.\n\nQuelle: URL"
  }},
  ...
]
'''
    response = llm.invoke(prompt)
    try:
        return json.loads(response.content)
    except Exception as e:
        print("❌ Fehler beim Parsen der Antwort:", e)
        return []


# Process all markdown files in a directory
def process_all_markdown_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    md_files = [f for f in os.listdir(input_dir) if f.endswith(".md")]

    for filename in tqdm(md_files):
        md_path = os.path.join(input_dir, filename)
        print(f"🔍 Verarbeite {md_path} ...")

        with open(md_path, "r", encoding="utf-8") as file:
            md_text = file.read()

        qa_pairs = generate_qa_from_markdown(md_text)

        out_path = os.path.join(output_dir, filename.replace(".md", ".json"))
        with open(out_path, "w", encoding="utf-8") as out_file:
            json.dump(qa_pairs, out_file, indent=2, ensure_ascii=False)

        print(
            f"✅ {len(qa_pairs)} Frage-Antwort-Paare gespeichert in {out_path}."
        )


# Entry point
if __name__ == "__main__":
    input_dir = "../data/markdown"
    output_dir = "../data/json"
    process_all_markdown_files(input_dir, output_dir)
