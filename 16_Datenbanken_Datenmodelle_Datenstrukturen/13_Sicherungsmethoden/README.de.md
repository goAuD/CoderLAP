# Sicherungsmethoden

## Schneller visueller Überblick

| Sicherungstyp | Merkmal |
|---|---|
| Vollsicherung | alle Daten werden gesichert |
| inkrementelle Sicherung | nur die Änderungen werden gesichert |
| logische Sicherung | zum Beispiel `dump`, Export von Schemata und Daten |
| physische Sicherung | Datendateien, WAL / Logs, vollständiger Zustand |

## Warum ist Sicherung wichtig?

- bei Hardwarefehler
- bei menschlichem Fehler
- bei Softwarefehler
- nach einem Angriff oder Datenverlust

## Typische Methoden

### Vollsicherung

Sicherung der gesamten Datenbank.

Vorteil:

- einfachere Wiederherstellung

Nachteil:

- zeit- und speicherintensiver

### Inkrementelle Sicherung

Sichert nur die seit der letzten Sicherung eingetretenen Änderungen.

Vorteil:

- weniger Speicherbedarf

Nachteil:

- die Wiederherstellung kann aufwendiger sein

### Logische Sicherung

Zum Beispiel:

- `SQL dump`
- Export von Schema + Daten

### Physische Sicherung

Sicherung der tatsächlichen Datendateien oder des Datenbankzustands auf Datenbankebene.

## Backup und Recovery gehören zusammen

Bei der Prüfung ist es gut zu sagen:

- es reicht nicht, nur zu sichern
- man muss auch wiederherstellen können
- die Wiederherstellungszeit und der akzeptable Datenverlust sind ebenfalls relevant

## Sicherung und Replikation - nicht verwechseln

| Begriff | Wozu? |
|---|---|
| Backup | Wiederherstellung zu einem späteren Zeitpunkt |
| Replikation | Aufrechterhaltung einer Kopie für Betrieb oder Verfügbarkeit |

## Prüfungstaugliche Formulierung

> Sicherungsmethoden dienen dazu, eine Datenbank nach einem Fehler, Datenverlust oder Angriff wiederherstellen zu können.  
> Gängige Lösungen sind die Vollsicherung, die inkrementelle Sicherung sowie die logische und physische Sicherung.  
> Für einen effektiven Datenschutz ist nicht nur ein Backup, sondern auch ein geplantes Wiederherstellungsverfahren erforderlich.

## Häufige Prüfungsfehler

- Backup und Recovery gleichsetzen.
- Behaupten, dass eine Vollsicherung immer die beste Lösung ist.
- Die Seite der Wiederherstellung nicht erwähnen.
- Replikation vollständig als Backup betrachten.

## Schnelle Selbstkontrolle

1. Was ist das Ziel der Sicherung?
2. Was ist der Unterschied zwischen Vollsicherung und inkrementeller Sicherung?
3. Was ist eine logische Sicherung?
4. Warum braucht man auch einen Recovery-Plan?
5. Was ist der Unterschied zwischen Backup und Replikation?

## Kurzantworten zur Selbstkontrolle

1. Sicherstellung der Wiederherstellbarkeit
2. Die eine sichert alles, die andere nur die Änderungen
3. Zum Beispiel eine SQL-Dump-basierte Sicherung
4. Weil man die Sicherung auch verwenden können muss
5. Backup dient der Wiederherstellung, Replikation auch der Verfügbarkeit

## Quellen

1. PostgreSQL - Backup and Restore  
   https://www.postgresql.org/docs/current/backup.html  
   Verwendung: offizielle Quelle zu den Grundlagen des Backups.

2. PostgreSQL - SQL Dump  
   https://www.postgresql.org/docs/current/backup-dump.html  
   Verwendung: offizieller Hintergrund zur logischen Sicherung.

3. PostgreSQL - Continuous Archiving and Point-in-Time Recovery (PITR)  
   https://www.postgresql.org/docs/current/continuous-archiving.html  
   Verwendung: offizieller Hintergrund zu erweiterten Wiederherstellungsmöglichkeiten.

Abgerufen: `2026-04-09`
