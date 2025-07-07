from fastapi import APIRouter
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

@router.get("/")
def chatbot(query: str):
    if not OPENROUTER_API_KEY:
        return {"error": "API key missing. Set OPENROUTER_API_KEY as an environment variable."}

    url = "https://openrouter.ai/api/v1/chat/completions"

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "You are a smart academic advisor for Nigerian university students. Be brief, helpful and realistic."
            },
            {
                "role": "user",
                "content": query
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {"answer": data['choices'][0]['message']['content']}
    else:
        return {
            "error": f"Request failed with status {response.status_code}",
            "details": response.text
        }
