---
title: Anleitung zur Spam-Quarantäne-Box (Proxmox Mail Gateway)
source_url_de: None
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/spam-quarantine-box-proxmox-mail-gateway-1/
category: Benutzung
tags: ['Spam', 'Phishing', 'Quarantäne', 'Mail Gateway', 'Proxmox', 'Exchange', 'Uni-ID']
language: de
---

# Spam-Quarantäne-Box (Proxmox Mail Gateway)

Um Spam- und Phishing-Attacken besser abzuwehren, wurde für alle Postfächer der Universität ein neues Mail Gateway eingeführt: das **Proxmox Mail Gateway**.

Erkannte Spam- und Phishing-E-Mails werden nicht direkt ins Exchange Postfach zugestellt, sondern in die Quarantäne vorgehalten. Dort werden sie nach 30 Tagen automatisch gelöscht. In der Quarantäne-Box können Sie diese E-Mails einsehen, verwalten und entsprechende Maßnahmen ergreifen.

## Zugriff und Anmeldung

Sie können die Quarantäne-Box auf zwei Wegen erreichen:

1. **Täglicher Bericht:** Einmal täglich wird eine Infomail an Ihr Exchange Postfach versandt, falls in den letzten 24 Stunden neue Spam-/Phishing-E-Mails eingegangen sind. Die Links in dieser E-Mail führen direkt zur Quarantäne-Box.
1. **Webzugriff:** Die Quarantäne-Box ist jederzeit über den Webbrowser unter [https://mailknast.uni-mannheim.de](https://mailknast.uni-mannheim.de) erreichbar.

**Anmeldedaten:**

| Feld | Wert |
| :--- | :--- |
| **Anmeldename** | `uni-id@ad.uni-mannheim.de` |
| **Passwort** | Passwort Ihrer Uni-ID |

## Funktionen der Quarantäne-Box

### 🔍 Leseansicht und Verwaltung

In der Quarantäne-Box können Sie die folgenden Aktionen für ausgewählte E-Mails durchführen:

- **Raw Umschalten:** Zeigt den Quellcode der ausgewählten E-Mail an.
- **Spam Info umschalten:** Zeigt die Spam-Evaluations-Informationen der E-Mail an.
- **Herunterladen:** Lädt die ausgewählte E-Mail als `.eml` Datei herunter.
- **Zustellen:** Stellt die ausgewählte E-Mail ins Exchange Postfach zu.
- **Löschen:** Löscht die ausgewählte E-Mail unwiderruflich.

### 🛡️ Whitelist (E-Mails zulassen)

Mit der Whitelist können Adressen und Domains hinzugefügt werden, deren E-Mails zukünftig ohne Spam-Überprüfung direkt in Ihr Exchange Postfach zugestellt werden.

- **Funktion:** E-Mails von gelisteten Absendern werden als vertrauenswürdig eingestuft.
- **Beispiele:**
  - `@gmail.com`: Alle E-Mails von Absendern, die auf @gmail.com enden.
  - `*unit.uni-mannheim.de`: Alle E-Mails, die auf diesen Adressbereich enden.
  - `melanie-muster@vertrieb-xyz.de`: E-Mails von dieser spezifischen Adresse.

### 🚫 Blacklist (E-Mails blockieren)

Mit der Blacklist können Adressen und Domains hinzugefügt werden, deren E-Mails sofort und unwiderruflich gelöscht werden, ohne in der Quarantäne vorgehalten oder ins Postfach zugestellt zu werden.

- **Funktion:** E-Mails von gelisteten Absendern werden sofort blockiert und gelöscht.
- **Anlage:** Die Einträge werden analog wie bei der Whitelist angelegt.

______________________________________________________________________

**Hinweis zur Anzeige:** Standardmäßig werden nur E-Mails der letzten 7 Tage angezeigt. Um ältere E-Mails (bis zu 30 Tage in der Vergangenheit) einzusehen, muss der Datums-Filter entsprechend angepasst werden.
