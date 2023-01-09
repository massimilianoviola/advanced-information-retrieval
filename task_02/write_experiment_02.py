import functools
import os

output_path = "task_02/outputs" # save search script outputs
result_path = "task_02/results" # save analysis made by trec_eval
datasets = ["med", "cacm", "npl"]

# write the experiment shell script to be executed via the command line
with open("task_02/experiment_02.sh", "w") as f:
    printf = functools.partial(print, file=f)

    printf(f"mkdir -p {output_path}")
    printf(f"mkdir -p {result_path}")
    printf(f"rm ./task_02/results/summary_strength_vs_accuracy_loss.txt")
    printf("# experiment 02: compare retrieval performance on summarized documents")

    for d in datasets:
        printf(f"# index {d}")
        printf(f"python3 bm25_index.py ./data/{d}/{d}.json {d}_bm25")

        printf(f"# index partly summarized {d}")
        printf(f"python3 bm25_index.py ./data/{d}/partly_summarized_{d}.json partly_summarized_{d}_bm25")

        printf(f"# index full summarized {d}")
        printf(f"python3 bm25_index.py ./data/{d}/full_summarized_{d}.json full_summarized_{d}_bm25")

        printf(f"# search {d}")
        printf(f"python3 bm25_search.py ./data/{d}/queries.json {d}_bm25 > {os.path.join(output_path, f'{d}_bm25.txt')}")

        printf(f"# search partly summarized {d}")
        printf(f"python3 bm25_search.py ./data/{d}/queries.json partly_summarized_{d}_bm25 > {os.path.join(output_path, f'partly_summarized_{d}_bm25.txt')}")

        printf(f"# search full summarized {d}")
        printf(f"python3 bm25_search.py ./data/{d}/queries.json full_summarized_{d}_bm25 > {os.path.join(output_path, f'full_summarized_{d}_bm25.txt')}")

        printf(f"# analyze {d}")
        printf(f"trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'{d}_bm25.txt')} > {os.path.join(result_path, f'map_{d}_bm25.txt')}")

        printf(f"# analyze partly summarized {d}")
        printf(f"trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'partly_summarized_{d}_bm25.txt')} > {os.path.join(result_path, f'map_partly_summarized_{d}_bm25.txt')}")

        printf(f"# analyze full summarized {d}")
        printf(f"trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'full_summarized_{d}_bm25.txt')} > {os.path.join(result_path, f'map_full_summarized_{d}_bm25.txt')}")

        printf(f"# calculate percentage differences: summary vs accuracy")
        printf(f"python3 percentage_calculation.py {d}")


