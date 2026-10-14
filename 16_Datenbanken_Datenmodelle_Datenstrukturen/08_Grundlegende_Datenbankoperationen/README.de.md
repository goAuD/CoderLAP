# Grundlegende Datenbankoperationen

## Schneller visueller Überblick

| Operation | Bedeutung |
|---|---|
| Create | neuen Datensatz erstellen |
| Read | Daten abfragen |
| Update | Daten ändern |
| Delete | Daten löschen |

## Warum sind diese Operationen grundlegend?

Weil fast jede Datenbankanwendung darauf aufbaut.

Zum Beispiel:

- neuen Kunden erfassen
- Bestellung abfragen
- Adresse ändern
- alten Datensatz löschen

## Die vier wichtigsten SQL-Befehle

### `SELECT`

Dient zum Auslesen von Daten.

### `INSERT`

Dient zum Einfügen einer neuen Zeile.

### `UPDATE`

Dient zum Ändern bestehender Datensätze.

### `DELETE`

Dient zum Löschen von Zeilen.

## Worauf muss man achten?

- die `WHERE`-Bedingung ist sehr wichtig
- ein fehlerhaftes `UPDATE` oder `DELETE` kann zu viele Zeilen betreffen
- Änderungsoperationen sollten häufig in einer Transaktion behandelt werden

## `CRUD` und SQL - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| `CRUD` | allgemeines Operationsmodell |
| `SQL` | konkrete sprachliche Umsetzung |

## Durchgearbeitetes CRUD-Beispiel mit Rücknahme

**MySQL 8.0 / InnoDB, leere Übungsdatenbank.** Das Beispiel legt zwei Aufgaben an, ändert und löscht innerhalb einer Transaktion und nimmt die Änderungen anschließend zurück. Das erste Ergebnis ist die eine Zeile innerhalb der Transaktion; das zweite Ergebnis sind die beiden wiederhergestellten Zeilen.

<!-- example:mysql -->
```sql
CREATE TABLE tasks (
  id INT PRIMARY KEY,
  status VARCHAR(10) NOT NULL
) ENGINE=InnoDB;
INSERT INTO tasks VALUES (1, 'draft'), (2, 'done');

START TRANSACTION;
UPDATE tasks SET status = 'done' WHERE id = 1;
DELETE FROM tasks WHERE id = 2;
SELECT id, status FROM tasks ORDER BY id;
ROLLBACK;
SELECT id, status FROM tasks ORDER BY id;
```

```text
1 done
1 draft
2 done
```

`CREATE TABLE` erstellt die Struktur und gehört zu DDL. Das „Create“ von CRUD entspricht hier `INSERT`, das einen Datensatz und keine Tabelle erzeugt. `INSERT`, `UPDATE` und `DELETE` ändern Daten; `GRANT` und `REVOKE` regeln Rechte. `SELECT` wird je nach Lehrbuch als eigene DQL-Gruppe oder als Teil der weiter gefassten DML eingeordnet.

Vor einer Änderung hilft ein `SELECT` mit derselben Bedingung, die Zielmenge zu prüfen. Kontrolliere danach die Anzahl betroffener Zeilen. Bei gleichzeitigen Benutzern schützt die separate Vorabfrage allein noch nicht vor zwischenzeitlichen Änderungen; dafür braucht es eine geeignete Transaktionsstrategie.

Im Beispiel liegen rücknehmbare Datenänderungen innerhalb der Transaktion. Mehrere strukturändernde MySQL-Anweisungen verursachen einen impliziten Commit. `CREATE TABLE` ist deshalb keine allgemeine „Probeaktion“, die man anschließend mit `ROLLBACK` zurücknimmt.

## Prüfungstaugliche Formulierung

> Die grundlegenden Datenbankoperationen sind das Erstellen, Abfragen, Ändern und Löschen von Datensätzen.  
> In einer relationalen Datenbank werden diese typischerweise mit den SQL-Befehlen `INSERT`, `SELECT`, `UPDATE` und  
> `DELETE` durchgeführt.  
> Diese Operationen bilden die Grundlage für den Betrieb der meisten datenbankbasierten Anwendungen.

## Schnelle Selbstkontrolle

1. Was bedeutet `CRUD`?
2. Wozu dient `SELECT`?
3. Wozu dient `UPDATE`?
4. Warum ist es gefährlich, ohne `WHERE` zu ändern oder zu löschen?
5. Warum werden diese als Grundoperationen bezeichnet?

## Kurzantworten zur Selbstkontrolle

1. Create, Read, Update, Delete
2. Zum Auslesen von Daten
3. Zum Ändern bestehender Daten
4. Weil es zu viele Datensätze betreffen kann
5. Weil fast jede Anwendung sie verwendet

## Quellen

1. PostgreSQL - SQL Commands  
   https://www.postgresql.org/docs/current/sql-commands.html  
   Verwendung: offizielle Quelle zu den grundlegenden SQL-Operationen.

2. PostgreSQL - Tutorial  
   https://www.postgresql.org/docs/current/tutorial-sql.html  
   Verwendung: praktische, offizielle Zusammenfassung zur Verwendung grundlegender Datenbankoperationen.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [MySQL: COMMIT and ROLLBACK](https://dev.mysql.com/doc/refman/8.0/en/commit.html): Transaktion und Rücknahme von Datenänderungen
- [MySQL: Implicit Commit](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html): DDL und impliziter Commit

Geprüft: `2026-10-14`.
