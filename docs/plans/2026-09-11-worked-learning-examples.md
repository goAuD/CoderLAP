# Kidolgozott példák: programozás és informatika

## Cél és szerkesztési elv

A 15. Programozási alapismeretek és a 11. Informatika kiemelt fejezet.
A magyarázat mellé ott kerül kód, ahol a végrehajtás megértését segíti.
Más témákban adatpélda, kérés–válasz, konfiguráció vagy egy konkrét helyzet
végigvezetése ad többet. A cél a LAP-szinten érthető szakmai mélység.

A helyes működést tanítjuk: feladat → bemenet és feltételek → kód → kimenet →
magyarázat → önellenőrzés. Az önálló hibalistát az átdolgozott témákból elhagyjuk;
az értékes feltételeket és korlátokat a magyarázatba építjük. A többi fejezet
meglévő hibalistáit későbbi, tartalmi ellenőrzéssel járó körökben vezetjük ki.
Ez szerkesztési döntés; nem állítunk bizonyított idegrendszeri hatást.

Általános példanyelv: a felhasználó választása alapján **JavaScript**.
A webes és technológiai témák saját nyelvüket használják. A példák futtatásához
szükséges környezetet megnevezzük; töredékes és szemléltető kódot külön jelölünk.
Új böngészős kódfuttató vagy futásidejű függőség nem része ennek a munkának.

## Kiinduló felmérés

Alap: `4c0436bcce15e0cde9db355a1ee7ec9fae8645ae`, ellenőrzés: `2026-09-11`.
Mindkét nyelvi változatban:

- 15. fejezet: 20 téma, 0 nyelvvel jelölt kódblokkot tartalmazó téma.
  Egyes témákban `text` jelölésű folyamatvázlat vagy pszeudokód van.
- 11. fejezet: 43 téma, 6 témában HTML-, CSS- vagy JSON-blokk
  (05, 06, 08, 15, 17, 21).

Ez szerkezeti felmérés, nem mind a 63 téma teljes szakmai lektorálása.
Az alábbi lista a bővítés munkasorrendjét és témánkénti célját rögzíti.
A változatlan példáknál is ellenőrizendő a magyarázat, a megjelenés és a pontosság.

## Első mintacsomag

Átdolgozva, magyar és német nyelven:

- **LAP-15-05:** Bubble Sort és Quick Sort, futtatható függvények, köztes
  állapotok, ismétlődő értékek, üres bemenet és a választott változat korlátai.
- **LAP-15-06:** lineáris és bináris keresés, indexek, találat nélküli eredmény,
  rendezett bemenet, tartományfelezés és a teljes munkaigény.
- **LAP-15-17:** `for`, `while`, `do...while`, `for...of`, kimenetek és
  végrehajtási sorrend, feltételvizsgálat, léptetés.

Mindhárom témában megszűnt az önálló hibalista. A többi alábbi tétel még terv.
A könyvtárak, azonosítók és a nyelvi útvonalak változatlanok.

## 15. fejezet – fennmaradó bővítések

| Téma | Konkrét példa vagy mélyítés |
|---|---|
| 01 – Fejlesztési szakaszok | Egy kis funkció útja az igénytől az átadásig, ellenőrizhető elfogadási feltétellel |
| 02 – Procedurális és OOP | Ugyanaz az egyszerű feladat függvénnyel, majd objektummal; állapot és művelet kapcsolata |
| 03 – Algoritmus | Bemenet, lépések, kimenet egy összegző feladaton |
| 04 – Pszeudokód | Egy feladat pszeudokódja és megfelelő JavaScript-megvalósítása |
| 07 – Programfejlesztés menete | Követelmény, kis függvény és ellenőrző esetek összekapcsolása |
| 08 – Programozási nyelv felépítése | Egy rövid függvény elemei: literál, változó, kifejezés, utasítás, paraméter, visszatérés |
| 09 – Interpreter és compiler | A forráskód és futtatókörnyezet útja, végrehajtási modell feltüntetésével |
| 10 – Debugger | Működő rövid program léptetése, változóértékek és hívási verem követése |
| 11 – Assembler | Néhány utasítás és regiszterváltozás; architektúra és szintaxis megnevezése |
| 12 – Rekurzió | Kis bemenet teljes hívási és visszatérési sora, alapeset és csökkenő feladat |
| 13 – ASCII | Karakter és kód közti átalakítás, ASCII és Unicode tartományainak magyarázata |
| 14 – Adattípusok | Konkrét értékek, műveletek és típusok; JavaScript sajátosságainak elkülönítése |
| 15 – Változó és konstans | `let`, `const`, értékadás; kötés és objektum tartalma |
| 16 – Hatókör | Blokk- és függvényhatókör működő példával, élettartam külön magyarázva |
| 18 – Fej- és lábvezérelt ciklus | Gyakorlati feladat a vizsgálat időpontjára, kapcsolódás a 17. témához |
| 19 – Elágazások | `if/else` és `switch`, bemenetenként követhető ág és kimenet |
| 20 – OOP | Kis osztály, két példány, konstruktor és metódus; fogalmak azonosítása a kódban |

## 11. fejezet – bővítési térkép

A fejezet két részben dolgozandó át: 01–21, majd 22–43.

