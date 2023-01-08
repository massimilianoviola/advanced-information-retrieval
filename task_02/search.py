import argparse
import json
from elasticsearch import Elasticsearch
import constants

# connect to the server
es = Elasticsearch("http://localhost:9200")

filename = "/home/manuel/PycharmProjects/advanced-information-retrieval/data/" + constants.QUERY_FILE + ".json"
# load queries in JSON format
with open(filename, "r") as infile:
    queries = json.loads(infile.read())
    queries_list = queries["QUERIES"]

for index in constants.INDEX_NAMES_TO_SEARCH:
    output_filename = f"/home/manuel/PycharmProjects/advanced-information-retrieval/task_02/outputs/{index}_bm25"
    with open(output_filename, "w") as output:
        for query in queries_list:
            num = query["QUERYID"]
            text = query["QUERY"]
            query_dict = {
                "bool": {
                    "should": [
                        { "match": { "TEXT": text } }
                    ]
                }
            }
            response = es.search(
                index=index,
                query=query_dict,
                size=1000
            )

            rank = 0
            for hit in response["hits"]["hits"]:
                rank += 1
                docid = hit["_source"]["DOCID"]
                score = hit["_score"]
                print(num, "Q0", docid, rank, score, "tag", sep="\t",file=output)

