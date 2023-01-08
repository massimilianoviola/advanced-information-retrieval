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
MODEL_FOLDER = f"./task_04/models"  # where to store fine-tuned models
EPOCHS = 1
WARMUP_STEPS = 500  # ? fraction of data set size
BATCH_SIZE = 16

for dataset in DATASETS:
    for model, model_shortcut in zip(MODELS, MODEL_SHORTCUTS):
        # translate English queries to target language
        for language in LANGUAGES:
            os.system(  # see translate.py regarding DeepL API key
                f"python3 translate.py -l {language} -s ./data/{dataset}/queries.json -t ./data/{dataset}/queries_{language}.json -d ./deepl_auth.key"
            )

        # fine-tune models on the data set
        model_path = f"{MODEL_FOLDER}/{model_shortcut}_{dataset}/"
        print(f"Fine-tuning {model} on {dataset}...")
        os.system(
            f"python3 finetune.py -m {model} -d ./data/{dataset}/{dataset}.json -f {model_path} -e {EPOCHS} -w {WARMUP_STEPS} -b {BATCH_SIZE}"
        )

        # convert documents to embeddings and create index in ElasticSearch
        print(f"Embedding docs and creating index for {dataset}...")
        os.system(
            f"python3 embedding_index.py -f ./data/{dataset}/{dataset}.json -i {model_shortcut.lower()}_{dataset}_fine_tuned -m {model_path} -v 0"
        )

        # search on indexed documents using queries in target languages
        for language in LANGUAGES:
            print(f"Searching for {language} queries in {dataset}...")
            os.system(
                f"python3 embedding_search.py -q ./data/{dataset}/queries_{language}.json -i {model_shortcut.lower()}_{dataset}_fine_tuned -m {model_path} -o ./task_04/outputs/{model_shortcut}_{dataset}_{language}.txt"
            )

            # evaluating the search results with trec_eval
            print(f"Evaluating {model_shortcut} on {dataset} with {language} queries...")
            os.system(
                f"trec_eval -m map -q ./data/{dataset}/qrels-treceval.txt ./task_04/outputs/{model_shortcut}_{dataset}_{language}.txt > ./task_04/results/map_{model_shortcut}_{dataset}_{language}.txt"
            )