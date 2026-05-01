from fastapi import APIRouter
from pathlib import Path
import json

router = APIRouter()

DATA_DIR = Path("app/data/processed")
MSCI_FILE = Path("app/data/msci_scores.json")


@router.get("/compare-msci/{ticker}")
def compare_msci(ticker: str):

    ticker = ticker.upper()

    # Load your ESG score
    file_path = DATA_DIR / f"{ticker}.json"

    if not file_path.exists():
        return {"error": "No ESG data found"}

    with open(file_path, "r") as f:
        local = json.load(f)

    # Load MSCI benchmark
    if not MSCI_FILE.exists():
        return {"error": "MSCI data file missing"}

    with open(MSCI_FILE, "r") as f:
        msci = json.load(f)

    msci_score = msci.get(ticker, {}).get("total")

    if msci_score is None:
        return {"error": "No MSCI data for this ticker"}

    your_score = local.get("total_score", 0)

    diff = round(your_score - msci_score, 2)

    return {
        "ticker": ticker,
        "your_score": your_score,
        "msci_score": msci_score,
        "difference": diff,
        "status": (
            "aligned" if abs(diff) < 5 else
            "overestimated" if diff > 0 else
            "underestimated"
        )
    }