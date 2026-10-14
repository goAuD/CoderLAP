# Index: Vor- und Nachteile

## Gyors vizuális kép

| Előny | Hátrány |
|---|---|
| gyorsabb keresés | extra tárhelyigény |
| jobb szűrés és rendezés | karbantartási költség |
| hatékonyabb joinok | módosítások lassulhatnak |

## Mi az index?

Az index egy olyan adatstruktúra, amely segít gyorsabban megtalálni bizonyos rekordokat anélkül, hogy a teljes táblát
végig kellene olvasni.

Hasonlat:

- mint egy könyv név- vagy tárgymutatója

## Miért jó?

Különösen hasznos:

- gyakran szűrt oszlopoknál
- kulcsmezőknél
- rendezésnél
- join műveleteknél

## Fő előnyök

- gyorsabb `SELECT` műveletek
- gyorsabb keresés feltétellel
- hatékonyabb relációs kapcsolódás
- jobb teljesítmény nagy tábláknál

## Fő hátrányok

- tárhelyet igényel
- minden írási műveletnél karban kell tartani
- túl sok index ronthatja az összteljesítményt
- rosszul megválasztott index nem hoz valódi hasznot

## Mikor érdemes indexet használni?

- ha sok a lekérdezés
- ha nagy az adatmennyiség
- ha adott oszlopon gyakran keresünk

## Mikor nem biztos, hogy jó?

- nagyon kicsi táblánál
- ritkán használt oszlopoknál
- ha túl sok módosítás történik és kevés a keresés

## Index és kulcs: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| kulcs | logikai adatmodellbeli szerep |
| index | teljesítményt javító technikai struktúra |

Gyakran kapcsolódnak egymáshoz, de nem ugyanazok.

## Kidolgozott összetett index

**MySQL 8.0 / InnoDB, üres gyakorló adatbázis.** Gyakori kérdés: egy adott ügyfél mely rendelései érkeztek egy dátumtól kezdve?

<!-- example:mysql -->
```sql
CREATE TABLE orders (
  id INT PRIMARY KEY,
  customer_id INT NOT NULL,
  ordered_on DATE NOT NULL
) ENGINE=InnoDB;
CREATE INDEX idx_customer_date ON orders(customer_id, ordered_on);
INSERT INTO orders VALUES
  (1, 7, '2026-01-10'), (2, 8, '2026-01-12'), (3, 7, '2026-01-20');
SELECT id, ordered_on FROM orders
WHERE customer_id = 7 AND ordered_on >= '2026-01-15'
ORDER BY ordered_on, id;
```

```text
3 2026-01-20
```

Az index sorrendje `(customer_id, ordered_on)`: jól illeszkedik az ügyfél egyenlőségfeltételéhez, majd a dátumtartományhoz. A csak dátumra szűrő lekérdezés nem ugyanígy használja a balról kezdődő indexrészt; a megfelelő tervet meg kell mérni. Az index létrehozása önmagában nem ír elő használati kötelezettséget az optimalizálónak.

A fenti `SELECT` elé írt `EXPLAIN` megmutatja a tervet. Nézd a lehetséges és választott indexet, a hozzáférés módját és a becsült sorszámot. Három sornál a teljes bejárás is olcsó lehet. Reális adatmennyiséggel és hasonló értékeloszlással érdemes mérni. Az `EXPLAIN ANALYZE` ténylegesen végre is hajtja a lekérdezést, ezért külön mérési művelet.

Az index többletterületet és az érintett kulcsok változásakor karbantartást igényel. Az alacsony szelektivitás, például egy majdnem minden sorban azonos állapot, önmagában nem feltétlenül ad jó szűkítést. A `LIKE 'abc%'` és a `LIKE '%abc%'` keresés indexelhetősége sem azonos.

## Vizsgán jól használható megfogalmazás

> Az index olyan adatbázis-struktúra, amely gyorsítja az adatok keresését és bizonyos lekérdezéseket.  
> Előnye a jobb lekérdezési teljesítmény, hátránya pedig a többlet tárhelyigény és az, hogy a módosító műveleteknél  
> karban kell tartani.  
> Ezért az indexek használata teljesítménynyereséget adhat, de csak megfelelő tervezéssel érdemes alkalmazni.

## Gyors önellenőrzés

1. Mi az index célja?
2. Mi az egyik fő előnye?
3. Mi az egyik fő hátránya?
4. Mikor hasznos különösen?
5. Mi a különbség kulcs és index között?

## Rövid válaszok az önellenőrzéshez

1. Gyorsabb keresés és lekérdezés
2. Jobb `SELECT` teljesítmény
3. Több tárhely és lassabb módosítások
4. Nagy táblán és gyakori szűrésnél
5. A kulcs logikai, az index technikai fogalom

## Források

1. PostgreSQL - Indexes  
   https://www.postgresql.org/docs/current/indexes.html  
   Használat: hivatalos forrás az indexek szerepéhez és működéséhez.

2. PostgreSQL - Indexes Introduction  
   https://www.postgresql.org/docs/current/indexes-intro.html  
   Használat: tömör, hivatalos bevezető az indexek előnyeihez és költségeihez.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [MySQL: Multiple-Column Indexes](https://dev.mysql.com/doc/refman/8.0/en/multiple-column-indexes.html): bal oldali indexelőtag és oszlopsorrend
- [MySQL: EXPLAIN](https://dev.mysql.com/doc/refman/8.0/en/explain.html): terv és tényleges végrehajtási mérés

Ellenőrizve: `2026-10-14`.
