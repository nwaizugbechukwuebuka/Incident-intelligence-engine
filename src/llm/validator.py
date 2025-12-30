from jsonschema import validate, ValidationError
import json

def validate_structured_incident(incident: dict) -> None:
    """Validate structured incident against schema."""
    with open("config/schema.json") as f:
        schema = json.load(f)
    try:
        validate(instance=incident, schema=schema)
    except ValidationError as e:
        raise ValueError(f"Schema validation error: {e}")
