import os
import re
import json
import json_repair
from rich import print
from openai import AsyncOpenAI
from prompts import ROUTER_AUGMENTOR_PROMPT


def is_valid_json(json_string):
    """
    Check if json_string is valid JSON.
    """
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError as e:
        print(f"... Invalid JSON: {e}")
        return False

async def route_and_augment_query(
    client: AsyncOpenAI | None,
    user_input: str,
    model: str = "gpt-4.1-nano-2025-04-14",
    debug: bool = False
) -> tuple[str, str, str]:
    """
    Function to route, detect the language and augment a user's query. 
    There are 3 possible routes: 'news', 'sitzplatz', or 'message'.
    The function returns a tuple: (language, route, augmented_query).
    Handles malformed/missing JSON keys, partial fallbacks, and better 
    error/debug output.
    
    If parsing fails the function will fallback to: 
        ("German", "message", user_input)
    """
    if not client:
        client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": ROUTER_AUGMENTOR_PROMPT},
                {"role": "user", "content": f"User query: '{user_input}'"}
            ],
            temperature=0
        )
        
        if response.choices and response.choices[0].message.content:
            json_str = response.choices[0].message.content.strip()
            try:
                # Remove any trailing Markdown code block markers (```json and ```)
                json_str = re.sub(r"```json\\s*", '', json_str, flags=re.IGNORECASE)
                json_str = re.sub(r"```\\s*", '', json_str)
                
                # Repair other json errors
                json_str = json_repair.repair_json(json_str)
            
                # Check if a valid json is now available
                if is_valid_json(json_str):
                    json_data = json.loads(json_str)
                    language = json_data.get('language', 'German')
                    category = json_data.get('category', 'message')
                    augmented_query = json_data.get('augmented_query', user_input)
                    if debug:
                        print(f"🚦 [bold]LLM Router classified and augmented query:")
                        print(f"   - Query: {user_input}")
                        print(f"   - Detected Language: {language}")
                        print(f"   - Detected Route Category: {category}")
                        print(f"   - Augmented Query: {augmented_query}")
                    return language, category, augmented_query
                else:
                    if debug:
                        print(f"⚠️  LLM response is not valid JSON. Returning fallback.")
            except Exception as e:
                if debug:
                    print(f"⚠️  Warning: Could not parse response json: {e}")
        else:
            if debug:
                print(f"⚠️  No content in LLM response. Returning fallback.")
        return ("German", "message", user_input)
    except Exception as e:
        print(f"⚠️  Warning: Could not route query: {e}")
        return ("German", "message", user_input)