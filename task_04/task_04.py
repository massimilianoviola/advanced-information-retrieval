import os

DATASETS = ["cacm", "med", "npl"]
LANGUAGES = ["EN", "DE"]

# multi-lingual sentence transformers models
MODELS = ["paraphrase-multilingual-MiniLM-L12-v2", "paraphrase-multilingual-mpnet-base-v2"]
MODEL_SHORTCUTS = ["ml_miniLM_L12_v2", "ml_mpnet_base_v2"]

# model fine-tuning parameters
FINETUNE_ENABLED = False
MODEL_FOLDER = f"./task_04/models"
EPOCHS = 10
WARMUP_STEPS = 50
BATCH_SIZE = 16

for dataset in DATASETS:
    for model, model_shortcut in zip(MODELS, MODEL_SHORTCUTS):
        # translate queries to target language
        for language in LANGUAGES:
            # see translate.py regarding DeepL API key
            os.system(f"python3 translate.py -l {language} -s ./data/{dataset}/queries.json -t ./data/{dataset}/queries_{language}.json -d ./deepl_auth.key")

        # fine-tune models on the data set
        model_path = f"{model}"
        if FINETUNE_ENABLED:
            model_path = f"{MODEL_FOLDER}/{model_shortcut}_{dataset}/"
            print(f"Fine-tuning {model} on {dataset}...")
            os.system(f"python3 finetune.py -m {model} -d ./data/{dataset}/{dataset}.json -f {model_path} -e {EPOCHS} -w {WARMUP_STEPS} -b {BATCH_SIZE}")

        # convert documents to embeddings and create index in ElasticSearch
        print(f"Embedding docs and creating index for {dataset}...")
        index = f"{model_shortcut.lower()}_{dataset}" + ("_finetuned" if FINETUNE_ENABLED else "_pretrained")
        os.system(f"python3 embedding_index.py -f ./data/{dataset}/{dataset}.json -i {index} -m {model_path} -v 0")

        # search on indexed documents using queries in target languages
        output_folder = "./task_04/outputs/" + ("finetuned" if FINETUNE_ENABLED else "pretrained")
        results_folder = "./task_04/results/" + ("finetuned" if FINETUNE_ENABLED else "pretrained")
        for language in LANGUAGES:
            os.system(f"python3 embedding_search.py -q ./data/{dataset}/queries_{language}.json -i {index} -m {model_path}"
                        f" -o {output_folder}/{model_shortcut}_{dataset}_{language}.txt")

            os.system(
                f"trec_eval -m map -q ./data/{dataset}/qrels-treceval.txt {output_folder}/{model_shortcut}_{dataset}_{language}.txt"
                f" > {results_folder}/map_{model_shortcut}_{dataset}_{language}.txt")

# index on German docs instead of English
for dataset in DATASETS:
    for model, model_shortcut in zip(MODELS, MODEL_SHORTCUTS):
        # translate queries to target language
        for language in LANGUAGES:
            # see translate.py regarding DeepL API key
            os.system(f"python3 translate.py -l {language} -s ./data/{dataset}/queries.json -t ./data/{dataset}/queries_{language}.json -d ./deepl_auth.key")

        # fine-tune models on the data set
        model_path = f"{model}"
        if FINETUNE_ENABLED:
            model_path = f"{MODEL_FOLDER}/{model_shortcut}_{dataset}/"
            print(f"Fine-tuning {model} on {dataset}...")
            os.system(f"python3 finetune.py -m {model} -d ./data/{dataset}/{dataset}.json -f {model_path} -e {EPOCHS} -w {WARMUP_STEPS} -b {BATCH_SIZE}")

        # convert documents to embeddings and create index in ElasticSearch
        print(f"Embedding docs and creating index for {dataset}...")
        index = f"{model_shortcut.lower()}_{dataset}_DE"
        os.system(f"python3 embedding_index.py -f ./data/{dataset}/ger_{dataset}.json -i {index} -m {model_path} -v 0")

        # search on indexed documents using queries in target languages
        for language in LANGUAGES:
            os.system(
                f"python3 embedding_search.py -q ./data/{dataset}/queries_{language}.json -i {index} -m {model_path}"
                f" -o ./task_04/outputs/DE/{model_shortcut}_{dataset}_{language}.txt")

            os.system(
                f"trec_eval -m map -q ./data/{dataset}/qrels-treceval.txt ./task_04/outputs/DE/{model_shortcut}_{dataset}_{language}.txt"
                f" > ./task_04/results/DE/map_{model_shortcut}_{dataset}_{language}.txt")

# mono-lingual sentence transformers models
MODELS = ["all-MiniLM-L12-v2", "all-mpnet-base-v2"]
MODEL_SHORTCUTS = ["miniLM_L12_v2", "mpnet_base_v2"]

# use monolingual sentence transformers instead of multilingual
# translate queries to English before searching
for dataset in DATASETS:
    for model, model_shortcut in zip(MODELS, MODEL_SHORTCUTS):
        # translate queries to English
        for language in LANGUAGES:
            os.system(f"python3 translate.py -l EN -s ./data/{dataset}/queries_{language}.json -t ./data/{dataset}/queries_from_{language}.json -d ./deepl_auth.key")

        # convert documents to embeddings and create index in ElasticSearch
        index = f"{model_shortcut.lower()}_{dataset}_monolingual"
        os.system(f"python3 embedding_index.py -f ./data/{dataset}/{dataset}.json -i {index} -m {model} -v 0")

        # search on indexed documents using English queries
        for language in LANGUAGES:
            os.system(
                f"python3 embedding_search.py -q ./data/{dataset}/queries_from_{language}.json -i {index} -m {model}"
                f" -o ./task_04/outputs/monolingual/{model_shortcut}_{dataset}_{language}.txt")

            os.system(
                f"trec_eval -m map -q ./data/{dataset}/qrels-treceval.txt ./task_04/outputs/monolingual/{model_shortcut}_{dataset}_{language}.txt"
                f" > ./task_04/results/monolingual/map_{model_shortcut}_{dataset}_{language}.txt")
