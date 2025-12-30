from src.ingestion.email_ingestor import ingest_email
from src.ingestion.webhook_ingestor import ingest_webhook
from src.ingestion.file_ingestor import ingest_file
import tempfile

def test_ingest_email():
    data = {"body": "test incident"}
    assert ingest_email(data) == "test incident"

def test_ingest_webhook():
    data = {"incident": "webhook incident"}
    assert ingest_webhook(data) == "webhook incident"

def test_ingest_file():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write("file incident")
        f.flush()
        assert ingest_file(f.name) == "file incident"
