import os
from constants import *

# create results folder
os.makedirs("./task_04/results", exist_ok=True)

# evaluate results with trec_eval
for data_set in DATA_SETS:
    for language in LANGUAGES:
        # calculate Mean Average Precision (MAP) using existing relevancies (qrels-treceval.txt) and search results (outputs)
        # store in results: map queryID score
        os.system(
            f"trec_eval -m map -q ./data/{data_set}/qrels-treceval.txt ./task_04/outputs/{MODEL_SHORTCUT}_{data_set}_{language}.txt > ./task_04/results/map_{MODEL_SHORTCUT}_{data_set}_{language}.txt"
        )