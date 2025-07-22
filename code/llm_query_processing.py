import os
import ast
from rich import print
from openai import AsyncOpenAI
from prompts import AUGMENT_USER_QUERY, ROUTER_LANGUAGE_DETECTION_PROMPT

async def augment_query_with_llm(
    client: AsyncOpenAI | None,
    user_input: str,
    detected_language: str,
    model: str = "gpt-4.1-nano-2025-04-14",
    debug: bool = False
) -> str:
    """
    Augments the user's query using an LLM to make it more semantically rich.
    """
    if not client:
        client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        
    system_prompt = AUGMENT_USER_QUERY.replace("{{language}}", detected_language)
    user_prompt = f"User query: '{user_input}'\nRephrased query: "
        
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0,
        )
        if response.choices and response.choices[0].message.content:
            augmented_query = response.choices[0].message.content.strip()
            if debug:
                print(f"🎨 [bold]Query augmentation:[/bold]\n   [cyan]Original:[/] {user_input}\n   [green]Augmented:[/] {augmented_query}")
            return augmented_query
        return user_input
    except Exception as e:
        print(f"⚠️  Warning: Could not augment query: {e}")
        return user_input

async def route_and_detect_language(
    client: AsyncOpenAI | None,
    user_input: str,
    model: str = "gpt-4.1-nano-2025-04-14",
    debug: bool = False
) -> tuple[str, str]:
    """
    Detects language of the user's query and routes the user's query
    to 'news', 'sitzplatz', or 'message'. Returns a tuple: (language, route).
    """
    if not client:
        client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": ROUTER_LANGUAGE_DETECTION_PROMPT},
                {"role": "user", "content": f"User query: '{user_input}'"}
            ],
            temperature=0,
            max_tokens=10
        )
        if response.choices and response.choices[0].message.content:
            route_str = response.choices[0].message.content.strip()
            
            # Check if response_str can be cast into a tuple
            try:
                route_tuple = ast.literal_eval(route_str)
                if not isinstance(route_tuple, tuple):                
                    return("German", "message")                    
                if debug:
                    print(f"🚦 [bold]LLM Router classified query as:")
                    print(f"   - Language: {route_tuple[0]}")
                    print(f"   - Route category: {route_tuple[1]}")
                return route_tuple
            except Exception as e:
                print(f"⚠️  Warning: Could not parse route tuple: {e}")
                return ("German", "message")
        return ("German", "message")
    except Exception as e:
        print(f"⚠️  Warning: Could not route query: {e}")
        return ("German", "message")