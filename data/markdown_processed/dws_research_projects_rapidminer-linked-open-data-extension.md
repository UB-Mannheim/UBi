---
title: RapidMiner Linked Open Data Extension – Data Mining with Web Knowledge
source_url_de: N/A
source_url_en: N/A
category: Services
tags: ['Linked Open Data', 'RapidMiner', 'Datenanalyse', 'Feature Generation', 'Semantic Web', 'Daten-Mining', 'SPARQL', 'Datenintegration']
language: en
---

# RapidMiner Linked Open Data Extension

The RapidMiner Linked Open Data (LOD) Extension is an add-on for the open-source data mining software [RapidMiner](http://rapid-i.com/content/view/181/190/). It enables users to incorporate data from [Linked Open Data](http://lod-cloud.net/) sources, allowing this data to be used both as input for data mining processes and for enriching existing datasets with background knowledge.

The extension is based on the earlier [FeGeLOD framework](http://www.ke.tu-darmstadt.de/resources/fegelod) (which is now discontinued).

## Key Features and Functionality

The extension is designed to work in a completely unsupervised manner, meaning that users generally do not require deep knowledge of the data source or technologies like RDF and SPARQL to begin using it.

The extension provides three main categories of operators:

1. **Data Importers:** Load data from Linked Open Data sources into RapidMiner for further processing.
1. **Linkers:** Create connections (links) between a given dataset and a dataset within Linked Open Data (e.g., linking a CSV file to DBpedia).
1. **Generators:** Gather data from Linked Open Data and add it as new attributes to the existing dataset.

Generators are highly customizable and can perform various tasks, such as:

- Adding specific data attributes (e.g., population).
- Adding categorical types (e.g., "G20 country").
- Adding aggregated relations (e.g., number of companies located in a city).
- Adding arbitrary data using customizable SPARQL statements.

These operators can be combined with built-in RapidMiner operators and other extensions to build powerful data mining processes.

## Use Cases and Examples

The extension supports diverse applications, including:

- **Data Import and Analysis:** Importing data from a Linked Data source, such as Eurostat, and analyzing it using RapidMiner operators.
- **Background Data Enrichment:** Adding data about population, GDP, and literacy from Eurostat to a dataset of countries.
- **Corporate Data Enrichment:** Adding data about turnover and number of employees from DBpedia to a dataset of companies.
- **Link Discovery:** Identifying potentially incorrect or missing links between datasets within Linked Open Data.
- **Predictive Modeling:** Predicting the fuel consumption of cars.
- **Recommender Systems:** Building hybrid recommender systems using Linked Open Data.
- **Feature Engineering:** Using Graph Kernels for advanced feature generation.

## Installation and Documentation

### Download

The RapidMiner Linked Open Data Extension is available from the [RapidMiner marketplace](https://marketplace.rapid-i.com/UpdateServer/faces/product_details.xhtml?productId=rmx_lod).

**To install the extension:**

1. Go to the “Help” $\\rightarrow$ “Updates and Extensions” menu in RapidMiner.
1. Search for “Linked Open Data”.

### Documentation

All operators and example workflows are described in the [user manual (PDF, 995 kB)](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Projects/RapidMinerLODExtensionManual.pdf).

## Publications and Research

The underlying algorithms and the extension itself have been described in numerous academic publications.

**Core Papers:**

- **Towards Linked Open Data enabled Data Mining:** Petar Ristoski (2015). [PDF](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Petar_Ristoski_-_PhD_Symposium_ESWC_2015.pdf). In: Extended Semantic Web Conference, 2015.
- **Data Mining with Background Knowledge from the Web:** Heiko Paulheim, Petar Ristoski, Evgeny Mitichkin, and Christian Bizer (2014). [PDF](http://www.heikopaulheim.com/documents/rmworld_2014.pdf). In: RapidMiner World, 2014.
- **Exploiting Linked Open Data as Background Knowledge in Data Mining:** Heiko Paulheim (2013). [PDF](http://ceur-ws.org/Vol-1082/extendedAbstract.pdf). In: CEUR workshop proceedings DMoLD 2013.
- **Unsupervised Generation of Data Mining Features from Linked Open Data:** Heiko Paulheim and Johannes Fürnkranz (2012). [PDF](http://www.heikopaulheim.com/documents/wims2012.pdf). In: International Conference on Web Intelligence, Mining, and Semantics (WIMS), 2012.

**Application-Specific Research:**

- **Identifying Wrong Links:** Heiko Paulheim (2014). [PDF](http://www.heikopaulheim.com/documents/wodoom_2014.pdf). In: Third International Workshop on Debugging Ontologies and Ontology Mappings (WoDOOM 2014).
- **Statistical Analysis:**
  - Heiko Paulheim (2012). [Generating Possible Interpretations for Statistics from Linked Open Data (PDF)](http://www.heikopaulheim.com/documents/eswc_2012.pdf). In: 9th Extended Semantic Web Conference, ESWC 2012.
  - Petar Ristoski and Heiko Paulheim (2013). [Analyzing Statistics with Background Knowledge from Linked Open Data (PDF)](http://www.heikopaulheim.com/documents/semstats_2013.pdf). In: First International Workshop on Semantic Statistics (SemStats 2013).
  - Petar Ristoski and Heiko Paulheim (2015). [Visual Analysis of Statistical Data on Maps using Linked Open Data (PDF, 896 kB)](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Web_Data_Mining/Ristoski_Paulheim_VisualAnalysisOfStatisticalDataOnMapsUsingLinkedOpenData.pdf). In: 12th Extended Semantic Web Conference, ESWC 2015.
- **Social Media & Event Data:**
  - Axel Schulz, Petar Ristoski and Heiko Paulheim (2013). [I See a Car Crash: Real-time Detection of Small Scale Incidents in Microblogs (PDF)](http://www.heikopaulheim.com/documents/smile2013.pdf). In: Workshop on Social Media and Linked Data for Emergency Response (SMILE), 2013.
  - Axel Schulz, Aristotelis Hadjakos, Heiko Paulheim, Johannes Nachtwey, Max Mühlhäuser (2013). [A Multi-Indicator Approach for Geolocalization of Tweets (PDF)](http://www.heikopaulheim.com/documents/icwsm2013.pdf). In: International AAAI Conference on Weblogs and Social Media (ICWSM 2013).
  - Daniel Hienert, Dennis Wegener and Heiko Paulheim (2012). [Automatic Classification and Relationship Extraction for Multi-Lingual and Multi-Granular Events from Wikipedia (PDF)](http://www.heikopaulheim.com/documents/derive2012.pdf). In: Proceedings of the Workhop on Detection, Representation, and Exploitation of Events in the Semantic Web (DeRiVE 2012).
- **Ontology Matching:** Frederik Janssen, Faraz Fallahi, Jan Nößner and Heiko Paulheim (2012). [Towards Rule Learning Approaches to Instance-based Ontology Matching (PDF)](http://www.ke.tu-darmstadt.de/know-a-lod-2012/wp-content/uploads/2012/04/knowalod2012_submission_2.pdf). In: Proceedings of the First International Workshop on Knowledge Discovery and Data Mining Meets Linked Open Data.

## Support & Community

Users are encouraged to join the Google Group at [https://groups.google.com/forum/#!forum/rmlod](https://groups.google.com/forum/#!forum/rmlod) or contact the user community via its mailing list.

## Team

**Project Lead:**

- [Heiko Paulheim](https://www.uni-mannheim.de/dws/people/professors/prof-dr-heiko-paulheim/)

**Current Team:**

- [Christian Bizer](https://www.uni-mannheim.de/dws/people/professors/prof-dr-christian-bizer/)
- Evgeny Mitichkin
- Petar Ristoski

**Past Contributors:**

- Raad Bahmani
- [Johannes Fürnkranz](http://www.ke.tu-darmstadt.de/staff/juffi)
- Alexander Gabriel
- Simon Holthausen
