import argparse


parser = argparse.ArgumentParser()
parser.add_argument("datafile", type=str, help="Input file")
args = parser.parse_args()

filename = args.datafile

parsed_lines = []
with open(filename, "r") as in_f:
    # Iterate over each line in the input file
    for line in in_f:
        start_idx = line.index('"TEXT": "') + len('"TEXT": "')
        end_idx = line.index('"}', start_idx)
        text = line[start_idx:end_idx].replace('"', " ")
        line = line[:start_idx] + text + line[end_idx:]
        parsed_lines.append(line)

with open(filename, "w") as out_file:
    for line in parsed_lines:
        out_file.write(line)
