from fastapi import APIRouter
from fastapi.responses import FileResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import json
from pathlib import Path

router = APIRouter()

DATA_DIR = Path("app/data/processed")


@router.get("/report/{ticker}")
def generate_report(ticker: str):

    try:
        file_path = DATA_DIR / f"{ticker.upper()}.json"

        if not file_path.exists():
            return {
                "status": "error",
                "message": "Company data not found"
            }

        with open(file_path, "r") as f:
            data = json.load(f)

        env = data.get("environmental_score", 0)
        soc = data.get("social_score", 0)
        gov = data.get("governance_score", 0)
        total = data.get("total_score", 0)

        pdf_path = f"{ticker}_esg_report.pdf"

        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(pdf_path)

        elements = []

        elements.append(Paragraph(f"{ticker} ESG Report", styles["Title"]))
        elements.append(Spacer(1, 20))

        # ✅ REAL DATA
        elements.append(Paragraph(f"Environmental Score: {env}", styles["Normal"]))
        elements.append(Paragraph(f"Social Score: {soc}", styles["Normal"]))
        elements.append(Paragraph(f"Governance Score: {gov}", styles["Normal"]))
        elements.append(Paragraph(f"Total ESG Score: {total}", styles["Normal"]))

        elements.append(Spacer(1, 20))

        elements.append(Paragraph("Generated from ESG AI Platform", styles["Normal"]))

        doc.build(elements)

        return FileResponse(
            path=pdf_path,
            filename=pdf_path,
            media_type="application/pdf"
        )

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }