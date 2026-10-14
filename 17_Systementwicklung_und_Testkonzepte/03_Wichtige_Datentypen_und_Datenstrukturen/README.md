# Wichtige Datentypen und Datenstrukturen

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
| tömb / array | indexelhető elemsor; a megengedett elemtípusok nyelvfüggők |
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

## A művelethez választunk adatszerkezetet

Feladat: egyszer számoljuk az elvégzett témákat, címüket pedig azonosító alapján
keressük. Node.js-ben futtatható megoldás:

<!-- example:run -->

```javascript
const completed = new Set(["LAP-15-01", "LAP-15-01", "LAP-15-02"]);
const titles = new Map([["LAP-15-01", "Lifecycle"], ["LAP-15-02", "Paradigms"]]);
console.log(completed.size);
console.log(completed.has("LAP-15-02"));
console.log(titles.get("LAP-15-01"));
```

```text
2
true
Lifecycle
```

A `Set` egyedi értékeket tárol, ezért az ismételt `LAP-15-01` nem növeli a
darabszámot. A `Map` kulcs alapján ad vissza értéket. Ha a tanulási sorrend és
az ismétlések is fontosak, külön tömbben tárolhatjuk a gyakorlási eseményeket.
Így a választást az elvárt művelet indokolja: sorrend, egyediség vagy kulcsos keresés.

A lista rendezettsége itt azt jelenti, hogy az elemeknek sorrendjük van, nem azt,
hogy érték szerint növekvők. Egy JavaScript `Array` különböző típusokat is
tartalmazhat; a homogén elemkövetelmény nyelv- vagy konkrét tárolótípus-függő.
A típus fogalma az összetett típusokra is kiterjed, tehát adattípus és
adatszerkezet nem két egymást kizáró kategória.

## Vizsgán jól használható megfogalmazás

> Az adattípus azt határozza meg, hogy milyen jellegű adatot kezelünk, például egész számot, szöveget vagy logikai  
> értéket.  
> Az adatszerkezet ezzel szemben azt írja le, hogyan szervezzük és tároljuk az adatokat, például tömbben, listában,  
> veremben vagy kulcs-érték párok formájában.  
> A megfelelő adattípus és adatszerkezet kiválasztása fontos a program helyes működése és teljesítménye szempontjából.

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

Ellenőrizve: `2026-10-14`.

- [MDN: Keyed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections): Map és Set választása.


1. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Használat: hivatalos, modern forrás az alap adattípusokhoz.

2. Python Docs - Data Structures  
   https://docs.python.org/3/tutorial/datastructures.html  
   Használat: hivatalos, jól strukturált forrás a gyakori adatszerkezetek szemléltetéséhez.

Megnyitva: `2026-04-09`
