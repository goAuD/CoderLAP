# Integritaet in Datenbanken

## Gyors vizuális kép

| Integritástípus | Példa |
|---|---|
| entitásintegritás | az elsődleges kulcs nem lehet `NULL` |
| referenciális integritás | idegen kulcs csak létező rekordra mutathat |
| tartományintegritás | az adat csak megengedett érték lehet |

## Mit jelent az integritás?

Az integritás azt biztosítja, hogy az adatbázis:

- logikailag következetes maradjon
- ne kerüljenek bele hibás kapcsolatok
- a szabályok ne sérüljenek adatbevitel vagy módosítás közben

## Tipikus integritási szabályok

### `NOT NULL`

Kötelező mező nem maradhat üres.

### `UNIQUE`

Egy érték csak egyszer fordulhat elő.

### `PRIMARY KEY`

Azonosítja a rekordot.

### `FOREIGN KEY`

Kapcsolatot biztosít másik táblával.

### `CHECK`

Értéktartományt vagy szabályt ír elő.

## Miért fontos?

- csökkenti a hibás adatbevitel esélyét
- megbízhatóbbá teszi a lekérdezéseket
- segít megőrizni a kapcsolatok helyességét
- alapja a jó minőségű adatbázisnak

## Integritás és validáció: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| alkalmazásoldali validáció | a program ellenőrzi a bevitt adatot |
| adatbázis-integritás | maga az adatbázis is kikényszeríti a szabályt |

A kettő együtt a legerősebb.

## Vizsgán jól használható megfogalmazás

> Az integritás az adatbázisban tárolt adatok helyességét és következetességét jelenti.  
> Ezt a `DBMS` különböző szabályokkal biztosíthatja, például `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE` és `CHECK` megszorításokkal.  
> Az integritás célja, hogy az adatbázis ne kerülhessen hibás vagy ellentmondásos állapotba.

## Gyakori vizsgahibák

- Az integritást csak “biztonságnak” nevezni.
- Nem megemlíteni a kulcsok szerepét.
- A referenciális integritást összekeverni az adatmentéssel.
- Kihagyni, hogy az integritás szabályokkal kikényszeríthető.

## Gyors önellenőrzés

1. Mit jelent az integritás adatbázisban?
2. Mi a referenciális integritás?
3. Mire jó a `CHECK`?
4. Miért fontos a `PRIMARY KEY`?
5. Miért jó, ha az adatbázis maga is ellenőriz?

## Rövid válaszok az önellenőrzéshez

1. Az adatok helyessége és következetessége
2. Az idegen kulcsok helyes kapcsolata
3. Szabály vagy értéktartomány előírására
4. Mert egyértelműen azonosítja a rekordot
5. Mert így kevesebb hibás adat kerülhet be

## Források

1. PostgreSQL - Constraints  
   https://www.postgresql.org/docs/current/ddl-constraints.html  
   Használat: hivatalos forrás az integritási megszorításokhoz.

2. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Használat: kiegészítő háttér a relációs adatmodell és integritási elvek megértéséhez.

Megnyitva: `2026-04-09`
