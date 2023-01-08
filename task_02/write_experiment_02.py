import functools
import os


output_path = "task_02/outputs" # save search script outputs
result_path = "task_02/results" # save analysis made by trec_eval
datasets = ["med", "cacm", "npl"]

# write the experiment shell script to be executed via the command line
with open("task_02/experiment_02.sh", "w") as f:
    printf = functools.partial(print, file=f)

    printf("# experiment 02: compare retrieval performance on summarized documents")
    printf(f"mkdir -p {output_path}")
    printf(f"mkdir -p {result_path}")

    for d in datasets:
        printf(f"# index {d}")
        printf(f"python3 bm25_index.py ./data/{d}/{d}.json {d}_bm25")

        printf(f"# index summarized {d}")
        printf(f"python3 bm25_index.py ./data/{d}/summarized_{d}.json summarized_{d}_bm25")

        printf(f"# search {d}")
        printf(f"python3 bm25_search.py ./data/{d}/queries.json {d}_bm25 > {os.path.join(output_path, f'{d}_bm25.txt')}")

        printf(f"# search summarized {d}")
        printf(f"python3 bm25_search.py ./data/{d}/queries.json summarized_{d}_bm25 > {os.path.join(output_path, f'summarized_{d}_bm25.txt')}")

        printf(f"# analyze {d}")
        printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'{d}_bm25.txt')} > {os.path.join(result_path, f'map_{d}_bm25.txt')}")

        printf(f"# analyze summarized {d}")
        printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'summarized_{d}_bm25.txt')} > {os.path.join(result_path, f'map_summarized_{d}_bm25.txt')}")
