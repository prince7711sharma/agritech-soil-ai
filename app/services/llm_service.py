import json
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=GROQ_API_KEY)


def explain_soil_report(soil_report: dict):
    prompt = f"""
You are an agricultural soil expert.

Explain the soil health report in simple farmer-friendly language.

Rules:
- Use ONLY the data provided
- Do NOT invent numbers
- Keep explanation practical and short

Soil Report:
{json.dumps(soil_report, indent=2)}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
