from langdetect import detect


def detect_language_and_get_name(text: str) -> str:
    """Detect language from text and return language name"""
    try:
        # Detect language code
        lang_code = detect(text)
        lang_map = {
            'af': 'Afrikaans',
            'ar': 'Arabisch',
            'bg': 'Bulgarisch',
            'bn': 'Bengalisch',
            'ca': 'Katalanisch',
            'cs': 'Tschechisch',
            'cy': 'Walisisch',
            'da': 'Dänisch',
            'de': 'Deutsch',
            'el': 'Griechisch',
            'en': 'Englisch',
            'es': 'Spanisch',
            'et': 'Estnisch',
            'fa': 'Persisch',
            'fi': 'Finnisch',
            'fr': 'Französisch',
            'gu': 'Gujarati',
            'he': 'Hebräisch',
            'hi': 'Hindi',
            'hr': 'Kroatisch',
            'hu': 'Ungarisch',
            'id': 'Indonesisch',
            'it': 'Italienisch',
            'ja': 'Japanisch',
            'kn': 'Kannada',
            'ko': 'Koreanisch',
            'lt': 'Litauisch',
            'lv': 'Lettisch',
            'mk': 'Mazedonisch',
            'ml': 'Malayalam',
            'mr': 'Marathi',
            'ne': 'Nepali',
            'nl': 'Niederländisch',
            'no': 'Norwegisch',
            'pa': 'Panjabi',
            'pl': 'Polnisch',
            'pt': 'Portugiesisch',
            'ro': 'Rumänisch',
            'ru': 'Russisch',
            'sk': 'Slowakisch',
            'sl': 'Slowenisch',
            'so': 'Somali',
            'sq': 'Albanisch',
            'sv': 'Schwedisch',
            'sw': 'Suaheli',
            'ta': 'Tamil',
            'te': 'Telugu',
            'th': 'Thailändisch',
            'tl': 'Tagalog',
            'tr': 'Türkisch',
            'uk': 'Ukrainisch',
            'ur': 'Urdu',
            'vi': 'Vietnamesisch',
            'zh-cn': 'Chinesisch (vereinfacht)',
            'zh-tw': 'Chinesisch (traditionell)'}
        return lang_map.get(lang_code, 'Deutsch')  # Default to German
    except Exception:
        return 'Deutsch'  # Default to German if detection fails 