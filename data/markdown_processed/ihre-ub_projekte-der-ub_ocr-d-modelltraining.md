---
title: OCR-D: Workflow für werk­spezifisches Training auf Basis generischer Modelle mit OCR-D sowie Ground-Truth-Aufwertung
source_url: https://www.bib.uni-mannheim.de/ihre-ub/projekte-der-ub/ocr-d-modelltraining/
category: Projekte
tags: [OCR-D, Workflow, werksspezifisches Training, generische Modelle, Ground Truth, Texterkennung, neuronale Netze, Finetuning, Volltextdigitalisierung, DFG-Förderung]
language: de
---

# OCR-D: Workflow für werk­spezifisches Training auf Basis generischer Modelle mit OCR-D sowie Ground-Truth-Aufwertung

**Kontakt:** [Stefan Weil](https://www.bib.uni-mannheim.de/ihre-ub/ansprechpersonen/stefan-weil/)  
**Förderung:** Deutsche Forschungs­gemeinschaft (DFG)  
**Laufzeit:** 2021–2023  
**Abschlussbericht:** [Workflow für werk­spezifisches Training auf Basis generischer Modelle mit OCR-D sowie Ground-Truth-Aufwertung](https://madoc.bib.uni-mannheim.de/67174/)

---

## Hintergrund und Zielsetzung

Im Rahmen des Koordinierungsprojekts [OCR-D](https://ocr-d.de/de/) fördert die DFG seit 2015 verschiedene Projekte zur Entwicklung eines Verfahrens zur Massenvolltextdigitalisierung der im deutschen Sprachraum erschienenen Drucke des 16. bis 19. Jahrhunderts. In der aktuellen dritten Förderphase arbeitet die Universitätsbibliothek Mannheim an einem Workflow für das werksspezifische Nachtraining mit Hilfe von generischen Modellen.

Bei der modernen Volltexterkennung bilden häufig mühsam händisch bzw. halb-automatisiert erfasste Trainingsdaten (Ground Truth) die Grundlage für die Texterkennung mittels künstlicher neuronaler Netze. Dies führt dazu, dass auch die durch die Transkription entstandenen Fehler von den neuronalen Netzen mittrainiert werden. Außerdem basieren die vorhandenen Modelle oftmals auf einzelnen Sprachen oder Schriftarten, die die tatsächlichen Werke nicht komplett abdecken können. Als Resultat entstehen fehlerhafte Modelle mit mangelhafter Genauigkeitsquote.

---

## Methodik und Vorteile des werksspezifischen Nachtrainings

Mit Hilfe generischer Modelle, die bereits mit unterschiedlichen Sprachen und Schriften trainiert sind, lässt sich diese Problematik umgehen. Durch das Nachtraining (Finetuning) eines generischen Modells kann die Genauigkeit für ein spezifisches Werk auf über 98 Prozent gesteigert werden. Auch spezielle Zeichen und Symbole lassen sich durch ein werksspezifisches Nachtraining besser erfassen.

Ziel des Projektes ist es, dass Einrichtungen unterschiedlicher Größe möglichst einfach die Module des OCR-D-Workflows nachtrainieren können, sodass bessere Erkennungsraten für spezifische Werke erreicht werden. Die Anwender sollen dabei durch softwaretechnische Werkzeuge Anleitungen erhalten und durch Best-Practice-Empfehlungen unterstützt werden. Außerdem wird ein zentrales und öffentliches Modellrepositorium erstellt, um die Auffindbarkeit der Modelle zu gewährleisten.

---

## Weiterführende Informationen

- [Projektseite DFG](https://gepris.dfg.de/gepris/projekt/460547474?context=projekt&task=showDetail&id=460547474&)