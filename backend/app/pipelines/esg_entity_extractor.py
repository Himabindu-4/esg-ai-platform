import re
from pathlib import Path

from app.pipelines.parse_filings import parse_company_filings
from app.pipelines.pdf_esg_parser import extract_pdf_text


PDF_DIR = Path(
    "app/data/raw/sustainability_reports"
)


ESG_PATTERNS = {

    # -----------------------------------
    # CARBON / EMISSIONS
    # -----------------------------------

    "carbon_reduction_percent": [

        r"(\d+(?:\.\d+)?)\s*percent lower than 2015 levels",

        r"(\d+(?:\.\d+)?)\s*%\s*lower"
    ],

    "carbon_neutral_goal": [

        r"carbon neutral",

        r"net zero"
    ],

    # -----------------------------------
    # RECYCLED MATERIALS
    # -----------------------------------

    "recycled_materials_percent": [

        r"(\d+(?:\.\d+)?)\s*percent of the materials",

        r"(\d+(?:\.\d+)?)\s*percent recycled",

        r"recycled content"
    ],

    # -----------------------------------
    # WATER
    # -----------------------------------

    "water_saved": [

        r"(\d+(?:\.\d+)?)\s*billion gallons",

        r"(\d+(?:,\d+)*)\s*gallons of freshwater"
    ],

    # -----------------------------------
    # PACKAGING
    # -----------------------------------

    "fiber_packaging": [

        r"100 percent fiber-based packaging"
    ],

    # -----------------------------------
    # RENEWABLE ENERGY
    # -----------------------------------

    "renewable_energy": [

        r"renewable energy",

        r"clean electricity"
    ],

    # -----------------------------------
    # EMPLOYEES
    # -----------------------------------

    "employee_count": [

        r"had\s+(\d{1,3}(?:,\d{3})+)\s+employees"
    ]
}


def extract_esg_entities(text):

    extracted = []

    lower_text = text.lower()

    for entity_name, patterns in ESG_PATTERNS.items():

        for pattern in patterns:

            matches = re.finditer(pattern, lower_text)

            for match in matches:

                try:

                    if match.groups():

                        value = match.group(1)

                    else:

                        value = "FOUND"

                    start = max(match.start() - 300, 0)

                    end = min(match.end() + 300, len(text))

                    context = text[start:end]

                    extracted.append({

                        "entity": entity_name,

                        "value": value,

                        "context": context
                    })

                except Exception:
                    pass

    return extracted


if __name__ == "__main__":

    all_entities = []

    # -----------------------------------
    # SEC FILINGS
    # -----------------------------------

    filings = parse_company_filings("AAPL")

    for filing in filings:

        entities = extract_esg_entities(filing)

        all_entities.extend(entities)

    # -----------------------------------
    # ESG PDFs
    # -----------------------------------

    pdf_files = list(PDF_DIR.glob("*.pdf"))

    for pdf in pdf_files:

        print(f"\nProcessing PDF: {pdf.name}")

        pdf_text = extract_pdf_text(pdf)

        entities = extract_esg_entities(pdf_text)

        all_entities.extend(entities)

    print(f"\nTotal ESG Entities Found: {len(all_entities)}\n")

    for entity in all_entities[:40]:

        print("=" * 80)

        print(f"ENTITY : {entity['entity']}")

        print(f"VALUE  : {entity['value']}")

        print("\nCONTEXT:\n")

        print(entity["context"][:1000])

        print("\n")