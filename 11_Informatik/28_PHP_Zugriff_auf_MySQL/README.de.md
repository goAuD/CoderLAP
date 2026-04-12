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

## Prüfungstaugliche Formulierung

> Mit PHP und MySQL-Zugriff können serverseitig Daten in einer Datenbank abgefragt, geändert und gespeichert werden.
> Dabei stellt PHP eine Verbindung zum MySQL-Server her, führt SQL-Abfragen aus und verarbeitet die Ergebnisse.
> Die Grundlage für eine sichere Lösung ist die Verwendung von Prepared Statements und parametrisierten Abfragen.

## Häufige Prüfungsfehler

- PHP und SQL gleichsetzen.
- Die Rolle des Prepared Statements nicht erwähnen.
- MySQL als Programmiersprache bezeichnen.
- Die Schritte Verbindung, Abfrage und Ergebnisverarbeitung nicht trennen.

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
