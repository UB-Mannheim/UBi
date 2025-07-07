import os
import datetime
import chainlit as cl
from rich import print
from chainlit import Message
from fastapi import Request, Response
from dotenv import load_dotenv
from config import ENV_PATH
from db import save_interaction
from rss_reader import get_rss_items
from custom_data_layer import CustomDataLayer
from terms_conditions import ask_terms_acceptance, check_terms_accepted
from free_seats import get_occupancy_data, make_plotly_figure
from conversation_memory import session_memory, MessageRole, create_conversation_context
from language_detection import detect_language_and_get_name

# === .env Configuration ===
load_dotenv(ENV_PATH)
USE_OPENAI_VECTORSTORE = True if os.getenv("USE_OPENAI_VECTORSTORE") == "True" else False

# === RAG / OpenAI Pipeline Chooser ===
if USE_OPENAI_VECTORSTORE:
    from openai import AsyncOpenAI
    from rag_openai import initialize_vectorstore
else:
    from rag_local import create_rag_chain

# === OpenAI Vectorstore Initialization ===
if USE_OPENAI_VECTORSTORE:
    initialize_vectorstore()
    OPENAI_VECTORSTORE_ID = os.getenv("OPENAI_VECTORSTORE_ID")
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    print(f'[bold]🔗 AIMA is running with OpenAI vectorstore: {OPENAI_VECTORSTORE_ID}')

# === Authentication (optional) ===
users = [
    cl.User(identifier="1", display_name="Admin", 
            metadata={"username": "admin", "password": "admin"})
]

# === Data Layer ===
@cl.data_layer
def get_data_layer():
    return CustomDataLayer()

# === Starter Buttons ===
@cl.set_starters
async def set_starters(user=None):
    return [
        cl.Starter(
            label="Öffnungszeiten", 
            message="Ist die Bibliothek jetzt geöffnet?"),
        cl.Starter(
            label="Sitzplätze", 
            message="Gibt es aktuell freie Sitzplätze in der Bibliothek?"),
        cl.Starter(
            label="Services", 
            message="Liste alle Dienstleistungen an der UB Mannheim auf"),
        cl.Starter(label="Standorte", message="Standorte der UB Mannheim"),
        cl.Starter(label="Neuigkeiten", message="Neues aus der UB"),
    ]

# === System Prompt for OpenAI Vectorstore Option ===
def get_instructions(detected_language=None):
    today = datetime.datetime.now().strftime('%B %d, %Y')
    time = datetime.datetime.now().strftime('%H:%M:%S')
    return f"""Du bist der virtuelle Assistent der Universitätsbibliothek Mannheim. Freundlich, kompetent und unterstützend beantwortest du Fragen zur Nutzung der Bibliothek, zu Services, Recherchemöglichkeiten und mehr.
**Regeln:**
1. Nutze nur die bereitgestellten Daten.
2. Keine externen Inhalte, wenn Kontext fehlt.
3. Antworten max. 300 Token lang.
4. Wenn du etwas nicht weißt, verweise auf den UB-Chat (Mo–Fr, 10–18 Uhr): https://www2.bib.uni-mannheim.de/mibew/index.php/chat?locale=de
5. Keine Annahmen, Erfindungen oder Fantasie-URLs.
6. Keine Buchempfehlungen – verweise stattdessen auf die Primo-Suche: https://primo.bib.uni-mannheim.de
7. Keine Paperempfehlungen - verweise stattdessen auf die MADOC-Suche: https://madoc.bib.uni-mannheim.de
8. Keine Datenempfehlungen - verweise stattdessen auf die MADATA-Suche: https://madata.bib.uni-mannheim.de
9. Schließe mit einer passenden Quell-URL.
10. Antworte auf: {detected_language}.
11. Heute ist {today} und die Uhrzeit ist {time}. Beachte dies, wenn ein Nutzer nach Öffnungszeiten fragt. Verweise auf: https://www.bib.uni-mannheim.de/oeffnungszeiten"""

# === Chat Start: Initialize Session Memory and Terms ===
@cl.on_chat_start
async def on_chat_start():
    session_id = cl.user_session.get("id") or "unknown"
    cl.user_session.set("session_id", session_id)
    
    # Check if terms are accepted
    terms_accepted = check_terms_accepted()
    
    if not terms_accepted:
        await ask_terms_acceptance()
        # Don't proceed until terms are accepted
        return
    
    # Clear any existing session memory for this user
    session_memory.clear_session(session_id)
    
    # If using RAG, load the chain
    if not USE_OPENAI_VECTORSTORE:
        rag_chain = await create_rag_chain()
        cl.user_session.set("rag_chain", rag_chain)

