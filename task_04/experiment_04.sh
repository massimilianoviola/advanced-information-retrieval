# experiment 04: compare retrieval performance with queries in different languages on english docs, using a multilingual model
mkdir -p task_04/outputs
mkdir -p task_04/results
# index med with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/med/med.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search med in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/queries.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/med_ml_minilm_l12_v2.txt
# search med in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/ger_queries.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/ger_med_ml_minilm_l12_v2.txt
# analyze med in english with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/med_ml_minilm_l12_v2.txt > task_04/results/map_med_ml_minilm_l12_v2.txt
# analyze med in german with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/ger_med_ml_minilm_l12_v2.txt > task_04/results/map_ger_med_ml_minilm_l12_v2.txt
# index med with model distiluse-base-multilingual-cased-v1
python3 embedding_index.py ./data/med/med.json med_dbmlc_v1 distiluse-base-multilingual-cased-v1
# search med in english with model distiluse-base-multilingual-cased-v1
python3 embedding_search.py ./data/med/queries.json med_dbmlc_v1 distiluse-base-multilingual-cased-v1 > task_04/outputs/med_dbmlc_v1.txt
# search med in german with model distiluse-base-multilingual-cased-v1
python3 embedding_search.py ./data/med/ger_queries.json med_dbmlc_v1 distiluse-base-multilingual-cased-v1 > task_04/outputs/ger_med_dbmlc_v1.txt
# analyze med in english with model distiluse-base-multilingual-cased-v1
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/med_dbmlc_v1.txt > task_04/results/map_med_dbmlc_v1.txt
# analyze med in german with model distiluse-base-multilingual-cased-v1
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/ger_med_dbmlc_v1.txt > task_04/results/map_ger_med_dbmlc_v1.txt
# index med with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/med/med.json med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search med in english with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/med/queries.json med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/med_ml_mpnet_base_v2.txt
# search med in german with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/med/ger_queries.json med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/ger_med_ml_mpnet_base_v2.txt
# analyze med in english with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/med_ml_mpnet_base_v2.txt > task_04/results/map_med_ml_mpnet_base_v2.txt
# analyze med in german with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/ger_med_ml_mpnet_base_v2.txt > task_04/results/map_ger_med_ml_mpnet_base_v2.txt
# index cacm with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search cacm in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/cacm_ml_minilm_l12_v2.txt
# search cacm in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/ger_queries.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/ger_cacm_ml_minilm_l12_v2.txt
# analyze cacm in english with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/cacm_ml_minilm_l12_v2.txt > task_04/results/map_cacm_ml_minilm_l12_v2.txt
# analyze cacm in german with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/ger_cacm_ml_minilm_l12_v2.txt > task_04/results/map_ger_cacm_ml_minilm_l12_v2.txt
# index cacm with model distiluse-base-multilingual-cased-v1
python3 embedding_index.py ./data/cacm/cacm.json cacm_dbmlc_v1 distiluse-base-multilingual-cased-v1
# search cacm in english with model distiluse-base-multilingual-cased-v1
python3 embedding_search.py ./data/cacm/queries.json cacm_dbmlc_v1 distiluse-base-multilingual-cased-v1 > task_04/outputs/cacm_dbmlc_v1.txt
# search cacm in german with model distiluse-base-multilingual-cased-v1
python3 embedding_search.py ./data/cacm/ger_queries.json cacm_dbmlc_v1 distiluse-base-multilingual-cased-v1 > task_04/outputs/ger_cacm_dbmlc_v1.txt
# analyze cacm in english with model distiluse-base-multilingual-cased-v1
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/cacm_dbmlc_v1.txt > task_04/results/map_cacm_dbmlc_v1.txt
# analyze cacm in german with model distiluse-base-multilingual-cased-v1
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/ger_cacm_dbmlc_v1.txt > task_04/results/map_ger_cacm_dbmlc_v1.txt
# index cacm with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search cacm in english with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/cacm_ml_mpnet_base_v2.txt
# search cacm in german with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/cacm/ger_queries.json cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/ger_cacm_ml_mpnet_base_v2.txt
# analyze cacm in english with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/cacm_ml_mpnet_base_v2.txt > task_04/results/map_cacm_ml_mpnet_base_v2.txt
# analyze cacm in german with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/ger_cacm_ml_mpnet_base_v2.txt > task_04/results/map_ger_cacm_ml_mpnet_base_v2.txt
# index npl with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/npl/npl.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search npl in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/queries.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/npl_ml_minilm_l12_v2.txt
# search npl in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/ger_queries.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/ger_npl_ml_minilm_l12_v2.txt
# analyze npl in english with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/npl_ml_minilm_l12_v2.txt > task_04/results/map_npl_ml_minilm_l12_v2.txt
# analyze npl in german with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/ger_npl_ml_minilm_l12_v2.txt > task_04/results/map_ger_npl_ml_minilm_l12_v2.txt
# index npl with model distiluse-base-multilingual-cased-v1
python3 embedding_index.py ./data/npl/npl.json npl_dbmlc_v1 distiluse-base-multilingual-cased-v1
# search npl in english with model distiluse-base-multilingual-cased-v1
python3 embedding_search.py ./data/npl/queries.json npl_dbmlc_v1 distiluse-base-multilingual-cased-v1 > task_04/outputs/npl_dbmlc_v1.txt
# search npl in german with model distiluse-base-multilingual-cased-v1
python3 embedding_search.py ./data/npl/ger_queries.json npl_dbmlc_v1 distiluse-base-multilingual-cased-v1 > task_04/outputs/ger_npl_dbmlc_v1.txt
# analyze npl in english with model distiluse-base-multilingual-cased-v1
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/npl_dbmlc_v1.txt > task_04/results/map_npl_dbmlc_v1.txt
# analyze npl in german with model distiluse-base-multilingual-cased-v1
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/ger_npl_dbmlc_v1.txt > task_04/results/map_ger_npl_dbmlc_v1.txt
# index npl with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/npl/npl.json npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search npl in english with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/npl/queries.json npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/npl_ml_mpnet_base_v2.txt
# search npl in german with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/npl/ger_queries.json npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/ger_npl_ml_mpnet_base_v2.txt
# analyze npl in english with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/npl_ml_mpnet_base_v2.txt > task_04/results/map_npl_ml_mpnet_base_v2.txt
# analyze npl in german with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/ger_npl_ml_mpnet_base_v2.txt > task_04/results/map_ger_npl_ml_mpnet_base_v2.txt
