import argparse
import json
from elasticsearch import Elasticsearch


parser = argparse.ArgumentParser()
parser.add_argument("queries", type=str, help="Input file with queries")
parser.add_argument("indexname", type=str, help="Elasticsearch index name")
args = parser.parse_args()
print(f"Searching index: {args.indexname}")
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
with open(args.queries, "r") as infile:
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
        index=args.indexname,
        query=query_dict,
        size=1000
    )
    res(response["hits"]["hits"], num)
