import json

def parse_llm_response(response: str) -> dict:
    """Parse the LLM's response into a structured incident dict."""
    try:
        return json.loads(response)
    except Exception:
        return {"error": "Invalid LLM response format"}
