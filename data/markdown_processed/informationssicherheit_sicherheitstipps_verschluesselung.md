---
title: Leitfaden zur Datenverschlüsselung – Geräte, Dokumente und Kommunikation
source_url_de: https://www.uni-mannheim.de/informationssicherheit/sicherheitstipps/verschluesselung/
source_url_en: https://www.uni-mannheim.de/en/information-security/security-tips/encryption/
category: Services
tags: ['Verschlüsselung', 'Datenschutz', 'Bitlocker', 'FileVault', 'Cryptomator', 'S/MIME', 'Passwort']
language: de
---

# Verschlüsselung: Schutz Ihrer Daten

Diese Seite erklärt, warum und wie Sie verschiedene Arten von Daten – von Computern über externe Speichermedien bis hin zu E-Mails und Cloud-Diensten – verschlüsseln können.

## 💻 Verschlüsselung von Geräten und Speichermedien

### Computer

**Warum verschlüsseln?**
Wenn Ihr Computer gestohlen oder verloren geht, kann durch Ausbauen der Festplatte auf alle Daten zugegriffen werden. Eine Verschlüsselung schützt die Festplatte vor fremdem Zugriff.

- **Apple Geräte:** Nutzen Sie FileVault. [FileVault Anleitung](https://www.uni-mannheim.de/it/anleitungen/filevault/)
- **Windows:** Hierfür eignet sich Bitlocker. [Bitlocker Anleitung](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-bitlocker/)
- **Linux:** Aufgrund der Vielfalt an Distributionen gibt es keine einheitliche Anleitung. Bitte erkundigen Sie sich bei Ihrer Distribution.

**Hinweis für Universitäts-IT-Bestellungen:**
Wenn Sie einen Computer über die Universitäts-IT bestellen und/oder einrichten lassen, wird die Festplatte durch die Beschäftigten der Universitäts-IT verschlüsselt (seit November 2022).

- [Mehr Infos zur Verschlüsselung](https://www.uni-mannheim.de/it/services/arbeitsplatz/digitaler-arbeitsplatz/verschluesselung/)
- **Überprüfung:** Sie können in den Einstellungen unter „Datenschutz und Sicherheit/BitLocker-verwalten“ prüfen, ob Ihre Festplatten verschlüsselt sind und BitLocker aktivieren.

### Externe Speichermedien (USB-Sticks, SD-Karten, Festplatten)

**Warum verschlüsseln?**
Diese Medien können leicht verloren gehen oder gestohlen werden. Zudem können bei den meisten externen Speichermedien Daten nicht zu 100% gelöscht werden.

- **Gesamtes Speichermedium verschlüsseln:** Nutzen Sie **VeraCrypt**. Beachten Sie, dass Administrator-Rechte für Installation und Verschlüsselung notwendig sind. [Anleitung VeraCrypt](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-veracrypt/)
- **Erweiterbarer verschlüsselter Ordner:** Mit **Cryptomator** können Sie einen verschlüsselten Ordner anlegen, der jederzeit erweitert, ergänzt oder bearbeitet werden kann. [Anleitung Cryptomator](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-cryptomator/)
- **Einzelne Dateien/Ordner:** Für Dateien oder Ordner, die nicht mehr bearbeitet werden müssen, eignet sich ein verschlüsseltes **ZIP-Archiv**. Folgen Sie der [Anleitung](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-verschluesseltes-zip-archiv/) und kopieren Sie das Archiv auf das Speichermedium.

## 📧 Verschlüsselung der Kommunikation

### E-Mails

**Warum verschlüsseln?**
Das Versenden einer E-Mail ist wie das Versenden einer Postkarte; der Inhalt ist für Dritte leicht lesbar.

- **S/MIME-Verschlüsselung:** E-Mails können sicher über S/MIME übertragen werden. Hierfür benötigen Sie ein digitales Zertifikat, das mit einem Passwort verbunden ist und langfristig gespeichert werden muss.

  - Antragsformular und weitere Informationen zum Zertifikat finden Sie [hier](https://www.uni-mannheim.de/it/services/digitale-zertifikate).

- **Anhänge schützen (ohne S/MIME):** Einzelne Anhänge können mit einem verschlüsselten **ZIP-Archiv** geschützt werden. **Wichtig:** Übermitteln Sie das Passwort des ZIP-Archivs niemals per E-Mail, sondern auf einem anderen Weg (z. B. persönlich, telefonisch oder per Brief).

### Office Dokumente

**Einzelne Dokumente (Word, Excel etc.):**
Dokumente können mit dem integrierten Dokumentenschutz mittels eines Passworts verschlüsselt werden.

- [Detaillierte Anleitung](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-office-dokumentenverschluesselung/)
- **Wichtig:** Übermitteln Sie das Passwort des Dokuments niemals per E-Mail, sondern auf einem anderen Weg.
- *Zusatz:* Zu diesem Thema wird regelmäßig eine Schulung angeboten. [Schulungsübersicht](https://www.uni-mannheim.de/informationssicherheit/schulungen/)

## ☁️ Verschlüsselung in der Cloud und im Netzwerk

### Netzlaufwerke der Universität Mannheim (NAS)

Netzlaufwerke sind zwar bequeme Speicherorte, aber es ist unklar, wer Zugriff auf die Daten hat.

- **Erweiterbarer Ordner:** Nutzen Sie **Cryptomator**, um einen verschlüsselten Ordner auf dem NAS abzulegen. [Anleitung Cryptomator](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-cryptomator/)
- **Einzelne Ordner/Dateien:** Schützen Sie diese mit einem verschlüsselten **ZIP-Archiv**. Ein solches Archiv kann jedoch nicht mehr erweitert werden; speichern Sie daher idealerweise nur abgeschlossene Dateien.

### Cloud-Dienste (Microsoft 365, OneDrive, etc.)

**Microsoft-Cloud (OneDrive, Teams, OneNote):**
Die Nutzung von Office 365 ist Standard. Beim Umgang mit Daten ist der sorgsame Umgang zwingend notwendig (z. B. dürfen nur Verwaltungsdaten vom Typ TLP white abgelegt werden).

- [Nutzerrichtlinien M365 Cloud Services](https://www.uni-mannheim.de/it/nutzungsbedingungen/richtlinien-m-365-cloud-services/)
- **Erweiterbarer Ordner:** Sie können einen verschlüsselten Ordner mit **Cryptomator** in der Cloud ablegen. Bei der Nutzung eines gemeinsamen Ordners ist es nicht möglich, zeitgleich an den Dateien zu arbeiten. [Anleitung Cryptomator](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-cryptomator/)
- **Einzelne Dateien:** Schützen Sie diese mit einem verschlüsselten **ZIP-Archiv**.

**Andere Cloud-Dienste (iCloud, Dropbox, GoogleDrive):**
Das Informationssicherheitsteam rät von der dienstlichen Nutzung solcher Dienste ab, da die Datenverarbeitung und der Zugriff durch die Anbieter nicht transparent sind.

### Allgemeine Kommunikation und Netzwerke

- **Webseiten:** Achten Sie beim Surfen auf das Schloss-Symbol im Adressfeld, um zu prüfen, ob die Kommunikation verschlüsselt ist.
- **Messenger Dienste:** Achten Sie auf **Ende-zu-Ende-Verschlüsselung** und darauf, dass der Dienst **Open-Source** ist. Für den dienstlichen Gebrauch wird die Nutzung solcher Messenger Dienste jedoch abgeraten.
- **WLAN:** Nutzen Sie bei der Nutzung von WLAN (insbesondere fremde oder öffentliche Netze) ausschließlich verschlüsselte Verbindungen wie HTTPS. Aktivieren Sie bei der Verarbeitung universitätsinterner Informationen in solchen Netzen zwingend die [VPN-Verbindung](https://www.uni-mannheim.de/it/anleitungen/vpn/) zur Universität.

## 🧠 Grundlagen der Verschlüsselung

### Arten der Verschlüsselung

- **Symmetrische Verschlüsselung:** Es wird ein einziger Schlüssel sowohl zum Ver- als auch zum Entschlüsseln verwendet. Das Hauptproblem ist die sichere Übertragung dieses Schlüssels.
- **Asymmetrische Verschlüsselung:** Es werden zwei Schlüssel verwendet: ein öffentlicher und ein privater Schlüssel. Der Klartext wird mit dem öffentlichen Schlüssel verschlüsselt und kann nur mit dem privaten Schlüssel des Empfängers entschlüsselt werden.

### Zusammenfassung der Tools

| Szenario | Empfohlenes Tool | Hinweise |
| :--- | :--- | :--- |
| **Computer/Festplatte** | FileVault (Apple), Bitlocker (Windows) | Wird bei IT-Bestellung standardmäßig aktiviert. |
| **Speichermedium (Gesamt)** | VeraCrypt | Erfordert Administrator-Rechte. |
| **Ordner (Flexibel)** | Cryptomator | Ideal für Cloud oder NAS, da jederzeit erweitert werden kann. |
| **Dateien/Anhänge (Statisch)** | ZIP-Archiv (verschlüsselt) | Gut für abgeschlossene Dateien. Passwort separat übermitteln! |
| **E-Mails** | S/MIME | Erfordert ein digitales Zertifikat. |
