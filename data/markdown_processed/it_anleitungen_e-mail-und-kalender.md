---
title: Anleitung und FAQ zum Exchange E-Mail-Service der Universität Mannheim
source_url_de: https://www.uni-mannheim.de/it/anleitungen/e-@und-kalender/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/e-mail-and-calendar/
category: Services
tags: ['Exchange', 'E-Mail', 'Outlook', 'Kalender', 'Postfach', 'Uni-ID', 'Anleitungen', 'Webmailer']
language: de
---

# 📧 Fragen und Anleitungen zum E-Mail-Service (Exchange)

Dieser Leitfaden bietet umfassende Informationen zum Zugriff, zur Nutzung und zur Fehlerbehebung im Exchange E-Mail-System der Universität Mannheim.

## 🚀 Zugriff auf Ihr Exchange Postfach

Sie haben zwei Hauptmöglichkeiten, auf Ihr Exchange Postfach zuzugreifen:

1. **Über den Webmailer OWA (Outlook Web App):**
   - [Anleitung Login OWA](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/login-outlook-web-app/)
1. **Über einen E-Mail-Client:**
   - Um E-Mails, Termine und Adressen über einen eigenen E-Mail-Client bearbeiten zu können, finden Sie in den folgenden Anleitungen die Verbindungsvoraussetzungen für Ihren Exchange-Postfach-Client.

## 🛠️ Wichtige Funktionen und Erweiterte Anleitungen

Hier finden Sie spezifische Anleitungen zu fortgeschrittenen Funktionen des Exchange-Systems:

