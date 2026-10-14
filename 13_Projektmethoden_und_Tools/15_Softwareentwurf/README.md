# Softwareentwurf

## Gyors vizuális kép

| Kérdés | Szoftverterv válasza |
|---|---|
| miből áll a rendszer? | komponensek, modulok |
| hogyan kapcsolódnak? | interfészek, adatáramlás |
| hol tároljuk az adatokat? | adatmodell, adatbázis |
| hogyan lesz jól bővíthető? | architektúra és felelősségek szétválasztása |

## Mi az a szoftverterv?

A szoftvertervezés a követelmények és az implementáció közti lépés.

Itt dől el többek között:

- milyen architektúrát használunk
- milyen modulokra bontjuk a rendszert
- milyen interfészek lesznek
- hogyan kezeljük az adatokat
- hogyan támogatjuk a tesztelhetőséget és karbantarthatóságot

## Miért fontos?

- csökkenti a káoszt a fejlesztés során
- segíti a csapatmunkát
- javítja a bővíthetőséget
- könnyebbé teszi a hibakeresést és módosítást

## Tipikus tervezési elemek

- architektúra
- rétegek vagy komponensek
- adatmodell
- API-k és interfészek
- üzleti logika elhelyezése
- hibakezelés
- biztonsági és teljesítmény-szempontok

## Követelmény, terv, implementáció: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| követelmény | mit kell tudnia a rendszernek |
| szoftverterv | hogyan építjük fel |
| implementáció | a konkrét megvalósítás kódban |

## Egy kölcsönzés feladatainak szétválasztása

Az alkalmazás kölcsönzési gombja három jól elkülöníthető felelősséghez kapcsolódik. A felület összegyűjti az eszközazonosítót és megjeleníti a választ. Az alkalmazási logika megállapítja, hogy a bejelentkezett személy jogosult-e, és milyen üzleti szabály érvényes. Az adattárolási réteg megbízhatóan rögzíti az új kölcsönzést.

Az interfész szerződése megadja a sikeres választ és az értelmezhető eredményeket, például „az eszköz már foglalt”. A párhuzamos kérések kezelése és az adatbázis-korlát a terv része; csak a gomb letiltása nem biztosít szerveroldali védelmet.

Ezek lehetnek egyetlen alkalmazás moduljai. A felelősségek szétválasztása nem követeli meg mikroszolgáltatások bevezetését. A tervet az ismert igényhez igazítjuk, és a döntések indokát megőrizzük, hogy később érthetően lehessen módosítani.

## Vizsgán jól használható megfogalmazás

> A szoftverterv a követelmények technikai megvalósításának terve.  
> Meghatározza a rendszer felépítését, a komponenseket,
> az interfészeket, az adatkezelést
> és a fontos tervezési döntéseket.  
> Célja, hogy a fejlesztés átlátható, bővíthető és karbantartható legyen.

## Gyors önellenőrzés

1. Mi a szoftverterv lényege?
2. Miért van szükség rá a kódolás előtt?
3. Milyen elemeket szokott tartalmazni?
4. Mi a különbség a követelmény és a terv között?
5. Hogyan segíti a karbantarthatóságot?

## Rövid válaszok az önellenőrzéshez

1. A technikai megvalósítás előzetes megtervezése
2. Mert szerkezetet és irányt ad
3. Architektúra, modulok, interfészek, adatkezelés
4. A követelmény a mit, a terv a hogyan kérdésére válaszol
5. Jobb szétválasztással és átláthatósággal

## Források

- [Microsoft: Architecture styles](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/)  
  Komponensek felelőssége és a választott felépítés kompromisszumai.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Microsoft Learn - Architecture styles  
   https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/  
   Használat: modern, hivatalos forrás az architektúra, rétegek és tervezési trade-offok szerepéhez.

2. Atlassian Confluence - UML diagram template  
   https://www.atlassian.com/software/confluence/templates/uml-diagram  
   Használat: gyakorlati forrás a szoftvertervezés vizuális dokumentálásához és rendszerábráihoz.

Megnyitva: `2026-04-08`
