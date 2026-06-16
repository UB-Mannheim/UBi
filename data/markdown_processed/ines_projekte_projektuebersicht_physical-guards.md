---
title: Physical Layer Security (Physical Guards) für Smart Homes
source_url_de: N/A
source_url_en: https://www.uni-mannheim.de/en/
category: Projekte
tags: ['Physical Layer Security', 'Smart Home', 'IoT-Sicherheit', 'KI', 'Intrusion Detection', 'Signalparameter', 'Verschlüsselung', 'Datenanalyse']
language: de
---

# Physical Guards: KI-basierte Absicherung von Smart Home Systemen

Das Projektkonzept „KI-basierte Analyse und Nutzung physikalischer Signalparameter zur Absicherung von Smart Home Systemen“ entwickelt den sogenannten „Physical-Guards“-Ansatz. Dieses Projekt leistet einen Beitrag zum Forschungsbereich „Physical Layer Security“ und dient der Weiterentwicklung des Standes der Technik aus den Bereichen IT-Security und Data Science/Machine Learning.

## 💡 Projektziel und Forschungsansatz

Der Physical-Guards-Ansatz nutzt physikalische Parameter (wie die lokale Signalstärke) der drahtlosen Kommunikation in Smart Homes, um die Sicherheit auf einer fundamentalen Ebene zu gewährleisten.

**Vorteile des Physical-Guards-Ansatzes:**

1. **Naturgesetzliche Grundlage:** Die physikalischen Eigenschaften von Kommunikationssignalen unterliegen Naturgesetzen. Die Berücksichtigung dieser Eigenschaften durch die Security-Infrastruktur macht viele Angriffsstrategien unmöglich oder erheblich erschwert.
1. **Heterogenität:** Im Gegensatz zu vielen höheren Schicht-Security-Lösungen ist dieser Ansatz nicht durch die große Heterogenität an Standards und Protokollen (z. B. Bluetooth, ZigBee, IEEE 802.15.4) in Smart Homes eingeschränkt.
1. **Unabhängigkeit:** Das System kann zusätzlich installiert werden, ohne Eingriff in die vorhandene Smart-Home-Infrastruktur oder die verwendeten Kommunikationsprotokolle.

Das Projektkonsortium aus der Universität Mannheim (Forschungsgruppen Dependable Systems Engineering und Institute for Enterprise Systems), M2M Germany und osapiens erforscht diesen Ansatz, realisiert Hard- und Softwarebausteine und evaluiert diese im wissenschaftlichen und Anwendungskontext.

## 🔬 Forschungs-Säulen der Physical-Guards-Technologie

Die Forschung konzentriert sich auf die Analyse und gezielte Manipulation physikalischer Signaleigenschaften drahtloser Kommunikation, da diese Methoden unabhängig von den verwendeten Protokollen (z. B. ISM-Band 2.4 GHz) sind.

### 1. Physical Intrusion Detection (PID)

- **Ziel:** Erkennung von IT-Sicherheitsvorfällen und Angriffsspuren.
- **Methode:** Physical Guards nutzt die Tatsache, dass selbst ein Angreifer physikalische Spuren hinterlassen kann. Es wird ein KI-basierter Klassifikator entwickelt, der auf Methoden des maschinellen Online-Learnings basiert.
- **Herausforderung:** Weiterentwicklung von Intrusion-Detection-Verfahren durch die Verarbeitung physikalischer Signalparameter, unter Einsatz von Forschungsansätzen aus Dynamic Data Streams, Knowledge Injection und Data Distillation.

### 2. Physical Integrity and Availability Enforcement (PIAE)

- **Ziel:** Verhinderung von Störungen (Jamming) und Manipulation des drahtlosen Kommunikationsmediums.
- **Methode:** Forschung an sogenannten **Jamming Resistant Bits**, die den Umstand ausnutzen, dass ein Angreifer den Beginn einer Nachricht physikalisch bedingt nicht manipulieren kann.
- **Herausforderung:** Entwicklung eines passenden Angreifermodells und die Balance zwischen Sicherheit und Praktikabilität.

### 3. Physical Confidentiality Protection (PCP)

- **Ziel:** Schutz vertraulicher Informationen vor unbefugtem Abhören (Eavesdropping).
- **Methode:** Die Physical-Guard-Architektur schützt die Kommunikation, indem eigene Signale gesendet werden, die mit den Nachrichten-Signalen überlagert werden. Diese Störsignale werden am Empfänger wieder annulliert. Angreifer können nur die überlagerten Signale abhören, nicht aber die ursprünglichen Nachrichtensignale bestimmen.
- **Herausforderung:** Entwicklung der Störsignale, die die Nachrichten ausreichend schützen, ohne andere Kommunikation im System ungewollt zu stören.

## 🤝 Projektpartner und Kernkompetenzen

### M2M Germany GmbH

M2M ist verantwortlich für die Entwicklung der physischen Komponenten:

- **Multi-Radio-Gateway („Center“):** Für die KI-basierte Überwachung sicherheitsrelevanter Ereignisse auf der Physical Layer.
- **Multi-Radio-Knoten („Guards“):** Zur aktiven Absicherung der Funkkommunikation im Smart Home Kontext.
- **Expertise:** Entwicklung, Produktion und Vertrieb von IoT-basierten Technologieneuheiten; verfügt über erfahrene Hard-, Firm- und Software-Entwicklungsingenieure.

### osapiens Services GmbH

osapiens bringt die KI- und Datenverarbeitungskompetenz ein:

- **Plattform:** Bereitstellung des „Augmentation Hub“, der Funktionen wie „AI Engine“ und „IoT Engine“ beinhaltet.
- **Fokus:** Schwerpunkt auf dem Prozessieren von Massendaten und deren Integration in den Learning-Prozess.
- **Beitrag:** Projektspezifische KI-Plattform-Entwicklung für die dynamische Einbeziehung von Attributen in neuronale Netze zur Detektion von Anomalien sowie die Entwicklung eines Dienstes zur Validierung von Sensordaten im Zeitverlauf.

______________________________________________________________________

*Die Physical-Guards-Technologie soll die klassischen CIA-Sicherheitsziele (Confidentiality, Integrity, Availability) durch physikalische Methoden verbessern.*
