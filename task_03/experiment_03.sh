# experiment 03: compare retrieval performance on translated documents
mkdir -p task_03/outputs
mkdir -p task_03/results
# index med in english
python3 bm25_index.py ./data/med/med.json med_bm25
# index med in german
python3 bm25_index.py ./data/med/ger_med.json ger_med_bm25
# index med in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/med/med.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# index med in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/med/ger_med.json ger_med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search med in english
python3 bm25_search.py ./data/med/queries.json med_bm25 > task_03/outputs/med_bm25.txt
# search med in german
python3 bm25_search.py ./data/med/ger_queries.json ger_med_bm25 > task_03/outputs/ger_med_bm25.txt
# search med in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/queries.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_03/outputs/med_ml_minilm_l12_v2.txt
# search med in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/ger_queries.json ger_med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_03/outputs/ger_med_ml_minilm_l12_v2.txt
# analyze med in english
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_03/outputs/med_bm25.txt > task_03/results/map_med_bm25.txt
# analyze med in german
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_03/outputs/ger_med_bm25.txt > task_03/results/map_ger_med_bm25.txt
# analyze med in english with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_03/outputs/med_ml_minilm_l12_v2.txt > task_03/results/map_med_ml_minilm_l12_v2.txt
# analyze med in german with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_03/outputs/ger_med_ml_minilm_l12_v2.txt > task_03/results/map_ger_med_ml_minilm_l12_v2.txt
# index cacm in english
python3 bm25_index.py ./data/cacm/cacm.json cacm_bm25
# index cacm in german
python3 bm25_index.py ./data/cacm/ger_cacm.json ger_cacm_bm25
# index cacm in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# index cacm in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/cacm/ger_cacm.json ger_cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search cacm in english
python3 bm25_search.py ./data/cacm/queries.json cacm_bm25 > task_03/outputs/cacm_bm25.txt
# search cacm in german
python3 bm25_search.py ./data/cacm/ger_queries.json ger_cacm_bm25 > task_03/outputs/ger_cacm_bm25.txt
# search cacm in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_03/outputs/cacm_ml_minilm_l12_v2.txt
# search cacm in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/ger_queries.json ger_cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_03/outputs/ger_cacm_ml_minilm_l12_v2.txt
# analyze cacm in english
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_03/outputs/cacm_bm25.txt > task_03/results/map_cacm_bm25.txt
# analyze cacm in german
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_03/outputs/ger_cacm_bm25.txt > task_03/results/map_ger_cacm_bm25.txt
# analyze cacm in english with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_03/outputs/cacm_ml_minilm_l12_v2.txt > task_03/results/map_cacm_ml_minilm_l12_v2.txt
# analyze cacm in german with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_03/outputs/ger_cacm_ml_minilm_l12_v2.txt > task_03/results/map_ger_cacm_ml_minilm_l12_v2.txt
# index npl in english
python3 bm25_index.py ./data/npl/npl.json npl_bm25
# index npl in german
python3 bm25_index.py ./data/npl/ger_npl.json ger_npl_bm25
# index npl in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/npl/npl.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# index npl in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/npl/ger_npl.json ger_npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search npl in english
python3 bm25_search.py ./data/npl/queries.json npl_bm25 > task_03/outputs/npl_bm25.txt
# search npl in german
python3 bm25_search.py ./data/npl/ger_queries.json ger_npl_bm25 > task_03/outputs/ger_npl_bm25.txt
# search npl in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/queries.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_03/outputs/npl_ml_minilm_l12_v2.txt
# search npl in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/ger_queries.json ger_npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_03/outputs/ger_npl_ml_minilm_l12_v2.txt
# analyze npl in english
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_03/outputs/npl_bm25.txt > task_03/results/map_npl_bm25.txt
# analyze npl in german
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_03/outputs/ger_npl_bm25.txt > task_03/results/map_ger_npl_bm25.txt
# analyze npl in english with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_03/outputs/npl_ml_minilm_l12_v2.txt > task_03/results/map_npl_ml_minilm_l12_v2.txt
# analyze npl in german with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_03/outputs/ger_npl_ml_minilm_l12_v2.txt > task_03/results/map_ger_npl_ml_minilm_l12_v2.txt
