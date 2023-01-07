import argparse
import json
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", type=str, help="Input file with documents to index")
parser.add_argument("-i", "--indexname", type=str, help="Elasticsearch index name")
parser.add_argument("-m", "--model", type=str, help="SentenceTransformer model to use")
parser.add_argument("-v", "--verbose", type=int, default=1, choices=[0, 1], help="Increase output verbosity")
args = parser.parse_args()

# connect to the server
es = Elasticsearch("http://localhost:9200", max_retries=5, retry_on_timeout=True)

# initialize the model
model = SentenceTransformer(args.model)

# configure index
if not es.indices.exists(index=args.indexname):
    mappings =  {
            "properties": {
                "EMBEDD": {"type": "dense_vector", "dims": model.get_sentence_embedding_dimension()}
            }
        }
    es.indices.create(index=args.indexname, mappings=mappings)
else:
    if args.verbose:
        print(f"Index with name '{args.indexname}' already exist. Delete it with this command: curl -X DELETE \"localhost:9200/{args.indexname}\"")
    exit(0)

if args.verbose:
    print(f"Indexing {args.filename} documents in index {args.indexname} with {args.model} ...")

# open the document file passed to the command line
with open(args.filename, "r") as infile:
    ndoc = 0
    for doc in infile:
        if len(doc) > 0:
            ndoc += 1
            # read document record in JSON format
            record = json.loads(doc)
            this_id = record["DOCID"]
            # encode text and remove it
            text = record.pop("TEXT")
            record["EMBEDD"] = model.encode(text, normalize_embeddings=True, show_progress_bar=False).tolist()
            if args.verbose:
                print(args.filename, ndoc, this_id, "...", end=" ")
            # insert record into index
            res = es.index(
                index=args.indexname,
                id=this_id,
                document=record
            )
            if args.verbose:
                print("added", end="\r")
    if args.verbose:
        print("\ndone")
