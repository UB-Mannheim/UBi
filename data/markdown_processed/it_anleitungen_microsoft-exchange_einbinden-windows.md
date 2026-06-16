---
title: Anleitung – Exchange Postfach mit Windows-Clients verbinden
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/einbinden-windows/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/adding-an-exchange-account-to-windows/
category: Benutzung
tags: ['Exchange', 'Outlook', 'Thunderbird', 'Postfach', 'Einrichtung', 'Uni-ID', 'Verbindung', 'E-Mail-Client']
language: de
---

# Anleitung: Ihr Exchange Postfach mit einem Desktop-Client verbinden

Diese Anleitung zeigt Ihnen, wie Sie Ihr Exchange Postfach mit einem E-Mail-Programm auf Ihrem Windows-Gerät verbinden.

**Wichtiger Hinweis:** Diese Anleitungen können erst angewendet werden, nachdem Ihr Exchange Postfach erfolgreich erstellt wurde.

### 💡 Empfehlung der Universitäts-IT

Wir empfehlen dringend die Verwendung von **Microsoft Outlook** als E-Mail-Client. Nur so können Sie alle Funktionen Ihres Exchange Postfachs (wie Kalender oder Adressbücher) vollumfänglich nutzen.

Alternative Clients (wie Thunderbird) können sich nur mit eingeschränktem Funktionsumfang verbinden und benötigen Add-ons, deren Aktualität und zukünftige Funktionalität nicht garantiert werden. Aus diesem Grund bietet die Universitäts-IT den vollständigen Support nur für Outlook an.

