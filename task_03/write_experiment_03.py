import functools
import os


output_path = "task_03/outputs" # save search script outputs
result_path = "task_03/results" # save analysis made by trec_eval
datasets = ["med", "cacm", "npl"]

# write the experiment shell script to be executed via the command line
with open("task_03/experiment_03.sh", "w") as f:
    printf = functools.partial(print, file=f)

    printf("# experiment 03: compare retrieval performance on translated documents")
    printf(f"mkdir -p {output_path}")
    printf(f"mkdir -p {result_path}")

    for d in datasets:
        printf(f"# index {d} in english")
        printf(f"python3 bm25_index.py ./data/{d}/{d}.json {d}_bm25")
    
        printf(f"# index {d} in german")
        printf(f"python3 bm25_index.py ./data/{d}/ger_{d}.json ger_{d}_bm25")

        printf(f"# search {d} in english")
        printf(f"python3 bm25_search.py ./data/{d}/queries.json {d}_bm25 > {os.path.join(output_path, f'{d}_bm25.txt')}")

        printf(f"# search {d} in german")
        printf(f"python3 bm25_search.py ./data/{d}/ger_queries.json ger_{d}_bm25 > {os.path.join(output_path, f'ger_{d}_bm25.txt')}")

        printf(f"# analyze {d} in english")
        printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'{d}_bm25.txt')} > {os.path.join(result_path, f'map_{d}_bm25.txt')}")

        printf(f"# analyze {d} in german")
        printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'ger_{d}_bm25.txt')} > {os.path.join(result_path, f'map_ger_{d}_bm25.txt')}")
