from lingua import Language, LanguageDetectorBuilder
from typing import Optional


# German question words for enhanced language detection
GERMAN_QUESTION_WORDS = [
    # Basic question words
    'wer', 'was', 'wann', 'wo', 'warum', 'wie', 'wohin', 'woher', 'wessen',
    'welcher', 'welche', 'welches', 'welchen',
    
    # German-specific question words
    'wieso', 'weshalb', 'weswegen', 'inwiefern', 'inwieweit',
    'woran', 'worauf', 'woraus', 'wobei', 'wodurch', 'wofür', 'wogegen',
    'wozu', 'womit', 'wonach', 'wovon', 'wovor', 'worin', 'worüber', 'worunter',
    
    # Time-related question starters
    'ab', 'seit', 'um',

    #modal verbs
    'ist', 'können', 'kannst', 'müssen', 'sollen', 'wollen', 'hat', 'wird',
    'hatte', 'hatten', 'werden', 'nenne', 'benenne', 'erkläre', 'zeige',
    'finde', 'suche', 'gebe', 'gib', 'gibt', 'gibts', 'gibst', 'schreibe',
]


# Build detector with common languages for better performance with at least 10% confidence
def _build_detector_german():
    """Build language detector with commonly used languages"""
    return LanguageDetectorBuilder.from_languages(
        Language.GERMAN
    ).with_minimum_relative_distance(0.1).build()


def _build_detector_english():
    """Build language detector with commonly used languages"""
    return LanguageDetectorBuilder.from_languages(
        Language.ENGLISH
    ).with_minimum_relative_distance(0.1).build()


def _build_detector_rest_common():
    """Build language detector with commonly used languages"""
    return LanguageDetectorBuilder.from_all_languages(
    ).with_preloaded_language_models(
    ).with_minimum_relative_distance(0.1).build()


# Create detector instance (shared across function calls)
_german_detector = _build_detector_german()
_english_detector = _build_detector_english()
_rest_common_detector = _build_detector_rest_common()

def _starts_with_german_question_word(text: str) -> bool:
    """
    Check if text starts with a German question word
    
    Args:
        text: Input text to check
        
    Returns:
        True if text starts with a German question word, False otherwise
    """
    if not text or not text.strip():
        return False
    
    # Get the first word and convert to lowercase
    first_word = text.strip().split()[0].lower()
    
    # Check if it's a German question word
    return first_word in GERMAN_QUESTION_WORDS


# Check if input is too short for reliable language detection
def _is_input_too_short(text: str) -> bool:
    """Check if input is too short for reliable language detection"""
    char_count = len(text.strip())
    word_count = len(text.strip().split())
    
    return char_count < 15 and word_count < 4


# Extend short input with previous user questions from session memory
def _extend_with_previous_context(
    text: str, session_id: str, session_memory
) -> str:
    """Extend short input with previous user questions from session memory"""
    if not session_memory or not session_id:
        return text
    
    try:
        # Get recent conversation history (last 3 turns)
        recent_turns = session_memory.get_context_window(
            session_id, window_size=6
        )
        
        # Collect previous user messages
        previous_user_messages = []
        for turn in recent_turns:
            if hasattr(turn, 'role') and turn.role.value == 'user':
                previous_user_messages.append(turn.content)
        
        # Combine current input with previous context
        if previous_user_messages:
            # Take the most recent 2 user messages to avoid too much context
            context_messages = previous_user_messages[-2:]
            extended_text = f"{' '.join(context_messages)} {text}"
            return extended_text
        
    except Exception as e:
        print(f"Error extending context: {e}")
    
    return text


def detect_language_and_get_name(
    text: str,
    session_id: Optional[str] = None,
    session_memory=None
) -> str:
    """
    Detect language from text and return its capitalized English name.
    
    Args:
        text: Input text to analyze
        session_id: Session ID for accessing conversation memory
        session_memory: Session memory instance for context extension
    
    Returns:
        Detected language name (capitalized) or 'German' as default
    """
    try:
        # First check if text starts with a German question word
        if _starts_with_german_question_word(text):
            return 'German'
        
        # Check if input is too short for reliable detection
        if _is_input_too_short(text):
            # Try to extend with previous context if session memory available
            if session_id and session_memory:
                extended_text = _extend_with_previous_context(
                    text, session_id, session_memory
                )
                
                # Check if extended text is now long enough
                if not _is_input_too_short(extended_text):
                    text = extended_text
                else:
                    # Still too short, default to German
                    return 'German'
            else:
                # No session memory available, default to German
                return 'German'
        
        # Detect language using lingua-language-detector
        german = _german_detector.detect_language_of(text)
        english = _english_detector.detect_language_of(text)
        if (german is None) != (english is None):
            language = german if german is not None else english
        else: 
            language = _rest_common_detector.detect_language_of(text)
        language_name = language.name.capitalize() if language else 'German'
        return language_name
    
    except Exception as e:
        print(f"Language detection error: {e}")
        return 'German'  # Default to German on any other error 