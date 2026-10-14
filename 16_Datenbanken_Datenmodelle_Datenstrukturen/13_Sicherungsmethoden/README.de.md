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
| Backup | Grundlage zur Wiederherstellung eines früher gesicherten, nutzbaren Zustands |
| Replikation | Aufrechterhaltung einer Kopie für Betrieb oder Verfügbarkeit |

## Durchgearbeiteter MySQL-Sicherungsfall

**Voll/inkrementell** beschreibt Umfang und Abhängigkeiten der Sicherungskette, **logisch/physisch** dagegen die technische Umsetzung. Eine Vollsicherung kann somit ein logischer Dump sein.

Bei MySQL/InnoDB kann `mysqldump --single-transaction` einen konsistenten logischen Snapshot der transaktionalen Tabellen erzeugen. Währenddessen darf die betroffene Tabellenstruktur nicht geändert werden. Die Option macht gleichzeitig veränderte MyISAM-Tabellen nicht auf dieselbe Weise konsistent. Auch das einfache Kopieren des Datenverzeichnisses eines laufenden Servers ist kein allgemeines Backup-Verfahren. Physische Sicherungen benötigen eine unterstützte Methode, die Konsistenz gewährleistet.

Beispiel: Um 02:00 liegt eine Vollsicherung vor, um 10:15 erfolgt eine versehentliche Löschung. Sind passende Binärlogs und Startposition vorhanden, können Änderungen nach dem Backup bis unmittelbar vor der Löschung eingespielt werden (**Point-in-Time Recovery**). Das löschende Ereignis wird nicht mehr wiedergegeben. Die Sicherung allein enthält keine Änderungen nach 02:00.

Der Test-Restore erfolgt in eine getrennte Datenbank. Prüfe Schema, Zeilenzahlen, Schlüssel und mindestens eine fachliche Abfrage. Routinen, Events, Rechte, Konfiguration und Schlüssel können gesonderte Behandlung benötigen. Replikation kann die versehentliche Löschung ebenfalls übertragen und ersetzt deshalb keine Wiederherstellung eines früheren Zustands.

## Prüfungstaugliche Formulierung

> Sicherungsmethoden dienen dazu, eine Datenbank nach einem Fehler, Datenverlust oder Angriff wiederherstellen zu  
> können.  
> Gängige Lösungen sind die Vollsicherung, die inkrementelle Sicherung sowie die logische und physische Sicherung.  
> Für einen effektiven Datenschutz ist nicht nur ein Backup, sondern auch ein geplantes Wiederherstellungsverfahren erforderlich.

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

### Geprüfte Quellen zur Ergänzung

- [MySQL: mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html): Voraussetzungen von single-transaction und Dump-Inhalt
- [MySQL: Point-in-Time Recovery](https://dev.mysql.com/doc/refman/8.0/en/point-in-time-recovery.html): Basissicherung und Wiedergabe des Binärlogs

Geprüft: `2026-10-14`.
