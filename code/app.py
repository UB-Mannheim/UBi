import chainlit as cl
from chainlit import Message
from fastapi import Request, Response
from db import save_interaction
from rag_pipeline import create_rag_chain
from rss_reader import get_rss_items
from custom_data_layer import CustomDataLayer
# from website_search import search_ub_website


# === Authentication (optional) ===
users = [
    cl.User(identifier="1", display_name="Admin", metadata={"username": "admin", "password": "admin"})
]

# === Data Layer ===
@cl.data_layer
def get_data_layer():
    return CustomDataLayer()

# === Starter Buttons ===
@cl.set_starters
async def set_starters():
    return [
        cl.Starter(label="Öffnungszeiten", message="Ist die Bibliothek jetzt geöffnet?"),
        cl.Starter(label="Sitzplätze", message="Gibt es aktuell freie Sitzplätze in der Bibliothek?"),
        cl.Starter(label="Services", message="Liste alle Dienstleistungen an der UB Mannheim auf"),
        cl.Starter(label="Standorte", message="Standorte der UB Mannheim"),
        cl.Starter(label="Neuigkeiten", message="Neues aus der UB"),
    ]

# === Chat Start: Load RAG Pipeline ===
@cl.on_chat_start
async def on_chat_start():
    rag_chain = await create_rag_chain()
    cl.user_session.set("chain", rag_chain)

# === Chat Message Handler ===
@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content.strip()
    session_id = cl.user_session.get("id") or "unknown"
    cl.user_session.set("session_id", session_id)

    # Special command: RSS feed
    if user_input.lower() == "neues aus der ub":
        items = get_rss_items()
        if not items:
            await Message(content="Keine Neuigkeiten gefunden.").send()
        else:
            news = "\n\n".join(f"- **{title}**\n  {link}" for title, link in items)
            await Message(content=news).send()
            await save_interaction(session_id, user_input, news)
        return

    # RAG Response
    rag_chain = cl.user_session.get("chain")
    full_answer = ""
    msg = Message(content="", author="assistant", metadata={"session_id": session_id})
    async for token in rag_chain.astream(user_input):
        await msg.stream_token(token)
        full_answer += token
    await msg.send()
    await save_interaction(session_id, user_input, full_answer)

    # Optional: fallback to web search
    # fallback = search_ub_website(user_input)
    # await Message(content=f"Ich konnte nichts Genaues finden. Ergebnisse von der UB-Website:\n\n{fallback}").send()
    # await save_interaction(session_id, user_input, fallback)

# === Chat End ===
@cl.on_chat_end
async def on_chat_end():
    print("User disconnected.")

# === Logout ===
@cl.on_logout
def on_logout(request: Request, response: Response):
    for cookie_name in request.cookies.keys():
        response.delete_cookie(cookie_name)

# === Optional: Password Auth ===
# @cl.password_auth_callback
# def on_login(username: str, password: str) -> Optional[cl.User]:
#     for user in users:
#         if user.metadata["username"] == username and user.metadata["password"] == password:
#             return user
#     return None
