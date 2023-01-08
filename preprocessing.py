import json
import os
import re
import shutil
from deep_translator import GoogleTranslator
from tqdm import tqdm


######### CONFIG #########

med_output_path = "data/med"
os.makedirs(med_output_path, exist_ok=True)

cacm_output_path = "data/cacm"
os.makedirs(cacm_output_path, exist_ok=True)

npl_output_path = "data/npl"
os.makedirs(npl_output_path, exist_ok=True)

translator = GoogleTranslator(source="en", target="de")
TRANSLATE_DOCS = True
TRANSLATE_QUERIES = True


######### MEDLINE #########

print("Preprocessing Medline...")

with open("download/med/MED.ALL") as f, \
     open(os.path.join(med_output_path, "med.json"), "w") as g, \
     open(os.path.join(med_output_path, "ger_med.json"), "w") as h:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    count = 0
    doc_dict = {}
    with tqdm(total=1033) as pbar:
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
                
                if TRANSLATE_DOCS:
                    ger_doc_dict = {
                        "DOCID" : doc_id,
                        "TEXT" : translator.translate(text=text)
                    }
                    json.dump(ger_doc_dict, h, ensure_ascii=False)
                    h.write("\n")
                
                count += 1
                doc_dict = {} # reset record
                pbar.update()
    
    print(f"Wrote {count} records to disk")

with open("download/med/MED.QRY") as f, \
     open(os.path.join(med_output_path, "queries.json"), "w") as g, \
     open(os.path.join(med_output_path, "ger_queries.json"), "w") as h:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    queries = []
    ger_queries = []
    query_dict = {}
    with tqdm(total=30) as pbar:
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
                
                if TRANSLATE_QUERIES:
                    ger_query_dict = {
                        "QUERYID" : query_id,
                        "QUERY" : translator.translate(text=query)
                    }
                    ger_queries.append(ger_query_dict)
                
                query_dict = {} # reset record
                pbar.update()
    
    # write queries list to file
    dictionary = {"QUERIES": queries}
    json.dump(dictionary, g)
    
    ger_dictionary = {"QUERIES": ger_queries}
    json.dump(ger_dictionary, h, ensure_ascii=False)
    
    print(f"Wrote {len(queries)} queries to disk")

# relevance judgements already in trec_eval format, just copy
shutil.copyfile("download/med/MED.REL", os.path.join(med_output_path, "qrels-treceval.txt"))


######### CACM #########

print("Preprocessing CACM...")

with open("download/cacm/cacm.all") as f, \
     open(os.path.join(cacm_output_path, "cacm.json"), "w") as g, \
     open(os.path.join(cacm_output_path, "ger_cacm.json"), "w") as h:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    count = 0
    doc_dict = {}
    with tqdm(total=3204) as pbar:
        for l in lines:
            # id
            if l.startswith(".I"):
                doc_id = l.split(" ")[1].strip()
                doc_dict["DOCID"] = doc_id
            # title
            elif l.startswith(".T"):
                title = l.strip()[3:]
                doc_dict["TEXT"] = title
            # abstract
            elif l.startswith(".W"):
                abstract = l.strip()[3:]
                doc_dict["TEXT"] += ": " + abstract
            # last attribute (a doc is a sequence of lines .I, .T, .W, .B, .A, .N, .X)
            elif l.startswith(".X"):
                json.dump(doc_dict, g) # write doc record to file
                g.write("\n")
                
                if TRANSLATE_DOCS:
                    ger_doc_dict = {
                        "DOCID" : doc_id,
                        "TEXT" : translator.translate(text=doc_dict["TEXT"])
                    }
                    json.dump(ger_doc_dict, h, ensure_ascii=False)
                    h.write("\n")
                
                count += 1
                doc_dict = {} # reset record
                pbar.update()
    
    print(f"Wrote {count} records to disk")

