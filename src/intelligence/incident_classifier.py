def classify_incident(incident: dict) -> str:
    """Classifies the incident type."""
    # Placeholder: Use keywords or LLM for real implementation
    text = incident.get("raw_text", "").lower()
    if "ransomware" in text:
        return "Ransomware"
    if "phishing" in text:
        return "Phishing"
    return "Other"
