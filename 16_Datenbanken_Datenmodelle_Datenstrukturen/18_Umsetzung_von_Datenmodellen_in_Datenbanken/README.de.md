# Umsetzung von Datenmodellen in Datenbanken

## Schneller visueller Überblick

| Modellelement | Datenbankumsetzung |
|---|---|
| Entität | Tabelle |
| Attribut | Spalte |
| eindeutiger Identifikator | `PRIMARY KEY` |
| Beziehung | `FOREIGN KEY` |
| Regel | `NOT NULL`, `UNIQUE`, `CHECK` |

## Wie erfolgt die Umsetzung?

### 1. Entitäten -> Tabellen

Zum Beispiel:

- Aus der Entität `Customer` wird die Tabelle `customers`

### 2. Attribute -> Spalten

Zum Beispiel:

- Name
- Adresse
- E-Mail
- Datum

### 3. Schlüssel festlegen

- Primärschlüssel
- Fremdschlüssel
- bei Bedarf eindeutige Schlüssel

### 4. Beziehungen abbilden

- `1:1`
- `1:n`
- `n:m` mit Verknüpfungstabelle

### 5. Integritätsregeln angeben

- Pflichtfelder
- Eindeutigkeit
- Wertebereiche
- Beziehungsregeln

## Warum ist dieser Schritt wichtig?

Weil hier entschieden wird, ob:

- das Modell tatsächlich zu einer funktionierenden Datenbank wird
- die Regeln durchgesetzt werden können
- die Datenbank wartbar sein wird

## Logische und physische Umsetzung

| Ebene | Worauf liegt der Fokus? |
|---|---|
| logisch | Tabellen, Schlüssel, Beziehungen |
| physisch | Datentypen, Indizes, herstellerspezifische Lösungen |

## Worauf muss man achten?

- richtige Wahl der Datentypen
- korrekte Festlegung der Schlüssel
- genaue Modellierung der Beziehungen
- Vermeidung unnötiger Redundanz

## Prüfungstaugliche Formulierung

> Bei der Umsetzung von Datenmodellen in Datenbanken werden die Elemente des konzeptionellen oder logischen Modells in konkrete Datenbankstrukturen überführt.  
> Aus Entitäten werden Tabellen, aus Attributen Spalten, aus Beziehungen Primär- und Fremdschlüssel sowie bei Bedarf Verknüpfungstabellen.  
> Dabei werden auch die Datentypen, Integritätsregeln und weitere technische Details festgelegt.

## Häufige Prüfungsfehler

- Modellierung und Umsetzung als dasselbe betrachten.
- Bei der `n:m`-Beziehung keine Verknüpfungstabelle verwenden.
- Die Constraints nicht erwähnen.
- Die Rolle der Datentypen weglassen.

## Schnelle Selbstkontrolle

1. Was wird aus einer Entität?
2. Was wird aus einem Attribut?
3. Wie wird eine Beziehung umgesetzt?
4. Warum braucht man Constraints?
5. Was ist der Unterschied zwischen logischer und physischer Umsetzung?

## Kurzantworten zur Selbstkontrolle

1. Eine Tabelle
2. Eine Spalte
3. Mit Schlüsseln und bei Bedarf mit Verknüpfungstabelle
4. Damit die Daten korrekt bleiben
5. Das eine ist die allgemeine Struktur, das andere sind technische Details

## Quellen

1. Oracle SQL Developer Data Modeler  
   https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/  
   Verwendung: offizielle Quelle zu den Ebenen logischer und physischer Umsetzung von Datenmodellen.

2. PostgreSQL - Data Definition  
   https://www.postgresql.org/docs/current/ddl.html  
   Verwendung: offizielle Quelle dazu, wie Modelle in Tabellen, Schlüsseln und Constraints umgesetzt werden.

Abgerufen: `2026-04-09`
