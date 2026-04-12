# Index: Vor- und Nachteile

## Schneller visueller Überblick

| Vorteil | Nachteil |
|---|---|
| schnellere Suche | zusätzlicher Speicherbedarf |
| bessere Filterung und Sortierung | Wartungskosten |
| effizientere Joins | Änderungsoperationen können langsamer werden |

## Was ist ein Index?

Ein Index ist eine Datenstruktur, die dabei hilft, bestimmte Datensätze schneller zu finden, ohne die gesamte Tabelle durchlesen zu müssen.

Analogie:

- wie ein Stichwort- oder Namensverzeichnis in einem Buch

## Warum ist er nützlich?

Besonders hilfreich bei:

- häufig gefilterten Spalten
- Schlüsselfeldern
- Sortierung
- Join-Operationen

## Hauptvorteile

- schnellere `SELECT`-Operationen
- schnellere Suche mit Bedingung
- effizientere relationale Verknüpfung
- bessere Leistung bei großen Tabellen

## Hauptnachteile

- benötigt Speicherplatz
- muss bei jeder Schreiboperation gewartet werden
- zu viele Indizes können die Gesamtleistung verschlechtern
- ein schlecht gewählter Index bringt keinen echten Nutzen

## Wann sollte man einen Index verwenden?

- wenn es viele Abfragen gibt
- wenn die Datenmenge groß ist
- wenn auf einer bestimmten Spalte häufig gesucht wird

## Wann ist ein Index nicht unbedingt sinnvoll?

- bei sehr kleinen Tabellen
- bei selten verwendeten Spalten
- wenn es viele Änderungen und wenige Abfragen gibt

## Index und Schlüssel - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Schlüssel | logische Rolle im Datenmodell |
| Index | technische Struktur zur Leistungsverbesserung |

Sie hängen häufig zusammen, sind aber nicht dasselbe.

## Prüfungstaugliche Formulierung

> Ein Index ist eine Datenbankstruktur, die die Suche nach Daten und bestimmte Abfragen beschleunigt.  
> Sein Vorteil ist die bessere Abfrageleistung, sein Nachteil der zusätzliche Speicherbedarf und die Tatsache, dass er bei Änderungsoperationen gewartet werden muss.  
> Daher können Indizes Leistungsgewinne bringen, sollten aber nur mit sorgfältiger Planung eingesetzt werden.

## Häufige Prüfungsfehler

- Behaupten, dass ein Index in jedem Fall eine Verbesserung bringt.
- Den Index mit dem Primärschlüssel gleichsetzen.
- Die Verlangsamung bei Schreiboperationen nicht erwähnen.
- Den Speicherbedarf vergessen.

## Schnelle Selbstkontrolle

1. Was ist das Ziel eines Index?
2. Was ist ein Hauptvorteil?
3. Was ist ein Hauptnachteil?
4. Wann ist er besonders nützlich?
5. Was ist der Unterschied zwischen Schlüssel und Index?

## Kurzantworten zur Selbstkontrolle

1. Schnellere Suche und Abfrage
2. Bessere `SELECT`-Leistung
3. Mehr Speicherplatz und langsamere Änderungen
4. Bei großen Tabellen und häufiger Filterung
5. Der Schlüssel ist ein logischer, der Index ein technischer Begriff

## Quellen

1. PostgreSQL - Indexes  
   https://www.postgresql.org/docs/current/indexes.html  
   Verwendung: offizielle Quelle zur Rolle und Funktionsweise von Indizes.

2. PostgreSQL - Indexes Introduction  
   https://www.postgresql.org/docs/current/indexes-intro.html  
   Verwendung: kompakte, offizielle Einführung zu den Vorteilen und Kosten von Indizes.

Abgerufen: `2026-04-09`
