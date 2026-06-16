---
title: Hybrid Recommender System using Linked Open Data in RapidMiner
source_url_de: https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-hybrid-recommender-system-using-linked-open-data/
source_url_en: None
category: Projekte
tags: ['Recommender', 'Linked Open Data', 'RapidMiner', 'DBpedia', 'SPARQL', 'Content-Based', 'Kollaborativ', 'Workflow']
language: en
---

# Hybrid Recommender System using Linked Open Data

This document describes the process of building a hybrid Linked Open Data (LOD) enabled recommender system for books using RapidMiner. The system combines multiple feature types extracted from LOD to enhance recommendation accuracy.

## 📚 Overview and Goal

The primary goal is to demonstrate how different types of features extracted from Linked Open Data can be combined to build a robust recommender system. The resulting system is a hybrid model combining:

1. A **Content-Based Recommender** (using extracted features).
1. A **User k-NN based Collaborative Recommender**.
1. An **Item k-NN based Collaborative Recommender**.

The corresponding RapidMiner workflow can be downloaded from [myExperiment](http://www.myexperiment.org/workflows/4285.html).

## ⚙️ Workflow Details

The overall workflow is depicted in Figure 1. The process involves three main stages: Feature Extraction, Content-Based Modeling, and Hybrid Combination.

### 1. Feature Extraction from Linked Open Data

The process begins by reading an input CSV file where all books are already linked to [DBpedia](http://dbpedia.org/). To extract additional features, three generators are used, all configured with the standard [DBpedia](http://dbpedia.org/) SPARQL endpoint:

- **Direct Types:** Extracts basic types.
- **Specific Relation:** Used to extract the direct categories of each book in the dataset.
- **Custom SPARQL Generator:** Used to retrieve complex relationships, such as:
  - The genres of the author.
  - Genres that influenced the author.
  - Genres of authors that influenced the current author, or authors influenced by the current author.

The output of these generators are joined into a single dataset, which is then prepared for the item attribute-based k-NN operator of the Recommender extension.

> **Reference:** For detailed instructions on input formats and the Recommender extension, please consult the [extension manual (PDF)](http://zel.irb.hr/wiki/lib/exe/fetch.php?media=del:projects:elico:recsys_manual_v1.1.pdf).

### 2. Content-Based Recommender

Using the item attribute-based k-NN operator, a content-based recommender is built. This recommender utilizes all features generated from DBpedia, providing recommendations based on the inherent attributes of the books.

### 3. Collaborative Modeling and Combination

Next, the training data, which contains user ratings for different books, is read into the system. This data is used to build two collaborative recommenders:

1. User k-NN based recommender.
1. Item k-NN based recommender.

Finally, all three models (Content-Based, User k-NN, and Item k-NN) are combined using the **Model Combiner** operator. The output of this operator is a single, comprehensive model capable of predicting ratings for unseen books.

______________________________________________________________________

**Data Sources:**

- **Challenge Data:** The data was obtained from the [Linked Open Data-enabled Recommender Systems Challenge](https://link.springer.com/chapter/10.1007/978-3-319-12024-9_17).
- **Input Files:** The input data files for the process can be downloaded [here](http://data.dws.informatik.uni-mannheim.de/rmlod/hybridrecommendersystem/input_data.zip).
