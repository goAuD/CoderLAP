# Anforderung und Setup

## Gyors vizuális kép

| Kell | Nem kell |
|---|---|
| HTML | adatbázis |
| `Bootstrap` | felhasználókezelés |
| JavaScript | admin felület |
| QR-library | extra feature-ök |

## Mit kér a feladat?

A PDF alapján:

- Stammdaten-űrlap
- responsive design
- `SV-Nr` validálás
- `QR`-kód generálás
- `QR` ellenőrzés tool segítségével

## Minimális setup

- `Browser`
- `Code Editor`
- egyszerű projektmappa
- `Bootstrap`
- egy helyi `QR`-kód library

## Javasolt mappaszerkezet

```text
Musterloesung_Minimal/
  index.html
  styles.css
  app.js
  vendor/
    qrcode.js
```

## Miért ez a jó vizsgastratégia?

- gyorsan átlátható
- könnyen hibakereshető
- kevés mozgó alkatrészből áll
- időnyomás alatt is reális

## Vizsgán jól használható megfogalmazás

> Ennél a gyakorlati feladatnál a minimális cél egy működő, responsive HTML-űrlap létrehozása, amely ellenőrzi az osztrák `SV-Nr` érvényességét, és ennek eredménye alapján `QR`-kódot generál.  
> A legegyszerűbb megoldás frontend-alapú `HTML`, `Bootstrap` és `JavaScript` használata, helyi QR-library-val.  
> Mivel a PDF nem kér adattárolást, az adatbázis és a backend nem kötelező része a minimális megoldásnak.

## Gyakori vizsgahibák

- Túl nagy projektet kezdeni építeni.
- Felesleges backend vagy adatbázis bevezetése.
- Az időt design-extra funkciókra pazarolni.
- Nem a PDF-ben megadott minimumkövetelményre optimalizálni.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Használat: elsődleges feladatszöveg.

Megnyitva: `2026-04-09`
