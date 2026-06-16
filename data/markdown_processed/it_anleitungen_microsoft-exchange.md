---
title: Anleitung und FAQ zu Microsoft Exchange an der Universität Mannheim
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/
category: Services
tags: ['Exchange', 'E-Mail', 'Kalender', 'Outlook', 'Uni-ID', 'Postfach', 'Anleitungen', 'Kommunikation']
language: de
---

# Microsoft Exchange: Nutzung und Anleitungen

Mit Microsoft Exchange steht allen Beschäftigten und Studierenden der Universität Mannheim ein einheitliches System für E-Mail, Kalender und Adressbücher zur Verfügung.

## 📧 Zugriff auf Ihr Exchange-Postfach

Sie haben zwei Hauptmöglichkeiten, auf Ihr Exchange Postfach zuzugreifen:

1. **Über den Webmailer OWA (Outlook Web App):**
   - [Anleitung Login OWA](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/login-outlook-web-app/)
1. **Über einen E-Mail-Client:**
   - Um Ihre E-Mails, Termine und Adressen über einen E-Mail-Client bearbeiten zu können, finden Sie in den folgenden Anleitungen die Verbindungsvorgänge für Ihren Client.
   - [Exchange Video-Tutorials](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/video-tutorials/)

## 📚 Weitere Exchange-Anleitungen

Hier finden Sie spezifische Anleitungen zu verschiedenen Funktionen des Exchange-Systems:

