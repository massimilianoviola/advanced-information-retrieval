
# ! DO NOT USE THIS SCRIPT WITHOUT TALKING TO ME FIRST! - Nico
# * you need the api key and must know about the limitations of the free api

# Setup:
# pip install --upgrade deepl
# requires Deepl API key stored in deepl_auth.key file
# can be obtained from https://www.deepl.com/de/pro-api?cta=header-pro-api/ with free account

import deepl
from os.path import exists

# todo set via command line argument
TARGET_LANG = 'DE'
SOURCE_LANG = 'EN'
QUERIES_FILE = './npl/data/queries.json'

if __name__ == '__main__':
    # retrieve API key from deepl_auth.key
    with open('./task4/deepl_auth.key', 'r') as f:
        auth_key = f.read()

    translator = deepl.Translator(auth_key)

    # read queries from file
    queries_file_without_extension = QUERIES_FILE[:QUERIES_FILE.rfind('.')]
    queries_file_extension = QUERIES_FILE[QUERIES_FILE.rfind('.') + 1:]
    translated_queries_file = queries_file_without_extension + "_" + TARGET_LANG + "." + queries_file_extension

    # print some info
    print("Translating queries from " + SOURCE_LANG + " to " + TARGET_LANG + " using DeepL API.")
    print("Reading queries from: " + QUERIES_FILE)
    print("Writing translated queries to: " + translated_queries_file + "\n")

    # do not translate if translated file already exists
    if exists(translated_queries_file):
        print("Translated queries already exists: " + translated_queries_file)
        print("Manually delete this file if you want to re-translate the queries.")
        exit(0)

    # read queries from file
    with open(QUERIES_FILE, 'r') as f:
        queries = f.read()  # json as string

    # translate queries
    # ! does not properly return special characters like "ä", "ö", "ü", "ß"
    # ! either retranslate with different settings or manually replace them
    # ? capitalization is also somewhat off 
    # ? probably not a problem for our use case
    result = translator.translate_text(queries,
                                       target_lang=TARGET_LANG,
                                       source_lang=SOURCE_LANG,
                                       formality='more',
                                       preserve_formatting=True)

    # write translated queries to file
    with open(translated_queries_file, 'w') as f:
        f.write(result.__str__())

    # print api usage
    usage = translator.get_usage()
    if usage.any_limit_reached:
        print('Translation limit reached.')
    if usage.character.valid:
        print(f"Character usage: {usage.character.count} of {usage.character.limit}")
    if usage.document.valid:
        print(f"Document usage: {usage.document.count} of {usage.document.limit}")
