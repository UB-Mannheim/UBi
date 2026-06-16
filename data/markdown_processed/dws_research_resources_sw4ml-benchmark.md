---
title: Benchmark Datasets für maschinelles Lernen auf dem Semantic Web
source_url_de: https://www.uni-mannheim.de/dws/research/resources/sw4ml-benchmark/
category: Services
tags: ['Machine Learning', 'Semantic Web', 'Benchmark', 'Datensätze', 'Linked Data', 'Evaluation']
language: en
---

# Benchmark Datasets für maschinelles Lernen auf dem Semantic Web

In den letzten Jahren wurden verschiedene Ansätze für maschinelles Lernen auf dem Semantic Web vorgeschlagen. Bisher fehlte es jedoch an umfassenden Vergleichen dieser Ansätze, insbesondere aufgrund eines Mangels an öffentlich verfügbaren, anerkannten Benchmark-Datensätzen.

Dieses Dokument stellt eine Sammlung von 22 Benchmark-Datensätzen unterschiedlicher Größe vor. Diese Datensätze stammen aus bestehenden Semantic Web-Datensätzen sowie aus externen Klassifizierungs- und Regressionsproblemen, die mit Datensätzen in der Linked Open Data (LOD) Cloud verknüpft sind. Diese Sammlung ermöglicht quantitative Leistungstests und systematische Vergleiche von Ansätzen und hilft zudem bei der Bestimmung der statistischen Signifikanz der Ergebnisse.

Die Datensätze und detaillierte Beschreibungen sind unter folgendem Link verfügbar: [http://data.dws.informatik.uni-mannheim.de/rmlod/LOD_ML_Datasets/](http://data.dws.informatik.uni-mannheim.de/rmlod/LOD_ML_Datasets/).

## Struktur der Datensammlung

Die Sammlung besteht aus 22 Datensätzen, die in drei Kategorien unterteilt sind:

1. **Bestehende Datensätze:** Datensätze, die häufig in ML-Experimenten verwendet werden.
1. **Datensätze aus offiziellen Beobachtungen:** Datensätze, die aus offiziellen Beobachtungen generiert wurden.
1. **Datensätze aus bestehenden RDF-Datensätzen:** Datensätze, die aus RDF-Quellen generiert wurden.

Die ersten beiden Kategorien sind anfänglich mit [DBpedia](http://dbpedia.org/) verknüpft. Dies dient mehreren Zwecken:

- [DBpedia](http://dbpedia.org/) ist eine plattformübergreifende Wissensbasis, die für Datensätze aus sehr unterschiedlichen Themenbereichen nutzbar ist.
- Tools wie [DBpedia](http://dbpedia.org/) Lookup und [DBpedia](http://dbpedia.org/) Spotlight erleichtern die Verknüpfung externer Datensätze mit [DBpedia](http://dbpedia.org/).

Wir nutzen die anfänglichen [DBpedia](http://dbpedia.org/) Links, um externe Links zu [YAGO](http://yago-knowledge.org/) und [Wikidata](http://www.wikidata.org/) zu extrahieren. Diese Verknüpfungen können für die systematische Bewertung der Relevanz von Daten verschiedener LOD-Datensätze in unterschiedlichen Lernaufgaben genutzt werden.

### 📊 Übersicht der Datensätze

**Existing ML Datasets**

| Dataset | Size | Type | Details | Status |
| :--- | :--- | :--- | :--- | :--- |
| Auto MPG | 371 | UCI ML | Regression | pending |
| AAUP | 960 | JSE | Regression/Classification (c=3) | pending |
| Auto 93 | 93 | JSE | Regression | pending |
| Zoo | 101 | UCI ML | Classification (c=3) | pending |
| Forbes | 1,585 | Forbes | Regression/Classification (c=2) | pending |
| Cities | 212 | Mercer | Regression/Classification (c=3) | pending |
| Facebook Books | 1,600 | Facebook | Regression/Classification (c=2) | pending |
| Facebook Movies | 1,600 | Facebook | Regression/Classification (c=2) | pending |
| Metacritic Albums | 1,600 | Metacritic | Regression/Classification (c=2) | pending |
| Metacritic Movies | 2,000 | Metacritic | Regression/Classification (c=2) | pending |
| HIV Deaths Country | 114 | WHO | Regression/Classification (c=2) | Open |
| Traffic Accidents Country | 146 | WHO | Regression/Classification (c=2) | Open |
| Energy Savings Country | 162 | WorldBank | Regression/Classification (c=2) | Open |
| Inflation Country | 160 | WorldBank | Regression/Classification (c=2) | Open |
| Scientific Journals Country | 160 | WorldBank | Regression/Classification (c=2) | Open |
| Unemployment French Region | 26 | SemStats 2013 | Regression/Classification (c=2) | pending |
| Endangered Species | 301 | a-z-animals | Regression/Classification (c=2) | pending |
| Drug-Food Interaction | 2,000 | FinkiLOD | Classification (c=2) | odc-by |

**Generated Datasets from Official Observations**

| Dataset | Size | Type | Details | License |
| :--- | :--- | :--- | :--- | :--- |
| AIFB | 176 | Classification (c=4) | CC-BY |
| AM | 1,000 | Classification (c=11) | cc-by-sa |
| MUTAG | 340 | Classification (c=2) | CC-BY |
| BGS | 146 | Classification (c=2) | Open |

**Datasets Generated from Existing RDF Datasets**
*(Keine spezifischen Datensätze in der Quelle aufgeführt, aber die Kategorie ist vorhanden.)*

## Link Quality Evaluation

Zur Bewertung der Qualität der DBpedia-Links wurden für jeden Datensatz zufällig mindestens 100 Instanzen (bei Datensätzen kleiner als 100 Instanzen wurden alle Instanzen) ausgewählt und die Korrektheit der Links manuell evaluiert.

| Dataset | Selected Instances | Evaluated Instances | Link Quality (%) |
| :--- | :--- | :--- | :--- |
| Auto MPG | 100 | 100 | 100.00 |
| AAUP | 100 | 100 | 100.00 |
| Auto 93 | 93 | 93 | 100.00 |
| Zoo | 101 | 99 | 98.01 |
| Forbes | 100 | 100 | 100.00 |
| Cities | 100 | 100 | 100.00 |
| Facebook Books | 100 | 98 | 98.00 |
| Facebook Movies | 130 | 130 | 100.00 |
| Metacritic Albums | 100 | 100 | 100.00 |
| Metacritic Movies | 130 | 128 | 98.46 |
| HIV Deaths Country | 114 | 114 | 100.00 |
| Traffic Accidents Country | 146 | 146 | 100.00 |
| Energy Savings Country | 162 | 162 | 100.00 |
| Inflation Country | 160 | 160 | 100.00 |
| Scientific Journals Country | 160 | 160 | 100.00 |
| Unemployment French Region | 26 | 26 | 100.00 |
| Endangered Species | 100 | 100 | 100.00 |
| Drug-Food Interaction | 100 | 100 | 100.00 |

## Zitierhinweis

Falls Sie die Sammlung von Datensätzen in Ihrer Forschung verwenden, zitieren Sie bitte das folgende Paper:

> Ristoski, P., de Vries, G.K.D., Paulheim, H.: A collection of benchmark datasets for systematic evaluations of machine learning on the semantic web. In: International Semantic Web Conference, 2016.
