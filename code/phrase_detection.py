from typing import Optional, Tuple


# Comprehensive phrase detection for cost-saving responses
THANK_YOU_PHRASES = {
    # German thank you phrases
    "danke": "German",
    "vielen dank": "German", 
    "dankeschön": "German",
    "danke schön": "German",
    "danke sehr": "German",
    "danke dir": "German",
    "danke ihnen": "German",
    "herzlichen dank": "German",
    "besten dank": "German",
    "tausend dank": "German",          # "A thousand thanks", very common and friendly
    "danke vielmals": "German",        # "Thanks many times"
    "ich danke dir": "German",         # "I thank you" (informal)
    "ich danke ihnen": "German",       # "I thank you" (formal)
    "danke im voraus": "German",       # "Thanks in advance"
    "vielen lieben dank": "German",    # A warmer, more personal version of 
                                       # "vielen dank"
    "danke für die antwort": "German", # "Thank you for the answer"
    "danke für die hilfe": "German",   # "Thank you for the help"
    "danke für die information": "German", # "Thank you for the information"
    "danke für die unterstützung": "German", # "Thank you for the support"
    "vielen lieben dank": "German", # "Thank you for the support"
    "vielen lieben thanks": "German", # "Thank you for the support"

    
    # English thank you phrases
    "thanks": "English",
    "thank you": "English",
    "ty": "English",
    "thanks a lot": "English",
    "thank you very much": "English",
    "thanks so much": "English",
    "thank you so much": "English",
    "many thanks": "English",
    "thanks again": "English",
    "thx": "English",                  # Common abbreviation for "thanks"
    "tysm": "English",                 # Common abbreviation for "thank you so much"
    "cheers": "English",               # Very common, especially in UK/Australia
    "i appreciate it": "English",
    "much appreciated": "English",
    "you're a lifesaver": "English",
    "i owe you one": "English",
}

GREETING_PHRASES = {
    # German greetings
    "hallo": "German",
    "guten tag": "German",
    "guten morgen": "German",
    "guten abend": "German",
    "servus": "German",                # Regional (Southern Germany/Austria)
    "moin": "German",                  # Regional (Northern Germany)
    "grüß gott": "German",             # Regional (Southern Germany/Austria)
    "tag": "German",                   # Short for "guten Tag"
    
    # English greetings
    "hello": "English",
    "hi": "English",
    "hey": "English",
    "good morning": "English",
    "good afternoon": "English",
    "good evening": "English",
    "howdy": "English",                # Regional (e.g., parts of the US)
    "yo": "English",
}

GOODBYE_PHRASES = {
    # German goodbyes
    "tschüss": "German",
    "auf wiedersehen": "German",
    "bis später": "German",
    "bis dann": "German",
    "bis bald": "German",
    "mach's gut": "German",
    "schönen tag noch": "German",      # "Have a nice day"
    
    # English goodbyes
    "goodbye": "English",
    "bye": "English",
    "bye-bye": "English",
    "see you": "English",
    "see ya": "English",
    "take care": "English",
    "have a good one": "English",
    "cheers": "English",               # Also used for goodbyes in the UK
}

APOLOGY_PHRASES = {
    # German apologies
    "entschuldigung": "German",        # "Sorry" or "Excuse me"
    "es tut mir leid": "German",       # "I'm sorry" (literally "It does me sorrow")
    "tut mir leid": "German",          # Common short form
    "verzeihung": "German",            # "Pardon" or "forgiveness"
    "sorry": "German",                 # Very common loanword from English
    "schere": "German",                # youth slang for "sorry"

    # English apologies
    "my apologies": "English",
    "i apologize": "English",
    "my bad": "English",               # Very informal
    "excuse me": "English",
    "pardon me": "English",
}


def detect_thank_you_phrase(text: str) -> Optional[Tuple[str, str]]:
    """
    Detect if text contains a thank you phrase and return the response.
    
    Args:
        text: Input text to check
        
    Returns:
        Tuple of (response, language) if thank you phrase detected, None 
        otherwise
    """
    # Check for exact matches first
    for phrase, language in THANK_YOU_PHRASES.items():
        if phrase == text:
            if language == "German":
                return ("Gern geschehen!", language)
            else:
                return ("You are welcome!", language)
    
    return None


def detect_greeting_phrase(text: str) -> Optional[Tuple[str, str]]:
    """
    Detect if text contains a greeting phrase and return the response.
    
    Args:
        text: Input text to check
        
    Returns:
        Tuple of (response, language) if greeting phrase detected, None 
        otherwise
    """
    # Check for exact matches first
    for phrase, language in GREETING_PHRASES.items():
        if phrase == text:
            if language == "German":
                return ("Hallo! Wie kann ich Ihnen helfen?", language)
            else:
                return ("Hello! How can I help you?", language)
    
    return None


def detect_goodbye_phrase(text: str) -> Optional[Tuple[str, str]]:
    """
    Detect if text contains a goodbye phrase and return the response.
    
    Args:
        text: Input text to check
        
    Returns:
        Tuple of (response, language) if goodbye phrase detected, None 
        otherwise
    """
    # Check for exact matches first
    for phrase, language in GOODBYE_PHRASES.items():
        if phrase == text:
            if language == "German":
                return ("Auf Wiedersehen! Schönen Tag noch!", language)
            else:
                return ("Goodbye! Have a great day!", language)
    
    return None


def detect_apology_phrase(text: str) -> Optional[Tuple[str, str]]:
    """
    Detect if text contains an apology phrase and return the response.
    
    Args:
        text: Input text to check
        
    Returns:
        Tuple of (response, language) if apology phrase detected, None 
        otherwise
    """
    # Check for exact matches first
    for phrase, language in APOLOGY_PHRASES.items():
        if phrase == text:
            if language == "German":
                return ("Kein Problem! Wie kann ich Ihnen helfen?", language)
            else:
                return ("No problem! How can I help you?", language)
    
    return None


def detect_common_phrase(text: str) -> Optional[Tuple[str, str]]:
    """
    Detect if text contains any common phrase and return the response.
    Priority: Thank you > Greeting > Goodbye > Apology
    
    Args:
        text: Input text to check
        
    Returns:
        Tuple of (response, language) if common phrase detected, None 
        otherwise
    """
    # Check in order of priority
    if not text or not text.strip():
        return None
    
    # Convert to lowercase for case-insensitive matching
    text = text.lower().strip('.!?').strip()

    result = detect_thank_you_phrase(text)
    if result:
        return result
    
    result = detect_greeting_phrase(text)
    if result:
        return result
    
    result = detect_goodbye_phrase(text)
    if result:
        return result
    
    result = detect_apology_phrase(text)
    if result:
        return result
    
    return None


def is_thank_you_message(text: str) -> bool:
    """
    Check if the text is a thank you message.
    
    Args:
        text: Input text to check
        
    Returns:
        True if text contains a thank you phrase, False otherwise
    """
    return detect_thank_you_phrase(text) is not None 