Alternativ können Sie Ihr Postfach jederzeit über einen Webbrowser unter [https://exchange.uni-mannheim.de](https://exchange.uni-mannheim.de) aufrufen. Die Anmeldung erfolgt einfach mit Ihrer Uni-ID und dem dazugehörigen Passwort.

______________________________________________________________________

## ⚙️ Vorbereitung: Initialer Setup (Für alle Clients)

Bevor Sie Ihren E-Mail-Client einrichten, müssen Sie folgende Schritte einmalig durchführen:

### 1. Autodiscovery RegKey setzen

Laden Sie die Datei „Outlook Autodiscovery RegKey setzen.bat“ herunter:
[Download Outlook Autodiscovery RegKey setzen.bat](https://www.uni-mannheim.de/media/Einrichtungen/it/Anleitungen/Exchange/Outlook_Autodiscovery_RegKey/Outlook_Autodiscovery_RegKey_setzen.bat)

Führen Sie die Datei mit einem Doppelklick aus.

- *Hinweis:* Sollte die Datei von Windows Defender oder einer anderen Antiviren-Software blockiert werden, lassen Sie diese bitte zu.
- *Hinweis:* Falls sich ein schwarzes Konsolenfenster öffnet, tippen Sie „j“ ein und bestätigen Sie die Eingabe mit der Enter-Taste.

### 2. Exchange-Absenderadresse ermitteln

1. Öffnen Sie Ihren Internetbrowser (z. B. FireFox oder Chrome) und rufen Sie [https://exchange.uni-mannheim.de](https://exchange.uni-mannheim.de) auf.
1. Geben Sie dort Ihre Uni-ID und das dazugehörige Passwort ein und klicken Sie auf den „Anmelden“-Button.
1. Klicken Sie nach der Anmeldung auf das Profilbild rechts oben. Ihre **Exchange-Absender\*innen-Adresse** wird im sich öffnenden Pop-Up angezeigt.
1. **Bitte notieren Sie sich diese Adresse**, da sie für die Einrichtung in Ihrem E-Mail-Client zwingend erforderlich ist.

______________________________________________________________________

## 📧 Anleitung für Microsoft Outlook (365, 2019, 2016)

Die Schritte zur Einrichtung sind für alle modernen Outlook-Versionen (365, 2019, 2016) nahezu identisch.

### 🚀 Einrichtungsschritte

1. **Starten Sie Outlook** auf Ihrem Rechner. (Falls dies Ihr erster Start ist, werden Sie automatisch zum Verbinden eines Kontos aufgefordert. Andernfalls klicken Sie auf den Reiter „Datei“).
1. Klicken Sie auf den „+ Konto hinzufügen“-Button.
1. Geben Sie nun Ihre Exchange-E-Mail-Adresse ein. (Siehe dazu oben, bei den initialen Schritten die Schritte 2.2 und 2.3).
1. Wählen Sie im nachfolgenden Fenster **„Exchange“** aus.
1. Im Login-Fenster gehen Sie wie folgt vor:
   - Öffnen Sie „Weitere Optionen“ $\\rightarrow$ „Anderes Konto verwenden“.
   - Geben Sie nun Ihre Uni-ID (=ehem. „Kennung“) mit einem vorangestellten **„ad\\“** und Ihr Passwort ein.
   - *Achtung:* Verwenden Sie den Backslash „\\“, nicht den Schrägstrich „/“.
   - Setzen Sie den Haken bei „Anmeldedaten speichern“ und klicken Sie auf „OK“.
1. Falls ein weiteres Popup erscheint, bestätigen Sie dieses mit einem Klick auf „OK“.
1. **Cache-Modus (Wichtig):**
   - *Outlook 365:* Belassen Sie „Verwenden Sie den Exchange-Cache-Modus“ angewählt, das Herunterladen bei „1 Jahr“ und klicken Sie anschließend auf „Weiter“.
   - *Outlook 2019/2016:* Folgen Sie den Anweisungen des Popups.
1. Bestätigen Sie das nachfolgende Fenster mit einem Klick auf „Vorgang abgeschlossen“ (oder „Fertig stellen“).
1. *Optional:* Stimmen Sie der Aufforderung zu, die Seite `exchange.uni-mannheim.de/owa` Einstellungen an Ihrem Konto vornehmen zu lassen.
1. **Beenden Sie Outlook und starten Sie es neu.** Ihr Postfach wird synchronisiert und ist nun erfolgreich eingebunden.

______________________________________________________________________

## 🐦 Anleitung für Thunderbird

**⚠️ Wichtiger Hinweis:** Thunderbird ist nicht für die volle Funktionalität von Exchange optimiert. Die Universitäts-IT bietet hierfür keinen Support an. Wir empfehlen dringend die Nutzung von Outlook oder dem Web-Client.

### 1. E-Mail-Postfach einrichten

1. **Web-Login:** Folgen Sie den Schritten 2.2 und 2.3, um Ihre Exchange-Absenderadresse zu ermitteln.
1. **Thunderbird starten:** Starten Sie Thunderbird und klicken Sie rechts oben auf das Anwendungsmenü $\\rightarrow$ „Neu“ $\\rightarrow$ „Bestehendes E-Mail-Konto…“.
1. Geben Sie Ihren Namen, Ihre **Exchange-Absender*innen-Adresse*** und das Passwort Ihrer Uni-ID ein. Klicken Sie auf den „Manuell einrichten…“-Button.
1. Tragen Sie die folgenden Werte ein:

| Einstellung | Wert |
| :--- | :--- |
| **Posteingangs-Server** | |
| Protokoll | IMAP |
| Server | `exchange.uni-mannheim.de` |
| Port | 993 |
| SSL | SSL/TLS |
| Authentifizierung | Passwort, normal |
| Benutzername | Uni-ID |
| **Postausgangs-Server** | |
| Server | `exchange.uni-mannheim.de` |
| Port | 587 |
| SSL | STARTTLS |
| Authentifizierung | Passwort, normal |
| Benutzername | Uni-ID |

5. Klicken Sie auf „Fertig“. Thunderbird verbindet sich und synchronisiert Ihre E-Mails.

### 2. Systemordner umstellen (Wichtig)

Um sicherzustellen, dass die Ordnerstruktur in Thunderbird mit dem Web-Client (OWA) übereinstimmt, müssen Sie die Systemordner manuell umstellen.

1. **Ordner synchronisieren:** Klicken Sie mit der rechten Maustaste auf Ihr E@Konto und wählen „Abonnieren…“.
1. Klicken Sie auf „Aktualisieren“ (1), setzen Sie die Häkchen bei allen gewünschten Ordnern (2) und klicken Sie auf „Abonnieren“ (3) und „OK“ (4).
1. **Einstellungen anpassen:** Klicken Sie erneut mit der rechten Maustaste auf Ihr E@Konto und wählen „Einstellungen“.
1. Gehen Sie zu „Kopien & Ordner“ (1). Aktivieren Sie unter „Beim Senden von Nachrichten automatisch“ die Option „Anderer Ordner“ (2). Wählen Sie im Dropdown-Menü (3) den Ordner „Gesendete Elemente“ (4) aus.

### 3. Kalender und Kontakte synchronisieren (Add-ons)

Für die Synchronisierung von Kalender und Kontakten müssen Sie zwei Add-ons installieren und einrichten:

1. **Add-ons installieren:**
   - Klicken Sie rechts oben auf das Anwendungsmenü $\\rightarrow$ „Add-ons“.
   - Suchen Sie nach „tbsync“ und fügen Sie das Add-on **„TbSync“** hinzu.
   - Wiederholen Sie den Vorgang für das Add-on **„Provider für Exchange ActiveSync“**.
1. **Konto einrichten:**
   - Klicken Sie unten rechts auf „TbSync: Leerlauf“.
   - Wählen Sie „Konto Aktionen“ $\\rightarrow$ „Neues Konto hinzufügen“ $\\rightarrow$ „Exchange-ActiveSync“.
   - Wählen Sie „Benutzerspezifische Konfiguration“ und tragen Sie Ihre Daten ein.
   - Im Feld „Benutzername (E-Mail Adresse)“ tragen Sie **`ad\Uni-ID`** ein (z. B. `ad\mamuster`).
   - Setzen Sie den Haken bei „Konto aktivieren und synchronisieren“.
   - Wählen Sie im Auswahlmenü die Häkchen bei **„Kontakte“** und **„Kalender“**.
   - Setzen Sie eine periodische Synchronisation (mindestens 5 Minuten) und klicken Sie auf „Jetzt synchronisieren“.

______________________________________________________________________

## ⚠️ Hinweise und Fehlerbehebung

### Einschränkungen des IMAP-Protokolls

Bitte beachten Sie, dass Thunderbird über das IMAP-Protokoll nur in eingeschränktem Funktionsumfang mit Ihrem Exchange Postfach verbinden kann. Im Gegensatz zu Outlook und dem Web-Client werden nicht alle E-Mail-Ordner automatisch in der korrekten Struktur synchronisiert und angelegt.

### Fehlerbehebung beim Synchronisieren

Falls es zu Fehlermeldungen beim Synchronisieren kommt:

1. Vergewissern Sie sich, dass Thunderbird im Onlinemodus ist.
1. Überprüfen Sie Ihre Konto-Eingaben, indem Sie den Haken bei „Konto aktivieren und synchronisieren“ entfernen und dann auf den Reiter „Kontoeinstellungen“ wechseln.
