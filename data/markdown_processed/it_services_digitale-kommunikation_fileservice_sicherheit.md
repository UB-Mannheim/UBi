---
title: Sicherheitsaspekte des zentralen Fileservice und des Uni-Netzes
source_url_de: https://www.uni-mannheim.de/it/services/digitale-kommunikation/fileservice/sicherheit/
source_url_en: https://www.uni-mannheim.de/en/
category: Benutzung
tags: ['Sicherheit', 'Fileservice', 'VPN', 'Verschlüsselung', 'Uni-ID', 'Zugriffsberechtigung', 'Daten', 'Angriff']
language: de
---

# Sicherheitsaspekte des zentralen Fileservice

## Schutz gegenüber Angriffen von Außen

Daten, die auf Netzlaufwerken abgelegt werden, sind grundsätzlich Angriffen über das Netz ausgesetzt, die trotz aller technischen Abwehrmaßnahmen nie vollständig ausgeschlossen werden können.

Um das Risiko solcher Angriffe zu minimieren und gleichzeitig den Nutzern der Universität den Zugriff auf ihre Daten von außen zu ermöglichen, ist der Zugang zum zentralen Fileservice **ausschließlich über den VPN-Client** möglich.

### Technische und organisatorische Anforderungen

- **VPN-Nutzung:** Der Zugang zum Universitätsnetz und den dort angebotenen Diensten setzt eine gültige Uni-ID und das zugehörige Passwort voraus. Dies schränkt den Kreis potenzieller Angreifer erheblich ein. Zudem wird der gesamte Datenverkehr durch den VPN-Client verschlüsselt, was die Sicherheit des Datentransfers gewährleistet.
- **Verschlüsselung:** Zur Erhöhung der Sicherheit kann zusätzlich ein Programm zur Verschlüsselung eingesetzt werden.
- **Zugriffsberechtigung:** Der Schutz vor unberechtigtem Zugriff auf einzelne Dateien und Verzeichnisse wird durch das zugrunde liegende Zugriffsberechtigungssystem mit Hilfe von ACLs (Access-Control-Lists) bewerkstelligt. Als Voreinstellung sind die Zugriffsrechte in den HOME-Verzeichnissen so gesetzt, dass nur der/die Eigentümer/in selbst irgendwelche Zugriffsrechte besitzt.

### Verantwortung der Nutzer

Die Nutzung des zentralen Fileservice erfordert von den Nutzern folgende Verpflichtungen:

1. **Datenverantwortung:** Auf Shares des zentralen Fileservices dürfen keine „personenbezogenen Daten“ abgelegt werden, die nicht verschlüsselt sind. Die Verschlüsselung muss durch die Personen selbst erfolgen. Die Personen sind selbst juristisch für die Daten verantwortlich.
1. **Verordnungen:** Personen, die den zentralen Fileservice nutzen, sind verpflichtet, die Vorgaben der [Verordnungen](https://www.uni-mannheim.de/media/Einrichtungen/it/Benutzerordnung_und_wichtige_Dokumente/Benutzungsordnung_Informationssysteme_Universitaet_Mannheim.pdf) einzuhalten.
1. **Sicheres Verhalten:** Nutzer müssen den sorgfältigen Umgang mit der eigenen Uni-ID und dem zugehörigen Passwort gewährleisten. Jeder angeschlossene Rechner trägt das gleiche Risiko, Opfer eines Angriffs zu werden.
