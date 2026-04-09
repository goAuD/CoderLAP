# Wichtige Datentypen und Datenstrukturen

## Lényeg 30 másodpercben

Az adattípus megmondja, milyen jellegű adatot kezelünk, az adatszerkezet pedig azt, hogyan rendezzük és tároljuk ezeket az adatokat.

Röviden:

- adattípus: az adat fajtája
- adatszerkezet: az adatok szervezett formája
- mindkettő fontos a jó programtervezéshez

## Gyors vizuális kép

| Fogalom | Példa |
|---|---|
| adattípus | `int`, `string`, `boolean`, `float` |
| adatszerkezet | tömb, lista, verem, sor, szótár, objektum |

## Mi az adattípus?

Az adattípus meghatározza:

- milyen értéket tárolunk
- milyen műveletek végezhetők rajta
- hogyan értelmezi a rendszer az adatot

## Fontos adattípusok

### Egész szám

Példa:

- `5`
- `-12`

### Lebegőpontos szám

Példa:

- `3.14`

### Logikai

Példa:

- `true`
- `false`

### Szöveg / karakterlánc

Példa:

- `"hello"`

## Mi az adatszerkezet?

Az adatszerkezet azt írja le, hogyan szervezzük az adatokat úgy, hogy:

- könnyű legyen kezelni őket
- hatékony legyen a keresés, módosítás vagy bejárás

## Fontos adatszerkezetek

| Adatszerkezet | Mire jó? |
|---|---|
| tömb / array | azonos típusú elemek sorozata |
| lista | rendezett elemsor |
| verem / stack | `LIFO` logika |
| sor / queue | `FIFO` logika |
| szótár / map | kulcs-érték alapú tárolás |
| objektum | összetartozó adatok és műveletek szervezése |

## Miért fontosak?

- helyes adattípus nélkül könnyen hibázik a program
- jó adatszerkezettel gyorsabb és tisztább megoldás készülhet
- befolyásolják a memóriahasználatot és a teljesítményt

## Adattípus és adatszerkezet: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| adattípus | egy adatfajta |
| adatszerkezet | adatok szervezett együttese |

## Vizsgán jól használható megfogalmazás

> Az adattípus azt határozza meg, hogy milyen jellegű adatot kezelünk, például egész számot, szöveget vagy logikai értéket.  
> Az adatszerkezet ezzel szemben azt írja le, hogyan szervezzük és tároljuk az adatokat, például tömbben, listában, veremben vagy kulcs-érték párok formájában.  
> A megfelelő adattípus és adatszerkezet kiválasztása fontos a program helyes működése és teljesítménye szempontjából.

## Gyakori vizsgahibák

- Az adattípust és adatszerkezetet összekeverni.
- Csak alap típusokat említeni, szerkezeteket nem.
- Nem megemlíteni a teljesítmény szempontját.
- Azt hinni, hogy az adatszerkezet csak adatbázisos fogalom.

## Gyors önellenőrzés

1. Mi az adattípus?
2. Mi az adatszerkezet?
3. Mondj négy fontos adattípust.
4. Mondj négy fontos adatszerkezetet.
5. Miért számít a jó választás?

## Rövid válaszok az önellenőrzéshez

1. Az adat fajtájának leírása
2. Az adatok szervezett formája
3. Egész, lebegőpontos, logikai, szöveg
4. Tömb, lista, verem, sor
5. Mert hat a helyességre és teljesítményre

## Források

1. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Használat: hivatalos, modern forrás az alap adattípusokhoz.

2. Python Docs - Data Structures  
   https://docs.python.org/3/tutorial/datastructures.html  
   Használat: hivatalos, jól strukturált forrás a gyakori adatszerkezetek szemléltetéséhez.

Megnyitva: `2026-04-09`
