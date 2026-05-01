from fastapi import APIRouter

router = APIRouter()


@router.get("/history/{ticker}")
def history(ticker: str):

    # ✅ Dummy 5-year data (REQUIRED for UI)
    return [
        {"year": 2021, "environmental": 60, "social": 55, "governance": 70, "total": 62},
        {"year": 2022, "environmental": 65, "social": 60, "governance": 72, "total": 65},
        {"year": 2023, "environmental": 70, "social": 65, "governance": 75, "total": 70},
        {"year": 2024, "environmental": 75, "social": 68, "governance": 78, "total": 74},
        {"year": 2025, "environmental": 80, "social": 70, "governance": 80, "total": 76},
    ]