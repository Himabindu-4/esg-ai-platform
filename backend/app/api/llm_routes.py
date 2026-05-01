from fastapi import APIRouter
from app.pipelines.llm_esg_extractor import extract_esg_from_text

router = APIRouter()

@router.post("/llm-esg")
def llm_esg(payload: dict):

    text = payload.get("text", "")

    if not text:
        return {"error": "No text provided"}

    result = extract_esg_from_text(text)

    return result