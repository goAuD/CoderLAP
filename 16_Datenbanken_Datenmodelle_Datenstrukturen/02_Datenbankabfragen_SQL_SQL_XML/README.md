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

## Vizsgán jól használható megfogalmazás

> Az adatbázis-lekérdezésekhez a relációs rendszerekben általában `SQL`-t használunk.  
> A `SQL` segítségével adatokat kérdezhetünk le, szúrhatunk be, módosíthatunk és törölhetünk.  
> A `SQL/XML` ezzel szemben az `XML` adatok és az SQL-alapú adatkezelés összekapcsolására szolgál, például XML adatok kiolvasására vagy SQL eredmények XML-formába alakítására.

## Gyakori vizsgahibák

- Azt gondolni, hogy a lekérdezés csak `SELECT` lehet.
- A `SQL/XML`-t egyszerűen `XML`-nek nevezni.
- Nem megemlíteni, hogy az SQL írni és módosítani is tud.
- Vendor-specifikus részletekbe elveszni az alapfogalom helyett.

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
