---
title: Predicting Fuel Consumption using Linked Open Data and RapidMiner
source_url_de: https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-predicting-the-fuel-consumption-of-cars/
category: Projekte
tags: ['Kraftstoffverbrauch', 'Linked Open Data', 'DBpedia', 'RapidMiner', 'Datenanalyse', 'UCI', 'Auto MPG']
language: en
---

# Predicting Fuel Consumption using Linked Open Data

This example demonstrates how Linked Open Data can be used to improve the prediction of car fuel consumption.

The process utilizes the [UCI Auto MPG dataset](http://archive.ics.uci.edu/ml/datasets/Auto+MPG). The corresponding RapidMiner workflow can be downloaded from [myExperiment](http://www.myexperiment.org/workflows/4284.html), and the input CSV file is available [here](http://data.dws.informatik.uni-mannheim.de/rmlod/predictingfuelconsumption/auto-mpg.data).

The initial dataset contains car names and eight other attributes, including the label attribute MPG (miles per gallon). This project shows that incorporating additional background knowledge from [DBpedia](http://dbpedia.org) for each car significantly improves the prediction of fuel consumption.

## Workflow and Methodology

The overall workflow, depicted in Fig. 1, is divided into two sub-flows:

1. Predicting fuel consumption using only the initial dataset.
1. Predicting fuel consumption using additional knowledge extracted from DBpedia.

### Prediction Model

To predict fuel consumption, the [M5 Rules](http://weka.sourceforge.net/doc.dev/weka/classifiers/rules/M5Rules.html) operator is used, which is part of the [Weka extension](http://marketplace.rapid-i.com/UpdateServer/faces/product_details.xhtml?productId=rmx_weka).

### Linking Data to DBpedia

To link the car dataset to DBpedia, the **DBpedia Lookuplinker** is employed.

- **Query Class:** "Automobile"
- **API Used:** PrefixSearch API (as shown in Fig. 2).

The output of the linker is multiplied and passed to the feature generators:

- **Direct Typesgenerator:** Used to extract direct types.
- **Specific Relationgenerator:** Used to extract categories.

Both generators are configured with the standard DBpedia Sparql Endpoint.

**Specific Relation Extraction Details:**
In the Specific Relationgenerator, the desired relation for extraction is set to `"http://purl.org/dc/terms/subject"` (as shown in Fig. 3). Additionally, broader categories can be extracted by setting `"http://www.w3.org/2004/02/skos/core#broader"` as the relation for hierarchy, and specifying the desired hierarchy depth.

The output of both generators is joined into a single dataset. All attributes are then converted from nominal to numerical using the **Nominal to Numerical** operator. Finally, 10-fold cross-validation is performed using M5 Rules.

## Results and Conclusion

The following table summarizes the results for fuel consumption prediction, comparing the use of the initial plain dataset versus the enhanced datasets. The performance metric used is the **Relative Error**. Results for Linear Regression are also reported for each dataset.

It is evident that the best prediction results are achieved when combining attributes derived from both direct types and categories.

**Key Insights:**

- The new attributes provide insights not possible from the original dataset alone.
- The results indicate that UK cars have lower consumption compared to other origins (the original dataset only differentiated between America, Europe, and Asia).
- Front-wheel-drive cars show lower consumption than rear-wheel-drive ones (the corresponding category has a negative correlation with MPG at a level of 0.411), largely attributed to them being lighter.
- A correlation with the car's design can also be observed (e.g., hatchbacks having lower consumption than station wagons).
