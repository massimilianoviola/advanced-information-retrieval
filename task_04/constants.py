MODEL_SHORTCUT = "ml_miniLM_L12_v2"
MODEL_SHORTCUT = "ml_mpnet_base_v2"
MODEL_SHORTCUT = "dbmlc_v1"

# ? Italian and Czech
LANGUAGES = ["EN", "DE"]
# LANGUAGES = ["EN", "DE", "IT", "CS"]

DATA_SETS = ["cacm", "med", "npl"]

# set variables based on model shortcut
if (MODEL_SHORTCUT == "ml_miniLM_L12_v2"):
    MODEL = "paraphrase-multilingual-MiniLM-L12-v2"
    EMBEDD_DIMENSION = 384
elif (MODEL_SHORTCUT == "ml_mpnet_base_v2"):
    MODEL = "paraphrase-multilingual-mpnet-base-v2"
    EMBEDD_DIMENSION = 768
elif (MODEL_SHORTCUT == "dbmlc_v1"):
    MODEL = "distiluse-base-multilingual-cased-v1"
    EMBEDD_DIMENSION = 512
