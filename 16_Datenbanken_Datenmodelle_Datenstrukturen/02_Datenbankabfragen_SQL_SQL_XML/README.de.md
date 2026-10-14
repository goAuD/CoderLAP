# Datenbankabfragen: SQL / SQL-XML

## Schneller visueller Überblick

| Begriff | Wozu? |
|---|---|
| `SELECT` | Daten abfragen |
| `INSERT` | neue Daten einfügen |
| `UPDATE` | bestehende Daten ändern |
| `DELETE` | Daten löschen |
| `SQL/XML` | XML-Daten in SQL-Umgebung verwalten und umwandeln |

## Was ist `SQL`?

`SQL` (`Structured Query Language`) ist die bekannteste Sprache für relationale Datenbanken.

Sie kann verwendet werden für:

- Erstellung von Tabellen
- Abfrage von Daten
- Änderung von Daten
- Verwaltung von Berechtigungen und Struktur

## Was ist eine Abfrage?

Unter einer Abfrage versteht man in der Prüfung meistens:

- welche Daten benötigt werden
- unter welcher Bedingung
- in welcher Sortierung oder Gruppierung

Die bekannteste Abfrageanweisung:

- `SELECT`

## Grundoperationen kurz erklärt

### `SELECT`

Daten auslesen.

### `INSERT`

Neuen Datensatz einfügen.

### `UPDATE`

Bestehende Daten ändern.

### `DELETE`

Zeilen löschen.

## Was ist `SQL/XML`?

`SQL/XML` verbindet die Welt der relationalen Datenbank mit der `XML`-Welt.

Es kann helfen bei:

- Speicherung von XML-Daten
- Datenextraktion aus XML
- tabellarischer Verarbeitung von XML-Strukturen
- Umwandlung von SQL-Ergebnissen in XML-Format

Das ist vor allem bei Systemen wichtig, die Daten zwischen verschiedenen Systemen austauschen.

## `SQL` und `SQL/XML` - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| `SQL` | allgemeine relationale Datenbanksprache |
| `SQL/XML` | Einbindung der XML-Verarbeitung in SQL-Umgebung |

## Worauf muss man achten?

- nicht jede Datenbank unterstützt die XML-Funktionen gleich
- `SQL/XML` ist ein spezielleres Thema als das grundlegende `SELECT`
- bei der Prüfung ist das Grundprinzip wichtiger als eine herstellerspezifische Funktionsliste

## Durchgearbeitetes SQL-Beispiel: Bestellübersicht

Das Beispiel verwendet **MySQL 8.0.16+ / InnoDB**. Führe es einmal in einer leeren Übungsdatenbank aus. Ergebnisspalten: Name, Anzahl der Bestellungen, Summe. Die Tabellen enthalten ausschließlich Beispieldaten.

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

`JOIN ... ON` verknüpft Zeilen, `WHERE` würde Zeilen vor der Gruppierung filtern, `GROUP BY` bildet Gruppen und `HAVING` filtert aggregierte Gruppen. `ORDER BY` legt eine verlässliche Reihenfolge fest; ohne diese Klausel ist die Reihenfolge nicht garantiert.

Der `LEFT JOIN` erhält zunächst auch Grace ohne Bestellung. Erst `HAVING` entfernt diese Gruppe. Ohne die `HAVING`-Zeile erhält Grace die Werte `0` und `0.00`. `COUNT(o.id)` zählt nicht-NULL-Bestellkennungen, `COUNT(*)` würde dagegen auch die durch den Join entstandene Zeile zählen. `COALESCE` ersetzt die fehlende Summe durch die Zahl null.

`NULL` steht für einen unbekannten oder fehlenden Wert, nicht für leeren Text oder die Zahl null. Geprüft wird mit `IS NULL`, nicht mit `= NULL`.

SQL/XML ist der XML-bezogene Teil des Standards. Beispielsweise kann PostgreSQL mit `XMLTABLE` aus XML-Elementen Zeilen bilden. Das obige MySQL-Beispiel verwendet normales relationales SQL. XML-Funktionen eines anderen Herstellers sind nicht automatisch übertragbar.

## Prüfungstaugliche Formulierung

> Für Datenbankabfragen verwendet man in relationalen Systemen üblicherweise `SQL`.  
> Mit `SQL` können Daten abgefragt, eingefügt, geändert und gelöscht werden.  
> `SQL/XML` dient hingegen der Verbindung von `XML`-Daten und SQL-basierter Datenverarbeitung, zum Beispiel zum Auslesen
> von XML-Daten oder zur Umwandlung von SQL-Ergebnissen ins XML-Format.

## Schnelle Selbstkontrolle

1. Was ist `SQL`?
2. Wozu dient `SELECT`?
3. Wozu dient `INSERT`?
4. Was ist `SQL/XML`?
5. Was ist der Hauptunterschied zwischen `SQL` und `SQL/XML`?

## Kurzantworten zur Selbstkontrolle

1. Abfrage- und Verwaltungssprache für relationale Datenbanken
2. Zum Abfragen von Daten
3. Zum Einfügen neuer Daten
4. Verbindung von SQL und XML
5. Das eine ist eine allgemeine Datenbanksprache, das andere ein um XML-Verarbeitung erweiterter Ansatz

## Quellen

1. PostgreSQL - SQL Commands  
   https://www.postgresql.org/docs/current/sql-commands.html  
   Verwendung: moderne, offizielle Quelle zu den grundlegenden SQL-Befehlen.

2. PostgreSQL - XML Functions  
   https://www.postgresql.org/docs/12/functions-xml.html  
   Verwendung: offizielle Quelle dazu, wie SQL und XML in der Praxis verbunden werden können.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [MySQL: SELECT](https://dev.mysql.com/doc/refman/8.0/en/select.html): JOIN, Gruppierung und Ergebnisreihenfolge
- [PostgreSQL: XML Functions](https://www.postgresql.org/docs/current/functions-xml.html): konkrete Unterstützung für SQL/XML und XMLTABLE

Geprüft: `2026-10-14`.
