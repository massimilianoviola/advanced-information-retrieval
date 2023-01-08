import argparse
import json
from elasticsearch import Elasticsearch
import constants
import os


es = Elasticsearch("http://localhost:9200", max_retries=5, retry_on_timeout=True)


for filename in constants.FILE_NAMES_TO_INDEX:
    filename = "/home/manuel/PycharmProjects/advanced-information-retrieval/data/"+filename+".json"

    # Extract the file name and extension
    index_name, file_ext = os.path.splitext(filename)
    # Extract the file name only
    index_name = os.path.basename(index_name)
    # open the document file passed to the command line
    index_name = f"{index_name}".lower()  # index names must be lowercase
    #if index doesnt exist
    if not es.indices.exists(index=index_name):
        print(f"Indexing {filename} documents in index {index_name} ...")
        with open(filename, "r") as infile:
            ndoc = 0
            for doc in infile:
                if len(doc) > 0:
                    ndoc += 1
                    # read document record in JSON format
                    record = json.loads(doc)
                    this_id = record["DOCID"]
                    res = es.index(
                        index=index_name,
                        id=this_id,
                        document=record
                    )
                    print(filename, ndoc, this_id, "...","\n", end=" ")
        print("done")
    else:
        print(f"{filename} is already indexed and has the name: {index_name}")
        print("To delete use following command: ")
        print(f"curl -X DELETE \"localhost:9200/{index_name}\"")