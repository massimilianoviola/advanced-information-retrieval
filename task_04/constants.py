MODELS = ["ml_miniLM_L12_v2", "dbmlc_v1", "ml_mpnet_base_v2"]

MODEL_SHORTCUT = "ml_miniLM_L12_v2"
MODEL_SHORTCUT = "dbmlc_v1"
MODEL_SHORTCUT = "ml_mpnet_base_v2"

# language settings + DeepL API key
API_KEY_FILE = './task_04/deepl_auth.key'
LANGUAGES = ["EN", "DE"]
# ? Italian and Czech
# LANGUAGES = ["EN", "DE", "IT", "CS"]
SOURCE_LANG = 'EN'

DATA_SETS = ["cacm", "med", "npl"]

# set variables based on selected model shortcut
if (MODEL_SHORTCUT == "ml_miniLM_L12_v2"):
    MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
    EMBEDD_DIMENSION = 384
elif (MODEL_SHORTCUT == "ml_mpnet_base_v2"):
    MODEL = "paraphrase-multilingual-mpnet-base-v2"
    EMBEDD_DIMENSION = 768
elif (MODEL_SHORTCUT == "dbmlc_v1"):
    MODEL = "distiluse-base-multilingual-cased-v1"
    EMBEDD_DIMENSION = 512

# model fine-tuning
MODEL_PATH = f"./task_04/models/"
EPOCHS = 1
WARMUP_STEPS = 500  # ? fraction of data set size
BATCH_SIZE = 16

# ElasticSearch
ES_URL = "http://localhost:9200"