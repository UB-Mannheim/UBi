---
title: VPN-Client Installation und Nutzung an der Universität Mannheim
source_url_de: https://www.uni-mannheim.de/it/anleitungen/vpn/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/vpn/
category: Services
tags: ['VPN', 'Installation', 'Windows', 'macOS', 'Android', 'iOS', 'Fernzugriff', 'Uni Mannheim']
language: de
---

# VPN-Client: Anleitung zur Einrichtung und Nutzung

Einige wichtige Dienste der Universität Mannheim, wie Bibliotheksdatenbanken oder der FileService, sind nur über eine gesicherte Verbindung auf dem Campus zugänglich. Für den Zugriff von zu Hause oder unterwegs ist daher eine VPN-Verbindung zur Universität erforderlich.

## 🧑‍💻 Wer kann den VPN-Client nutzen?

Der VPN-Client steht ausschließlich folgenden Gruppen zur Verfügung:

- Beschäftigte der Universität Mannheim
- Immatrikulierte Promovierende
- Studierende (inkl. Senior- und Gaststudierenden)
- Privatdozent\*innen der Universität Mannheim

## 🌐 VPN-Profile: WebVPN vs. WebVPN-Split

Beim Aufbau der Verbindung werden Ihnen zwei Profile zur Auswahl gestellt. Die Wahl des Profils bestimmt, welche Daten über den VPN-Tunnel geleitet werden.

| Profil | Beschreibung | Nutzungsempfehlung | Einschränkungen |
| :--- | :--- | :--- | :--- |
| **WebVPN** | Der komplette Internetverkehr wird durch den VPN-Tunnel geleitet (Standardprofil). | **Muss** verwendet werden, wenn Sie auf Online-Bibliotheksdatenbanken zugreifen müssen. | Der gesamte Internetverkehr wird durch den Tunnel geleitet. |
| **WebVPN-Split** | Nur der Datenverkehr zur Universität Mannheim wird durch den VPN-Tunnel geleitet. | Empfohlen für Mitarbeitende der Universität, da die Verbindung vergleichsweise schneller ist. | Kein Zugriff auf Online-Bibliotheksdatenbanken möglich. |

______________________________________________________________________

## 📱 Installation nach Betriebssystem

### 🖥️ Windows

