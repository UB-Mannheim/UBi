---
title: Postfachregeln für Aliasadressen in Microsoft Exchange
source_url_de: https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/postfachregeln-fuer-aliasadressen/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/microsoft-exchange/mailbox-rules-for-alias-addresses/
category: Benutzung
tags: ['Postfachregeln', 'Aliasadressen', 'Microsoft Exchange', 'Weiterleitung', 'OWA', 'Uni-ID']
language: de
---

# Postfachregeln für Aliasadressen in Microsoft Exchange

**Wichtiger Hinweis:** Sie können diese Anleitung überspringen, falls Sie keine Postfachregeln eingerichtet haben oder falls diese Regeln nicht explizit nur für einzelne Alias-Adressen gelten.

Aufgrund einer technischen Anpassung von Microsoft Exchange funktionieren Postfachregeln, die sich auf explizite E-Mail-Adressen („Aliasse“) beziehen, nach der Umstellung auf das Proxmox Mail Gateway anders als bisher.

**Betroffen sind nur Regeln, die nur dann greifen sollen, wenn eine E-Mail an eine bestimmte Adresse Ihres Postfachs eingeht.**

Regeln, die grundsätzlich für **alle** eingehenden E-Mails gelten sollen, funktionieren weiterhin wie gewünscht und erfordern keine Änderungen.

______________________________________________________________________

## Empfohlene Alternativen bei betroffenen Regeln

Falls Sie eine betroffene Weiterleitungsregel eingerichtet haben, wählen Sie bitte eine der folgenden Alternativen:

### 💡 Alternative 1 (Unsere Empfehlung!)

Bei Weiterleitungsregeln lassen Sie die betroffene Mailadresse durch den IT-Support auf ein **neues oder ein bereits vorhandenes Funktionspostfach** übertragen.

- **Vorteil:** Die Mails gehen nicht über Ihr persönliches Postfach, sondern kommen direkt im Funktionspostfach an und müssen gar nicht erst umgeleitet werden. Das Funktionspostfach kann von mehreren Personen eingebunden werden, was die gemeinsame Arbeit verbessert.

### 👤 Alternative 2

Bei Weiterleitungsregeln, bei denen die Mails nur an eine einzelne Person weitergeleitet werden, kann der IT-Support die betroffene Mailadresse in das **Postfach der anderen Person** übertragen lassen.

- **Vorteil:** Die Mails müssen nicht über Ihr Postfach laufen, sondern kommen direkt bei der Wunschperson an. Eine Weiterleitung ist damit nicht mehr notwendig.

### ⚙️ Alternative 3: Anpassung der vorhandenen Regel

Sie können die vorhandene Regel wie unten gezeigt anpassen.
**⚠️ Bitte beachten Sie:** Bei dieser Lösung werden **alle** Mails verarbeitet, die die gewünschte Adresse im Briefkopf (= Empfänger\*in, CC, Betreff) enthalten. Das bedeutet, es werden auch alle Mails verarbeitet, die die entsprechende Adresse im Betreff-Feld enthalten.

______________________________________________________________________

## Anleitung: Anpassung der Postfachregel (Alternative 3)

Folgen Sie diesen Schritten, um die Regel anzupassen:

**Schritt 1:** Rufen Sie die [Outlook Web App (OWA)](https://exchange.uni-mannheim.de) auf.

**Schritt 2:** Geben Sie unter „Uni-ID“ Ihre Uni-ID und unter „Kennwort“ das zu Ihrer Uni-ID zugehörige Passwort ein. Klicken Sie anschließend auf „Anmelden“.

**Schritt 3:** Sie gelangen zu Ihrem Postfach. Klicken Sie dort rechts oben auf das Zahnrad, um auf die Einstellungen zu gelangen und anschließend auf „Optionen“.

**Schritt 4:** Klicken Sie im sich öffnenden Menü auf „Posteingangs- und Aufräumregeln“ und dort auf das „+“-Symbol.

**Schritt 5:** Geben Sie einen Namen für die Regel ein und klicken Sie dann unter „Wenn die Nachricht eintrifft […]“ auf das Dropdown-Menü, dort auf „Enthält diese Wörter“ und dann auf „in der Nachrichtenkopfzeile…“.

**Schritt 6:** Tragen Sie nun in das obere Feld die gewünschte Adresse ein (hier die beispielhafte Adresse aus dem Diagramm). Klicken Sie dann auf das „+“-Symbol und danach auf den „OK“-Button.

- **Achtung bei Teil-Suchtreffern:** Wenn Sie beispielsweise „`unituni-mannheim.de`“ eintragen und dieses Postfach auch die Adresse „`sekretariat.unituni-mannheim.de`“ hat, greift die Regel auch bei dieser Adresse, da der Suchbegriff „`unituni-mannheim.de`“ in der längeren Adresse enthalten ist. In solchen Fällen sollten Sie die Alternativen 1 und 2 erneut in Betracht ziehen oder lassen Sie diese Alias-Adresse aus.

**Schritt 7:** Wählen Sie nun die gewünschte Aktion aus, die mit E-Mails an diese Adresse ausgeführt werden soll. In den meisten Fällen sind dies Weiter- oder Umleitungen.

- **Weiterführende Hilfe:** Für die Einrichtung der Aktion (Weiterleitung) können Sie mit folgender Anleitung weitermachen: [https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/weiterleitung-einrichten/](https://www.uni-mannheim.de/it/anleitungen/microsoft-exchange/weiterleitung-einrichten/)
