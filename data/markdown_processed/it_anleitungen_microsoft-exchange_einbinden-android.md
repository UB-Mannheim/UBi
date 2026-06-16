---
title: Exchange Postfach mit Android-Geräten verbinden
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/einbinden-android/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/adding-an-exchange-account-to-android-devices/
category: Services
tags: ['Exchange', 'Android', 'Postfach', 'Einrichtung', 'Uni-ID', 'G@App', 'IMAP', 'Outlook']
language: de
---

# Exchange Postfach mit Android-Geräten verbinden

Diese Anleitung erklärt, wie Sie Ihr Exchange Postfach mit Ihrem Android Smartphone oder Tablet verbinden.

**Wichtige Hinweise vorab:**

- Diese Anleitung kann erst angewendet werden, nachdem Ihr Exchange Postfach erstellt wurde.
- Die folgenden Schritte beziehen sich auf die **G@App**, die auf den meisten Android-Geräten vorinstalliert ist. Die Schritte können jedoch analog für andere Mail-Apps (außer Outlook) angewendet werden.
- Die Verknüpfung mit der offiziellen Outlook-App für Android ist aus datenschutzrechtlichen Gründen nicht möglich.
- **Alternative:** Sie können Ihr Exchange Postfach auch über Ihren Webbrowser unter [https://exchange.uni-mannheim.de/owa](https://exchange.uni-mannheim.de/owa) aufrufen. Dort melden Sie sich mit Ihrer Uni-ID und dem zugehörigen Passwort an und greifen auf E-Mails, Kalender und Adressbücher zu.
- Falls Sie abweichend von dieser Anleitung IMAP verwenden möchten, finden Sie die notwendigen Verbindungsdaten am Ende des Dokuments.

## Schritt-für-Schritt-Anleitung (Empfohlen: Exchange-Protokoll)

Folgen Sie diesen Schritten, um Ihr Postfach in der G@App einzurichten:

### 1. Exchange-Absender-Adresse ermitteln

1. Öffnen Sie Ihren Internetbrowser (z. B. Chrome oder FireFox) und rufen Sie [https://exchange.uni-mannheim.de](https://exchange.uni-mannheim.de) auf.
1. Geben Sie Ihre Uni-ID und das Passwort ein und klicken Sie auf „Anmelden“.
1. Klicken Sie links oben auf das Menü.
1. Ihre Exchange-Absender-Adresse wird oben angezeigt.
   - *Tipp:* Falls die Adresse nicht vollständig einsehbar ist, besuchen Sie [https://exchange.uni-mannheim.de](https://exchange.uni-mannheim.de) auf Ihrem Rechner/Laptop/Macbook, loggen Sie sich ein und klicken Sie rechts oben auf das Profilbild, um die vollständige Adresse zu sehen.
1. **Notieren Sie sich diese Adresse** – dies ist die Exchange-Absender-Adresse, die Sie für die Einrichtung benötigen.

### 2. G@App einrichten

1. Öffnen Sie die G@App.
1. Tippen Sie auf das Menüsymbol in der oberen linken Ecke.
1. Tippen Sie auf **Einstellungen**.
1. Tippen Sie auf **„Konto hinzufügen“**.
1. Wählen Sie im Menü **„Exchange und Office 365“** aus.
1. Geben Sie Ihre notierte Exchange-Absender-Adresse ein und tippen Sie auf **„Manuell einrichten“**.

### 3. Verbindungsdaten eintragen

Tragen Sie die folgenden Werte in das folgende Fenster ein und tippen Sie danach auf „Weiter“:

- **Passwort:** Das Passwort Ihrer Uni-ID
- **Domain\\Nutzer\*innenname:** `ad\Uni-ID`
- **Server:** `exchange.uni-mannheim.de`
- **Port:** `443`
- **Sicherheitstyp:** `SSL/TLS`

Ihr Postfach ist nun eingerichtet.

**Optional:** Standardmäßig werden E-Mails der letzten Woche synchronisiert. Um diesen Zeitraum zu verlängern, gehen Sie in die Einstellungen, wählen Sie Ihr neues Postfach aus und wählen Sie unter dem Punkt „E-Mails synchronisieren ab“ einen längeren Zeitraum aus.

## IMAP Kontoeinstellungen (Alternative)

Wir empfehlen dringend die Verwendung des **Exchange**-Protokolls. Sollten Sie jedoch eine Verbindung über IMAP herstellen wollen, verwenden Sie bitte die folgenden Verbindungsdaten:

### IMAP (Posteingang)

| Protokoll | IMAP |
| :--- | :--- |
| **Server** | `exchange.uni-mannheim.de` |
| **Port** | `993` |
| **Sicherheitstyp/Verschlüsselung** | `SSL/TLS` |
| **Benutzername** | `Uni-ID` |
| **Passwort** | Passwort Ihrer Uni-ID |

### SMTP (Postausgang)

| Parameter | Wert |
| :--- | :--- |
| **Server** | `exchange.uni-mannheim.de` |
| **Port** | `587` |
| **Sicherheitstyp/Verschlüsselung** | `STARTTLS` |
| **Authentifizierung erforderlich** | Ja |
| **Benutzername** | `Uni-ID` |
| **Passwort** | Passwort Ihrer Uni-ID |
