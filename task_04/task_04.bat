:: DO NOT FORGET TO ADJUST constants.py BEFORE RUNNING THIS SCRIPT
:: Description: Run all scripts in task_04 in order
cd ..
python3 task_04/translate_queries.py
python3 task_04/finetuning.py
python3 task_04/embeddings.py
python3 task_04/index.py
python3 task_04/search.py
python3 task_04/evaluate.py