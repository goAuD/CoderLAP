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

## Kidolgozott séma: a jelentkezési modell megvalósítása

**MySQL 8.0 / InnoDB.** Válassz egy üres, UTF-8-at (`utf8mb4`) használó gyakorló adatbázist. A korábbi modell szerint egy tanuló egy kurzusra egyszer jelentkezhet.

<!-- example:mysql -->
```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(80) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE courses (
  id INT PRIMARY KEY,
  title VARCHAR(80) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE enrollments (
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrolled_on DATE NOT NULL,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE RESTRICT,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE RESTRICT
) ENGINE=InnoDB;
INSERT INTO students VALUES (1, 'Anna');
INSERT INTO courses VALUES (10, 'SQL'), (20, 'JavaScript');
INSERT INTO enrollments VALUES
  (1, 10, '2026-01-10'), (1, 20, '2026-01-11');
SELECT s.name, c.title, e.enrolled_on
FROM enrollments AS e
JOIN students AS s ON s.id = e.student_id
JOIN courses AS c ON c.id = e.course_id
ORDER BY c.id;
```

```text
Anna SQL 2026-01-10
Anna JavaScript 2026-01-11
```

Az összetett elsődleges kulcs megakadályozza ugyanannak a jelentkezésnek az ismétlését. Az idegen kulcsok nem engednek nem létező tanulóra vagy kurzusra mutató sort. A `RESTRICT` miatt az érintett törzsadat nem törölhető addig, amíg jelentkezés hivatkozik rá. Ez tudatos példaszabály; más megőrzési igény más eljárást kívánhat.

Adattípusnál a jelentést kövesd: dátumhoz `DATE`, rögzített pontosságú pénzhez például `DECIMAL`, telefonszámhoz általában szöveg kell. A telefonszám nem számolási mennyiség, és kezdődhet `+` vagy `0` karakterrel. A szövegek karakterkészlete és összehasonlítási szabálya, a collation is számít.

A sémát verziózott migrációval változtasd. Új kötelező oszlopnál a meglévő sorok értékét is rendezni kell. A sikeres `CREATE TABLE` mellé próbáld ki a megengedett beszúrást, az ismételt kulcs és hibás hivatkozás elutasítását, valamint a szükséges lekérdezést.

## Vizsgán jól használható megfogalmazás

> Az adatmodellek adatbázisba történő megvalósítása során a fogalmi vagy logikai modell elemeit konkrét  
> adatbázis-struktúrává alakítjuk.  
> Az entitásokból táblák, az attribútumokból oszlopok, a kapcsolatokból pedig elsődleges és idegen kulcsok, illetve  
> szükség esetén kapcsolótáblák lesznek.  
> Emellett ekkor kerülnek meghatározásra az adattípusok, integritási szabályok és más technikai részletek is.

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

### A bővítés ellenőrzött forrásai

- [MySQL: CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html): séma, adattípusok és megszorítások
- [MySQL: FOREIGN KEY constraints](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html): InnoDB idegen kulcsok és RESTRICT

Ellenőrizve: `2026-10-14`.
