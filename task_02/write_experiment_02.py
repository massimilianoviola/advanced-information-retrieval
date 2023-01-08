import functools
import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", action='store_true')
args = parser.parse_args()

output_path = "task_02/outputs" # save search script outputs
result_path = "task_02/results" # save analysis made by trec_eval
datasets = ["med", "cacm", "npl"]
models = ["average_word_embeddings_glove.6B.300d", "all-MiniLM-L6-v2", "all-MiniLM-L12-v2", "all-mpnet-base-v2"]
shortcuts = ["glove", "minil6", "minil12", "mpnetv2"]

file = open("task_02/experiment_02.sh", "w") if args.file else sys.stdout

# write the experiment in shell language to be executed via the command line
printf = functools.partial(print, file=file)

printf("# experiment 02: compare retrieval performance with language models")
printf(f"mkdir -p {output_path}")
printf(f"mkdir -p {result_path}")

for d in datasets:
    printf(f"# index {d}")
    printf(f"python3 bm25_index.py ./data/{d}/{d}.json {d}_bm25")

    for m, s in zip(models, shortcuts):
        printf(f"# index {d} with model {m}")
        printf(f"python3 embedding_index.py ./data/{d}/{d}.json {d}_{s} {m}")

    printf(f"# search {d}")
    printf(f"python3 bm25_search.py ./data/{d}/queries.json {d}_bm25 > {os.path.join(output_path, f'{d}_bm25.txt')}")

    for m, s in zip(models, shortcuts):
        printf(f"# search {d} with model {m}")
        printf(f"python3 embedding_search.py ./data/{d}/queries.json {d}_{s} {m} > {os.path.join(output_path, f'{d}_{s}.txt')}")

    printf(f"# analyze {d}")
    printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'{d}_bm25.txt')} > {os.path.join(result_path, f'map_{d}_bm25.txt')}")

    for m, s in zip(models, shortcuts):
        printf(f"# analyze {d} with model {m}")
        printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'{d}_{s}.txt')} > {os.path.join(result_path, f'map_{d}_{s}.txt')}")

file.close()
