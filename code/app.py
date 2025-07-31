# === Imports ===
import datetime
import os
import chainlit as cl
from chainlit import Message
from fastapi import Request, Response
from dotenv import load_dotenv
from typing import Optional
from config import ENV_PATH
from conversation_memory import (
    MessageRole,
    create_conversation_context,
    session_memory,
)
from custom_data_layer import CustomDataLayer
from db import save_interaction
from dotenv import load_dotenv
from fastapi import Request, Response

# from website_search import search_ub_website
from free_seats import get_occupancy_data, make_plotly_figure
from html_template_modifier import main as modify_html_template
from llm_query_processing import route_and_augment_query
from phrase_detection import detect_common_phrase
from prompts import BASE_SYSTEM_PROMPT
from rich import print
from rss_reader import get_rss_items
from session_stats import check_session_warnings, get_session_usage_message
from terms_conditions import ask_terms_acceptance, check_terms_accepted
from translations import translate

# === .env Configuration ===
load_dotenv(ENV_PATH)
USE_OPENAI_VECTORSTORE = (
    True if os.getenv("USE_OPENAI_VECTORSTORE") == "True" else False
)
DEBUG = True if os.getenv("DEBUG") == "True" else False

# === Conditional Imports RAG Pipelines (local / OpenAI) ===
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
    print(
        f"[bold]🔗 AIMA is running with OpenAI vectorstore: {OPENAI_VECTORSTORE_ID}"
    )

# === Initialize HTML Template ===
# Modify Chainlit's HTML template to use local assets
try:
    modify_html_template()
except Exception as e:
    print(f"[bold]Warning: Could not modify HTML template: {e}")

# === Authentication (optional) ===
users = [
    cl.User(
        identifier="1",
        display_name="Admin",
        metadata={"username": "admin", "password": "admin"},
    )
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
            message="Welche Bibliotheksbereiche der UB Mannheim haben jetzt geöffnet? Gib mir eine Übersicht über alle Öffnungszeiten der Bibliotheksbereiche und einen Link zur Öffnungszeiten-Webseite.",
        ),
        cl.Starter(
            label="Sitzplätze",
            message="Gibt es aktuell freie Sitzplätze in der Bibliothek?",
        ),
        cl.Starter(
            label="Services",
            message="Liste alle Dienstleistungen und Services der UB Mannheim für Studierende und Forschende auf.",
        ),
        cl.Starter(
            label="Standorte",
            message="Gib mir eine Liste aller Standorte der UB Mannheim mit ihrer fachlichen Ausrichtung und dem Webseitenlink in Klammern.",
        ),
        cl.Starter(
            label="Neuigkeiten",
            message="Was für Neuigkeiten gibt es aus der UB Mannheim?",
        ),
    ]


# === System Prompt for OpenAI Vectorstore Option ===
def get_instructions(language="German"):
    today = datetime.datetime.now().strftime("%B %d, %Y")
    prompt = BASE_SYSTEM_PROMPT.format(today=today)
    return prompt.replace("{language}", language)

# === OpenAI Vectorstore Logic ===
async def handle_openai_vectorstore_query(
    client: AsyncOpenAI,
    chat_history: Optional[list[dict[str, str]]],
    augmented_input: str,
    detected_language: str,
    msg: cl.Message,
    session_id: str,
    user_input: str
    ):
    """
    Handle queries using OpenAI vectorstore
    """
    if chat_history:
        # Append new message to chat_history
        new_chat_message = {"role": "user", "content": augmented_input}
        chat_history.append(new_chat_message)
    else:
        # Start new chat_history
        chat_history = [{"role": "user", "content": augmented_input}]
    
    if DEBUG:
        print(f"💬 Chat history: {chat_history}")
 
    full_answer = ""
    try:
        stream = await client.responses.create(
            model="gpt-4o-mini-2024-07-18",
            input=chat_history,
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
        error_response = f"{translate('openai_api_error', detected_language)}: {e}"
        await msg.stream_token("")
        for char in error_response:
            await msg.stream_token(char)
        await msg.update()

        # Add error to memory
        session_memory.add_turn(session_id, MessageRole.USER, user_input)
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, error_response)
        await save_interaction(session_id, user_input, error_response, augmented_input)
        return False, error_response

    if full_answer:
        await msg.update()
    else:
        error_response = f"{translate('response_error', detected_language)}"
        await msg.stream_token("")
        for char in error_response:
            await msg.stream_token(char)
        await msg.update()
        return False, error_response

    # Save interaction
    session_memory.add_turn(session_id, MessageRole.ASSISTANT, full_answer)
    await save_interaction(session_id, user_input, full_answer, augmented_input)
    return True, full_answer

# === Local RAG Logic ===
async def handle_local_rag_query(
    chat_history: Optional[list[dict[str, str]]],
    augmented_input: str,
    detected_language: str,
    msg: cl.Message,
    session_id: str,
    user_input: str
    ):
    """
    Handle queries using local RAG chain
    """
    rag_chain = cl.user_session.get("rag_chain")
    if not rag_chain:
        rag_chain = await create_rag_chain(debug=DEBUG)
        cl.user_session.set("rag_chain", rag_chain)
    
    try:
        # Convert conversation context list to string format for the RAG chain
        if chat_history:
            context_string = "\n".join([f"{msg['role']}: {msg['content']}" for msg in chat_history])
        else:
            context_string = ""

        response_generator = rag_chain.astream({
            "question": augmented_input,
            "conversation_context": context_string,
            "language": detected_language
        })

        # Stream response
        full_response = ""
        async for token in response_generator:
            await msg.stream_token(token)
            full_response += token
        await msg.update()

        # Add assistant response to memory
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, full_response)
        await save_interaction(session_id, user_input, full_response, augmented_input)
        return True, full_response

    except Exception as e:
        error_response = f"{translate('local_rag_error', detected_language)}: {str(e)}"
        await msg.stream_token("")
        for char in error_response:
            await msg.stream_token(char)
        await msg.update()

        # Add error to memory
        session_memory.add_turn(session_id, MessageRole.USER, user_input)
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, error_response)
        await save_interaction(session_id, user_input, error_response, augmented_input)
        return False, error_response

