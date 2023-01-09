import json
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("datafile", type=str, help="Input file")
args = parser.parse_args()

origin_file = f"./data/{args.datafile}/{args.datafile}.json"
compare_files = [f"./data/{args.datafile}/full_summarized_{args.datafile}.json",f"./data/{args.datafile}/partly_summarized_{args.datafile}.json"]
origin_result = f"./task_02/results/map_{args.datafile}_bm25.txt"
compare_results = [f"./task_02/results/map_full_summarized_{args.datafile}_bm25.txt",f"./task_02/results/map_partly_summarized_{args.datafile}_bm25.txt"]
origin_count_word = 0

with open(origin_file, 'r') as f:
    for doc in f:
        if len(doc) > 0:
            data = json.loads(doc)
            text = data['TEXT']
            words = text.split()
            origin_count_word = origin_count_word + len(words)

differences_summary = []
for compare_file in compare_files:
    compare_count_word = 0
    with open(compare_file, 'r') as f:
        for doc in f:
            if len(doc) > 0:
                data = json.loads(doc)
                text = data['TEXT']
                words = text.split()
                compare_count_word = compare_count_word + len(words)
    diff = abs(float(compare_count_word) - float(origin_count_word))
    diff = diff * 100 / origin_count_word
    differences_summary.append(diff)

origin_accuracy_value = 0
with open(origin_result) as f:
    for line in f:
        if 'all' in line:
            origin_accuracy_value = float(line.split()[-1])

difference_accuracy = []
for s in compare_results:
    with open(s) as f:
        for line in f:
            if 'all' in line:
                diff = abs(float(origin_accuracy_value) - float(line.split()[-1]))
                diff = diff * 100 / float(origin_accuracy_value)

                difference_accuracy.append(diff)

with open('./task_02/results/summary_strength_vs_accuracy_loss.txt', 'a+') as f:
    file_string = ""
    for i in range(len(differences_summary)):
        file_string = file_string + str(differences_summary[i]) + " " + str(difference_accuracy[i])+ " "
    f.write(file_string[:-1] + "\n")
