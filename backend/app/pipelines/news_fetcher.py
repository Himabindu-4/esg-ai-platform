import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def fetch_esg_news(ticker: str):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={ticker}&language=en&sortBy=publishedAt&pageSize=10&apiKey={API_KEY}"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()
    articles = data.get("articles", [])

    results = []

    for article in articles:

        title = article.get("title", "")
        desc = article.get("description", "")

        text = f"{title} {desc}".lower()

        severity = "low"

        if any(word in text for word in ["fraud", "scandal", "fine", "lawsuit"]):
            severity = "high"
        elif any(word in text for word in ["investigation", "violation", "controversy"]):
            severity = "medium"

        results.append({
            "title": title,
            "source": article.get("source", {}).get("name"),
            "url": article.get("url"),
            "published_at": article.get("publishedAt"),
            "severity": severity
        })

    return results