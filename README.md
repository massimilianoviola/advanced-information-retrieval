# advanced-information-retrieval

## Prerequisites
This project uses [Elasticsearch](https://www.elastic.co/) as a tool to easily implement indexing, searching and retrieving data. To reproduce the results, a working installation of Elasticsearch is required. More can be found at https://www.elastic.co/downloads/elasticsearch

This project also uses trec_eval, the standard tool used by the TREC community for evaluating an ad hoc retrieval run, given the results file and a standard set of judged results. After downloading the latest version from https://trec.nist.gov/trec_eval/, installation should be as easy as typing "make" in the source directory. Once successful, place the executable `trec_eval` in the root directory of the project. More information can be found at https://github.com/usnistgov/trec_eval

Finally, a working installation of Python is required as a prerequisite. All the necessary libraries to run all experiments can then be installed with `pip install -r requirements.txt`. 

## Results reproduction

### Download and preprocess data
The content in the `data/` folder can be reproduced by running the `download_and_preprocess_data.sh` script. The script downloads the three datasets (MED, CACM, NPL) from source http://ir.dcs.gla.ac.uk/resources/test_collections/, parses them in the desired format, translates documents and queries, and summarizes documents over a specified length. Since the process takes a while, the datasets are available as part of the repository.

### Launch the experiments
To launch experiment $i \in {1,2,3,4}$, from the root directory run the following sequence of commands to generate the experiment shell script to be executed via the command line, give it permission to execute, and get the results.
```
python ./task_0i/write_experiment_0i.py
chmod +x ./task_0i/experiment_0i.sh
./task_0i/experiment_0i.sh
```
Search outputs get saved into the `task_0i/outputs` folder while `trec_eval` analysis are generated into `task_0i/results`