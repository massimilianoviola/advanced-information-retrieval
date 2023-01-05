import os

DATA_SETS = ["cacm", "med", "npl"]

# sentence transformers models
MODELS = [
    "paraphrase-multilingual-MiniLM-L12-v2", "distiluse-base-multilingual-cased-v1",
    "paraphrase-multilingual-mpnet-base-v2"
]
MODEL_SHORTCUTS = ["ml_miniLM_L12_v2", "dbmlc_v1", "ml_mpnet_base_v2"]

# language settings + DeepL API key
API_KEY_FILE = './task_04/deepl_auth.key'
LANGUAGES = ["EN", "DE"]
# ? Italian and Czech
# LANGUAGES = ["EN", "DE", "IT", "CS"]

# model fine-tuning
MODEL_PATH = f"./task_04/models/"
EPOCHS = 1
WARMUP_STEPS = 500  # ? fraction of data set size
BATCH_SIZE = 16

# ElasticSearch
ES_URL = "http://localhost:9200"  # todo

for data_set in DATA_SETS:
    for model, model_shortcut in zip(MODELS, MODEL_SHORTCUTS):
        # translate queries to target language
        for language in LANGUAGES:
            os.system(
                f"python3 translate.py -l EN -s ./data/{data_set}/queries.json -t ./data/{data_set}/queries_{language}.json -k ./deepl_auth.key"
            )

        model_path = f"./task_04/models/{data_set}_{model_shortcut}/"

        # finetune models on the data set
        os.system(
            f"python3 finetune.py -m {model} -d ./data/{data_set}/{data_set}.json -d {model_path} -e {EPOCHS} -w {WARMUP_STEPS} -b {BATCH_SIZE}"
        )

        # convert documents to embeddings and create index in ElasticSearch
        print(f"Embedding docs and creating index for {data_set}...")
        os.system(
            f"python3 embedding_index.py -f ./data/{data_set}/{data_set}.json -i {model_shortcut.lower()}_{data_set}_finetuned -m {model_path} -v 0"
        )

        # search on indexed documents using queries in target languages
        for language in LANGUAGES:
            print(f"Searching for {language} queries in {data_set}...")
            os.system(
                f"python3 embedding_search.py -q ./data/{data_set}/queries_{language}.json -i {model_shortcut.lower()}_{data_set}_finetuned -m {model_path} -o ./task_04/outputs/{model_shortcut}_{data_set}_{language}.txt"
            )

            # evaluating the search results with trec_eval
            os.system(
                f"trec_eval -m map -q ./data/{data_set}/qrels-treceval.txt ./task_04/outputs/{model_shortcut}_{data_set}_{language}.txt > ./task_04/results/map_{model_shortcut}_{data_set}_{language}.txt"
            )
