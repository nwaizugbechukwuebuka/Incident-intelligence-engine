from src.storage.incident_model import Incident
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os

engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///incident_intel.db"))

# Placeholder for actual ORM session management
def save_incident(incident: dict) -> None:
    # In production, use SQLAlchemy ORM session
    pass
