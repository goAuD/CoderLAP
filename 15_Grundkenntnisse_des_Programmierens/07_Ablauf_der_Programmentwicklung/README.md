# Ablauf der Programmentwicklung

## Lényeg 30 másodpercben

A programfejlesztés gyakorlati menete általában: problémaértés, tervezés, kódolás, futtatás, hibakeresés, tesztelés és javítás.

Röviden:

- ez egy gyakorlati ciklus
- ritkán lineáris
- sokszor vissza kell lépni és pontosítani

## Gyors vizuális kép

```text
Feladat megértése
    -> megoldás tervezése
    -> kódolás
    -> futtatás / fordítás
    -> hibakeresés
    -> tesztelés
    -> javítás / finomítás
```

## Miért más ez, mint a teljes szoftver-életciklus?

Az előző, nagyobb életciklus-szakaszok inkább projekt-szintű nézőpontot adnak.  
Az `Ablauf der Programmentwicklung` inkább a fejlesztő gyakorlati munkafolyamatát írja le.

## Tipikus lépések részletesebben

### 1. Feladat megértése

Meg kell érteni:

- mi a cél
- mi a bemenet
- mi a kimenet
- milyen szabályokat kell követni

### 2. Megoldás megtervezése

Itt jöhet:

- algoritmus
- pseudocode
- folyamatábra
- adatszerkezet kiválasztása

### 3. Kódolás

A tervet átalakítjuk:

- konkrét programnyelvi utasításokká
- függvényekké
- változókká
- szerkezetekké

### 4. Futtatás vagy fordítás

Itt derül ki például:

- van-e szintaktikai hiba
- elindul-e a program
- a környezet helyesen van-e beállítva

### 5. Debuggolás

Ha hiba van:

- meg kell keresni az okát
- figyelni kell a változókat
- ellenőrizni kell a vezérlési utat

### 6. Tesztelés

Itt nem csak az számít, hogy “lefut-e”, hanem az is, hogy:

- helyes eredményt ad-e
- szélső esetekben is jól működik-e

### 7. Javítás és finomítás

Gyakran vissza kell menni:

- a logikához
- a kódhoz
- vagy akár a tervezéshez

## Ez nem egyszeri sor, hanem ciklus

Vizsgán érdemes kimondani:

- a fejlesztés sokszor iteratív
- a hibajavítás és tesztelés többször ismétlődik

## Vizsgán jól használható megfogalmazás

> A programfejlesztés gyakorlati menete általában a feladat megértésével kezdődik, majd következik a megoldás megtervezése, a kódolás, a futtatás vagy fordítás, a hibakeresés, a tesztelés és a javítás.  
> Ez a folyamat a gyakorlatban sokszor iteratív, mert a fejlesztő a tesztek és hibák alapján visszaléphet korábbi lépésekhez is.  
> A cél nemcsak a futó program, hanem a helyes és megbízható program elkészítése.

## Gyakori vizsgahibák

- Kihagyni a tervezést.
- A tesztelést összekeverni az egyszerű futtatással.
- Nem megemlíteni a debuggolást.
- Úgy leírni a folyamatot, mintha mindig teljesen lineáris lenne.

## Gyors önellenőrzés

1. Mivel kezdődik a programfejlesztés?
2. Miért fontos a tervezés?
3. Mi a különbség a futtatás és a tesztelés között?
4. Mi a debugger szerepe?
5. Miért iteratív a folyamat?

## Rövid válaszok az önellenőrzéshez

1. A feladat megértésével
2. Mert így strukturáltabban lehet kódolni
3. A futtatás még nem bizonyít helyes működést
4. Segít megtalálni a hibák okát
5. Mert a hibák miatt vissza kell térni korábbi lépésekhez

## Források

1. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Használat: háttér a fejlesztési lépések logikai sorrendjéhez.

2. Atlassian - SDLC  
   https://www.atlassian.com/en/agile/software-development/sdlc  
   Használat: gyakorlati összefoglaló a fejlesztési folyamat iteratív jellegéhez.

Megnyitva: `2026-04-09`
