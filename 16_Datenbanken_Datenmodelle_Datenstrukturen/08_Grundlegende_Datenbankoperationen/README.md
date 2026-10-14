# Grundlegende Datenbankoperationen

## Gyors vizuális kép

| Művelet | Jelentés |
|---|---|
| Create | új adat létrehozása |
| Read | adat lekérdezése |
| Update | adat módosítása |
| Delete | adat törlése |

## Miért alapvetőek ezek a műveletek?

Mert szinte minden adatbázisos alkalmazás ezekre épül.

Például:

- új ügyfél rögzítése
- rendelés lekérdezése
- cím módosítása
- régi rekord törlése

## A négy legfontosabb SQL-parancs

### `SELECT`

Adatok kiolvasására szolgál.

### `INSERT`

Új sor beszúrására szolgál.

### `UPDATE`

Meglévő rekordok módosítására szolgál.

### `DELETE`

Sorok törlésére szolgál.

## Mire kell figyelni?

- a `WHERE` feltétel nagyon fontos
- hibás `UPDATE` vagy `DELETE` túl sok sort érinthet
- a módosító műveleteket gyakran tranzakcióban érdemes kezelni

## `CRUD` és SQL: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| `CRUD` | általános műveleti modell |
| `SQL` | konkrét nyelvi megvalósítás |

## Kidolgozott CRUD-példa visszavonással

**MySQL 8.0 / InnoDB, üres gyakorló adatbázis.** A példa létrehoz két feladatot, egy tranzakción belül módosít és töröl, majd visszavonja a módosításokat. Az első eredmény a tranzakción belüli egy sor; a második eredmény a visszaállított két sor.

<!-- example:mysql -->
```sql
CREATE TABLE tasks (
  id INT PRIMARY KEY,
  status VARCHAR(10) NOT NULL
) ENGINE=InnoDB;
INSERT INTO tasks VALUES (1, 'draft'), (2, 'done');

START TRANSACTION;
UPDATE tasks SET status = 'done' WHERE id = 1;
DELETE FROM tasks WHERE id = 2;
SELECT id, status FROM tasks ORDER BY id;
ROLLBACK;
SELECT id, status FROM tasks ORDER BY id;
```

```text
1 done
1 draft
2 done
```

A `CREATE TABLE` a szerkezetet hozza létre: ez DDL. A CRUD „Create” lépése itt az `INSERT`, amely adatot hoz létre, nem új táblát. Az `INSERT`, `UPDATE`, `DELETE` adatkezelő művelet; a `GRANT` és `REVOKE` jogosultságokat szabályoz. A `SELECT` külön DQL-csoportként vagy a tágabb DML részeként is szerepelhet a tankönyvekben.

Módosítás előtt egy azonos feltételű `SELECT` segít ellenőrizni a célhalmazt. Utána az érintett sorok számát is nézd meg. Többfelhasználós környezetben a külön előzetes lekérdezés önmagában még nem véd egy közben történő változástól; ehhez megfelelő tranzakciós eljárás kell.

Ebben a példában a visszavonható adatmódosítások vannak a tranzakcióban. MySQL-ben több szerkezetmódosító utasítás implicit commitot okoz, ezért a `CREATE TABLE` nem általános „biztonsági próba” egy `ROLLBACK` előtt.

## Vizsgán jól használható megfogalmazás

> Az alapvető adatbázis-műveletek a rekordok létrehozása, lekérdezése, módosítása és törlése.  
> Ezeket relációs adatbázisban tipikusan az `INSERT`, `SELECT`, `UPDATE` és `DELETE` SQL-parancsokkal végezzük.  
> Ezek a műveletek alkotják a legtöbb adatbázis-alapú alkalmazás működésének alapját.

## Gyors önellenőrzés

1. Mit jelent a `CRUD`?
2. Mire való a `SELECT`?
3. Mire való az `UPDATE`?
4. Miért veszélyes `WHERE` nélkül módosítani vagy törölni?
5. Miért nevezhetők ezek alapműveleteknek?

## Rövid válaszok az önellenőrzéshez

1. Create, Read, Update, Delete
2. Adatok kiolvasására
3. Meglévő adatok módosítására
4. Mert túl sok rekordot érinthet
5. Mert szinte minden alkalmazás használja őket

## Források

1. PostgreSQL - SQL Commands  
   https://www.postgresql.org/docs/current/sql-commands.html  
   Használat: hivatalos forrás az alap SQL-műveletekhez.

2. PostgreSQL - Tutorial  
   https://www.postgresql.org/docs/current/tutorial-sql.html  
   Használat: gyakorlati, hivatalos összefoglaló az alapvető adatbázis-műveletek használatához.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [MySQL: COMMIT and ROLLBACK](https://dev.mysql.com/doc/refman/8.0/en/commit.html): tranzakció és az adatmódosítás visszavonása
- [MySQL: Implicit Commit](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html): DDL és implicit commit

Ellenőrizve: `2026-10-14`.
