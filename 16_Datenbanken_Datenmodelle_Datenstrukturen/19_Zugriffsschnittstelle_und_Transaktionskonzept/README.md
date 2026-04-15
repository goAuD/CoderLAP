# Zugriffsschnittstelle und Transaktionskonzept

## Gyors vizuális kép

```text
Alkalmazás
    -> hozzáférési interfész / driver / API
    -> DBMS
    -> adatbázis

Tranzakció:
    BEGIN
      művelet 1
      művelet 2
    COMMIT vagy ROLLBACK
```

## Mi az a hozzáférési interfész?

Ez az a technikai réteg, amelyen keresztül az alkalmazás kommunikál az adatbázissal.

Tipikus példák:

- `JDBC`
- `ODBC`
- `ADO.NET`
- ORM vagy adat-hozzáférési rétegek

Feladatuk:

- kapcsolat létrehozása
- SQL-parancsok küldése
- eredmények fogadása
- hibák kezelése

## Mi az a tranzakció?

A tranzakció több adatbázis-művelet olyan egysége, amely:

- együtt hajtódik végre
- vagy együtt hiúsul meg

Példa:

- rendelés rögzítése
- készlet csökkentése

Ha az egyik sikerül, a másik nem, akkor a rendszer hibás állapotba kerülhetne, ezért kell tranzakció.

## Alapfogalmak

| Fogalom | Jelentés |
|---|---|
| `BEGIN` | tranzakció indítása |
| `COMMIT` | véglegesítés |
| `ROLLBACK` | visszavonás |

## Miért fontos a tranzakciós koncepció?

- megőrzi a konzisztenciát
- csökkenti a részben elvégzett műveletek veszélyét
- alapja a megbízható üzleti folyamatoknak

## Interfész és tranzakció: ne keverd össze

| Fogalom | Szerep |
|---|---|
| hozzáférési interfész | technikai kapcsolat az alkalmazás és a DB között |
| tranzakció | logikai műveleti egység az adatkezelésben |

## ACID röviden

Vizsgán plusz pontot érhet:

- `Atomicity`
- `Consistency`
- `Isolation`
- `Durability`

Nem mindig kell mélyen kifejteni, de jó, ha tudod, hogy a tranzakciók klasszikus minőségi alapelvei.

## Vizsgán jól használható megfogalmazás

> A hozzáférési interfész biztosítja, hogy egy alkalmazás kapcsolatba tudjon lépni az adatbázissal, SQL-parancsokat  
> küldjön és eredményeket kapjon vissza.  
> A tranzakciós koncepció pedig azt jelenti, hogy az összetartozó adatbázis-műveleteket egy egységként kezeljük,  
> amelyek vagy teljes egészében végrehajtódnak, vagy hiba esetén visszagörgethetők.  
> Ez a megbízható és konzisztens adatkezelés alapja.

## Gyakori vizsgahibák

- Az interfészt magával az adatbázissal azonosítani.
- A tranzakciót egyszerű lekérdezésnek nevezni.
- Nem megemlíteni a `COMMIT` és `ROLLBACK` szerepét.
- Kihagyni, hogy a cél a konzisztencia megőrzése.

## Gyors önellenőrzés

1. Mi az a hozzáférési interfész?
2. Mi az a tranzakció?
3. Mire jó a `COMMIT`?
4. Mire jó a `ROLLBACK`?
5. Miért fontos az, hogy több műveletet együtt kezeljünk?

## Rövid válaszok az önellenőrzéshez

1. Alkalmazás és adatbázis közti kapcsolati réteg
2. Összetartozó adatbázis-műveletek egysége
3. A módosítások véglegesítésére
4. A sikertelen műveletek visszavonására
5. Mert így marad konzisztens az adat

## Források

1. Oracle - JDBC Basics  
   https://docs.oracle.com/javase/tutorial/jdbc/basics/index.html  
   Használat: hivatalos forrás a tipikus adatbázis-hozzáférési interfész működéséhez.

2. Microsoft Learn - Local Transactions  
   https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/local-transactions  
   Használat: hivatalos, jól érthető forrás a tranzakciók programozási kezeléséhez.

3. PostgreSQL - Transactions  
   https://www.postgresql.org/docs/current/tutorial-transactions.html  
   Használat: hivatalos háttér a `BEGIN`, `COMMIT`, `ROLLBACK` alaplogikájához.

Megnyitva: `2026-04-09`
