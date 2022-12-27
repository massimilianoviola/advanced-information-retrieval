import json
import sys
from elasticsearch import Elasticsearch


INDEXNAME = "medindex"
VERBOSE = True

# connect to the server
es = Elasticsearch("http://localhost:9200", max_retries=5, retry_on_timeout=True)

# scan document files passed to the command line
nargs = len(sys.argv)
for i in range(1, nargs):
    if VERBOSE:
        print(f"processing {sys.argv[i]} ...")
    # open the document file
    with open(sys.argv[i], "r") as infile:
        ndoc = 0
        for doc in infile:
            if len(doc) > 0:
                ndoc += 1
                # read document record in JSON format
                record = json.loads(doc)
                this_id = record["DOCID"]
                if this_id is not None:
                    if VERBOSE:
                        print(sys.argv[i], ndoc, this_id, "...", end=" ")
                    # insert record into index
                    res = es.index(
                        index=INDEXNAME,
                        id=this_id,
                        document=record
                    )
                    if VERBOSE:
                        print("added")
        if VERBOSE:
            print("done")
if VERBOSE:
    print("done")
