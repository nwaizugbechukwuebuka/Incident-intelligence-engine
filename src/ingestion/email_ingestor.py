from typing import Dict

def ingest_email(email_data: Dict) -> str:
    """Extracts incident text from email payload."""
    return email_data.get("body", "")
