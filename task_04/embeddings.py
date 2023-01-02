import json
from sentence_transformers import SentenceTransformer

# ? add Italian and Czech
# ? is English also needed?
LANGUAGES = ["DE"]
DATA_SETS = ["cacm", "med", "npl"]
MODEL_SHORTCUT = "ml_miniLM_L12_v2"

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# todo fine tune model?

# create embeddings for each data set
for data_set in DATA_SETS:
    input_docs_file = f"./data/{data_set}/{data_set}.json"
    output_queries_file = f"./data/{data_set}/{MODEL_SHORTCUT}_embed_{data_set}.json"

    # read input docs and write embeddings to output docs
    with open(input_docs_file, "r") as input_docs, open(output_queries_file, "w") as output_docs:
        for input_doc in input_docs:
            input_doc = json.loads(input_doc)
            output_doc = {}
            output_doc["DOCID"] = input_doc["DOCID"]
            output_doc["EMBEDD"] = model.encode(input_doc["TEXT"], normalize_embeddings=True).tolist()
            json.dump(output_doc, output_docs, ensure_ascii=False)
        output_docs.write("\n")

    # embed queries for each language
    for language in LANGUAGES:
        input_queries_file = f"./data/{data_set}/queries_{language}.json"
        output_queries_file = f"./data/{data_set}/{MODEL_SHORTCUT}_embed_queries_{language}.json"

        # read input queries and write embeddings to output queries
        with open(input_queries_file, "r") as input_queries, open(output_queries_file, "w") as output_queries:
            output_queries_dict = {"QUERIES": []}
            output_queries_list = output_queries_dict["QUERIES"]
            for input_query in json.loads(input_queries.read())["QUERIES"]:
                output_query = {}
                output_query["QUERYID"] = input_query["QUERYID"]
                output_query["QUERY"] = model.encode(input_query["QUERY"], normalize_embeddings=True).tolist()
                output_queries_list.append(output_query)

            json.dump(output_queries_dict, output_queries, ensure_ascii=False)