- [Kalender freigeben](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/kalender-freigabe/)
- [Archiv Mailbox verwalten](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/archiv-mailbox/)
- [Spam Quarantäne-Box (Proxmox Mail Gateway)](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/proxmox-@gateway/)
- [Spam-Wortfilter-Regel erstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/spam-wortfilter/)
- [Gelöschte E-Mails wiederherstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/wiederherstellen-geloeschter-mails/)
- [Anzeigenamen/Adresse meiner Funktionskennung(en) anpassen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/funktionskennung/)
- [Weiterleitungen an universitäre E-Mail-Adressen einrichten](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/weiterleitung-einrichten/)
- [Weiterleitungs- und andere Regeln für Alias-Adressen erstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/postfachregeln-fuer-aliasadressen/)
- [Ordner im Webmailer OWA freigeben oder einen freigegebenen Ordner hinzufügen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/ordner-freigeben-outlook-web-app/)
- [Abwesenheitsnotiz via Outlook oder Webmailer OWA einstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/abwesenheitsnotizen/)
- [Kontakte freigeben](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/kontakte-freigabe/)
- [E-Mail aus einem Funktionspostfach im Webmailer OWA erstellen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/funktionspostfach-im-webmailer/)
- [Mail Header in Outlook auslesen und tatsächlichen Absender bestimmen](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/outlook-@header-auslesen/)
- [Mailinglisten (z. B. für Massenversand von E-Mails) erstellen und verwalten mit Mailman](https://www.uni-mannheim.de/it/anleitungen/mailman/)
- [Signatur für Ihren Uni-Mailaccount erstellen](https://signatur.uni-mannheim.de/)

______________________________________________________________________

## ❓ FAQ: Häufig gestellte Fragen zum Exchange-Service

### 📧 E-Mail-Adresse und Adressstruktur

**Wie lautet meine Exchange E-Mail-Adresse?**
Sie können Ihre Exchange E-Mail-Adresse über Ihren Webbrowser (z. B. FireFox, Edge, Chrome) im [Outlook Web-Client](https://exchange.uni-mannheim.de/owa) einsehen.

- **Anleitung als Video:** [Video-Anleitung](https://www.uni-mannheim.de/media/Einrichtungen/it/Anleitungen/Exchange/FAQ/Exchange_Absender_Adresse_GER.mp4)
- **Vorgehen:**
  1. Rufen Sie in Ihrem Webbrowser [https://exchange.uni-mannheim.de/](https://exchange.uni-mannheim.de/) auf.
  1. Melden Sie sich mit Ihrer Uni-ID und dem dazugehörigen Passwort an.
  1. Klicken Sie nach dem Anmelden auf das Profilbild rechts oben; Ihre E-Mail-Adresse wird im Pop-Up angezeigt.
- **Hinweis zur Adressstruktur:** Aufgrund der einheitlichen Adressstruktur fallen die Subdomains (Adress-Zusätze vor „uni-mannheim.de“, z. B. @\*\*unit.\*\*uni-mannheim.de) zukünftig für die Absender-Adressen weg. Sie können jedoch weiterhin E-Mails empfangen, die an Adressen mit einer Subdomain gesendet werden.

**Wie kann ich meinen akademischen Titel in Exchange anzeigen lassen?**
Um Ihren akademischen Titel im Exchange Anzeigenamen zu hinterlegen, rufen Sie die Seite [MyUni-ID](https://id.uni-mannheim.de/) auf und setzen Sie unter „E-Mail | Uni-ID“ → „Status Uni-ID“ unten den entsprechenden Haken. Für Korrekturen wenden Sie sich bitte direkt an die Personalabteilung der Universität Mannheim.

### 📥 Eingehende E-Mails und Sicherheit

**Warum erhalte ich manche Mails als Anhang?**
Eingehende E-Mails von extern, welche **signiert** wurden, können aus technischen Gründen nicht den Hinweis „External Sender: Achtung bei Links […]“ im Original erhalten. Daher erstellt das Exchange Mailsystem eine neue leere E-Mail, schreibt den Hinweis hinein und hängt die ursprüngliche E-Mail als Anhang an.

- **Tipp:** Wenn Sie dem Inhalt der ursprünglichen E-Mail vertrauen, können Sie den Anhang mit der Maus in den Posteingang ziehen. Die E-Mail wird dann im Posteingang erstellt und kann normal beantwortet werden.
- **Alternative:** Ein anderer FAQ-Eintrag zeigt eine Variante des externen-Absender-Hinweises, bei der signierte E-Mails nicht als Anhang gepackt, sondern normal empfangen werden.

**Wie kann ich den „externe-Absender-Hinweis“ ändern?**
Eingehende E-Mails von extern werden in Ihrem Postfach entsprechend markiert. Sie können diese Markierung über [MyUni-ID](https://id.uni-mannheim.de/login.php) (Reiter E-Mail/Uni-ID → Externe E-Mails) nach Ihren Wünschen anpassen.

- **Standard-Hinweistext:** Standardmäßig ausgewählt und für die Nutzung von E-Mail-Anwendungen auf PC/Laptop geeignet. Verschlüsselte und signierte externe E-Mails werden als Anhang im Original angefügt.
- **Kurzer Hinweistext:** Diese Variante verändert den Vorschautext einer Nachricht am geringfügigsten und eignet sich besonders bei Nutzung von Smartphones. Verschlüsselte & signierte externe E-Mails werden als Anhang im Original angefügt.
- **Präfix im Betreff:** Diese Variante fügt an den Anfang des Betreffs einen Präfix ein. Je nach Client kann dies dazu führen, dass E-Mails nicht mehr als Bestandteil einer Konversation, sondern einzeln dargestellt werden. Verschlüsselte und signierte externe E-Mails werden normal empfangen und nicht als Anhang gepackt.

### 📅 Kalender und Terminplanung

**Warum erscheinen meine Outlook-Termine nicht in Microsoft Teams und umgekehrt?**
Das neue Exchange Mailsystem ist nicht vollumfänglich mit den Microsoft 365 Cloud-Diensten der Universität (zu denen auch Teams gehört) verbunden. Daher sind Ihr Microsoft Teams Kalender und Ihr Exchange Kalender aktuell zwei voneinander getrennte, eigene Kalender, die sich nicht gegenseitig synchronisieren.

- *Hinweis:* Diese Funktion ist auf der M365-Instanz für Studierende nicht vorhanden.

**Warum kann ich meinen Kalender nicht freigeben?**
Die Kalenderfreigabe ist auf interne Postfächer mit „...**@uni-mannheim.de**" Adressen beschränkt (Domain „uni-mannheim.de“). Wird versucht, den Kalender für andere Domains (z. B. „xyz@gmx.de“) freizugeben, wird dies als externe Adresse abgelehnt.

- *Lösung:* Falls Sie Ihren Kalender für ein Uni-Mannheim-internes Postfach freigeben möchten und dennoch eine Fehlermeldung erhalten, folgen Sie bitte der [Anleitung zur Freigabe von Kalendern](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/kalender-freigabe/).

**Warum kann ich keine Teams-Termine in Outlook erstellen?**

1. Beenden Sie Outlook und MS Teams und starten Sie beide Programme neu.
1. Sollte das Problem bestehen, installieren Sie MS Teams neu und beenden Sie Outlook. Starten Sie Teams nach der Neuinstallation und rufen Sie anschließend Outlook auf.

- **Wichtig:** Sie können Teams-Termine nur für Ihren eigenen Kalender erstellen. Für freigegebene Kalender können Sie nur „normale“ Termine erstellen.
- *Hinweis:* Diese Funktion ist auf der M365-Instanz für Studierende grundsätzlich nicht vorhanden.

### 🔍 Suche und Adressbuch

**Warum findet die Outlook-Suche meine E-Mail nicht?**
Die Outlook-Anwendung durchsucht beim Starten einer Suche standardmäßig das **aktuell ausgewählte Postfach**. Wenn Sie mehrere Postfächer eingebunden haben und die E-Mail in einem anderen, nicht ausgewählten Postfach liegt, wird sie nicht angezeigt.

- **Lösung:** Tippen Sie Ihren Suchbegriff ein, klicken Sie links daneben auf „Aktuelles Postfach“ und wählen Sie danach „Alle Postfächer“ aus.
- **Standardeinstellung:** Um die Suche immer über alle Postfächer zu durchführen, gehen Sie wie folgt vor:
  1. Öffnen Sie Outlook auf Ihrem Rechner.
  1. Klicken Sie links oben auf „Datei“ und dann unten links auf „Optionen“.
  1. Klicken Sie im sich öffnenden Fenster auf den Reiter „Suchen“.
  1. Wählen Sie „Allen Postfächern“ aus und bestätigen Sie mit „OK“.

**Warum finde ich im Outlook-Adressbuch einen Kontakt nicht?**
Wenn Sie einen Kontakt nicht finden, der im Adressbuch sein sollte, gehen Sie bitte wie folgt vor:

1. Öffnen Sie das Outlook Adressbuch.
1. Vergewissern Sie sich, dass die Globale Adressliste und die Option „Alle Spalten“ ausgewählt sind.
1. Geben Sie den gewünschten Namen in das Suchfeld ein und klicken Sie auf das Pfeil-Symbol.

### ⚙️ Technische Protokolle und Speicherung

**Wird das POP3 Protokoll noch zur Verfügung gestellt?**
Nein. POP3 ist ein veraltetes Mailprotokoll. Es lädt E-Mails auf den lokalen Rechner der Nutzer\*innen herunter und löscht diese im Exchange Postfach. Dies ist riskant, da bei einem Defekt die E-Mails ohne Backup verloren gehen können. Daher ist die Einbindung über POP3 für die Postfächer des Exchange Mailsystems nicht akzeptabel.

**Wo werden E-Mails gespeichert, die ich über ein Funktionspostfach versende?**
Seit dem 1.2.2023 werden alle E-Mails, die Sie über ein Funktionspostfach senden, in Ihrem persönlichen Postfach **und zusätzlich in Kopie** im Funktionspostfach unter „Gesendete Elemente“ gespeichert. Dies vereinfacht die Verwaltung der gesamten Kommunikation.

### 📱 Mobile und Client-Nutzung

**Warum kann ich die offizielle Outlook App nicht verwenden?**
Die offizielle Outlook App für Android & iOS verbindet sich nicht direkt mit dem Exchange Mailsystem der Universität, sondern mit Microsoft Servern. Dabei werden diverse Daten (darunter alle E-Mails der letzten 30 Tage) auf diesen Microsoft Servern zwischengespeichert. Dies verletzt die Anforderungen der Universität, keine E-Mails in der Cloud zu speichern, weshalb der Zugriff blockiert wird.

**Wie kann ich Outlook barrierefrei einstellen?**
Hinweise zum Versenden und Empfangen barrierefreier Nachrichten finden Sie in der Anleitung [Barrierefreiheit](https://www.uni-mannheim.de/it/anleitungen/barrierefreiheit/).
