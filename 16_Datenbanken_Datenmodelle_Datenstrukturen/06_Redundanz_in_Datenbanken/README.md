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

Ha az ügyfél aktuális törzsadatcímét minden rendelési sorban újra tároljuk, az felesleges redundancia lehet. A rendeléskori szállítási cím viszont külön történeti tény, amelyet indokolt változatlanul megőrizni.

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

## Kidolgozott példa: háromféle anomália

Tegyük fel, hogy egy táblában tároljuk a `course_id`, `course_title`, `student_id` és `student_name` mezőket. Egy sor egy jelentkezést jelent.

- **Módosítás:** a kurzus címét húsz jelentkezési sorban kell átírni. Ha egy kimarad, két cím lesz ugyanahhoz a kurzushoz.
- **Beszúrás:** egy új kurzust még nem tudunk megfelelően rögzíteni, mert nincs hozzá jelentkező.
- **Törlés:** az utolsó jelentkezés törlésével a kurzus neve is eltűnik a nyilvántartásból.

A megoldás `courses`, `students` és `enrollments` táblák kialakítása. A cím a kurzusnál, a név a tanulónál marad, a jelentkezés pedig két idegen kulcsot tartalmaz. Az azonosító ismétlődése az `enrollments` táblában a kapcsolatot fejezi ki, nem ugyanaz a probléma, mint a név minden sorban történő másolása.

Ha egy gyors riport kedvéért előre tároljuk a jelentkezők számát, meg kell határozni az újraszámítást és frissítést is. Ez tudatos denormalizálás. A mentés vagy replikáció szintén több adatpéldányt hozhat létre, de más célból, nem a logikai séma rossz felosztása miatt.

## Vizsgán jól használható megfogalmazás

> A redundancia adatbázisban azt jelenti, hogy ugyanaz az információ feleslegesen több helyen is tárolódik.  
> Ez növeli a tárhelyigényt és adatinkonzisztenciához vezethet, például akkor, ha egy módosítást nem végzünk el minden  
> előfordulási helyen.  
> A relációs adatbázistervezés egyik célja a felesleges redundancia csökkentése, például normalizálással.

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

### A bővítés ellenőrzött forrásai

- [Microsoft: Database design basics](https://support.microsoft.com/en-us/access/database-design-basics): követelmények, táblák, kapcsolatok és normalizálás

Ellenőrizve: `2026-10-14`.
