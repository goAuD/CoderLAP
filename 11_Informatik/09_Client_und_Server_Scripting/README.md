# Client und Server Scripting

## Lényeg 30 másodpercben

A **client-side scripting** a felhasználó eszközén, főleg a böngészőben fut.

A **server-side scripting** a szerveren fut, és ott dolgozza fel a kéréseket.

Röviden:

- kliensoldal: felület, interakció, böngészőlogika
- szerveroldal: üzleti logika, adatbázis, hitelesítés, adatfeldolgozás

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

## Miért kell mindkettő?

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

## Vizsgán jól használható megfogalmazás

> A kliensoldali scripting a felhasználó böngészőjében fut, és főleg a felület interaktív működéséért felel.  
> A szerveroldali scripting a szerveren fut, és az üzleti logikát, az adatkezelést, a hitelesítést és a válasz előállítását végzi.  
> Egy modern webalkalmazás jellemzően mindkét megközelítést együtt használja.

## Gyakori vizsgahibák

- Azt állítani, hogy minden JavaScript csak kliensoldali lehet.
- A kliensoldali validálást elégséges biztonsági megoldásnak tekinteni.
- A dinamikus oldalt kizárólag szerveroldali fogalomnak nevezni.
- Nem megemlíteni az adatbázis- és jogosultságkezelést a szerveroldalon.

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
