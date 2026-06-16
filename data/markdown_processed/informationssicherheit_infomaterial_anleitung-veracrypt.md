---
title: VeraCrypt Anleitung – Verschlüsselung externer Speichermedien
source_url_de: https://www.uni-mannheim.de/en/
source_url_en: https://www.uni-mannheim.de/en/
category: Services
tags: ['VeraCrypt', 'Verschlüsselung', 'Speichermedium', 'USB-Stick', 'Passwort', 'Datensicherheit', 'Anleitung', 'Datenverschlüsselung']
language: de
---

# VeraCrypt: Verschlüsselung externer Speichermedien

Mit VeraCrypt ist es möglich, gesamte Speichermedien wie externe Festplatten und USB-Sticks zu verschlüsseln. Das System erlaubt es, Dateien jederzeit auf dem verschlüsselten Speichermedium hinzuzufügen, zu ändern und zu löschen.

## ⚠️ Wichtige Hinweise und Voraussetzungen

Bevor Sie mit der Verschlüsselung beginnen, beachten Sie bitte folgende Punkte:

- **Administrator-Rechte:** Sowohl für die Installation als auch für die Verschlüsselung externer Speichermedien sind Administrator-Rechte auf dem Computer erforderlich. Falls Sie diese Rechte nicht besitzen, empfehlen wir Ihnen den Einsatz von [Cryptomator](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-cryptomator/).
- **Passwortsicherheit:** Die Sicherheit des verschlüsselten Speichermediums hängt maßgeblich von der Stärke Ihres Passworts ab. Wählen Sie ein sicheres Passwort (mindestens 12 Zeichen). Weitere Tipps zur [Passwortsicherheit](https://www.uni-mannheim.de/informationssicherheit/sicherheitstipps/passwortsicherheit/) finden Sie auf unserer Seite.
- **Verwendungszweck:** Verwenden Sie VeraCrypt nicht für die Systemfestplatte oder für Ablagen auf einem NAS oder in der Cloud.
- **Austausch:** Wenn Sie ein verschlüsseltes Speichermedium mit jemandem austauschen möchten, muss diese Person ebenfalls VeraCrypt auf ihrem Computer installiert haben, um das Medium öffnen zu können.
- **Speichermedium:** Das Speichermedium muss vor der Formatierung leer sein, da ansonsten alle vorhandenen Daten unwiederbringlich gelöscht werden.

## ⚙️ VeraCrypt nutzen: Schritt-für-Schritt-Anleitung

### 1. Installation und Vorbereitung

**Download & Installation**

1. **Herunterladen:** Laden Sie VeraCrypt unter folgendem Link herunter und installieren Sie die Anwendung: [https://www.veracrypt.fr/en/Downloads.html](https://www.veracrypt.fr/en/Downloads.html)
1. **Installation:** Öffnen Sie die heruntergeladene EXE-Datei, um die Installation zu starten.

### 2. Externes Speichermedium verschlüsseln (Volume erstellen)

Dieser Prozess erfordert ein leeres Speichermedium.

1. **Speichermedium anschließen:** Starten Sie VeraCrypt und schließen Sie das gewünschte Speichermedium an.
1. **Volume erstellen:** Klicken Sie auf den Button „Volume erstellen“.
1. **Partition auswählen:** Wählen Sie den Punkt „Eine Partition/ein Laufwerk verschlüsseln“ und bestätigen Sie mit „Weiter >“. (Hierfür sind Administrator-Rechte erforderlich.)
1. **Volumen-Typ:** Wählen Sie „Standard VeraCrypt-Volumen“ und bestätigen Sie mit „Weiter“.
1. **Datenträger auswählen:** Wählen Sie über den Button „Datenträger ...“ Ihr eingestecktes Speichermedium aus und bestätigen Sie mit „OK“.
1. **Formatieren:** Wählen Sie „Verschlüsseltes Volume erstellen und formatieren“ und bestätigen Sie mit „Weiter >“.
1. **Einstellungen:** Behalten Sie die Standardeinstellungen bei und bestätigen Sie diese mit „Weiter >“.
1. **Passwort festlegen:** Legen Sie ein sicheres Passwort fest (mindestens 12 Zeichen).
1. **Formatierung starten:** Bewegen Sie den Mauszeiger zufällig im Fenster, bis die Anzeige unten grün wird. Klicken Sie anschließend auf „Formatieren“ und bestätigen Sie die Sicherheitsabfrage mit „Ja“.
   - *Hinweis:* Die Formatierung kann je nach Größe des Speichermediums einige Zeit in Anspruch nehmen.
1. **Abschluss:** Bestätigen Sie die Meldung der erfolgreichen Erstellung mit „OK“ und beenden Sie VeraCrypt.

### 3. Verschlüsseltes Speichermedium öffnen und bearbeiten

Wenn Sie das verschlüsselte Speichermedium wiederverwenden möchten, gehen Sie wie folgt vor:

1. **Anschließen:** Schließen Sie das verschlüsselte Speichermedium an Ihren Computer an.
1. **Formatierung verhindern:** Sollte eine Meldung erscheinen, die eine Formatierung vorschlägt, bestätigen Sie diese **NICHT** mit „Datenträger formatieren“, sondern klicken Sie auf „Abbrechen“.
1. **Speichermedium auswählen:** Öffnen Sie VeraCrypt. Wählen Sie über „Datenträger ...“ Ihr verschlüsseltes Speichermedium aus und bestätigen Sie mit „OK“.
1. **Einbinden:** Klicken Sie auf „Einbinden“, um das ausgewählte Speichermedium auf einem verfügbaren Laufwerk einzubinden.
1. **Passwort eingeben:** Geben Sie das zuvor festgelegte Passwort ein und bestätigen Sie es.
1. **Zugriff:** Das Speichermedium wird nun als lokaler Datenträger angezeigt. Sie können Dateien abspeichern, ändern oder löschen.
1. **Trennen:** Nachdem Sie Ihre Arbeit beendet haben, klicken Sie auf „Trennen“ und beenden Sie VeraCrypt.
