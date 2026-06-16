---
title: MinIE – Open Information Extraction System for NLP Research
source_url_de: https://www.uni-mannheim.de/dws/research/resources/minie/
category: Projekte
tags: ['Open Information Extraction', 'NLP', 'Triples', 'Forschung', 'Daten', 'System', 'Textanalyse']
language: en
---

# MinIE: Open Information Extraction System

MinIE is an Open Information Extraction (OIE) system designed to extract useful information from natural language sentences in an unsupervised manner. The system represents extracted information in the form of semantic triples.

MinIE enhances the extraction process by annotating information regarding polarity, modality, and attribution, rather than relying solely on the raw extraction. Furthermore, it identifies and removes overly specific words from the extractions, resulting in shorter, semantically enriched extractions with high precision and recall.

## 📚 Resources and Implementation

### Publication

The foundational work on MinIE is detailed in the following publication:

- **MinIE: Minimizing Facts in Open Information Extraction**
  - *Authors:* Kiril Gashteovski, Rainer Gemulla, Luciano del Corro
  - *Conference:* Conference on Empirical Methods in Natural Language Processing (EMNLP), 2017
  - *Link:* [http://aclweb.org/anthology/D17-1278](http://aclweb.org/anthology/D17-1278)

### Source Code and Documentation

The system's source code and detailed documentation are available online:

- **GitHub Repository:** [https://github.com/rgemulla/minie](https://github.com/rgemulla/minie)
- **Documentation:** [https://rgemulla.github.io/minie/](https://rgemulla.github.io/minie/)

## 💾 Datasets and Guides

### Datasets for Experiments

The following datasets were used in the paper's experiments and are available for download:

- [NYT Dataset](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Software/MinIE/NYT.zip)
- [Wikipedia Dataset](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Software/MinIE/Wiki.zip)
- [NYT-10k Dataset](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Software/MinIE/nyt10k.zip)

### Dictionary Resources

A dictionary containing frequent relations and arguments is provided:

- **Wikipedia Frequent Relations and Arguments:** [zip](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Software/MinIE/wiki-freq-args-rels.zip)

### Labeling Guide

For human judges requiring guidelines on labeling:

- [MinIE Labeling Guide](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Software/MinIE/minie-labeling-guide.pdf)
