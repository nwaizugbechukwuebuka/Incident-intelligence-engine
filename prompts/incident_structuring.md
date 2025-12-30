# Incident Structuring Prompt

You are a security incident analyst. Given the following unstructured incident report, extract the following fields in JSON:
- id (string, unique)
- timestamp (ISO8601)
- source (string)
- raw_text (string)
- entities (list of objects)
- classification (string)
- severity (string)
- confidence (float, 0-1)
- actions (list of strings)

Incident:
---
{incident_text}
---
