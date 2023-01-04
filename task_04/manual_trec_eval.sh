# script for manual evaluation without prior search
# ml_miniLM_L12_v2
# german
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt ./task_04/outputs/ml_miniLM_L12_v2_cacm_DE.txt > ./task_04/results/map_ml_miniLM_L12_v2_cacm_DE.txt
./trec_eval -m map -q ./data/med/qrels-treceval.txt ./task_04/outputs/ml_miniLM_L12_v2_med_DE.txt > ./task_04/results/map_ml_miniLM_L12_v2_med_DE.txt
./trec_eval -m map -q ./data/npl/qrels-treceval.txt ./task_04/outputs/ml_miniLM_L12_v2_npl_DE.txt > ./task_04/results/map_ml_miniLM_L12_v2_npl_DE.txt

# english
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt ./task_04/outputs/ml_miniLM_L12_v2_cacm_EN.txt > ./task_04/results/map_ml_miniLM_L12_v2_cacm_EN.txt
./trec_eval -m map -q ./data/med/qrels-treceval.txt ./task_04/outputs/ml_miniLM_L12_v2_med_EN.txt > ./task_04/results/map_ml_miniLM_L12_v2_med_EN.txt
./trec_eval -m map -q ./data/npl/qrels-treceval.txt ./task_04/outputs/ml_miniLM_L12_v2_npl_EN.txt > ./task_04/results/map_ml_miniLM_L12_v2_npl_EN.txt

# ml_mpnet_base_v2
# german
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt ./task_04/outputs/ml_mpnet_base_v2_cacm_DE.txt > ./task_04/results/map_ml_mpnet_base_v2_cacm_DE.txt
./trec_eval -m map -q ./data/med/qrels-treceval.txt ./task_04/outputs/ml_mpnet_base_v2_med_DE.txt > ./task_04/results/map_ml_mpnet_base_v2_med_DE.txt
./trec_eval -m map -q ./data/npl/qrels-treceval.txt ./task_04/outputs/ml_mpnet_base_v2_npl_DE.txt > ./task_04/results/map_ml_mpnet_base_v2_npl_DE.txt

# english
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt ./task_04/outputs/ml_mpnet_base_v2_cacm_EN.txt > ./task_04/results/map_ml_mpnet_base_v2_cacm_EN.txt
./trec_eval -m map -q ./data/med/qrels-treceval.txt ./task_04/outputs/ml_mpnet_base_v2_med_EN.txt > ./task_04/results/map_ml_mpnet_base_v2_med_EN.txt
./trec_eval -m map -q ./data/npl/qrels-treceval.txt ./task_04/outputs/ml_mpnet_base_v2_npl_EN.txt > ./task_04/results/map_ml_mpnet_base_v2_npl_EN.txt

# dbmlc_v1
# german
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt ./task_04/outputs/dbmlc_v1_cacm_DE.txt > ./task_04/results/map_dbmlc_v1_cacm_DE.txt
./trec_eval -m map -q ./data/med/qrels-treceval.txt ./task_04/outputs/dbmlc_v1_med_DE.txt > ./task_04/results/map_dbmlc_v1_med_DE.txt
./trec_eval -m map -q ./data/npl/qrels-treceval.txt ./task_04/outputs/dbmlc_v1_npl_DE.txt > ./task_04/results/map_dbmlc_v1_npl_DE.txt

# english
./trec_eval -m map -q ./data/cacm/qrels-treceval.txt ./task_04/outputs/dbmlc_v1_cacm_EN.txt > ./task_04/results/map_dbmlc_v1_cacm_EN.txt
./trec_eval -m map -q ./data/med/qrels-treceval.txt ./task_04/outputs/dbmlc_v1_med_EN.txt > ./task_04/results/map_dbmlc_v1_med_EN.txt
./trec_eval -m map -q ./data/npl/qrels-treceval.txt ./task_04/outputs/dbmlc_v1_npl_EN.txt > ./task_04/results/map_dbmlc_v1_npl_EN.txt
