import argparse
import json
from elasticsearch import Elasticsearch


parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="Input file with documents to index")
parser.add_argument("indexname", type=str, help="Elasticsearch index name")
parser.add_argument("-v", "--verbose", type=int, default=1, choices=[0, 1], help="Increase output verbosity")
args = parser.parse_args()

# connect to the server
es = Elasticsearch("http://localhost:9200", max_retries=5, retry_on_timeout=True)

if args.verbose:
    print(f"Indexing {args.filename} documents in index {args.indexname} ...")
# open the document file passed to the command line
with open(args.filename, "r") as infile:
    ndoc = 0
    for doc in infile:
        if len(doc) > 0:
            ndoc += 1
            # read document record in JSON format
            record = json.loads(doc)
            this_id = record["DOCID"]
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
