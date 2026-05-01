import json
from pathlib import Path

from app.pipelines.parse_filings import parse_company_filings
from app.pipelines.pdf_esg_parser import extract_pdf_text
from app.pipelines.esg_scoring import calculate_esg_scores


OUTPUT_DIR = Path(
    "app/data/processed"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

PDF_DIR = Path(
    "app/data/raw/sustainability_reports"
)


def build_company_text(ticker):

    combined_text = ""

    filings = parse_company_filings(ticker)

    for filing in filings:

        combined_text += filing + "\n"

    pdf_files = list(PDF_DIR.glob("*.pdf"))

    for pdf in pdf_files:

        pdf_text = extract_pdf_text(pdf)

        combined_text += pdf_text + "\n"

    return combined_text


if __name__ == "__main__":

    ticker = "TSLA"

    print(f"\nBuilding ESG dataset for {ticker}\n")

    text = build_company_text(ticker)

    print("\nCalculating ESG scores...\n")

    result = calculate_esg_scores(text)

    output_path = OUTPUT_DIR / f"{ticker}.json"

    with open(output_path, "w") as f:

        json.dump(result, f, indent=4)

    print(f"\nSaved ESG results to:\n")

    print(output_path)