# Datenbankabfragen: SQL / SQL-XML

## Gyors vizuális kép

| Fogalom | Mire jó? |
|---|---|
| `SELECT` | adatok lekérdezése |
| `INSERT` | új adatok beszúrása |
| `UPDATE` | meglévő adatok módosítása |
| `DELETE` | adatok törlése |
| `SQL/XML` | XML adatok kezelése és átalakítása SQL környezetben |

## Mi az a `SQL`?

A `SQL` (`Structured Query Language`) a relációs adatbázisok legismertebb nyelve.

Használható:

- táblák létrehozására
- adatok lekérdezésére
- adatok módosítására
- jogosultságok és szerkezet kezelésére is

## Mi az a lekérdezés?

Lekérdezés alatt vizsgán legtöbbször azt értjük, hogy:

- milyen adatokra van szükségünk
- milyen feltétellel
- milyen rendezésben vagy csoportosításban

A legismertebb lekérdező utasítás:

- `SELECT`

## Alapműveletek röviden

### `SELECT`

Adatok kiolvasása.

### `INSERT`

Új rekord beszúrása.

### `UPDATE`

Meglévő adatok módosítása.

### `DELETE`

Sorok törlése.

## Mi az a `SQL/XML`?

Az `SQL/XML` a relációs adatbázis és az `XML` világát kapcsolja össze.

Segíthet:

- XML adatok tárolásában
- XML-ből történő adatkinyerésben
- XML struktúrák táblás feldolgozásában
- SQL eredmények XML-formára alakításában

Ez főleg olyan rendszereknél fontos, ahol eltérő rendszerek adatot cserélnek egymással.

## `SQL` és `SQL/XML`: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| `SQL` | általános relációs adatbázis-nyelv |
| `SQL/XML` | XML kezelésének bekapcsolása SQL környezetbe |

## Mire kell figyelni?

- nem minden adatbázis támogatja ugyanúgy az XML-funkciókat
- a `SQL/XML` már speciálisabb téma, mint az alap `SELECT`
- vizsgán az alapelv fontosabb, mint egy konkrét vendor-specifikus függvénylista

## Kidolgozott SQL-példa: rendelési összesítő

A példa **MySQL 8.0.16+ / InnoDB** nyelvjáráshoz készült. Üres gyakorló adatbázisban, egyszer futtasd. A lekérdezés eredményoszlopai: név, rendelések száma, összeg. A táblák itt csak a példa adatait tartalmazzák.

<!-- example:mysql -->
```sql
CREATE TABLE customers (
  id INT PRIMARY KEY,
  name VARCHAR(40) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  amount DECIMAL(8,2) NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES customers(id)
) ENGINE=InnoDB;
INSERT INTO customers VALUES (1, 'Ada'), (2, 'Linus'), (3, 'Grace');
INSERT INTO orders VALUES (10, 1, 10.00), (11, 1, 18.00), (12, 2, 5.00);

SELECT c.name, COUNT(o.id) AS order_count,
       COALESCE(SUM(o.amount), 0) AS total
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.id
GROUP BY c.id, c.name
HAVING COALESCE(SUM(o.amount), 0) >= 10
ORDER BY total DESC, c.id;
```

```text
Ada 2 28.00
```

A `JOIN ... ON` kapcsolja össze a sorokat, a `WHERE` a csoportosítás előtti sorokat szűrné, a `GROUP BY` csoportokat képez, a `HAVING` pedig az összesített csoportokra szűr. Az `ORDER BY` ad kiszámítható sorrendet; anélkül nem garantált a találatok sorrendje.

A `LEFT JOIN` a rendelés nélküli Grace sorát is megőrzi, de a `HAVING` feltétel végül kiszűri. Ha elhagyod a `HAVING` sort, Grace értékei `0` és `0.00` lesznek. A `COUNT(o.id)` a nem NULL rendelésazonosítókat számolja, míg a `COUNT(*)` a kapcsolásban létrejött sort is számolná. A `COALESCE` a hiányzó összeget alakítja `NULL`-ról számszerű nullára.

A `NULL` ismeretlen vagy hiányzó érték, nem üres szöveg és nem nulla. Vizsgálata `IS NULL`, nem `= NULL`.

Az SQL/XML a szabvány XML-kezelési része; például PostgreSQL-ben az `XMLTABLE` XML-elemekből képezhet sorokat. A fenti MySQL-példa normál relációs SQL. Más gyártó XML-függvényeinek nevét nem lehet automatikusan átvinni rá.

## Vizsgán jól használható megfogalmazás

> Az adatbázis-lekérdezésekhez a relációs rendszerekben általában `SQL`-t használunk.  
> A `SQL` segítségével adatokat kérdezhetünk le, szúrhatunk be, módosíthatunk és törölhetünk.  
> A `SQL/XML` ezzel szemben az `XML` adatok és az SQL-alapú adatkezelés összekapcsolására szolgál, például XML adatok
> kiolvasására vagy SQL eredmények XML-formába alakítására.

## Gyors önellenőrzés

1. Mi az a `SQL`?
2. Mire való a `SELECT`?
3. Mire való az `INSERT`?
4. Mi az a `SQL/XML`?
5. Mi a fő különbség `SQL` és `SQL/XML` között?

## Rövid válaszok az önellenőrzéshez

1. Relációs adatbázisok lekérdező- és kezelőnyelve
2. Adatok lekérdezésére
3. Új adatok beszúrására
4. SQL és XML összekapcsolása
5. Az egyik általános adatbázisnyelv, a másik XML-kezeléssel bővített szemlélet

## Források

1. PostgreSQL - SQL Commands  
   https://www.postgresql.org/docs/current/sql-commands.html  
   Használat: modern, hivatalos forrás az alapvető SQL-parancsokhoz.

2. PostgreSQL - XML Functions  
   https://www.postgresql.org/docs/12/functions-xml.html  
   Használat: hivatalos forrás arra, hogyan kapcsolható össze az SQL és az XML a gyakorlatban.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [MySQL: SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html): JOIN, csoportosítás és eredménysorrend
- [PostgreSQL: XML Functions](https://www.postgresql.org/docs/current/functions-xml.html): az SQL/XML és XMLTABLE konkrét támogatása

Ellenőrizve: `2026-10-14`.
