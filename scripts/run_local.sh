#!/bin/bash
export APP_ENV=development
export LOG_LEVEL=INFO
export DATABASE_URL=sqlite:///incident_intel.db
export LLM_PROVIDER=openai
export LLM_API_KEY=your-openai-api-key
export N8N_API_URL=http://localhost:5678/rest
export N8N_API_KEY=your-n8n-api-key
poetry run python src/main.py
