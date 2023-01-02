import json
from elasticsearch import Elasticsearch

DATA_SETS = ["cacm", "med", "npl"]
MODEL_SHORTCUT = "ml_miniLM_L12_v2"
EMBEDD_DIMENSION = 384

es = Elasticsearch("http://localhost:9200")

for data_set in DATA_SETS:
    index_name = f"{MODEL_SHORTCUT}_{data_set}"

    # create index
    if not es.indices.exists(index=index_name):
        index_config = {
            "mappings": {
                "properties": {
                    "DOCID": {
                        "type": "text"
                    },
                    "EMBEDD": {
                        "type": "dense_vector",
                        "dims": EMBEDD_DIMENSION
                    }
                }
            }
        }
        es.indices.create(index=index_name, body=index_config, ignore=400)

    # index documents
    with open(f"./data/{data_set}/{MODEL_SHORTCUT}_embed_{data_set}.json", "r") as docs:
        for doc in docs:
            doc = json.loads(doc)
            es.index(index=index_name, id=doc["DOCID"], document=doc)
