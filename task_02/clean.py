import os
from constants import MODEL_SHORTCUTS
from constants import DATA_SETS

for model in MODEL_SHORTCUTS:
    for data_set in DATA_SETS:
        os.system(f"curl -X DELETE 'http://localhost:9200/{model}_{data_set}'")
        os.system(f"rm -rf ../data/{data_set}/{model}_embed_{data_set}.json")
        os.system(f"rm -rf ../data/{data_set}/{model}_embed_queries.json")

os.system(f"rm -rf ./outputs")
os.system(f"rm -rf ./results")
