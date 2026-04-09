# Index: Vor- und Nachteile

## Lényeg 30 másodpercben

Az **index** olyan segédstruktúra, amely felgyorsíthatja az adatok keresését, de helyet foglal és lassíthat bizonyos írási műveleteket.

Röviden:

- gyorsabb lekérdezések
- több tárhely
- lassabb `INSERT`, `UPDATE`, `DELETE` bizonyos esetekben

## Gyors vizuális kép

| Előny | Hátrány |
|---|---|
| gyorsabb keresés | extra tárhelyigény |
| jobb szűrés és rendezés | karbantartási költség |
| hatékonyabb joinok | módosítások lassulhatnak |

## Mi az index?

Az index egy olyan adatstruktúra, amely segít gyorsabban megtalálni bizonyos rekordokat anélkül, hogy a teljes táblát végig kellene olvasni.

Hasonlat:

- mint egy könyv név- vagy tárgymutatója

## Miért jó?

Különösen hasznos:

- gyakran szűrt oszlopoknál
- kulcsmezőknél
- rendezésnél
- join műveleteknél

## Fő előnyök

- gyorsabb `SELECT` műveletek
- gyorsabb keresés feltétellel
- hatékonyabb relációs kapcsolódás
- jobb teljesítmény nagy tábláknál

## Fő hátrányok

- tárhelyet igényel
- minden írási műveletnél karban kell tartani
- túl sok index ronthatja az összteljesítményt
- rosszul megválasztott index nem hoz valódi hasznot

## Mikor érdemes indexet használni?

- ha sok a lekérdezés
- ha nagy az adatmennyiség
- ha adott oszlopon gyakran keresünk

## Mikor nem biztos, hogy jó?

- nagyon kicsi táblánál
- ritkán használt oszlopoknál
- ha túl sok módosítás történik és kevés a keresés

## Index és kulcs: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| kulcs | logikai adatmodellbeli szerep |
| index | teljesítményt javító technikai struktúra |

Gyakran kapcsolódnak egymáshoz, de nem ugyanazok.

## Vizsgán jól használható megfogalmazás

> Az index olyan adatbázis-struktúra, amely gyorsítja az adatok keresését és bizonyos lekérdezéseket.  
> Előnye a jobb lekérdezési teljesítmény, hátránya pedig a többlet tárhelyigény és az, hogy a módosító műveleteknél karban kell tartani.  
> Ezért az indexek használata teljesítménynyereséget adhat, de csak megfelelő tervezéssel érdemes alkalmazni.

## Gyakori vizsgahibák

- Azt állítani, hogy az index minden esetben javít.
- Az indexet elsődleges kulccsal azonosítani.
- Nem megemlíteni az írási műveletek lassulását.
- Elfelejteni a tárhelyigényt.

## Gyors önellenőrzés

1. Mi az index célja?
2. Mi az egyik fő előnye?
3. Mi az egyik fő hátránya?
4. Mikor hasznos különösen?
5. Mi a különbség kulcs és index között?

## Rövid válaszok az önellenőrzéshez

1. Gyorsabb keresés és lekérdezés
2. Jobb `SELECT` teljesítmény
3. Több tárhely és lassabb módosítások
4. Nagy táblán és gyakori szűrésnél
5. A kulcs logikai, az index technikai fogalom

## Források

1. PostgreSQL - Indexes  
   https://www.postgresql.org/docs/current/indexes.html  
   Használat: hivatalos forrás az indexek szerepéhez és működéséhez.

2. PostgreSQL - Indexes Introduction  
   https://www.postgresql.org/docs/current/indexes-intro.html  
   Használat: tömör, hivatalos bevezető az indexek előnyeihez és költségeihez.

Megnyitva: `2026-04-09`
