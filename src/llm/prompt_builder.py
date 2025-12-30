def build_prompt(text: str) -> str:
    """Builds a prompt for the LLM to structure an incident."""
    return f"""Analyze the following incident report and extract structured information:\n{text}"""
