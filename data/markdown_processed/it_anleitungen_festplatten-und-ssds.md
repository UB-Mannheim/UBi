---
title: Anleitung zum sicheren Löschen von Daten von Festplatten (HDD & SSD)
source_url_de: https://www.uni-mannheim.de/it/anleitungen/festplatten-und-ssds/
source_url_en: https://www.uni-mannheim.de/en/it/instructions/hard-drives-and-ssds/
category: Services
tags: ['Datenlöschung', 'Festplatte', 'SSD', 'ShredOS', 'sicheres Löschen', 'HDD', 'ATA Secure Erase']
language: de
---

# Sicheres Löschen von Daten von Festplatten und SSDs

Um Daten von nicht mehr genutzten Speichermedien zu entfernen, ist ein sicheres Löschen unerlässlich, um eine Wiederherstellung der Daten zu verhindern. Ein einfaches Löschen oder klassisches Formatieren von Laufwerken ist hierfür nicht ausreichend.

Die Methode hängt vom Speichertyp ab:

- **HDDs (klassische Festplatten):** Das sichere Löschen erfolgt durch das mehrfache Überschreiben der gespeicherten Daten mit Zufallsdaten.
- **SSDs:** Hier wird der spezielle Befehl „ATA Secure Erase“ verwendet.

______________________________________________________________________

## 💾 Sicheres Löschen von HDDs (Klassische Festplatten)

### 📋 Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass folgende Punkte erfüllt sind:

- Die zu löschende Festplatte ist entweder noch im PC verbaut oder kann über einen USB-Adapter angeschlossen werden.
- Ein leerer USB-Stick.
- Ein PC mit Internetverbindung und Zugriff auf ein Admin-Konto.

### 🛠️ Schritt 1: Erstellen des ShredOS Bootsticks

Wir verwenden die kostenlose Software [ShredOS](https://github.com/PartialVolume/shredos.x86_64) zur sicheren Datenlöschung.

**Vorbereitung:**

1. Verbinden Sie den USB-Stick mit dem PC.
1. Laden Sie die neueste Version von [ShredOS](https://github.com/PartialVolume/shredos.x86_64) herunter.
1. Wählen Sie die Datei „... for USB Vanilla DRM“ (z.B. „ShredOS .img x86_64bit for USB Vanilla DRM“).

**Bootstick erstellen nach Betriebssystem:**

- **Unter Windows (mit Rufus):**
  1. Laden Sie Rufus von [hier](https://rufus.ie/de/) herunter und führen Sie die Installationsdatei aus.
  1. Wählen Sie das Ziel-USB-Laufwerk.
  1. Fügen Sie die heruntergeladene Image-Datei von ShredOS per Drag-and-Drop hinzu.
  1. Starten Sie den Schreibvorgang. **Achtung:** Alle Daten auf dem USB-Stick werden unwiederbringlich gelöscht.
- **Unter macOS (mit Etcher):**
  1. Laden Sie Etcher von [hier](https://etcher.balena.io/) herunter und installieren Sie es.
  1. Wählen Sie „Flash from file“ und öffnen Sie die ShredOS Image-Datei.
  1. Wählen Sie den gewünschten USB-Stick als Ziel. **Achtung:** Alle Daten auf dem ausgewählten USB-Stick werden unwiederbringlich gelöscht.
  1. Klicken Sie auf „Flash“ und warten Sie, bis der Vorgang abgeschlossen ist.
- **Unter Linux:**
  - Verwenden Sie [Etcher](https://etcher.balena.io/) oder ähnliche Tools.

### 🚀 Schritt 2: Durchführung der Datenlöschung

1. Entfernen Sie den USB-Stick sicher vom System und schließen Sie ihn an den PC an, dessen Festplatte gelöscht werden soll.
1. Starten Sie den PC und wählen Sie im Boot-Menü (oft über F12 erreichbar) den USB-Stick als Startlaufwerk.
1. ShredOS startet vom USB-Stick.
1. Wählen Sie die zu löschenden Festplatten aus (durch Pfeiltasten wechseln und mit der Leertaste auswählen).
1. Starten Sie den Löschvorgang, indem Sie **Shift + S** drücken.
1. Der Prozess wird angezeigt. Sie können den USB-Stick bereits in dieser Phase vom PC trennen.

______________________________________________________________________

## 💿 Sicheres Löschen von SSDs

### ⚠️ Wichtige Hinweise

Das Löschen von SSDs ist technisch anspruchsvoller als bei HDDs, da die interne Struktur und Datenspeicherung anders sind. Es muss zwingend der Befehl **„ATA Secure Erase“** verwendet werden.

**Voraussetzung:**

- Ein PC mit Windows, auf dem die SSD als zusätzliches Laufwerk eingebaut ist.
- Die Software des jeweiligen Produktionsherstellers.

**Wichtig:** Die SSD darf beim Ausführen des „ATA Secure Erase“-Befehls **nicht** über einen USB-Adapter an dem ausführenden Rechner angeschlossen sein, da dies zu einem Funktionsverlust führen kann.

### 🔗 Hersteller-Software

Die benötigte Software kann auf den folgenden Seiten heruntergeladen werden:

- [Samsung](https://www.samsung.com/de/ssd/magiciansoftware/)
- [Crucial](https://www.crucial.de/support/storage-executive)
- [Kingston](https://www.kingston.com/de/support/technical/ssdmanager)
- [Intel](https://www.intel.de/content/www/de/de/support/articles/000006231/memory-and-storage.html)
- [Kioxia](https://europe.kioxia.com/de-de/personal/software/ssd-utility.html)
- [SanDisk und Western Digital](https://support-de.sandisk.com/app/answers/detailweb/a_id/50714)
