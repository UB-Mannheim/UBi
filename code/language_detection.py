from lingua import Language, LanguageDetectorBuilder


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


def detect_language_and_get_name(text: str) -> str:
    """Detect language from text and return its capitalized English name."""
    try:
        # Detect language using lingua-language-detector
        language = _german_detector.detect_language_of(text)
        if language is None:
            language = _english_detector.detect_language_of(text)
        if language is None:
            language = _rest_common_detector.detect_language_of(text)
        language = language.name.capitalize() if language else 'German'
        return language
    
    except Exception as e:
        print(e)
        return 'German'  # Default to German on any other error 