---
title: Beantragung, Verwaltung und Sperrung digitaler Zertifikate an der Universität Mannheim
source_url_de: N/A
source_url_en: https://www.uni-mannheim.de/en/
category: Services
tags: ['Zertifikat', 'Digital', 'Beantragung', 'Server', 'Personal', 'Sperrung', 'HARICA', 'E-Mail']
language: de
---

# Digitale Zertifikate: Beantragung und Verwaltung

Dieses Dokument enthält Schritt-für-Schritt-Anleitungen zur Beantragung, Verwaltung und Sperrung verschiedener Arten digitaler Zertifikate (persönlich, für Gruppen und für Server).

**Wichtiger Hinweis:** Nähere Informationen zu den einzelnen Zertifikaten finden Sie unter [Services/ TCS Zertifikate](https://www.uni-mannheim.de/it/services/tsc-zertifikate).

## 🔑 Persönliches Zertifikat

### 1. Beantragung eines persönlichen Zertifikats

Die Beantragung erfolgt über den Zertifikatsanbieter HARICA.

**Schritte zur Beantragung:**

1. **Zugang:** Klicken Sie auf diesen [Link](https://cm.harica.gr), um zur Beantragung bei HARICA zu gelangen.
1. **Login:** Wählen Sie den „Academic Login“ zur Anmeldung.
1. **Institution wählen:** Wählen Sie die „University of Mannheim“ aus der Liste (Suche nach „Mannheim“). Melden Sie sich mit Ihrer Uni-ID und Ihrem Passwort an.
1. **Menüpunkt:** Wählen Sie auf der linken Seite den Menüpunkt „Email“.
1. **Zertifikatstyp:** Wählen Sie als Zertifikatstyp „**E@only**“.
1. **Fortfahren:** Klicken Sie auf **Next** (zweimal).
1. **Überprüfung:** Überprüfen Sie die Angaben und stimmen Sie den „Terms of Use“ von HARICA zu.
1. **Bestätigung:** Sie erhalten eine E-Mail mit einem Bestätigungslink. Klicken Sie auf die Schaltfläche „Confirm“, um fortzufahren.
1. **Dashboard:** Sie werden zum Dashboard des HARICA Zertifikatsmanagers weitergeleitet. Klicken Sie auf „Enroll your Certificate“.
1. **Generierung:** Wählen Sie als Keysize den Wert „4096“ und legen Sie ein sicheres Passwort fest. Bestätigen Sie, dass Sie das alleinige Wissen über dieses Passwort haben. Klicken Sie auf „Enroll Certificate“.
1. **Download:** Laden Sie Ihr Zertifikat im **.p12 Format** herunter. Die Datei enthält Ihr öffentliches Zertifikat und den privaten Schlüssel. **Geben Sie diese Datei niemals an andere Personen weiter!**

### 2. Einbindung in Outlook

Standardmäßig verwendet Outlook das Verfahren SHA1, was zu Fehlermeldungen führen kann. Die Universitäts-IT empfiehlt daher die Verwendung eines neueren Verfahrens wie SHA256.

**Zertifikat importieren:**

1. Klicken Sie in Outlook unter „Datei“ auf „Optionen“ und anschließend auf „Trust Center“. Wählen Sie „Einstellungen für das Trust Center...“.
1. Klicken Sie unter „E-Mail-Sicherheit“ auf „Importieren/ Exportieren...“.
1. Wählen Sie die exportierte Zertifikatsdatei aus, geben Sie das Kennwort ein und klicken Sie auf „OK“.
1. Setzen Sie den Haken bei „Ausgehende Nachrichten digitale Signatur hinzufügen“.

**Zertifikat anzeigen:**

1. Klicken Sie in Outlook unter „Datei“ auf „Optionen“ und anschließend auf „Trust Center“. Wählen Sie „Einstellungen für das Trust Center...“.
1. Klicken Sie unter dem Reiter „E-Mail-Sicherheit“ bei „Verschlüsselte E-Mail-Nachrichten“ auf „Einstellungen“.
1. Wählen Sie die entsprechende Sicherheitsregel aus und klicken Sie auf „Auswählen...“.
1. Das Zertifikat kann nun unter „Zertifikateigenschaften anzeigen“ eingesehen werden.

### 3. Sperrung des persönlichen Zertifikats

Sollten Sie Ihr Zertifikat nicht mehr benötigen, kompromittiert sein oder wenn nicht mehr berechtigte Personen Zugriff auf den privaten Schlüssel haben, veranlassen Sie bitte eine Sperrung.

- **Per E-Mail:** Schreiben Sie eine E-Mail an [ca-admin@uni-mannheim.de](mailto:ca-admin@uni-mannheim.de) mit der Bitte um Sperrung und der Nennung des betroffenen Zertifikats.
- **Selbstveranlassung:** Alternativ können Sie die Sperrung selbst über den [Zertifikatsmanager von HARICA](https://cm.harica.gr) veranlassen.

## 🌐 Serverzertifikat

### 1. Beantragung eines Serverzertifikats

**Optionale Vorbereitung (Certificate Request - CSR):**
Sie können optional einen „Certificate Request“ (CSR) erzeugen. Dies kann entweder automatisch im Browser oder manuell über die Kommandozeile geschehen.

*Beispielbefehl (Windows/Linux mit openssl):*
`openssl req -new -newkey rsa:4096 -sha512 -nodes -subj '/C=DE/ST=Baden-Wuerttemberg/O=Universitet Mannheim/CN=******FQDN******/emailAddress=**ihre-emailadresseuni-mannheim.de**' -keyout******FQDN******.key -out******FQDN******.csr`
*(Bitte ersetzen Sie die fett markierten Attribute durch die passenden Werte.)*

**Schritte zur Beantragung über HARICA:**

1. **Zugang:** Klicken Sie auf diesen [Link](https://cm.harica.gr), um zur Beantragung bei HARICA zu gelangen.
1. **Login:** Wählen Sie den „Academic Login“ zur Anmeldung.
1. **Institution wählen:** Wählen Sie die „University of Mannheim“ aus der Liste. Melden Sie sich mit Ihrer Uni-ID und Ihrem Passwort an.
1. **Menüpunkt:** Wählen Sie auf der linken Seite den Menüpunkt „Server“.
1. **Servername:** Geben Sie den gewünschten Servernamen an und klicken Sie auf **Next**.
1. **Zertifikatstyp:** Wählen Sie „**For enterprises or organizations (OV)**“.
1. **Bestätigung:** Bestätigen Sie die angezeigten Organisationsinformationen und stimmen Sie den „Terms of Use“ zu.
1. **Generierung:** Wählen Sie die Keysize „4096“ und legen Sie ein sicheres Passwort fest. Klicken Sie auf „Generate Private Key, CSR, and submit order“.
1. **Download:** Laden Sie den privaten Schlüssel für Ihr Zertifikat herunter und speichern Sie diesen auf Ihrem Computer.
1. **Fertigstellung:** Ihr Antrag wird von HARICA geprüft. Nach erfolgreicher Prüfung erhalten Sie eine E-Mail. Über das Dashboard können Sie das neue Zertifikat herunterladen.

### 2. Sperrung des Serverzertifikats

Sollte das Zertifikat nicht mehr benötigt, kompromittiert sein oder wenn nicht mehr berechtigte Personen Zugriff auf den privaten Schlüssel haben, veranlassen Sie bitte eine Sperrung.

- **Per E-Mail:** Schreiben Sie eine E-Mail an [ca-admin@uni-mannheim.de](mailto:ca-admin@uni-mannheim.de) mit der Bitte um Sperrung und der Nennung des betroffenen Zertifikats.
- **Selbstveranlassung (Empfohlen):**
  1. Rufen Sie den [HARICA Zertifikatsmanager](https://cm.harica.gr) auf.
  1. Melden Sie sich mit Ihrer Uni-ID und Ihrem Passwort an.
  1. Wählen Sie im Bereich „Valid Certificates“ das Zertifikat aus, das Sie sperren möchten, und klicken Sie auf die drei Punkte, gefolgt von „Revoke“.
  1. Geben Sie einen Grund für die Sperrung an und klicken Sie auf „Revoke“.
  1. Sie erhalten von HARICA eine Bestätigung per E-Mail.

## 👥 Gruppenzertifikat

### 1. Beantragung und Sperrung

**Beantragung:**
Falls Sie ein Gruppenzertifikat beantragen möchten, senden Sie bitte eine E-Mail an [ca-admin@uni-mannheim.de](mailto:ca-admin@uni-mannheim.de), um die Möglichkeiten zu besprechen.

**Sperrung:**
Sollte das Zertifikat nicht mehr benötigt, kompromittiert sein oder wenn nicht mehr berechtigte Personen Zugriff auf den privaten Schlüssel haben, veranlassen Sie bitte eine Sperrung.

- **Per E-Mail:** Schreiben Sie eine E-Mail an [ca-admin@uni-mannheim.de](mailto:ca-admin@uni-mannheim.de) mit der Bitte um Sperrung und der Nennung des betroffenen Zertifikats.
- **Selbstveranlassung:** Die Sperrung kann alternativ über den [Zertifikatsmanager von HARICA](https://cm.harica.gr) veranlasst werden (siehe Abschnitt Serverzertifikat).

______________________________________________________________________

**Tipp:** Speichern und verwalten Sie Ihre Passwörter sicher mit dem kostenfreien Passwort Manager [KeePass](https://www.uni-mannheim.de/informationssicherheit/infomaterial/anleitung-keepass/).
