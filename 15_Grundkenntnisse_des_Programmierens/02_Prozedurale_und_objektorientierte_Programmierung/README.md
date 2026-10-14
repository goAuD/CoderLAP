# Prozedurale und objektorientierte Programmierung

## Gyors vizuális kép

| Szempont | Procedurális | Objektumorientált |
|---|---|---|
| fő egység | eljárás / függvény | osztály / objektum |
| fókusz | mit csinál a program? | milyen dolgok vannak a rendszerben? |
| adatok | gyakran külön kezeljük | az objektumhoz kapcsoljuk |
| szervezési szempont | jól elkülöníthető műveletek | összetartozó állapot és viselkedés |

## Mi az a procedurális programozás?

A procedurális megközelítésben a program:

- utasítások sorozatából áll
- függvényekre vagy eljárásokra tagolódik
- az adatokon végzett műveletekre koncentrál

Ez a gondolkodás közel áll az algoritmusokhoz:

- bemenet
- feldolgozás
- kimenet

## Mi az az objektumorientált programozás?

Az objektumorientált megközelítésben a rendszer elemeit objektumokként modellezzük.

Egy objektum jellemzően tartalmaz:

- adatot, azaz állapotot
- műveleteket, azaz metódusokat

Az objektumok általában osztályok alapján jönnek létre.

## Miért fontos a különbség?

Mert nem ugyanúgy szervezed meg a programot.

### Procedurális megközelítésnél

- a lépéssor dominál
- gyorsan áttekinthető lehet
- kisebb feladatoknál egyszerű

### Objektumorientált megközelítésnél

- a rendszer elemei jobban modellezhetők
- könnyebb lehet a bővíthetőség
- nagyobb projekteknél jobban skálázódhat

## Egyszerű példa

### Procedurális gondolkodás

```text
számol_bér()
kiír_bérjegyzék()
ment_fájlba()
```

### Objektumorientált gondolkodás

```text
Alkalmazott
  - név
  - fizetés
  - számolBér()
```

## A megközelítés kiválasztása

A feladat adatainak, műveleteinek és változási igényeinek megfelelő szervezést válasszunk. Egy program több paradigmát is használhat.

## Ugyanaz a pontszám kétféle szervezéssel

Feladat: először 3, majd 2 pontot adunk egy nulláról induló pontszámhoz. A példa
ellenőrzött, nemnegatív egész bemeneteket feltételez. Node.js-ben futtatható.

<!-- example:run -->

```javascript
function addPoints(score, points) {
  return score + points;
}
class Score {
  #value = 0;
  add(points) { this.#value += points; }
  get value() { return this.#value; }
}
let total = addPoints(0, 3);
total = addPoints(total, 2);
const score = new Score();
score.add(3);
score.add(2);
console.log(total, score.value);
```

```text
5 5
```

A függvény megkapja a régi értéket, és új értéket ad vissza. Az osztály példánya
őrzi a saját állapotát, az `add` metódus ezt változtatja. A `#value` privát mező;
a kívülről olvasható `value` getter csak lekérdezést enged. Két `Score` példány
két külön pontszámot tárolna. Egy egyszerű számításhoz a függvény gyakran elég;
összetartozó állapot és műveletek esetén indokolt lehet az objektum.

A választás nem a program méretéből következik. Nagy rendszert is lehet
moduláris függvényekből építeni. JavaScriptben osztály nélkül, objektumliterállal
is készülhet objektum; az objektum és az osztály ezért nem szinonima.

## Vizsgán jól használható megfogalmazás

> A procedurális programozás a feladatot műveletek és függvények sorozataként szervezi meg, míg az objektumorientált  
> programozás a rendszer elemeit objektumokkal és osztályokkal modellezi.  
> A procedurális megközelítés főleg a végrehajtandó lépésekre, az objektumorientált megközelítés pedig az adatok és a  
> hozzájuk tartozó műveletek egységére koncentrál.  
> Mindkét paradigma hasznos, és a választás a feladattól függ.

## Gyors önellenőrzés

1. Mi a procedurális programozás fő fókusza?
2. Mi a OOP fő fókusza?
3. Mi az osztály és objektum kapcsolata?
4. Melyik megközelítés lehet egyszerűbb kisebb feladatokra?
5. Miért nem igaz, hogy csak egyetlen jó paradigma létezik?

## Rövid válaszok az önellenőrzéshez

1. A műveletek és függvények
2. Az objektumok és azok állapota + viselkedése
3. Az objektum az osztály példánya
4. Gyakran a procedurális
5. Mert a feladat dönti el, melyik előnyösebb

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes): privát mező, getter és példányállapot.


1. Oracle Java Tutorials - Object-Oriented Programming Concepts  
   https://docs.oracle.com/javase/tutorial/java/concepts  
   Használat: hivatalos alapforrás az objektumorientált szemlélet fő fogalmaihoz.

2. Oracle - Lesson 8: Object-Oriented Programming  
   https://www.oracle.com/java/technologies/oop.html  
   Használat: rövid, hivatalos áttekintés az OOP alapgondolatáról és nyelvi elemeiről.

Megnyitva: `2026-04-09`
