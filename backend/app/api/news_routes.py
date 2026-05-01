from fastapi import APIRouter
from app.pipelines.news_fetcher import fetch_esg_news

router = APIRouter()


@router.get("/news/{ticker}")
def get_news(ticker: str):

    try:
        return fetch_esg_news(ticker)
    except Exception as e:
        return {"error": str(e)}