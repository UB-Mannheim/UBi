---
title: Raumverwaltung und Raumanfragen in Portal2 für Raum-Manager*innen
source_url_de: https://www.uni-mannheim.de/it/anleitungen/portal2/admins-und-verwaltung/raumverwaltung/
source_url_en: https://www.uni-mannheim.de/en/
category: Services
tags: ['Raumverwaltung', 'Raumanfragen', 'Portal2', 'Buchung', 'Konflikte', 'Department-Admin', 'Raumzuweisung']
language: de
---

# Leitfaden für Raum-Manager\*innen: Verwaltung von Raumanfragen in Portal2

Als Raum-Manager\*in sind Sie für die Verwaltung einer oder mehrerer Gruppen von Räumen zuständig. Wenn ein Dozent oder Sekretariat eine Nutzung dieser Räume anfragt, werden Sie benachrichtigt. Die Benachrichtigung erfolgt zunächst per E-Mail. Danach erhalten Sie keine weiteren E-Mails vom System, bis Sie sich im Portal2 eingeloggt haben. Erst danach werden Sie bei neuen Meldungen erneut per E-Mail benachrichtigt.

## 1. Wege zur Raumverwaltung

Es gibt drei Wege, um die Raumanfragen zu bearbeiten:

- **Startseite (Empfohlen):** Auf der Startseite von Portal² werden neue Raumanfragen für die verwalteten Räume als Portalnachricht angezeigt. Ein Klick auf die Nachricht (rechts oben) leitet Sie zur Maske für die Raumverwaltung. Die Nachrichten bleiben erhalten, bis sie manuell gelöscht werden.
- **Über Menüpfad:** Alternativ erreichen Sie die Bearbeitung über den Pfad: `Organisation` > `Räume und Gebäude` > `Raumanfragemanagement` > `Raumanfragen verwalten`.
- **Über Menü-Suche:** Sie können auch direkt in der Menü-Suche nach „Raumanfragen verwalten“ suchen.

## 2. Konfiguration der Filtermaske

Unabhängig vom gewählten Zugang gelangen Sie zur Übersichtsseite der Raumverwaltung. Im oberen Bereich finden Sie die Konfigurationseinstellungen, mit denen Sie die angezeigten Raumanfragen filtern, gruppieren und sortieren können.

### 2.1. Grundlegende Filterkriterien

Sie können die Anzeige filtern, indem Sie folgende Kriterien wählen:

- Semester
- Startdatum
- Enddatum
- Rhythmus
- Wochentag

### 2.2. Gruppierung und Sortierung

Die angezeigten Raumanfragen können wie folgt gruppiert werden:

- **Veranstaltung/Prüfung:** Die Anfragen werden nach der jeweiligen Veranstaltung oder Prüfung gruppiert.
- **Raum:** Die Anfragen werden nach dem angefragten Raum gruppiert.
- **Ohne:** Alle Anfragen werden einzeln ohne Gruppierung angezeigt.

Darüber hinaus können Sie die Sortierung und Reihenfolge definieren (u. a.):

- Älteste Raumanfrage zuerst
- Anfragesteller\*in
- Angefragter Raum
- Beste Raumauslastung zuerst
- Neuste Raumanfrage zuerst
- Veranstaltungs-/Prüfungstitel

### 2.3. Erweiterte Filterkriterien (Filterkriterien Bearbeiten)

Für eine präzisere Suche können Sie zusätzliche Filterkriterien anwenden:

**A. Status- und Konfliktbezogene Filter:**

- **Anfragestatus:** Offen, zurückgestellt, erfüllt, erfüllt durch alternativen Raum, abgelehnt.
- **Konflikte:** Konfliktfrei, Anfragekonflikt, Terminkonflikt, Raumsperrkonflikt.
- **Terminabweichungen:** Ausweichtermine, Zeitslotsabweichungen.
- **Anfrageart:** Nur spezifische / Nur unspezifische Raumanfragen.
- **Raumzuordnungsgruppe:** Filterung nach bestimmten Räumen.

**B. Termin- und Veranstaltungsbezogene Filter:**

