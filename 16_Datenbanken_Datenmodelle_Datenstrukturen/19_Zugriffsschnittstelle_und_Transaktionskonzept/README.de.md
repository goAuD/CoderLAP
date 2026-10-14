# Zugriffsschnittstelle und Transaktionskonzept

## Schneller visueller Überblick

```text
Anwendung
    -> Zugriffsschnittstelle / Treiber / API
    -> DBMS
    -> Datenbank

Transaktion:
    BEGIN
      Operation 1
      Operation 2
    COMMIT oder ROLLBACK
```

## Was ist eine Zugriffsschnittstelle?

Das ist die technische Schicht, über die eine Anwendung mit der Datenbank kommuniziert.

Typische Beispiele:

- `JDBC`
- `ODBC`
- `ADO.NET`
- ORM oder Datenzugriffsschichten

Ihre Aufgaben:

- Verbindung herstellen
- SQL-Befehle senden
- Ergebnisse empfangen
- Fehler behandeln

## Was ist eine Transaktion?

Eine Transaktion ist eine Einheit aus einer oder mehreren Datenbankoperationen, die:

- gemeinsam ausgeführt wird
- oder gemeinsam fehlschlägt

Beispiel:

- Bestellung erfassen
- Lagerbestand verringern

Wenn das eine gelingt und das andere nicht, könnte das System in einen fehlerhaften Zustand geraten - deshalb braucht
man eine Transaktion.

## Grundbegriffe

| Begriff | Bedeutung |
|---|---|
| `BEGIN` | Transaktion starten |
| `COMMIT` | Änderungen festschreiben |
| `ROLLBACK` | Änderungen zurücknehmen |

## Warum ist das Transaktionskonzept wichtig?

- bewahrt die Konsistenz
- reduziert die Gefahr teilweise ausgeführter Operationen
- ist die Grundlage zuverlässiger Geschäftsprozesse

## Schnittstelle und Transaktion - nicht verwechseln

| Begriff | Rolle |
|---|---|
| Zugriffsschnittstelle | technische Verbindung zwischen Anwendung und DB |
| Transaktion | logische Operationseinheit in der Datenverarbeitung |

## ACID in der Praxis

| Prinzip | Bedeutung bei einer Umbuchung zwischen zwei Konten |
|---|---|
| Atomicity, Atomarität | Belastung und Gutschrift werden gemeinsam bestätigt oder zurückgenommen |
| Consistency, Konsistenz | festgelegte Regeln, etwa nicht negativer Bestand, bleiben eingehalten |
| Isolation | die gewählte Isolationsstufe regelt Wechselwirkungen paralleler Transaktionen |
| Durability, Dauerhaftigkeit | erfolgreich bestätigte Änderungen überstehen Systemfehler entsprechend den Dauerhaftigkeitseinstellungen |

Das DBMS erfindet keine Geschäftsregeln. Sie müssen durch Constraints und korrekte Anwendungslogik festgelegt werden. Dauerhaftigkeit schützt nicht vor jedem Datenträgerschaden oder versehentlicher Löschung; Backups bleiben nötig. Eine Transaktion kann auch aus einer einzigen Anweisung bestehen. Ein ORM ist eine höher liegende Abbildungsschicht, während der Treiber mit der Datenbank kommuniziert.

## Durchgearbeitetes Beispiel: parametrisierte Umbuchung

**PHP 8 + PDO-MySQL-Treiber, MySQL 8.0.16+ / InnoDB.** `$pdo` ist eine bereits hergestellte Verbindung zu einer leeren Übungsdatenbank. Verbindungsdaten stammen aus vertrauenswürdiger Konfiguration, nicht aus dem Browser. Führe das Beispiel einmal aus; es verwendet ausschließlich die beiden angelegten Testkonten.

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

Parameterwerte werden getrennt übergeben und dadurch nicht zu SQL-Code. Parameter binden Werte, keine beliebigen Tabellen- oder Spaltennamen. Im Beispiel ist der Betrag eine feste positive Dezimalzeichenfolge. Bei externen Eingaben müssen vorher Format, Bereich und Berechtigung geprüft werden. Statt Gleitkommarechnung für Geld verwendet die Übung DECIMAL und einen Betrag als Zeichenfolge.

Die Bedingung des ersten `UPDATE` prüft Deckung und belastet die Zeile in einem Schritt. Wurde nicht genau eine Zeile geändert, folgt keine Gutschrift. Fehlt das Zielkonto oder tritt ein anderer Fehler auf, wird auch die bereits erfolgte Belastung zurückgenommen. Die Gesamtsumme bleibt 150.00. Eine externe Zahlung oder versandte E-Mail wird dadurch noch nicht Teil der Datenbanktransaktion.

Ohne explizite Transaktion würden die beiden Anweisungen bei Autocommit getrennt bestätigt. Fehlerbehandlung ist wichtig: Eine fehlerhafte MySQL-Anweisung rollt nicht in jedem Fall automatisch die gesamte Transaktion zurück. Bei Deadlocks muss die Anwendung außerdem auf begrenzte erneute Versuche vorbereitet sein.

## Prüfungstaugliche Formulierung

> Die Zugriffsschnittstelle stellt sicher, dass eine Anwendung sich mit der Datenbank verbinden, SQL-Befehle senden  
> und Ergebnisse zurückerhalten kann.  
> Das Transaktionskonzept bedeutet, dass zusammengehörige Datenbankoperationen als Einheit behandelt werden, die  
> entweder vollständig ausgeführt oder im Fehlerfall zurückgerollt werden können.  
> Das ist die Grundlage einer zuverlässigen und konsistenten Datenverarbeitung.

## Schnelle Selbstkontrolle

1. Was ist eine Zugriffsschnittstelle?
2. Was ist eine Transaktion?
3. Wozu dient `COMMIT`?
4. Wozu dient `ROLLBACK`?
5. Warum ist es wichtig, mehrere Operationen als Einheit zu behandeln?

## Kurzantworten zur Selbstkontrolle

1. Verbindungsschicht zwischen Anwendung und Datenbank
2. Einheit zusammengehörender Datenbankoperationen
3. Zum Festschreiben der Änderungen
4. Zum Zurücknehmen der noch nicht bestätigten Änderungen einer Transaktion
5. Weil so die Daten konsistent bleiben

## Quellen

1. Oracle - JDBC Basics  
   https://docs.oracle.com/javase/tutorial/jdbc/basics/index.html  
   Verwendung: offizielle Quelle zur Funktionsweise einer typischen Datenbankzugriffsschnittstelle.

2. Microsoft Learn - Local Transactions  
   https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/local-transactions  
   Verwendung: offizielle, gut verständliche Quelle zur programmatischen Behandlung von Transaktionen.

3. PostgreSQL - Transactions  
   https://www.postgresql.org/docs/current/tutorial-transactions.html  
   Verwendung: offizieller Hintergrund zur Grundlogik von `BEGIN`, `COMMIT`, `ROLLBACK`.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [PHP: Prepared Statements](https://www.php.net/manual/en/pdo.prepared-statements.php): getrennte Parameterwerte und PDO-Verwendung
- [MySQL: COMMIT and ROLLBACK](https://dev.mysql.com/doc/refman/8.0/en/commit.html): Autocommit und explizite Transaktion
- [MySQL: InnoDB error handling](https://dev.mysql.com/doc/refman/8.0/en/innodb-error-handling.html): Fehler auf Anweisungs- und Transaktionsebene

Geprüft: `2026-10-14`.
