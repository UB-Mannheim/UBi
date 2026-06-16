---
title: Exchange Postfach mit iOS Mail-App verbinden
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/einbinden-ios/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/adding-an-exchange-account-to-ios/
category: Services
tags: ['Exchange', 'iOS', 'Mail', 'Einrichtung', 'Uni-ID', 'Anleitung', 'Postfach']
language: de
---

# Exchange Postfach mit iOS Mail-App verbinden

Diese Anleitung beschreibt, wie Sie Ihr Exchange Postfach mit Ihrem iPhone oder iPad verbinden. **Wichtig:** Diese Schritte können erst angewendet werden, nachdem Ihr Exchange Postfach erfolgreich erstellt wurde.

## ℹ️ Wichtige Hinweise vorab

- **Ziel-App:** Die folgende Anleitung bezieht sich auf die **iOS Mail-App**, die auf den meisten iOS-Geräten vorinstalliert ist.
- **Alternative Apps:** Die gezeigten Schritte können analog für andere Mail-Apps (außer Outlook) auf Ihren iOS-Geräten angewendet werden.
- **Outlook-App:** Die Verknüpfung mit der offiziellen Outlook-App für iOS ist aus datenschutzrechtlichen Gründen nicht möglich.
- **Web-Zugriff:** Sie sind nicht auf eine Mail-App angewiesen. Ihr Exchange Postfach können Sie jederzeit über Ihren Webbrowser unter [https://exchange.uni-mannheim.de/owa](https://exchange.uni-mannheim.de/owa) aufrufen. Dort melden Sie sich mit Ihrer Uni-ID (= ehem. „Kennung“) und dem zugehörigen Passwort an, um auf E-Mails, Kalender und Adressbücher zuzugreifen.
- **IMAP-Alternative:** Falls Sie abweichend von dieser Anleitung IMAP verwenden möchten, finden Sie die Verbindungsdaten zum Server [hier](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/einbinden-android/#c259568).

## ⚙️ Schritt-für-Schritt-Anleitung (iOS Mail-App)

Folgen Sie diesen Schritten, um Ihr neue E-Mail-Konto in der iOS Mail-App einzurichten:

### 1. Exchange-Absender-Adresse ermitteln

1. Öffnen Sie Ihren Internetbrowser (z. B. Safari, Chrome oder FireFox) und rufen Sie [https://exchange.uni-mannheim.de](https://exchange.uni-mannheim.de) auf.
1. Geben Sie dort Ihre Uni-ID und das dazugehörige Passwort ein und klicken Sie auf „Anmelden“.
1. Klicken Sie im oberen Menü auf das Profilbild.
1. Notieren Sie sich die dort angezeigte **Exchange-Absender-Adresse**. Diese Adresse benötigen Sie für die Einrichtung.

### 2. Konto in die iOS Einstellungen einbinden

1. Öffnen Sie die App „Einstellungen“ auf Ihrem Smartphone oder Tablet.
1. Wählen Sie „Mail“ und anschließend „Accounts“.
1. Tippen Sie auf „Account hinzufügen“.
1. Wählen Sie „Microsoft Exchange“.
1. Geben Sie Ihren Namen und die zuvor notierte **Exchange-Absender-Adresse** ein. Wählen Sie eine gewünschte Beschreibung und tippen Sie auf „Weiter“.

### 3. Manuelle Konfiguration durchführen

1. Wählen Sie im nächsten Fenster die Option **„Manuell konfigurieren“**.
1. Geben Sie unter „Benutzername“ Ihre Uni-ID (= ehem. „Kennung“) ein, wobei Sie unbedingt ein vorangestelltes **`AD\`** verwenden. Geben Sie anschließend Ihr Passwort ein.
   > **⚠️ Achtung:** Achten Sie darauf, einen Backwards-Slash (`\`) und keinen Forwards-Slash (`/`) zu verwenden.
1. *Optional:* Bei manchen iOS-Versionen ist es notwendig, im Feld „Server“ den Eintrag `exchange.uni-mannheim.de` zu ergänzen.
1. Bestätigen Sie Ihre Eingabe mit „Weiter“.

### 4. Abschluss

1. Die Mail-App verbindet sich mit Ihrem neuen Postfach.
1. Es erscheint eine Auswahl, welche Apps mit dem neuen Exchange-Account verwendet werden sollen. Setzen Sie alle gewünschten Haken und klicken Sie auf „Fertig“.

______________________________________________________________________

**Hinweis zur Sicherheit:** Der Hinweis in den Eingabefeldern bezüglich der Verwaltung des Geräts per Fernzugriff ist irrelevant. Die Möglichkeit der Rücksetzung ist auf dem Exchange der Universität Mannheim **DEAKTIVIERT**. Die Universitäts-IT hat keinen Zugriff auf Ihre Smartphone-Daten.
