# 🤖 AIMA – Artificially Intelligent Mannheim Assistant

*AIMA* is an AI-powered assistant for the [Universitätsbibliothek Mannheim](https://www.bib.uni-mannheim.de), built with Chainlit and LangChain. It combines large language models (LLMs) with data from the library website to deliver context-aware answers.

## 🚀 Features

- [x] 🔎 **RAG Pipeline** – Retrieval-Augmented Generation using markdown sources scraped from the library website 
- [x] 📚 **Document Loader** – Loads and chunks library documents in markdown enriched with metadata
- [x] 💬 **LLM Integration** – Uses OpenAI models
- [x] 🧠 **Embeddings** – Uses OpenAI embedding models
- [x] 💾 **Chroma Vectorstore** – Local document storage and similarity search
- [x] 📰 **RSS Integration** – Fetches live updates from the UB Mannheim blog
- [x] 📝 **Feedback Storage** – Logs user questions, answers, and ratings
- [x] 🔐 **Login System** – _Optional_ password-based access
- [ ] 📄  **Terms of Use Popup** – Ensures legal compliance before interaction
- [ ] 🪑 **Real-time Seat Availability** – Displays up-to-date information on available study spaces
- [ ] 🔗 **Integration with Primo, MADOC, and MADATA APIs** – Search for scholarly publications, library holdings, and research data 


## 🛠 Tech Stack

| Component        | Technology                           |
|------------------|--------------------------------------|
| Frontend UI      | [Chainlit](https://www.chainlit.io/) |
| Backend Logic    | Python + LangChain                   |
| LLMs             | OpenAI                               |
| Embeddings       | OpenAI                               |
| Vector Database  | Chroma                               |
| DB (feedback)    | SQLite                               |
| Deployment       | Docker + Docker Compose              |

## ⚙️ Native installation

### 1. Clone the repository

```bash
git clone https://github.com/UB-Mannheim/AIMA.git
cd AIMA/code
```

### 2. Move `.env.template` to `.env` and add your OpenAI API key

```env
OPENAI_API_KEY=sk-...
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run locally

```bash
chainlit run app.py
```

### 5. Use

Open http://localhost:8000 in a browser.

## 🐳 Docker Deployment

### 1. Move `.env.template` to `.env` and add your OpenAI API key

```env
OPENAI_API_KEY=sk-...
```

Optionally, set the exposed TCP port using the environment variable `PORT` (default: 8000). 

### 2. Build and run

```bash
docker-compose up --build
```

### 3. Use

Open http://localhost:8000 in a browser.

## 💬 Feedback Logging

All chats and feedback are stored in the database `data/feedback.db`:

| Field        | Description                  |
|--------------|------------------------------|
| session_id   | Random session ID            |
| question     | User input                   |
| answer       | LLM-generated response       |
| timestamp    | UTC datetime                 |
| feedback     | Score + optional comment     |

You can view or export this data for improving the bot.

## License

This work is licensed under the MIT license (code) and Creative Commons Attribution 4.0 International license (for everything else). You are free to share and adapt the material for any purpose, even commercially, as long as you provide attribution.
