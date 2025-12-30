from pydantic import BaseModel, Field
from typing import List, Any

class IncidentIn(BaseModel):
    source: str = Field(..., description="Source of the incident report")
    raw_text: str = Field(..., description="Unstructured incident text")

class IncidentOut(BaseModel):
    id: str
    timestamp: str
    source: str
    raw_text: str
    entities: List[Any]
    classification: str
    severity: str
    confidence: float
    actions: List[str]
