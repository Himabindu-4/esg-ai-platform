import re
from pathlib import Path

from app.pipelines.parse_filings import parse_company_filings


SECTION_PATTERNS = {
    "risk_factors": [
        r"item\s+1a\.\s+risk\s+factors"
    ],

    "management_discussion": [
        r"item\s+7\.\s+management.s\s+discussion\s+and\s+analysis"
    ],

    "environmental": [
        r"environment",
        r"sustainability",
        r"carbon",
        r"climate",
        r"emissions",
        r"renewable"
    ],

    "governance": [
        r"governance",
        r"board\s+of\s+directors",
        r"ethics",
        r"compliance"
    ]
}


def extract_sections(text):

    extracted = {}

    lower_text = text.lower()

    for section_name, patterns in SECTION_PATTERNS.items():

        matches = []

        for pattern in patterns:

            found = re.finditer(pattern, lower_text)

            for match in found:

                start = max(match.start() - 1000, 0)

                end = min(match.end() + 4000, len(text))

                snippet = text[start:end]

                matches.append(snippet)

        extracted[section_name] = matches

    return extracted


if __name__ == "__main__":

    filings = parse_company_filings("AAPL")

    if filings:

        sample_text = filings[0]

        sections = extract_sections(sample_text)

        for section, content in sections.items():

            print(f"\n{'='*60}")
            print(f"SECTION: {section.upper()}")
            print(f"{'='*60}")

            print(f"Matches Found: {len(content)}")

            if content:

                print("\nSample Extract:\n")

                print(content[0][:3000])