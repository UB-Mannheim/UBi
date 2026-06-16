---
title: Spam-Wortfilter in Outlook/Exchange einrichten und verwalten
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/spam-wortfilter/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/spam-word-filter/
category: Services
tags: ['Spam', 'Wortfilter', 'Outlook', 'Exchange', 'Regeln', 'Posteingang', 'Uni-ID', 'Junk-Ordner']
language: de
---

# Spam-Wortfilter in Outlook/Exchange einrichten

Sie können einen eigenen Spam-Wortfilter für Ihr Exchange Postfach erstellen, um unerwünschte E-Mails zu filtern.

**Hinweis:** Wenn Sie verhindern möchten, dass E-Mails von gesamten Adressbereichen („Domains“) eingehen, konsultieren Sie bitte die [Mail Gateway Anleitung](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/proxmox-@gateway/#c347511) und das Kapitel „Blacklist“.

## 1. Neue Spam-Wortfilter-Regel erstellen

Folgen Sie diesen Schritten, um die erste Wortfilter-Regel einzurichten:

1. **Zugriff auf OWA:** Rufen Sie die [Outlook Web App (OWA)](https://exchange.uni-mannheim.de) auf.
1. **Anmelden:** Geben Sie Ihre Uni-ID und Ihr zugehöriges Passwort ein und klicken Sie auf „Anmelden“.
1. **Einstellungen öffnen:** Klicken Sie rechts oben auf das Zahnrad-Symbol, um die Einstellungen zu öffnen, und wählen Sie anschließend „Optionen“.
1. **Regeln aufrufen:** Klicken Sie im Menü auf „Posteingangs- und Aufräumregeln“ und klicken Sie auf das „+“-Symbol, um eine neue Regel zu erstellen.
1. **Regel definieren:**
   - Geben Sie einen Namen für die Regel ein.
   - Klicken Sie unter „Wenn die Nachricht eintrifft […]“ auf das Dropdown-Menü, wählen Sie „Enthält diese Wörter“ und anschließend „im Betreff…“.
1. **Wörter hinzufügen:** Im sich öffnenden Fenster geben Sie nacheinander die gewünschten Wörter ein, die Sie filtern möchten. Klicken Sie nach jedem Wort auf das „+“-Symbol und bestätigen Sie abschließend mit „OK“.
1. **Aktion festlegen:** Wählen Sie unter „Alle folgenden Aktionen ausführen“ die Aktion „Verschieben, kopieren, oder löschen“ und wählen Sie dort „Nachricht in Ordner verschieben…“.
1. **Zielordner wählen:** Wählen Sie Ihren Junk-Ordner aus und bestätigen Sie mit „OK“.
1. **Regel speichern:** Legen Sie die Regel abschließend mit einem Klick auf „OK“ an.

## 2. Bestehende Spam-Wortfilter ergänzen

Sie können die erstellte Spam-Wortfilter-Regel nachträglich um weitere Wörter erweitern:

1. **Regeln aufrufen:** Gehen Sie wie in der Anleitung oben beschrieben zu den „Posteingangs- und Aufräumregeln“.
1. **Regel bearbeiten:** Markieren Sie die bestehende Spam-Wortfilter-Regel und klicken Sie auf das Stift-Symbol, um sie zu bearbeiten.
1. **Wörterliste öffnen:** Klicken Sie bei den Bedingungen auf die Wörterliste, um diese zu öffnen.
1. **Wörter hinzufügen und speichern:** Fügen Sie die weiteren Wörter hinzu und speichern Sie die Regel anschließend ab.

______________________________________________________________________

**Tipp:** Prüfen Sie nach dem Anlegen der Wortfilter-Regel regelmäßig Ihren Junk-Ordner auf neue E-Mails.
