from sqlalchemy import Column, String, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Incident(Base):
    __tablename__ = "incidents"
    id = Column(String, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    source = Column(String)
    raw_text = Column(String)
    entities = Column(JSON)
    classification = Column(String)
    severity = Column(String)
    confidence = Column(Float)
    actions = Column(JSON)
