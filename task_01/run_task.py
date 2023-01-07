import os

#Adjust this array for all possible json-files
#Json file and folder name has to be the same

DATA_SETS = ["med", "cacm", "npl"]
os.makedirs("./outputs", exist_ok=True)
os.makedirs("./results", exist_ok=True)

print("----------------------------------------------------------")
print("Summarize datasets")
print("----------------------------------------------------------")
for data in DATA_SETS:
    os.system(f"python3 summarize_data.py {data}")
    print()
print("----------------------------------------------------------")
print("Remove quotes to bring file in json format")
print("----------------------------------------------------------")
for data in DATA_SETS:
    os.system(f"python3 remove_quotes.py ../data/{data}/{data}_summarize_en.json")
print("----------------------------------------------------------")
print("Index datasets in elasticsearch")
print("----------------------------------------------------------")
for data in DATA_SETS:
    os.system(f"python3 ../bm25_index.py -f ../data/{data}/{data}.json -i {data}")
    print()
    os.system(f"python3 ../bm25_index.py -f ../data/{data}/{data}_summarize_en.json -i {data}_summarize_en")
    print()
print("----------------------------------------------------------")
print("Search using bm25")
print("----------------------------------------------------------")\

for data in DATA_SETS:
    os.system(f"python3 ../bm25_search.py -q ../data/{data}/queries.json -i {data} > ./outputs/{data}_bm25.txt")
    print(f"Search for index {data} is done... ")
    os.system(f"python3 ../bm25_search.py -q ../data/{data}/queries.json -i {data}_summarize_en > ./outputs/{data}_summarize_en_bm25.txt")
    print(f"Search for index {data}_summarize_en is done... ")

print("----------------------------------------------------------")
print("Using trec-eval for evaluation")
print("----------------------------------------------------------")
for data in DATA_SETS:
    os.system(f"trec_eval -m map -q ../data/{data}/qrels-treceval.txt ./outputs/{data}_bm25.txt > ./results/{data}_bm25.txt")
    print(f"Trec eval  {data} is done... ")
    os.system(f"trec_eval -m map -q ../data/{data}/qrels-treceval.txt ./outputs/{data}_summarize_en_bm25.txt > ./results/{data}_summarize_en_bm25.txt")
    print(f"Trec eval  {data}_summarize is done... ")
print("----------------------------------------------------------")
print("Task 01 is done")
print("----------------------------------------------------------")