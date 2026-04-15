# Prozedurale und objektorientierte Programmierung

## Gyors vizuális kép

| Szempont | Procedurális | Objektumorientált |
|---|---|---|
| fő egység | eljárás / függvény | osztály / objektum |
| fókusz | mit csinál a program? | milyen dolgok vannak a rendszerben? |
| adatok | gyakran külön kezeljük | az objektumhoz kapcsoljuk |
| jó választás | kisebb, lineárisabb feladatok | nagyobb, összetettebb rendszerek |

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

## Ne keverd össze

| Tévhit | Miért hibás? |
|---|---|
| az OOP mindig jobb | nem mindig, feladattól függ |
| a procedurális programozás elavult | ma is sok helyen hasznos |
| OOP = csak class kulcsszó | az OOP szemlélet ennél több |

## Vizsgán jól használható megfogalmazás

> A procedurális programozás a feladatot műveletek és függvények sorozataként szervezi meg, míg az objektumorientált  
> programozás a rendszer elemeit objektumokkal és osztályokkal modellezi.  
> A procedurális megközelítés főleg a végrehajtandó lépésekre, az objektumorientált megközelítés pedig az adatok és a  
> hozzájuk tartozó műveletek egységére koncentrál.  
> Mindkét paradigma hasznos, és a választás a feladattól függ.

## Gyakori vizsgahibák

- Az OOP-t automatikusan fejlettebbnek nevezni minden helyzetben.
- A procedurális megközelítést csak “régi stílusnak” beállítani.
- Nem megemlíteni az adatok és műveletek kapcsolatát.
- Az OOP-t pusztán öröklésre leszűkíteni.

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

1. Oracle Java Tutorials - Object-Oriented Programming Concepts  
   https://docs.oracle.com/javase/tutorial/java/concepts  
   Használat: hivatalos alapforrás az objektumorientált szemlélet fő fogalmaihoz.

2. Oracle - Lesson 8: Object-Oriented Programming  
   https://www.oracle.com/java/technologies/oop.html  
   Használat: rövid, hivatalos áttekintés az OOP alapgondolatáról és nyelvi elemeiről.

Megnyitva: `2026-04-09`
