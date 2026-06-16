---
title: FileService Zugang einrichten – Netzlaufwerk unter Windows 11
source_url_de: https://www.uni-mannheim.de/it/anleitungen/fileservice-windows/
source_url_en: https://www.uni-mannheim.de/en/
category: Services
tags: ['FileService', 'Windows 11', 'Netzlaufwerk', 'Zugang', 'Uni-ID', 'Anleitung', 'Beschäftigte']
language: de
---

# FileService Zugang einrichten: Netzlaufwerk unter Windows 11

Mit dem FileService bieten wir für **Beschäftigte** der Universität Mannheim einen universitätsinternen Speicherplatz, der online weltweit für PCs und Laptops zugänglich ist.

**Wichtiger Hinweis:** Die Nutzung des File-Service ist im universitären Netz oder, bei Zugriff von außerhalb, mit einem VPN-Client möglich.

## Voraussetzungen und Support

**Sie benötigen:**

- Ihre [Uni-ID](https://www.uni-mannheim.de/it/anleitungen/uni-id/)
- Das dazugehörige Passwort

**Passwort vergessen?**
Bitte folgen Sie unserer Anleitung zur [Passwortrücksetzung](https://www.uni-mannheim.de/it/anleitungen/passwort/).

**Uni-ID oder Passwort vergessen?**
Wenden Sie sich bitte an unseren Support:

- **Telefon:** +49 621 181-2000
- **E-Mail:** itsupport@uni-mannheim.de

## So binden Sie einen Netzwerkordner unter Windows 11 als Laufwerk ein

Ordner im Netzwerk lassen sich unter Windows wie Laufwerke behandeln. Die Einbindung erfolgt in folgenden Schritten:

**Schritt 1:** Öffnen Sie den **Windows Datei-Explorer** und wählen Sie in der linken Navigationsspalte „Dieser PC“ aus.
**Schritt 2:** Klicken Sie oben in der Menüleiste auf die drei Punkte und dann auf „**Netzlaufwerk verbinden**“.
**Schritt 3:** Wählen Sie im Dropdown-Menü „Laufwerk“ den Laufwerksbuchstaben, unter dem das verbundene Netzlaufwerk im Explorer erscheinen soll.
**Schritt 4:** Tragen Sie im Feld „Ordner“ die Netzwerkadresse ein:
`\\nas.uni-mannheim.de\uni-shares`
Dies wird als Laufwerk unter Windows künftig verwendet.

**Schritt 5:** Bevor Sie das Netzlaufwerk verbinden, können Sie folgende Optionen auswählen:

- **„Verbindung bei Anmeldung wiederherstellen“:** Der Netzwerkordner wird auch beim nächsten Neustart versucht wiederherzustellen.
- **„Verbindung mit anderen Anmeldeinformationen herstellen“:** Diese Option ist wichtig, wenn auf dem Netzlaufwerk verschiedene Accounts mit unterschiedlichen Zugriffsrechten konfiguriert wurden.

Nachdem Sie die Optionen gewählt haben, klicken Sie auf „Fertig stellen“.

**Authentifizierung:**
Handelt es sich um eine passwortgeschützte Freigabe, werden Sie vorher nach einem Kennwort gefragt. Geben Sie hier Ihre Uni-ID mit einem zusätzlichen „ad\\“ am Anfang ein (`ad\Uni-ID`). Klicken Sie anschließend auf „OK“. Das Laufwerk steht Ihnen nun zur Verfügung.

## Wie trenne ich das Netzlaufwerk?

Wenn Sie ein Netzlaufwerk nicht mehr benötigen, klicken Sie mit der rechten Maustaste auf das entsprechende Laufwerk und wählen Sie „Trennen“.

______________________________________________________________________

[Alle Anleitungen auf einen Blick](https://www.uni-mannheim.de/it/anleitungen/)
