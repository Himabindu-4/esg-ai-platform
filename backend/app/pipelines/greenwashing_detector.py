import re

from app.pipelines.parse_filings import parse_company_filings


GREENWASHING_PATTERNS = [

    r"committed to sustainability",

    r"aim to reduce",

    r"working toward",

    r"strive to",

    r"focused on environmental responsibility",

    r"plans to improve",

    r"dedicated to ESG",

    r"supporting a greener future",

    r"environmentally friendly",

    r"net zero ambition"
]


METRIC_PATTERNS = [

    r"\d+\s*%",

    r"\d+\s*tons",

    r"\d+\s*tonnes",

    r"\d+\s*employees",

    r"\d+\s*metric",

    r"\d+\s*mwh",

    r"\d+\s*co2"
]


def detect_greenwashing(text):

    sentences = re.split(r'(?<=[.!?])\s+', text)

    suspicious = []

    for sentence in sentences:

        lower = sentence.lower()

        matched_phrase = None

        for pattern in GREENWASHING_PATTERNS:

            if re.search(pattern, lower):

                matched_phrase = pattern

                break

        if matched_phrase:

            has_metrics = False

            for metric_pattern in METRIC_PATTERNS:

                if re.search(metric_pattern, lower):

                    has_metrics = True
                    break

            if not has_metrics:

                suspicious.append({

                    "sentence": sentence,

                    "matched_pattern": matched_phrase,

                    "risk_level": "HIGH"
                })

    return suspicious


if __name__ == "__main__":

    filings = parse_company_filings("AAPL")

    all_flags = []

    for filing in filings:

        flags = detect_greenwashing(filing)

        all_flags.extend(flags)

    print(f"\nPotential Greenwashing Signals: {len(all_flags)}\n")

    for flag in all_flags[:20]:

        print("=" * 80)

        print(f"PATTERN: {flag['matched_pattern']}")

        print(f"RISK   : {flag['risk_level']}")

        print("\nSENTENCE:\n")

        print(flag["sentence"])

        print("\n")