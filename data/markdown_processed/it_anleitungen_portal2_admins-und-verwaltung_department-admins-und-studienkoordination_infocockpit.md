---
title: InfoCockpit – Konfiguration und Nutzung des Studierendenportals an der Universität Mannheim
source_url_de: https://www.uni-mannheim.de/
source_url_en: https://www.uni-mannheim.de/en/
category: Benutzung
tags: ['InfoCockpit', 'Portal²', 'Studierende', 'Konfiguration', 'Studieninformationen', 'Erstsemester', 'Studienmanagement']
language: de
---

# InfoCockpit: Leitfaden zur Verwaltung von Studieninformationen

Das InfoCockpit ist das zentrale Werkzeug zur zielgruppenspezifischen Bereitstellung von Informationen auf der Startseite des Portal² für Studierende und Bewerber. Es ermöglicht die Pflege von Inhalten durch die Zulassungsstelle, Studienbüros, das Studiengangsmanagement und das Akademische Auslandsamt.

## 📞 Kontakt bei Fragen oder Problemen

Für Fragen oder technische Probleme mit dem InfoCockpit wenden Sie sich bitte an:

**Alexandra Theobalt**
*Leitung Koordinationsstelle Studieninformationen*

- **Adresse:** Universität Mannheim, Dezernat II – Studienangelegenheiten, L 1, 1 – Raum 115, 68161 Mannheim
- **Telefon:** +49 621 181-3157
- **E-Mail:** [alexandra.theobalt@uni-mannheim.de](mailto:alexandra.theobalt@uni-mannheim.de)
- **Web:** [Informationen zur Studienwahl](/studium/vor-dem-studium/)

## 📚 1. Hintergrund und Überblick

Die Startseite des Portal² dient der zielgruppenspezifischen Information (z. B. Erstsemester oder spezifische Studiengangskohorten). Die angezeigten Inhalte können Themen wie Orientierung an der Universität, aktuelle Hinweise, Veranstaltungen, Prüfungen und Fristen umfassen.

Das InfoCockpit dient dazu, folgende Aspekte zu steuern:

- Überblick über die verschiedenen Gestaltungselemente.
- Anleitung zum Anlegen und Bearbeiten der Inhalte.
- Tipps zur Nutzung des InfoCockpits.

## 🖥️ 2. Überblick über die Gestaltungselemente

Die Art der angezeigten Informationen variiert je nach Zielgruppe (Erstsemester vs. Studierende).

### 2.1. Informationen für Erstsemester

Für Erstsemester können vier verschiedene Arten von Informationen angezeigt werden:

- **Obere Kachel:** Wird für studiengangsspezifische Informationen genutzt (Titel, Text, Verlinkung).
- **Mittlere Kachel (Teaser Box TYPO3):** Wird für Einführungsveranstaltungen und wichtige ToDos genutzt.
- **Untere Kachel (Teaser Box TYPO3):** Wird für allgemeine Informationen genutzt.
- **Verlinkung in der rechten Spalte:** Wird für allgemeine und studiengangsspezifische Informationen genutzt (Titel, Text, Verlinkung).

### 2.2. Informationen für Studierende

Für Studierende werden aktuell drei Hauptmöglichkeiten genutzt, wobei weitere Optionen verfügbar sind:

- **News-Kachel:** Wird zentral für alle gepflegt und ist nicht differenzierbar.
- **Untere Kachel (Teaser Box TYPO3):** Wird für allgemeine Informationen genutzt.
- **Verlinkung in der rechten Spalte:** Wird für allgemeine und studiengangsspezifische Informationen genutzt.
- **Optionale Elemente:**
  - Obere Kachel (Titel, Text, Verlinkung): Für studiengangsspezifische Informationen.
  - Mittlere Kachel (Teaser Box TYPO3): Für allgemeine Informationen.

### 2.3. Differenzierungsmöglichkeiten

Die angezeigten Informationen (mit Ausnahme der News-Kachel) können anhand folgender Kriterien unterschieden und zielgruppenspezifisch angezeigt werden:

- Bewerber/Studierender
- Abschluss (Bachelor/Master)
- Studienfach
- Bildungsinländer/-ausländer
- Fachsemester

### 2.4. Darstellung der Inhalte

Die Inhalte werden in TYPO3 angelegt und können auf zwei Arten im Portal angezeigt werden:

- Inhalte der TYPO3-Seite im Portal anzeigen.
- Komplette TYPO3-Seite in neuem Fenster öffnen.

## ⚙️ 3. Konfiguration des InfoCockpits

Die Konfiguration erfolgt im Portal² über den Menüpunkt: **Administration –> InfoCockpit –> Konfigurieren**.

### 3.1. Inhaltselemente anlegen oder suchen

Es besteht die Möglichkeit, einen neuen Eintrag anzulegen oder einen vorhandenen Eintrag zu suchen und zu bearbeiten.

**Wichtige Parameter bei der Erstellung:**

