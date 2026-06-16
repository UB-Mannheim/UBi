---
title: Anleitung zur Erstellung und Entpackung verschlüsselter ZIP-Archive mit 7-Zip
source_url_de: https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-verschluesseltes-zip-archiv/
category: Benutzung
tags: ['7-Zip', 'Verschlüsselung', 'ZIP-Archiv', 'Passwort', 'Sicherheit', 'Datenübertragung', 'AES-256']
language: de
---

# Verschlüsselte ZIP-Archive mit 7-Zip: Anleitung und Sicherheitshinweise

Der Einsatz von verschlüsselten ZIP-Archiven ist eine einfache und kostenlose Methode, um Informationen durch Verschlüsselung zu schützen, beispielsweise beim Versenden per E-Mail oder beim Speichern auf einem USB-Stick. Diese Anleitung erklärt, wie Sie mit dem Tool 7-Zip ein solches Archiv erstellen und entpacken können.

## 🔒 Sicherheitshinweise und Best Practices

Bevor Sie ein verschlüsseltes Archiv erstellen, beachten Sie bitte folgende wichtige Sicherheitsempfehlungen:

### 1. Passwortsicherheit

Auch wenn Sie das sichere Verschlüsselungsverfahren AES-256 verwenden, ist die Sicherheit der Datei immer nur so gut wie Ihr Passwort.

- **Passwortwahl:** Wählen Sie ein sicheres Passwort mit mindestens 12 Zeichen.
- **Tipps:** Weitere Tipps zum Erstellen sicherer Passwörter finden Sie auf unserer Seite zur [Passwortsicherheit](https://www.uni-mannheim.de/informationssicherheit/sicherheitstipps/passwortsicherheit/).

### 2. Übermittlung des Passworts

Wenn Sie ein verschlüsseltes ZIP-Archiv per E-Mail versenden, senden Sie das Passwort **niemals** zusammen mit dem Archiv. Teilen Sie das Passwort stattdessen über einen anderen, sicheren Kanal mit dem Empfänger, wie z. B. telefonisch, per Brief oder persönlich.

### 3. Funktionsweise und Einschränkungen

- **Vorteile:** Verschlüsselte ZIP-Archive sind einfach zu erstellen, können mit wenigen Klicks erstellt werden und gewährleisten durch AES-256 eine sichere Verschlüsselung.
- **Nachteile:**
  - Es können nur einzelne Dateien oder Ordner gepackt werden; die Verschlüsselung eines gesamten USB-Sticks oder einer Festplatte ist nicht möglich.
  - Ein einmal erstelltes Archiv lässt sich nicht erweitern. Um Dateien hinzuzufügen, muss ein neues Archiv erstellt werden.

## 🛠️ Anleitung: 7-Zip verwenden

### ⚠️ Wichtig: Software-Update

Bitte beachten Sie, dass in veralteten 7-Zip Versionen Sicherheitslücken entdeckt wurden. Aktualisieren Sie daher 7-Zip auf die Version 23.01 oder höher.

### 📥 1. 7-Zip herunterladen und installieren

Falls 7-Zip noch nicht auf Ihrem Computer installiert ist, laden Sie die Anwendung unter folgendem Link herunter und installieren Sie sie:
[https://www.heise.de/download/product/7-zip-13139](https://www.heise.de/download/product/7-zip-13139)
**Hinweis:** Für die Installation benötigen Sie Administrator-Rechte. Falls diese fehlen, wenden Sie sich bitte an Ihren Administrator oder den IT-Support unter der -2000.

### 📂 2. Verschlüsseltes Archiv erstellen

1. **Dateiauswahl:** Öffnen Sie das Kontextmenü (Rechtsklick) auf der Datei oder dem Ordner, der verschlüsselt werden soll. Wählen Sie unter „7-Zip“ den Punkt „Zu einem Archiv hinzufügen...“ aus.
1. **Passwort festlegen:** Legen Sie ein sicheres Passwort fest (mindestens 12 Zeichen).
1. **Verfahren wählen:** Stellen Sie sicher, dass das Verschlüsselungsverfahren auf **AES-256** eingestellt ist.
1. **Abschluss:** Bestätigen Sie die Eingaben mit „OK“, um das verschlüsselte Archiv zu erstellen.

### 🔓 3. Verschlüsseltes Archiv entpacken

1. **Speicherort auswählen:** Doppelklicken Sie auf das verschlüsselte Archiv, um 7-Zip zu öffnen. Klicken Sie anschließend auf „Entpacken“ und wählen Sie den gewünschten Speicherort.
1. **Passwort eingeben:** Geben Sie das korrekte Passwort ein und bestätigen Sie mit „OK“. Das Archiv wird nun an dem ausgewählten Speicherort entpackt.
