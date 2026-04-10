# Reproduzierbare und nicht reproduzierbare Fehler

## Gyors vizuális kép

| Hibatípus | Jellemző |
|---|---|
| reprodukálható | ugyanazokkal a lépésekkel újra előidézhető |
| nem reprodukálható / intermittáló | időszakos, bizonytalan, “flaky” jellegű |

## Mi az a reprodukálható hiba?

Ha ugyanazokkal a feltételekkel:

- ugyanaz a bemenet
- ugyanaz a környezet
- ugyanaz a lépéssor

ismét ugyanaz a hiba jelentkezik, akkor a hiba reprodukálható.

## Mi az a nem reprodukálható hiba?

Ilyenkor:

- a hiba nem jelenik meg mindig
- környezeti tényezők befolyásolhatják
- időzítés, állapot, hálózat, párhuzamosság is szerepet játszhat

Ezt a gyakorlatban gyakran:

- intermittáló hibának
- vagy teszteknél `flaky` problémának is nevezik

## Miért fontos ez a különbség?

- a reprodukálható hibát könnyebb elemezni és javítani
- a nem reprodukálható hibához több adatgyűjtés kell
- a hibajegy minősége nagyban befolyásolja a javíthatóságot

## Mi segíthet a nem reprodukálható hibáknál?

- pontos logok
- környezet rögzítése
- tesztadatok rögzítése
- időbélyegek és lépések dokumentálása
- állapotmegosztás csökkentése

## Hiba és teszt instabilitás: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| valódi szoftverhiba | a rendszer hibás működése |
| instabil teszt | maga a teszt környezete vagy felépítése bizonytalan |

## Vizsgán jól használható megfogalmazás

> A reprodukálható hiba olyan hiba, amely ugyanazokkal a bemenetekkel és lépésekkel megbízhatóan újra előidézhető.  
> A nem reprodukálható vagy intermittáló hiba ezzel szemben nem jelentkezik minden alkalommal, ezért nehezebb elemezni és javítani.  
> Az ilyen hibáknál különösen fontos a részletes hibadokumentáció, a logok és a környezeti feltételek rögzítése.

## Gyakori vizsgahibák

- Azt gondolni, hogy a nem reprodukálható hiba “nem is valódi hiba”.
- Nem megemlíteni a környezeti tényezőket.
- A flaky tesztet automatikusan alkalmazáshibának tekinteni.
- Kihagyni a részletes dokumentálás szerepét.

## Gyors önellenőrzés

1. Mi a reprodukálható hiba?
2. Mi a nem reprodukálható hiba?
3. Miért nehezebb javítani az utóbbit?
4. Milyen okok állhatnak mögötte?
5. Mi segíthet a feltárásában?

## Rövid válaszok az önellenőrzéshez

1. Stabilan újra előidézhető hiba
2. Olyan hiba, ami nem jelentkezik kiszámíthatóan
3. Mert nehezebb biztosan megfigyelni
4. Időzítés, állapot, hálózat, párhuzamosság
5. Logok, pontos lépések, környezet rögzítése

## Források

1. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Használat: hivatalos fogalmi háttér a hiba, failure, incident és kapcsolódó tesztelési terminológia pontosításához.

2. Selenium - Avoid sharing state  
   https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/  
   Használat: hivatalos, modern forrás arra, hogyan okozhat a megosztott állapot intermittáló vagy flaky tesztviselkedést.

Megnyitva: `2026-04-09`
