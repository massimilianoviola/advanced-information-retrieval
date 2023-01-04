from os.path import exists
import io
import json
from xml.etree.ElementTree import tostring

import sentencepiece as spm
from numba.cuda import jit
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

DATA_FILE = '/home/manuel/PycharmProjects/advanced-information-retrieval/data/npl/npl.json'
TARGET_LANG = 'EN'

#GPU optimisation
@jit(forceobj=True)
def sum():
    for i in range(len(json_read_in_objects)):
        # Use tokenizer on the text
        token = pegasus_tokenizer.encode(json_read_in_objects[i]['TEXT'], return_tensors='pt', truncation=True)
        # encode the token
        encode_token = pegasus_model.generate(token)
        # decode the token to get words
        decode_token = pegasus_tokenizer.decode(encode_token[0], skip_special_tokens=True)
        print(i)
        json_write_out_objects.append(decode_token)

if __name__ == '__main__':
    data_file_without_extension = DATA_FILE[:DATA_FILE.rfind('.')]
    data_file_extension = DATA_FILE[DATA_FILE.rfind('.') + 1:]
    summarized_data_file = data_file_without_extension + "_" + "summarize" + "_2" + TARGET_LANG + "_" + data_file_extension

    #do not summarize if summarized file already exists
    if exists(summarized_data_file):
        print("Translated queries already exist: " + summarized_data_file)
        print("Manually delete this file if you want to re-summarize the queries.")
        exit(1)
    # read data from file
    print("Reading data from: " + DATA_FILE)
    json_read_in_objects = []
    with open(DATA_FILE, 'r') as f:
        for line in f:
            # Parse the line as a JSON object
            item = json.loads(line)
            json_read_in_objects.append(item)

    # Define the used model
    model_name = "google/pegasus-xsum"
    # Load tokenizer
    pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
    # Define Pegasus model
    pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name)

    json_write_out_objects = []


    for i in range(6000,11000):
        # Use tokenizer on the text
        token = pegasus_tokenizer(json_read_in_objects[i]['TEXT'], return_tensors="pt", truncation=True)
        # encode the token
        encode_token = pegasus_model.generate(**token)
        # decode the token to get words
        decode_token = pegasus_tokenizer.decode(encode_token[0], skip_special_tokens=True)
        print(i)
        json_write_out_objects.append(decode_token)

    doc_id = 6001
    str1 = "{\"DOCID\": \""
    str2 = "\", \"TEXT\": \""
    str3 = "\"}"
    with open(summarized_data_file, 'w+') as f:
        for line in json_write_out_objects:
            # Parse the line as a JSON object
            #   {"DOCID": "1", "TEXT": "Preliminary Report-International Algebraic Language"}
            result_string = str1 + str(doc_id) + str2 + line + str3+ "\n"
            f.write(result_string)
            doc_id += 1
            print("Current ", doc_id)

