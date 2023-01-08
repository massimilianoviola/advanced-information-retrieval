mkdir -p task_02/outputs
mkdir -p task_02/results
# experiment 02: compare retrieval performance on summarized documents
# index med
python3 bm25_index.py ./data/med/med.json med_bm25
# index partly summarized med
python3 bm25_index.py ./data/med/partly_summarized_med.json partly_summarized_med_bm25
# index full summarized med
python3 bm25_index.py ./data/med/full_summarized_med.json full_summarized_med_bm25
# search med
python3 bm25_search.py ./data/med/queries.json med_bm25 > task_02/outputs/med_bm25.txt
# search partly summarized med
python3 bm25_search.py ./data/med/queries.json partly_summarized_med_bm25 > task_02/outputs/partly_summarized_med_bm25.txt
# search full summarized med
python3 bm25_search.py ./data/med/queries.json full_summarized_med_bm25 > task_02/outputs/full_summarized_med_bm25.txt
# analyze med
trec_eval -m map -q ./data/med/qrels-treceval.txt task_02/outputs/med_bm25.txt > task_02/results/map_med_bm25.txt
# analyze partly summarized med
trec_eval -m map -q ./data/med/qrels-treceval.txt task_02/outputs/partly_summarized_med_bm25.txt > task_02/results/map_partly_summarized_med_bm25.txt
# analyze full summarized med
trec_eval -m map -q ./data/med/qrels-treceval.txt task_02/outputs/full_summarized_med_bm25.txt > task_02/results/map_full_summarized_med_bm25.txt
# index cacm
python3 bm25_index.py ./data/cacm/cacm.json cacm_bm25
# index partly summarized cacm
python3 bm25_index.py ./data/cacm/partly_summarized_cacm.json partly_summarized_cacm_bm25
# index full summarized cacm
python3 bm25_index.py ./data/cacm/full_summarized_cacm.json full_summarized_cacm_bm25
# search cacm
python3 bm25_search.py ./data/cacm/queries.json cacm_bm25 > task_02/outputs/cacm_bm25.txt
# search partly summarized cacm
python3 bm25_search.py ./data/cacm/queries.json partly_summarized_cacm_bm25 > task_02/outputs/partly_summarized_cacm_bm25.txt
# search full summarized cacm
python3 bm25_search.py ./data/cacm/queries.json full_summarized_cacm_bm25 > task_02/outputs/full_summarized_cacm_bm25.txt
# analyze cacm
trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_02/outputs/cacm_bm25.txt > task_02/results/map_cacm_bm25.txt
# analyze partly summarized cacm
trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_02/outputs/partly_summarized_cacm_bm25.txt > task_02/results/map_partly_summarized_cacm_bm25.txt
# analyze full summarized cacm
trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_02/outputs/full_summarized_cacm_bm25.txt > task_02/results/map_full_summarized_cacm_bm25.txt
# index npl
python3 bm25_index.py ./data/npl/npl.json npl_bm25
# index partly summarized npl
python3 bm25_index.py ./data/npl/partly_summarized_npl.json partly_summarized_npl_bm25
# index full summarized npl
python3 bm25_index.py ./data/npl/full_summarized_npl.json full_summarized_npl_bm25
# search npl
python3 bm25_search.py ./data/npl/queries.json npl_bm25 > task_02/outputs/npl_bm25.txt
# search partly summarized npl
python3 bm25_search.py ./data/npl/queries.json partly_summarized_npl_bm25 > task_02/outputs/partly_summarized_npl_bm25.txt
# search full summarized npl
python3 bm25_search.py ./data/npl/queries.json full_summarized_npl_bm25 > task_02/outputs/full_summarized_npl_bm25.txt
# analyze npl
trec_eval -m map -q ./data/npl/qrels-treceval.txt task_02/outputs/npl_bm25.txt > task_02/results/map_npl_bm25.txt
# analyze partly summarized npl
trec_eval -m map -q ./data/npl/qrels-treceval.txt task_02/outputs/partly_summarized_npl_bm25.txt > task_02/results/map_partly_summarized_npl_bm25.txt
# analyze full summarized npl
trec_eval -m map -q ./data/npl/qrels-treceval.txt task_02/outputs/full_summarized_npl_bm25.txt > task_02/results/map_full_summarized_npl_bm25.txt
