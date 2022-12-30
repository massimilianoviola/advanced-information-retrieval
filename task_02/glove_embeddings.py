import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("average_word_embeddings_glove.6B.300d")

for data_set in ["cacm", "med", "npl"]:
    with open(f"../data/{data_set}/{data_set}.json", "r") as input_docs, open(f"../data/{data_set}/glove_embed_{data_set}.json", "w") as output_docs:
        for input_doc in input_docs:
            input_doc = json.loads(input_doc)
            output_doc = {}
            output_doc["DOCID"] = input_doc["DOCID"]
            output_doc["EMBEDD"] = model.encode(input_doc["TEXT"], normalize_embeddings=True).tolist()
            json.dump(output_doc, output_docs, ensure_ascii=False)
            output_docs.write("\n")

    with open(f"../data/{data_set}/queries.json", "r") as input_queries, open(f"../data/{data_set}/glove_embed_queries.json", "w") as output_queries:
        output_queries_dict = {"QUERIES": []}
        output_queries_list = output_queries_dict["QUERIES"]
        for input_query in json.loads(input_queries.read())["QUERIES"]:
            output_query = {}
            output_query["QUERYID"] = input_query["QUERYID"]
            output_query["QUERY"] = model.encode(input_query["QUERY"], normalize_embeddings=True).tolist()
            output_queries_list.append(output_query)
        
        json.dump(output_queries_dict, output_queries, ensure_ascii=False)
        
