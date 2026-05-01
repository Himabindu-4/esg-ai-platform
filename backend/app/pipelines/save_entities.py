import json
from pathlib import Path

from app.pipelines.parse_filings import parse_company_filings
from app.pipelines.pdf_esg_parser import extract_pdf_text
from app.pipelines.esg_entity_extractor import extract_esg_entities


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

    ticker = "AAPL"

    print(f"\nBuilding entity dataset for {ticker}\n")

    text = build_company_text(ticker)

    entities = extract_esg_entities(text)

    output_path = OUTPUT_DIR / f"{ticker}_entities.json"

    with open(output_path, "w") as f:

        json.dump(entities, f, indent=4)

    print(f"\nSaved entities to:\n")

    print(output_path)