---
title: Datenanreicherung von Unternehmensdaten mittels DBpedia in RapidMiner
source_url_de: https://www.uni-mannheim.de/dws/research/projects/rapidminer-linked-open-data-extension/example-adding-background-information-from-dbpedia-with-multiple-generators/
source_url_en: None
category: Benutzung
tags: ['RapidMiner', 'DBpedia', 'Datenanreicherung', 'Workflow', 'Datenverarbeitung', 'Unternehmensdaten', 'Generatoren']
language: en
---

# Datenanreicherung von Unternehmensdaten mittels DBpedia in RapidMiner

Dieses Dokument beschreibt einen Workflow zur Anreicherung eines statistischen Datensatzes über Burnout-Raten in deutschen DAX-Unternehmen. Die Anreicherung erfolgt durch die Integration von Hintergrundinformationen aus der Linked Open Data Quelle DBpedia mithilfe der RapidMiner-Plattform.

**Datenquelle:**
Der Ausgangspunkt ist ein CSV-File, das Daten zum Frauenanteil in ausgewählten DAX-Unternehmen enthält.

- **Daten-CSV:** [women.csv](https://dws.informatik.uni-mannheim.de/fileadmin/lehrstuehle/ki/research/RapidMinerLODExtension/women.csv)
- **Workflow:** Der gesamte Workflow ist auf [myExperiment](http://www.myexperiment.org/workflows/3813.html) verfügbar.

## ⚙️ Workflow-Design und Datenverknüpfung

Der grundlegende Workflow zur Kombination mehrerer Generatoren folgt diesen Schritten:

1. **Multiplizieren der Outputs:** Die Outputs aller Linker werden multipliziert. Dies stellt sicher, dass sowohl die Datentabelle als auch die Liste der Attribute, die die Links enthalten, für die verschiedenen Generatoren verfügbar sind.
1. **Join-Operation:** Die Ergebnisse werden mithilfe des integrierten `Join`-Operators von RapidMiner zusammengeführt. Für diesen Join ist zwingend ein ID-Attribut erforderlich. Dieses kann entweder beim Datenimport oder mithilfe des `Set Role`-Operators gesetzt werden (im Beispiel wird letzteres verwendet).

### 🔗 Pattern-Based Linker zur DBpedia-Verknüpfung

Um den Unternehmensdatensatz mit DBpedia zu verknüpfen, wird ein **pattern-based linker** verwendet. Dieser generiert URIs basierend auf einem vom Benutzer definierten Muster.

- **Funktionsweise:** Der Linker verwendet den Wert des Feldes „Link to merge with“ und konkateniert diesen mit dem Wert des vom Benutzer spezifizierten Attributs.
- **Beispiel:** Der Attributwert „Henkel“ im Attribut „Company“ führt zum Link „http://dbpedia.org/resource/Henkel“.
- **Expertenparameter:**
  - **URL encoding:** Führt die Kodierung von Sonderzeichen durch.
  - **Use DBpedia link format:** Führt spezielle String-Operationen für das DBpedia-Link-Format durch. Beispielsweise werden Leerzeichen durch Unterstriche ersetzt, sodass „Deutsche Telekom“ zum Link „http://dbpedia.org/resource/Deutsche_Telekom“ wird.

## 🧬 Spezifische Generatoren zur Datenanreicherung

Im Beispiel werden zwei spezifische Generatoren eingesetzt, um unterschiedliche Arten von Hintergrundinformationen zu extrahieren:

### 1. Direct Types Generator

Dieser Generator erstellt für jeden direkten Typ ein boolesches Feature.

- **Funktion:** Er identifiziert die Klassifizierung eines Unternehmens (z.B. YAGO-Typen) in DBpedia.
- **Beispiel:** Das Unternehmen Henkel hat den Typ „ChemicalCompanies“ in DBpedia. Der Generator erstellt daher ein Attribut für diesen Typ, das für Henkel `true` und für andere Unternehmen `false` ist.

### 2. DataProperties Generator

Dieser Generator erstellt Features für alle Daten-Eigenschaften, die meist numerische Werte sind.

- **Funktion:** Er extrahiert quantitative Fakten über die Entitäten.
- **Beispiel:** Zu diesen Eigenschaften gehören Werte wie `netIncome`, `assets` und `numberOfEmployees`.

## 📊 Analyse und Erkenntnisse

Die Ergebnisse beider Generatoren werden mithilfe des `Join`-Operators zusammengeführt. Aus dem kombinierten Output kann eine Korrelationsmatrix berechnet werden, um Attribute zu untersuchen, die mit dem Zielattribut (Prozentsatz der weiblichen Mitarbeiter) korrelieren.

**Beobachtete Korrelationen:**

- **Mitarbeiterzahl vs. Frauenanteil:** Unternehmen mit einer großen Anzahl von Mitarbeitern weisen tendenziell einen niedrigeren Frauenanteil auf.
- **Betriebsergebnis vs. Frauenanteil:** Unternehmen mit einem hohen operativen Ergebnis zeigen einen niedrigeren Frauenanteil.
- **Branche vs. Frauenanteil:** Sportartikelhersteller weisen einen hohen Frauenanteil auf, während Kfz-Hersteller einen niedrigeren Anteil aufweisen.

**Fazit:**
Dieses Beispiel demonstriert, wie Daten über Entitäten (wie Unternehmen) aus externen Quellen wie DBpedia mithilfe verschiedener Generatoren gleichzeitig hinzugefügt werden können, um tiefgehende Analysen zu ermöglichen.
