# Data Flow

1. **Ingestion:** Incident reports are received via email, webhook, or file upload.
2. **Preprocessing:** Text is cleaned, normalized, and language is detected.
3. **LLM Processing:** LLMs structure the incident, extract entities, and score severity.
4. **Intelligence Extraction:** Entities, classifications, and confidence scores are produced.
5. **Automation:** n8n workflows escalate and notify based on intelligence.
6. **Storage:** All structured data is persisted for audit and analytics.
