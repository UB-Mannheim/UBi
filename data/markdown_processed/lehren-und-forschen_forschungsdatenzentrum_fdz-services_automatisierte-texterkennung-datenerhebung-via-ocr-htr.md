---
title: Automatisierte Texterkennung – Datenerhebung via OCR/HTR
source_url: https://www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum/fdz-services/automatisierte-texterkennung-datenerhebung-via-ocr-htr/
category: Services
tags: [OCR, HTR, Texterkennung, Digitalisierung, Forschungsdatenzentrum, Universitätsbibliothek Mannheim, Transkription, Ground-Truth, Open Source, Texterkennungssoftware]
language: de
---

# Automatisierte Texterkennung – Datenerhebung via OCR/HTR

Mithilfe von maschineller Texterkennung (OCR) werden Texte aus digitalen Bildern automatisiert erfasst und so durchsuchbare und analysierbare Daten erzeugt. Die [Universitätsbibliothek Mannheim](https://www.bib.uni-mannheim.de) verfügt über langjährige Erfahrung in der Digitalisierung und der Anwendung verschiedener Texterkennungssoftware. Das Forschungsdatenzentrum unterstützt Forschende der Universität Mannheim entlang des gesamten Workflows – von der Digitalisierung über Layout- und Texterkennung, dem Nachtraining spezialisierter Modelle bis hin zur Datenstrukturierung.

## Services

- Beratung zur maschinellen Texterhebung für Forschungsprojekte
- [OCR Recommender](https://www.berd-nfdi.de/limesurvey/index.php/996387?lang=de)
- Offene OCR-Sprechstunde: jeden 2. Donnerstag im Monat, 15–16 Uhr, ohne Anmeldung  
  [Zoom-Meeting](https://ocr-bw.bib.uni-mannheim.de/sprechstunde)  
  Meeting ID: 682 8185 1819, Kenncode: 443071

## Auswahl an Texterkennungs- und Transkriptionsplattformen

| Tool           | Kostenmodell             | Eigenschaften                                                                 | Besonders geeignet für                                      |
|----------------|-------------------------|-------------------------------------------------------------------------------|------------------------------------------------------------|
| ABBYY Finereader | kostenpflichtig/kommerziell | Text- und Layouterkennung; gute Layoutanalyse                                | Moderne Drucke, komplexes Layout                            |
| eScriptorium   | Open Source             | Grafische Benutzeroberfläche für Kraken; intuitive Nutzung                    | Historische Drucke und Handschriften, auch nicht-lateinische Schrift |
| Google Vision  | kostenpflichtig/kommerziell | Texterkennung; Bild- und Videoanalyse; für Handschriften und Drucke          | Drucke und Handschriften                                    |
| Kraken         | Open Source             | Kommandozeilenbasierte Texterkennungssoftware; optimiert für historisches und nicht-lateinisches Schriftmaterial | Historische Drucke und Handschriften, auch nicht-lateinische Schrift |
| OCR4All        | Open Source             | Grafische Benutzeroberfläche für verschiedene Open Source Texterkennungsprogramme | Historische Drucke und Handschriften                        |
| OCRmyPDF       | Open Source             | Kommandozeilenprogramm zur Texterkennung von PDF-Dateien; nutzt Tesseract als OCR-Engine | Historische/moderne Drucke                                  |
| OCR-D          | Open Source             | Modular aufgebaute, kommandozeilenbasierte Texterkennungssoftware             | Historische Drucke                                         |
| PERO-OCR       | Open Source             | Webbasierte Texterkennungsplattform; gute Universalmodelle; momentan kein Nachtraining möglich | Historische/moderne Drucke und Handschriften               |
| Tesseract      | Open Source             | Kommandozeilenbasierte Texterkennungssoftware; geeignet für umfangreiche Datensätze | Historische/moderne Drucke                                  |
| Transkribus    | kostenpflichtig/kommerziell | Umfangreiche Texterkennungs- und Transkriptionsplattform; mit intuitiver Benutzeroberfläche | Historische Handschriften und Tabellen                      |

## Anleitungen und Materialien zu OCR-Software

### eScriptorium

- [Alle Github-Dokumentationen der UB Mannheim zu eScriptorium](https://ub-mannheim.github.io/eScriptorium_Dokumentation/)
- [Lokale Installation (Windows/Linux)](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Lokale_Installation_eScriptorium.html)
- [Lokale Installation (MacOS)](https://github.com/UB-Mannheim/escriptorium/wiki/Installation-on-MacOS) (Englisch)
- [Nutzungsanleitungen Deutsch](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Nutzungsanleitung_eScriptorium.html) und [Englisch](https://escriptorium-tutorial.readthedocs.io/en/latest/)
- [Video: Einführung in eScriptorium](https://www.youtube.com/watch?v=aQuwh3OaKqg)
- [Modellübertragung von Transkribus nach eScriptorium](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Modell%C3%BCbertragung_Transkribus_nach_eScriptorium.html)

### OCR-D

- [Nutzungs- und Installationsanleitung](https://ocr-d.de/de/use)

### OCRmyPDF

- [Installations- und Nutzungsanleitung (Windows/Linux)](https://ub-mannheim.github.io/Tesseract_Dokumentation/OCRmyPDF_Windows_und_Linux.html)

### Tesseract

- [Alle Github-Dokumentationen der UB Mannheim zu Tesseract](https://ub-mannheim.github.io/Tesseract_Dokumentation/)
- [Installations- und Nutzungsanleitung Linux](https://ub-mannheim.github.io/Tesseract_Dokumentation/Tesseract_Doku_Linux.html) und [Windows](https://ub-mannheim.github.io/Tesseract_Dokumentation/Tesseract_Doku_Windows.html)
- [Anleitung zum Training mit Tesseract und Tesstrain](https://github.com/th-schmidt/training-with-tesseract)

## Hinweise zur Erstellung von Ground-Truth (Trainingsdaten)

Im Rahmen des Projekts OCR-D wurden drei Transkriptionsstufen für historische Dokumente definiert, die sich im Grad der originalgetreuen Wiedergabe unterscheiden. Die Richtlinien sind auf der [OCR-D Projekthomepage](https://ocr-d.de/de/gt-guidelines/trans/index.html) verfügbar. Eine Leitlinie zur Veröffentlichung eigener Trainingsdaten finden Sie auf [Github](https://github.com/OCR-D/gt-repo-template).

Hilfreiche Ressourcen für Ground-Truth-Daten:

- [OCR & Ground-Truth-Resources](https://github.com/cneud/ocr-gt)
- [HTR United](https://htr-united.github.io/)
- [Ground-Truth für Charlottenburger Amtsschrifttum](https://github.com/UB-Mannheim/charlottenburger-amtsschrifttum)
- [Ground-Truth für Digitalisate der UB Mannheim](https://github.com/UB-Mannheim/digi-gt)
- [Ground-Truth für Digitalisate der UB Tübingen](https://github.com/UB-Mannheim/digitue-gt)
- [IAM Database für Handschriften](https://fki.tic.heia-fr.ch/databases)

Für die Erstellung von Ground-Truth kann ein virtuelles Keyboard mit benötigten Sonderzeichen hilfreich sein. Virtuelle Keyboards für verschiedene Transkriptionsplattformen finden Sie auf [Github](https://github.com/tboenig/keyboardGT).

In den [FAQs](https://ocr-bw.bib.uni-mannheim.de/faq/) des Projekts OCR-BW finden Sie Antworten auf häufig gestellte Fragen zur automatisierten Texterkennung und den eingesetzten Softwarelösungen. Bei weiteren Fragen können Sie sich per E-Mail an das Team wenden.

## Projekte und Kooperationen

- Kooperationsprojekt zur Texterkennung und Datenstrukturierung mit dem [Lehrstuhl für Wirtschaftsgeschichte (Prof. Streb)](https://www.vwl.uni-mannheim.de/streb/)
- Kooperationsprojekt zur Handschriftenerkennung mit dem [Lehrstuhl für Spätmittelalter und Frühe Neuzeit (Prof. Kümper)](https://www.phil.uni-mannheim.de/spaetmittelalter-und-fruehe-neuzeit/)

## Kontakt

### Forschungsdatenzentrum (FDZ)

Team: Irene Schumm, Phil Kolbe, David Morgan, Thomas Schmidt, Renat Shigapov, Christos Sidiropoulos, Vasilka Stoilova, Larissa Will  
Adresse: Universität Mannheim, Universitätsbibliothek Mannheim, Schloss Schneckenhof West, 68161 Mannheim  
Web: [www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum](https://www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum/)  
E-Mail: forschungsdaten@uni-mannheim.de