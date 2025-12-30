# Architecture Overview

The Incident Intelligence Engine is a modular, production-ready platform for transforming unstructured incident reports into actionable intelligence using LLMs and n8n automation.

## High-Level Components
- **Ingestion:** Email, webhook, and file-based intake.
- **Preprocessing:** Text cleaning, language detection, normalization.
- **LLM Processing:** Prompting, response parsing, validation.
- **Intelligence Extraction:** Entity extraction, classification, severity scoring.
- **Automation:** n8n-driven escalation and notification workflows.
- **Storage:** Structured repository with migrations.
- **Evaluation:** Metrics, golden datasets, and model evaluation.

## See Also
- [System Overview](system_overview.md)
- [Data Flow](data_flow.md)
- [Security Considerations](security_considerations.md)
- [Evaluation Methodology](evaluation_methodology.md)
