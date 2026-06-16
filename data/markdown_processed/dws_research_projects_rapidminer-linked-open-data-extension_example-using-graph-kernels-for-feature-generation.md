---
title: Graph Kernels zur Feature-Generierung mit RapidMiner
source_url_de: https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-using-graph-kernels-for-feature-generation/
category: Services
tags: ['Graph-Kernel', 'RapidMiner', 'RDF', 'Feature-Generierung', 'DBpedia', 'Daten-Mining', 'Weisfeiler-Lehman']
language: en
---

# Using Graph Kernels for Feature Generation in RapidMiner

This example demonstrates how to utilize graph kernels for advanced feature generation. The corresponding RapidMiner workflow can be downloaded from [myExperiment](http://www.myexperiment.org/workflows/4647.html).

The RapidMiner LOD extension integrates two distinct types of graph kernels for RDF data sourced from the [mustard library](https://github.com/Data2Semantics/mustard):

## 1. RDF Walk Count Kernel

This kernel counts the different walks found within the subgraphs (up to the specified Graph Depth) surrounding the instance nodes. The maximum length of the walks considered is controlled by the **Walk Length** parameter.

- **Fast:** A fast approximation of counting all walks in the subgraph (using the Full setting).
- **Root:** Only considers walks that start with the instance node (the root).
- **Tree:** Counts all walks in the subtree rooted at the instance node. This is faster than the Full subgraph version because a tree structure contains no cycles.
- **Full:** Counts all walks in the subgraph. *(Note: This variant is typically very slow.)*

## 2. RDF WL Sub Tree Kernel

This kernel counts the different full subtrees within the subgraphs (up to the specified Graph Depth) surrounding the instance nodes, utilizing the Weisfeiler-Lehman algorithm. The maximum size of the subtrees is controlled by the **Iterations** parameter.

- **Fast:** A fast approximation of counting all subtrees in the subgraph (using the Full setting).
- **Root:** Only considers subtrees that start with the instance node (the root). *(Note: This setting is included for completeness but is likely to yield poor results.)*
- **Tree:** Counts all subtrees in the subtree rooted at the instance node. This is faster than the Full subgraph version because a tree structure contains no cycles.
- **Full:** Counts all subtrees in the subgraph.

## Workflow Implementation Steps

In this specific example, the process uses the **Root RDF Walk Count Kernel** [1] and the **Fast RDF WL Sub Tree Kernel** [2].

The workflow begins by reading a CSV file. This file contains a list of French regions, each labeled with an unemployment rate and including a DBpeida URI for that region. The dataset can be retrieved [here](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Web_Data_Mining/RapidMiner/completedataset.txt).

**Graph Import:**

1. The "Graph Importer" operator is used to import a sub-graph from DBpedia for the French regions.
1. The DBpedia endpoint is selected, and the "DBpedia_URI" attribute is chosen for extension.
1. A graph depth of 2 is set, and the regular expression `http://dbpedia.org/property.*` is added to the "Properties to be avoid" parameter to exclude properties from the "dbprop" namespace.

**Kernel Application:**

1. The graph output of the "Graph Importer" operator is connected to the graph input port of the Kernel operators. This process is repeated for the ExampleSet.
1. Four graph kernel operators are configured and used:
   - Root RDF Walk Count Kernel (Walk Length 2)
   - Root RDF Walk Count Kernel (Walk Length 3)
   - Fast RDF WL Sub Tree Kernel (Graph Depth 1, 2 Iterations)
   - Fast RDF WL Sub Tree Kernel (Graph Depth 2, 2 Iterations)

______________________________________________________________________

**References:**
[1] “A Fast and Simple Graph Kernel for RDF”, GKD de Vries and S de Rooij, *DMoLD* (2013).
[2] “A fast approximation of the Weisfeiler-Lehman graph kernel for RDF data”, GKD de Vries, *Machine Learning and Knowledge Discovery in Databases*, 606–621 (2013).
