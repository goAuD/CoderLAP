# Redundanz in Datenbanken

## Gyors vizuális kép

| Helyzet | Következmény |
|---|---|
| ugyanaz az adat több táblában / sorban ismétlődik | nő a hibalehetőség |
| egy adat változik, de nem mindenhol | ellentmondás keletkezik |
| jól normalizált modell | kevesebb felesleges ismétlés |

## Mi az a redundancia?

Redundanciáról beszélünk, ha egy adat:

- ugyanazzal a jelentéssel
- több helyen
- szükségtelenül ismétlődik

Példa:

ha egy ügyfél címe minden rendelési sorban teljes egészében újra meg újra szerepel, az tipikus redundancia.

## Miért probléma?

- több tárhelyet használ
- nehezebb karbantartani
- könnyen ellentmondó adat keletkezik
- frissítési, beszúrási és törlési anomáliákhoz vezethet

## Tipikus anomáliák

### Frissítési anomália

Ugyanazt az adatot sok helyen kell átírni.

### Beszúrási anomália

Nem tudsz valamit tárolni anélkül, hogy más fölösleges adatokkal együtt ne kelljen rögzíteni.

### Törlési anomália

Egy rekord törlésével akaratlanul más fontos információ is elveszik.

## Mindig rossz a redundancia?

Nem feltétlenül.

Néha tudatosan vállalják:

- teljesítmény miatt
- riportolás vagy adattárház esetén
- gyorsabb olvasás érdekében

Vizsgán jó válasz, ha kimondod:

- a fölösleges redundancia kerülendő
- de bizonyos helyzetekben a kontrollált redundancia indokolt lehet

## Redundancia és ismétlődő adatok: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| értelmes ismétlődés | például több rendelés ugyanattól az ügyféltől |
| redundancia | ugyanazon információ fölösleges újratárolása |

## Vizsgán jól használható megfogalmazás

> A redundancia adatbázisban azt jelenti, hogy ugyanaz az információ feleslegesen több helyen is tárolódik.  
> Ez növeli a tárhelyigényt és adatinkonzisztenciához vezethet, például akkor, ha egy módosítást nem végzünk el minden előfordulási helyen.  
> A relációs adatbázistervezés egyik célja a felesleges redundancia csökkentése, például normalizálással.

## Gyakori vizsgahibák

- A redundanciát önmagában mindig hibának nevezni.
- Nem megemlíteni az inkonzisztencia veszélyét.
- Összekeverni a természetes többszörös előfordulással.
- Kihagyni a normalizálás kapcsolatát.

## Gyors önellenőrzés

1. Mi az adatredundancia?
2. Miért veszélyes?
3. Mi az a frissítési anomália?
4. Hogyan csökkenthető a redundancia?
5. Lehet-e néha indokolt a redundancia?

## Rövid válaszok az önellenőrzéshez

1. Ugyanazon információ fölösleges ismétlődése
2. Mert hibához és ellentmondáshoz vezethet
3. Amikor több helyen kell ugyanazt az adatot módosítani
4. Jó tervezéssel és normalizálással
5. Igen, például teljesítmény miatt

## Források

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Használat: hivatalos, jól használható forrás a redundancia és relációs tervezés kapcsolatának megértéséhez.

2. Microsoft Learn - Description of the database normalization basics  
   https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/access/database-normalization-description  
   Használat: hivatalos háttér a redundancia csökkentéséhez és a normalizálás céljához.

Megnyitva: `2026-04-09`
