# advanced-information-retrieval

## Prerequisites
This project uses [Elasticsearch](https://www.elastic.co/) as a tool to easily implement indexing, searching and retrieving data. To reproduce the results, a working installation of Elasticsearch is required. Information on how to install and start Elasticsearch can be found at https://www.elastic.co/downloads/elasticsearch.

Experiments also require [trec_eval](https://github.com/usnistgov/trec_eval), the standard tool used by the TREC community for evaluating an ad hoc retrieval run, given the results file and a standard set of judged results. The latest version can be downloaded from https://trec.nist.gov/trec_eval. Installation should be as easy as typing `make` in the source directory. Once successful, the generated `trec_eval` executable needs to be placed in the root directory of the project. More information can be found in the previously linked repository.

Finally, a working installation of Python is required as a prerequisite. All the necessary libraries to run all experiments can be installed with `pip install -r requirements.txt`. We recommend creating a virtual environment using a tool like [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Results reproduction

### Download and preprocess data
The content in the `data/` folder can be reproduced by running the `download_and_preprocess_data.sh` script. The script downloads the three datasets (MED, CACM, NPL) from source http://ir.dcs.gla.ac.uk/resources/test_collections/, parses them in the desired format, translates documents and queries, and summarizes documents. Since the process is very time consuming, the datasets are made available as part of the repository.

### Launch the experiments
To launch experiment $i \in {1,2,3,4}$, from the root directory run the following sequence of commands to generate the experiment shell script to be executed via the command line, give it permission to execute, and get the results.
```
python ./task_0i/write_experiment_0i.py
chmod +x ./task_0i/experiment_0i.sh
./task_0i/experiment_0i.sh
```
Search outputs get saved into the `task_0i/outputs` folder while `trec_eval` analysis are generated into `task_0i/results`