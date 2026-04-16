# Uebungsbeispiel

## Gyors vizuális kép

```text
Űrlap
    -> kötelező mezők ellenőrzése
    -> SV-Nr ellenőrzése
    -> eredmény: Richtig / Falsch
    -> QR-kód generálás
    -> QR-kód ellenőrzése scannerrel
```

## Hivatalos feladatértelmezés a PDF alapján

A rootban lévő PDF (`2026-04-09`-én újraellenőrizve) a `18)` blokkban ezt várja el:

1. HTML-form `Vorname`, `Nachname`, `SV-NR` mezőkkel
2. responsive kialakítás, lehetőleg frameworkkel, például `Bootstrap`
3. az osztrák `SV`-szám érvényességvizsgálata
4. `QR`-kód generálása
5. a QR-kód tartalma csak `Richtig` vagy `Falsch` lehet
6. a QR-kód ellenőrzése külön toollal

## A projektben választott minimál megoldás

Azért, hogy ez vizsgán is reálisan megoldható legyen, itt egy **tudatosan egyszerű** mintamegoldás készül:

- egyetlen `index.html`
- egyetlen `app.js`
- kevés saját `CSS`
- `Bootstrap` a gyors és responsive űrlaphoz
- helyi `QR`-library a kódgeneráláshoz

## Megoldási terv

### 1. Anforderung und Setup

- a feladat céljának tisztázása
- minimális szükséges eszközlista
- egyszerű projektstruktúra

### 2. Eingabe-Formular mit Framework

- `Bootstrap`-alapú űrlap
- kötelező mezők ellenőrzése
- mobilon és desktopon is jól használható elrendezés

### 3. Gültigkeitsprüfung der SV-Nummer

- a PDF-ben megadott mintaszámokkal ellenőrizhető
- az osztrák hivatalos Prüfziffer-logika alapján

### 4. Ausgabe eines QR-Codes

- a payload csak `Richtig` vagy `Falsch`
- nincs szükség adatbázisra
- nincs szükség szerveroldali mentésre

### 5. QR-Code Prüfung und Tools

- külön asztali scannerrel ellenőrizhető
- a cél itt a működő vizsgafeladat, nem extra funkciók gyártása

## Fájlok

### Elméleti és vizsgafelkészítő bontás

- [01_Anforderung_und_Setup/README.md](./01_Anforderung_und_Setup/README.md)
- [02_Eingabe_Formular_mit_Framework/README.md](./02_Eingabe_Formular_mit_Framework/README.md)
- [03_Gueltigkeitspruefung_der_SV_Nummer/README.md](./03_Gueltigkeitspruefung_der_SV_Nummer/README.md)
- [04_Ausgabe_eines_QR_Codes/README.md](./04_Ausgabe_eines_QR_Codes/README.md)
- [05_QR_Code_Pruefung_und_Tools/README.md](./05_QR_Code_Pruefung_und_Tools/README.md)

### Konkrét mintamegoldás

- [06_Musterloesung_Minimal/README.md](./06_Musterloesung_Minimal/README.md)
- [06_Musterloesung_Minimal/index.html](./06_Musterloesung_Minimal/index.html)
- [06_Musterloesung_Minimal/styles.css](./06_Musterloesung_Minimal/styles.css)
- [06_Musterloesung_Minimal/app.js](./06_Musterloesung_Minimal/app.js)

## Vizsgastratégia

Ha ezt vizsgán kell megcsinálni, akkor a sorrend legyen:

1. működő űrlap
2. kötelező mezők ellenőrzése
3. `SV-Nr` validálás
4. `QR` generálás
5. végső ellenőrzés scannerrel

Ez jobb stratégia, mint túl korán extra funkciókat építeni.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Használat: elsődleges feladatszöveg és elvárásrendszer.

2. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135  
   Használat: hivatalos Prüfziffer-logika a `SV-Nr` ellenőrzéséhez.

Megnyitva: `2026-04-09`
