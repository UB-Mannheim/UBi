---
title: ILIAS-Anbindung und Verwaltung von E-Learning-Kursen in Portal²
source_url_de: https://www.uni-mannheim.de/it/anleitungen/portal2/lehrende/ilias-anbindung/
source_url_en: https://www.uni-mannheim.de/en/
category: Benutzung
tags: ['ILIAS', 'E-Learning', 'Portal²', 'Kurs', 'Gruppe', 'Admin', 'Lehrperson', 'Anbindung']
language: de
---

# E-Learning-Plattform ILIAS: Anbindung und Verwaltung

Auf dieser Seite finden Sie eine Sammlung von Erklärungen zu technischen Fragen, die bei der Arbeit mit dem [E-Learning System ILIAS](http://ilias.uni-mannheim.de) aufkommen können.

**Wichtig:** Für inhaltliche Ressourcen zu digitaler Lehre und die Verwendung von ILIAS zur Unterstützung dieser, besuchen Sie die ILIAS-Kurse „Matilde – Wiki zum digitalen Lehren und Lernen“ und „Digitalisierung der Lehre“.

## 📚 Übersicht und Dashboard

Das Dashboard wird beim Einloggen in ILIAS automatisch geladen oder über den Button **Dashboard** im linken Menü oben erreicht.

Hier werden alle ILIAS-Mitgliedschaften in Kursen und Gruppen angezeigt, sowohl vom aktuellen als auch von vergangenen Semestern. Neben dem Kurs- bzw. Gruppennamen befindet sich ein Aktionsfeld, das Befehle enthält, die auch nach Anklicken des Kurs- bzw. Gruppennamens aus der Gruppe heraus gewählt werden können.

**Zum Verwalten:** Um einen Kurs oder eine Gruppe zu verwalten, muss zunächst auf den Namen des Kurses oder der Gruppe geklickt werden.

## ⚙️ ILIAS-Kurs für eine Veranstaltung anlegen

Um einen ILIAS-Kurs anzulegen, muss vorab eine Portal² Veranstaltung angelegt worden sein. Anschließend kann die E-Learning (ILIAS) Anbindung aus Portal² aktiviert werden.

### Voraussetzungen und Vorgehen

**Voraussetzung:** Rolle Department-Admin oder Lehrperson.

- **Department-Admin:** Die E-Learning-Einstellungen finden Sie am schnellsten über „Lehrorganisation" > „Veranstaltungen meiner Einrichtung“.
  - *Hilfe zur Nutzung:* [Veranstaltungsmanagement für Department-Admins](https://www.uni-mannheim.de/it/anleitungen/portal2/admins-und-verwaltung/department-admins-und-studienkoordination/veranstaltungsmanagement/)
- **Lehrperson:** Die E-Learning-Einstellungen finden Sie am schnellsten über „Lehrorganisation" > „Meine Veranstaltungen“.
  - *Hilfe zur Nutzung:* [Veranstaltungsmanagement für Lehrpersonen](https://www.uni-mannheim.de/it/anleitungen/portal2/admins-und-verwaltung/department-admins-und-studienkoordination/veranstaltungsmanagement/)

**Schritte zur Aktivierung:**

1. Gehen Sie zur Bearbeitungsseite der gewünschten semesterabhängigen Veranstaltung (Parallelgruppe).
1. Klicken Sie auf den Reiter „E-Learning“, um die E-Learning-Einstellungen zu öffnen.

**Mögliche Situationen:**

- **Keine Zuordnung:** Wird der Hinweis „Es existiert keine Zuordnung zu externen Systemen“ angezeigt, ist ILIAS für diesen Kurs nicht aktiviert. Klicken Sie auf **„Mit E-Learning-System (ILIAS) verknüpfen“**.
- **Bereits aktiviert:** Ist bereits etwas eingetragen (Option, Kurstitel, Lehrpersonen etc.), ist ILIAS bereits aktiviert.

> **Hinweis:** Wenn Sie weitere ILIAS-Admins hinzufügen möchten, lesen Sie den Abschnitt „Zusätzliche Lehrpersonen und Admins“ weiter unten. Wenn Sie die Art der Zuordnung verändern wollen, müssen Sie zuerst die ILIAS-Verknüpfung deaktivieren und dann neu anlegen.

### Auswahl der ILIAS-Verknüpfung

Nach dem Klick auf „Mit E-Learning-System (ILIAS) verknüpfen“ öffnet sich ein Fenster. Wählen Sie im ersten Feld **„ILIAS“** aus. Im zweiten Feld haben Sie zwei Optionen:

**Option 1: „jede Parallelgruppe als separaten, eigenständigen Kurs“**
Diese Option ist für eine Parallelgruppe gedacht, die unabhängig von anderen Parallelgruppen besteht oder bei der keine weiteren Parallelgruppen vorhanden sind. Es wird ein ILIAS-Kurs mit dem Namen der Parallelgruppe und dem aktuellen Semester erstellt.

**Option 2: „alle Parallelgruppen als Gruppen eines gemeinsamen Kurses“**
Wenn Sie diese Option wählen, wird:

- Ein ILIAS-Kurs für die semesterunabhängige Veranstaltung erstellt.
- Für jede aktivierte semesterabhängige Parallelgruppe eine ILIAS-Gruppe erstellt.

Die Namen werden dabei übernommen: Der ILIAS-Kurs trägt den Namen der semesterunabhängigen Veranstaltung, und die ILIAS-Gruppe trägt den Namen der semesterabhängigen Parallelgruppe.

> **⚠️ Wichtig (Umschaltung zwischen Option 1 und 2):** Wenn Sie von Option 2 zu Option 1 wechseln (oder umgekehrt), wird der bereits erstellte Kurs archiviert und ein neuer Kurs erstellt. Sie können nicht auf beide gleichzeitig zugreifen, da immer einer im Archiv ist.

### Link zum ILIAS-Kurs

Auf der Detailansicht unter dem Tab „Parallelgruppen / Termine“ finden Sie neben „Details einblenden“ den direkten Link zur ILIAS-Gruppe. Die Aktivierung kann bis zu 5 Minuten dauern. Bitte rufen Sie die Detailansichtsseite mehrmals auf, bis der Link erscheint.

## 🧑‍🎓 Teilnehmende auf Inhalte zugreifen lassen

Damit zugelassene Teilnehmende (Mitglieder) auf die ILIAS-Inhalte zugreifen können, müssen diese freigeschaltet werden. Dies erfolgt direkt in ILIAS.

**Voraussetzungen:**

- Veranstaltung mit Veranstaltungsanmeldung in Portal².
- ILIAS-Admin-Rechte für die jeweilige Gruppe.

Im ILIAS wird Ihnen als ILIAS-Admin rechts in der Navigation der Link **„Portal²-Mitglieder“** angeboten.

### Synchronisation der Teilnehmenden

- **Aktiviert:** Werden alle zugelassenen Teilnehmenden aus Portal² übernommen. Ebenso werden später zugelassene Teilnehmende automatisch aufgenommen. Die Teilnehmenden können über Portal² oder ihre ILIAS-Übersicht zugreifen.
- **Deaktiviert:** Bleiben alle zu diesem Zeitpunkt aufgenommenen Teilnehmer\*innen im ILIAS, es werden jedoch keine nachträglich zugelassenen Teilnehmende mehr hinzugefügt.

> **Wichtig:** Übernehmen Sie die Teilnehmenden **ERST DANN**, wenn die Ergebnisse einer eventuellen Verteilung/Zulassung auf Portal²-Seite für die Studierenden freigegeben sind.

### Sammelbearbeitung der Teilnehmendenfreischaltung

Wenn eine Veranstaltung mehrere Parallelgruppen hat und Sie Admin-Rechte in allen Gruppen besitzen, können Sie die Einstellungen der Teilnehmendenfreischaltung direkt bearbeiten:

1. Wählen Sie den Kurs, der den Gruppen übergeordnet ist.
1. Gehen Sie auf „Portal²-Mitglieder“.
1. Hier sehen Sie eine Übersicht aller Gruppen dieses Kurses und können einzeln wählen, zu welcher Gruppe die Teilnehmende freigeschaltet werden sollen.

## 👤 Zusätzliche Lehrpersonen und Admins

### Standard-Administration

Sowohl die durchführende als auch die verantwortliche Lehrperson werden automatisch als Administration des Kurses und der zugehörigen ILIAS-Gruppe eingetragen (basierend auf der Zuordnung in Portal²).

> **Achtung:** Personen, die Admin des ILIAS-Kurses sind, können nicht automatisch auf alle untergeordneten Gruppen zugreifen. Der Zugriff ist nur auf die ILIAS-Gruppe möglich, zu der die Person in Portal² zugeordnet wurde.

### Hinzufügen zusätzlicher Admins

Zusätzlich können Personen hinzugefügt werden, die außer den Dozent\*innen zusätzlich Admin für den ILIAS-Kurs und die zugehörige ILIAS-Gruppe sein sollen (z.B. Department-Admins).

1. Klicken Sie auf das **Person-mit-Stern-Symbol** rechts neben der ILIAS-Gruppe (die Gruppe, zu der die Person im Portal² zugeordnet wurde).
1. Suchen Sie die gewünschten Personen.
1. **Tipp:** Nutzen Sie die Suchfunktion „Bezeichnung, Nachname, Vorname ODER Einrichtung“, um die Personen nach den Organisationseinheiten zu filtern.

**Für die gesamte Gruppe:** Wenn Sie (in Option 2) zusätzliche Personen hinzufügen wollen, die alle Gruppen betreuen können sollen, klicken Sie auf das Person-mit-Stern-Symbol, das **in der Zeile hinter der Veranstaltung** steht. Die hinzugefügten Personen erscheinen dann unter „Zusätzliche Personen für externes System“.

## ℹ️ Weitere Informationen

Weitere Informationen zu den ILIAS-Grundlagen finden Sie auf unserer [ILIAS Grundlagen-Seite](https://www.uni-mannheim.de/it/anleitungen/portal2/lehrende/ilias-anbindung/). Dort erhalten Sie auch Informationen, wie Sie den Beitritt zum Kurs über ILIAS regeln, indem Sie dort ein Beitrittsverfahren definieren.

Tiefergehende Informationen zu ILIAS und E-Learning bekommen Sie direkt in ILIAS selbst, unter dem Kurs: [„Digitalisierung in der Lehre“](http://ilias.uni-mannheim.de/goto.php?target=crs_980882&client_id=ILIAS).
