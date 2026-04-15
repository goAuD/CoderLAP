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

## Prüfungstaugliche Formulierung

> Die grundlegenden Datenbankoperationen sind das Erstellen, Abfragen, Ändern und Löschen von Datensätzen.  
> In einer relationalen Datenbank werden diese typischerweise mit den SQL-Befehlen `INSERT`, `SELECT`, `UPDATE` und  
> `DELETE` durchgeführt.  
> Diese Operationen bilden die Grundlage für den Betrieb der meisten datenbankbasierten Anwendungen.

## Häufige Prüfungsfehler

- Abfrage mit Änderung verwechseln.
- `SELECT` als einzige wichtige Operation betrachten.
- Die Rolle von `WHERE` nicht erwähnen.
- Nicht erwähnen, dass diese Operationen auf Anwendungsebene dem `CRUD`-Konzept zugeordnet sind.

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
