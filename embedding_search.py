import argparse
import json
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer


parser = argparse.ArgumentParser()
parser.add_argument("queries", type=str, help="Input file with queries")
parser.add_argument("indexname", type=str, help="Elasticsearch index name")
parser.add_argument("model", type=str, help="SentenceTransformer model to use")
args = parser.parse_args()

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

# initialize the model
model = SentenceTransformer(args.model)

# load queries in JSON format
with open(args.queries, "r") as infile:
    queries = json.loads(infile.read())
    queries_list = queries["QUERIES"]

for query in queries_list:
    num = query["QUERYID"]
    text = query["QUERY"]
    text_embedd = model.encode(text, normalize_embeddings=True, show_progress_bar=False).tolist()
    query_dict = {
        "script_score": {
            "query": {
                "match_all": {}
            },
            "script": {
                "source": "dotProduct(params.query_embedd, 'EMBEDD') + 1.0", # dotProduct equals cosineSimilarity with normalized vectors
                "params": {"query_embedd": text_embedd}
            }
        }
    }
    response = es.search(
        index=args.indexname,
        query=query_dict,
        size=1000
    )
    res(response["hits"]["hits"], num)