with open("download/cacm/query.text") as f, \
     open(os.path.join(cacm_output_path, "queries.json"), "w") as g, \
     open(os.path.join(cacm_output_path, "ger_queries.json"), "w") as h:
    lines = ""
    for l in f.readlines():
        lines += "\n" + l.strip() if l.startswith(".") else " " + l.strip()
    lines = lines.lstrip("\n").split("\n")
    
    queries = []
    ger_queries = []
    query_dict = {}
    with tqdm(total=64) as pbar:
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
                
                if TRANSLATE_QUERIES:
                    ger_query_dict = {
                        "QUERYID" : query_id,
                        "QUERY" : translator.translate(text=query)
                    }
                    ger_queries.append(ger_query_dict)
                
                query_dict = {} # reset record
                pbar.update()
    
    # write queries list to file
    dictionary = {"QUERIES": queries}
    json.dump(dictionary, g)

    ger_dictionary = {"QUERIES": ger_queries}
    json.dump(ger_dictionary, h, ensure_ascii=False)
    
    print(f"Wrote {len(queries)} queries to disk")

with open("download/cacm/qrels.text") as f, open(os.path.join(cacm_output_path, "qrels-treceval.txt"), "w") as g:
    lines = f.readlines()
    for l in lines:
        query_id, doc_id, _, _ = l.split()
        # write in trec_eval format
        g.write(f"{int(query_id)} 0 {doc_id} 1\n")


######### NPL #########

print("Preprocessing NPL...")

pattern = r"(\d+)\n(.*?)\n   /"
with open("download/npl/doc-text") as f, \
    open(os.path.join(npl_output_path, "npl.json"), "w") as g, \
    open(os.path.join(npl_output_path, "ger_npl.json"), "w") as h:
    document = f.read()
    count = 0
    with tqdm(total=11429) as pbar:
        for match in re.findall(pattern, document, re.DOTALL):
            doc_id = match[0]
            text = re.sub(r" +", " ", match[1].replace("\n", ' ')) # remove new lines and double spaces
            doc_dict = {
                "DOCID": doc_id,
                "TEXT": text
            }
            json.dump(doc_dict, g)
            g.write("\n")

            if TRANSLATE_DOCS:
                ger_doc_dict = {
                    "DOCID": doc_id,
                    "TEXT": translator.translate(text=text)
                }
                json.dump(ger_doc_dict, h, ensure_ascii=False)
                h.write("\n")
            
            count += 1
            pbar.update()
    
    print(f"Wrote {count} records to disk")

pattern = r"(\d+)\n(.*?)\n/"
with open("download/npl/query-text") as f, \
     open(os.path.join(npl_output_path, "queries.json"), "w") as g, \
     open(os.path.join(npl_output_path, "ger_queries.json"), "w") as h:
    document = f.read()
    queries = []
    ger_queries = []
    with tqdm(total=93) as pbar:
        for match in re.findall(pattern, document, re.DOTALL):
            query_id = match[0]
            query = match[1].lower()
            
            query_dict = {
                "QUERYID": query_id,
                "QUERY": query
            }
            queries.append(query_dict)
            
            if TRANSLATE_QUERIES:
                ger_query_dict = {
                    "QUERYID": query_id,
                    "QUERY": translator.translate(text=query)
                }
                ger_queries.append(ger_query_dict)
            pbar.update()
    
    json.dump({"QUERIES": queries}, g)
    json.dump({"QUERIES": ger_queries}, h, ensure_ascii=False)
    
    print(f"Wrote {len(queries)} queries to disk")

pattern = r"(\d+)\n(.*?)\n   /"
with open("download/npl/rlv-ass") as f, open(os.path.join(npl_output_path, "qrels-treceval.txt"), "w") as g:
    document = f.read()
    for match in re.findall(pattern, document, re.DOTALL):
        query_id = match[0]
        for doc_id in match[1].split():
            g.write(f"{int(query_id)} 0 {doc_id} 1\n")


######### REMOVE FILES #########

if not TRANSLATE_DOCS:
    os.remove(os.path.join(med_output_path, "ger_med.json"))
    os.remove(os.path.join(cacm_output_path, "ger_cacm.json"))
    os.remove(os.path.join(npl_output_path, "ger_npl.json"))

if not TRANSLATE_QUERIES:
    os.remove(os.path.join(med_output_path, "ger_queries.json"))
    os.remove(os.path.join(cacm_output_path, "ger_queries.json"))
    os.remove(os.path.join(npl_output_path, "ger_queries.json"))
