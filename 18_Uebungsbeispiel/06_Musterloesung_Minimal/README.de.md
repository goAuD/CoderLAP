# Musterlösung Minimal

## Ziel

Dies ist eine bewusst einfache, prüfungstaugliche Musterlösung für den Block `18_Uebungsbeispiel`.

## Dateien

- [index.html](./index.html)
- [styles.css](./styles.css)
- [app.js](./app.js)
- [vendor/qrcode.js](./vendor/qrcode.js)

## Was kann sie?

- Responsives Formular mit `Bootstrap`
- Pflichtfeldvalidierung
- Österreichische `SV-Nr` Validierung
- `QR`-Code Generierung mit Inhalt `Richtig` / `Falsch`

## Was kann sie nicht?

- Datenspeicherung
- Backend
- Datenbank
- Extra UX- oder Admin-Funktionen

## Ausführung

1. Öffne die Datei [index.html](./index.html) im Browser.
2. Fülle die Felder aus.
3. Klicke auf den Button.
4. Überprüfe das angezeigte Ergebnis und den `QR`-Code.

## Empfohlene Testdaten

### Gültig

- `4422 180599`
- `3567 010705`
- `5884 050902`

### Ungültig

- `2511 010100`
- `5255 121299`
- `4999 070700`

## Quellen

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`

2. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135

3. Bootstrap Docs  
   https://getbootstrap.com/docs/5.3/getting-started/introduction/

4. qrcode-generator package  
   https://www.npmjs.com/package/qrcode-generator

Abgerufen: `2026-04-09`
