# Reproduzierbare und nicht reproduzierbare Fehler

## Gyors vizuális kép

| Hibatípus | Jellemző |
|---|---|
| reprodukálható | ugyanazokkal a lépésekkel újra előidézhető |
| egyelőre nem reprodukálható | a megismétlés feltételei még ismeretlenek |
| intermittáló | csak bizonyos futásokban jelentkezik |

## Mi az a reprodukálható hiba?

Ha ugyanazokkal a feltételekkel:

- ugyanaz a bemenet
- ugyanaz a környezet
- ugyanaz a lépéssor

ismét ugyanaz a hiba jelentkezik, akkor a hiba reprodukálható.

## Mi az a nem reprodukálható hiba?

Ilyenkor az észlelt eltérést a jelenleg ismert lépésekkel nem sikerül megbízhatóan
újra előidézni. Még hiányozhat egy környezeti feltétel, állapot vagy időzítési adat.
Ha az eltérés időnként újra előfordul, intermittáló jelenségről beszélünk.
Teszteknél a változó sikeres/sikertelen eredményt gyakran `flaky` viselkedésnek nevezik.

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
| instabil teszteredmény | oka lehet az alkalmazás, a teszt vagy a környezet időzítése/állapota |

## Megismételhető körülmények kialakítása

A „néha kétszer ment” jelzésből konkrét vizsgálatot készítünk: ugyanazt a
mentési műveletet két gyors kérés indítja. Rögzítjük a verziót, a kérések sorrendjét, az érintett személytelenített tesztadatot és a két válasz
eredményét. Külön vizsgáljuk a felület dupla kattintását és a szerver párhuzamos
kéréseit, mert ezek más rétegben jelentkeznek.

Az „egyelőre nem reprodukálható” a vizsgálat állapota: még nincs megbízható
lépéssorunk. Az **intermittáló** azt írja le, hogy a jelenség időszakosan lép fel.
Egy intermittáló hibát is reprodukálhatóvá tehetünk az időzítés kontrollálásával.

Tesztben a véletlen generátor rögzített kezdőértéke, a befecskendezett óra,
elkülönített tesztadatok és megfigyelhető kész állapotra várás segítenek. Egy
hosszabb, vak várakozás csak elfedhet időzítési problémát. Az ismételt futtatás
eredményét megőrizzük; egy későbbi siker nem törli a korábbi eltérés bizonyítékát.
Naplóba a szükséges diagnosztikai adat kerüljön, jelszó és munkamenettoken nélkül.

## Vizsgán jól használható megfogalmazás

> A reprodukálható hiba olyan hiba, amely ugyanazokkal a bemenetekkel és lépésekkel megbízhatóan újra előidézhető.  
> Egyelőre nem reprodukálható hiba esetén a megismétlés feltételei még nem ismertek. Az intermittáló hiba csak időnként  
> jelentkezik; megfelelő feltételekkel ez is reprodukálhatóvá válhat.  
> Az ilyen hibáknál különösen fontos a részletes hibadokumentáció, a logok és a környezeti feltételek rögzítése.

## Gyors önellenőrzés

1. Mi a reprodukálható hiba?
2. Mi a nem reprodukálható hiba?
3. Miért nehezebb javítani az utóbbit?
4. Milyen okok állhatnak mögötte?
5. Mi segíthet a feltárásában?

## Rövid válaszok az önellenőrzéshez

1. Stabilan újra előidézhető hiba
2. Olyan észlelt hiba, amelyet a jelenleg ismert lépésekkel nem tudunk megbízhatóan megismételni
3. Mert nehezebb biztosan megfigyelni
4. Időzítés, állapot, hálózat, párhuzamosság
5. Logok, pontos lépések, környezet rögzítése

## Források

Ellenőrizve: `2026-10-14`.

- [Selenium: Avoid sharing state](https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/): elkülönített tesztadatok és futtatás.


1. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Használat: hivatalos fogalmi háttér a hiba, failure, incident és kapcsolódó tesztelési terminológia pontosításához.

2. Selenium - Avoid sharing state  
   https://www.selenium.dev/documentation/test_practices/encouraged/avoid_sharing_state/  
   Használat: hivatalos, modern forrás arra, hogyan okozhat a megosztott állapot intermittáló vagy flaky tesztviselkedést.

Megnyitva: `2026-04-09`
