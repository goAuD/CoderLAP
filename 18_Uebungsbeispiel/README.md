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

- `01_Anforderung_und_Setup`
- `02_Eingabe_Formular_mit_Framework`
- `03_Gueltigkeitspruefung_der_SV_Nummer`
- `04_Ausgabe_eines_QR_Codes`
- `05_QR_Code_Pruefung_und_Tools`

### Konkrét mintamegoldás

- `06_Musterloesung_Minimal/index.html`
- `06_Musterloesung_Minimal/styles.css`
- `06_Musterloesung_Minimal/app.js`
- `06_Musterloesung_Minimal/vendor/qrcode.js`

## Vizsgastratégia

Ha ezt vizsgán kell megcsinálni, akkor a sorrend legyen:

1. működő űrlap
2. kötelező mezők ellenőrzése
3. `SV-Nr` validálás
4. `QR` generálás
5. végső ellenőrzés scannerrel

Ez jobb stratégia, mint túl korán extra funkciókat építeni.

## Mit tudunk igazolni a végén?

| Követelmény | Ellenőrzés |
|---|---|
| Kötelező névmezők és SV-NR | üres és csak szóközös mezőknél visszajelzés, eredmény nélkül |
| Formai SV-ellenőrzés | a PDF három pozitív és három negatív mintája |
| Pontos QR-tartalom | külön olvasóval `Richtig`, illetve `Falsch` |
| Új bevitel | a régi QR eltűnik; az új eredmény új ellenőrzésből készül |
| Reszponzív űrlap | keskeny nézet, nagyítás és billentyűzetes kitöltés |

A formai ellenőrzés azt állapítja meg, hogy a szám megfelel-e a megvalósított
formátum- és ellenőrzőszám-szabályoknak. Nem igazolja, hogy egy adott személyhez
valóban ezt a számot rendelte a biztosító, vagy hogy fennáll a biztosítási jogviszonya.
A névmezők kitöltését ellenőrizzük, a név és a szám összetartozását nem.

A PDF 11–12. oldalát 2026-10-14-én ismét összevetettük a megoldással.
A példákat a feladatlap adataival és kitalált nevekkel futtatjuk.
Vizsgán a PDF telefonhasználati tilalma miatt előre egyeztetett asztali olvasó szükséges.

## Gyors önellenőrzés

1. Mit tartalmazhat a QR?
2. Mit igazol a helyes ellenőrzőszám?
3. Kell-e adatbázis a PDF feladatához?

## Rövid válaszok az önellenőrzéshez

1. Pontosan a Richtig vagy Falsch szót.
2. Formai összefüggést a számjegyek között; nem a szám valódi kiadását vagy a biztosítási jogviszonyt.
3. Nem, adattárolást a PDF nem kér.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Használat: elsődleges feladatszöveg és elvárásrendszer.

2. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135  
   Használat: hivatalos Prüfziffer-logika a `SV-Nr` ellenőrzéséhez.

Megnyitva: `2026-04-09`
