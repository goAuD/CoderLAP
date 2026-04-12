# Sperrtabelle und Sperrverhalten

## Schneller visueller Überblick

| Phänomen | Was bedeutet das? |
|---|---|
| Lock / Sperre | vorübergehende Einschränkung anderer Operationen |
| Warten | eine Transaktion wartet auf die andere |
| Deadlock | zwei Transaktionen warten gegenseitig aufeinander und blockieren sich |

## Was ist eine Sperre?

Wenn mehrere Benutzer oder Prozesse gleichzeitig mit denselben Daten arbeiten, schützt das `DBMS` die Konsistenz häufig durch Sperren.

Das kann zum Beispiel geschehen:

- auf Zeilenebene
- auf Tabellenebene
- mit verschiedenen Lock-Typen

## Was ist eine "Sperrtabelle"?

Im Prüfungskontext bedeutet dies im Allgemeinen, dass:

- das System erfasst, welche Sperren aktuell gelten
- welche Transaktion was sperrt

Es handelt sich nicht unbedingt um eine vom Benutzer verwaltete "normale Tabelle", sondern um die logische oder interne Darstellung des Sperrzustands.

## Warum ist das Sperrverhalten wichtig?

- verhindert, dass zwei Operationen gleichzeitig widersprüchlich schreiben
- hilft, die Konsistenz zu bewahren
- beeinflusst die Leistung und die Parallelität

## Mögliche Probleme

### Warten

Eine Transaktion wartet, bis die andere die Sperre freigibt.

### Deadlock

Zwei Transaktionen warten gegenseitig aufeinander, und keine kann weitermachen.

### Zu starke Sperrung

Verschlechtert die parallele Leistung.

## Sperre und Transaktion - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Transaktion | Einheit logisch zusammengehörender Operationen |
| Sperre | technischer Mechanismus zur Vermeidung von Konflikten |

## Prüfungstaugliche Formulierung

> Sperren dienen dazu, die Datenkonsistenz auch bei gleichzeitiger Datenverarbeitung durch mehrere Benutzer zu gewährleisten.  
> Das `DBMS` kann verschiedene Lock-Mechanismen anwenden, und deren Verhalten beeinflusst das Warten, die Parallelität und die Leistung.  
> Falsche oder zu starke Sperrung kann zu Problemen führen, zum Beispiel zu Wartezeiten oder Deadlocks.

## Häufige Prüfungsfehler

- Sperren einfach als Fehler betrachten.
- Nicht erwähnen, dass das Ziel der Schutz der Konsistenz ist.
- Den Begriff `Sperrtabelle` wörtlich als Benutzerdatentabelle behandeln.
- Die Möglichkeit eines Deadlocks weglassen.

## Schnelle Selbstkontrolle

1. Warum braucht man Sperren?
2. Was bedeutet Sperrverhalten?
3. Was ist ein Deadlock?
4. Was ist der Zusammenhang zwischen Transaktion und Lock?
5. Warum kann zu viel Sperrung Leistungsprobleme verursachen?

## Kurzantworten zur Selbstkontrolle

1. Zum Schutz der Datenkonsistenz
2. Das praktische Verhalten der Sperren
3. Ein Stillstand durch gegenseitiges Warten von Transaktionen
4. Die Transaktion kann Sperren zum Schutz verwenden
5. Weil es den parallelen Zugriff einschränkt

## Quellen

1. PostgreSQL - Explicit Locking  
   https://www.postgresql.org/docs/current/explicit-locking.html  
   Verwendung: offizielle Quelle zu den Lock-Typen und deren Verhalten.

2. PostgreSQL - Transaction Isolation  
   https://www.postgresql.org/docs/current/transaction-iso.html  
   Verwendung: ergänzender Hintergrund zum Verständnis des Zusammenhangs zwischen parallelem Zugriff und Konsistenz.

Abgerufen: `2026-04-09`
