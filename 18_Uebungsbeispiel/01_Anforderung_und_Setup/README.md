# Anforderung und Setup

## Gyors vizuális kép

| Kell | Nem kell |
|---|---|
| HTML | adatbázis |
| reszponzív CSS, itt `Bootstrap` | felhasználókezelés |
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

## A feladatlistától az első működő változatig

Először létrehozzuk a HTML-vázat és az üres JavaScript-fájlt, majd megnyitjuk az oldalt.
A böngésző fejlesztői eszközeiben ellenőrizzük, hogy minden fájl betöltődött-e.
Ezután külön készül az űrlap, a bemenetet ellenőrző függvény és a QR-megjelenítés.
Így egy hibánál tudjuk, melyik réteget kell megvizsgálni.

Az oldal fájlból is elindítható. Ha a környezet helyi webszervert igényel,
a repo gyökerében használható például:

```powershell
py -m http.server 8780 --bind 127.0.0.1 --directory 18_Uebungsbeispiel/06_Musterloesung_Minimal
```

Ekkor a cím `http://127.0.0.1:8780`. A `Ctrl+C` leállítja a szervert.
Ez statikus kiszolgálás, nem adatfeldolgozó backend.

A mintamegoldás QR-könyvtára helyi, a Bootstrap CSS jelenleg CDN-ről érkezik.
Ezért teljesen offline vizsgakörnyezethez a szükséges CSS-t is előre helyben kell
előkészíteni, és hálózat nélkül kipróbálni. A framework a PDF szerint lehetőség szerinti
segítség, a reszponzív működés viszont követelmény.

Forrás: a katalógus 11. oldala; [Python: http.server](https://docs.python.org/3/library/http.server.html),
[Bootstrap: letöltés](https://getbootstrap.com/docs/5.3/getting-started/download/).

## Vizsgán jól használható megfogalmazás

> Ennél a gyakorlati feladatnál a minimális cél egy működő, responsive HTML-űrlap létrehozása, amely ellenőrzi az  
> osztrák `SV-Nr` érvényességét, és ennek eredménye alapján `QR`-kódot generál.  
> A legegyszerűbb megoldás frontend-alapú `HTML`, `Bootstrap` és `JavaScript` használata, helyi QR-library-val.  
> Mivel a PDF nem kér adattárolást, az adatbázis és a backend nem kötelező része a minimális megoldásnak.

## Gyors önellenőrzés

1. Mely három mező szükséges?
2. Hogyan készülünk hálózat nélküli környezetre?
3. Miért érdemes külön elkészíteni a validáló függvényt?

## Rövid válaszok az önellenőrzéshez

1. Vorname, Nachname és SV-NR.
2. A függőségeket, köztük a CSS-t előkészítjük helyben, majd hálózat nélkül próbálunk.
3. A logika külön bemenetekkel, a felület elkészülte előtt is ellenőrizhető.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Használat: elsődleges feladatszöveg.

2. Python - http.server
   https://docs.python.org/3/library/http.server.html

3. Bootstrap - Download
   https://getbootstrap.com/docs/5.3/getting-started/download/

Használat: helyi statikus előnézet és a CSS előkészítése.

Megnyitva: `2026-10-14`
