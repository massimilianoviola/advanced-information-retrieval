import json
from elasticsearch import Elasticsearch
from constants import MODEL_SHORTCUTS
from constants import DATA_SETS
from constants import EMBEDD_DIMENSIONS

es = Elasticsearch("http://localhost:9200")

for model, dimensions in zip(MODEL_SHORTCUTS, EMBEDD_DIMENSIONS):
    for data_set in DATA_SETS:
        index_name = f"{model}_{data_set}"
        if not es.indices.exists(index=index_name):
            index_config = {
                "mappings": {
                    "properties": {
                        "DOCID": {"type": "text"},
                        "EMBEDD": {"type": "dense_vector", "dims": dimensions}
                    }
                }
            }
            es.indices.create(index=index_name, body=index_config, ignore=400)

        with open(f"../data/{data_set}/{model}_embed_{data_set}.json", "r") as docs:
            for doc in docs:
                doc = json.loads(doc)
                es.index(index=index_name, id=doc["DOCID"], document=doc)

