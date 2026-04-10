# Umsetzung von Datenmodellen in Datenbanken

## Gyors vizuális kép

| Modell elem | Adatbázis-megvalósítás |
|---|---|
| entitás | tábla |
| attribútum | oszlop |
| egyedi azonosító | `PRIMARY KEY` |
| kapcsolat | `FOREIGN KEY` |
| szabály | `NOT NULL`, `UNIQUE`, `CHECK` |

## Hogyan történik az átültetés?

### 1. Entitások -> táblák

Például:

- `Customer` entitásból `customers` tábla

### 2. Attribútumok -> oszlopok

Például:

- név
- cím
- e-mail
- dátum

### 3. Kulcsok kijelölése

- elsődleges kulcs
- idegen kulcs
- szükség szerint egyedi kulcsok

### 4. Kapcsolatok leképezése

- `1:1`
- `1:n`
- `n:m` kapcsolótáblával

### 5. Integritási szabályok megadása

- kötelező mezők
- egyediség
- értéktartományok
- kapcsolati szabályok

## Miért fontos ez a lépés?

Mert itt dől el, hogy:

- a modell ténylegesen működő adatbázissá válik-e
- a szabályok mennyire lesznek kikényszeríthetők
- az adatbázis mennyire lesz karbantartható

## Logikai és fizikai megvalósítás

| Szint | Mire fókuszál? |
|---|---|
| logikai | táblák, kulcsok, kapcsolatok |
| fizikai | adattípusok, indexek, vendor-specifikus megoldások |

## Mire kell figyelni?

- jó adattípus választás
- kulcsok helyes kijelölése
- kapcsolatok pontos modellezése
- fölösleges redundancia elkerülése

## Vizsgán jól használható megfogalmazás

> Az adatmodellek adatbázisba történő megvalósítása során a fogalmi vagy logikai modell elemeit konkrét adatbázis-struktúrává alakítjuk.  
> Az entitásokból táblák, az attribútumokból oszlopok, a kapcsolatokból pedig elsődleges és idegen kulcsok, illetve szükség esetén kapcsolótáblák lesznek.  
> Emellett ekkor kerülnek meghatározásra az adattípusok, integritási szabályok és más technikai részletek is.

## Gyakori vizsgahibák

- A modellezést és a megvalósítást ugyanannak tekinteni.
- Az `n:m` kapcsolatnál nem használni kapcsolótáblát.
- Nem megemlíteni a megszorításokat.
- Kihagyni az adattípusok szerepét.

## Gyors önellenőrzés

1. Mi lesz az entitásból?
2. Mi lesz az attribútumból?
3. Hogyan valósítunk meg kapcsolatot?
4. Miért kellenek megszorítások?
5. Mi a különbség logikai és fizikai megvalósítás között?

## Rövid válaszok az önellenőrzéshez

1. Tábla
2. Oszlop
3. Kulcsokkal és szükség esetén kapcsolótáblával
4. Hogy az adatok helyesek maradjanak
5. Az egyik általános szerkezet, a másik technikai részletek

## Források

1. Oracle SQL Developer Data Modeler  
   https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/  
   Használat: hivatalos forrás az adatmodellek logikai és fizikai megvalósítási szintjeihez.

2. PostgreSQL - Data Definition  
   https://www.postgresql.org/docs/current/ddl.html  
   Használat: hivatalos forrás arra, hogyan jelennek meg a modellek táblákban, kulcsokban és megszorításokban.

Megnyitva: `2026-04-09`
