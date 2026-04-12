# DBMS

## Schneller visueller Überblick

| `DBMS`-Aufgabe | Was bedeutet das? |
|---|---|
| Speicherung | Verwaltung der Daten im Hintergrund |
| Abfrage | Auslesen und Ändern von Daten |
| Zugriffskontrolle | wer was sehen / ändern darf |
| Integrität | Einhaltung von Regeln |
| Administration | Sicherung, Recovery, Tuning, Überwachung |

## Was ist ein `DBMS`?

Ein `DBMS` ist eine Softwareschicht zwischen dem Benutzer oder der Anwendung und den gespeicherten Daten.

Seine Aufgaben sind unter anderem:

- physische und logische Verwaltung der Daten
- Ausführung von Abfragen
- Koordination gleichzeitiger Zugriffe
- Durchsetzung von Regeln und Schlüsseln

## Warum ist das wichtig?

- man muss sich nicht direkt mit der Low-Level-Speicherung befassen
- bietet sicherere und strukturiertere Datenverwaltung
- unterstützt Mehrbenutzerbetrieb
- hilft bei der Leistungsoptimierung

## Typische Bestandteile

Auf Basis des Oracle-Datenbankkonzepts enthält ein `DBMS` typischerweise:

- Steuerungs- und Speicherverwaltungskomponenten
- ein Metadaten-Repository oder Datenwörterbuch
- Unterstützung für Abfragesprachen

## `DBMS` und Datenbank - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Datenbank | die Menge der gespeicherten Daten |
| `DBMS` | die Software, die diese verwaltet |

## Beispiele

Bekannte `DBMS`:

- `PostgreSQL`
- `MySQL`
- `Oracle Database`
- `Microsoft SQL Server`
- `SQLite`

## Prüfungstaugliche Formulierung

> Das `DBMS`, also Database Management System, ist die Software, die die Erstellung, Verwaltung, Abfrage, den Schutz und die Administration der Datenbank durchführt.  
> Das `DBMS` vermittelt zwischen Anwendungen und den gespeicherten Daten und gewährleistet unter anderem die Integrität, den Mehrbenutzerbetrieb und die Regeln der Datenverwaltung.  
> Daher ist das `DBMS` das zentrale Element des Datenbanksystems.

## Häufige Prüfungsfehler

- Das `DBMS` mit der Datenbank gleichsetzen.
- Das `DBMS` lediglich als Abfrageprogramm bezeichnen.
- Die Administrations- und Integritätsfunktionen nicht erwähnen.
- Nicht erwähnen, dass es auch den Mehrbenutzerzugriff verwaltet.

## Schnelle Selbstkontrolle

1. Was ist ein `DBMS`?
2. Welche Hauptaufgaben hat es?
3. Worin unterscheidet es sich von der Datenbank?
4. Warum ist die Verwaltung des Mehrbenutzerbetriebs wichtig?
5. Nenne drei bekannte `DBMS`.

## Kurzantworten zur Selbstkontrolle

1. Datenbankverwaltungssoftware
2. Speicherung, Abfrage, Zugriff, Integrität, Administration
3. Das eine sind die Daten, das andere ist die Verwaltungssoftware
4. Weil viele gleichzeitig mit denselben Daten arbeiten können
5. PostgreSQL, MySQL, Oracle Database

## Quellen

1. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Verwendung: offizielle Primärquelle zur Definition und den Hauptelementen des `DBMS`.

2. Oracle - What Is a Database?  
   https://www.oracle.com/database/what-is-database/  
   Verwendung: moderne, gut lesbare Zusammenfassung zur Rolle des `DBMS`.

Abgerufen: `2026-04-09`
