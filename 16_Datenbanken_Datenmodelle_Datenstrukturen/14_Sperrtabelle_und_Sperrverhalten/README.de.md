# Sperrtabelle und Sperrverhalten

## Schneller visueller Überblick

| Phänomen | Was bedeutet das? |
|---|---|
| Lock / Sperre | vorübergehende Einschränkung anderer Operationen |
| Warten | eine Transaktion wartet auf die andere |
| Deadlock | zwei Transaktionen warten gegenseitig aufeinander und blockieren sich |

## Was ist eine Sperre?

Wenn mehrere Benutzer oder Prozesse gleichzeitig mit denselben Daten arbeiten, schützt das `DBMS` die Konsistenz häufig
durch Sperren.

Das kann zum Beispiel geschehen:

- auf Zeilenebene
- auf Tabellenebene
- mit verschiedenen Lock-Typen

## Was ist eine "Sperrtabelle"?

Im Prüfungskontext bedeutet dies im Allgemeinen, dass:

- das System erfasst, welche Sperren aktuell gelten
- welche Transaktion was sperrt

Es handelt sich nicht unbedingt um eine vom Benutzer verwaltete "normale Tabelle", sondern um die logische oder interne
Darstellung des Sperrzustands.

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

## Durchgearbeiteter Fall: den letzten Bestand reservieren

Von einem Produkt ist noch ein Stück vorhanden. Verbindung A und B wollen es gleichzeitig reservieren. In **MySQL/InnoDB** liest A die Produktzeile innerhalb einer expliziten Transaktion mit `SELECT ... FOR UPDATE` und ändert sie anschließend. B wartet beim sperrenden Lesen derselben Zeile, bis A bestätigt oder zurückrollt. Danach kann B anhand des aktuellen Zustands entscheiden.

Ein gewöhnliches konsistentes `SELECT` kann MVCC, also Lesen anhand mehrerer Datenversionen, verwenden. Deshalb wartet nicht jede Leseoperation auf den Schreiber. `FOR UPDATE` verhält sich anders. Die Sperre bleibt bis zum Transaktionsende bestehen; währenddessen sollte man nicht auf einen Benutzerklick oder langsamen externen Dienst warten.

| Situation | Bedeutung |
|---|---|
| B wartet auf eine Sperre von A | kann normale Konfliktbehandlung sein |
| A hält Zeile 1, B Zeile 2 und beide verlangen die jeweils andere | Deadlock, zyklisches Warten |
| alle Transaktionen fordern Zeilen in derselben Reihenfolge an | geringeres Deadlock-Risiko |

InnoDB kann einen Deadlock erkennen und eine beteiligte Transaktion zurückrollen. Die Anwendung muss auf einen kontrollierten erneuten Versuch der gesamten betroffenen Transaktion vorbereitet sein. Ein Timeout rollt nicht zwingend auf dieselbe Weise die gesamte Transaktion zurück; explizites Rollback kann deshalb zur Fehlerbehandlung gehören.

Die Verträglichkeit exklusiver und geteilter Sperren, Indizes und Isolationsstufe bestimmen gemeinsam das genaue Verhalten. Mit passenden Rechten lassen sich Sperren beispielsweise über MySQL `performance_schema.data_locks` und `data_lock_waits` untersuchen.

## Prüfungstaugliche Formulierung

> Sperren dienen dazu, die Datenkonsistenz auch bei gleichzeitiger Datenverarbeitung durch mehrere Benutzer zu  
> gewährleisten.  
> Das `DBMS` kann verschiedene Lock-Mechanismen anwenden, und deren Verhalten beeinflusst das Warten, die Parallelität  
> und die Leistung.  
> Falsche oder zu starke Sperrung kann zu Problemen führen, zum Beispiel zu Wartezeiten oder Deadlocks.

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

### Geprüfte Quellen zur Ergänzung

- [MySQL: Locking Reads](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-reads.html): FOR UPDATE und Warten
- [MySQL: Deadlocks](https://dev.mysql.com/doc/refman/8.0/en/innodb-deadlocks-handling.html): Deadlock-Behandlung und erneuter Transaktionsversuch
- [MySQL: InnoDB error handling](https://dev.mysql.com/doc/refman/8.0/en/innodb-error-handling.html): Unterschied zwischen Timeout und vollständigem Transaktionsrollback

Geprüft: `2026-10-14`.
