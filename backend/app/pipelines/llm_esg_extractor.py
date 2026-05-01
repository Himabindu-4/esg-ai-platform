import os
import json
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are an ESG analyst. Extract structured ESG data from text.

Return ONLY valid JSON with this schema:

{
  "environmental_score": number (0-100),
  "social_score": number (0-100),
  "governance_score": number (0-100),
  "total_score": number (0-100),
  "evidence_quotes": [string, string, ...],
  "greenwashing_flags": number,
  "confidence": number (0-1)
}

Rules:
- Base scores on concrete metrics (emissions, energy, labor, governance)
- Penalize vague claims (greenwashing)
- Use quotes directly from the text
- No explanations outside JSON
"""

def extract_esg_from_text(text: str):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text[:12000]}  # limit size
        ],
        temperature=0
    )

    raw = completion.choices[0].message.content.strip()

    try:
        data = json.loads(raw)
        return data
    except Exception:
        return {
            "error": "Invalid JSON from LLM",
            "raw": raw
        }