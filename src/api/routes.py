from fastapi import APIRouter, HTTPException
from src.api.schemas import IncidentIn, IncidentOut
from src.ingestion.email_ingestor import ingest_email
from src.ingestion.webhook_ingestor import ingest_webhook
from src.ingestion.file_ingestor import ingest_file
from src.preprocessing.text_cleaner import clean_text
from src.preprocessing.language_detection import detect_language
from src.preprocessing.normalization import normalize_text
from src.llm.client import process_with_llm
from src.llm.response_parser import parse_llm_response
from src.llm.validator import validate_structured_incident
from src.intelligence.incident_classifier import classify_incident
from src.intelligence.entity_extractor import extract_entities
from src.intelligence.severity_scorer import score_severity
from src.intelligence.confidence_estimator import estimate_confidence
from src.automation.n8n_client import dispatch_workflow
from src.storage.repository import save_incident
from src.utils.logger import log_event

router = APIRouter()

@router.post("/ingest", response_model=IncidentOut)
def ingest_incident(incident: IncidentIn):
    log_event("Received incident", incident.model_dump())
    cleaned = clean_text(incident.raw_text)
    lang = detect_language(cleaned)
    normalized = normalize_text(cleaned, lang)
    llm_result = process_with_llm(normalized)
    structured = parse_llm_response(llm_result)
    validate_structured_incident(structured)
    structured["classification"] = classify_incident(structured)
    structured["entities"] = extract_entities(structured)
    structured["severity"] = score_severity(structured)
    structured["confidence"] = estimate_confidence(structured)
    save_incident(structured)
    dispatch_workflow(structured)
    return structured
