import fitz
import re
from pathlib import Path


PDF_DIR = Path(
    "app/data/raw/sustainability_reports"
)


def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_pdf_text(pdf_path):

    doc = fitz.open(pdf_path)

    full_text = []

    for page in doc:

        text = page.get_text()

        full_text.append(text)

    return clean_text(" ".join(full_text))


if __name__ == "__main__":

    pdf_files = list(PDF_DIR.glob("*.pdf"))

    print(f"\nPDF Files Found: {len(pdf_files)}\n")

    for pdf in pdf_files:

        print("=" * 80)

        print(f"\nProcessing: {pdf.name}\n")

        text = extract_pdf_text(pdf)

        print(f"\nExtracted Characters: {len(text)}\n")

        print("\nSAMPLE TEXT:\n")

        print(text[:5000])