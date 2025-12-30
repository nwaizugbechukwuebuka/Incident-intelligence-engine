# Security Considerations

- All secrets are managed via environment variables and never hardcoded.
- LLM API keys are stored securely and rotated regularly.
- Input validation and schema enforcement at every stage.
- Structured logging for auditability.
- n8n workflows are access-controlled and monitored.
- Data is encrypted at rest and in transit (where supported).
