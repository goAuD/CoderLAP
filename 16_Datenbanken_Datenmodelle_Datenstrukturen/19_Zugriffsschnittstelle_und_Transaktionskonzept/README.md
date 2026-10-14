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

A tranzakció egy vagy több adatbázis-művelet olyan egysége, amely:

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

## ACID a gyakorlatban

| Elv | Jelentése egy két számla közti átvezetésnél |
|---|---|
| Atomicity, atomiság | a terhelés és jóváírás együtt véglegesül vagy együtt visszavonható |
| Consistency, konzisztencia | az előírt szabályok, például a nem negatív egyenleg, megmaradnak |
| Isolation, elkülönítés | a párhuzamos tranzakciók kölcsönhatását a választott izolációs szint szabályozza |
| Durability, tartósság | a sikeresen véglegesített változás a tartóssági beállítások szerinti rendszerhibát túléli |

A DBMS nem találja ki az üzleti szabályokat. Ezeket megszorításokkal és helyes alkalmazáslogikával kell megadni. A tartósság nem jelent védelmet minden lemezkár vagy véletlen törlés ellen; mentés továbbra is kell. Egy tranzakció akár egyetlen utasításból is állhat. Az ORM egy magasabb szintű leképezési réteg, a driver pedig az adatbázissal való kommunikációt végzi.

## Kidolgozott példa: paraméterezett átvezetés

**PHP 8 + PDO MySQL driver, MySQL 8.0.16+ / InnoDB.** A `$pdo` egy már létrehozott, üres gyakorló adatbázisra mutató kapcsolat. A kapcsolati adatot megbízható konfigurációból kapja, nem böngészőből. A mintát egyszer futtasd; kizárólag a két létrehozott tesztszámlával dolgozik.

<!-- example:php-pdo-mysql -->
```php
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
$pdo->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
$pdo->exec('CREATE TABLE accounts (
    id INT PRIMARY KEY,
    balance DECIMAL(10,2) NOT NULL CHECK (balance >= 0)
) ENGINE=InnoDB');
$pdo->exec('INSERT INTO accounts VALUES (1, 100.00), (2, 50.00)');

$amount = '20.00';
try {
    $pdo->beginTransaction();
    $debit = $pdo->prepare('UPDATE accounts SET balance = balance - :amount
        WHERE id = :id AND balance >= :minimum');
    $debit->execute(['amount' => $amount, 'id' => 1, 'minimum' => $amount]);
    if ($debit->rowCount() !== 1) {
        throw new RuntimeException('Debit rejected');
    }
    $credit = $pdo->prepare('UPDATE accounts SET balance = balance + :amount
        WHERE id = :id');
    $credit->execute(['amount' => $amount, 'id' => 2]);
    if ($credit->rowCount() !== 1) {
        throw new RuntimeException('Credit rejected');
    }
    $pdo->commit();
} catch (Throwable $error) {
    if ($pdo->inTransaction()) {
        $pdo->rollBack();
    }
    throw $error;
}
foreach ($pdo->query('SELECT id, balance FROM accounts ORDER BY id') as $row) {
    echo $row['id'] . ': ' . $row['balance'] . PHP_EOL;
}
```

```text
1: 80.00
2: 70.00
```

A paraméterérték külön kerül átadásra, így nem válik SQL-kóddá. Paraméterrel értéket kötünk, nem tetszőleges tábla- vagy oszlopnevet. A mintában az összeg rögzített, pozitív decimális karakterlánc; külső adatnál előbb a formátumot, tartományt és a jogosultságot is ellenőrizni kell. Lebegőpontos pénzszámolás helyett itt DECIMAL és szöveges összeg szerepel.

Az első `UPDATE` feltétele egyszerre ellenőrzi a fedezetet és terheli a sort. Ha nem pontosan egy sor változott, a jóváírás nem következik. Ha a cél nem létezik vagy más hiba lép fel, a már elvégzett terhelést is visszavonjuk. A pénzösszeg végig 150.00 marad. Külső fizetés vagy e-mail-küldés ettől még nem válik az adatbázis-tranzakció részévé.

Az explicit tranzakció nélkül a két külön utasítás autocommit mellett külön véglegesülne. A hibakezelés fontos: MySQL-ben egy hibás utasítás nem minden esetben vonja vissza automatikusan a teljes tranzakciót. Holtpontnál az alkalmazásnak korlátozott újrapróbálásra is fel kell készülni.

## Vizsgán jól használható megfogalmazás

> A hozzáférési interfész biztosítja, hogy egy alkalmazás kapcsolatba tudjon lépni az adatbázissal, SQL-parancsokat  
> küldjön és eredményeket kapjon vissza.  
> A tranzakciós koncepció pedig azt jelenti, hogy az összetartozó adatbázis-műveleteket egy egységként kezeljük,  
> amelyek vagy teljes egészében végrehajtódnak, vagy hiba esetén visszagörgethetők.  
> Ez a megbízható és konzisztens adatkezelés alapja.

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
4. A tranzakció még nem véglegesített módosításainak visszavonására
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

### A bővítés ellenőrzött forrásai

- [PHP: Prepared Statements](https://www.php.net/manual/en/pdo.prepared-statements.php): paraméterértékek elkülönítése és PDO használata
- [MySQL: COMMIT and ROLLBACK](https://dev.mysql.com/doc/refman/8.0/en/commit.html): autocommit és explicit tranzakció
- [MySQL: InnoDB error handling](https://dev.mysql.com/doc/refman/8.0/en/innodb-error-handling.html): utasítás- és tranzakciószintű hibák

Ellenőrizve: `2026-10-14`.
