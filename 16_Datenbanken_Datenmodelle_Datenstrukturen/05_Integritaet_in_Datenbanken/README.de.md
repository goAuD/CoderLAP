# Integritaet in Datenbanken

## Schneller visueller Überblick

| Integritätstyp | Beispiel |
|---|---|
| Entitätsintegrität | der Primärschlüssel darf nicht `NULL` sein |
| referentielle Integrität | ein angegebener, nicht-NULL-Fremdschlüsselwert benötigt einen existierenden referenzierten Schlüssel |
| Domänenintegrität | der Wert darf nur ein erlaubter Wert sein |

## Was bedeutet Integrität?

Integrität stellt sicher, dass die Datenbank:

- logisch konsistent bleibt
- keine fehlerhaften Beziehungen entstehen
- die Regeln bei Dateneingabe oder Änderung nicht verletzt werden

## Typische Integritätsregeln

### `NOT NULL`

Der Wert darf nicht `NULL` sein. Leerer Text (`''`) wird dadurch allein nicht verboten.

### `UNIQUE`

Die Wertekombination der angegebenen Spalten ist eindeutig; die Behandlung von `NULL` hängt vom DBMS ab.

### `PRIMARY KEY`

Identifiziert den Datensatz.

### `FOREIGN KEY`

Sichert einen Verweis auf einen passenden Schlüssel derselben oder einer anderen Tabelle ab.

### `CHECK`

Schreibt einen Wertebereich oder eine Regel vor.

## Warum ist das wichtig?

- reduziert die Wahrscheinlichkeit fehlerhafter Dateneingabe
- macht Abfragen zuverlässiger
- hilft, die Korrektheit der Beziehungen zu bewahren
- ist die Grundlage einer qualitativ hochwertigen Datenbank

## Integrität und Validierung - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| anwendungsseitige Validierung | das Programm prüft die eingegebenen Daten |
| Datenbankintegrität | die Datenbank selbst erzwingt die Regel |

Beides zusammen ist am stärksten.

## Durchgearbeitete Constraints

**MySQL 8.0.16+ / InnoDB, leere Übungsdatenbank.** In diesem Versionsbereich setzt der Server `CHECK` tatsächlich durch.

<!-- example:mysql -->
```sql
CREATE TABLE products (
  id INT PRIMARY KEY,
  sku VARCHAR(20) NOT NULL UNIQUE,
  price DECIMAL(8,2) NOT NULL CHECK (price >= 0),
  note VARCHAR(40) NULL
) ENGINE=InnoDB;
INSERT INTO products VALUES (1, 'BOOK-1', 12.50, '');
SELECT id, price, note IS NULL AS note_is_null,
       CHAR_LENGTH(note) AS note_length
FROM products ORDER BY id;
```

```text
1 12.50 0 0
```

Die leere `note` hat Länge null, ist aber nicht `NULL`. Ein Einfügen mit `price = -1` scheitert an `CHECK`, eine erneute Artikelnummer `BOOK-1` an `UNIQUE` und ein `NULL`-Preis an `NOT NULL`. `CHECK (price >= 0)` allein würde den aus `NULL` entstehenden unbekannten Wahrheitswert zulassen. Deshalb wird zusätzlich `NOT NULL` verwendet.

MySQL erlaubt in einer nullable `UNIQUE`-Spalte mehrere `NULL`-Werte. Ist ein Wert verpflichtend und eindeutig, müssen beide Anforderungen festgelegt werden. Constraints erzwingen die hinterlegten Regeln. Ob der Preis eines echten Produkts inhaltlich richtig eingegeben wurde, erkennen sie nicht selbst; dafür braucht es zusätzlich fachliche Prüfung.

## Prüfungstaugliche Formulierung

> Integrität bedeutet die Korrektheit und Konsistenz der in der Datenbank gespeicherten Daten.  
> Das `DBMS` kann dies durch verschiedene Regeln sicherstellen, zum Beispiel durch `PRIMARY KEY`, `FOREIGN KEY`, `NOT  
> NULL`, `UNIQUE` und `CHECK`-Constraints.  
> Ziel der Integrität ist es, dass die Datenbank nicht in einen fehlerhaften oder widersprüchlichen Zustand geraten kann.

## Schnelle Selbstkontrolle

1. Was bedeutet Integrität in einer Datenbank?
2. Was ist referentielle Integrität?
3. Wozu dient `CHECK`?
4. Warum ist `PRIMARY KEY` wichtig?
5. Warum ist es gut, wenn die Datenbank selbst prüft?

## Kurzantworten zur Selbstkontrolle

1. Korrektheit und Konsistenz der Daten
2. Korrekte Verknüpfung der Fremdschlüssel
3. Zur Vorgabe von Regeln oder Wertebereichen
4. Weil er den Datensatz eindeutig identifiziert
5. Weil so weniger fehlerhafte Daten eingegeben werden können

## Quellen

1. PostgreSQL - Constraints  
   https://www.postgresql.org/docs/current/ddl-constraints.html  
   Verwendung: offizielle Quelle zu Integritäts-Constraints.

2. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Verwendung: ergänzender Hintergrund zum Verständnis des relationalen Datenmodells und der Integritätsprinzipien.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [MySQL: CHECK constraints](https://dev.mysql.com/doc/refman/8.0/en/create-table-check-constraints.html): CHECK, TRUE/UNKNOWN und Versionsgrenze
- [MySQL: CREATE TABLE](https://dev.mysql.com/doc/refman/8.0/en/create-table.html): NOT NULL, UNIQUE und Schlüssel

Geprüft: `2026-10-14`.
