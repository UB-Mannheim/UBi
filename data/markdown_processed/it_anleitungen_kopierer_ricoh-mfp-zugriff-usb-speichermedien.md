---
title: Ricoh Kopierer – USB-Speichermedien einrichten und formatieren
source_url_de: https://www.uni-mannheim.de/it/anleitungen/kopierer/ricoh-mfp-zugriff-usb-speichermedien/
source_url_en: https://www.uni-mannheim.de/en/
category: Services
tags: ['Ricoh', 'Kopierer', 'USB', 'FAT32', 'Formatieren', 'Anleitung', 'MFP', 'Speichermedien']
language: de
---

# Ricoh Kopierer: Zugriff auf USB-Speichermedien einrichten

Dieser Leitfaden beschreibt die Schritte zur Aktivierung des Zugriffs auf USB-Speichermedien (Scannen und Drucken) am Ricoh Kopierer sowie die notwendige Vorbereitung des USB-Sticks.

## ⚙️ Teil 1: Konfiguration des Kopierers (Webinterface)

Um den USB-Stick nutzen zu können, müssen Sie die Einstellungen über das Webinterface des Kopierers vornehmen.

**Vorbereitung:**

1. **IP-Adresse ermitteln:** Rufen Sie über Ihren Browser das Webinterface des Ricoh-Kopierers auf, indem Sie die IP-Adresse in die Adresszeile eingeben: `https://IP-Adresse Ihres Kopierers`
   - *Hinweis:* Die IP-Adresse finden Sie auf dem Hauptbildschirm links unten unter „Status prüfen“ → „Gerätestatus“ / „Netzwerk“.
1. **Adblocker deaktivieren:** Falls Sie einen Adblocker (Werbeblocker) aktiv haben, deaktivieren Sie diesen bitte für das Webinterface des Kopierers, da sonst die Darstellung fehlerhaft sein kann.

**Zugriff und Anmeldung:**

1. **Warnmeldung bestätigen:** Bestätigen Sie *ausnahmsweise* die Warnmeldung, indem Sie auf „Erweitert“ und dann auf „Risiko akzeptieren und fortfahren“ klicken. (Dies ist notwendig, da der Kopierer ein selbst-signiertes Zertifikat verwendet.)
1. **Login:** Klicken Sie oben rechts auf „Login“.
1. **Anmelden:** Melden Sie sich mit der Kennung `admin` und dem bei der Ersteinrichtung erhaltenen Kennwort an.
   - *Hilfe bei Passwörtern:* Bei Problemen kontaktieren Sie bitte den IT-Support unter der Hotline -2000, per E-Mail unter [itsupport@uni-mannheim.de](mailto:itsupport@uni-mannheim.de) oder per Teams unter „UNIT Support“. Halten Sie hierzu die Seriennummer des Kopierers bereit.

**Einstellungen vornehmen:**

1. **Navigation:** Falls nach der Anmeldung ein anderer Bildschirm angezeigt wird, klicken Sie links oben auf „Home“.
1. **Gerätemanagement:** Fahren Sie mit der Maus über den Menüpunkt „Gerätemanagement“ und klicken Sie auf „Konfiguration“.
1. **Systemeinstellungen:** Klicken Sie unter „Geräteeinstellungen“ auf „System:“.
1. **Mediensteckplatz:** Wählen Sie bei „Allgemeine Einstellungen“ unter „Verwendung des Mediensteckplatzes“ für die folgenden beiden Optionen:
   - „Im Speichergerät speichern“
   - „Vom Speichergerät drucken“
   - Stellen Sie bei beiden Optionen „Erlauben“ ein.
1. **Speichern und Abmelden:** Klicken Sie oben links auf „OK“ und anschließend rechts oben auf „Abmelden“.

**✅ Fertig:** Die Konfiguration ist abgeschlossen. Sie können nun am Ricoh-Kopierer sowohl auf USB-Sticks scannen als auch Dokumente ausdrucken, die auf dem USB-Stick gespeichert sind.

______________________________________________________________________

## 💾 Teil 2: Vorbereitung des USB-Sticks (FAT32 Formatierung)

Der USB-Stick muss zwingend im **FAT32**-Format vorliegen, da das System ihn sonst nicht erkennt.

**Vorgehensweise unter Windows:**

1. **Verbinden:** Schließen Sie den USB-Stick an Ihren Windows-PC an.
1. **Explorer öffnen:** Öffnen Sie den Windows-Explorer (Windows-Taste + E).
1. **Rechtsklick:** Klicken Sie mit der rechten Maustaste auf den USB-Stick und wählen Sie „Formatieren“.
   - **⚠️ Wichtig:** Vergewissern Sie sich, dass Sie das korrekte Laufwerk auswählen, da andernfalls Datenverlust droht. Der gesamte Inhalt des Sticks wird gelöscht.
1. **Einstellungen wählen:**
   - Dateisystem: **FAT32**
   - Volumebezeichnung: Geben Sie einen Namen ein (z. B. „MFP-Stick“).
   - Haken bei „Schnellformatierung“ aktivieren.
1. **Starten:** Klicken Sie auf „Starten“ und bestätigen Sie die Warnmeldung.
1. **Ablösung:** Melden Sie den USB-Stick anschließend wie gewohnt vom System ab („sicheres Entfernen“).

Der USB-Stick kann nun für die Verwendung an den Ricoh-Kopierern für Scan-to-USB und zum Ausdrucken von Dateien genutzt werden.

______________________________________________________________________

**🔗 Weitere Anleitungen:**

- [Ricoh MFP USB-Stick mit FAT32 formatieren](https://www.uni-mannheim.de/it/anleitungen/kopierer/ricoh-mfp-usb-stick-formatieren/)
- [Weitere Anleitungen für Ricoh Kopierer](https://www.uni-mannheim.de/it/anleitungen/kopierer/)
