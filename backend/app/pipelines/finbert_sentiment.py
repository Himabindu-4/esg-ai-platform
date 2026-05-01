from transformers import pipeline

from app.pipelines.parse_filings import parse_company_filings
from app.pipelines.extract_sections import extract_sections


print("\nLoading FinBERT model...\n")

classifier = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)


def analyze_sentiment(text):

    # limit text length for transformer
    text = text[:1000]

    result = classifier(text)

    return result[0]


if __name__ == "__main__":

    filings = parse_company_filings("AAPL")

    if filings:

        sample_text = filings[0]

        sections = extract_sections(sample_text)

        environmental_sections = sections.get("environmental", [])

        print(f"\nEnvironmental Sections Found: {len(environmental_sections)}\n")

        for idx, section in enumerate(environmental_sections[:5]):

            print("=" * 80)

            print(f"SECTION {idx+1}")

            print("\nRunning FinBERT sentiment...\n")

            sentiment = analyze_sentiment(section)

            print(sentiment)

            print("\nTEXT SAMPLE:\n")

            print(section[:1000])

            print("\n")