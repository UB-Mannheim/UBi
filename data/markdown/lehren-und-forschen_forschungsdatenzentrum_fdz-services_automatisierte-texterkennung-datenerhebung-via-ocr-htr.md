<en_url>https://www.bib.uni-mannheim.de/en/teaching-and-research/research-data-center-fdz/services-of-the-fdz/automated-text-recognition-extracting-data-via-ocr-htr/</en_url>


# [Automatisierte Texterkennung – Datenerhebung via OCR/HTR](https://www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum/fdz-services/automatisierte-texterkennung-datenerhebung-via-ocr-htr/)

Mithilfe von maschineller Texterkennung (OCR) werden Texte aus digitalen Bildern automatisiert erfasst und auf diese Weise durchsuchbare und analysierbare Daten erzeugt. Die Universitätsbibliothek Mannheim blickt auf langjährige Erfahrung in der Digitalisierung und mit der Anwendung verschiedenerTexterkennungssoftware zurück.
Gerne unterstützt das Forschungsdatenzentrum Forschende der Universität Mannheim entlang des gesamten Workflows von der Digitalisierung über die Layout- und Texterkennung sowie dem Nachtraining spezialisierter Modelle bis hin zur Strukturierung der Daten.


## Services


- Beratung zur maschinellen Texterhebung für Forschungsprojekte
- [OCR Recommender](https://www.berd-nfdi.de/limesurvey/index.php/996387?lang=de)
- Offene OCR-Sprechstunde: jeden 2. Donnerstag im Monat, von 15 bis 16 Uhr, ohne Anmeldung (Link zum Zoom-Meeting: [https://ocr-bw.bib.uni-mannheim.de/sprechstunde](https://ocr-bw.bib.uni-mannheim.de/sprechstunde), Meeting ID: 682 8185 1819, Kenncode: 443071)



### Auswahl an Texterkennungs- und Transkriptionsplattformen

| Tool | Kostenmodell | Eigenschaften | Besonders geeignet für |
| --- | --- | --- | --- |
| ABBYY Finereader | kostenpflichtig/kommerziell | Text- und Layouterkennung; gute Layoutanalyse | Moderne Drucke, komplexes Layout |
| eScriptorium | Open Source | Graphische Benutzeroberfläche für Kraken; intuitive Nutzung | Historische Drucke und Handschriften, auch nicht-lateinische Schrift |
| Google Vision | kostenpflichtig/kommerziell | Texterkennung; Bild- und Videoanalyse; für Handschriften und Drucke | Drucke und Handschriften |
| Kraken | Open Source | kommandozeilenbasierte Texterkennungssoftware; optimiert für historisches und nicht-lateinisches Schriftmaterial | Historische Drucke und Handschriften, auch nicht-lateinische Schrift |
| OCR4All | Open Source | graphische Benutzeroberfläche für verschiedene Open Source Texterkennungsprogramme | Historische Drucke und Handschriften |
| OCRmyPDF | Open Source | Kommandozeilenprogramm zur Texterkennung von PDF-Dateien; nutzt Tesseract als OCR-Engine | Historische/moderne Drucke |
| OCR-D | Open Source | modular aufgebaute, kommandozeilenbasierte Texterkennungssoftware | Historische Drucke |
| PERO-OCR | Open Source | webbasierte Texterkennungsplattform; gute Universalmodelle; momentan kein Nachtraining möglich | Historische/moderne Drucke und Handschriften |
| Tesseract | Open Source | kommandozeilenbasierte Texterkennungssoftware; geeignet für umfangreiche Datensätze | Historische/moderne Drucke |
| Transkribus | kostenpflichtig/kommerziell | umfangreiche Texterkennungs- und Transkriptionsplattform; mit intuitiver Benutzeroberfläche | Historische Handschriften und Tabellen |



### Anleitungen und Materialien zu verschiedener OCR-Software

Hier finden Sie Anleitungen und Materialien zu verschiedenen Open-Source-Texterkennungsprogrammen und Transkriptionsplattformen. Es handelt sich um eine Sammlung nützlicher Referenzen, nicht alle Ressourcen wurden von der UB Mannheim selbst erstellt.


## eScriptorium


- [Alle Github-Dokumentationen der UB Mannheim zu eScriptorium](https://ub-mannheim.github.io/eScriptorium_Dokumentation/)
- [Lokale Installation (Windows/Linux)](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Lokale_Installation_eScriptorium.html)
- [Lokale Installation (MacOS)](https://github.com/UB-Mannheim/escriptorium/wiki/Installation-on-MacOS) (Englisch)
- Nutzungsanleitungen ([Deutsch](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Nutzungsanleitung_eScriptorium.html) und [Englisch](https://escriptorium-tutorial.readthedocs.io/en/latest/))
- [Video: Einführung in eScriptorium](https://www.youtube.com/watch?v=aQuwh3OaKqg)
- [Modellübertragung von Transkribus nach eScriptorium](https://ub-mannheim.github.io/eScriptorium_Dokumentation/Modell%C3%BCbertragung_Transkribus_nach_eScriptorium.html)



## OCR-D


- [Nutzungs- und Installationsanleitung](https://ocr-d.de/de/use)



## OCRmyPDF


- [Installations- und Nutzungsanleitung (Windows/Linux)](https://ub-mannheim.github.io/Tesseract_Dokumentation/OCRmyPDF_Windows_und_Linux.html)



## Tesseract


- [Alle Github-Dokumentationen der UB Mannheim zu Tesseract](https://ub-mannheim.github.io/Tesseract_Dokumentation/)
- Installations- und Nutzungsanleitung ([Linux](https://ub-mannheim.github.io/Tesseract_Dokumentation/Tesseract_Doku_Linux.html) und [Windows](https://ub-mannheim.github.io/Tesseract_Dokumentation/Tesseract_Doku_Windows.html))
- [Anleitung zum Training mit Tesseract und Tesstrain](https://github.com/th-schmidt/training-with-tesseract)



### Hinweise zur Erstellung von Ground-Truth (Trainingsdaten)

Im Rahmen des Projekts OCR-D wurden drei verschiedene Transkriptionsstufen für die Transkription historischer Dokumente in Transkriptionsrichtlinien festgelegt. Die Stufen unterscheiden sich im Grad der originalgetreuen Wiedergabe. Die Richtlinien sind auf der [OCR-D Projekthomepage](https://ocr-d.de/de/gt-guidelines/trans/index.html) zu finden. Zudem finden Sie auf Github auch eine [Leitlinie](https://github.com/OCR-D/gt-repo-template) zur Veröffentlichung Ihrer eigenen Trainingsdaten.
Hier finden Sie Ground-Truth zum Training bzw. Nachtraining eigener Modelle:

- [OCR & Ground-Truth-Resources](https://github.com/cneud/ocr-gt)
- [HTR United](https://htr-united.github.io/)
- [Ground-Truth für Charlottenburger Amtsschrifttum](https://github.com/UB-Mannheim/charlottenburger-amtsschrifttum)
- [Ground-Truth für Digitalisate der UB Mannheim](https://github.com/UB-Mannheim/digi-gt)
- [Ground-Truth für Digitalisate der UB Tübingen](https://github.com/UB-Mannheim/digitue-gt)
- [IAM Database für Handschriften](https://fki.tic.heia-fr.ch/databases)

Hilfreich bei der Erstellung von Ground-Truth kann auch ein virtuelles Keyboard mit den benötigten Sonderzeichen sein. Virtuelle Keyboards für unterschiedliche Transkriptionsplattformen  finden Sie ebenfalls auf [Github](https://github.com/tboenig/keyboardGT).
In unseren [FAQs](https://ocr-bw.bib.uni-mannheim.de/faq/) finden Sie Antworten auf die am häufigst gestellten Fragen rund um das Thema automatisierte Texterkennung sowie die im Projekt [OCR-BW](https://ocr-bw.bib.uni-mannheim.de/projektuebersicht/) genutzte Software.
Wenn die gesuchte Antwort nicht dabei ist, wenden Sie sich einfach per E-Mail an uns.


## Projekte und Kooperationen


- Kooperationsprojekt zur Texterkennung und Datenstrukturierung mit[ Lehrstuhl für Wirtschaftsgeschichte (Prof. Streb)](https://www.vwl.uni-mannheim.de/streb/)
- Kooperationsprojekt zur Handschriftenerkennung mit [Lehrstuhl für Spätmittelalter und Frühe Neuzeit (Prof. Kümper)](https://www.phil.uni-mannheim.de/spaetmittelalter-und-fruehe-neuzeit/)

Wenn wir Sie unterstützen können oder Sie Fragen haben, zögern Sie nicht uns zu kontaktieren.


## Kontakt



### Forschungsdatenzentrum (FDZ)

Team: Irene Schumm, Phil Kolbe, David Morgan, Thomas Schmidt, Renat Shigapov, Christos Sidiropoulos, Vasilka Stoilova, Larissa Will
- Adresse: Universität Mannheim, Universitätsbibliothek Mannheim, Schloss Schneckenhof West, 68161 Mannheim
- Web: [www.bib.uni-mannheim.de/lehren-und-forschen/forschungsdatenzentrum](/lehren-und-forschen/forschungsdatenzentrum/)
- E-Mail: forschungsdaten@uni-mannheim.de
