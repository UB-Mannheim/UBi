---
title: Datenanreicherung mit Linked Open Data (Eurostat) in RapidMiner
source_url_de: https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-adding-background-data-from-eurostat/
category: Benutzung
tags: ['RapidMiner', 'Linked Open Data', 'Eurostat', 'Daten-Mining', 'Daten-Anreicherung', 'Entscheidungsbaum', 'Datenverarbeitung']
language: en
---

# Data Enhancement using Linked Open Data (Eurostat) in RapidMiner

This example demonstrates how to enhance an existing dataset with background data from a Linked Open Data source, specifically using Eurostat. The corresponding RapidMiner workflow can be downloaded from myExperiment.

### 1. Data Sources

- **Input Data:** The initial dataset is a CSV file containing country names and the alcohol consumption among adults. This original dataset was obtained from the [OECD](http://www.oecd-ilibrary.org/sites/9789264183896-en/02/06/index.html?contentType=/ns/StatisticalPublication,/ns/Chapter&itemId=/content/chapter/9789264183896-25-en&containerItemId=/content/serial/23056088&accessItemIds=&mimeType=text/html).
  - *Download Link:* The input CSV file is available [here](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Web_Data_Mining/RapidMiner/alcohol-eu.csv).
- **Background Data Source:** Eurostat (Linked Open Data).
- **Prerequisite:** It is assumed that the RapidMiner workflow has been prepared by configuring the SPARQL endpoint for Eurostat, as detailed in [this example](https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-reading-and-analyzing-data-from-eurostat/).

### 2. Data Processing Workflow in RapidMiner

The overall process is visualized in RapidMiner and involves several key steps:

#### A. Linking and Validation

1. **Linking:** The process begins by using the **Label-based linker** on the Eurostat dataset. This operator searches for entities whose labels match the country names present in the original dataset.
1. **Validation:** The **WebValidator** operator is then used to remove any instances that cannot be found or validated within the Eurostat source. The resulting table now contains established links to countries within Eurostat.

#### B. Data Property Generation

1. **Enhancement:** In the next step, the **DataPropertyGenerator** reads all available data properties (e.g., GDP, population, etc.) from the validated entities in the Eurostat dataset.
1. **Result:** This action enriches the original data table, resulting in a data table enhanced by many new attributes.

#### C. Modeling and Analysis

1. **Goal:** The objective is to create a predictive model for the target variable: alcohol consumption.
1. **Preprocessing:** Before training the decision tree, two preprocessing steps are necessary:
   - Missing values are replaced (as not all data properties exist for all countries).
   - The data is discretized, as the decision tree learning operator cannot handle numerical data.
1. **Modeling:** A decision tree is trained using the enhanced dataset.

### 3. Results and Conclusion

The resulting decision tree provides insights, such as:

- Alcohol consumption in smaller countries tends to be higher than in larger ones.
- Alcohol consumption is lower in countries experiencing large population growth.

**Summary:** The RapidMiner Linked Open Data extension successfully adds comprehensive background information to a given dataset. This capability allows for deeper analysis using both the original data and the newly added external context.
