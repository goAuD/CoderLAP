# Statische und dynamische Webseiten

## Gyors vizuális kép

| Típus | Jellemző | Példa |
|---|---|---|
| statikus | előre elkészült fájl | egyszerű bemutatkozó oldal |
| dinamikus | futásidőben generált vagy módosított tartalom | webshop, belépett felhasználói felület |

## Mi az a statikus weboldal?

Statikus oldalnál a szerver többnyire:

- kész HTML, CSS, JS fájlokat szolgál ki

A tartalom:

- nem feltétlenül változik felhasználónként
- gyakran gyors és egyszerű

Példák:

- cégbemutató oldal
- portfólió
- dokumentációs oldal

## Mi az a dinamikus weboldal?

Dinamikus oldalnál a tartalom:

- adatbázisból jöhet
- felhasználó szerint változhat
- kérés közben állhat elő

Példák:

- webshop terméklista
- bejelentkezett adminfelület
- fórum
- foglalási rendszer

## Hogyan lehet valami dinamikus?

Két gyakori út:

### 1. Szerveroldalon

A szerver:

- lekér adatokat
- logikát futtat
- személyre szabott HTML-t vagy adatot küld

### 2. Kliensoldalon

A böngésző:

- JavaScript segítségével módosítja a felületet
- API-ból adatot kér
- új tartalmat jelenít meg új oldalbetöltés nélkül

## Miért fontos a különbség?

Mert más lesz:

- a fejlesztési logika
- a teljesítmény
- a cache-elés
- a biztonsági megfontolás
- a karbantartás

## Fontos pontosítás

Sok mai weboldal vegyes.

Például:

- az alapoldal statikusnak tűnhet
- de a tartalom egy része dinamikusan töltődik be

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| statikus oldal | előre elkészült tartalom |
| dinamikus oldal | futásidőben generált vagy módosított tartalom |
| interaktív oldal | nem mindig ugyanaz, mint a dinamikus |

## Mikor készül el a HTML?

Ugyanaz a tananyagoldal többféleképpen is kiszolgálható:

| Megoldás | Folyamat egy oldal megnyitásakor |
|---|---|
| Előre generált statikus oldal, SSG | a build már elkészítette a HTML-t; a szerver a kész fájlt küldi |
| Szerveroldali renderelés, SSR | a szerver a kéréshez összegyűjti az adatokat és HTML-t állít elő |
| Kliensoldali renderelés, CSR | JavaScript a böngészőben állítja össze a felületet, szükség esetén API-adatokból |

Az SSG-ben egy szövegmódosítás rendszerint új buildet és közzétételt igényel.
SSR-nél az adatbázisban módosított tartalom a következő kiszolgáláskor megjelenhet;
a gyorsítótár ezt befolyásolhatja. CSR-nél a kezdeti HTML lehet kevés tartalom,
ezért a betöltési és hibaállapotot is meg kell tervezni.

Egy statikusan kiszolgált oldal JavaScripttel szűrheti a témákat és helyben
mentheti a haladást. Ettől még nincs szerveroldali felhasználói adatbázisa.
Fordítva: egy dinamikus alkalmazás CSS-e és képei többnyire statikus fájlok.
Érdemes tehát külön megnevezni a **kiszolgálás módját** és a **böngészőbeli
interakciót**, mert a „statikus” szó nem jelenti azt, hogy az oldal mozdulatlan.

## Vizsgán jól használható megfogalmazás

> A statikus weboldal előre elkészített fájlokból áll,
> ezért a szerver jellemzően minden látogatónak ugyanazt a tartalmat küldi.  
> A dinamikus weboldal ezzel szemben futás közben,
> adatok és logika alapján állíthat elő tartalmat,
> például felhasználóhoz vagy adatbázishoz igazítva.  
> A mai webalkalmazások gyakran a két megközelítést kombinálják.

## Gyors önellenőrzés

1. Mi a statikus oldal lényege?
2. Mi a dinamikus oldal lényege?
3. Mondj két példát statikus oldalra.
4. Mondj két példát dinamikus oldalra.
5. Lehet-e egy weboldal részben statikus, részben dinamikus?

## Rövid válaszok az önellenőrzéshez

1. Előre elkészített tartalmat szolgál ki
2. Futás közben változhat vagy generálódhat
3. Portfólió, céges bemutatkozó oldal
4. Webshop, fórum
5. Igen

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Client-server overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview): a kérés és válasz útja.
- [MDN: SSR](https://developer.mozilla.org/en-US/docs/Glossary/SSR): renderelési időpontok megkülönböztetése.


1. MDN - Server-side website programming first steps  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps  
   Használat: hivatalos forrás a statikus és dinamikus weboldalak különbségéhez.

2. MDN - Introduction to the server side  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction  
   Használat: részletesebb hivatalos magyarázat arra, hogyan áll elő a dinamikus tartalom.

3. MDN - HTML basics  
   https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics  
   Használat: a statikus alapoldal-felépítés és kliensoldali webes tartalom kiindulópontjához.

Megnyitva: `2026-04-08`
