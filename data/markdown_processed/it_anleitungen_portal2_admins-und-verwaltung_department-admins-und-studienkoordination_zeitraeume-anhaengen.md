---
title: Verwaltung von Belegungs- und Verteilungsverfahren im Portal²
source_url_de: (Keine spezifische deutsche URL im Dokument)
source_url_en: https://www.uni-mannheim.de/en/
category: Benutzung
tags: ['Belegungsverfahren', 'Verteilungsverfahren', 'Portal²', 'Zeiträume', 'Studienkoordination', 'Anmeldung', 'Kurszuweisung']
language: de
---

# Belegungs- und Verteilungsverfahren im Portal²

Dieses Dokument beschreibt die notwendigen Schritte und Verfahren zur Einrichtung von Belegungs- und Verteilungsverfahren für Veranstaltungen im Portal².

**Hinweis:** Eine allgemeine Erklärung zu Belegungen und zu den Einstellungen, die nötig sind, um Belegungen durch Studierende zu ermöglichen, finden Sie [in unserer Dokumentation zur Veranstaltungsbelegung](https://www.uni-mannheim.de/it/anleitungen/portal2/lehrende/veranstaltungsbelegung/).

## 1. Grundlagen der Belegungsplanung

Um die Veranstaltungsbelegung möglich zu machen, müssen zu jeder Veranstaltung Zeiträume zugeordnet werden. Diese Zeiträume definieren, wer und wann an einer Veranstaltung teilnehmen kann.

- **Belegungsverfahren:** Definiert, wie sich die Studierenden für die Veranstaltungen anmelden können.
- **Verteilungsverfahren:** Bestimmt, wie die Studierenden den Kursen zugeordnet werden.

### Zeitraumarten

Die korrekte Zuordnung von Zeiträumen ist essenziell, um klarzustellen, wie die Belegungen ablaufen sollen.

## 2. Belegungsverfahren (Anmeldung)

Die Belegungsverfahren bestimmen die Art und Weise der Studierendenanmeldung.

### Überblick der Verfahren

| Verfahren | Beschreibung | Anwendungsfall |
| :--- | :--- | :--- |
| **Gruppenpriorität** | Studierende ordnen Alternativen in einer Rangreihenfolge. Nach diesen Prioritäten erfolgt die Zuteilung. | Geeignet, wenn eine Veranstaltung aus mehreren inhaltlich gleichen Parallelgruppen besteht. |
| **Modulpriorität** | Studierende vergeben Alternativen auf Modulebene für Veranstaltungen, deren Inhalte sich voneinander unterscheiden. | Wird beispielsweise bei Hauptseminaren der Politikwissenschaft verwendet. |
| **Echtzeitbelegung** | Für Vorlesungen mit ausreichend Kapazitäten. Anmeldungen werden direkt zugelassen, da keine Auswahl der Studierenden notwendig ist. | Direkte Zulassung. |
| **Echtzeitbelegung mit Verteilung** | Alle angemeldeten Studierenden werden nach der Belegung mittels Losverfahren zugelassen. | Bei Bedarf wenden Sie sich an den zuständigen Studiengangsmanager oder das Portal-Team. |

### Detaillierte Verfahrensübersicht

| Bezeichnung | Eigenschaften | Auswirkungen |
| :--- | :--- | :--- |
| **Echtzeitbelegung ZU** | Belegung und automatische Zulassung. Studierende sind zugelassen (ZU). | Keine Teilnehmerbegrenzung. |
| **Echtzeitbelegung ZU FCFS** | Belegung und automatische Zulassung bis zu einer maximalen Teilnehmerzahl (TN). Studierende sind zugelassen (ZU). | First-come-first-serve! |
| **Echtzeitbelegung AN** | Belegung. Studierende sind angemeldet (AN). | Ein Verteilungsverfahren muss durchgeführt werden. |
| **Echtzeitbelegung Stg. ZU/AN** | Belegung und automatische Zulassung für Studierende mit dieser Veranstaltung in PO. Diese TN sind ZU, alle anderen TN sind AN. | Ein Verteilungsverfahren muss durchgeführt werden. |
| **Gruppenpriorität ALLE** | Verpflichtende Priorisierung aller Parallelgruppen. Prioritäten sind vorbelegt. TN sind AN. | Ein Verteilungsverfahren ist notwendig. |
| **Gruppenpriorität mit 2 Alternativen (= 3 Prioritäten)** | Eine Gruppe bevorzugt (Prio 1). Alternativen dürfen mehrfach vergeben werden (Prio 2/3). | Ein Verteilungsverfahren ist notwendig; psychologischer Effekt. |
| **Modulpriorität ALLE** | Verpflichtende Priorisierung aller Veranstaltungen. Prioritäten sind vorbelegt. TN sind AN. | Ein Verteilungsverfahren ist notwendig. |
| **Modulpriorität mit 2 Alternativen (= 3 Prioritäten)** | Eine Veranstaltung bevorzugt (Prio 1). Alternativen dürfen mehrfach vergeben werden (Prio 2/3). | Ein Verteilungsverfahren ist notwendig; psychologischer Effekt. |

## 3. Verteilungsverfahren (Zuteilung)

Die Verteilungsverfahren bestimmen die Methode der finalen Zuteilung der Studierenden.

### Verteilungsverfahren für Echtzeit- und Gruppenpriorität

| Bezeichnung | Eigenschaften |
| :--- | :--- |
| **Losverfahren** | Vergabe von Losnummern. Zufällige Verteilung nach Losnummer. |
| **Sortiertes Verfahren** | Sortierung nach: Studiengang (Studiengänge der Veranstaltung zuerst) und Fachsemester (hohe Semester zuerst). Vergabe von Losnummern. |
| **Sortiertes Verfahren mit Konfliktknüpfung** | Zusätzliche Überprüfung auf Konflikte mit anderer Zulassung. Falls ein Konflikt besteht, erfolgt die Auswertung der nächsten abgegebenen Priorität. |
| **Rücknahme der Verteilung** | (Keine Details angegeben) |

### Verteilungsverfahren für Modulpriorität

| Bezeichnung | Eigenschaften |
| :--- | :--- |
| **Modulverteilung** | Vergabe von Losnummern. Zufällige Verteilung nach Modulprioritäten. |
| **Modulverteilung mit Sortierung** | Sortierung nach Studiengang und Fachsemester. Vergabe von Losnummern. |
| **Rücknahme der Verteilung** | (Keine Details angegeben) |

## 4. Administration und Zuordnung von Zeiträumen

### Zeitraum zuordnen

Um eine Belegung zu ermöglichen, muss jeder im Portal² belegbare Veranstaltung mindestens einen Belegungszeitraum zugeordnet bekommen.

**Vorgehen:**

1. Öffnen Sie die Bearbeitungsansicht der Veranstaltung (z. B. mit der Rolle „Department-Admin“).
1. Unter dem Reiter „Zeiträume“ werden alle Zeitraumgruppen angezeigt, die dieser Veranstaltung angehängt wurden.
1. **Wichtig:** Zeitraumgruppen müssen nur einmalig verknüpft werden, da sie semesterunabhängig an der Veranstaltung hängen. Die spezifischen Laufzeiten müssen anschließend vom Studiengangsmanagement beim Portal² Team angefordert werden.
1. Um eine (andere) Zeitraumgruppe zu verknüpfen, klicken Sie auf „Zeitraumgruppe zuordnen“. Setzen oder entfernen Sie dort einen Haken bei der gewünschten Zeitraumgruppe und beenden Sie die Bearbeitung mit Klick auf „Zuordnungen aktualisieren“.

**Achtung:** Es dürfen sich mehrere Belegungsverfahren für dieselbe Rolle (meist Student\*in) nicht zeitlich überschneiden. Dies verhindert, dass das System eindeutig feststellen kann, welches Belegungsverfahren anzuwenden ist, und verbietet die Belegung.

### Zuordnen und Löschen

Sollte kein passender Zeitraum in der Liste zu finden sein, wenden Sie sich bitte mit folgendem ausgefüllten Formular ans Portal-Team: [Download Formular (DOCX)](https://portal2.uni-mannheim.de/portal2/download/help/Formular_Zeitraumgruppe.docx).

## 5. Wichtige Hinweise für einen reibungslosen Ablauf

Um einen möglichst reibungslosen Ablauf der Belegung und Verteilung zu gewährleisten, beachten Sie bitte folgende Zeitrahmen:

- Die Konfiguration der Veranstaltungsbelegung (inkl. Zeitraum, Belegverfahren, Zuordnungen) sollte **mindestens 1 Woche** vor Beginn der Belegung durch die Studierenden erfolgen.
- Es sollten **3 Werktage** zwischen dem Ende der Belegungsphase und der Bekanntgabe der Verteilung eingeplant werden.
- Es sollten **2 Werktage** zwischen der Bekanntgabe der Verteilung und dem Start der Veranstaltung eingeplant werden.

### Änderungen, die während der Belegungsphase NICHT vorgenommen werden dürfen:

- Hinzufügen oder Löschen von Parallelgruppen.
- „Fällt aus“-Setzen von Parallelgruppen.
- Hinzufügen oder Löschen von Veranstaltungen in zu belegenden Modulen bei „Belegung mit Modulpriorität“.
- Hinzufügen oder Löschen von (Teil-)Modulen im Prüfungsordnungsbaum.
- Bearbeiten von Regeln an Modulen.
- Ändern der Zeitraumgruppen der zu belegenden Veranstaltungen.
- Manuelle Platzvergabe (Zulassung, Änderung) einzelner Studierender.

Weitere Erklärungen zur Platzvergabe finden Sie in unseren [Anleitungen zur Verteilung und Platzvergabe](https://www.uni-mannheim.de/it/anleitungen/portal2/admins-und-verwaltung/department-admins-und-studienkoordination/verteilung-und-platzvergabe-fuer-veranstaltungen/).
