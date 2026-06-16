---
title: Verwaltung und Übertragung von Lehrdeputaten im Portal²
source_url_de: https://www.uni-mannheim.de/it/anleitungen/portal2/admins-und-verwaltung/department-admins-und-studienkoordination/lehrdeputate/
source_url_en: https://www.uni-mannheim.de/en/
category: Services
tags: ['Lehrdeputat', 'Portal²', 'Verwaltung', 'Credits', 'Semester', 'Dozenten', 'Soll', 'Ist']
language: de
---

# Lehrdeputatsverwaltung im Portal²

Die Lehrdeputatsverwaltung im Portal² ermöglicht die umfassende Verwaltung der Lehrleistungen (Lehrdeputate) einer Einrichtung. Die Module dienen der Überprüfung des Soll-Deputats (geplanter Umfang), der Erfassung des Ist-Deputats (tatsächlicher Umfang) und der Verwaltung der Überträge zwischen den Semestern.

## 🔍 Allgemeine Funktionen und Suchmaske

In allen Deputatsbereichen dient eine **Suchmaske** zur Eingrenzung der Verwaltung. Sie können nach verschiedenen Kriterien suchen, beispielsweise nach dem Namen einer bestimmten Person oder nach allen Lehrpersonen einer Einrichtung (Funktion = Lehrperson).

Nach dem Klick auf "Suchen" werden die gefundenen Personen tabellarisch aufgelistet und die relevanten Informationen für das aktuelle Semester angezeigt. Nutzer können zudem das **Semester wechseln**, um Überträge aus Vorsemestern zu bearbeiten.

## 📊 1. Deputate meiner Einrichtung (Übersicht)

Dieser Bereich bietet einen Überblick über das Lehrdeputats-Soll, die geleisteten Ist-Stunden und eventuelle Minderungen der Lehrpersonen der Einrichtung.

**Verfügbare Informationen:**

- Lehrdeputats-Soll
- Übertrag aus dem Vorsemester
- Summe der Minderungen
- Summe der angerechneten SWS
- Übertrag in das Folgesemester

**Aktionsmöglichkeiten:**

- **Lehrdeputatserklärung für Einrichtung erzeugen:** Erstellt eine Excel-Datei mit den Lehrdeputatserklärungen für alle gefundenen Personen.
- **Alle Überträge in das Folgesemester übernehmen:** Überträgt alle eingetragenen Überträge in das Folgesemester.
- **Übertrag für eine bestimmte Person übernehmen:** Überträgt den Wert für eine einzelne Person in das Folgesemester.
- **Lehrdeputatsübersicht für eine bestimmte Person anzeigen:** Öffnet die Detailansicht, welche alle Veranstaltungen und Minderungen der Person listet. Hier kann auch eine individuelle Lehrdeputatserklärung erstellt werden.

## 📝 2. Soll-Deputate tabellarisch bearbeiten (Planung)

Über diese Maske wird das **geplante** Lehrdeputat (Soll-Deputat) der Lehrpersonen verwaltet.

**Verfügbare Informationen:**

- Übertrag aus dem Vorsemester
- Lehrdeputats-Soll
- Optionaler Vermerk
- Eventuelle Minderungen

**Bearbeitungsfunktionen:**

- **Übertrag anpassen:** Der Wert wird automatisch aus dem vorherigen Semester übernommen, kann aber manuell angepasst werden.
- **Soll-Stunden eintragen:** Festlegung des geplanten Stundenumfangs.
- **Vermerk verfassen:** Hinzufügen von Notizen.
- **Minderungen verwalten:**
  - *Hinzufügen:* Ermöglicht die Angabe des Minderungsgrunds, der geminderten SWS und eines optionalen Vermerks.
  - *Entfernen:* Löscht einen bestehenden Minderungs-Eintrag.

## 🗓️ 3. Ist-Deputate tabellarisch bearbeiten (Erfassung)

Dieser Bereich dient der Verwaltung und Erfassung der **tatsächlich geleisteten** Lehrdeputate (Ist-Deputat), die bei einzelnen Veranstaltungen hinterlegt werden.

**Verfügbare Informationen:**

- Liste der bearbeitbaren Veranstaltungen.
- Die SWS einer Veranstaltung werden genutzt, um Vorschlagswerte für die Ist-Stunden zu berechnen.

**Rollen und Berechnung der Ist-Stunden:**
Ist-Deputate können sowohl an **verantwortliche** als auch an **durchführende** Lehrpersonen vergeben werden.

- **Durchführende Lehrperson:** Wird in der Übersicht kursiv dargestellt. Dahinter ist die Anzahl der durchgeführten Einzeltermine in Klammern vermerkt.
- **Verantwortliche Lehrperson:** Wird in normaler Schriftart dargestellt.

**Berechnungslogik der SWS:**

1. **Nur eine verantwortliche Lehrperson:** Die gesamten SWS werden komplett angerechnet.
1. **Mehrere verantwortliche Lehrpersonen:** Die SWS werden gleichmäßig auf diese Personen aufgeteilt.
1. **Durchführende Lehrpersonen:** Die SWS werden entsprechend der durchgeführten Einzeltermine aufgeteilt. Eventuelle verantwortliche Lehrpersonen werden in diesem Fall nicht angerechnet.

**Aktionsmöglichkeiten:**

- **Vorschlagswert übernehmen:** Der automatisch berechnete Wert wird einer Lehrperson angerechnet. Alternativ kann ein abweichender Wert manuell eingetragen werden.
- **Detailansicht/Bearbeitung:** Über die Symbole in der Spalte "Aktion" gelangt man zur Detailansicht oder zur Bearbeitungsmaske der jeweiligen Veranstaltung.
