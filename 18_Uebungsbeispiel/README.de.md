# Übungsbeispiel

## Schneller visueller Überblick

```text
Formular
    -> Pflichtfelder prüfen
    -> SV-Nr prüfen
    -> Ergebnis: Richtig / Falsch
    -> QR-Code generieren
    -> QR-Code mit Scanner prüfen
```

## Offizielle Aufgabenstellung laut PDF

Die PDF (`2026-04-09` erneut geprüft) verlangt im Block `18)` folgendes:

1. HTML-Formular mit `Vorname`, `Nachname`, `SV-NR`
2. Responsives Design, idealerweise mit einem Framework wie `Bootstrap`
3. Gültigkeitsprüfung der österreichischen `SV`-Nummer
4. `QR`-Code Generierung
5. Inhalt des QR-Codes darf nur `Richtig` oder `Falsch` sein
6. Überprüfung des QR-Codes mit einem separaten Tool

## Gewählter Minimalansatz im Projekt

Damit die Aufgabe auch unter Prüfungsbedingungen realistisch umsetzbar bleibt, wird hier eine **bewusst einfache** Musterlösung erstellt:

- eine einzige `index.html`
- eine einzige `app.js`
- wenig eigenes `CSS`
- `Bootstrap` für ein schnelles, responsives Formular
- lokale `QR`-Library zur Codegenerierung

## Lösungsplan

### 1. Anforderung und Setup

- Klärung des Aufgabenziels
- minimale Werkzeugliste
- einfache Projektstruktur

### 2. Eingabe-Formular mit Framework

- `Bootstrap`-basiertes Formular
- Pflichtfeldvalidierung
- Layout für Mobil und Desktop

### 3. Gültigkeitsprüfung der SV-Nummer

- Prüfbar mit den in der PDF angegebenen Musternummern
- Basiert auf der offiziellen österreichischen Prüfziffer-Logik

### 4. Ausgabe eines QR-Codes

- Payload nur `Richtig` oder `Falsch`
- Keine Datenbank erforderlich
- Keine serverseitige Speicherung nötig

### 5. QR-Code Prüfung und Tools

- Überprüfbar mit einem separaten Desktop-Scanner
- Ziel ist eine funktionsfähige Prüfungsaufgabe, keine Extra-Features

## Dateien

### Theoretische und prüfungsvorbereitende Aufteilung

- `01_Anforderung_und_Setup`
- `02_Eingabe_Formular_mit_Framework`
- `03_Gueltigkeitspruefung_der_SV_Nummer`
- `04_Ausgabe_eines_QR_Codes`
- `05_QR_Code_Pruefung_und_Tools`

### Konkrete Musterlösung

- `06_Musterloesung_Minimal/index.html`
- `06_Musterloesung_Minimal/styles.css`
- `06_Musterloesung_Minimal/app.js`
- `06_Musterloesung_Minimal/vendor/qrcode.js`

## Prüfungsstrategie

Bei der Umsetzung in der Prüfung empfiehlt sich folgende Reihenfolge:

1. Funktionierendes Formular
2. Pflichtfeldvalidierung
3. `SV-Nr` Validierung
4. `QR` Generierung
5. Abschlussprüfung mit Scanner

Diese Strategie ist besser, als zu früh an Extra-Features zu arbeiten.

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Verwendung: Primärer Aufgabentext und Anforderungssystem.

2. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135  
   Verwendung: Offizielle Prüfziffer-Logik für die `SV-Nr` Validierung.

Abgerufen: `2026-04-09`
