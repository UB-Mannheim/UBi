---
title: Identifying Wrong Links Between Datasets using Outlier Detection
source_url_en: https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-discovering-wrong-links-between-datasets/
category: Projekte
tags: ['Linked Open Data', 'Outlier Detection', 'Datensätze', 'Verlinkung', 'Anomaly Detection', 'DBpedia', 'EventMedia']
language: en
---

# Discovering Wrong Links Between Datasets

Links between datasets are an essential ingredient to the [Linked Open Data cloud](http://lod-cloud.net/). Since creating links manually is not scalable, automatic tools, such as [Silk](https://wifo5-03.informatik.uni-mannheim.de/bizer/silk/), are often used to create links using heuristics. While these tools can generate large amounts of links efficiently, they may not be 100% accurate.

This example demonstrates how to use [outlier detection](http://en.wikipedia.org/wiki/Outlier_detection) to identify erroneous links. The process combines operators from the Linked Open Data extension with those from the [Anomaly Detection extension](http://madm.dfki.de/rapidminer/anomalydetection).

## Methodology Overview

In this specific example, we read links between the [EventMedia dataset](https://eventmedia.eurecom.fr/) and [DBpedia](http://dbpedia.org/) and identify errors among those links. The overall process involves three main steps:

1. Reading the links between the two datasets.
1. Creating features for the types of each linked resource.
1. Identifying suspicious links using outlier detection.

The full process is available from [myExperiment](http://www.myexperiment.org/workflows/4159.html).

## Step-by-Step Process

### 1. Reading the Links

The process begins by reading the list of links from the EventMedia dataset to DBpedia using the SPARQL data importer.

### 2. Feature Creation

Next, features are created for the direct types of both linked resources:

- **EventMedia Resources:** The Direct Types generator is used.
- **DBpedia Resources:** A custom SPARQL generator is used to ensure that only types from the DBpedia ontology are included.

### 3. Identifying Outliers

Finally, the Local Outlier Factor (LOF) operator from the Anomaly Detection extension is applied. This operator finds links whose pattern of types deviates significantly from the overall pattern.

The result is a list of links accompanied by scores. These scores can be sorted to pinpoint the most suspicious links.

## Analysis of Results

Upon reviewing the results, the top 5 identified links contained three links that were actually incorrect:

- The first two links incorrectly refer to rivers in DBpedia, but they actually link to music clubs of the same name in EventMedia.
- The fifth link links a DBpedia concept to a non-dereferencable URI.

The remaining two elements in the top 5 were a bridge and a library. While these are technically correct links, they are rare event locations, and thus were identified as outliers by the system.
