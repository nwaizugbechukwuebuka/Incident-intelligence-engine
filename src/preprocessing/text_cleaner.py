import re

def clean_text(text: str) -> str:
    """Basic cleaning: remove extra whitespace, control chars, etc."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()
