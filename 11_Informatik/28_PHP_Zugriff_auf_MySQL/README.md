# PHP Zugriff auf MySQL

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

## Paraméterezett lekérés és biztonságos HTML-kimenet

**Környezet:** PHP 8.x webszerveren, engedélyezett `pdo_mysql`, elérhető MySQL,
`learning.courses(id, title)` tábla. A kurzuscímek ebben a példában nyilvánosak.
Az `APP_DB_USER` és `APP_DB_PASSWORD` környezeti változókat a szerver konfigurációja
adja, a kódba nem írunk valódi jelszót. Éles környezetben a részletes PHP-hibák
képernyőre írása legyen kikapcsolva. Ez nem adatbázis nélküli önálló példa.

```php
<?php
declare(strict_types=1);

$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT,
    ['options' => ['min_range' => 1]]);
if ($id === false || $id === null) {
    http_response_code(400);
    exit('Invalid course id');
}

$dbUser = getenv('APP_DB_USER');
$dbPassword = getenv('APP_DB_PASSWORD');
if ($dbUser === false || $dbPassword === false) {
    error_log('Course database configuration missing');
    http_response_code(503);
    exit('Course service unavailable');
}

try {
    $pdo = new PDO(
        'mysql:host=127.0.0.1;dbname=learning;charset=utf8mb4',
        $dbUser,
        $dbPassword,
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
         PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
         PDO::ATTR_EMULATE_PREPARES => false]
    );
    $statement = $pdo->prepare('SELECT title FROM courses WHERE id = :id');
    $statement->bindValue(':id', $id, PDO::PARAM_INT);
    $statement->execute();
    $course = $statement->fetch();
    if ($course === false) {
        http_response_code(404);
        exit('Course not found');
    }
    header('Content-Type: text/html; charset=utf-8');
    echo '<h1>' . htmlspecialchars($course['title'],
        ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8') . '</h1>';
} catch (PDOException $error) {
    error_log('Course database request failed');
    http_response_code(503);
    echo 'Course service unavailable';
}
```

Ha a `15` azonosítójú rekord címe `Schleifen`, az `?id=15` kérés
`<h1>Schleifen</h1>` HTML-t eredményez. `?id=0` vagy hiányzó azonosító `400`,
nem létező pozitív azonosító `404` választ ad. A kapcsolódási/lekérdezési hiba
általános `503` üzenetet kap, kapcsolati adat nem jelenik meg.

A `:id` helyére **értéket** kötünk, nem SQL-kódrészletet. Táblanevet vagy
`ORDER BY` oszlopot nem lehet így paraméterezni; ilyen választást engedélyezett
nevek rögzített listájából képzünk. A bemenetellenőrzés, az SQL-paraméterezés
és a `htmlspecialchars` három külön feladat: üzleti forma, SQL-szerkezet,
illetve HTML-megjelenítés védelme. Egyik sem helyettesíti a másikat.

Összetartozó írásokhoz tranzakció szükséges, megfelelő hibánál rollbackkel.
A PDO közös API-t ad, de ettől az adatbázisok SQL-dialektusa nem válik azonossá.

## Vizsgán jól használható megfogalmazás

> A PHP MySQL-hozzáféréssel szerveroldalon tud adatokat lekérni, módosítani és tárolni egy adatbázisban.  
> Ehhez a PHP kapcsolatot létesít a MySQL szerverrel, SQL-lekérdezéseket futtat, majd feldolgozza az eredményeket.  
> A biztonságos megoldás alapja a prepared statement és a paraméterezett lekérdezés használata.

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

Ellenőrizve: `2026-10-14`.

- [PHP: PDO prepare](https://www.php.net/manual/en/pdo.prepare.php): értékparaméterek és korlátok.
- [PHP: htmlspecialchars](https://www.php.net/manual/en/function.htmlspecialchars.php): HTML-kontextusú szövegkimenet.


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