1. **Start:** Öffnen Sie einen Webbrowser und rufen Sie [https://vpn.uni-mannheim.de/](https://vpn.uni-mannheim.de/) auf.
1. **Login:** Melden Sie sich mit Ihrer Uni-ID und dem zugehörigen Passwort an. *Hinweis: Falls Sie ein WLAN/VPN-Passwort anstelle Ihres Passworts gesetzt haben, verwenden Sie dieses.*
1. **Passwort vergessen?** Nutzen Sie die [Anleitung zur Passwortrücksetzung](https://www.uni-mannheim.de/it/anleitungen/passwort/).
1. **Support:** Bei Problemen mit Uni-ID oder Passwort wenden Sie sich an den Support:
   - Telefon: +49 621 181-2000
   - E-Mail: itsupport@uni-mannheim.de
1. **Download:** Klicken Sie auf „Download for Windows“.
1. **Installation:** Führen Sie die heruntergeladene Datei aus. Folgen Sie dem Installationsprozess, stimmen Sie der Lizenzvereinbarung zu und klicken Sie auf „Install“ und anschließend auf „Finish“.
1. **Verbindung herstellen:** Führen Sie den Cisco-Anyconnect-Secure-Mobility-Client aus.
1. **Setup:** Tragen Sie in das Feld `vpn.uni-mannheim.de` ein und klicken Sie auf „Connect“.
1. **Verbindung:** Wählen Sie das passende Profil (WebVPN oder WebVPN-Split) und drücken Sie auf „Ok“.

### 🍎 macOS

1. **Start:** Öffnen Sie einen Webbrowser und rufen Sie [https://vpn.uni-mannheim.de](https://vpn.uni-mannheim.de) auf.
1. **Login:** Melden Sie sich mit Ihrer Uni-ID und dem zugehörigen Passwort an. *Hinweis: Falls Sie ein WLAN/VPN-Passwort anstelle Ihres Passworts gesetzt haben, verwenden Sie dieses.*
1. **Passwort vergessen?** Nutzen Sie die [Anleitung zur Passwortrücksetzung](https://www.uni-mannheim.de/it/anleitungen/passwort/).
1. **Support:** Bei Problemen mit Uni-ID oder Passwort wenden Sie sich an den Support:
   - Telefon: +49 621 181-2000
   - E-Mail: itsupport@uni-mannheim.de
1. **Download:** Klicken Sie auf „Download for macOS“.
1. **Installation:** Führen Sie die heruntergeladene Datei aus. Folgen Sie dem Installationsprozess, stimmen Sie der Lizenzvereinbarung zu und klicken Sie auf „Install“.
1. **Verbindung herstellen:** Führen Sie den Cisco-Anyconnect-Secure-Mobility-Client aus.
1. **Setup:** Tragen Sie in das Feld `vpn.uni-mannheim.de` ein und klicken Sie auf „Connect“.
1. **Verbindung:** Wählen Sie das passende Profil (WebVPN oder WebVPN-Split) und drücken Sie auf „Ok“.

### 🤖 Android

1. **Download:** Öffnen Sie den Google PlayStore und suchen Sie nach „Cisco Secure Client“.
1. **Installation:** Installieren Sie die App und öffnen Sie sie.
1. **Zugriff:** Akzeptieren Sie die Lizenzbedingungen und erlauben Sie dem Client den Zugriff auf Systeminformationen.
1. **Setup:**
   - Klicken Sie auf „Verbindungen“.
   - Geben Sie die Details ein:
     - Beschreibung (z.B. Universität Mannheim)
     - Serveradresse: `vpn.uni-mannheim.de`
   - Klicken Sie auf „Fertig“.
1. **Verbindung:** Starten Sie die VPN-Verbindung über den Schieberegler.
1. **Login:** Geben Sie die Zugangsdaten ein und wählen Sie das gewünschte Profil.

### 🍏 iOS (iPhone/iPad)

1. **Download:** Öffnen Sie den Apple AppStore und suchen Sie nach „Cisco Secure Client“.
1. **Installation:** Installieren Sie die App und öffnen Sie sie.
1. **Setup:**
   - Klicken Sie auf „Verbindungen“ und wählen Sie „VPN-Verbindung hinzufügen“.
   - Geben Sie die Details ein:
     - Beschreibung (z.B. Universität Mannheim)
     - Serveradresse: `vpn.uni-mannheim.de`
   - Speichern Sie die Verbindung.
1. **Bestätigung:** Bestätigen Sie die Profilerweiterung durch iOS und geben Sie ggf. Ihren „iPhone-Code“ ein.
1. **Verbindung:** Die Verbindung ist eingerichtet. Starten Sie die Verbindung über den Schieberegler und geben Sie die Zugangsdaten ein.

______________________________________________________________________

## ❓ Häufige Fragen und Fehlerbehebung

### ⚠️ Fehler: AnyConnect Client funktioniert nicht

**Fehlermeldung:** „The VPN client agent was unable to create the interprocess communication depot“
**Mögliche Ursache:** Auf einem oder mehreren Netzwerkinfaces ist die „Gemeinsame Nutzung der Internetverbindung“ aktiviert.
**Lösung:** Deaktivieren Sie die „Gemeinsame Nutzung der Internetverbindung“:

1. Starten Sie die Systemsteuerung → Netzwerk- und Freigabecenter.
1. Rechtsklick auf den Netzwerkadapter (LAN oder WLAN) → Eigenschaften.
1. Öffnen Sie den Reiter „Freigabe“ und entfernen Sie ein eventuell gesetztes Häkchen bei „Anderen Benutzern im Netzwerk gestatten, diese Verbindung des Computers als Internetverbindung zu verwenden“.

### 📚 Zugriff auf Online-Bibliotheken

**Problem:** Auf einige Online-Bibliotheken kann via VPN nicht zugegriffen werden.
**Lösung:**

1. **Profilwahl:** Wählen Sie zwingend das **„WebVPN“** Profil. Mit dem „WebVPN-Split“ Profil ist kein Zugriff auf die Online-Bibliotheken möglich.
1. **Weitere Infos:** Bitte beachten Sie den [Hinweis zur Datenbanknutzung](https://www.bib.uni-mannheim.de/datenbanknutzung/).

### 📡 Welche Daten gehen über den VPN-Tunnel?

Sie können vor dem Verbinden selbst entscheiden, welche Daten über den VPN-Tunnel gehen:

- **WebVPN:** Der komplette Internetverkehr wird durch den VPN-Tunnel gesendet. (Ausnahme: Private Netzwerkbereiche wie 192.168.X.X).
- **WebVPN-Split:** Nur der Internetverkehr bzw. die Daten zur Universität Mannheim werden durch den VPN-Tunnel gesendet. Der restliche Internetverkehr bleibt außerhalb des Tunnels.

### 💻 Fehler: Zertifikatsprüfung fehlschlägt (Linux)

**Fehlermeldung:** „The following Certificate received from the Server could not be verified“
**Problem:** Der AnyConnect-Client sucht nach gültigen SSL-Stammzertifikaten, die auf verschiedenen Linux-Distributionen nicht immer an der gleichen Stelle abgelegt sind.
**Lösung:** Der Cisco AnyConnect Client unter Linux verwendet das Verzeichnis `/opt/.cisco/certificates/ca`. Hier muss ein symbolischer Link vom „T-TeleSec GlobalRoot Class 2“ SSL-Stammzertifikat angelegt werden:

```bash
cd /opt/.cisco/certificates/ca
ln -s /etc/ssl/certs/T-TeleSec_GlobalRoot_Class_2.pem
```

______________________________________________________________________

## 🛠️ Service-Links

- **Speedtest:** Überprüfen Sie die Qualität Ihrer Verbindung zum Uni-Netz: [zum Speedtest](https://www.uni-mannheim.de/it/services/speedtest/)
- **Alle Anleitungen:** Übersicht aller IT-Anleitungen: [alle Anleitungen auf einen Blick](https://www.uni-mannheim.de/it/anleitungen/)
