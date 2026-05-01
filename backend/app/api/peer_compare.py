from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter()

DATA_DIR = Path("app/data/processed")


@router.get("/peer-comparison")
def peer_comparison():

    companies = [
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN"
    ]

    results = []

    for ticker in companies:

        file_path = DATA_DIR / f"{ticker}.json"

        if file_path.exists():

            with open(file_path, "r") as f:

                data = json.load(f)

            results.append({

                "ticker": ticker,

                "environmental":
                    data.get("environmental_score", 0),

                "social":
                    data.get("social_score", 0),

                "governance":
                    data.get("governance_score", 0),

                "total":
                    data.get("total_score", 0),
            })

        else:

            results.append({

                "ticker": ticker,

                "environmental": 0,

                "social": 0,

                "governance": 0,

                "total": 0,
            })

    return results