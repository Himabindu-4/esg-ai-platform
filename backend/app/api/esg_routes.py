from fastapi import APIRouter

router = APIRouter()


# =========================
# DUMMY EVIDENCE GENERATOR
# =========================
def generate_evidence():
    return {
        "environmental": [
            "Company reduced carbon emissions significantly.",
            "Renewable energy adoption increased."
        ],
        "social": [
            "Improved employee diversity and inclusion.",
            "Enhanced worker safety policies."
        ],
        "governance": [
            "Board independence improved.",
            "Strong corporate governance structure."
        ]
    }


# =========================
# SCORE API
# =========================
@router.get("/score/{ticker}")
def get_score(ticker: str):

    # 🔹 Keep your existing scoring logic
    environmental_score = 80
    social_score = 70
    governance_score = 75
    total_score = round((environmental_score + social_score + governance_score) / 3, 2)

    evidence = generate_evidence()

    # =========================
    # ✅ UPDATED RESPONSE (NEW + OLD)
    # =========================
    return {

        # 🔴 NEW STANDARD FORMAT
        "status": "success",
        "data": {
            "environmental_score": environmental_score,
            "social_score": social_score,
            "governance_score": governance_score,
            "total_score": total_score,
            "evidence_quotes": evidence
        },

        # 🔴 OLD FORMAT (KEEP FOR COMPATIBILITY)
        "environmental_score": environmental_score,
        "social_score": social_score,
        "governance_score": governance_score,
        "total_score": total_score,
        "evidence_quotes": evidence
    }


# =========================
# GREENWASHING API
# =========================
@router.get("/greenwashing/{ticker}")
def greenwashing(ticker: str):

    flags = [
        {
            "sentence": "We aim to become sustainable in the future.",
            "matched_pattern": "vague commitment",
            "risk_level": "HIGH"
        }
    ]

    return {
        "status": "success",
        "data": {
            "flags": flags
        },

        # old compatibility
        "flags": flags
    }