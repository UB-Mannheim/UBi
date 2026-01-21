# 🤖 UBi – Agentic AI-Chatbot of UB Mannheim

*UBi* is an agentic AI-powered assistant for the [Universitätsbibliothek Mannheim](https://www.bib.uni-mannheim.de), built with Chainlit and LangChain. It combines large language models (LLMs) with data from the library website to deliver context-aware answers.

## 🚀 Features

- [x] 🧭 **Agentic Router** – Dynamically detects language, augments user queries, and intelligently routes them to the most suitable tool
- [x] 🧠 **Semantic Augmentation** – Enhances questions with context to optimize semantic search and retrieval
- [x] 🔌 **Tool selector** – Routes queries to one of three specialized tools:
  - **📖 RAG Pipeline** – Retrieval-Augmented Generation using OpenAI embeddings, OpenAI inference, and OpenAI Cloud-based vectorstore
  - **📰 Library News Fetcher** – Retrieves the latest updates directly from the UB Mannheim blog
  - **🪑 Real-time Seat Availability** – Displays real-time information on study space availability at the library
- [x] 🌍 **Multilingual Support** – Detects and processes user input in multiple languages
- [x] 📝 **Feedback Collection** – Stores user questions, answers, and satisfaction ratings for continuous improvement
- [x] 📄 **Terms of Use Popup** – Ensures users accept terms before interaction
- [x] 🔐 **Optional Login System** – Supports password-protected access for restricted deployments

## 🛠 Tech Stack

| Component        | Technology                     |
|------------------|--------------------------------|
| Frontend UI      | [Chainlit](https://www.chainlit.io/) |
| Backend Logic    | Python + LangChain             |
| LLMs             | OpenAI                         |
| Embeddings       | OpenAI                         |
| Vector Database  | OpenAI                         |
| Deployment       | Docker + Docker Compose        |

## ⚙️ Native installation

### 1. Clone the repository

```bash
git clone https://github.com/UB-Mannheim/UBi.git
cd UBi/code
```

### 2. Move `.env.template` to `.env` and add your OpenAI API key

```env
OPENAI_API_KEY=sk-...
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. RAG Pipeline Options

You can choose between two ways of running the app:

1. Running the RAG pipeline **locally**
    - This option will embed all documents locally using the OpenAI embedding model `text-embedding-ada-002` and create a `chromadb` vectorstore.
2. Running the RAG pipeline with an **OpenAI vectorstore**
    - This option will create and upload all document to an [OpenAI vectorstore](https://platform.openai.com/docs/api-reference/vector-stores)

#### 4.1 Running the app with local RAG pipeline

##### Start the app

```bash
chainlit run app.py
```

##### Open the app

Open http://localhost:8000 in a browser.

#### 4.2 Running the app with an OpenAI vectorstore

##### Set `USE_OPENAI_VECTORSTORE='True'` in `.env`

```env
OPENAI_API_KEY=sk-...
USE_OPENAI_VECTORSTORE='True'
```

##### Start the app

```bash
chainlit run app.py
```

##### Open the app

Open http://localhost:8000 in a browser.

## 🐳 Docker Deployment

### 1. Move `.env.template` to `.env` and add your OpenAI API key

```env
OPENAI_API_KEY=sk-...
USE_OPENAI_VECTORSTORE='True' # Optional (for use with OpenAI vectorstore)
```

* Optionally, set the exposed TCP port using the environment variable `PORT` (default: 8000).

### 2. Build and run

```bash
docker-compose up --build
```

### 3. Use

Open http://localhost:8000 in a browser.

## 💬 Feedback Logging

All chats and feedback are stored in the database `data/feedback.db`:

| Field              | Description              |
|--------------------|--------------------------|
| session_id         | Random session ID        |
| question           | User input               |
| augmented_question | Augmented user input     |
| answer             | LLM-generated response   |
| timestamp          | UTC datetime             |
| feedback           | Score + optional comment |

You can view or export this data for improving the bot.

## License

This work is licensed under the MIT license (code) and Creative Commons Attribution 4.0 International license (for everything else). You are free to share and adapt the material for any purpose, even commercially, as long as you provide attribution.
