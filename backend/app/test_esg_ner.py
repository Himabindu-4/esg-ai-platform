from transformers import pipeline

ner = pipeline(
    "token-classification",
    model="app/models/esg_ner_model",
    tokenizer="app/models/esg_ner_model",
    aggregation_strategy="simple"
)

text = "carbon emissions reduced by 60 percent"

results = ner(text)

for r in results:
    print(r)