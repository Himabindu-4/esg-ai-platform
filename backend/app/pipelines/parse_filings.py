from bs4 import BeautifulSoup
from pathlib import Path
import re


BASE_PATH = Path(
    "app/data/raw/sec_filings/sec-edgar-filings"
)


def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def parse_html_file(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="ignore"
    ) as f:

        html = f.read()

    soup = BeautifulSoup(html, "lxml")

    text = soup.get_text(separator=" ")

    return clean_text(text)


def parse_company_filings(ticker):

    ticker_path = BASE_PATH / ticker / "10-K"

    all_text = []

    if not ticker_path.exists():
        print(f"No filings found for {ticker}")
        return []

    for filing_folder in ticker_path.iterdir():

        if filing_folder.is_dir():

            for file in filing_folder.iterdir():

                if (
                    file.suffix == ".html"
                    or file.suffix == ".htm"
                    or file.suffix == ".txt"
                ):

                    try:

                        text = parse_html_file(file)

                        all_text.append(text)

                        print(f"Parsed: {file.name}")

                    except Exception as e:

                        print(f"Error parsing {file.name}: {e}")

    return all_text


if __name__ == "__main__":

    filings = parse_company_filings("AAPL")

    print(f"\nTotal filings parsed: {len(filings)}")

    if filings:

        print("\nSample Extracted Text:\n")

        print(filings[0][:5000])