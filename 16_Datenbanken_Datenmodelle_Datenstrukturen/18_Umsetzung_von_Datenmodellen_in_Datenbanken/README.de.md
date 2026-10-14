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

## Durchgearbeitetes Schema: das Anmeldemodell umsetzen

**MySQL 8.0 / InnoDB.** Verwende eine leere Übungsdatenbank mit UTF-8 (`utf8mb4`). Nach dem vorherigen Modell darf eine Person je Kurs einmal angemeldet sein.

<!-- example:mysql -->
```sql
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(80) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE courses (
  id INT PRIMARY KEY,
  title VARCHAR(80) NOT NULL
) ENGINE=InnoDB;
CREATE TABLE enrollments (
  student_id INT NOT NULL,
  course_id INT NOT NULL,
  enrolled_on DATE NOT NULL,
  PRIMARY KEY (student_id, course_id),
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE RESTRICT,
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE RESTRICT
) ENGINE=InnoDB;
INSERT INTO students VALUES (1, 'Anna');
INSERT INTO courses VALUES (10, 'SQL'), (20, 'JavaScript');
INSERT INTO enrollments VALUES
  (1, 10, '2026-01-10'), (1, 20, '2026-01-11');
SELECT s.name, c.title, e.enrolled_on
FROM enrollments AS e
JOIN students AS s ON s.id = e.student_id
JOIN courses AS c ON c.id = e.course_id
ORDER BY c.id;
```

```text
Anna SQL 2026-01-10
Anna JavaScript 2026-01-11
```

Der zusammengesetzte Primärschlüssel verhindert doppelte Anmeldungen. Die Fremdschlüssel verhindern Verweise auf nicht vorhandene Personen oder Kurse. `RESTRICT` verhindert das Löschen betroffener Stammdaten, solange Anmeldungen darauf verweisen. Das ist eine bewusste Beispielregel; andere Aufbewahrungsanforderungen können ein anderes Verfahren verlangen.

Datentypen folgen der Bedeutung: `DATE` für ein Datum, beispielsweise `DECIMAL` für Geld mit fester Genauigkeit und normalerweise Text für Telefonnummern. Eine Telefonnummer ist keine Rechengröße und kann mit `+` oder `0` beginnen. Auch Zeichensatz und Vergleichsregeln, die Collation, sind wichtig.

Ändere das Schema mit versionierten Migrationen. Bei einer neuen Pflichtspalte müssen auch vorhandene Zeilen passende Werte erhalten. Prüfe neben erfolgreichem `CREATE TABLE` gültiges Einfügen, Ablehnung doppelter Schlüssel und ungültiger Verweise sowie die benötigte Abfrage.

## Prüfungstaugliche Formulierung

> Bei der Umsetzung von Datenmodellen in Datenbanken werden die Elemente des konzeptionellen oder logischen Modells in  
> konkrete Datenbankstrukturen überführt.  
> Aus Entitäten werden Tabellen, aus Attributen Spalten, aus Beziehungen Primär- und Fremdschlüssel sowie bei Bedarf  
> Verknüpfungstabellen.  
> Dabei werden auch die Datentypen, Integritätsregeln und weitere technische Details festgelegt.

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

### Geprüfte Quellen zur Ergänzung

- [MySQL: CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html): Schema, Datentypen und Constraints
- [MySQL: FOREIGN KEY constraints](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html): InnoDB-Fremdschlüssel und RESTRICT

Geprüft: `2026-10-14`.
