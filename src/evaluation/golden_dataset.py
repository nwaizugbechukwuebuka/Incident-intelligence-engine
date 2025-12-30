import json

def load_golden_dataset(path: str) -> list:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
