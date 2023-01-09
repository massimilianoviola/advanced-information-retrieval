import functools
import os


output_path = "task_04/outputs" # save search script outputs
result_path = "task_04/results" # save analysis made by trec_eval
datasets = ["med", "cacm", "npl"]
models = ["paraphrase-multilingual-MiniLM-L12-v2", "paraphrase-multilingual-mpnet-base-v2"]
shortcuts = ["ml_minilm_l12_v2", "ml_mpnet_base_v2"]

# write the experiment shell script to be executed via the command line
with open("task_04/experiment_04.sh", "w") as f:
    printf = functools.partial(print, file=f)

    printf("# experiment 04: compare retrieval performance with queries in different languages on english and german docs, using a multilingual model")
    printf(f"mkdir -p {output_path}")
    printf(f"mkdir -p {result_path}")

    for d in datasets:
        for m, s in zip(models, shortcuts):

            # index naming convention {d}_{s} or ger_{d}_{s}
            # search and result naming convention {QUERYLANGUAGE: EN/DE}_{d}_{s} or {QUERYLANGUAGE: EN/DE}_ger_{d}_{s}

            # english docs
            printf(f"# index {d} in english with model {m}")
            printf(f"python3 embedding_index.py ./data/{d}/{d}.json {d}_{s} {m}")

            printf(f"# search english {d} with english queries with model {m}")
            printf(f"python3 embedding_search.py ./data/{d}/queries.json {d}_{s} {m} > {os.path.join(output_path, f'EN_{d}_{s}.txt')}")

            printf(f"# search english {d} with german queries with model {m}")
            printf(f"python3 embedding_search.py ./data/{d}/ger_queries.json {d}_{s} {m} > {os.path.join(output_path, f'DE_{d}_{s}.txt')}")

            printf(f"# analyze english {d} with english queries with model {m}")
            printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'EN_{d}_{s}.txt')} > {os.path.join(result_path, f'map_EN_{d}_{s}.txt')}")

            printf(f"# analyze english {d} with german queries with model {m}")
            printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'DE_{d}_{s}.txt')} > {os.path.join(result_path, f'map_DE_{d}_{s}.txt')}")

            # german docs
            printf(f"# index {d} in german with model {m}")
            printf(f"python3 embedding_index.py ./data/{d}/ger_{d}.json ger_{d}_{s} {m}")

            printf(f"# search german {d} with english queries with model {m}")
            printf(f"python3 embedding_search.py ./data/{d}/queries.json ger_{d}_{s} {m} > {os.path.join(output_path, f'EN_ger_{d}_{s}.txt')}")

            printf(f"# search german {d} with german queries with model {m}")
            printf(f"python3 embedding_search.py ./data/{d}/ger_queries.json ger_{d}_{s} {m} > {os.path.join(output_path, f'DE_ger_{d}_{s}.txt')}")

            printf(f"# analyze german {d} with english queries with model {m}")
            printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'EN_ger_{d}_{s}.txt')} > {os.path.join(result_path, f'map_EN_ger_{d}_{s}.txt')}")

            printf(f"# analyze german {d} with german queries with model {m}")
            printf(f"./trec_eval -m map -q ./data/{d}/qrels-treceval.txt {os.path.join(output_path, f'DE_ger_{d}_{s}.txt')} > {os.path.join(result_path, f'map_DE_ger_{d}_{s}.txt')}")
