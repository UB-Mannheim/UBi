from __future__ import annotations

import json
import os
import re
import json_repair
from openai import AsyncOpenAI
from prompts import ROUTER_AUGMENTOR_PROMPT
from utils import (
    is_valid_json,
    set_quiet_mode,
    print_info,
    print_err
)


def _openai_key_is_set() -> bool:
    key = os.getenv("OPENAI_API_KEY", "").strip()
    return bool(key) and key != "sk-"


async def route_and_augment_query(
    client: AsyncOpenAI | None,
    user_input: list[dict],
    model: str = os.getenv("ROUTER_MODEL", "gpt-4.1-nano-2025-04-14"),
    quiet: bool = False,
) -> tuple[str, str, str]:
    """
    Function to route, detect the language and augment a user's query.
    There are 3 possible routes: 'news', 'sitzplatz', or 'message'.
    The function returns a tuple: (language, route, augmented_query).
    Handles malformed/missing JSON keys, partial fallbacks, and better
    error/debug output.

    If parsing fails the function will fallback to:
        ("German", "message", user_input[-1]["content"])
    """
    # Set quiet mode
    if quiet:
        set_quiet_mode(True)

    # When no OpenAI key is configured, fall back to a local Ollama model
    if not _openai_key_is_set() and client is None:
        try:
            from langchain_ollama import ChatOllama
        except ImportError as exc:
            raise ImportError(
                "langchain-ollama is required when OPENAI_API_KEY is not set. "
                "Install it with: pip install langchain-ollama"
            ) from exc

        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        ollama_model = os.getenv("OLLAMA_MODEL", "llama3.2")
        ollama_client = ChatOllama(
            model=ollama_model,
            base_url=ollama_base_url,
            temperature=0,
        )
        try:
            from langchain_core.messages import HumanMessage, SystemMessage
            messages = [SystemMessage(content=ROUTER_AUGMENTOR_PROMPT)]
            for msg in user_input:
                if msg.get("role") == "user":
                    messages.append(HumanMessage(content=msg["content"]))
            response = await ollama_client.ainvoke(messages)
            json_str = response.content.strip() if response.content else ""
            try:
                json_str = re.sub(
                    r"```json\s*", "", json_str, flags=re.IGNORECASE
                )
                json_str = re.sub(r"```\s*", "", json_str)
                json_str = json_repair.repair_json(json_str)
                if is_valid_json(json_str):
                    json_data = json.loads(json_str)
                    language = json_data.get("language", "German")
                    category = json_data.get("category", "message")
                    augmented_query = json_data.get("augmented_query") or user_input[-1]["content"]
                    print_info("🚦 [bold]LLM Router classified and augmented query:")
                    last_content = user_input[-1]["content"] if user_input else ""
                    print_info(f"   - Query: {last_content}")
                    print_info(f"   - Detected Language: {language}")
                    print_info(f"   - Detected Route Category: {category}")
                    print_info(f"   - Augmented Query: {augmented_query}")
                    return language, category, augmented_query
                else:
                    print_err("⚠️  LLM response is not valid JSON. Returning fallback.")
            except Exception as e:
                print_err(f"⚠️  Warning: Could not parse response json: {e}")
        except Exception as e:
            print_err(f"⚠️  Warning: Could not route query via Ollama: {e}")
        return ("German", "message", user_input[-1]["content"])

    if not client:
        client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": ROUTER_AUGMENTOR_PROMPT},
            ] + user_input,
            temperature=0,
            service_tier="priority",
        )

        if response.choices and response.choices[0].message.content:
            json_str = response.choices[0].message.content.strip()
            try:
                # Remove any trailing Markdown code block markers (```json and ```)
                json_str = re.sub(
                    r"```json\s*", "", json_str, flags=re.IGNORECASE
                )
                json_str = re.sub(r"```\s*", "", json_str)

                # Repair other json errors
                json_str = json_repair.repair_json(json_str)

                # Check if a valid json is now available
                if is_valid_json(json_str):
                    json_data = json.loads(json_str)
                    language = json_data.get("language", "German")
                    category = json_data.get("category", "message")
                    augmented_query = json_data.get("augmented_query") or user_input[-1]["content"]
                    print_info(
                        "🚦 [bold]LLM Router classified and augmented query:"
                    )
                    print_info(f"   - Query: {user_input[-1]['content']}")
                    print_info(f"   - Detected Language: {language}")
                    print_info(f"   - Detected Route Category: {category}")
                    print_info(f"   - Augmented Query: {augmented_query}")
                    return language, category, augmented_query
                else:
                    print_err(
                        "⚠️  LLM response is not valid JSON. Returning fallback."
                    )
            except Exception as e:
                print_err(f"⚠️  Warning: Could not parse response json: {e}")
        else:
            print_err("⚠️  No content in LLM response. Returning fallback.")
        return ("German", "message", user_input[-1]["content"])
    except Exception as e:
        print_err(f"⚠️  Warning: Could not route query: {e}")
        return ("German", "message", user_input[-1]["content"])
