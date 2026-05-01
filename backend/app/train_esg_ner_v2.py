from transformers import pipeline

print("\nLoading ESG NER model...\n")

ner = pipeline(
    "ner",
    model="dslim/bert-base-NER",
    aggregation_strategy="simple"
)

sample_text = """

Apple reduced carbon emissions by 60 percent.
Renewable energy usage reached 100 percent.
Water usage declined by 25 percent.

"""

results = ner(sample_text)

print("\nESG ENTITY RESULTS\n")

for r in results:
    print(r)