| Parameter | Beschreibung | Auswahlmöglichkeiten | Hinweise |
| :--- | :--- | :--- | :--- |
| **Abschluss und Studienfach**\* | Definiert, für welchen Studiengang das Element sichtbar ist. | Kombination von Abschluss und Studienfach. | Mehrfachauswahl möglich. Der Eintrag „(nur studiengangsunabhängige Informationen anzeigen)“ darf nicht gleichzeitig mit anderen Kombinationen ausgewählt werden. |
| **Fakultät** | Definition des Corporate Design für das Inhaltselement. | Auswahl über Dropdown Menü. | |
| **Rolle**\* | Definiert die Zielgruppe: Bewerber*in, Student*in (vorläufig), Student*in oder eine ausgewählte Kombination. | Auswahl über Anklicken der Kästchen. | Nach der Immatrikulation erhalten Studierende die normale „Student*in“-Rolle. |
| **Semester** | Nur für die Rolle Student*in: Definiert das Fachsemester. | Eintragen der Ganzzahl (z. B. 2,4,6). | Unterstützte Ganzzahlen liegen im Intervall 1..99. |
| **Hochschulzugangs-berechtigung*** | Definiert die Berechtigung: nicht EU-Ausländer/in ohne dt. HZB (A), Ausländer/in mit dt. HZB (B), dt. Staatsbürger/in (D), EU-Ausländer/in ohne dt. HZB (E) oder Keine Angabe (–). | Auswahl über Anklicken der Kästchen. | |
| **Gültigkeit**\* | Definiert den Zeitraum, in dem das Element angezeigt werden soll. | Auswahl über Kalender. | |
| **Art des Inhaltselements und Anzeigemodus**\* | Definiert das Layout und die Platzierung: Link rechte Spalte, Obere Kachel, Mittlere Kachel, Untere Kachel oder Super-Kachel (News). | Auswahl über Dropdown Menü. | Kombination aus Art und Anzeigemodus. |
| **Priorität** | Definiert die Reihenfolge der Elemente. | Eintragen als Zahl. | Je höher die Zahl, desto weiter vorne wird das Element angezeigt. |
| **URL für die Verlinkung des Inhaltselementes**\* | Definiert den Inhalt, der verlinkt werden soll. | Angabe einer (TYPO3-)URL. | |
| **URL für die Verlinkung des Inhaltselementes EN**\* | Definiert die englische Übersetzung des verlinkten Inhalts. | Angabe einer (TYPO3-)URL. | Falls keine Übersetzung vorhanden ist, muss die deutsche URL erneut eingegeben werden. |
| **URL für den Teaser des Inhaltselementes** | Nur für „mittlere Kachel“ und „untere Kachel“: Definiert die Teaserbox. | Angabe der TYPO3-URL. | |
| **Titel/Text des Inhaltselementes** | Für „obere Kachel“ und „Link rechte Spalte“: Definition des Titels und des Textes. | Freie Eingabe. | Der Text sollte kurz und ohne Formatierung erfolgen. |

**Technische Hinweise zur URL-Eingabe:**

- **Standard-URL:** `https://www.uni-mannheim.de/index.php?+`
- **Typo3 ID-Inhalt:** `id=15913`
- **Sprache Deutsch:** `&L=0`
- **Sprache Englisch:** `&L=1`
- **Nur Seiteninhalt:** `&type=105`
- *Beispiel:* `https://www.uni-mannheim.de/index.php?id=15913&L=0&type=105`

### 3.2. Suchen von Inhaltselementen

Über die Suchmaske können die verschiedenen Parameter definiert werden (z. B. alle Inhaltselemente der Philosophischen Fakultät). Die Ergebnisse werden tabellarisch angezeigt und können dort ausgewählt und bearbeitet werden.

### 3.3. Tipps im Umgang mit der Konfigurationsmaske

- **Schlüsselwörter:** Die Vergabe von Schlüsselwörtern hilft bei der Suche nach bestehenden Links.
- **Ergebnistabelle anpassen:** Die Ergebnistabelle kann personalisiert werden, um relevante Informationen schneller zu finden.
- **Standardabfragen:** Häufige Suchanfragen können als Standardabfrage gespeichert werden.
- **PDF vs. TYPO3:** Für Inhalte wie Begrüßungsschreiben kann statt eines PDFs auch eine TYPO3-Seite angelegt werden, die im Portal angezeigt wird.

## 🔍 4. Vorschau und Statistik

### 4.1. Vorschau der Inhalte

Die Inhalte können über den Menüpunkt **Administration –> InfoCockpit –> Vorschau** eingesehen werden. Hier können verschiedene Parameter (Abschluss, Studienfach, Rolle, HZB, Fachsemester, Gültigkeit) definiert werden. Alternativ kann die Matrikelnummer oder Uni-ID (Kennung) eines Studierenden oder Bewerbenden eingegeben werden.

### 4.2. Download der Statistik

Der Download der InfoCockpit-Statistik erfolgt über **Administration –> InfoCockpit –> Download Statistik**. Die betroffenen Gruppen sind Bewerber\*innen und Studierende.

**Erläuterung der Statistik-Tabelle:**

- **Datum:** Bezeichnet den Tag der statistischen Erfassung.
- **Abschluss/Studienfach:** Bezeichnet den Abschluss bzw. das Studienfach des Benutzers.
- **Rolle:** 65 = Bewerber*in; 6 = Student*in (vorläufig); 5 = Student\*in.
- **Fachsemester:** Wird nur bei Studierenden geprüft. Bei Bewerbern wird immer NULL gespeichert.
- **HZB:** Bezeichnet die Hochschulzugangsberechtigung (A, B, D, E).
- **Aufgerufener Inhalt:** `home` bezieht sich auf die InfoCockpit-Startseite. Eine Zahl bezieht sich auf die ID des geöffneten InfoCockpit-Inhaltselementes.
- **Aufrufhäufigkeit:** Bezeichnet, wie oft der entsprechende Inhalt aufgerufen wurde.
