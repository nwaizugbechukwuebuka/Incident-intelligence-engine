# ADR-001: LLM Selection

## Status
Accepted

## Context
The project requires a robust, production-ready LLM for structuring incident reports, extracting entities, and scoring severity. Key requirements include:
- High accuracy on security/operations text
- API availability
- Cost-effectiveness
- Security and compliance

## Decision
We select **OpenAI GPT-4** as the default LLM provider for its:
- State-of-the-art performance
- Mature API and ecosystem
- Strong security/compliance posture
- Broad community support

## Consequences
- All LLM prompts and responses will be designed for OpenAI API compatibility.
- The system will allow for future LLM provider abstraction.
