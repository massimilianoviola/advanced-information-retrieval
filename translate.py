# Setup:
# pip install --upgrade deepl
# requires Deepl API key stored in deepl_auth.key file
# can be obtained from https://www.deepl.com/de/pro-api?cta=header-pro-api/ with free account

import deepl
from os.path import exists
import io
import argparse

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--language", type=str, help="target language e.g. 'EN' or 'DE'")
parser.add_argument("-s", "--source_file", type=str, help="Path to file to translate")
parser.add_argument("-t", "--target_file", type=str, help="Path to file to write translation to")
parser.add_argument("-d", "--deepl_api_key", type=str,
                    help="Path to file with Deepl API key")  # ? should this be a parameter?
args = parser.parse_args()

language = args.language
source_file = args.source_file
target_file = args.target_file

# retrieve API key from file
with open(args.deepl_api_key, 'r') as f:
    auth_key = f.read()

translator = deepl.Translator(auth_key)

# check if language is supported by DeepL API
'''
if args.language not in deepl.LANGUAGES:
    print("Language " + args.language + " is not supported by DeepL API.")
    print("Supported languages are: " + str(deepl.LANGUAGES))
    exit(1)
'''

# do not translate if translated file already exists
if exists(target_file):
    print("Translation already exists: " + target_file)
    print("Manually delete this file if you want to translate again.")
    exit(1)

# read text from file
print("Reading " + target_file)
with io.open(target_file, 'r', encoding="UTF8") as f:
    text = f.read()  # json as string

# translate text
print("Translating to " + language + " using DeepL API.")
# ? capitalization is sometimes off - probably no problem for our use case
translation = translator.translate_text(text, target_lang=language, formality='more',
                                        preserve_formatting=True).__str__()

# replace ABFRAGE/ANFRAGE/FRAGE with QUERY
# ! does not work for languages other than German
translation = translation.replace("ABFRAGE", "QUERY")
translation = translation.replace("ANFRAGE", "QUERY")
translation = translation.replace("FRAGE", "QUERY")

# write translation to file
print("Writing translation to: " + target_file + "\n")
# * io + UTF8 encoding is required to write special characters like ä, ö, ü, ß
with io.open(target_file, 'w', encoding="UTF8") as f:
    f.write(translation)

# print api usage
usage = translator.get_usage()
if usage.any_limit_reached:
    print('Translation limit reached.')
if usage.character.valid:
    print(f"Character usage: {usage.character.count} of {usage.character.limit}")
if usage.document.valid:
    print(f"Document usage: {usage.document.count} of {usage.document.limit}")
