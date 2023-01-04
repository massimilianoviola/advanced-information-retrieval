import json
import os
from elasticsearch import Elasticsearch
import constants

if __name__ == '__main__':

    es = Elasticsearch("http://localhost:9200")

    query_template = {
        "script_score": {
            "query": {
                "match_all": {}
            },
            # https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-scripting-using.html
            "script": {
                "source":  # "cosineSimilarity(params.query_embedd, 'EMBEDD') + 1.0",  # ! does this work?
                # dotProduct is the same as cosineSimilarity on normalized vectors
                    "dotProduct(params.query_embedd, 'EMBEDD') + 1.0",
                "params": {
                    "query_embedd": None
                }
            }
        }
    }

    query_params = query_template["script_score"]["script"]["params"]

    # execute search for each data set and language

    for data_set in constants.DATA_SETS:
            index_name = f"{data_set}".lower()

            queries_file = f"/home/manuel/PycharmProjects/advanced-information-retrieval/data/{data_set}/queries.json"
            outputs_file = f"/home/manuel/PycharmProjects/advanced-information-retrieval/task_01/outputs/{data_set}_summarize.txt"

            with open(queries_file, "r") as queries, open(outputs_file, "w") as outputs:
                for query in json.loads(queries.read())["QUERIES"]:
                    query_params["query_embedd"] = query["QUERY"]
                    response = es.search(index=index_name, query=query_template,
                                         size=1000)  # return 1000 most relevant documents
                    query_id = query["QUERYID"]
                    for rank, hit in enumerate(response["hits"]["hits"]):
                        # input format: query_id Q0 doc_id rank_of_document score_of_document tag_for_current_run
                        print(query_id,
                              "Q0",
                              hit["_source"]["DOCID"],
                              rank + 1,
                              hit["_score"],
                              "tag",
                              sep="\t",
                              file=outputs)

    # evaluate results with trec_eval
    for data_set in constants.DATA_SETS:
            # calculate Mean Average Precision (MAP) using existing relevancies (qrels-treceval.txt) and search results (outputs)
            # store in results: map queryID score
            os.system(
                f"trec_eval -m map -q /home/manuel/PycharmProjects/advanced-information-retrieval/data/{data_set}/qrels-treceval.txt /home/manuel/PycharmProjects/advanced-information-retrieval/task_01/outputs/{data_set}_summarize.txt > /home/manuel/PycharmProjects/advanced-information-retrieval/task_01/results/{data_set}_summarize.txt"
            )

