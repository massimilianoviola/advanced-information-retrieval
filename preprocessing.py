import json
import os
import shutil


######### CONFIG #########

med_output_path = "data/med"
os.makedirs(med_output_path, exist_ok=True)

cacm_output_path = "data/cacm"
os.makedirs(cacm_output_path, exist_ok=True)


######### MEDLINE #########

print("Preprocessing Medline...")

with open("med/MED.ALL") as f, open(os.path.join(med_output_path, "med.json"), "w") as g:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    count = 0
    doc_dict = {}
    for l in lines:
        # id
        if l.startswith(".I"):
            doc_id = l.split(" ")[1].strip()
            doc_dict["DOCID"] = doc_id
        # text content
        elif l.startswith(".W"):
            text = l.strip()[3:]
            doc_dict["TEXT"] = text
            
            json.dump(doc_dict, g) # write doc record to file
            g.write("\n")
            count += 1
            
            doc_dict = {} # reset record
    
    print(f"Wrote {count} records to disk")

with open("med/MED.QRY") as f, open(os.path.join(med_output_path, "queries.json"), "w") as g:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    queries = []
    query_dict = {}
    for l in lines:
        # id
        if l.startswith(".I"):
            query_id = l.split(" ")[1].strip()
            query_dict["QUERYID"] = query_id
        # query text
        elif l.startswith(".W"):
            query = l.strip()[3:]
            query_dict["QUERY"] = query
            
            queries.append(query_dict) # add record to queries list
            query_dict = {} # reset record
    
    # write queries list to file
    dictionary = {"QUERIES": queries}
    json.dump(dictionary, g)
    
    print(f"Wrote {len(queries)} queries to disk")

# relevance judgements already in trec_eval format, just copy
shutil.copyfile("med/MED.REL", os.path.join(med_output_path, "qrels-treceval.txt"))


######### CACM #########

print("Preprocessing CACM...")

with open("cacm/cacm.all") as f, open(os.path.join(cacm_output_path, "cacm.json"), "w") as g:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    count = 0
    doc_dict = {}
    for l in lines:
        # id
        if l.startswith(".I"):
            doc_id = l.split(" ")[1].strip()
            doc_dict["DOCID"] = doc_id
        # title
        elif l.startswith(".T"):
            title = l.strip()[3:]
            doc_dict["TITLE"] = title
        # abstract
        elif l.startswith(".W"):
            abstract = l.strip()[3:]
            doc_dict["ABSTRACT"] = abstract
        # last attribute (a doc is a sequence of lines .I, .T, .W, .B, .A, .N, .X)
        elif l.startswith(".X"):
            json.dump(doc_dict, g) # write doc record to file
            g.write("\n")
            count += 1
            
            doc_dict = {} # reset record
    
    print(f"Wrote {count} records to disk")

with open("cacm/query.text") as f, open(os.path.join(cacm_output_path, "queries.json"), "w") as g:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    queries = []
    query_dict = {}
    for l in lines:
        # id
        if l.startswith(".I"):
            query_id = l.split(" ")[1].strip()
            query_dict["QUERYID"] = query_id
        # query text and last useful attribute
        elif l.startswith(".W"):
            query = l.strip()[3:]
            query_dict["QUERY"] = query
            
            queries.append(query_dict) # add record to queries list
            query_dict = {} # reset record
    
    # write queries list to file
    dictionary = {"QUERIES": queries}
    json.dump(dictionary, g)
    
    print(f"Wrote {len(queries)} queries to disk")

with open("cacm/qrels.text") as f, open(os.path.join(cacm_output_path, "qrels-treceval.txt"), "w") as g:
    lines = f.readlines()
    for l in lines:
        query_id, doc_ic, _, _ = l.split()
        # write in trec_eval format
        g.write(f"{query_id} 0 {doc_ic} 1\n")
