---
title: Anleitung zur Nutzung von Cryptomator zur Datenverschlüsselung
source_url_de: https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-cryptomator/
source_url_en: https://www.uni-mannheim.de/en/information-security/information-material/instructions-for-cryptomator/
category: Services
tags: ['Cryptomator', 'Verschlüsselung', 'Cloud', 'NAS', 'Passwort', 'Anleitung', 'Datenmanagement']
language: de
---

# Was ist Cryptomator?

Cryptomator ist eine kostenlose Anwendung, die es Ihnen ermöglicht, Daten einfach und komfortabel in einer Cloud oder einem NAS zu verschlüsseln. Die folgende Anleitung erklärt Ihnen, wie Sie Daten mithilfe von Cryptomator verschlüsseln.

## 💡 Wichtige Hinweise zur Nutzung von Cryptomator

Bevor Sie mit der Nutzung beginnen, beachten Sie bitte folgende Punkte:

- **Administrator-Rechte:** Für die Installation benötigen Sie Administrator-Rechte auf Ihrem Computer. Falls Sie diese nicht besitzen, wenden Sie sich bitte an Ihren Administrator oder den IT-Support unter der -2000.
- **Passwortsicherheit:** Auch bei Verwendung des sicheren Verschlüsselungsverfahrens AES-256 ist die Sicherheit der Datei immer nur so gut wie Ihr Passwort. Beachten Sie dies bei der Passwortwahl! Tipps zum Erstellen sicherer Passwörter finden Sie auf unserer Seite zur [Passwortsicherheit](https://www.uni-mannheim.de/informationssicherheit/sicherheitstipps/passwortsicherheit/).
- **Wiederherstellungsschlüssel:** Es besteht die Möglichkeit, sich einen Wiederherstellungsschlüssel erstellen zu lassen. Sollten Sie Ihr Passwort vergessen, ist dieser Schlüssel die einzige Möglichkeit, wieder Zugriff auf Ihre verschlüsselten Daten zu erhalten. **Wichtig:** Bewahren Sie diesen Schlüssel sicher und für Dritte unzugänglich auf.
- **Zugriff und Teilen:**
  - Wenn Sie einen verschlüsselten Ordner mit jemandem austauschen möchten, muss diese Person ebenfalls Cryptomator installiert haben, um den Ordner zu öffnen.
  - Bei der Verwendung eines gemeinsamen verschlüsselten Ordners (z. B. in OneDrive) ist es nicht möglich, zeitgleich an den dort abgelegten Dateien zu arbeiten.

### Vor- und Nachteile

**Vorteile:**

- Verschlüsselte Ordner können einfach und unkompliziert erstellt werden.
- Dateien können in den Ordnern geändert, gelöscht und hinzugefügt werden.

**Nachteile:**

- Beim Öffnen eines verschlüsselten Ordners, ohne diesen zuvor zu entsperren, werden die Dateien darin angezeigt. Cryptomator wandelt die Dateien jedoch in das C9R-Format um, wodurch kein Rückschluss auf die ursprünglichen Dateien möglich ist. Es werden weder Dateiformat, Erstellungsdatum noch die Dateinamen angezeigt, lediglich die Anzahl der Dateien ist ersichtlich.
- Aktuell gibt es noch keine offizielle portable Version dieser Anwendung.

## 🛠️ Wie kann ich Cryptomator nutzen?

### 📥 Download & Installation

**Schritt 1: Cryptomator herunterladen**
Laden Sie Cryptomator unter folgendem Link herunter und installieren Sie es: [https://cryptomator.org/de/downloads/](https://cryptomator.org/de/downloads/)
*(Den Link enthält auch Versionen für MacOS oder Linux.)*

**Schritt 2: Installation durchführen**
Öffnen Sie die heruntergeladene EXE-Datei, um die Installation zu starten. Nach erfolgreicher Installation können Sie Cryptomator direkt starten.

### 📂 Neuen Tresor erstellen

1. **Tresor hinzufügen:** Starten Sie Cryptomator und wählen Sie das "+"-Symbol, gefolgt von „Neuen Tresor erstellen...“.
1. **Tresorname festlegen:** Geben Sie einen Namen für Ihren Tresor ein und bestätigen Sie diesen mit „Weiter“.
1. **Speicherort auswählen:** Wählen Sie über „Durchsuchen...“ den gewünschten Speicherort für Ihren Tresor und bestätigen Sie Ihre Auswahl mit „Weiter“.
1. **Experteneinstellung:** Überspringen Sie das nächste Fenster direkt mit „Weiter“.
1. **Passwort festlegen:** Geben Sie ein sicheres Passwort ein (mindestens 12 Zeichen).
1. **Wiederherstellungsschlüssel:** Sie haben die Möglichkeit, sich einen Wiederherstellungsschlüssel zu erstellen. Sollten Sie Ihr Passwort vergessen, ist dieser Schlüssel die einzige Möglichkeit, Ihren Tresor wieder zu entschlüsseln.
1. **Schlüssel sichern:** Drucken Sie sich den Wiederherstellungsschlüssel aus oder kopieren Sie ihn in einen Passwortmanager oder auf einen USB-Stick. Der Schlüssel darf Dritten nicht zugänglich sein und sollte nicht zusammen mit dem verschlüsselten Tresor aufbewahrt werden.
1. **Tresor entsperren:** Entsperren Sie den neuen Tresor durch Eingabe des Passworts.
1. **Dateien verwalten:** Sie können nun Dateien einfügen, bearbeiten oder löschen. Die Datei „WILLKOMMEN.rtf“ enthält kurze Infos zum Tresor und kann nach dem Lesen gelöscht werden.
1. **Tresor sperren:** Sperren Sie den Tresor, wenn Sie mit dem Bearbeiten der Dateien fertig sind.

### 🔓 Existierenden Tresor öffnen

1. **Tresor auswählen:** Wählen Sie das "+"-Symbol und „Bestehenden Tresor öffnen...“ aus.
1. **Datei auswählen:** Öffnen Sie den gewünschten Tresor und wählen Sie die Datei „vault.cryptomator“ aus.
1. **Tresor entsperren:** Geben Sie das Passwort ein, um den Tresor zu entsperren.
1. **Dateien verwalten:** Sie können die darin abgelegten Dateien öffnen, bearbeiten, löschen oder neue hinzufügen.

### 🔄 Passwort zurücksetzen

Sollten Sie Ihr Passwort vergessen haben, benötigen Sie den Wiederherstellungsschlüssel, um es zurückzusetzen.

1. **Tresoroptionen:** Wählen Sie bei dem entsprechenden Ordner „Tresoroptionen“ aus.
1. **Passwort zurücksetzen:** Unter dem Reiter „Passwort“ haben Sie die Möglichkeit, Ihr Passwort zurückzusetzen.
