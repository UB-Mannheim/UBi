---
title: Exchange Postfach mit Thunderbird auf Linux einbinden
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/einbinden-linux/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/adding-an-exchange-account-to-linux/
category: Benutzung
tags: ['Thunderbird', 'Exchange', 'Linux', 'IMAP', 'Postfach', 'Einbindung', 'Uni-ID', 'ActiveSync']
language: de
---

# Anleitung: Exchange Postfach mit Thunderbird auf Linux einbinden

Diese Anleitungen zeigen Ihnen, wie Sie Ihre Linux-Geräte mit Ihrem Exchange Postfach verbinden. **Bitte beachten Sie:** Diese Anleitungen können erst angewendet werden, nachdem Ihr Exchange Postfach erstellt wurde.

## ⚠️ Wichtige Hinweise und Disclaimer

Bevor Sie beginnen, beachten Sie bitte folgende Einschränkungen:

- **Empfehlung:** Die Universitäts-IT empfiehlt ausdrücklich die Nutzung der **Outlook-Clients** für Windows/Mac oder des [Outlook Web-Clients](https://exchange.uni-mannheim.de/owa) für die Nutzung Ihres Exchange Postfachs.
- **Synchronisierung (Kalender/Kontakte):** Die dauerhafte Funktionalität der Synchronisierung von Kalender und Kontakten ist von den jeweiligen Add-ons abhängig. Die UNIT bietet hierfür keinen Support an.
- **Funktionsumfang (IMAP):** Thunderbird verbindet sich über das IMAP-Protokoll nur in einem eingeschränkten Funktionsumfang mit Ihrem Exchange Postfach. Nicht alle E-Mail-Ordner werden automatisch in derselben Struktur wie im Exchange Postfach synchronisiert und angelegt. Das Ordner-Mapping muss daher manuell vorgenommen werden.

## 📧 1. E-Mail-Konto mit Thunderbird verbinden

### Vorbereitung: Exchange-Absender-Adresse ermitteln

1. Öffnen Sie Ihren Internetbrowser (z. B. FireFox oder Chrome) und rufen Sie [https://exchange.uni-mannheim.de](https://exchange.uni-mannheim.de) auf.
1. Geben Sie dort Ihre Uni-ID und das dazugehörige Passwort ein und klicken Sie auf den „Anmelden“-Button.
1. Klicken Sie nach der Anmeldung auf das Profilbild rechts oben. Ihre Exchange-Absender-Adresse wird im sich öffnenden Pop-Up angezeigt.
1. **Notieren Sie sich diese Adresse** – dies ist die Exchange-Absender-Adresse, die Sie für die Einrichtung benötigen.

### Einrichtung in Thunderbird

1. Starten Sie Thunderbird und klicken Sie rechts oben auf das Anwendungsmenü und wählen Sie die Option „Neu“. Wählen Sie anschließend „Bestehendes E-Mail-Konto…“.
1. Geben Sie Ihren Namen, Ihre **Exchange-Absender-Adresse** und das Passwort Ihrer Uni-ID ein. Klicken Sie auf den „Manuell einrichten…“-Button.
1. Tragen Sie in die folgenden Felder die Werte ein und klicken Sie auf „Fertig“.

**Konfigurationsdetails:**

| Einstellung | Posteingangs-Server | Postausgangs-Server |
| :--- | :--- | :--- |
| **Protokoll** | IMAP | (N/A) |
| **Server** | `exchange.uni-mannheim.de` | `exchange.uni-mannheim.de` |
| **Port** | 993 | 587 |
| **SSL** | SSL/TLS | STARTTLS |
| **Authentifizierung** | Passwort, normal | Passwort, normal |
| **Benutzername** | Uni-ID | Uni-ID |

Nach der Eingabe verbindet sich Thunderbird mit Ihrem neuen Postfach und synchronisiert Ihre E-Mails.

## 📂 2. Systemordner in Thunderbird umstellen (Mapping)

Um sicherzustellen, dass sowohl über den E-Mail-Client als auch über das OWA die gleichen Ordner verwendet werden, müssen Sie die Systemordner in Thunderbird identisch mit den Ordnern des Microsoft Exchange OWA einrichten.

**Schritte zur Umstellung:**

1. **Ordner sichtbar machen:** Klicken Sie mit der rechten Maustaste auf Ihr E@Konto und wählen Sie „Abonnieren…“.
1. Klicken Sie auf „Aktualisieren“ (1), um die aktuelle Ordnerliste des Exchange zu empfangen. Setzen Sie die Haken bei allen Ordnern, die künftig in Thunderbird angezeigt werden sollen (2). Klicken Sie anschließend auf „Abonnieren“ (3) und abschließend auf „OK“ (4).
1. **Einstellungen anpassen:** Klicken Sie erneut mit der rechten Maustaste auf Ihr E@Konto und wählen Sie „Einstellungen“.
1. **Gesendete Elemente (Beispiel):** Im linken Menü wählen Sie „Kopien & Ordner“ (1). Im mittleren Bereich aktivieren Sie unter „Beim Senden von Nachrichten automatisch“ die Option „Anderer Ordner“ (2). Klicken Sie auf den Dropdown-Pfeil (3) und wählen Sie unter Ihrem E@Account (**NICHT** „Lokaler Ordner“) den Ordner „Gesendete Elemente“ (4).

*Nach einem Neustart von Thunderbird sollten die Systemordner nun korrekt angezeigt werden.*

## 📅 3. Kalender und Kontakte synchronisieren

Um Kalender und Kontakte zu synchronisieren, müssen Sie zwei spezifische Add-ons installieren und einrichten.

**Installation der Add-ons:**

1. Klicken Sie rechts oben im Anwendungsmenü auf „Add-ons“.
1. Geben Sie in die Suchleiste „tbsync“ ein und bestätigen Sie die Eingabe.
1. Im Suchergebnis klicken Sie beim Addon **„TbSync“** auf den „Zu Thunderbird hinzufügen“-Button und wiederholen Sie dies für das Addon **„Provider für Exchange ActiveSync“**.
1. Schließen Sie die Addon-Tabs und wechseln Sie zurück ins Hauptfenster von Thunderbird.

**Einrichtung des Kontos:**

1. Klicken Sie unten rechts auf „TbSync: Leerlauf“.
1. Wählen Sie in der Kontoverwaltung links unten: „Konto Aktionen“ > „Neues Konto hinzufügen“ > „Exchange-ActiveSync“.
1. Wählen Sie „Benutzerspezifische Konfiguration“ und tragen Sie Ihre Daten ein. Im Feld „Benutzername (E-Mail Adresse)“ tragen Sie `Ihread\Uni-ID` ein (z. B. `ad\mamuster`). Klicken Sie auf „Konto hinzufügen“.
1. Das Konto wird übernommen. Setzen Sie den Haken bei „Konto aktivieren und synchronisieren“.
1. Wählen Sie im Auswahlmenü die gewünschten Elemente: Setzen Sie die Häkchen bei **„Kontakte“** und bei **„Kalender“**.
1. Setzen Sie eine periodische Synchronisation (mindestens ≥ 5 Minuten) und klicken Sie auf „Jetzt synchronisieren“.

*Wenn neben Ihrem Kontonamen ein grünes Häkchen erscheint, wurde alles erfolgreich synchronisiert. Sie können nun auf Ihren Kalender und Ihre Kontakte zugreifen.*

______________________________________________________________________

## 🛠️ Hinweise und Fehlerbehebung

### Fehlerbehebung beim Synchronisieren

Falls es zu Fehlermeldungen beim Synchronisieren kommt:

- **Online-Modus prüfen:** Vergewissern Sie sich, dass Thunderbird im Onlinemodus ist. Falls nicht, klicken Sie auf den entsprechenden Button unten links.
- **Kontoeingaben prüfen:** Falls das Problem weiterhin besteht, entfernen Sie den Haken bei „Konto aktivieren und synchronisieren“ und wechseln Sie dann auf den Reiter „Kontoeinstellungen“, um Ihre Konto-Eingaben zu überprüfen.

### Globales Adressbuch

Um in den globalen Adressbüchern der Universität Kontakte zu suchen, wechseln Sie in Thunderbird auf das Adressbuch, markieren Sie Ihr neues Exchange Konto mit einem Klick darauf und suchen Sie anschließend im Suchfeld oben rechts nach den Kontakten.
