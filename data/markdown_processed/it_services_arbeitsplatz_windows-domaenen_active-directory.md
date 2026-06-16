---
title: Active Directory – Verzeichnisdienst der Universität Mannheim
source_url_de: https://www.uni-mannheim.de/it/services/arbeitsplatz/windows-domaenen/active-directory/
source_url_en: https://www.uni-mannheim.de/en/
category: Services
tags: ['Active Directory', 'Verzeichnisdienst', 'Benutzergruppen', 'Zugriffsrechte', 'Organisationseinheiten', 'IT-Support', 'Windows']
language: de
---

# Active Directory: Der Verzeichnisdienst von Windows

Das Active Directory ist der zentrale Verzeichnisdienst von Windows. In diesem Verzeichnis werden alle Informationen über die Organisationsstruktur einer Domäne sowie über deren Mitglieder (Organisationseinheiten, Computer, Benutzerkennungen etc.) gespeichert.

## 🏛️ Struktur und Aufbau

Die Struktur des Active Directory ist hierarchisch aufgebaut:

1. **Grobstruktur:** Auf der obersten Ebene sind die Organisationseinheiten (Fakultäten und universitäre Einrichtungen) sowie die Containern zu finden, in denen Computer und Personen abgelegt sind.
1. **Unterstruktur:** Auf tieferen Ebenen (z.B. einer Fakultät) werden weitere Organisationseinheiten (wie Lehrstühle) mit ihren untergeordneten Elementen wie **Benutzergruppen** und schließlich den einzelnen Benutzern verwaltet.

Im Active Directory werden neben allgemeinen Informationen (Name, E-Mail-Adresse) auch grundlegende Eigenschaften der Benutzerkennungen und Informationen zum Ablageort der Benutzerdaten gespeichert.

## 👥 Benutzergruppen und Zugriffsrechte

Neben der Speicherung von Benutzerdaten dienen Benutzergruppen zur Verwaltung von Zugriffsrechten.

**Vorteil von Gruppen:**
Der wesentliche Vorteil der Bindung von Zugriffsrechten an Gruppen gegenüber einzelnen Benutzerkennungen ist die Effizienz bei Personalwechseln.

- **Ohne Gruppen:** Muss bei einem Personalwechsel der Zugriff auf ganze Verzeichnishierarchien manuell geändert werden.
- **Mit Gruppen:** Ist es ausreichend, den betreffenden Mitarbeiter lediglich aus der entsprechenden Gruppe zu entfernen oder ihn als Mitglied in eine andere Gruppe einzufügen. Dies ist ein Vorgang von wenigen Mausklicks.

## ⚙️ Verwaltung von Gruppen

Gruppen können innerhalb einer Organisationseinheit (OU) erstellt werden.

**Anleitung zur Erstellung einer Gruppe:**

1. Klicken Sie innerhalb der gewünschten OU (im rechten Fenster) mit der rechten Maustaste.
1. Wählen Sie „Neu“ $\\rightarrow$ „Gruppe“.
1. Geben Sie in das erscheinende Dialogfeld den gewünschten Namen für die neue Gruppe ein.

## ❓ Support und Hilfe

Bei Fragen zur Nutzung oder Verwaltung des Active Directory wenden Sie sich bitte an den [IT-Support](https://www.uni-mannheim.de/it/support/).
