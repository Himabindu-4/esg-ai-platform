import csv
import io
import json
from pathlib import Path
from fastapi import APIRouter, UploadFile, File

router = APIRouter()

DATA_DIR = Path("app/data/processed")


@router.post("/portfolio/upload")
async def upload_portfolio(file: UploadFile = File(...)):

    try:
        content = await file.read()
        decoded = content.decode("utf-8")

        reader = csv.DictReader(io.StringIO(decoded))

        total_env = 0
        total_soc = 0
        total_gov = 0
        total_weight = 0

        for row in reader:

            ticker = row.get("ticker", "").upper()

            if not ticker:
                return {
                    "status": "error",
                    "message": "Missing ticker in CSV"
                }

            try:
                weight = float(row.get("weight", 0))
            except:
                return {
                    "status": "error",
                    "message": f"Invalid weight for {ticker}"
                }

            total_weight += weight

            file_path = DATA_DIR / f"{ticker}.json"

            if not file_path.exists():
                return {
                    "status": "error",
                    "message": f"Data not found for {ticker}"
                }

            with open(file_path, "r") as f:
                data = json.load(f)

            env = data.get("environmental_score", 0)
            soc = data.get("social_score", 0)
            gov = data.get("governance_score", 0)

            total_env += env * weight
            total_soc += soc * weight
            total_gov += gov * weight

        # ✅ VALIDATION
        if round(total_weight, 2) != 1.0:
            return {
                "status": "error",
                "message": "Weights must sum to 1"
            }

        total_esg = round((total_env + total_soc + total_gov) / 3, 2)

        return {
            "status": "success",
            "data": {
                "environmental": round(total_env, 2),
                "social": round(total_soc, 2),
                "governance": round(total_gov, 2),
                "total": total_esg
            }
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }