import openai
import os

def process_with_llm(text: str) -> str:
    """Send text to LLM and return response using OpenAI SDK >=1.0.0."""
    api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a security incident analyst."},
            {"role": "user", "content": text}
        ],
        max_tokens=512
    )
    return response.choices[0].message.content
