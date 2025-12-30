import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_full_pipeline():
    payload = {
        "source": "email",
        "raw_text": "At 03:14 UTC, the finance server (host: FIN-SRV-01, IP: 10.1.2.3) reported abnormal encryption activity. Suspicious process: cryptolocker.exe. User: jdoe. Immediate containment required."
    }
    response = client.post("/ingest", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "entities" in data
    assert "classification" in data
    assert "severity" in data
