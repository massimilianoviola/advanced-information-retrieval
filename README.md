# Advanced IR Experiments with Language Models, Summarization and Translation using SBERT, Elasticsearch and trec_eval

This repository contains the implementation of the final project for the **Advanced Information Retrieval** course that took place at TU Graz during the winter semester of 2022. The goal of the project is to perform advanced IR experiments, covering topics such as document summarization, query and document translation, neural and multilingual IR with pre-trained and fine-tuned language models, often compared against traditional BM25-based retrieval. Furthermore, established tools in the IR community, Elasticsearch and trec_eval, are utilized to efficiently implement and easily evaluate complex experiments across multiple datasets.

## Authors
David Mihola, Manuel Riedl, Massimiliano Viola, Nico Ohler.

## Tasks and datasets description

Using common building blocks from the root directory, the repository contains four folders for running experiments. In summary, it implements the following ideas:
- `task_01/`: compare BM25-based indexing and retrieval against neural IR powered by language models.
- `task_02/`: compare the retrieval performance of summarized documents against standard documents.
- `task_03/`: evaluate the effect of translating English documents and queries to German.
- `task_04/`: perform multilingual IR with queries in different languages (English and German) on English docs.

Each experiment is replicated across three different datasets (MED, CACM, NPL), available to download at http://ir.dcs.gla.ac.uk/resources/test_collections, to verify the consistency of results. Here is a brief description of dataset domains and sizes:
- **Medline**: a collection of articles from a medical journal with 1033 documents and 30 queries.
- **CACM**: a collection of titles and abstracts from the journal CACM with 3204 documents and 64 queries.
- **NPL**: a collection of document titles with 11429 records and 93 queries.

## Results reproduction

### Prerequisites

- This project uses [Elasticsearch](https://www.elastic.co) as a tool to easily implement indexing, searching and retrieving data. To reproduce the results, a working installation of Elasticsearch is required. Information on how to install and start Elasticsearch can be found at https://www.elastic.co/downloads/elasticsearch.
- Experiments also require [trec_eval](https://github.com/usnistgov/trec_eval), the standard tool used by the TREC community for evaluating an ad hoc retrieval run, given the results file and a standard set of judged results. The latest version can be downloaded from https://trec.nist.gov/trec_eval. Installation should be as easy as typing `make` in the source directory. Once successful, the generated `trec_eval` executable needs to be placed in the root directory of the project. More information can be found in the previously linked repository.
- Finally, a working installation of **Python on a MacOS or Linux system** is required as a prerequisite. All the necessary libraries to run all experiments can be installed with `pip install -r requirements.txt`. We recommend creating a virtual environment using a tool like [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

### Download and preprocess data

The content in the `data/` folder can be reproduced by running the `download_and_preprocess_data.sh` script, which downloads the three datasets (MED, CACM, NPL) from source http://ir.dcs.gla.ac.uk/resources/test_collections, parses them in the desired format, translates documents and queries, and summarizes documents. Since the process is very time-consuming, processed datasets are made available as part of the repository.

### Launch the experiments

To launch experiment $i \in {1,2,3,4}$, first start an Elasticsearch instance by running `bin/elasticsearch` from the Elasticsearch download folder. Then, from another terminal window where the working environment has been activated, run the following sequence of commands from the root directory of the project to generate the experiment shell script, give it permission to execute, and get the results.
```
python ./task_0i/write_experiment_0i.py
chmod +x ./task_0i/experiment_0i.sh
./task_0i/experiment_0i.sh
```
This ensures that Elasticsearch outputs are saved in the `task_0i/outputs` folder while trec_eval analysis is generated in `task_0i/results`.
