import json
import sys
from elasticsearch import Elasticsearch


INDEXNAME = "medindex"
SIZE = 1000

def res(results, query="1", tag="tag"):
    # process query results and output them in trec_eval format
    rank = 0
    for hit in results:
        rank += 1
        docid = hit["_source"]["DOCID"]
        score = hit["_score"]
        print(query, "Q0", docid, rank, score, tag, sep="\t")

# connect to the server
es = Elasticsearch("http://localhost:9200")

# load queries in JSON format
with open(sys.argv[1], "r") as infile:
    queries = json.loads(infile.read())
    queries_list = queries["QUERIES"]

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
        index=INDEXNAME,
        query=query_dict,
        size=SIZE
    )
    res(response["hits"]["hits"], num)
