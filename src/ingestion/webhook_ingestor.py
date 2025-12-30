from typing import Dict

def ingest_webhook(webhook_data: Dict) -> str:
    """Extracts incident text from webhook payload."""
    return webhook_data.get("incident", "")