- Datum, Uhrzeit, Wochentag, Rhythmus, Teilnehmerzahl.
- **Veranstaltungsart:** Vorlesung, Seminar, Übung etc.
- **Einrichtung.**

**C. Personenbezogene Filter:**

- Bestimmte/r Anfragesteller/-in oder Dozent/-in.

*Hinweis: Diese Filterkriterien können gespeichert werden, um sie später über die Dropdownbox auszuwählen.*

## 3. Bearbeiten von Raumanfragen

Unter der Filtermaske sehen Sie die Tabelle der aktuellen Raumanfragen.

### 3.1. Struktur der Tabelle

Die erste Spalte zeigt je nach Gruppierung entweder die Veranstaltung (mit Titel) oder den angefragten Raum (mit zugehöriger Veranstaltung) an.

- **Klicks:**
  - Klick auf den Namen des Raums führt zum jeweiligen Raumplan.
  - Klick auf den Titel der Veranstaltung führt zur [Detailseite](https://www.uni-mannheim.de/it/anleitungen/portal2/allgemein/veranstaltungsdetailseite/).
- **Weitere Spalten:** Geben Auskunft über Konflikte, Alternativen, Sitzplatzauslastung, Tag, Uhrzeit, Zeitraum, Dozent/in und Anfragesteller/in.

### 3.2. Konflikt- und Alternativanzeigen

- **Konflikte (Rote Markierung):**
  - **Anfragekonflikt:** Die offene Raumanfrage kollidiert mit einer anderen offenen Raumanfrage.
  - **Terminkonflikt:** Der angefragte Raum ist zum Zeitpunkt bereits vergeben.
  - **Raumsperrkonflikt:** Der angefragte Raum ist zum Zeitpunkt mit einer Raumsperre belegt.
  - *Hinweis:* Die Zahl am Konfliktsymbol gibt die Anzahl der Einzeltermine der Terminserie an, an denen der Konflikt besteht.
- **Alternative Raumanfragen (Grüne Markierung):** Zeigt die Anzahl paralleler Raumanfragen an, die für diese Veranstaltung gestellt wurden. Über die Lupe können alle parallelen Anfragen eingesehen werden.

### 3.3. Aktionen und Massenbearbeitung

In der Spalte **Aktionen (Orange Markierung)** stehen folgende Optionen zur Verfügung:

- Raumanfrage erfüllen
- Alternativen Raum zuordnen
- Raumanfrage zurückstellen (später bearbeiten)
- Raumanfrage ablehnen

Über die **Massenbearbeitung (Blaue Markierung)** können Sie mehrere Anfragen gleichzeitig auswählen und bearbeiten (z. B. ablehnen oder zulassen).

> **Wichtiger Hinweis für Raumverwalter:** Sie können nur Alternativräume vergeben/zuweisen, die auch von Ihnen verwaltet werden. Wenn ein Raumwunsch nicht bestätigt werden kann, wenden Sie sich direkt an den/die Anfragesteller/-in und bitten Sie ihn/sie, die Anfrage zu stornieren und stattdessen den alternativen Raum anzufordern.

## 4. Mehrfach-Raumbuchungen (Für Department-Admins)

Department-Admins, die auch Raummanager\*innen sind, können mehrere Räume gleichzeitig für einen Termin buchen.

1. Rufen Sie die Veranstaltung auf, für die die Mehrfach-Raumbuchung erfolgen soll, und gehen Sie in die **Veranstaltungsbearbeitung**.
1. Navigieren Sie zu **Termine und Räme** und legen Sie einen Termin an.
1. Wenn die nötigen Rechte vorliegen, erscheint neben dem Symbol zum normalen Raumbuchen ein zweites Tür-Symbol für die Mehrfach-Raumbuchung.
1. Wählen Sie alle gewünschten Räume aus und klicken Sie auf **Auswahl hinzufügen**.
1. Das System erstellt automatisch eine eigene Terminserie für jeden gebuchten Raum.

______________________________________________________________________

*Disclaimer: Die Informationen beziehen sich auf die Nutzung des Portal2-Systems der Universität Mannheim.*
