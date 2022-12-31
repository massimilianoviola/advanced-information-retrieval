import json
import os
from elasticsearch import Elasticsearch
from constants import MODEL_SHORTCUTS
from constants import DATA_SETS

os.makedirs("outputs", exist_ok=True)
os.makedirs("results", exist_ok=True)

es = Elasticsearch("http://localhost:9200")

query_template = {
    "script_score": {
        "query": {
            "match_all": {}
        },
        "script": {
            "source": "dotProduct(params.query_embedd, 'EMBEDD') + 1.0", # dotProduct is the same as cosineSimilarity on normalized vectors
            "params": {"query_embedd": None}
        }
    }
}

query_params = query_template["script_score"]["script"]["params"]

for model in MODEL_SHORTCUTS:
    for data_set in DATA_SETS:
        index_name = f"{model}_{data_set}"
        with open(f"../data/{data_set}/{model}_embed_queries.json", "r") as queries, open(f"./outputs/{model}_{data_set}.txt", "w") as results:
            for query in json.loads(queries.read())["QUERIES"]:
                query_params["query_embedd"] = query["QUERY"]
                response = es.search(index=index_name, query=query_template, size=1000)
                query_id = query["QUERYID"]
                for rank, hit in enumerate(response["hits"]["hits"]):
                    print(query_id, "Q0", hit["_source"]["DOCID"], rank + 1, hit["_score"], "tag", sep="\t", file=results)

    for data_set in DATA_SETS:
        os.system(f"trec_eval -m map -q ../data/{data_set}/qrels-treceval.txt ./outputs/{model}_{data_set}.txt > ./results/map_{model}_{data_set}.txt")
