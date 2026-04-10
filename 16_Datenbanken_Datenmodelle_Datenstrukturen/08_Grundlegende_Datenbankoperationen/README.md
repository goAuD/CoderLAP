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

## Vizsgán jól használható megfogalmazás

> Az alapvető adatbázis-műveletek a rekordok létrehozása, lekérdezése, módosítása és törlése.  
> Ezeket relációs adatbázisban tipikusan az `INSERT`, `SELECT`, `UPDATE` és `DELETE` SQL-parancsokkal végezzük.  
> Ezek a műveletek alkotják a legtöbb adatbázis-alapú alkalmazás működésének alapját.

## Gyakori vizsgahibák

- A lekérdezést összekeverni a módosítással.
- A `SELECT`-et az egyetlen fontos műveletnek tekinteni.
- Nem megemlíteni a `WHERE` szerepét.
- Kihagyni, hogy ezek alkalmazásszinten a `CRUD` fogalomhoz kötődnek.

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
