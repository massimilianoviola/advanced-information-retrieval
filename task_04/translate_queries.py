# Setup:
# pip install --upgrade deepl
# requires Deepl API key stored in deepl_auth.key file
# can be obtained from https://www.deepl.com/de/pro-api?cta=header-pro-api/ with free account
# * feel free to contact me for my key - Nico

import deepl
from os.path import exists
import io

# todo set via command line argument
TARGET_LANG = 'DE'
SOURCE_LANG = 'EN'
QUERIES_FILE = './data/cacm/queries_DE.json'
API_KEY_FILE = './task_04/deepl_auth.key'

if __name__ == '__main__':
    # retrieve API key from deepl_auth.key
    with open(API_KEY_FILE, 'r') as f:
        auth_key = f.read()

    translator = deepl.Translator(auth_key)

    # create file name for translated queries
    queries_file_without_extension = QUERIES_FILE[:QUERIES_FILE.rfind('.')]
    queries_file_extension = QUERIES_FILE[QUERIES_FILE.rfind('.') + 1:]
    translated_queries_file = queries_file_without_extension + "_" + TARGET_LANG + "." + queries_file_extension

    # do not translate if translated file already exists
    if exists(translated_queries_file):
        print("Translated queries already exist: " + translated_queries_file)
        print("Manually delete this file if you want to re-translate the queries.")
        exit(1)

    # read queries from file
    print("Reading queries from: " + QUERIES_FILE)
    with io.open(QUERIES_FILE, 'r', encoding="UTF8") as f:
        queries = f.read()  # json as string

    # translate queries
    print("Translating queries from " + SOURCE_LANG + " to " + TARGET_LANG + " using DeepL API.")
    # ? capitalization is sometimes off - probably no problem for our use case
    translated_queries = translator.translate_text(queries,
                                                   target_lang=TARGET_LANG,
                                                   source_lang=SOURCE_LANG,
                                                   formality='more',
                                                   preserve_formatting=True).__str__()

    # replace ABFRAGE/ANFRAGE/FRAGE with QUERY
    translated_queries = translated_queries.replace("ABFRAGE", "QUERY")
    translated_queries = translated_queries.replace("ANFRAGE", "QUERY")
    translated_queries = translated_queries.replace("FRAGE", "QUERY")

    # write translated queries to file
    print("Writing translated queries to: " + translated_queries_file + "\n")
    # * io + UTF8 encoding is required to write special characters like ä, ö, ü, ß
    with io.open(translated_queries_file, 'w', encoding="UTF8") as f:
        f.write(translated_queries)

    # print api usage
    usage = translator.get_usage()
    if usage.any_limit_reached:
        print('Translation limit reached.')
    if usage.character.valid:
        print(f"Character usage: {usage.character.count} of {usage.character.limit}")
    if usage.document.valid:
        print(f"Document usage: {usage.document.count} of {usage.document.limit}")

    exit(0)
