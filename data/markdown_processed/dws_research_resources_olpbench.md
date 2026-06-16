---
title: OLPBENCH – Open Link Prediction Benchmark
source_url_de: https://www.uni-mannheim.de/dws/research/resources/olpbench/
category: Projekte
tags: ['Open Link Prediction', 'Knowledge Graph', 'Benchmark', 'OPIEC', 'NLP', 'Daten', 'Forschung']
language: en
---

# OLPBENCH: Open Link Prediction Benchmark

OLPBENCH is a large-scale Open Link Prediction benchmark. It was derived from the state-of-the-art Open Information Extraction corpus (OPIEC) (Gashteovski et al., 2019).

The benchmark contains:

- 30 million open triples.
- 1 million distinct open relations.
- 2.5 million distinct mentions of approximately 800,000 entities.

### Understanding Open Link Prediction

Open Link Prediction is defined as follows: Given an Open Knowledge Graph and a question consisting of an entity mention and an open relation, the goal is to predict mentions that serve as answers. A predicted mention is considered correct if it is a mention of the correct answer entity.

**Example:** Given the question (“NBC-TV”, “has office in”, ?), correct answers include “NYC” and “New York”.

## Publication Details

The benchmark was presented in the following publication:

**Title:** Can We Predict New Facts with Open Knowledge Graph Embeddings? A Benchmark for Open Link Prediction
**Authors:** Samuel Broscheit, Kiril Gashteovski, Yanjie Wang, Rainer Gemulla
**Conference:** The 58th Annual Meeting of the Association for Computational Linguistics (ACL), 2020
**Paper:** [PDF Link](https://www.aclweb.org/anthology/2020.acl-main.209.pdf)

## Resources and Downloads

### OLPBENCH Corpus Data

The full dataset used in the paper's experiments is available for download. This includes all data types (train THOROUGH, BASIC, SIMPLE, valid ALL, MENTION, LINKED, and test).

- **Full Data Download:** [http://data.dws.informatik.uni-mannheim.de/olpbench/olpbench.tar.gz](http://data.dws.informatik.uni-mannheim.de/olpbench/olpbench.tar.gz)
  *(Note: Compressed size is ~2.4 GB; uncompressed size is ~7.9 GB)*

### Code Implementation

The code required for creating OLPBENCH from OPIEC and for training the models used in the paper will be published on GitHub.

- **GitHub Repository:** [https://github.com/samuelbroscheit](https://github.com/samuelbroscheit)
