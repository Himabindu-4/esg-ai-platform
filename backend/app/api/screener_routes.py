from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

DATA_DIR = Path("app/data/processed")


@router.get("/screener")
def esg_screener(
    min_esg: float = 0,
    min_env: float = 0,
    min_soc: float = 0,
    min_gov: float = 0
):

    companies = ["AAPL", "MSFT", "GOOGL", "AMZN"]

    results = []

    for ticker in companies:

        file_path = DATA_DIR / f"{ticker}.json"

        if file_path.exists():

            with open(file_path, "r") as f:
                data = json.load(f)

            company = {
                "ticker": ticker,
                "environmental": data.get("environmental_score", 0),
                "social": data.get("social_score", 0),
                "governance": data.get("governance_score", 0),
                "total": data.get("total_score", 0),
            }

            # ✅ FILTER LOGIC
            if (
                company["total"] >= min_esg and
                company["environmental"] >= min_env and
                company["social"] >= min_soc and
                company["governance"] >= min_gov
            ):
                results.append(company)

    return results