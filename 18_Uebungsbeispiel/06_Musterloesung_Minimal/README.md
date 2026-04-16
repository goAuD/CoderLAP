# Musterloesung Minimal

## Cél

Ez egy tudatosan egyszerű, vizsgabarát mintamegoldás a `18_Uebungsbeispiel` blokkhoz.

## Fájlok

- `index.html`
- `styles.css`
- `app.js`
- `vendor/qrcode.js`

## Mit tud?

- responsive űrlap `Bootstrap`-pel
- kötelező mezők ellenőrzése
- osztrák `SV-Nr` validálása
- `QR`-kód generálása `Richtig` / `Falsch` tartalommal

## Mit nem tud?

- adatmentés
- backend
- adatbázis
- extra UX vagy admin funkciók

## Futtatás

1. Nyisd meg az `index.html` fájlt böngészőben.
2. Töltsd ki a mezőket.
3. Kattints a gombra.
4. Ellenőrizd a megjelenő eredményt és a `QR`-kódot.

## Ajánlott tesztadatok

### Érvényes

- `4422 180599`
- `3567 010705`
- `5884 050902`

### Érvénytelen

- `2511 010100`
- `5255 121299`
- `4999 070700`

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`

2. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135

3. Bootstrap Docs  
   https://getbootstrap.com/docs/5.3/getting-started/introduction/

4. qrcode-generator package  
   https://www.npmjs.com/package/qrcode-generator

Megnyitva: `2026-04-09`
