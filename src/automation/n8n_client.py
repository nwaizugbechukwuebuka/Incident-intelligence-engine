import os
import httpx

def dispatch_workflow(incident: dict) -> None:
    """Dispatches incident to n8n workflow via REST API."""
    n8n_url = os.getenv("N8N_API_URL")
    n8n_key = os.getenv("N8N_API_KEY")
    headers = {"Authorization": f"Bearer {n8n_key}"}
    try:
        httpx.post(f"{n8n_url}/webhook/incident-intake", json=incident, headers=headers, timeout=10)
    except Exception as e:
        print(f"n8n dispatch error: {e}")
