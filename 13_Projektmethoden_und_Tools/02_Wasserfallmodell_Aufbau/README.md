# Wasserfallmodell Aufbau

## Gyors vizuális kép

`Követelmények -> Tervezés -> Implementáció -> Teszt -> Bevezetés -> Karbantartás`

## Mi a vízesésmodell lényege?

Az, hogy egy fázist lehetőleg lezárunk, mielőtt a következőre átlépünk.

Ezért a modell:

- jól strukturált
- erősen dokumentációközpontú
- kevésbé rugalmas változó környezetben

## Tipikus fázisai

### 1. Követelmények

- mit kell tudnia a rendszernek

### 2. Tervezés

- hogyan fog felépülni a megoldás

### 3. Implementáció

- a tényleges fejlesztés

### 4. Verifikáció / tesztelés

- ellenőrzés, hogy jól működik-e

### 5. Bevezetés és karbantartás

- használatba vétel és hibajavítás

## Miért volt sokáig népszerű?

- egyszerűen érthető
- könnyű kommunikálni
- jól dokumentálható
- stabil, előre ismert követelményeknél működhet

## Vízesés és agilis: ne keverd össze

| Szempont | Vízesés | Agilis |
|---|---|---|
| felépítés | lineáris | iteratív |
| változáskezelés | nehezebb | rugalmasabb |
| visszajelzés | később | gyakrabban |

## Mit adunk át az egyes fázisok között?

Egy megadott számlaformátum átalakítójánál a követelményszakasz eredménye lehet a mezőleírás és az elfogadott bemenet-kimenet példák. A terv megmondja a feldolgozás lépéseit és a hibajelzéseket. Az implementáció után a tesztek ugyanazokkal a mintákkal ellenőrzik az átalakítást, majd dokumentált telepítés és átadás következik.

A fázishatáron rögzítjük, ki fogadja el az eredményt és melyik változat az alap. Ha később új kötelező mező jelenik meg, hatáselemzés készül: melyik követelményt, tervet, kódot és tesztet kell módosítani? A visszalépés lehetséges, de összehangolt változáskezelést igényel.

A fázisok sorrendje nem tiltja a korai dokumentumreview-t vagy a tesztek előzetes megtervezését. Ezekkel még az implementáció előtt tisztázhatók a félreérthető szabályok.

## Vizsgán jól használható megfogalmazás

> A vízesésmodell egy lineáris szoftverfolyamat-modell,
> amelyben a fejlesztés fő fázisai
> jellemzően egymás után következnek.  
> Tipikus fázisai a követelményelemzés, tervezés, implementáció, tesztelés, bevezetés és karbantartás.  
> Előnye az átlátható szerkezet, hátránya pedig az, hogy kevésbé rugalmas, ha a követelmények menet közben változnak.

## Gyors önellenőrzés

1. Mi a vízesésmodell lényege?
2. Melyek a tipikus fázisai?
3. Miért könnyen érthető?
4. Milyen projektnél lehet jó választás?
5. Mi a fő különbség közte és az agilis között?

## Rövid válaszok az önellenőrzéshez

1. Egymás utáni, lineáris fázisok
2. Követelmény, tervezés, fejlesztés, teszt, bevezetés
3. Mert világos sorrendje van
4. Stabil követelményű projektnél
5. A vízesés kevésbé rugalmas

## Források

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Teszttevékenységek a fejlesztési életciklusban, korai ellenőrzés.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Atlassian - What is the Waterfall methodology?  
   https://www.atlassian.com/agile/project-management/waterfall-methodology  
   Használat: a vízesésmodell modern, jól strukturált összefoglalása és tipikus fázisai.

2. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Használat: a lineáris és iteratív modellek összevetésének hivatalos, aktuális háttere.

Megnyitva: `2026-04-08`
