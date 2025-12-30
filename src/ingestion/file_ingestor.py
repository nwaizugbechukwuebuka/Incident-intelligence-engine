def ingest_file(file_path: str) -> str:
    """Reads incident text from a file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
