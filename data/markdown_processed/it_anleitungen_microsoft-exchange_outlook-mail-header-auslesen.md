---
title: Anleitung zur Analyse von E-Mail-Headern in Outlook
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/outlook-@header-auslesen/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/outlook-analyze-mail-header/
category: Benutzung
tags: ['Outlook', 'E-Mail', 'Header', 'Absender', 'Analyse', 'Internetkopfzeilen', 'Microsoft Exchange']
language: de
---

# Wie Sie den tatsächlichen Absender einer E-Mail bestimmen (Header-Analyse)

Diese Anleitung zeigt Ihnen Schritt für Schritt, wie Sie den Header einer E-Mail in Outlook auslesen und analysieren können, um den tatsächlichen Ursprung und Absender der Nachricht zu identifizieren.

## 📧 Schritt-für-Schritt-Anleitung in Outlook

Folgen Sie diesen Schritten, um die notwendigen Informationen zu extrahieren:

1. **E-Mail öffnen:** Öffnen Sie die betreffende E-Mail mit einem Doppelklick.
1. **Eigenschaften aufrufen:** Klicken Sie links oben im Menü auf **„Datei“**.
1. **Header kopieren:**
   - Klicken Sie im sich öffnenden Menü auf **„Eigenschaften“**.
   - Markieren Sie den gesamten Text unter **„Internetkopfzeilen“** (Strg + A) und kopieren Sie ihn (Strg + C).
   - Schließen Sie das Eigenschaften-Fenster.

## 🌐 Analyse des Headers im Webbrowser

Der kopierte Text muss nun in einem spezialisierten Analysewerkzeug verarbeitet werden:

1. **Analyse-Tool nutzen:** Rufen Sie einen „Mail Header Analyse“-Webdienst auf, wie zum Beispiel von Microsoft ([https://mha.azurewebsites.net/](https://mha.azurewebsites.net/)).
1. **Text einfügen:** Fügen Sie den kopierten Text in das Analyse-Tool ein.

## 🔍 Interpretation der Ergebnisse

Um den Ursprung der E-Mail zu bestimmen, müssen Sie die folgenden Bereiche im Analyse-Tool überprüfen:

- **Prüfen Sie den „Hop“-Bereich:** Suchen Sie in der Spalte **„Submitting Host“** nach dem Eintrag. Dieser zeigt den Ursprung der E-Mail und den absendenden Server.
- **Bestimmung des Ursprungs:** Wenn die Adresse in diesem Bereich auf `[…].uni-mannheim.de` endet, wurde die E-Mail von den Servern der Universität Mannheim versendet.
