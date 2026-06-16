---
title: Shibboleth Single Sign-On (SSO) Login und Logout Anleitung
source_url_de: https://www.uni-mannheim.de/it/services/zentrale-authentifizierung/shibboleth-idp/anleitung-login/
source_url_en: https://www.uni-mannheim.de/en/it/services/central-authentication/shibboleth-idp/login-instructions/
category: Benutzung
tags: ['Shibboleth', 'SSO', 'Login', 'Logout', 'Authentifizierung', 'Uni Mannheim', 'Zugang', 'bwidm']
language: de
---

# Shibboleth Single Sign-On (SSO) Login und Logout

## 🔐 Shibboleth SSO Login-Verfahren

Der Login-Prozess ist in mehrere Schritte unterteilt und beginnt immer auf der Webseite des jeweiligen Dienstes.

**1. Dienstauswahl:**
Wählen Sie auf der Startseite des Dienstes die gewünschte Login-Möglichkeit (z.B. „Shibboleth“ oder „bwIDM“).

**2. Hochschule und Föderation:**

- Wählen Sie anschließend Ihre Hochschule („Universität Mannheim“).
- Bei nicht-deutschen Diensten muss zuvor die Föderation „DFN-AAI“ oder „German Higher Education and Research“ ausgewählt werden.
- Der Dienst fragt nach dem Herkunftsort („Where Are You From“ oder WAYF). Bei manchen Diensten (wie bwidm.scc.kit.edu) ist der WAYF-Dienst bereits auf der Startseite integriert.

**3. Authentifizierung:**
Sie werden zum IdP der Universität Mannheim weitergeleitet, wo Sie sich mit Kennung und Passwort authentifizieren.

> **💡 Hinweis:** Um beispielsweise für Support-Zwecke einen bestimmten Schritt zu erzwingen, setzen Sie den Haken bei: „Lösche die frühere Einwilligung zur Weitergabe Ihrer Informationen an diesen Dienst.“

**4. Datenübermittlung:**
Nach der erfolgreichen Authentifizierung werden alle Daten, die an den Dienst gesendet werden sollen, zur Kenntnisnahme angezeigt. Anschließend werden die Daten an den Dienst übermittelt.

**Wichtige Hinweise:**

- **Neuer Dienst:** Benötigen Sie Zugang zu einem Dienst, der bisher nicht unterstützt wird, melden Sie sich bitte bei uns. Wir werden unser Bestes tun, um den Zugang zeitnah zu ermöglichen.
- **Selten genutzte Dienste:** Speziell für Dienste, die Sie nicht regelmäßig verwenden, empfiehlt sich die Option „Bei nächster Anmeldung erneut anzeigen“ auszuwählen.

## 🚪 Logout-Verfahren

Ein Single-Logout (Ausloggen bei allen angemeldeten Diensten auf Knopfdruck) ist aktuell nicht möglich.

**Empfohlene Vorgehensweise:**

1. **Browser schließen:** Schließen Sie den Browser.
1. **Cookies löschen:** Löschen Sie die Cookies.
1. **Sitzenauslaufen:** Die Sitzung des Dienstes läuft nach einiger Zeit automatisch ab.

### Anleitung zum Löschen von Cookies (Beispiel Mozilla Firefox)

Das Löschen der aktuellsten Chronik/des aktuellsten Verlaufs ist der einfachste Weg, um Cookies zu entfernen.

1. Wählen Sie unter „Chronik“ den Punkt „Neueste Chronik löschen...“ aus. (In älteren Browsern ist dies unter „Extras“ zu finden; Shortcut: `Strg + Umschalt + Entf`).
1. Wählen Sie den gewünschten Zeitrahmen aus (z.B. „Alles“).
1. Aktivieren Sie nur „Cookies“, „Cache“ und „Aktive Logins“ und klicken Sie auf „Jetzt löschen“.
