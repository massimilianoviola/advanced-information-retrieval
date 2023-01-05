import json
from elasticsearch import Elasticsearch
from constants import *

es = Elasticsearch(ES_URL)

for data_set in DATA_SETS:
    # todo separate index for fine-tuned models
    index_name = f"{MODEL_SHORTCUT}_{data_set}_finetuned".lower()  # index names must be lowercase

    # create index
    if not es.indices.exists(index=index_name):
        index_mappings = {
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
        es.options(ignore_status=400)
        es.indices.create(index=index_name, mappings=index_mappings)
        print(f"Created index {index_name}")

    # index documents
    with open(f"./data/{data_set}/{MODEL_SHORTCUT}_embed_{data_set}.json", "r") as docs:
        doc_count = 0
        for doc in docs:
            doc = json.loads(doc)
            es.index(index=index_name, id=doc["DOCID"], document=doc)
            doc_count += 1
            if doc_count % 500 == 0:
                print(f"\tIndexed {doc_count} documents for {data_set}")
        print(f"Indexed all documents for {data_set}")