# experiment 01: compare retrieval performance with language models
mkdir -p task_01/outputs
mkdir -p task_01/results
# index med
python3 bm25_index.py ./data/med/med.json med_bm25
# index med with model average_word_embeddings_glove.6B.300d
python3 embedding_index.py ./data/med/med.json med_glove average_word_embeddings_glove.6B.300d
# index med with model all-MiniLM-L6-v2
python3 embedding_index.py ./data/med/med.json med_minil6 all-MiniLM-L6-v2
# index med with model all-MiniLM-L12-v2
python3 embedding_index.py ./data/med/med.json med_minil12 all-MiniLM-L12-v2
# index med with model all-mpnet-base-v2
python3 embedding_index.py ./data/med/med.json med_mpnetv2 all-mpnet-base-v2
# search med
python3 bm25_search.py ./data/med/queries.json med_bm25 > task_01/outputs/med_bm25.txt
# search med with model average_word_embeddings_glove.6B.300d
python3 embedding_search.py ./data/med/queries.json med_glove average_word_embeddings_glove.6B.300d > task_01/outputs/med_glove.txt
# search med with model all-MiniLM-L6-v2
python3 embedding_search.py ./data/med/queries.json med_minil6 all-MiniLM-L6-v2 > task_01/outputs/med_minil6.txt
# search med with model all-MiniLM-L12-v2
python3 embedding_search.py ./data/med/queries.json med_minil12 all-MiniLM-L12-v2 > task_01/outputs/med_minil12.txt
# search med with model all-mpnet-base-v2
python3 embedding_search.py ./data/med/queries.json med_mpnetv2 all-mpnet-base-v2 > task_01/outputs/med_mpnetv2.txt
# analyze med
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_01/outputs/med_bm25.txt > task_01/results/map_med_bm25.txt
# analyze med with model average_word_embeddings_glove.6B.300d
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_01/outputs/med_glove.txt > task_01/results/map_med_glove.txt
# analyze med with model all-MiniLM-L6-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_01/outputs/med_minil6.txt > task_01/results/map_med_minil6.txt
# analyze med with model all-MiniLM-L12-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_01/outputs/med_minil12.txt > task_01/results/map_med_minil12.txt
# analyze med with model all-mpnet-base-v2
./trec_eval -m map -q ./data/med/qrels-treceval.txt task_01/outputs/med_mpnetv2.txt > task_01/results/map_med_mpnetv2.txt
# index cacm
python3 bm25_index.py ./data/cacm/cacm.json cacm_bm25
# index cacm with model average_word_embeddings_glove.6B.300d
python3 embedding_index.py ./data/cacm/cacm.json cacm_glove average_word_embeddings_glove.6B.300d
# index cacm with model all-MiniLM-L6-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_minil6 all-MiniLM-L6-v2
# index cacm with model all-MiniLM-L12-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_minil12 all-MiniLM-L12-v2
# index cacm with model all-mpnet-base-v2
python3 embedding_index.py ./data/cacm/cacm.json cacm_mpnetv2 all-mpnet-base-v2
# search cacm
python3 bm25_search.py ./data/cacm/queries.json cacm_bm25 > task_01/outputs/cacm_bm25.txt
# search cacm with model average_word_embeddings_glove.6B.300d
python3 embedding_search.py ./data/cacm/queries.json cacm_glove average_word_embeddings_glove.6B.300d > task_01/outputs/cacm_glove.txt
# search cacm with model all-MiniLM-L6-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_minil6 all-MiniLM-L6-v2 > task_01/outputs/cacm_minil6.txt
# search cacm with model all-MiniLM-L12-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_minil12 all-MiniLM-L12-v2 > task_01/outputs/cacm_minil12.txt
# search cacm with model all-mpnet-base-v2
python3 embedding_search.py ./data/cacm/queries.json cacm_mpnetv2 all-mpnet-base-v2 > task_01/outputs/cacm_mpnetv2.txt
# analyze cacm
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_01/outputs/cacm_bm25.txt > task_01/results/map_cacm_bm25.txt
# analyze cacm with model average_word_embeddings_glove.6B.300d
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_01/outputs/cacm_glove.txt > task_01/results/map_cacm_glove.txt
# analyze cacm with model all-MiniLM-L6-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_01/outputs/cacm_minil6.txt > task_01/results/map_cacm_minil6.txt
# analyze cacm with model all-MiniLM-L12-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_01/outputs/cacm_minil12.txt > task_01/results/map_cacm_minil12.txt
# analyze cacm with model all-mpnet-base-v2
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt task_01/outputs/cacm_mpnetv2.txt > task_01/results/map_cacm_mpnetv2.txt
# index npl
python3 bm25_index.py ./data/npl/npl.json npl_bm25
# index npl with model average_word_embeddings_glove.6B.300d
python3 embedding_index.py ./data/npl/npl.json npl_glove average_word_embeddings_glove.6B.300d
# index npl with model all-MiniLM-L6-v2
python3 embedding_index.py ./data/npl/npl.json npl_minil6 all-MiniLM-L6-v2
# index npl with model all-MiniLM-L12-v2
python3 embedding_index.py ./data/npl/npl.json npl_minil12 all-MiniLM-L12-v2
# index npl with model all-mpnet-base-v2
python3 embedding_index.py ./data/npl/npl.json npl_mpnetv2 all-mpnet-base-v2
# search npl
python3 bm25_search.py ./data/npl/queries.json npl_bm25 > task_01/outputs/npl_bm25.txt
# search npl with model average_word_embeddings_glove.6B.300d
python3 embedding_search.py ./data/npl/queries.json npl_glove average_word_embeddings_glove.6B.300d > task_01/outputs/npl_glove.txt
# search npl with model all-MiniLM-L6-v2
python3 embedding_search.py ./data/npl/queries.json npl_minil6 all-MiniLM-L6-v2 > task_01/outputs/npl_minil6.txt
# search npl with model all-MiniLM-L12-v2
python3 embedding_search.py ./data/npl/queries.json npl_minil12 all-MiniLM-L12-v2 > task_01/outputs/npl_minil12.txt
# search npl with model all-mpnet-base-v2
python3 embedding_search.py ./data/npl/queries.json npl_mpnetv2 all-mpnet-base-v2 > task_01/outputs/npl_mpnetv2.txt
# analyze npl
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_01/outputs/npl_bm25.txt > task_01/results/map_npl_bm25.txt
# analyze npl with model average_word_embeddings_glove.6B.300d
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_01/outputs/npl_glove.txt > task_01/results/map_npl_glove.txt
# analyze npl with model all-MiniLM-L6-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_01/outputs/npl_minil6.txt > task_01/results/map_npl_minil6.txt
# analyze npl with model all-MiniLM-L12-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_01/outputs/npl_minil12.txt > task_01/results/map_npl_minil12.txt
# analyze npl with model all-mpnet-base-v2
./trec_eval -m map -q ./data/npl/qrels-treceval.txt task_01/outputs/npl_mpnetv2.txt > task_01/results/map_npl_mpnetv2.txt
