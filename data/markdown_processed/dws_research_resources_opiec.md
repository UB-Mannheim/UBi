---
title: OPIEC Corpus – Open Information Extraction Data from Wikipedia
source_url_de: https://www.uni-mannheim.de/dws/research/resources/opiec/
source_url_en: https://www.uni-mannheim.de/dws/research/resources/opiec/
category: Medien
tags: ['OPIEC', 'Informationsextraktion', 'Wikipedia', 'NLP', 'Korpus', 'Daten', 'OpenIE']
language: en
---

# OPIEC: Open Information Extraction Corpus

OPIEC is an Open Information Extraction (OIE) corpus constructed from the entire English Wikipedia. It contains over 341 million triples. Each triple is rich with metadata, including:

- **Token-level annotations**: POS tags, NER tags, etc., for the subject, object, and relation.
- **Provenance**: The original sentence (with its dependency parse) and the sentence's order relative to the article.
- **Links**: Original (golden) links contained within the Wikipedia articles, along with space/time information.

For a detailed explanation of the metadata, please see the [OPIEC pipeline documentation](https://github.com/uma-pi1/OPIEC-pipeline#metadata).

## 📚 Data Resources

The corpus is available in three main versions, allowing users to select the level of data cleaning required:

### 1. OPIEC Corpus Versions

| Corpus Type | Description | Full Data Download | Example File |
| :--- | :--- | :--- | :--- |
| **OPIEC-full** | The complete, raw corpus. | [Full data](http://data.dws.informatik.uni-mannheim.de/opiec/OPIEC-full.zip) (~928.7 GB uncompressed) | [Example file](http://data.dws.informatik.uni-mannheim.de/opiec/OPIEC-Raw-example.avro) (~129 M) |
| **OPIEC-Clean** | Contains arguments considered "clean" (filtered). | [Full data](http://data.dws.informatik.uni-mannheim.de/opiec/OPIEC-Clean.zip) (~292.4 GB uncompressed) | [Example file](http://data.dws.informatik.uni-mannheim.de/opiec/OPIEC-Clean-example.avro) (~40 MB) |
| **OPIEC-Linked** | Contains fully linked arguments. | [Full data](http://data.dws.informatik.uni-mannheim.de/opiec/OPIEC-Linked.zip) (~19.8 GB uncompressed) | [Example file](http://data.dws.informatik.uni-mannheim.de/opiec/OPIEC-Linked-example.avro) (~2.4 MB) |

### 2. Bonus Corpus: WikipediaNLP

As an additional resource, the entire English Wikipedia is provided with comprehensive NLP annotations (dependency parse, POS tags, NER tags, etc.).

- **Full data**: [WikiNLP.zip](http://data.dws.informatik.uni-mannheim.de/opiec/WikiNLP.zip) (~155 GB uncompressed)
- **Example file**: [WikiNLP-example.avro](http://data.dws.informatik.uni-mannheim.de/opiec/WikiNLP-example.avro) (~327 MB)

## 📰 Publications

The following are key publications related to the OPIEC corpus:

- **OPIEC: An Open Information Extraction Corpus**

  - Kiril Gashteovski, Sebastian Wanner, Sven Hertling, Samuel Broscheit, Rainer Gemulla (2019).
  - [OpenReview](https://openreview.net/forum?id=HJxeGb5pTm) | [PDF](https://openreview.net/pdf?id=HJxeGb5pTm) | [Author's version (arXiv)](https://arxiv.org/abs/1904.12324)
  - *In Proc. of Conference on Automated Knowledge Base Construction (AKBC), 2019.*

- **On Aligning OpenIE Extractions with Knowledge Bases: A Case Study**

  - Kiril Gashteovski, Rainer Gemulla, Bhushan Kotnis, Sven Hertling, Christian Meilicke (2020).
  - [PDF](https://www.aclweb.org/anthology/2020.eval4nlp-1.14.pdf) | [Slides](https://www.uni-mannheim.de/media/Einrichtungen/dws/pi1/opiec/dsa-ota-talk-final.pdf) | [Resources](https://www.uni-mannheim.de/media/Einrichtungen/dws/pi1/opiec/opiec_dbpedia_study.zip)
  - *In Proc. of Workshop on Evaluation and Comparison of NLP Systems (Eval4NLP at EMNLP), 2020.*

## 💻 Code and Licensing

- **Code for Reading Data**: [GitHub Repository](https://github.com/uma-pi1/OPIEC)
- **Code for Corpus Construction**: [GitHub Repository](https://github.com/uma-pi1/OPIEC-pipeline)

**Licenses:**

- **Code**: Licensed under the [GPL-3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html).
- **Data**: Licensed under the [Creative Commons Attribution Share-Alike license](https://en.wikipedia.org/wiki/Wikipedia:CCBYSA) (CC-BY-SA) and the [GNU Free Documentation License](https://en.wikipedia.org/wiki/Wikipedia:Text_of_the_GNU_Free_Documentation_License).
