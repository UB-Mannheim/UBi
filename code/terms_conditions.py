import chainlit as cl


async def ask_terms_acceptance():
    """Ask user to accept terms and conditions with CustomElement"""
    # **Einverständniserklärung zu den Nutzungsbedingungen des KI-Chatbots der UB Mannheim**
    terms_content = ""
    element = cl.CustomElement(name="TermsAcceptBox")
    await cl.Message(content=terms_content, elements=[element]).send()


@cl.action_callback("accept_terms_button")
async def on_accept_terms(action):
    """Handle terms acceptance"""
    await cl.Message(
        content="✅ Nutzungsbedingungen akzeptiert! Die Seite wird neu "
        "geladen...",
        author="system",
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