# === Chat Message Handler ===
@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content.strip()
    session_id = cl.user_session.get("session_id") or "unknown"
    
    terms_accepted = check_terms_accepted()
    
    if not terms_accepted:
        await ask_terms_acceptance()
        return
    
    # RSS feed
    news_keywords = ["news", "neues", "neuigkeiten", "aktuelles", "nachrichten"]
    if any(keyword in user_input.lower() for keyword in news_keywords):
        items = get_rss_items()
        if not items:
            response = "Keine Neuigkeiten gefunden."
            await Message(content=response).send()
        else:
            response = "\n\n".join(f"- **{title}**\n  {link}" for title, link in items)
            await Message(content=response).send()

        # Add to memory
        session_memory.add_turn(session_id, MessageRole.USER, user_input)
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, response)
        await save_interaction(session_id, user_input, response)
        return
    
    # Free seats
    seat_keywords = ["sitzplatz", "sitzplätze", "arbeitsplatz", "arbeitsplätze", "arbeitsplätzen",
                     "plätze", "freier platz", "freie plätze", "seats", "workspaces"]
    if any(keyword in user_input.lower() for keyword in seat_keywords):
        try:
            data = get_occupancy_data()
            areas = data["areas"]
            fig = make_plotly_figure(areas)
            response = f"📅 Zuletzt aktualisiert: {data['lastupdated']}"
            
            await cl.Message(
                content=response,
                elements=[
                    cl.Plotly(name="Bibliotheksauslastung", figure=fig, display="inline", size="large")
                ]
            ).send()
            
            # Add to memory
            session_memory.add_turn(session_id, MessageRole.USER, user_input)
            session_memory.add_turn(session_id, MessageRole.ASSISTANT, response+f" Data:{data}")
            await save_interaction(session_id, user_input, response)
        except Exception as e:
            error_response = f"❌ Fehler beim Abrufen der Sitzplatzdaten: {str(e)}"
            await cl.Message(content=error_response).send()
            
            # Add to memory
            session_memory.add_turn(session_id, MessageRole.USER, user_input)
            session_memory.add_turn(session_id, MessageRole.ASSISTANT, error_response)
            await save_interaction(session_id, user_input, error_response)
        return
    
    # Add user message to memory
    session_memory.add_turn(session_id, MessageRole.USER, user_input)
    
    # Detect language
    detected_language = detect_language_and_get_name(user_input)
    
    # Build conversation context
    conversation_context = create_conversation_context(session_id)
    
    if USE_OPENAI_VECTORSTORE:
        # Compose input for the model: prepend context if available
        if conversation_context:
            model_input = f"{conversation_context}\nNutzer: {user_input}"
        else:
            model_input = user_input
        msg = cl.Message(content="", author="assistant")
        await msg.send()
        await msg.stream_token(" ")
        full_answer = ""
        try:
            stream = await client.responses.create(
                model="gpt-4o-mini-2024-07-18",
                input=[{"role": "user", "content": model_input}],
                tools=[{
                    "type": "file_search",
                    "vector_store_ids": [OPENAI_VECTORSTORE_ID],
                    "max_num_results": 6
                }],
                instructions=get_instructions(detected_language),
                stream=True,
                temperature=0
            )
            async for event in stream:
                if event.type == 'response.output_text.delta' and event.delta:
                    token = event.delta
                    await msg.stream_token(token)
                    full_answer += token
        except Exception as e:
            await cl.Message(content=f"An error occurred while using the Responses API: {e}").send()
            return
        if full_answer:
            await msg.update()
        else:
            await cl.Message(content="Sorry, I could not retrieve a response.").send()
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, full_answer)
        await save_interaction(session_id, user_input, full_answer)
    else:
        # RAG chain logic
        rag_chain = cl.user_session.get("rag_chain")
        if not rag_chain:
            rag_chain = await create_rag_chain()
            cl.user_session.set("rag_chain", rag_chain)
        try:
            # Get conversation context
            response_generator = rag_chain.astream({
                "question": user_input,
                "conversation_context": conversation_context,
                "language": detected_language
            })

            # Stream response
            full_response = ""
            msg = Message(content="", author="assistant")
            async for token in response_generator:
                await msg.stream_token(token)
                full_response += token
            await msg.send()

            # Add assistant response to memory
            session_memory.add_turn(session_id, MessageRole.ASSISTANT, full_response)
            await save_interaction(session_id, user_input, full_response)

        except Exception as e:
            error_response = f"❌ Fehler bei der Verarbeitung: {str(e)}"
            await Message(content=error_response).send()

            # Add error to memory
            session_memory.add_turn(session_id, MessageRole.USER, user_input)
            session_memory.add_turn(session_id, MessageRole.ASSISTANT, error_response)
            await save_interaction(session_id, user_input, error_response)

        # Optional: fallback to web search
        # fallback = search_ub_website(user_input)
        # await Message(
        #     content=f"Ich konnte nichts Genaues finden. "
        #             f"Ergebnisse von der UB-Website:\n\n{fallback}"
        # ).send()
        # await save_interaction(session_id, user_input, fallback)

# === Chat End ===
@cl.on_chat_end
async def on_chat_end():
    session_id = cl.user_session.get("session_id")
    if session_id:
        # End session and clear memory
        session_memory.end_session(session_id)

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