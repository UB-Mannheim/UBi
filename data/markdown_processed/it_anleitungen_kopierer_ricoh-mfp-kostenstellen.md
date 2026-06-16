---
title: Anleitung zur Einrichtung von Kostenstellen auf Ricoh MFP Kopierern
source_url_de: https://www.uni-mannheim.de/it/anleitungen/kopierer/ricoh-mfp-kostenstellen/
source_url_en: https://www.uni-mannheim.de/en/
category: Benutzung
tags: ['Ricoh', 'MFP', 'Kostenstelle', 'Einrichtung', 'Anleitung', 'Kopierer', 'Anwender-Authentifizierung', 'Druckertreiber']
language: de
---

# Kostenstellen-Verwaltung auf Ricoh MFP Kopierern

Dieser Leitfaden beschreibt die Schritte zur Einrichtung von Kostenstellen (Anwender-Authentifizierung) sowohl über das Webinterface des Kopierers als auch über den lokalen Druckertreiber.

## 🖥️ Kostenstellen-Einrichtung über das Webinterface

Die Einrichtung erfolgt schrittweise über die IP-Adresse des Kopierers.

### 1. Vorbereitung und Login

1. **Webinterface aufrufen:** Geben Sie die IP-Adresse des Ricoh-Kopierers in die Adresszeile Ihres Browsers ein (z.B. `https://IP-Adresse Ihres Kopierers`).
   - *Hinweis:* Die IP-Adresse finden Sie auf dem Hauptbildschirm des Kopierers unter „Status prüfen“ $\\rightarrow$ „Gerätestatus“ / „Netzwerk“.
1. **Warnmeldung bestätigen:** Bestätigen Sie *ausnahmsweise* die Warnmeldung, indem Sie auf „Erweitert“ und dann auf „Risiko akzeptieren und fortfahren“ klicken.
   - *Wichtig:* Dieses Vorgehen ist nur für diesen Ausnahmefall notwendig, da der Kopierer ein selbst-signiertes Zertifikat verwendet.
1. **Adblocker deaktivieren:** Deaktivieren Sie bitte alle Adblocker (Werbeblocker) für das Webinterface des Kopierers, um eine korrekte Darstellung aller Menüelemente zu gewährleisten.
1. **Anmelden:** Klicken Sie oben rechts auf „Login“ und melden Sie sich mit der Kennung `admin` und dem bei der Ersteinrichtung erhaltenen Kennwort an.
   - *Hilfe:* Bei Problemen mit dem Kennwort kontaktieren Sie bitte den IT-Support unter der Hotline -2000, per E-Mail unter [itsupport@uni-mannheim.de](mailto:itsupport@uni-mannheim.de) oder per Teams unter „UNIT Support“. Halten Sie hierzu die Seriennummer des Kopierers bereit.

### 2. Konfiguration der Kostenstelle

1. **Navigation:** Klicken Sie links oben auf „Home“ (falls dieser Bildschirm angezeigt wird).
1. **Gerätemanagement:** Fahren Sie mit der Maus über den Menüpunkt „Gerätemanagement“ und klicken Sie auf „Konfiguration“.
1. **Authentifizierungseinstellungen:** Klicken Sie unter „Geräteeinstellungen“ auf „Anwender-Authentifizierungsverwaltung“.
1. **Standardeinstellung ändern:** Stellen Sie bei „Anwender-Authentifizierungsverwaltung“ die Standardeinstellung von „Aus“ (1) auf „Anwendercode“ (2) um.
1. **Druckerjob-Authentifizierung:** Wählen Sie unter „Druckerjob-Authentifizierung“ den Eintrag „Gesamt“ aus (1).
1. **Funktionen einschränken:** Setzen Sie unter „Anwendercode-Authentifizierungseinstellungen“ bei „Einzuschränkende Funktionen“ die Häkchen bei **allen** Optionen, außer „PC-Steuerung“, „Document Server“ und „Fax“ (2). Klicken Sie abschließend auf „OK“ (3).

### 3. Hinzufügen der Kostenstelle

1. **Zurück zur Konfiguration:** Sie werden automatisch zur Seite „Konfiguration“ zurückgeleitet. Klicken Sie dort links oben auf „Zurück“.
1. **Adressbuch öffnen:** Fahren Sie mit der Maus über „Gerätemanagement“ und klicken Sie auf „Adressbuch“.
1. **Eingabe:** Klicken Sie auf den Reiter „Detaillierte Eingabe“ und anschließend auf „Anwender hinzufügen“.
1. **Einstellungen vornehmen:**
   - **Name:** Geben Sie den gewünschten Namen der Kostenstelle ein (1).
   - **Titel:** Wählen Sie für Titel 1 „Kein(e)“, für Titel 2 „1“ und für Titel 3 „Kein(e)“.
   - **Oft hinzufügen:** Wählen Sie „Aus“ (2).
   - **Authentifizierungscode:** Geben Sie unter „Anwendifizierungsinformationen“ unter „Anwendercode“ den gewünschten Code für die Kostenstelle ein (3).
   - **Verfügbare Funktionen:** Setzen Sie alle Häkchen, außer „Document Server“, „Fax“ und „Browser“, und wählen Sie „Vollfarbe / Automatische Farbauswahl“ aus (4).
   - **Speichern:** Schließen Sie die Einstellungen mit „OK“ ab (5).

### 4. Abschluss und Timer-Einstellung

1. **Zurückkehren:** Klicken Sie links oben auf „Zurück“, um zur Adressliste zu gelangen.
1. **Timer einstellen:** Fahren Sie erneut mit der Maus über „Gerätemanagement“ und klicken Sie auf „Konfiguration“. Klicken Sie unter „Geräteeinstellungen“ auf „Timer“.
1. **Auto-Abmelde-Timer:** Schalten Sie den „Auto-Abmelde-Timer“ auf „Ein“ und tragen Sie die Zahl **60** bei „Sekunden“ ein. Schließen Sie die Einstellungen links oben mit „OK“ ab.
1. **Fertigstellung:** Die Konfiguration ist abgeschlossen. Bei Bedarf können weitere Kostenstellen eingerichtet werden. Andernfalls melden Sie sich über den Button „Abmelden“ vom Kopierer-Webinterface ab.

______________________________________________________________________

## 💻 Kostenstellen-Verwaltung über den Druckertreiber (Windows)

Dieser Prozess dient der Verknüpfung des Kopiercodes direkt im lokalen Druckertreiber.

1. **Einstellungen öffnen:** Drücken Sie die Windows-Taste und `i` gleichzeitig, um die Einstellungen zu öffnen.
1. **Geräteauswahl:** Wählen Sie in der Seitenleiste „Bluetooth und Geräte“ (1) aus und klicken Sie danach auf „Drucker und Scanner“ (2).
1. **Drucker auswählen:** Wählen Sie den passenden Drucker aus der Liste der verbundenen Geräte.
1. **Eigenschaften öffnen:** Klicken Sie auf „Druckereigenschaften“.
1. **Einstellungen:** Wählen Sie danach „Einstellungen…“ aus.
1. **Code-Eingabe:** Klicken Sie auf „Anwendercode-Einst…“.
1. **Code eingeben:** Geben Sie nun Ihren Kopiercode ein.

[Weitere Anleitungen für Ricoh Kopierer](https://www.uni-mannheim.de/it/anleitungen/kopierer/)
