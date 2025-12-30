def should_escalate(incident: dict) -> bool:
    """Determines if incident should be escalated."""
    return incident.get("severity", "Medium") == "Critical"
