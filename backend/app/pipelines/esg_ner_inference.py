from transformers import pipeline


ner_pipeline = pipeline(

    "token-classification",

    model="app/models/esg_ner_model",

    tokenizer="app/models/esg_ner_model",

    aggregation_strategy="simple",
)


def run_esg_ner(text):

    return ner_pipeline(text)