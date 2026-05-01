def split_esg_evidence(raw_text_list):
    """
    Convert raw paragraphs into ESG categories
    """

    environmental_keywords = [
        "emission", "carbon", "climate", "energy",
        "renewable", "water", "waste", "environment"
    ]

    social_keywords = [
        "employee", "labor", "diversity", "human rights",
        "community", "safety"
    ]

    governance_keywords = [
        "board", "governance", "audit", "compliance",
        "ethics", "shareholder"
    ]

    env = []
    soc = []
    gov = []

    for text in raw_text_list:

        t = text.lower()

        if any(k in t for k in environmental_keywords):
            env.append(text)

        elif any(k in t for k in social_keywords):
            soc.append(text)

        elif any(k in t for k in governance_keywords):
            gov.append(text)

    return {
        "environmental": env,
        "social": soc,
        "governance": gov
    }