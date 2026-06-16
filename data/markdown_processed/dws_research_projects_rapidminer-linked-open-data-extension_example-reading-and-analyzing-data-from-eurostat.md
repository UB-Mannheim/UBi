---
title: Datenanalyse von Linked Open Data (Eurostat) mit RapidMiner
source_url_de: https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-reading-and-analyzing-data-from-eurostat/
category: Benutzung
tags: ['RapidMiner', 'Eurostat', 'Linked Open Data', 'SPARQL', 'Datenanalyse', 'Korrelation', 'Workflow']
language: en
---

# Datenanalyse von Linked Open Data: Ein Beispiel mit Eurostat

Dieses Dokument demonstriert, wie Daten aus der Linked Open Data Quelle Eurostat gelesen und analysiert werden können. Der zugehörige RapidMiner Workflow kann unter [myExperiment](http://www.myexperiment.org/workflows/3757.html) heruntergeladen werden.

**Ziel des Beispiels:**
Die Analyse der Korrelation zwischen dem Bruttoinlandsprodukt (BIP) und dem Energieverbrauch europäischer Länder.

## 🛠️ Vorgehensweise in RapidMiner

Um Daten aus einer Linked Open Data Quelle wie Eurostat zu verarbeiten, sind folgende Schritte notwendig:

1. **SPARQL Endpoint definieren:**
   - Zuerst muss ein SPARQL Endpoint definiert werden. Dies geschieht über das Menü „Tools“ $\\rightarrow$ „Manage SPARQL Connections“.
1. **Datenimport (SPARQL Data Importer):**
   - Zum Lesen der Daten wird der Operator „SPARQL Data Importer“ verwendet.
   - Dieser Operator benötigt zwei Parameter: den zuvor definierten SPARQL Endpoint und einen SPARQL-Abfrage-Statement, das zur Erstellung der Tabelle dient.
   - Da das SPARQL-Statement drei Variablen (Land, BIP, Strom) enthält, wird eine Tabelle mit drei Spalten generiert. Die Datentypen werden automatisch zugewiesen (z. B. wird der Ländername als Textattribut, während BIP und Strom als numerisch erkannt werden).
1. **Korrelationsanalyse:**
   - Um einen ersten Eindruck zu gewinnen, kann die Streudiagramm-Ansicht (scatter plot view) von RapidMiner genutzt werden.
   - Für eine formale Berechnung der Korrelation wird der Output des „SPARQL Data Importer“ mit dem Operator „Correlation Matrix“ verbunden.

## 📊 Ergebnisse und Fazit

Die Analyse zeigt eine starke Korrelation zwischen dem BIP und dem Energieverbrauch der europäischen Länder.

**Zusammenfassend:**
Die RapidMiner Linked Open Data Extension ermöglicht es, Daten aus offenen Datenquellen wie Eurostat zu lesen und sie für weitere Analysen in RapidMiner zugänglich zu machen.