# === News Route ===
async def handle_news_route(
    detected_language: str,
    msg: cl.Message,
    session_id: str,
    user_input: str
    ):
    """
    Handle news/neuigkeiten route
    """
    items = get_rss_items()        
    if not items:
        response = translate("no_news_found", detected_language)
    else:
        heading = translate("news_heading", detected_language)
        body = "\n\n".join(f"- **{title}**\n  {link}" for title, link, _ in items)
        response = heading + body

    # Clear the message and stream the response
    await msg.stream_token("")
    for char in response:
        await msg.stream_token(char)
    await msg.update()

    # Add to memory
    session_memory.add_turn(session_id, MessageRole.USER, user_input)
    session_memory.add_turn(session_id, MessageRole.ASSISTANT, response)
    await save_interaction(session_id, user_input, response)
    return response

# === Sitzplatz Route ===
async def handle_sitzplatz_route(
    detected_language: str,
    msg: cl.Message,
    session_id: str,
    user_input: str
    ):
    """
    Handle sitzplatz/free seats route
    """
    try:
        data = get_occupancy_data()
        areas = data["areas"]

        # Plot title and labels
        heading = translate("seats_last_updated", detected_language)
        response = f"{heading}: {data['lastupdated']}"
        plot_label = translate("library_capacity", detected_language)

        # Generate the plot
        fig = make_plotly_figure(areas, detected_language)

        # Update the existing message with content and add elements
        await msg.stream_token("")
        for char in response:
            await msg.stream_token(char)

        # Set the elements on the existing message
        msg.elements = [cl.Plotly(name=plot_label, figure=fig, display="inline", size="large")]
        await msg.update()

        # Add to memory
        session_memory.add_turn(session_id, MessageRole.USER, user_input)
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, response+f" Data:{data}")
        await save_interaction(session_id, user_input, response)
        return response
    except Exception as e:
        error_response = f"{translate('seats_error', detected_language)}: {str(e)}"
        await msg.stream_token("")
        for char in error_response:
            await msg.stream_token(char)
        await msg.update()

        # Add to memory
        session_memory.add_turn(session_id, MessageRole.USER, user_input)
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, error_response)
        await save_interaction(session_id, user_input, error_response)
        return error_response

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
        rag_chain = await create_rag_chain(debug=DEBUG)
        cl.user_session.set("rag_chain", rag_chain)


# === Chat Message Handler ===
@cl.on_message
async def on_message(message: cl.Message):
    session_id = cl.user_session.get("session_id") or "unknown"

    # Get message content and session_id
    user_input = message.content.strip()

    # Check if Terms of Use are accepted
    terms_accepted = check_terms_accepted()
    if not terms_accepted:
        await ask_terms_acceptance()
        return

    # Check rate limits
    allowed, error_message = session_memory.check_rate_limits(
        session_id, user_input
    )
    if not allowed:
        await cl.Message(
            content=error_message or "Rate limit exceeded", author="assistant"
        ).send()
        return

    # Record the request if it passes all checks
    session_memory.record_request(session_id, user_input)

    # Session stats
    if user_input.lower() == "session stats":
        stats_message = get_session_usage_message(session_id)
        await cl.Message(content=stats_message, author="assistant").send()

        # Check for warnings
        warning = check_session_warnings(session_id)
        if warning:
            await cl.Message(content=warning, author="assistant").send()
        return

    # Catch common phrases
    phrase_result = detect_common_phrase(user_input)
    if phrase_result:
        response, _ = phrase_result
        await Message(content=response, author="assistant").send()

        # Add to memory
        session_memory.add_turn(session_id, MessageRole.USER, user_input)
        session_memory.add_turn(session_id, MessageRole.ASSISTANT, response)
        await save_interaction(session_id, user_input, response)
        return

    # Create chat message
    msg = cl.Message(content="", author="assistant")
    await msg.send()
    await msg.stream_token(" ")

    # === LLM Router ===
    detected_language, route, augmented_input = await route_and_augment_query(
        client if USE_OPENAI_VECTORSTORE else None, user_input, debug=DEBUG
    )

    # "News" Route
    if route and route.lower() == "news":
        await handle_news_route(detected_language, msg, session_id, user_input)
        return

    # "Free seats" Route
    if route and route.lower() == "sitzplatz":
        await handle_sitzplatz_route(detected_language, msg, session_id, user_input)
        return

    # Build chat_history with previous conversation context
    chat_history = create_conversation_context(session_id)

    # Add user message to memory (after getting context)
    session_memory.add_turn(session_id, MessageRole.USER, user_input)

    # === OpenAI Vectorstore Logic ===
    if USE_OPENAI_VECTORSTORE:
        success, response = await handle_openai_vectorstore_query(
            client,
            chat_history,
            augmented_input,
            detected_language,
            msg,
            session_id,
            user_input
        )
        if not success:
            return

    # === Local RAG Logic ===
    else:
        success, response = await handle_local_rag_query(
            chat_history,
            augmented_input,
            detected_language,
            msg,
            session_id,
            user_input
        )
        if not success:
            return

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
