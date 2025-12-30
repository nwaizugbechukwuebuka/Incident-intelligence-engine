from langdetect import detect

def detect_language(text: str) -> str:
    """Detects the language of the input text."""
    try:
        return detect(text)
    except Exception:
        return "unknown"
