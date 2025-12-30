import json
from src.storage.repository import save_incident

def main():
    with open("data/processed/structured_incidents.json") as f:
        incidents = json.load(f)
    for incident in incidents:
        save_incident(incident)

if __name__ == "__main__":
    main()
