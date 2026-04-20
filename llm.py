import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"


def generate_answer(query, context):
    prompt = f"""
You are a helpful assistant.
Answer ONLY from the context.
Cite sources like [Doc1].

Context:
{context}

Question:
{query}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        return response.json()["response"]
    except Exception as e:
        return f"❌ LLM Error: {str(e)}"