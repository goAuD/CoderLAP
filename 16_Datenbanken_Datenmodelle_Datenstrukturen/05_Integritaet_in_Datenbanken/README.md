# Integritaet in Datenbanken

## Gyors vizuális kép

| Integritástípus | Példa |
|---|---|
| entitásintegritás | az elsődleges kulcs nem lehet `NULL` |
| referenciális integritás | a megadott, nem NULL idegenkulcsértékhez létező hivatkozott kulcs tartozik |
| tartományintegritás | az adat csak megengedett érték lehet |

## Mit jelent az integritás?

Az integritás azt biztosítja, hogy az adatbázis:

- logikailag következetes maradjon
- ne kerüljenek bele hibás kapcsolatok
- a szabályok ne sérüljenek adatbevitel vagy módosítás közben

## Tipikus integritási szabályok

### `NOT NULL`

Az érték nem lehet `NULL`. Üres szöveget (`''`) önmagában nem tilt.

### `UNIQUE`

A megadott oszlopok értékkombinációja egyedi; a `NULL` kezelése DBMS-függő.

### `PRIMARY KEY`

Azonosítja a rekordot.

### `FOREIGN KEY`

Hivatkozási szabályt biztosít ugyanannak vagy egy másik táblának a megfelelő kulcsára.

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

## Kidolgozott megszorítások

**MySQL 8.0.16+ / InnoDB, üres gyakorló adatbázis.** Ebben a verziótartományban a `CHECK` feltételt a szerver ténylegesen ellenőrzi.

<!-- example:mysql -->
```sql
CREATE TABLE products (
  id INT PRIMARY KEY,
  sku VARCHAR(20) NOT NULL UNIQUE,
  price DECIMAL(8,2) NOT NULL CHECK (price >= 0),
  note VARCHAR(40) NULL
) ENGINE=InnoDB;
INSERT INTO products VALUES (1, 'BOOK-1', 12.50, '');
SELECT id, price, note IS NULL AS note_is_null,
       CHAR_LENGTH(note) AS note_length
FROM products ORDER BY id;
```

```text
1 12.50 0 0
```

Az üres `note` hosszúsága nulla, de nem `NULL`. A `price = -1` értékkel próbált beszúrást a `CHECK`, az ismételt `BOOK-1` cikkszámot a `UNIQUE`, a `NULL` árat a `NOT NULL` tiltja. A `CHECK (price >= 0)` önmagában megengedné a `NULL`-ból eredő ismeretlen logikai értéket, ezért együtt használjuk a `NOT NULL` szabállyal.

MySQL-ben egy nullable `UNIQUE` oszlop több `NULL`-t is megenged. Ha az érték kötelező és egyedi, mindkét követelményt írd elő. A megszorítások a tárolt szabályokat kényszerítik ki: azt nem tudják maguktól, hogy egy valós termék árát helyesen írtuk-e be. Ehhez üzleti ellenőrzés is kell.

## Vizsgán jól használható megfogalmazás

> Az integritás az adatbázisban tárolt adatok helyességét és következetességét jelenti.  
> Ezt a `DBMS` különböző szabályokkal biztosíthatja, például `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `UNIQUE` és  
> `CHECK` megszorításokkal.  
> Az integritás célja, hogy az adatbázis ne kerülhessen hibás vagy ellentmondásos állapotba.

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

### A bővítés ellenőrzött forrásai

- [MySQL: CHECK constraints](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html): CHECK, TRUE/UNKNOWN és verzióhatár
- [MySQL: CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html): NOT NULL, UNIQUE és kulcsok

Ellenőrizve: `2026-10-14`.
