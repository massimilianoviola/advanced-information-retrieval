# experiment 04: compare retrieval performance with queries in different languages on english and german docs, using a multilingual model
mkdir -p task_04/outputs
mkdir -p task_04/results
# index med in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/med/med.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search english med with english queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/queries.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/EN_med_ml_minilm_l12_v2.txt
# search english med with german queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/ger_queries.json med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/DE_med_ml_minilm_l12_v2.txt
# analyze english med with english queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/EN_med_ml_minilm_l12_v2.txt > task_04/results/map_EN_med_ml_minilm_l12_v2.txt
# analyze english med with german queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/DE_med_ml_minilm_l12_v2.txt > task_04/results/map_DE_med_ml_minilm_l12_v2.txt
# index med in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/med/ger_med.json ger_med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search german med with english queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/queries.json ger_med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/EN_ger_med_ml_minilm_l12_v2.txt
# search german med with german queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/med/ger_queries.json ger_med_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/DE_ger_med_ml_minilm_l12_v2.txt
# analyze german med with english queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/EN_ger_med_ml_minilm_l12_v2.txt > task_04/results/map_EN_ger_med_ml_minilm_l12_v2.txt
# analyze german med with german queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/DE_ger_med_ml_minilm_l12_v2.txt > task_04/results/map_DE_ger_med_ml_minilm_l12_v2.txt
# index med in english with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/med/med.json med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search english med with english queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/med/queries.json med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/EN_med_ml_mpnet_base_v2.txt
# search english med with german queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/med/ger_queries.json med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/DE_med_ml_mpnet_base_v2.txt
# analyze english med with english queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/EN_med_ml_mpnet_base_v2.txt > task_04/results/map_EN_med_ml_mpnet_base_v2.txt
# analyze english med with german queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/DE_med_ml_mpnet_base_v2.txt > task_04/results/map_DE_med_ml_mpnet_base_v2.txt
# index med in german with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/med/ger_med.json ger_med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search german med with english queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/med/queries.json ger_med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/EN_ger_med_ml_mpnet_base_v2.txt
# search german med with german queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/med/ger_queries.json ger_med_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/DE_ger_med_ml_mpnet_base_v2.txt
# analyze german med with english queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/EN_ger_med_ml_mpnet_base_v2.txt > task_04/results/map_EN_ger_med_ml_mpnet_base_v2.txt
# analyze german med with german queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_04/outputs/DE_ger_med_ml_mpnet_base_v2.txt > task_04/results/map_DE_ger_med_ml_mpnet_base_v2.txt
# index cacm in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search english cacm with english queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/EN_cacm_ml_minilm_l12_v2.txt
# search english cacm with german queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/ger_queries.json cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/DE_cacm_ml_minilm_l12_v2.txt
# analyze english cacm with english queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/EN_cacm_ml_minilm_l12_v2.txt > task_04/results/map_EN_cacm_ml_minilm_l12_v2.txt
# analyze english cacm with german queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/DE_cacm_ml_minilm_l12_v2.txt > task_04/results/map_DE_cacm_ml_minilm_l12_v2.txt
# index cacm in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/cacm/ger_cacm.json ger_cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search german cacm with english queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/queries.json ger_cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/EN_ger_cacm_ml_minilm_l12_v2.txt
# search german cacm with german queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/ger_queries.json ger_cacm_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/DE_ger_cacm_ml_minilm_l12_v2.txt
# analyze german cacm with english queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/EN_ger_cacm_ml_minilm_l12_v2.txt > task_04/results/map_EN_ger_cacm_ml_minilm_l12_v2.txt
# analyze german cacm with german queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/DE_ger_cacm_ml_minilm_l12_v2.txt > task_04/results/map_DE_ger_cacm_ml_minilm_l12_v2.txt
# index cacm in english with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search english cacm with english queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/EN_cacm_ml_mpnet_base_v2.txt
# search english cacm with german queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/cacm/ger_queries.json cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/DE_cacm_ml_mpnet_base_v2.txt
# analyze english cacm with english queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/EN_cacm_ml_mpnet_base_v2.txt > task_04/results/map_EN_cacm_ml_mpnet_base_v2.txt
# analyze english cacm with german queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/DE_cacm_ml_mpnet_base_v2.txt > task_04/results/map_DE_cacm_ml_mpnet_base_v2.txt
# index cacm in german with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/cacm/ger_cacm.json ger_cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search german cacm with english queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/cacm/queries.json ger_cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/EN_ger_cacm_ml_mpnet_base_v2.txt
# search german cacm with german queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/cacm/ger_queries.json ger_cacm_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/DE_ger_cacm_ml_mpnet_base_v2.txt
# analyze german cacm with english queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/EN_ger_cacm_ml_mpnet_base_v2.txt > task_04/results/map_EN_ger_cacm_ml_mpnet_base_v2.txt
# analyze german cacm with german queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_04/outputs/DE_ger_cacm_ml_mpnet_base_v2.txt > task_04/results/map_DE_ger_cacm_ml_mpnet_base_v2.txt
# index npl in english with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/npl/npl.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search english npl with english queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/queries.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/EN_npl_ml_minilm_l12_v2.txt
# search english npl with german queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/ger_queries.json npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/DE_npl_ml_minilm_l12_v2.txt
# analyze english npl with english queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/EN_npl_ml_minilm_l12_v2.txt > task_04/results/map_EN_npl_ml_minilm_l12_v2.txt
# analyze english npl with german queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/DE_npl_ml_minilm_l12_v2.txt > task_04/results/map_DE_npl_ml_minilm_l12_v2.txt
# index npl in german with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_index.py ./data/npl/ger_npl.json ger_npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2
# search german npl with english queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/queries.json ger_npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/EN_ger_npl_ml_minilm_l12_v2.txt
# search german npl with german queries with model paraphrase-multilingual-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/ger_queries.json ger_npl_ml_minilm_l12_v2 paraphrase-multilingual-MiniLM-L12-v2 > task_04/outputs/DE_ger_npl_ml_minilm_l12_v2.txt
# analyze german npl with english queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/EN_ger_npl_ml_minilm_l12_v2.txt > task_04/results/map_EN_ger_npl_ml_minilm_l12_v2.txt
# analyze german npl with german queries with model paraphrase-multilingual-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/DE_ger_npl_ml_minilm_l12_v2.txt > task_04/results/map_DE_ger_npl_ml_minilm_l12_v2.txt
# index npl in english with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/npl/npl.json npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search english npl with english queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/npl/queries.json npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/EN_npl_ml_mpnet_base_v2.txt
# search english npl with german queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/npl/ger_queries.json npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/DE_npl_ml_mpnet_base_v2.txt
# analyze english npl with english queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/EN_npl_ml_mpnet_base_v2.txt > task_04/results/map_EN_npl_ml_mpnet_base_v2.txt
# analyze english npl with german queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/DE_npl_ml_mpnet_base_v2.txt > task_04/results/map_DE_npl_ml_mpnet_base_v2.txt
# index npl in german with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_index.py ./data/npl/ger_npl.json ger_npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2
# search german npl with english queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/npl/queries.json ger_npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/EN_ger_npl_ml_mpnet_base_v2.txt
# search german npl with german queries with model paraphrase-multilingual-mpnet-base-v2
python3 embedding_search.py ./data/npl/ger_queries.json ger_npl_ml_mpnet_base_v2 paraphrase-multilingual-mpnet-base-v2 > task_04/outputs/DE_ger_npl_ml_mpnet_base_v2.txt
# analyze german npl with english queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/EN_ger_npl_ml_mpnet_base_v2.txt > task_04/results/map_EN_ger_npl_ml_mpnet_base_v2.txt
# analyze german npl with german queries with model paraphrase-multilingual-mpnet-base-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_04/outputs/DE_ger_npl_ml_mpnet_base_v2.txt > task_04/results/map_DE_ger_npl_ml_mpnet_base_v2.txt
