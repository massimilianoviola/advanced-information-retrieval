import json
import os
from elasticsearch import Elasticsearch

os.makedirs("output", exist_ok=True)
os.makedirs("result", exist_ok=True)

es = Elasticsearch("http://localhost:9200")

query_template = {
    "script_score": {
        "query": {
            "match_all": {}
        },
        "script": {
            "source": "cosineSimilarity(params.query_embedd, 'EMBEDD') + 1.0",
            "params": {"query_embedd": None}
        }
    }
}

query_params = query_template["script_score"]["script"]["params"]

for data_set in ["cacm", "med", "npl"]:
    index_name = f"glove_{data_set}"
    with open(f"../data/{data_set}/glove_embed_queries.json", "r") as queries, open(f"./output/{data_set}.txt", "w") as results:
        for query in json.loads(queries.read())["QUERIES"]:
            query_params["query_embedd"] = query["QUERY"]
            response = es.search(index=index_name, query=query_template, size=1000)
            query_id = query["QUERYID"]
            for rank, hit in enumerate(response["hits"]["hits"]):
                print(query_id, hit["_source"]["DOCID"], rank + 1, hit["_score"], "tag", sep="\t", file=results)
