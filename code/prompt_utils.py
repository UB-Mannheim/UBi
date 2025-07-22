import os
from rich import print
from openai import AsyncOpenAI
from prompts import AUGMENT_USER_QUERY

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