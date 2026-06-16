---
title: Exchange Postfach mit macOS (MacBook/iMac) verbinden
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/einbinden-macos/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/adding-an-exchange-account-to-macos/
category: Services
tags: ['Exchange', 'macOS', 'Outlook', 'Apple Mail', 'Uni-ID', 'Einrichtung', 'Anleitung', 'Postfach']
language: de
---

# Exchange Postfach mit macOS verbinden

Diese Anleitungen zeigen Ihnen, wie Sie Ihr MacBook oder iMac mit Ihrem Exchange Postfach verbinden. **Bitte beachten Sie:** Diese Anleitungen können erst angewendet werden, nachdem Ihr Exchange Postfach erstellt wurde.

**Hinweis:** Sie sind nicht auf Mail-Clients wie Outlook oder Apple-Mail angewiesen. Ihr Exchange Postfach können Sie auch über Ihren Webbrowser unter [https://exchange.uni-mannheim.de/owa](https://exchange.uni-mannheim.de/owa) aufrufen. Dort melden Sie sich mit Ihrer Uni-ID (= ehem. „Kennung“) und dem zugehörigen Passwort an, um auf E-Mails, Kalender und Adressbücher zuzugreifen.

## 📧 Anleitung für Outlook für Mac

Folgen Sie diesen Schritten, um Ihr Exchange-Konto in Outlook 365 einzurichten:

**Schritt 1:** Starten Sie Outlook 365. Klicken Sie oben links auf „Outlook“ und dann auf „Einstellungen“.
**Schritt 2:** Klicken Sie auf „Konten“.
**Schritt 3:** Klicken Sie links unten auf „+ Neues Konto hinzufügen“.
**Schritt 4:** Geben Sie Ihre Exchange-Adresse ein und klicken Sie auf „Weiter“.

- **Falls das IdP-Login-Fenster** der Uni Mannheim öffnet (Schloss im Hintergrundbild und Logo der Uni im Vordergrund): Führen Sie die Schritte 5–7 aus.
- **Falls sofort das Exchange-Anmeldedaten-Fenster** öffnet: Überspringen Sie die Schritte 5–7 und fahren Sie mit Schritt 8 fort.

**Schritt 5:** Schließen Sie das IdP-Fenster mit einem Klick links oben auf den Schließen-Button.
**Schritt 6:** Klicken Sie im darunterliegenden Fenster auf „Nicht Microsoft 365?“.
**Schritt 7:** Klicken Sie auf den „Exchange“-Button.

**Schritt 8:**

1. Tragen Sie im Feld „DOMÄNE\\Benutzername“ ein: **`AD\Uni-ID`** (Beispiel: `AD\memuster`).
   > **Wichtig:** Verwenden Sie den Backslash (`\`), nicht den Schrägstrich (`/`). Den Backslash können Sie mit `ALT + Shift + 7` erzeugen.
1. Geben Sie das Passwort Ihrer Uni-ID ein.
1. Tragen Sie im Feld „Server“ folgenden Wert ein: [https://exchange.uni-mannheim.de/EWS/Exchange.asmx](https://exchange.uni-mannheim.de/EWS/Exchange.asmx).
1. Bestätigen Sie mit einem Klick auf „Konto hinzufügen“.

**Schritt 9:** Bestätigen Sie danach erneut mit einem Klick auf „Dieses Mal überspringen“. Ihr Postfach wird eingerichtet und synchronisiert. Dies kann je nach Postfachgröße einige Zeit in Anspruch nehmen.

## ✉️ Anleitung für Apple Mail

### 1. Exchange-Absender-Adresse ermitteln (Vorbereitung)

Bevor Sie Mail einrichten, benötigen Sie Ihre Exchange-Absender-Adresse:

1. Öffnen Sie Ihren Internetbrowser (z. B. Safari oder Chrome) und rufen Sie [https://exchange.uni-mannheim.de](https://exchange.uni-mannheim.de) auf.
1. Geben Sie dort Ihre Uni-ID und das dazugehörige Passwort ein und klicken Sie auf „Anmelden“.
1. Klicken Sie nach dem Anmelden auf das Profilbild rechts oben. Ihre Exchange-Absender-Adresse wird im sich öffnenden Pop-Up angezeigt.
1. **Notieren Sie sich diese Adresse.**

### 2. E-Mail-Konto in Apple Mail einrichten

**Falls Sie noch kein Konto in Apple Mail verbunden haben:** Fahren Sie mit Schritt 7 fort.

**Schritt 1:** Starten Sie die Mail-App auf Ihrem Mac und klicken Sie auf „Mail“ und dann auf „Einstellungen“.
**Schritt 2:** Klicken Sie im nachfolgenden Fenster auf den „Accounts“-Reiter und dann auf das „+“-Symbol.
**Schritt 3:** Wählen Sie „Anderer Mail-Account …“ und klicken Sie auf „Fortfahren“.
**Schritt 4:** Geben Sie den gewünschten Namen, Ihre **Exchange-Absender-Adresse** und das Passwort Ihrer Uni-ID ein. Klicken Sie auf „Anmelden“.

- *Hinweis:* Die Schritte 1–4 dienen der Erfassung der Exchange-Absender-Adresse.

**Schritt 5:** Es erscheint die Meldung, dass Accountname/Passwort nicht überprüft werden konnten. Dies ist normal.
**Schritt 6:** Geben Sie Ihren Accountnamen im Format **`AD\Uni-ID`** (Beispiel: `AD\memuster`) ein.
**Schritt 7:** Tragen Sie in die Felder für eintreffende & ausgehende E-Mails den Server **`exchange.uni-mannheim.de`** ein und klicken Sie auf „Anmelden“.

**Schritt 8:** Wählen Sie „Mail“ und ggf. „Notizen“ aus und klicken Sie auf „Fertig“.

### 3. Kalender in Apple Mail einbinden

Um Ihren Kalender einzubinden, führen Sie bitte die folgenden Schritte durch:

**Schritt 1:** Öffnen Sie die Kalender-App und klicken Sie links oben auf „Kalender“ und dort auf „Account hinzufügen …“.
**Schritt 2:** Wählen Sie „Microsoft Exchange“ und klicken Sie auf „Fortfahren“.
**Schritt 3:** Tragen Sie Ihren gewünschten Namen und Ihre Exchange-Adresse ein und klicken Sie auf „Anmelden“.
**Schritt 4:** Wählen Sie im nachfolgenden Fenster „Manuell konfigurieren“.
**Schritt 5:** Geben Sie das Passwort Ihrer Uni-ID ein und klicken Sie auf „Anmelden“.
**Schritt 6:** Es erscheint die Meldung, dass Accountname/Passwort nicht überprüft werden konnten. Dies ist normal. Bitte tragen Sie im Feld „Benutzername“ Ihre Uni-ID im Format **`AD\Uni-ID`** (Beispiel: `AD\memuster`) ein und klicken Sie auf „Anmelden“.
**Schritt 7:** Falls das nachfolgende Fenster erscheint, tragen Sie in den Feldern Interne- und Externe URL bitte **`https://exchange.uni-mannheim.de/EWS/Exchange.asmx`** ein und klicken Sie auf „Anmelden“.
**Schritt 8:** Wählen Sie im nächsten Fenster **„Kalender“**, „Erinnerungen“ und „Kontakte“ aus und klicken Sie auf „Fertig“.

> **Achtung:** Wählen Sie **NICHT** „Mail“ aus.

Ihr Kalender und an Sie freigegebene Kalender beginnen nun sich zu synchronisieren. Je nach Größe des Kalenders kann dies einige Zeit in Anspruch nehmen.
