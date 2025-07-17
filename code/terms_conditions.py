import chainlit as cl


async def ask_terms_acceptance():
    """Ask user to accept terms and conditions with AskUser Action"""
    
    terms_content = """
    **Einverständniserklärung zu den Nutzungsbedingungen des KI-Chatbots der UB Mannheim**
    Sie bestätigen:
    ✅ Sie werden keine personenbezogenen Daten eingeben.
    ✅ Ihre Eingaben dürfen zur Verbesserung des Services anonymisiert ausgewertet werden.
    ✅ Sie verpflichten sich, die Nutzungsbedingungen einzuhalten.
    Stimmen Sie den Nutzungsbedingungen zu?
    """
    
    actions = [
        cl.Action(
            name="accept_terms_button",
            value="accept", 
            label="✅ Akzeptieren",
            description="Nutzungsbedingungen akzeptieren",
            payload={"action": "accept"}
        )
    ]
    await cl.Message(
        content=terms_content,
        actions=actions
    ).send()


@cl.action_callback("accept_terms_button")
async def on_accept_terms(action):
    """Handle terms acceptance"""
    await cl.Message(
        content="✅ Nutzungsbedingungen akzeptiert! Die Seite wird neu "
                "geladen...",
        author="system"
    ).send()



def check_terms_accepted():
    """Check if terms are accepted via cookie using session"""
    cookie_header = cl.user_session.get("http_cookie", "")
    cookie_name = "accepted_terms"
    if cookie_header:
        terms_accepted = f"{cookie_name}=true" in cookie_header
    else:
        terms_accepted = False
    return terms_accepted 
