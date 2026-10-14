# Programmspezifikation

## Gyors vizuális kép

| Specifikáció része | Mit ír le? |
|---|---|
| funkcionális elvárások | mit csináljon a program |
| bemenetek | milyen adatokat kap |
| kimenetek | mit ad vissza |
| szabályok / feltételek | milyen korlátok vannak |
| hibakezelés | mi történjen problémánál |

## Mi az a programspecifikáció?

A programspecifikáció egy olyan leírás, amely rögzíti:

- a program célját
- a feladatot
- a szükséges funkciókat
- a feldolgozási szabályokat
- az elvárt eredményeket

Ez lehet:

- rövidebb feladatleírás
- részletes követelményspecifikáció
- fejlesztési vagy termékspecifikáció része

## Miért fontos?

- csökkenti a félreértéseket
- segít a fejlesztőknek tudni, mit kell megvalósítani
- segít a tesztelőknek tudni, mit kell ellenőrizni
- később is visszakereshető referencia marad

## Mit tartalmazhat?

Tipikusan:

- program célja
- bemenetek és kimenetek
- fő folyamatok
- üzleti szabályok
- kivételek és hibák kezelése
- korlátok és nem funkcionális elvárások

## Specifikáció és megoldás: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| specifikáció | mit kell tudnia a programnak |
| terv / design | hogyan építjük fel |
| implementáció | hogyan írjuk meg konkrétan |

## Jó specifikáció jellemzői

- világos
- egyértelmű
- ellenőrizhető
- nem önellentmondó
- a célt és a szabályokat is leírja

## Ellenőrizhető szerződés egy foglaláshoz

A „rendszer gyors és biztonságos legyen” kívánságot konkrét feltételekre bontjuk.
Példa egy tanfolyami férőhely foglalására:

| Rész | Megállapodás |
|---|---|
| Előfeltétel | bejelentkezett felhasználó, létező tanfolyam |
| Bemenet | tanfolyamazonosító; a felhasználót a szerver azonosítja |
| Siker | egy foglalás keletkezik, a visszaigazolás ezt azonosítja |
| Betelt tanfolyam | érthető elutasítás, foglalás nem keletkezik |
| Ismételt kérés | ugyanarra a tanfolyamra nem keletkezik újabb foglalás |
| Teljesítmény | előre megadott tesztgépen, adatmennyiségen és terhelésen mérjük |

Az utófeltétel írja le, mi legyen igaz a sikeres művelet végén. A követelményhez
azonosítót rendelhetünk, például `FOG-01`, és a teszteset erre hivatkozhat. Így
változáskor kiderül, mely teszteket kell újragondolni. A homályos időelvárást a
megrendelővel pontosítjuk, például a kérések 95%-a egy megadott terhelés mellett
egy másodpercen belül válaszoljon. Ez a példában választott cél, nem általános előírás.

## Vizsgán jól használható megfogalmazás

> A programspecifikáció olyan leírás, amely rögzíti, hogy a programnak milyen feladatot kell ellátnia, milyen  
> bemenetekkel dolgozik, milyen kimenetet ad, és milyen szabályok szerint működik.  
> A specifikáció célja a követelmények egyértelmű rögzítése, hogy a fejlesztés és a tesztelés ugyanarra az elvárt  
> működésre épülhessen.  
> A specifikáció tehát nem a kódot, hanem az elvárt viselkedést írja le.

## Gyors önellenőrzés

1. Mi a programspecifikáció lényege?
2. Miért fontos a fejlesztés előtt?
3. Mit ír le a specifikáció?
4. Mi a különbség specifikáció és implementáció között?
5. Miért fontos a teszteléshez is?

## Rövid válaszok az önellenőrzéshez

1. Az elvárt működés leírása
2. Mert tisztázza a követelményeket
3. Cél, bemenet, kimenet, szabályok, hibakezelés
4. Az egyik elvárást, a másik megvalósítást ír le
5. Mert ez alapján ellenőrizhető a helyes működés

## Források

Ellenőrizve: `2026-10-14`.

- [Atlassian: Product specifications](https://www.atlassian.com/agile/product-management/product-specification): mérhető cél és hatókör; saját foglalási példa.


1. IEEE SA - IEEE/ISO/IEC P29148  
   https://standards.ieee.org/ieee/29148/12262  
   Használat: hivatalos szabványoldal a követelménymérnökség és a jó követelmények alapfogalmaihoz.

2. Atlassian - What are Product Specifications?  
   https://www.atlassian.com/agile/product-management/product-specification  
   Használat: modern, gyakorlati forrás a specifikáció üzleti és fejlesztési szerepéhez.

Megnyitva: `2026-04-09`
