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
    # Check Chainlit version for compatibility
    try:
        version_tuple = tuple(map(int, cl.__version__.split('.')[:4]))
        if version_tuple > (2, 7, 1, 0):
            # New version: use cl.context.session.environ
            cookie_header = cl.context.session.environ.get("HTTP_COOKIE", "")
        else:
            # Old version: use cl.user_session
            cookie_header = cl.user_session.get("http_cookie", "")
    except (AttributeError, ValueError):
        # Fallback to old method if version check fails
        cookie_header = cl.context.session.environ.get("HTTP_COOKIE", "")
    cookie_header = cookie_header if cookie_header else ""
    cookie_name = "accepted_terms"
    terms_accepted = f"{cookie_name}=true" in cookie_header
    return terms_accepted
