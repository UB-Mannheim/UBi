```yaml
title: OCR-D: Workflow für werk­spezifisches Training
source_url: https://www.bib.uni-mannheim.de/ihre-ub/projekte-der-ub/ocr-d-modelltraining/
tags: [OCR-D, Modelltraining, DFG, Volltextdigitalisierung]
language: de
```

# OCR-D: Workflow für werk­spezifisches Training

**Kontakt:** [Stefan Weil](https://www.bib.uni-mannheim.de/ihre-ub/ansprechpersonen/stefan-weil/)  
**Förderung:** Deutsche Forschungs­gemeinschaft (DFG)  
**Laufzeit:** 2021–2023  
**Abschlussbericht:** [Workflow für werk­spezifisches Training auf Basis generischer Modelle mit OCR-D sowie Ground-Truth-Aufwertung](https://madoc.bib.uni-mannheim.de/67174/)  

Im Rahmen des Koordinierungs­projekts [OCR-D](https://ocr-d.de/de/) fördert die DFG seit 2015 verschiedene Projekte zur Entwicklung eines Verfahrens zur Massenvolltextdigitalisierung der im deutschen Sprachraum erschienenen Drucke des 16. bis 19. Jahrhunderts. In der aktuellen dritten Förder­phase arbeitet die Universitäts­bibliothek Mannheim an einem Workflow für das werk­spezifische Nachtraining mit Hilfe von generischen Modellen.

## Herausforderungen der Texterkennung

Bei der modernen Volltexterkennung bilden häufig mühsam händisch oder halb-automatisiert erfasste Trainingsdaten (Ground Truth) die Grundlage für die Texterkennung mittels künstlicher neuronaler Netze. Dies führt dazu, dass auch die durch die Transkription entstandenen Fehler von den neuronalen Netzen mittrainiert werden. Zudem basieren die vorhandenen Modelle oft auf einzelnen Sprachen oder Schriftarten, die die tatsächlichen Werke nicht vollständig abdecken können. Das Resultat sind fehlerhafte Modelle mit mangelhafter Genauigkeitsquote.

## Lösung durch generische Modelle

Mit Hilfe generischer Modelle, die bereits mit unterschiedlichen Sprachen und Schriften trainiert sind, lässt sich diese Problematik umgehen. Durch das Nachtraining (Finetuning) eines generischen Modells kann die Genauigkeit für ein spezifisches Werk auf über 98 Prozent gesteigert werden. Auch spezielle Zeichen und Symbole lassen sich durch ein werk­spezifisches Nachtraining besser erfassen.

## Ziel des Projektes

Das Ziel des Projektes ist es, dass Einrichtungen unterschiedlicher Größe möglichst einfach die Module des OCR-D-Workflows nachtrainieren können, um bessere Erkennungs­raten für spezifische Werke zu erreichen. Die Anwender sollen durch softwaretechnische Werkzeuge Anleitungen erhalten und durch Best-Practice-Empfehlungen unterstützt werden. Zudem wird ein zentrales und öffentliches Modellrepositorium erstellt, um die Auffindbarkeit der Modelle zu gewährleisten.

Für weitere Informationen besuchen Sie die [Projektseite der DFG](https://gepris.dfg.de/gepris/projekt/460547474?context=projekt&task=showDetail&id=460547474&).