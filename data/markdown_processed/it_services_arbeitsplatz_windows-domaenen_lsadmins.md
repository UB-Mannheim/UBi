---
title: Einrichtung und Verwaltung von Organisations-Einheiten (OUs) in der Domäne
source_url_de: https://www.uni-mannheim.de/it/services/arbeitsplatz/windows-domaenen/lsadmins/
category: Services
tags: ['Active Directory', 'OU', 'Domäne', 'Arbeitsplatz', 'Benutzergruppen', 'Profile', 'Administration', 'IT-Support']
language: de
---

# Leitfaden zur Einrichtung von Organisations-Einheiten (OUs) und Arbeitsplätzen in der Domäne

Dieser Leitfaden richtet sich an Lehrstuhladministrator\*innen, die eine größere Anzahl von Arbeitsplätzen in die Domäne integrieren müssen. Die folgenden Schritte dienen als umfassende Planungsgrundlage für die Organisation der DV-Infrastruktur.

## 1. Beantragung und Einrichtung der Organizational Unit (OU)

Die Einrichtung einer OU ist notwendig, um die DV-Organisation eines Lehrstuhls oder einer zentralen Einrichtung zu strukturieren und zentrale Ressourcen effizient zu verwalten.

- **Funktion:** OUs sind Mechanismen des Windows-Domänen-Konzepts, die eine effiziente Organisation der Infrastruktur ermöglichen.
- **Wichtig:** OUs werden nicht automatisch erstellt, nur weil eine Lehrstuhlkennung beantragt wurde. Sie müssen von einem Domänen-Admin (Universitäts-IT-Mitarbeiter) angelegt und mit den notwendigen Eigenschaften zur Verwaltung von Berechtigungen und Ressourcen ausgestattet werden.
- **Vorgehen:** Wenden Sie sich bei der Beabsichtigung, eine OU zur Organisation Ihrer DV-Infrastruktur zu nutzen, bitte an den [IT-Support](https://www.uni-mannheim.de/it/support/).

## 2. Einrichtung des Admin-Arbeitsplatzes

Für die Verwaltung der OU ist ein spezieller Admin-Arbeitsplatz erforderlich.

- **Admin-Arbeitsplatz:** Dieser Arbeitsplatz stellt spezielle Plugins für den Zugriff auf das Active Directory bereit.
- **Mmc:** Die Bezeichnung für die „Microsoft-Management-Console“. Diese grafische Oberfläche kann mit Snap-Ins ausgestattet werden, die spezifische Funktionalitäten zur Verfügung stellen.
- **OU-Administration:** Für die Verwaltung einer OU wird ein Snap-In benötigt, das es ermöglicht, die OU direkt im Active Directory zu verwalten.

## 3. Definition und Befüllung von Benutzergruppen

Sobald die OU existiert und Sie als OU-Admin eingetragen sind, ist die Definition von Benutzergruppen der nächste Schritt. Diese Gruppen sind essenziell für die Festlegung der Nutzungsberechtigung von Ressourcen und die Aufnahme der Mitarbeitenden des Lehrstuhls.

### Namenskonventionen beachten

Um Namenskonflikte zu vermeiden, müssen bestimmte Namenskonventionen beachtet werden:

- **Standard-Gruppen:** Beginnen mit dem Namen der **OU**, gefolgt von einem Unterstrich (`_`) und dem eigentlichen Gruppennamen.
- **Gruppen für zentrale Ressourcen:** Folgen nach dem **OU**-Namen zwei Unterstrichen (`__`), gefolgt von einer Abkürzung des Dienstnamens, erneut zwei Unterstrichen (`__`) und schließlich dem eigentlichen Gruppennamen.

**Beispiel:**

- Die Gruppen mit dem Präfix `lsxyz__FS__` sind für die Regelung der Nutzungsberechtigung des zentralen Fileservice reserviert.
- Die Gruppe `lsxyz_admins` beinhaltet die Administratoren dieser OU.

## 4. Aufnahme der Arbeitsplätze in die Domäne

Nachdem der Admin-Arbeitsplatz eingerichtet und die OU-Gruppen definiert wurden, müssen die Arbeitsplätze des Lehrstuhls in die Domäne aufgenommen werden. Dieser Prozess besteht aus mehreren Teilaufgaben:

1. **Domänen-Join:** Der Rechner muss zunächst mithilfe des Skripts `"join-ad-mit-ou.bat"` in die Domäne aufgenommen werden.
1. **Gruppenanpassung:**
   - Mit dem Skript `"group-ad.bat"` muss der Domänen-Admin aus der Gruppe „Lokale Administrator\*innen“ entfernt werden.
   - Die OU-Gruppe „Lehrstuhl-Administrator*innen“ muss in die Gruppe „Lokale Administrator*innen“ aufgenommen werden.
   - Schließlich muss sichergestellt werden, dass nur Benutzerkennungen, die Mitglied in der OU-Gruppe „Lehrstuhl_alle“ sind, sich an diesem Rechner anmelden können.
1. **Profile kopieren:** Folgen Sie anschließend der Anleitung [Wie kopiere ich Profile?](https://www.uni-mannheim.de/it/services/arbeitsplatz/windows-domaenen/lsadmins/#wie-kopiere-ich-profile).

## 5. Übertragung lokaler Profile auf Domänen-Profile

Der letzte Schritt ist die Herstellung der gewohnten Umgebung für Personen, die bisher mit einer lokalen Benutzerkennung gearbeitet haben, indem deren lokales Profil auf das entsprechende Domänen-Profil übertragen wird.

**Wichtige Unterscheidung:** Ein lokaler Benutzer und ein Domänenbenutzer sind aus Sicht von Windows unterschiedliche Benutzerkennungen.

### Schritt-für-Schritt-Anleitung zur Profilübertragung:

1. **Vorbereitung:** Der/die Domänen-Benutzer\*in muss sich zunächst an und wieder abmelden, damit ein neues Domänen-Profil erzeugt und gespeichert wird.
1. **Zugriff:** Melden Sie sich anschließend als lokaler Admin (weder mit der lokalen noch mit der zugehörigen Domänenkennung) an.
1. **Einstellungen öffnen:** Klicken Sie mit der rechten Maustaste auf „Arbeitsplatz“ und wählen Sie den Menüpunkt „Eigenschaften“. Wählen Sie dort die Registerkarte „Erweitert“ und klicken Sie im Abschnitt „Benutzerprofile“ auf „Einstellungen“.
1. **Kopieren starten:** Wählen Sie in der rechten Dialogbox die lokale Benutzerkennung aus. Klicken Sie auf „Kopieren nach“.
1. **Ziel festlegen:** Klicken Sie auf „Durchsuchen“ und wählen Sie das Verzeichnis `C:\Dokumente und Einstellungen`. Wählen Sie den Ordner, der das Suffix **`.AD`** trägt (dies ist das Ziel des Kopiervorgangs).
1. **Berechtigung anpassen (Wichtig!):** Klicken Sie im Abschnitt „Benutzer\*in“ auf „Ändern“. Hier muss die **Domänen-Benutzerkennung** die Zugriffsrechte erhalten, nicht die lokale Kennung.
   - Geben Sie die Benutzerkennung ein und klicken Sie auf „Namen überprüfen“.
   - Bestätigen Sie die vollständige Kennung und klicken Sie in der Dialogbox „Kopieren nach“ erneut auf „OK“.
1. **Abschluss:** Das lokale Profil wird auf das Domänen-Profil kopiert. Bestätigen Sie die Überschreibung des vorhandenen Profils mit „Ja“.

**Hinweis:**

- Die Profilübertragung ist ein **einmaliger Vorgang**.
- Änderungen, die Sie an dem Domänen-Profil vornehmen, werden **nicht** an das lokale Profil weitergereicht.
- Im Regelfall sollten Sie sich ab diesem Zeitpunkt nur noch mit Ihrer Domänenkennung anmelden.
