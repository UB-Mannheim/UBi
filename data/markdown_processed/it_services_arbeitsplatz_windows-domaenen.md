---
title: Windows Domänen-Verwaltung und -Nutzung an der Universität Mannheim
source_url_de: https://www.uni-mannheim.de/it/services/arbeitsplatz/windows-domaenen/
source_url_en: https://www.uni-mannheim.de/en/it/services/workplace/windows-domains/
category: Services
tags: ['Windows', 'Domäne', 'IT', 'Verwaltung', 'Active Directory', 'Benutzer', 'Arbeitsplatz', 'Uni-ID']
language: de
---

# Windows Domänen an der Universität Mannheim

Die Universitäts-IT betreibt eine zentrale Windows Domäne für die Universität (`ad.uni-mannheim.de`). Diese Domäne wird über die Seite [MyUni-ID](https://id.uni-mannheim.de/login.php?ref=index.php) der Universitäts-IT synchronisiert.

Mit der Windows-Domäne werden alle Aufgaben, die mit der Verwaltung von Uni-IDs verbunden sind, an die Domäne delegiert und von dieser automatisch erledigt. Die Nutzung der Windows-Domäne ist besonders vorteilhaft, je größer die Anzahl der Arbeitsplätze ist, an denen sich unterschiedliche Personen anmelden. Dies vermeidet die Notwendigkeit, die Uni-IDs für jeden einzelnen Rechner manuell einzutragen. Alle Personen, die in der Domäne eingetragen sind, können sich somit anmelden.

**Vorteile der Domänenmitgliedschaft:**

- **Einheitliche Verwaltung:** Besonders interessant für Einrichtungen, die eine größere Anzahl von Rechnern betreiben und die Benutzerverwaltung vereinheitlichen und automatisieren möchten.
- **Zentrale Ressourcen:** Die Nutzung lohnt sich auch für Rechner, die auf zentrale Ressourcen wie den zentralen File-Service zugreifen.
- **Organisation:** Die Mitgliedschaft erleichtert die Organisation eines Rechnerverbundes an einem Lehrstuhl, da Nutzungsberechtigungen für private oder zentrale DV-Ressourcen mithilfe von Gruppenberechtigungen im Active Directory (dem Verzeichnis-Dienst von Windows) mit geringem Aufwand verwaltet werden können.

*Hinweis:* Wenn eine größere Anzahl von Arbeitsplätzen in die Domäne integriert werden soll, ist die Einrichtung einer Organisations-Einheit (OU) zweckmäßig, was eine umfassende Planung erfordert.

## Hinweise zur Mitgliedschaft in der Domäne

### Abhängigkeit von Domain Controllern

Durch die Mitgliedschaft in der Domäne entsteht eine zwangsläufige Abhängigkeit von funktionierenden Domain Controllern. Da die Authentifizierung der Accounts nicht mehr lokal, sondern an der Domäne vorgenommen wird, sind reibungslos funktionierende und rund um die Uhr verfügbare Domain Controller die vitale Voraussetzung für den Betrieb einer Windows-Domäne.

Um negative Auswirkungen dieser Abhängigkeit zu vermeiden, wurde die technische Infrastruktur für den Betrieb der Domain Controller so redundant wie möglich ausgebaut. Dennoch ist es wichtig zu wissen, dass an jedem Arbeitsplatz nach wie vor eine lokale Anmeldung möglich ist, wodurch die negativen Konsequenzen eines Totalausfalls der Domäne begrenzt sind. Ein solcher Totalausfall ist seit der Existenz der Domäne (seit 2002) noch nie aufgetreten.

### Domänen-Administration und Rechte

Eine Domäne ist ein technisches Mittel zur Organisation eines ausgedehnten Rechnerverbundes, dessen wesentliches Merkmal die zentrale Verwaltbarkeit ist, insbesondere in der einheitlichen Benutzerverwaltung.

**Administrative Rechte:**
Die zentrale Verwaltung setzt einen Agenten voraus, der auf allen beteiligten Systemen entsprechende administrative Rechte besitzt. Standardmäßig (Windows-Voreinstellung) besitzen Domänen-Admins auf allen Mitgliedsrechnern administrative Rechte. Ein lokaler Administrator kann diesen Rechten jedoch entziehen und den Rechner damit gegen externe Einflüsse sperren. Grundsätzlich verfügen die Domänen-Admins jedoch über die Mittel, solche Sperren wieder rückgängig zu machen.

**Sicherheitskonzept der Uni Mannheim:**
In der Praxis wird von den weitreichenden Rechten des Domänen-Admins an der Universität Mannheim kein Gebrauch gemacht, da die Administration der Arbeitsplätze nicht Aufgabe der Universitäts-IT ist. Die Universitäts-IT beschränkt die Zugriffsmöglichkeiten des Domänen-Admins daher auf das technisch notwendige Minimum, um die Sicherheit der Arbeitsplätze zu erhöhen und den Schutz vor unbeabsichtigten Auswirkungen zentraler Aktionen zu verbessern. Wird zur Aufnahme von Rechnern in die Domäne die von der Universitäts-IT bereitgestellte Skripte genutzt, werden den Domänen-Admins die administrativen Rechte für die Arbeitsplätze automatisch wieder entzogen.
