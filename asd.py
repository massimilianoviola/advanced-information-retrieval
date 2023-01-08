import os

DATASETS = ["cacm", "med", "npl"]

# sentence transformers models
MODELS = [
    "paraphrase-multilingual-MiniLM-L12-v2", "distiluse-base-multilingual-cased-v1",
    "paraphrase-multilingual-mpnet-base-v2"
]
MODEL_SHORTCUTS = ["ml_miniLM_L12_v2", "dbmlc_v1", "ml_mpnet_base_v2"]

# language settings + DeepL API key
LANGUAGES = ["EN", "DE"]
# ? Italian and Czech
# LANGUAGES = ["EN", "DE", "IT", "CS"]

# model fine-tuning
USE_EXISTING_MODEL = True  # reuse already fine-tuned models
MODEL_PATH = f"./task_04/models/"
EPOCHS = 1
WARMUP_STEPS = 500  # ? fraction of data set size
BATCH_SIZE = 16

# create trec_eval command which evaluates all results
# separated by newlines
trec_eval_command = ""
for dataset in DATASETS:
    for language in LANGUAGES:
        for model_shortcut in MODEL_SHORTCUTS:
            trec_eval_command += "./trec_eval -m map -q "
            trec_eval_command += f"./data/{dataset}/qrels-treceval.txt ./task_04/outputs/{model_shortcut}_{dataset}_{language}_ger_docs.txt > ./task_04/results/map_{model_shortcut}_{dataset}_{language}_ger_docs.txt\n"

print(trec_eval_command)
