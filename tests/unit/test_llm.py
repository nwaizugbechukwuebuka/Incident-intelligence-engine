from src.llm.response_parser import parse_llm_response
from src.llm.validator import validate_structured_incident
import pytest
import json

def test_parse_llm_response_valid():
    response = '{"id": "1", "timestamp": "2025-12-29T03:14:00Z", "source": "email", "raw_text": "test", "entities": [], "classification": "Test", "severity": "Low", "confidence": 0.9, "actions": []}'
    result = parse_llm_response(response)
    assert result["id"] == "1"

def test_parse_llm_response_invalid():
    response = 'not a json'
    result = parse_llm_response(response)
    assert "error" in result

def test_validate_structured_incident():
    incident = json.loads('{"id": "1", "timestamp": "2025-12-29T03:14:00Z", "source": "email", "raw_text": "test", "entities": [], "classification": "Test", "severity": "Low", "confidence": 0.9, "actions": []}')
    validate_structured_incident(incident)
