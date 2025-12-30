def score_severity(incident: dict) -> str:
    """Scores the severity of the incident."""
    # Placeholder: Use rules or LLM for real implementation
    if "critical" in incident.get("raw_text", "").lower():
        return "Critical"
    return "Medium"
