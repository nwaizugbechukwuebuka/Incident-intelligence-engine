from src.intelligence.incident_classifier import classify_incident
from src.intelligence.entity_extractor import extract_entities
from src.intelligence.severity_scorer import score_severity
from src.intelligence.confidence_estimator import estimate_confidence

def test_classify_incident():
    assert classify_incident({"raw_text": "ransomware"}) == "Ransomware"
    assert classify_incident({"raw_text": "phishing"}) == "Phishing"
    assert classify_incident({"raw_text": "other"}) == "Other"

def test_extract_entities():
    assert extract_entities({}) == ["entity1", "entity2"]

def test_score_severity():
    assert score_severity({"raw_text": "critical"}) == "Critical"
    assert score_severity({"raw_text": "normal"}) == "Medium"

def test_estimate_confidence():
    assert estimate_confidence({}) == 0.95
