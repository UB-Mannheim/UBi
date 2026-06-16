---
title: Anleitung zur Nutzung des Passwort-Managers KeePass
source_url_de: N/A
source_url_en: https://www.uni-mannheim.de/en/information-security/information-material/keepass-instructions/
category: Benutzung
tags: ['Passwort-Manager', 'KeePass', 'Passwortsicherheit', 'Datenbank', 'Installation', 'Uni Mannheim', 'Zugangsdaten']
language: de
---

# KeePass: Anleitung zur Nutzung des Passwort-Managers

Ein Passwort Manager dient als sicherer Tresor, in dem Sie Ihre Passwörter speichern können, um bei Bedarf darauf zugreifen zu können. Die Universität Mannheim stellt keinen Passwort Manager zentral zur Verfügung, weshalb wir Ihnen den kostenlosen Passwort Manager „KeePass“ empfehlen.

**⚠️ Wichtige Sicherheitshinweise:**

- Laden Sie KeePass **nur** über die in dieser Anleitung genannten Links herunter.
- Seien Sie vorsichtig: Angreifer bauen Webseiten nach, um Sie zum Download von Schadprogrammen zu verleiten.
- **Hinweis:** Die folgenden Anleitungen beziehen sich auf Windows-Systeme. Für andere Betriebssysteme finden Sie die Version unter [https://keepass.info/](https://keepass.info/).

## ⚙️ 1. Installation und Einrichtung

### 1.1 KeePass herunterladen

1. **Download der Anwendung:** Laden Sie die „Professional Edition Portable“ Version von KeePass unter folgendem Link herunter: [https://www.heise.de/download/product/keepass-15712/download](https://www.heise.de/download/product/keepass-15712/download).
1. **Sprachpaket (Optional):** Das deutsche Sprachpaket können Sie auf der Herstellerseite herunterladen. Klicken Sie dort links auf „Translations“ und wählen Sie „German“ mit der aktuellsten Version aus.
1. **Überprüfung der Integrität (Wichtig):**
   - Rechtsklicken Sie auf die heruntergeladene Zip-Datei und zeigen Sie den Hash-Wert über „CRC-SHA“ -> „SHA-256“ an (Dafür ist ggf. 7-Zip nötig).
   - Vergleichen Sie diesen Wert mit dem Hash-Wert der Original-Datei, den Sie unter [https://keepass.info/integrity.html](https://keepass.info/integrity.html) finden.
   - **Nur wenn die Hash-Werte übereinstimmen**, können Sie mit der Installation fortfahren. Stimmen sie nicht überein, wenden Sie sich bitte an den IT-Support (Tel.: +49 621 181–2000 oder E-Mail: [IT-Support-E-Mail]).

### 1.2 KeePass starten und Sprache ändern

1. **Starten:** Entpacken Sie die Zip-Dateien auf Ihrem Desktop und öffnen Sie die Anwendung „KeePass.exe“.
1. **Updates:** Aktivieren Sie zur regelmäßigen Information über Updates „Enable (recommended)“.
1. **Sprache ändern:**
   - Entpacken Sie das deutsche Sprachpaket und kopieren Sie die Datei „German.lngx“ in den Ordner „KeePass-2.41\\Languages“.
   - In KeePass wählen Sie unter „View“ -> „Change Language…“ das deutsche Sprachpaket aus.
   - Starten Sie KeePass anschließend neu.

## 💾 2. Datenbank erstellen und sichern

Bevor Sie Passwörter speichern können, müssen Sie eine neue Datenbank anlegen.

### 2.1 Datenbank-Setup

1. **Neue Datenbank anlegen:** Gehen Sie zu „Datei“ -> „Neu…“ oder klicken Sie über das entsprechende Icon.
1. **Speicherort wählen:** Wählen Sie einen Speicherort und einen Namen für die Datei.
   - **Wichtig:** Der Speicherort muss sicher sein und nur Ihnen zugänglich. Speichern Sie die Datenbank **nicht** im KeePass-Ordner, um zu verhindern, dass sie bei der Löschung einer älteren Version gelöscht wird.
   - *Für Beschäftigte der Verwaltungen:* Es wird ein spezieller Ordner auf dem Netzlaufwerk eingerichtet. Bei Fragen wenden Sie sich bitte an Herrn Martin Stachniss (martin.stachniss@uni-mannheim.de oder -3181).
1. **Hauptschlüssel vergeben:** Geben Sie ein Hauptpasswort ein. Dieses Passwort schützt alle Ihre Passwörter und sollte daher sehr komplex und lang sein (mindestens 12 Zeichen, Groß-/Kleinbuchstaben, Sonderzeichen und Zahlen).

### 2.2 Wahl des Schutzlevels

Sie müssen entscheiden, ob die Datenbank zusätzlich durch eine Schlüsseldatei geschützt werden soll.

#### 🔑 Option A: Datenbank mit Schlüsseldatei schützen (Zwei-Faktor-Authentifizierung)

- **Schlüsseldatei erstellen:** Setzen Sie den Haken bei „Expertenoptionen anzeigen:“ und erstellen Sie eine Schlüsseldatei. Diese dient als zweiter Faktor.
- **Sicherung:** Legen Sie die Schlüsseldatei sicher ab, **getrennt** von der Datenbank. Eine Sicherung (z. B. auf einer verschlüsselten externen Festplatte) ist zwingend erforderlich, da ohne diese Datei die Datenbank nicht mehr zu öffnen ist.
- **Einstellungen:** Fahren Sie mit der Festlegung der Datenbankeinstellungen fort (siehe unten).

#### 🔒 Option B: Datenbank ohne Schlüsseldatei erstellen

- **Empfehlung für Verwaltungskräfte:** Aufgrund der sicheren Ablage in einem speziellen Ordner auf dem Netzlaufwerk ist die Verwendung einer externen Schlüsseldatei nicht möglich. Ein komplexes Hauptpasswort ist daher ausreichend.
- **Vorgehen:** Wählen Sie diese Option und fahren Sie mit der Festlegung der Datenbankeinstellungen fort.

### 2.3 Datenbankeinstellungen festlegen (Gemeinsame Schritte)

1. **Allgemein:** Geben Sie einen beliebigen Datenbanknamen inklusive Beschreibung ein.
1. **Erweitert:** Hier können Sie zusätzliche Einstellungen zum Hauptschlüssel vornehmen, z. B. Werte für die Erinnerung an einen Passwortwechsel festlegen.
1. **Notfallblatt:** Nach dem Bestätigen wird die Datenbank angelegt. Sie können den Punkt des Notfallblattes überspringen.

## 📝 3. Verwaltung und Nutzung der Einträge

### 3.1 Gruppen und Einträge verwalten

- **Neue Gruppe hinzufügen:** Sie können eigene Gruppen erstellen und hinzufügen („Bearbeiten“ -> „Gruppe hinzufügen…“).
- **Gruppe bearbeiten:** Wählen Sie eine bestehende Gruppe aus und führen Sie unter „Bearbeiten“ -> „Gruppe bearbeiten…“ Änderungen durch.
- **Neuen Eintrag hinzufügen:**
  1. Wählen Sie die Zielgruppe aus.
  1. Klicken Sie auf „Bearbeiten“ -> „Eintrag hinzufügen…“.
  1. Geben Sie Titel, Benutzername und Passwort ein.
  1. **Passwort-Generator:** Nutzen Sie das integrierte Icon (Schlüssel und Stern), um ein Passwort generieren zu lassen.

### 3.2 Passwort-Generator einrichten

Um ein eigenes Profil für den Passwort-Generator zu erstellen:

1. Öffnen Sie den Generator über „Extras“ -> „Passwort generieren...“.
1. Wählen Sie bei Profil „(Benutzerdefiniert)“ und treffen Sie Ihre gewünschten Einstellungen (z. B. Groß-/Kleinbuchstaben, Ziffern und Sonderzeichen wie `!@#$%()+=:;",.?/**`).
1. Speichern Sie das Profil unter einem Namen (z. B. „Vorgabe Kennung“) und bestätigen Sie mit „OK“.

### 3.3 Sicherheitseinstellungen anpassen

Nach der Datenbankerstellung sollten Sie folgende Einstellungen vornehmen:

1. **Sperren bei Inaktivität:** Gehen Sie zu „Extras“ -> „Optionen“ und setzen Sie unter „Sicherheit“ den Haken bei „Arbeitsfläche nach KeePass-Inaktivität sperren (Sekunden)“ und geben Sie den Wert 120 ein.
1. **Hauptschlüssel-Sperre:** Setzen Sie den Haken bei „Hauptschlüssel auf sicherem Desktop eingeben“. Dies pausiert Hintergrundprozesse und blockiert potenzielle Keylogger.
1. **Manuelles Sperren:** Sie können KeePass auch manuell über das Icon oder die Tastenkombination **Strg + L** sperren.

### 3.4 Auto-Type deaktivieren

Um zu verhindern, dass Passwörter versehentlich im Klartext sichtbar werden:

1. Wählen Sie die Gruppe aus und gehen Sie zu „Gruppe“ -> „Gruppe bearbeiten…“.
1. Im Reiter „Auto-Type“ wählen Sie die Einstellung „Deaktiviert“.

## 🌐 4. Nutzung und Wartung

### 4.1 Anmeldung an Webseiten und Anwendungen

Um sich anzumelden, muss der entsprechende Eintrag ausgewählt sein:

- **URL:** Bei hinterlegter URL kann diese über „URL(s)“ oder das Weltkugel-Icon geöffnet werden.
- **Benutzername:** Klicken Sie auf das Menschen-Icon oder nutzen Sie „Benutzernamen kopieren“, um den Benutzernamen einzufügen.
- **Passwort:** Klicken Sie auf das Schlüssel-Icon oder nutzen Sie „Passwort kopieren“, um das Passwort einzufügen.

### 4.2 Datenbank aktualisieren

Wenn eine neue portable Version verfügbar ist:

1. **Herunterladen:** Laden Sie die neue Version über [https://www.heise.de/download/product/keepass-15712/download](https://www.heise.de/download/product/keepass-15712/download) herunter.
1. **Starten:** Führen Sie die Schritte „Download“, „KeePass starten“ und „Sprache ändern“ durch.
1. **Alte Datenbank einfügen:** Gehen Sie zu „Datei“ -> „Öffnen“ -> „Datei öffnen…“ und fügen Sie Ihre alte Datenbank hinzu.
1. **Zugriff:** Geben Sie Ihr Hauptpasswort ein (und wählen Sie ggf. die Schlüsseldatei aus).
1. **Aufräumen:** Löschen Sie anschließend den Ordner mit der veralteten KeePass Version. Achten Sie darauf, dass die Datenbank und die Schlüsseldatei nicht in diesem Ordner liegen.
