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

## Prüfungstaugliche Formulierung

> Für Datenbankabfragen verwendet man in relationalen Systemen üblicherweise `SQL`.  
> Mit `SQL` können Daten abgefragt, eingefügt, geändert und gelöscht werden.  
> `SQL/XML` dient hingegen der Verbindung von `XML`-Daten und SQL-basierter Datenverarbeitung, zum Beispiel zum Auslesen von XML-Daten oder zur Umwandlung von SQL-Ergebnissen ins XML-Format.

## Häufige Prüfungsfehler

- Denken, dass eine Abfrage nur `SELECT` sein kann.
- `SQL/XML` einfach als `XML` bezeichnen.
- Nicht erwähnen, dass SQL auch schreiben und ändern kann.
- Sich in herstellerspezifischen Details verlieren statt den Grundbegriff zu erklären.

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
