# Sperrtabelle und Sperrverhalten

## Lényeg 30 másodpercben

A zárolás (`locking`) célja, hogy több felhasználó egyidejű munkája mellett se sérüljön az adatkonzisztencia.

Röviden:

- bizonyos műveletek ideiglenesen zárolnak adatokat
- így elkerülhető az ütközés
- de túl sok vagy rossz zárolás várakozást és holtpontot okozhat

## Gyors vizuális kép

| Jelenség | Mit jelent? |
|---|---|
| lock / zárolás | más műveletek korlátozása ideiglenesen |
| várakozás | egyik tranzakció a másikra vár |
| deadlock | két tranzakció egymásra vár és megakad |

## Mi az a zárolás?

Ha több felhasználó vagy folyamat egyszerre dolgozik ugyanazzal az adattal, a `DBMS` gyakran zárolással védi a konzisztenciát.

Ez történhet például:

- sor szinten
- tábla szinten
- különféle lock-típusokkal

## Mi az a “Sperrtabelle”?

Vizsgás értelemben ez általában azt jelenti, hogy:

- a rendszer nyilvántartja, milyen zárolások vannak érvényben
- melyik tranzakció mit zárol

Nem feltétlenül egy felhasználó által kezelt “normál tábla”, hanem a zárolási állapot logikai vagy belső reprezentációja.

## Miért fontos a zárolási viselkedés?

- megakadályozza, hogy két művelet egyszerre ellentmondó módon írjon
- segít megőrizni a konzisztenciát
- befolyásolja a teljesítményt és a párhuzamosságot

## Lehetséges problémák

### Várakozás

Az egyik tranzakció vár, amíg a másik elengedi a lockot.

### Deadlock

Két tranzakció egymásra vár, és egyik sem tud továbbmenni.

### Túl erős zárolás

Rontja a párhuzamos teljesítményt.

## Zárolás és tranzakció: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| tranzakció | logikailag összetartozó műveletek egysége |
| zárolás | technikai mechanizmus az ütközések elkerülésére |

## Vizsgán jól használható megfogalmazás

> A zárolás célja, hogy több felhasználó egyidejű adatkezelése mellett is megmaradjon az adatkonzisztencia.  
> A `DBMS` különböző lock-mechanizmusokat alkalmazhat, és ezek viselkedése befolyásolja a várakozást, a párhuzamosságot és a teljesítményt.  
> A helytelen vagy túl erős zárolás problémákhoz vezethet, például várakozáshoz vagy deadlockhoz.

## Gyakori vizsgahibák

- A zárolást egyszerű hibának tekinteni.
- Nem megemlíteni, hogy a cél a konzisztencia védelme.
- A `Sperrtabelle` fogalmát szó szerint felhasználói adattáblaként kezelni.
- Kihagyni a deadlock lehetőségét.

## Gyors önellenőrzés

1. Miért van szükség zárolásra?
2. Mit jelent a zárolási viselkedés?
3. Mi a deadlock?
4. Mi a kapcsolat a tranzakció és lock között?
5. Miért okozhat teljesítménygondot a túl sok lock?

## Rövid válaszok az önellenőrzéshez

1. Az adatkonzisztencia védelmére
2. A lockok gyakorlati működését
3. Egymásra váró tranzakciók holtpontja
4. A tranzakció használhat lockokat a védelemhez
5. Mert csökkenti a párhuzamos hozzáférést

## Források

1. PostgreSQL - Explicit Locking  
   https://www.postgresql.org/docs/current/explicit-locking.html  
   Használat: hivatalos forrás a lockok típusaihoz és viselkedéséhez.

2. PostgreSQL - Transaction Isolation  
   https://www.postgresql.org/docs/current/transaction-iso.html  
   Használat: kiegészítő háttér a párhuzamos hozzáférés és konzisztencia kapcsolatának megértéséhez.

Megnyitva: `2026-04-09`
