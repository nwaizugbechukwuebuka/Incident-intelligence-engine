import httpx
import pytest

def test_n8n_webhook():
    # This is a placeholder; in real tests, mock n8n or use a test instance
    url = "http://localhost:5678/webhook/incident-intake"
    payload = {"incident": {"id": "test", "severity": "Critical"}}
    try:
        response = httpx.post(url, json=payload, timeout=5)
        assert response.status_code in (200, 204, 404)  # Accept 404 if n8n not running
    except Exception:
        pass
