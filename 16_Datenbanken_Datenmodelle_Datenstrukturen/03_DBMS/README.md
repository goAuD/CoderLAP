# DBMS

## Gyors vizuális kép

| `DBMS` feladat | Mit jelent? |
|---|---|
| tárolás | adatok kezelése a háttérben |
| lekérdezés | adatok kiolvasása és módosítása |
| hozzáférésvezérlés | ki mit láthat / módosíthat |
| integritás | szabályok betartása |
| adminisztráció | mentés, recovery, tuning, felügyelet |

## Mi az a `DBMS`?

A `DBMS` egy szoftverréteg a felhasználó vagy alkalmazás és a tárolt adatok között.

Feladata például:

- az adatok fizikai és logikai kezelése
- a lekérdezések végrehajtása
- az egyidejű hozzáférések koordinálása
- a szabályok és kulcsok érvényesítése

## Miért fontos?

- nem kell közvetlenül az alacsony szintű tárolással foglalkozni
- biztonságosabb és strukturáltabb adatkezelést ad
- támogatja a többfelhasználós működést
- segíti a teljesítmény optimalizálását

## Tipikus részei

Az Oracle adatbázisos fogalomrendszer alapján egy `DBMS` tipikusan tartalmaz:

- vezérlő és tárolókezelő komponenseket
- metaadattárat vagy adatszótárat
- lekérdezőnyelvi támogatást

## `DBMS` és adatbázis: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| adatbázis | a tárolt adatok halmaza |
| `DBMS` | az ezeket kezelő szoftver |

## Példák

Ismert `DBMS`-ek:

- `PostgreSQL`
- `MySQL`
- `Oracle Database`
- `Microsoft SQL Server`
- `SQLite`

## Vizsgán jól használható megfogalmazás

> A `DBMS`, vagyis Database Management System az a szoftver, amely az adatbázis létrehozását, kezelését, lekérdezését, védelmét és adminisztrációját végzi.  
> A `DBMS` közvetít az alkalmazások és a tárolt adatok között, valamint biztosítja például az integritást, a többfelhasználós működést és az adatkezelés szabályait.  
> Ezért a `DBMS` az adatbázisrendszer központi eleme.

## Gyakori vizsgahibák

- A `DBMS`-t az adatbázissal azonosítani.
- A `DBMS`-t pusztán lekérdezőprogramnak nevezni.
- Nem megemlíteni az adminisztrációs és integritási funkciókat.
- Kihagyni, hogy többfelhasználós hozzáférést is kezel.

## Gyors önellenőrzés

1. Mi az a `DBMS`?
2. Milyen fő feladatai vannak?
3. Miben különbözik az adatbázistól?
4. Miért fontos a többfelhasználós működés kezelése?
5. Mondj három ismert `DBMS`-t.

## Rövid válaszok az önellenőrzéshez

1. Adatbáziskezelő szoftver
2. Tárolás, lekérdezés, hozzáférés, integritás, adminisztráció
3. Az egyik az adat, a másik a kezelő szoftver
4. Mert sokan dolgozhatnak ugyanazzal az adattal
5. PostgreSQL, MySQL, Oracle Database

## Források

1. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Használat: hivatalos elsődleges forrás a `DBMS` definíciójához és fő elemeihez.

2. Oracle - What Is a Database?  
   https://www.oracle.com/database/what-is-database/  
   Használat: modern, könnyen olvasható összefoglaló a `DBMS` szerepéhez.

Megnyitva: `2026-04-09`
