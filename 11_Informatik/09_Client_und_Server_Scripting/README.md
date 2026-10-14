# Client und Server Scripting

## Gyors vizuális kép

| Típus | Hol fut? | Mire jó? |
|---|---|---|
| client-side scripting | böngészőben | űrlapellenőrzés, interakció, DOM-kezelés |
| server-side scripting | szerveren | adatok feldolgozása, adatbázis-kezelés, jogosultság |

## Mi az a kliensoldali scripting?

Ez a kód a felhasználó böngészőjében fut le.

Tipikusan:

- `JavaScript`
- DOM-manipuláció
- gombkattintások kezelése
- űrlapellenőrzés
- dinamikus felületek

Előnye:

- gyors visszajelzés a felhasználónak
- interaktív élmény
- kevesebb újratöltés

Korlátja:

- a felhasználó környezetében fut
- nem tekinthető teljesen megbízhatónak
- érzékeny adatok és végső ellenőrzések nem maradhatnak csak itt

## Mi az a szerveroldali scripting?

Ez a kód a webszerveren fut le.

Tipikus feladatok:

- üzleti logika
- adatbázis-lekérdezés
- bejelentkezés és jogosultságkezelés
- rendelésfeldolgozás
- API-válasz előállítása

Tipikus technológiák:

- `PHP`
- `Node.js`
- `Python`
- `Java`
- `.NET`

## Egy egyszerű kérés útja

1. A böngésző elküld egy HTTP-kérést.
2. A szerveroldali kód feldolgozza.
3. Szükség esetén adatbázist használ.
4. A szerver HTML-t, JSON-t vagy más választ küld.
5. A kliensoldali kód ezt megjeleníti vagy tovább kezeli.

## Hogyan osztjuk meg a feladatokat?

Mert más a szerepük.

### Kliensoldal

- felhasználói élmény
- vizuális dinamika
- azonnali reakció

### Szerveroldal

- központi adatkezelés
- biztonság
- üzleti szabályok végrehajtása
- több felhasználó egyidejű kiszolgálása

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| client-side | a böngészőben fut |
| server-side | a szerveren fut |
| dinamikus oldal | lehet kliens- vagy szerveroldalon is dinamikus |
| validálás | kliensen kényelmi, szerveren kötelező végső ellenőrzés |

## Mire kell figyelni?

- A kliensoldali ellenőrzés önmagában nem biztonság.
- A szerveroldalon mindig újra kell ellenőrizni a bemenetet.
- A jó webalkalmazás általában mindkét oldalt használja.
- A felhasználói élmény és a biztonság egyensúlya fontos.

## A bizalmi határ egy rendelésnél

A kliens és a szerver közötti határ egyben bizalmi határ. A felhasználó a saját
böngészőjében módosíthatja a JavaScriptet és a küldött kérést. Egy rendelésnél
ezért más feladatot kap a két oldal:

| Kliens küldi vagy végzi | Szerver ellenőrzi vagy számítja |
|---|---|
| termékazonosító és darabszám | létező termék, megengedett mennyiség és készlet |
| a kiválasztott szállítási mód | az adott rendeléshez engedett mód és díj |
| gyors mezőellenőrzés és visszajelzés | az összes beérkező adat és az üzleti szabály |
| munkamenethez tartozó kérés | a hitelesített felhasználó kiléte és jogosultsága |

A szerver a saját adataiból számolja a végösszeget, és nem a kérésben kapott
„admin” vagy „price” érték alapján dönt. A válasz lehet HTML vagy JSON;
JSON esetén a böngészőnek még meg kell jelenítenie az adatot.

A JavaScript nyelv önmagában nem dönti el a végrehajtás helyét: DOM-kódot a
böngészőben, Node.js-kódot szerveren vagy helyi eszközként is futtathatunk.
Egy hagyományos HTML-űrlap kliensoldali JavaScript nélkül is küldhet adatot
a szervernek. A kliensoldali kód mennyiségét a szükséges felhasználói élmény
alapján választjuk meg.

## Vizsgán jól használható megfogalmazás

> A kliensoldali scripting a felhasználó böngészőjében fut, és főleg a felület interaktív működéséért felel.  
> A szerveroldali scripting a szerveren fut,
> és az üzleti logikát, az adatkezelést,
> a hitelesítést és a válasz előállítását végzi.  
> Egy modern webalkalmazás jellemzően mindkét megközelítést együtt használja.

## Gyors önellenőrzés

1. Hol fut a kliensoldali scripting?
2. Hol fut a szerveroldali scripting?
3. Miért kell a bemenetet szerveroldalon is ellenőrizni?
4. Mondj két kliensoldali és két szerveroldali feladatot.
5. Lehet-e egy oldal mindkét oldalon dinamikus?

## Rövid válaszok az önellenőrzéshez

1. A böngészőben
2. A szerveren
3. Mert a kliens nem teljesen megbízható
4. Kliens: DOM, űrlapellenőrzés. Szerver: adatbázis, hitelesítés
5. Igen

## Források

Ellenőrizve: `2026-10-14`.

- [OWASP: Business Logic Security](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html): szerveroldali bizalmi határ.
- [MDN: Server-side introduction](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction): szerver és kliens feladatmegosztása.


1. MDN - Introduction to the server side  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction  
   Használat: a szerveroldali feldolgozás szerepe és helye a webes kérés-válasz modellben.

2. MDN - Client-side web APIs  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction  
   Használat: kliensoldali működés, böngészőoldali programozási környezet és interakció.

3. Node.js - Introduction to Node.js  
   https://nodejs.org/en/learn/getting-started/introduction-to-nodejs  
   Használat: szerveroldali JavaScript hivatalos példája és működési modellje.

Megnyitva: `2026-04-08`
