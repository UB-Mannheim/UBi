---
title: Nameserver und DNS-Dienste der Universität Mannheim
source_url_de: None
source_url_en: https://www.uni-mannheim.de/en/it/services/internet-and-servers/name-server/
category: Services
tags: ['Nameserver', 'DNS', 'IT-Dienste', 'IPv4', 'IPv6', 'Domainstruktur', 'Uni Mannheim']
language: de
---

## Nameserver und DNS-Dienste

Die Universitäts-IT betreibt die zentralen Nameserver (DNS-Server) für die Universität Mannheim.

### Technische Adressen der Nameserver

Die Nameserver sind sowohl über IPv4 als auch über IPv6 erreichbar:

**Über IPv4:**

- `134.155.96.51` (dns1.uni-mannheim.de)
- `134.155.96.52` (dns2.uni-mannheim.de)
- `134.155.96.53` (dns3.uni-mannheim.de)

**Über IPv6:**

- `2001:7c0:2900:60::869b:6033` (dns1.uni-mannheim.de)
- `2001:7c0:2900:60::869b:6034` (dns2.uni-mannheim.de)
- `2001:7c0:2900:60::869b:6035` (dns3.uni-mannheim.de)

### Funktionen und Zuständigkeiten

Nameserver sind für folgende Aufgaben zuständig:

- **Adressübersetzung:** Umsetzung von öffentlichen und privaten IP-Adressen zu System-Namen und umgekehrt.
- **Mailrouting:** Bereitstellung von Informationen zum Mailrouting.
- **Autorität:** Sie sind für die Verbreitung registrierter IP-Adressen, System-Namen und des Mailroutings für die eingetragenen Mailadressen der von der Universität betriebenen Domains nach außen hin zuständig (authoritative Nameserver).

### Abgedeckte Domains und Netze

Die Nameserver sind autoritativ für folgende Domains und Netze:

- `uni-mannheim.de`
- `uni-mannheim.eu`
- Netze `134.155.x.x`
- Netze `2001:7c0:600::`
- Zusätzlich werden auch Domains von Einrichtungen und Kooperationen der Universität Mannheim abgedeckt.

### Erweiterung der Domainstruktur

- **Andere Domains:** Bei entsprechender Notwendigkeit und Befürwortung besteht die Möglichkeit, andere Domains auf Servern innerhalb des Universitätsnetzes zu betreiben. Das Vorgehen hierzu ist unter [virtueller Webserver](https://www.uni-mannheim.de/it/services/internet-und-server/webhosting/#c223943) beschrieben.
- **Weitere Informationen:** Allgemeine Informationen über die Domainstruktur der Universitätsnetze in Baden-Württemberg finden Sie beim [BelWü](https://www.belwue.de/angebot/dienste/nameserver.html).
