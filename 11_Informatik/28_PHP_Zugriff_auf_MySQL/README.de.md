# PHP Zugriff auf MySQL

## Schneller visueller Überblick

| Schritt | Was tun wir? |
|---|---|
| 1. Verbindung | PHP verbindet sich mit dem MySQL-Server |
| 2. Anfrage | SQL-Anweisung wird gesendet |
| 3. Antwort | Ergebnismenge oder Status kommt zurück |
| 4. Verarbeitung | Daten werden angezeigt oder weiterverwendet |

## Womit kann man sich verbinden?

In PHP gibt es typischerweise zwei bekannte Richtungen:

- `mysqli`
- `PDO`

### `mysqli`

- speziell für MySQL/MariaDB-Umgebung
- kann objektorientiert und prozedural verwendet werden

### `PDO`

- allgemeinere Datenbankzugriffsschicht
- kann auch für verschiedene Datenbanksysteme verwendet werden

## Was passiert in der Praxis?

Typischer Ablauf:

1. Verbindung zur Datenbank herstellen
2. SQL-Anweisung senden
3. Ergebnisse einlesen
4. Verbindung verwalten

Beispielaufgaben:

- Benutzer abfragen
- Produktliste anzeigen
- neuen Datensatz einfügen
- Datensatz aktualisieren oder löschen

## Warum muss man auf die Sicherheit achten?

Weil wenn man Benutzerdaten falsch in die SQL-Abfrage einbaut:

- eine `SQL injection`-Schwachstelle entstehen kann

Daher ist wichtig:

- Prepared Statements verwenden
- parametrisierte Abfragen
- Eingabevalidierung

## PHP + MySQL: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| PHP | serverseitige Programmiersprache |
| MySQL | relationales Datenbankmanagementsystem |
| SQL | Abfragesprache |

## Worauf muss man achten?

- Die Abfrage nicht mit rohen Benutzereingaben zusammenbauen.
- Die Fehlerbehandlung nicht während der Entwicklung komplett verbergen.
- Der Datenbankzugriff sollte geordnet sein, nicht verstreut.
- Besonders wichtig ist der Schutz von Berechtigungen und Verbindungsdaten.

## Parametrisierte Abfrage und sichere HTML-Ausgabe

**Umgebung:** PHP 8.x auf einem Webserver, aktiviertes `pdo_mysql`, erreichbares
MySQL und die Tabelle `learning.courses(id, title)`. Die Kurstitel sind in diesem
Beispiel öffentlich. `APP_DB_USER` und `APP_DB_PASSWORD` stammen aus der
Serverkonfiguration; echte Passwörter stehen nicht im Code. In Produktion
bleibt die Anzeige detaillierter PHP-Fehler deaktiviert. Das Beispiel läuft
nicht eigenständig ohne Datenbank.

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

Hat Datensatz `15` den Titel `Schleifen`, liefert `?id=15` das HTML
`<h1>Schleifen</h1>`. `?id=0` oder eine fehlende ID ergibt `400`, eine unbekannte
positive ID `404`. Verbindungs-/Abfragefehler führen zu einer allgemeinen
`503`-Meldung, ohne Verbindungsdaten anzuzeigen.

An `:id` wird ein **Wert** gebunden, kein SQL-Codefragment. Tabellenname oder
`ORDER BY`-Spalte lassen sich so nicht parametrisieren. Solche Auswahlwerte
werden aus einer festen Liste erlaubter Namen abgeleitet. Eingabeprüfung,
SQL-Parameter und `htmlspecialchars` erfüllen verschiedene Aufgaben:
fachliches Format, SQL-Struktur und HTML-Ausgabe schützen. Sie ersetzen
einander nicht.

Zusammengehörige Schreiboperationen benötigen eine Transaktion mit Rollback
bei entsprechenden Fehlern. PDO bietet eine gemeinsame API, vereinheitlicht
aber nicht die SQL-Dialekte verschiedener Datenbanken.

## Prüfungstaugliche Formulierung

> Mit PHP und MySQL-Zugriff können serverseitig Daten in einer Datenbank abgefragt, geändert und gespeichert werden.
> Dabei stellt PHP eine Verbindung zum MySQL-Server her, führt SQL-Abfragen aus und verarbeitet die Ergebnisse.
> Die Grundlage für eine sichere Lösung ist die Verwendung von Prepared Statements und parametrisierten Abfragen.

## Schnelle Selbstkontrolle

1. Was ist die Rolle von PHP beim MySQL-Zugriff?
2. Was ist ein Prepared Statement?
3. Warum ist die parametrisierte Abfrage wichtig?
4. Was ist der Unterschied zwischen PHP und MySQL?
5. Welche zwei Haupt-PHP-Lösungen werden üblicherweise genannt?

## Kurzantworten zur Selbstkontrolle

1. Es verwaltet die Verbindung und die Abfragen
2. Eine vorbereitete, sicherere Abfrage
3. Gegen SQL Injection
4. PHP ist eine Sprache, MySQL ein Datenbankmanagementsystem
5. `mysqli` und `PDO`

## Quellen

Geprüft: `2026-10-14`.

- [PHP: PDO prepare](https://www.php.net/manual/en/pdo.prepare.php): Wertparameter und ihre Grenzen.
- [PHP: htmlspecialchars](https://www.php.net/manual/en/function.htmlspecialchars.php): Textausgabe im HTML-Kontext.


1. PHP Manual - MySQLi Quickstart
   https://www.php.net/manual/en/mysqli.quickstart.php
   Verwendung: offizielle Zusammenfassung der grundlegenden MySQLi-Arbeitsweise.

2. PHP Manual - Prepared Statements
   https://www.php.net/manual/en/mysqli.quickstart.prepared-statements.php
   Verwendung: Rolle der sicheren, parametrisierten Abfragen.

3. PHP Manual - PDO
   https://www.php.net/manual/en/book.pdo.php
   Verwendung: allgemeinerer PHP-Datenbankzugriffsansatz.

Abgerufen: `2026-04-08`
