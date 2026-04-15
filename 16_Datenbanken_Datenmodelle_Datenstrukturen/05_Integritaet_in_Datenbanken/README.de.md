# Integritaet in Datenbanken

## Schneller visueller Überblick

| Integritätstyp | Beispiel |
|---|---|
| Entitätsintegrität | der Primärschlüssel darf nicht `NULL` sein |
| referentielle Integrität | ein Fremdschlüssel darf nur auf einen existierenden Datensatz verweisen |
| Domänenintegrität | der Wert darf nur ein erlaubter Wert sein |

## Was bedeutet Integrität?

Integrität stellt sicher, dass die Datenbank:

- logisch konsistent bleibt
- keine fehlerhaften Beziehungen entstehen
- die Regeln bei Dateneingabe oder Änderung nicht verletzt werden

## Typische Integritätsregeln

### `NOT NULL`

Ein Pflichtfeld darf nicht leer bleiben.

### `UNIQUE`

Ein Wert darf nur einmal vorkommen.

### `PRIMARY KEY`

Identifiziert den Datensatz.

### `FOREIGN KEY`

Stellt die Verbindung zu einer anderen Tabelle sicher.

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

## Prüfungstaugliche Formulierung

> Integrität bedeutet die Korrektheit und Konsistenz der in der Datenbank gespeicherten Daten.  
> Das `DBMS` kann dies durch verschiedene Regeln sicherstellen, zum Beispiel durch `PRIMARY KEY`, `FOREIGN KEY`, `NOT  
> NULL`, `UNIQUE` und `CHECK`-Constraints.  
> Ziel der Integrität ist es, dass die Datenbank nicht in einen fehlerhaften oder widersprüchlichen Zustand geraten kann.

## Häufige Prüfungsfehler

- Integrität nur als "Sicherheit" bezeichnen.
- Die Rolle der Schlüssel nicht erwähnen.
- Referentielle Integrität mit Datensicherung verwechseln.
- Nicht erwähnen, dass Integrität durch Regeln erzwungen werden kann.

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
