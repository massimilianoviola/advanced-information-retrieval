import json
import os
from elasticsearch import Elasticsearch

os.makedirs("./task_04/outputs", exist_ok=True)
os.makedirs("./task_04/results", exist_ok=True)

# ? add Italian and Czech
# ? is English also needed?
LANGUAGES = ["DE"]
DATA_SETS = ["cacm", "med", "npl"]
MODEL_SHORTCUT = "ml_miniLM_L12_v2"

es = Elasticsearch("http://localhost:9200")

query_template = {
    "script_score": {
        "query": {
            "match_all": {}
        },
        "script": {
            "source":
                "dotProduct(params.query_embedd, 'EMBEDD') + 1.0",  # dotProduct is the same as cosineSimilarity on normalized vectors
            "params": {
                "query_embedd": None
            }
        }
    }
}

# execute search for each data set and language
for data_set in DATA_SETS:
    for language in LANGUAGES:
        index_name = f"{MODEL_SHORTCUT}_{data_set}"

        queries_file = f"./data/{data_set}/{MODEL_SHORTCUT}_embed_queries_{language}.json"
        results_file = f"./task_04/outputs/{MODEL_SHORTCUT}_{data_set}_{language}.txt"

        with open(queries_file, "r") as queries, open(results_file, "w") as results:
            for query in json.loads(queries.read())["QUERIES"]:
                response = es.search(index=index_name, query=query_template, size=1000)
                query_id = query["QUERYID"]
                for rank, hit in enumerate(response["hits"]["hits"]):
                    print(query_id,
                          "Q0",
                          hit["_source"]["DOCID"],
                          rank + 1,
                          hit["_score"],
                          "tag",
                          sep="\t",
                          file=results)

# evaluate results with trec_eval
for data_set in DATA_SETS:
    for language in LANGUAGES:
        os.system(
            f"trec_eval -m map -q ./data/{data_set}/qrels-treceval.txt ./task_04/outputs/{MODEL_SHORTCUT}_{data_set}_{language}.txt > ./task_04/results/map_{MODEL_SHORTCUT}_{data_set}_{language}.txt"
        )
