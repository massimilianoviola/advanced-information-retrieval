import json
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

for data_set in ["cacm", "med", "npl"]:
    index_name = f"glove_{data_set}"
    if not es.indices.exists(index=index_name):
        index_config = {
            "mappings": {
                "properties": {
                    "id": {"type": "text"},
                    "document": {"type": "dense_vector", "dims": 300}
                }
            }
        }
        es.indices.create(index=index_name, body=index_config, ignore=400)

    with open(f"../data/{data_set}/glove_embed_{data_set}.json", "r") as docs:
        for doc in docs:
            doc = json.loads(doc)
            es.index(index=index_name, id=doc["DOCID"], document=doc)