| Téma | Konkrét példa vagy mélyítés |
|---|---|
| 01 – Informatika fogalma | Információfeldolgozási helyzet bemenettel, feldolgozással és kimenettel |
| 02 – Statikus/dinamikus web | Statikus HTML és helyi DOM-változtatás; szerveroldali feldolgozás külön |
| 03 – Weblog/webshop/platform | Ugyanazon felhasználói igény három megvalósítási helyzete |
| 04 – HTML/XML | Rövid, érvényes dokumentumpár, szerkezet és felhasználás |
| 05 – HTML5-alapváz | Meglévő kód ellenőrzése, szemantikus elemek és megjelenés magyarázata |
| 06 – Metaelemek | Meglévő példa mellett a charset, viewport, title és leírás szerepe |
| 07 – SEO | Cím, leírás és értelmes hivatkozás egy konkrét oldalon |
| 08 – CSS | Meglévő szabályokhoz minimális HTML és látható eredmény |
| 09 – Kliens-/szerveroldal | Helyi kliensesemény és elkülönített szerveroldali feldolgozás |
| 10 – Webes eszközök | DOM-, stílus- és hálózati ellenőrzés egy kis oldalon |
| 11 – CMS | Tartalom → sablon → megjelenés, egy konkrét tartalomelemmel |
| 12 – LIFO/FIFO | Ugyanaz a három elem, eltérő kivételi sorrend és kimenet |
| 13 – Stack/queue | Műveletek és állapotváltozások; a tömbös megoldás költségei |
| 14 – UI | Címkézett beviteli mező és visszajelzés rövid HTML-példával |
| 15 – Karakterkódolás | Karakter, kódpont és UTF-8 bájtok; meglévő charset példa |
| 16 – Szabványok | Egy konkrét formátum követése két rendszer közti adatcserében |
| 17 – Frame | Meglévő iframe ellenőrzése, modern és történeti használat elkülönítése |
| 18 – Webservice | Konkrét HTTP-kérés és válasz, mindkét oldal szerepe |
| 19 – SOAP/WSDL | Kis XML-üzenet és a szolgáltatási leírás kapcsolata |
| 20 – REST API | Erőforrás, metódus, státuszkód, JSON-válasz; helyi mintaadat |
| 21 – JSON | Meglévő adatpélda mellett `JSON.parse`, hozzáférés és `JSON.stringify` |
| 22 – Agilis fejlesztés | Kis történet, elfogadási feltétel és visszajelzési kör |
| 23 – Reaktív programozás | Esemény és változó állapot követése; fogalmi határok tisztázása |
| 24 – Framework | Egy konkrét feladat és a keretrendszer által biztosított részek |
| 25 – AngularJS | Történeti példa pontos verzióval és támogatási státusszal; modern Angular külön |
| 26 – Bootstrap | Kis elrendezés és osztályok szerepe, verzió megjelölve |
| 27 – jQuery | Egy DOM-művelet és eseménykezelő, függőség feltüntetve |
| 28 – PHP/MySQL | Paraméterezett PDO-lekérdezés, bemenet és eredmény; titkok nélkül |
| 29 – Multitasking | Folyamat, szál, párhuzamosság és aszinkron végrehajtás egy konkrét helyzetben |
| 30 – Mobil web | Viewport és rugalmas szélesség kis HTML/CSS-példában |
| 31 – Responsive | Egy- és többoszlopos elrendezés media queryvel |
| 32 – Mobile first | Mobil alapstílus és nagyobb képernyőre bővítő szabály |
| 33 – Programozási nyelvek | Feladathoz illő nyelvválasztás; kevés, célzott összehasonlítás |
| 34 – Mobil/internet nyelvek | Egy alkalmazás rétegei és a hozzájuk választott technológia |
| 35 – Java web | Kis kéréskezelő, szükséges környezet és verzió feltüntetve |
| 36 – .NET web | Kis C# végpont és válasz, szükséges környezet feltüntetve |
| 37 – Metaadatok | Adat és leíró mezők egy konkrét fájl-/JSON-példában |
| 38 – KISS/DRY | Egy érthető függvény két valódi hívási hellyel, absztrakció célja |
| 39 – Coding standards | Rövid, következetes kód; elnevezések és formázás indoklása |
| 40 – Cross-platform | Ugyanazon funkció több célplatformon, közös és platformfüggő részek |
| 41 – CI | Kis ellenőrző pipeline és tesztlépés, jogosultságokkal |
| 42 – Delivery/deployment | Ugyanazon sikeres build két kiadási útja, jóváhagyási ponttal |
| 43 – CI/CD előírások | Meglévő pipeline konkrét szabályai: teszt, jogosultság, titokkezelés, visszaállítás |

## Ellenőrzés és átadás

- A futtatható kód a Markdownból közvetlenül ellenőrizhető:
  `node --test tests/learning-examples.test.cjs`.
- A teszt ellenőrzi a közölt kimeneteket, a két nyelv kódegyezését, valamint
  a rendezés és keresés határeseteit. A Node.js `vm` itt a saját, ellenőrzött
  példákat futtatja; nem szolgál idegen kód biztonsági elkülönítésére.
- A GitHub CI ugyanezt a tesztet és a meglévő JavaScript-interakciós teszteket is
  futtatja az Ubuntu runner Node.js környezetében. Új npm-csomag nem szükséges.
- Futtassuk a Python-teszteket, a tartalmi ellenőrzőt és a kétnyelvű buildet is.
- A Markdownban közölt kód a weboldalon szövegként jelenjen meg. Ellenőrizzük
  a mobil olvashatóságot és a vízszintes görgetést a hosszabb soroknál.
- Témakörönként külön commit/PR; a példák szakmai ellenőrzését friss elsődleges
  forrásokkal végezzük. A kiadás a szokásos, külön jóváhagyott folyamatot követi.

Első mintacsomag helyi eredménye: 80 Python-teszt, 27 tananyagpélda-teszt és
8 JavaScript-interakciós teszt sikeres; a 15. fejezet 20 magyar dokumentuma
átment a szerkezeti ellenőrzőn. A kétnyelvű build sikeres, a hat generált
témalapon a kód szövegként megmarad, és az önálló hibalista nincs jelen.
A böngészős és fizikai mobilos vizuális ellenőrzés még hátravan.
