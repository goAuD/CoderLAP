# PHP Zugriff auf MySQL

## Lényeg 30 másodpercben

A **PHP hozzáférés MySQL-hez** azt jelenti, hogy a PHP-kód adatbázis-kapcsolatot nyit, SQL-lekérdezéseket futtat, és az eredményt feldolgozza.

Röviden:

- kapcsolat létrehozása
- lekérdezés futtatása
- eredmény feldolgozása
- hibakezelés
- biztonságos paraméterezés

## Gyors vizuális kép

| Lépés | Mit csinálunk? |
|---|---|
| 1. kapcsolat | PHP csatlakozik a MySQL szerverhez |
| 2. kérés | SQL utasítás küldése |
| 3. válasz | eredményhalmaz vagy státusz érkezik |
| 4. feldolgozás | adatok megjelenítése vagy további használata |

## Mivel lehet csatlakozni?

A PHP-ben tipikusan két ismert irány van:

- `mysqli`
- `PDO`

### `mysqli`

- kifejezetten MySQL/MariaDB környezethez
- objektumorientált és procedurális módon is használható

### `PDO`

- általánosabb adatbázis-hozzáférési réteg
- többféle adatbázis-kezelőhöz is használható

## Mi történik a gyakorlatban?

Tipikus folyamat:

1. kapcsolódás az adatbázishoz
2. SQL utasítás elküldése
3. eredmények beolvasása
4. kapcsolat kezelése

Példafeladatok:

- felhasználó lekérése
- terméklista megjelenítése
- új rekord beszúrása
- rekord frissítése vagy törlése

## Miért kell figyelni a biztonságra?

Mert ha a felhasználói adatot rosszul építjük be az SQL-be, akkor:

- `SQL injection` sérülékenység keletkezhet

Ezért fontos:

- prepared statement használata
- paraméterezett lekérdezések
- bemenetellenőrzés

## PHP + MySQL: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| PHP | szerveroldali programozási nyelv |
| MySQL | relációs adatbázis-kezelő |
| SQL | lekérdezőnyelv |

## Mire kell figyelni?

- Ne építsd össze a lekérdezést nyers felhasználói bemenettel.
- A hibakezelést ne rejtsd el teljesen fejlesztés közben.
- Az adatbázis-hozzáférés legyen rendezett, ne szétszórt.
- Különösen fontos a jogosultságok és a kapcsolati adatok védelme.

## Vizsgán jól használható megfogalmazás

> A PHP MySQL-hozzáféréssel szerveroldalon tud adatokat lekérni, módosítani és tárolni egy adatbázisban.  
> Ehhez a PHP kapcsolatot létesít a MySQL szerverrel, SQL-lekérdezéseket futtat, majd feldolgozza az eredményeket.  
> A biztonságos megoldás alapja a prepared statement és a paraméterezett lekérdezés használata.

## Gyakori vizsgahibák

- A PHP-t és az SQL-t ugyanannak tekinteni.
- Nem megemlíteni a prepared statement szerepét.
- A MySQL-t programozási nyelvnek nevezni.
- Nem elkülöníteni a kapcsolat, lekérdezés és eredmény feldolgozás lépéseit.

## Gyors önellenőrzés

1. Mi a PHP szerepe a MySQL-hozzáférésben?
2. Mi az a prepared statement?
3. Miért fontos a paraméterezett lekérdezés?
4. Mi a különbség a PHP és a MySQL között?
5. Melyik két fő PHP-s megoldást szokás említeni?

## Rövid válaszok az önellenőrzéshez

1. A kapcsolat és lekérdezések kezelését végzi
2. Előkészített, biztonságosabb lekérdezés
3. Az SQL injection ellen
4. A PHP nyelv, a MySQL adatbázis-kezelő
5. `mysqli` és `PDO`

## Források

1. PHP Manual - MySQLi Quickstart  
   https://www.php.net/manual/en/mysqli.quickstart.php  
   Használat: a MySQLi alapműködésének hivatalos összefoglalója.

2. PHP Manual - Prepared Statements  
   https://www.php.net/manual/en/mysqli.quickstart.prepared-statements.php  
   Használat: a biztonságos, paraméterezett lekérdezések szerepe.

3. PHP Manual - PDO  
   https://www.php.net/manual/en/book.pdo.php  
   Használat: általánosabb PHP-adatbázis hozzáférési megközelítés.

Megnyitva: `2026-04-08`
