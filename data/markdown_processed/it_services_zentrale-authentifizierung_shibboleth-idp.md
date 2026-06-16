---
title: Shibboleth Identity Provider (IdP) und Single Sign-On (SSO) an der Universität Mannheim
source_url_de: https://www.uni-mannheim.de/it/services/zentrale-authentifizierung/shibboleth-idp/
source_url_en: https://www.uni-mannheim.de/en/it/services/central-authentication/shibboleth-idp/
category: Services
tags: ['Shibboleth', 'SSO', 'Single Sign-On', 'Authentifizierung', 'IdP', 'bwIDM', 'Uni Mannheim', 'SAML']
language: de
---

# Shibboleth Identity Provider (IdP) und Single Sign-On (SSO)

Der Shibboleth Identity Provider (IdP) ermöglicht die zentrale Authentifizierung und Autorisierung mittels Single Sign-On (SSO) für verschiedene Dienste. Der IdP ist ein integraler Bestandteil der [bwIDM](https://www.bwidm.de/)-Infrastruktur.

## 💡 Was ist Single Sign-On (SSO)?

Single Sign-On (SSO) ist ein Login-Dienst, der es Nutzern ermöglicht, sich nur einmal einzuloggen, um gleichzeitig Zugang zu mehreren Webseiten zu erhalten.

- **CAS:** Bietet beispielsweise Zugang zum internen Portal der Uni Mannheim.
- **Shibboleth Identity Provider (IdP):** Bietet Zugang zu lokalen Diensten, die von anderen Hochschulen und Einrichtungen betrieben werden.

## 🌐 Wofür wird der IdP benötigt?

Viele wissenschaftliche Dienste sind für eine große Anzahl von Nutzern erreichbar. Anstatt für jede Person ein eigenes Konto anzulegen, nutzen diese Dienste die [SAML-Technologie](https://www.uni-mannheim.de/it/services/zentrale-authentifizierung/shibboleth-idp-dienste/).

Dank des IdP kann das Konto der Heimatuniversität verwendet werden, wodurch die Notwendigkeit eines separaten Kontos entfällt. Der IdP kann alle notwendigen Nutzerdaten an den jeweiligen Dienst übermitteln.

## 🚀 Ablauf des IdP-Logins

Der Anmeldeprozess ist mehrstufig:

1. **Start:** Der Vorgang beginnt auf der Webseite des Ziel-Dienstes, wo Sie eine Login-Möglichkeit (z.B. „Shibboleth“ oder „bwIDM“) auswählen.
1. **Hochschule wählen:** Sie wählen die Hochschule aus, der Sie angehören. Bei nicht-deutschen Diensten muss zuvor die Föderation „DFN-AAI“ oder „German Higher Education and Research“ ausgewählt werden.
1. **Authentifizierung:** Sie werden zum IdP der Universität Mannheim weitergeleitet und authentifizieren sich mit Ihrer Uni-ID und dem zugehörigen Passwort.
1. **Datenübermittlung:** Nach erfolgreicher Authentifizierung werden alle an den Dienst zu sendenden Daten zur Kenntnisnahme angezeigt und anschließend übermittelt. Der Dienst nimmt die Daten entgegen und gewährt in der Regel den Zugriff.

- **Anleitung:** Einen detaillierten Ablauf finden Sie in unserer [Anleitung zum Login](https://www.uni-mannheim.de/it/services/zentrale-authentifizierung/shibboleth-idp/anleitung-login/).
- **Probleme:** Bei Problemen beachten Sie bitte die [Hinweise zu den Diensten](https://www.uni-mannheim.de/it/services/zentrale-authentifizierung/shibboleth-idp-dienste/) oder wenden Sie sich an den [IT-Support](https://www.uni-mannheim.de/it/support/).

## 📚 Verfügbare Dienste

Eine [Liste der eingerichteten Dienste](https://www.uni-mannheim.de/it/services/zentrale-authentifizierung/shibboleth-idp-dienste/) ist auf einer separaten Seite verfügbar. Diese Liste ist nicht abschließend.

- **Baden-Württemberg:** Alle Dienste aus Baden-Württemberg sind auf der [Dienste-Seite von bwIDM](https://www.bwidm.de/dienste/) zu finden und sind auch Dienste der Föderation [DFN-AAI](https://www.aai.dfn.de/der-dienst/).
- **DFN-AAI:** Eine umfassende Liste aller Dienste der DFN-AAI-Föderation ist auf den [Seiten des DFN](https://www.aai.dfn.de/verzeichnis/sp-dfn-aai/) zu finden.

**Wichtig:** Nicht alle DFN-Dienste sind über den IdP der Universität Mannheim nutzbar, da für jeden Dienst ein Datenabgleich notwendig ist. Benötigen Sie Zugang zu einem bisher nicht unterstützten Dienst, melden Sie sich bitte beim [IT-Support](https://www.uni-mannheim.de/it/support/).

## ⚙️ Verwaltung und Sicherheit

### Logout und Sitzungsdauer

- **Single-Logout:** Ein automatisches Ausloggen bei allen angemeldeten Diensten (Single-Logout) ist aktuell nicht möglich.
- **Manuelles Logout:** Zum Ausloggen müssen Sie den Browser schließen oder Cookies löschen.
- **Sitzung:** Die Sitzung ist zeitlich begrenzt. Ist die Sitzung beim Dienst abgelaufen, ist ein erneuter Besuch beim IdP notwendig.

### Passwort und Sprache

- **Passwort vergessen:** Folgen Sie bitte unserer Anleitung [„Passwort vergessen“](https://www.uni-mannheim.de/it/anleitungen/passwort/).
- **Sprache:** Die Sprache im IdP wird automatisch durch die Browsersprache festgelegt.

## 💻 Technische Metainformationen

| Parameter | Wert |
| :--- | :--- |
| **EntityID** | `https://idp.uni-mannheim.de/idp/shibboleth` |
| **Scope** | `uni-mannheim.de` (ausschließlich) |
| **Federations** | German Higher Education and Research (DFN-AAI), eduGAIN |
