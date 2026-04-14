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

## Vizsgán jól használható megfogalmazás

> A szoftverterv a követelmények technikai megvalósításának terve.  
> Meghatározza a rendszer felépítését, a komponenseket,
> az interfészeket, az adatkezelést
> és a fontos tervezési döntéseket.  
> Célja, hogy a fejlesztés átlátható, bővíthető és karbantartható legyen.

## Gyakori vizsgahibák

- A szoftvertervet összekeverni a követelményspecifikációval.
- Azt hinni, hogy ez már maga a kódolás.
- Kihagyni az architektúra és interfészek szerepét.
- Csak a felületre gondolni, és nem az egész rendszerre.

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

1. Microsoft Learn - Architecture styles  
   https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/  
   Használat: modern, hivatalos forrás az architektúra, rétegek és tervezési trade-offok szerepéhez.

2. Atlassian Confluence - UML diagram template  
   https://www.atlassian.com/software/confluence/templates/uml-diagram  
   Használat: gyakorlati forrás a szoftvertervezés vizuális dokumentálásához és rendszerábráihoz.

Megnyitva: `2026-04-08`
