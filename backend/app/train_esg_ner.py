import json
from datasets import Dataset
from transformers import (
    RobertaTokenizerFast,
    RobertaForTokenClassification,
    TrainingArguments,
    Trainer
)

# ============================
# LOAD DATA
# ============================

with open("app/data/esg_ner/train.json", "r") as f:
    raw_data = json.load(f)

# ============================
# LABELS
# ============================

label_list = [
    "O",
    "B-ESG_METRIC",
    "I-ESG_METRIC",
    "B-VALUE",
    "I-VALUE"
]

label_to_id = {l: i for i, l in enumerate(label_list)}

# ============================
# TOKENIZER (IMPORTANT FIX)
# ============================

tokenizer = RobertaTokenizerFast.from_pretrained(
    "roberta-base",
    add_prefix_space=True
)

# ============================
# FORMAT DATASET
# ============================

def convert_data(example):
    return {
        "tokens": example["tokens"],
        "ner_tags": [label_to_id[t] for t in example["ner_tags"]]
    }

dataset = Dataset.from_list(raw_data)
dataset = dataset.map(convert_data)

# ============================
# TOKENIZATION
# ============================

def tokenize(example):

    tokenized = tokenizer(
        example["tokens"],
        is_split_into_words=True,
        truncation=True,
        padding="max_length",
        max_length=64
    )

    word_ids = tokenized.word_ids()

    labels = []
    previous_word = None

    for word_id in word_ids:

        if word_id is None:
            labels.append(-100)

        elif word_id != previous_word:
            labels.append(example["ner_tags"][word_id])

        else:
            labels.append(-100)

        previous_word = word_id

    tokenized["labels"] = labels
    return tokenized

dataset = dataset.map(tokenize)

# ============================
# MODEL
# ============================

model = RobertaForTokenClassification.from_pretrained(
    "roberta-base",
    num_labels=len(label_list)
)

# ============================
# TRAIN
# ============================

training_args = TrainingArguments(
    output_dir="app/models/esg_ner_model",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_steps=1,
    save_strategy="epoch",
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()

# ============================
# SAVE
# ============================

model.save_pretrained("app/models/esg_ner_model")
tokenizer.save_pretrained("app/models/esg_ner_model")

print("\nESG NER TRAINED SUCCESSFULLY\n")