- [Kalender freigeben](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/kalender-freigabe/)
- [Archiv Mailbox](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/archiv-mailbox/)
- [Spam Quarantäne-Box (Proxmox Mail Gateway)](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/proxmox-@gateway/)
- [Spam-Wortfilter-Regel erstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/spam-wortfilter/)
- [Gelöschte E-Mails wiederherstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/wiederherstellen-geloeschter-mails/)
- [Anzeigenamen/Adresse meiner Funktionskennung(en) anpassen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/funktionskennung/)
- [Weiterleitungen an universitäre E-Mail-Adressen einrichten](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/weiterleitung-einrichten/)
- [Weiterleitungs- und andere Regeln für Alias-Adressen erstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/postfachregeln-fuer-aliasadressen/)
- [Ordner im Webmailer OWA freigeben oder einen freigegebenen Ordner hinzufügen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/ordner-freigeben-outlook-web-app/)
- [Abwesenheitsnotiz via Outlook oder Webmailer OWA einstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/abwesenheitsnotizen/)
- [Kontakte freigeben](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/kontakte-freigabe/)
- [Wie schreibe ich eine E-Mail aus einem Funktionspostfach im Webmailer OWA?](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/funktionspostfach-im-webmailer/)
- [Mail Header in Outlook auslesen und tatsächlichen Absender bestimmen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/outlook-@header-auslesen/)
- [Mailinglisten (z. B. für Massenversand von E-Mails) erstellen und verwalten mit Mailman](https://www.uni-mannheim.de/it/anleitungen/mailman/)
- [Erstellen einer Signatur für Ihren Uni-Mailaccount](https://signatur.uni-mannheim.de/)

## ❓ FAQ: Häufig gestellte Fragen

### 🆔 E-Mail-Adresse und Adressstruktur

**Wie lautet meine Exchange E-Mail-Adresse?**
Sie können Ihre Exchange E-Mail-Adresse über Ihren Webbrowser (z.B. FireFox, Edge, Chrome) im [Outlook Web-Client](https://exchange.uni-mannheim.de/owa) einsehen.

- **Video-Anleitung:** [Die Anleitung als Video](https://www.uni-mannheim.de/media/Einrichtungen/it/Anleitungen/Exchange/FAQ/Exchange_Absender_Adresse_GER.mp4)
- **Vorgehen:**
  1. Rufen Sie in Ihrem Webbrowser [https://exchange.uni-mannheim.de/](https://exchange.uni-mannheim.de/) auf.
  1. Melden Sie sich mit Ihrer Uni-ID und dem dazugehörigen Passwort an.
  1. Klicken Sie nach dem Anmelden auf das Profilbild rechts oben; Ihre E-Mail-Adresse wird im Pop-Up angezeigt.

**Wird das POP3 Protokoll noch zur Verfügung gestellt?**
Nein. Das POP3 Protokoll ist ein veraltetes Mailprotokoll. Es lädt E-Mails auf den lokalen Rechner herunter und löscht diese im Exchange Postfach. Dies ist aus folgenden Gründen nicht akzeptabel:

- Bei einem Defekt des Rechners sind die E-Mails ohne Backup verloren und nicht wiederherstellbar.
- Das Einbinden über POP3 ist daher für die Postfächer des Exchange Mailsystems nicht vorgesehen.

**Wie kann ich meinen akademischen Titel in Exchange anzeigen lassen?**
Um Ihren akademischen Titel im Exchange Anzeigenamen zu hinterlegen, rufen Sie die Seite [MyUni-ID](https://id.uni-mannheim.de/) auf und setzen Sie unter „E-Mail | Uni-ID“ → „Status Uni-ID“ unten den entsprechenden Haken. Korrekturen an dem gespeicherten akademischen Grad müssen direkt mit der Personalabteilung der Universität Mannheim geklärt werden.

### 📧 E-Mail-Verarbeitung und Sicherheit

**Warum erhalte ich manche Mails als Anhang?**
Eingehende E-Mails von extern, welche **signiert** wurden, können aus technischen Gründen nicht den Hinweis „External Sender: Achtung bei Links […]“ im Original erhalten. Daher erstellt das Exchange Mailsystem eine neue leere E-Mail, schreibt den Hinweis hinein und hängt die ursprüngliche E-Mail als Anhang an.

- **Tipp:** Wenn Sie dem Inhalt der ursprünglichen E-Mail vertrauen, können Sie den Anhang mit der Maus in den Posteingang ziehen.
- **Hinweis:** Es gibt eine alternative Ansichtsoption, bei der signierte E-Mails normal empfangen und nicht als Anhang gepackt werden.

**Wie kann ich den „externe-Absender-Hinweis“ ändern?**
Eingehende E-Mails von extern werden in Ihrem Postfach entsprechend markiert. Sie können diese Markierung über [MyUni-ID](https://id.uni-mannheim.de/login.php) (Reiter E-Mail/Uni-ID → Externe E-Mails) anpassen. Es stehen folgende Ansichts-Optionen zur Auswahl:

- **Standard-Hinweistext:** Standardmäßig ausgewählt, geeignet für PC/Laptop. Verschlüsselte und signierte externe E-Mails werden als Anhang im Original angefügt.
- **Kurzer Hinweistext:** Minimale Veränderung des Vorschautextes, ideal für Smartphones. Verschlüsselte & signierte externe E-Mails werden als Anhang im Original angefügt.
- **Präfix im Betreff:** Fügt einen Präfix an den Betreff an. E-Mails werden normal empfangen und nicht als Anhang gepackt.

**Wo werden E-Mails gespeichert, die ich über ein Funktionspostfach versende?**
Seit dem 1.2.2023 werden alle E-Mails, die Sie über ein Funktionspostfach senden, in Ihrem persönlichen Postfach **und zusätzlich in Kopie** im Funktionspostfach unter „Gesendete Elemente“ gespeichert. Dies vereinfacht die Verwaltung der gesamten Kommunikation.

### 🗓️ Kalender und Termine

**Warum erscheinen meine Outlook-Termine nicht in Microsoft Teams und umgekehrt?**
Das neue Exchange Mailsystem ist nicht vollumfänglich mit den Microsoft 365 Cloud-Diensten (wie Teams) verbunden. Ihr Microsoft Teams Kalender und Ihr Exchange Kalender sind daher aktuell zwei getrennte Kalender, die sich nicht synchronisieren.

- *Hinweis:* Diese Funktion ist auf der M365-Instanz für Studierende nicht vorhanden.

**Warum kann ich meinen Kalender nicht freigeben?**
Die Kalenderfreigabe ist auf interne Postfächer mit „...**@uni-mannheim.de**" Adressen beschränkt. Der Versuch, den Kalender für andere Domains (z.B. „xyz@gmx.de“) freizugeben, wird als externe Adresse abgelehnt. Bei Problemen bei der Freigabe für ein Uni-Mannheim-internes Postfach beachten Sie bitte die [Anleitung zur Freigabe von Kalendern](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/kalender-freigabe/).

### 🔍 Suche und Adressbuch

**Warum findet die Outlook-Suche meine E-Mail nicht?**
Die Outlook Anwendung durchsucht standardmäßig das **aktuell ausgewählte Postfach**. Wenn die gewünschte E-Mail in einem anderen, nicht ausgewählten Postfach liegt, wird sie nicht angezeigt.

- **Lösung:** Tippen Sie Ihren Suchbegriff ein, klicken Sie links daneben auf „Aktuelles Postfach“ und wählen Sie danach „Alle Postfächer“ aus.
- **Standardeinstellung:** Sie können Outlook so einstellen, dass es immer über alle eingebundenen Postfächer sucht:
  1. Öffnen Sie Outlook.
  1. Klicken Sie links oben auf „Datei“ und dann unten links auf „Optionen“.
  1. Klicken Sie auf den Reiter „Suchen“ und wählen Sie „Allen Postfächern“ aus.

**Warum finde ich im Outlook-Adressbuch einen Kontakt nicht?**
Wenn Sie einen Kontakt nicht finden, gehen Sie bitte wie folgt vor:

1. Öffnen Sie das Outlook Adressbuch.
1. Vergewissern Sie sich, dass die Globale Adressliste und die Option „Alle Spalten“ ausgewählt sind.
1. Geben Sie den gewünschten Namen ein und klicken Sie auf das Pfeil-Symbol.

### 📱 Client-Nutzung und Barrierefreiheit

**Warum kann ich die offizielle Outlook App nicht verwenden?**
Die offizielle Outlook App für Android & iOS verbindet sich nicht direkt mit dem Exchange Mailsystem der Universität, sondern mit Microsoft Servern. Da dabei diverse Daten (inkl. E-Mails der letzten 30 Tage) auf diesen externen Servern zwischengespeichert werden, verletzt dies die Anforderungen der Universität, keine E-Mails in der Cloud zu speichern. Daher wird der Zugriff blockiert.

**Wie kann ich Outlook barrierefrei einstellen?**
Hinweise zum Versenden und Empfangen barrierefreier Nachrichten finden Sie in der Anleitung [Barrierefreiheit](https://www.uni-mannheim.de/it/anleitungen/barrierefreiheit/).

### ⚙️ Für Administratoren

**Informationen für Admins:**
Sind Sie Admin an einem Lehrstuhl oder in einer Einrichtung? Wir stellen Ihnen alle notwendigen Informationen bereit, um Ihre Nutzenden beim Umzug auf das Exchange Mailsystem bestmöglich unterstützen zu können.
[Mehr lesen für Administratoren](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/informationen-admins/)
