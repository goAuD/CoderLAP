# Datenbanksysteme

## Schneller visueller Überblick

| Element | Rolle |
|---|---|
| Datenbank | Speicherung der Daten |
| `DBMS` | Verwaltung, Abfrage, Zugriff, Schutz |
| Anwendungen | geschäftliche oder technische Nutzung |
| Benutzer | Dateneingabe, Abfrage, Administration |

## Was ist ein Datenbanksystem?

Im engeren fachlichen Sinn besteht ein Datenbanksystem aus **Datenbank und verwaltendem DBMS**. Zum weiteren betrieblichen Umfeld gehören Anwendungen, Benutzer, Betriebspersonal und Hardware. Benenne, in welchem Sinn du den Begriff verwendest.

Das DBMS kann ein separater Server wie MySQL oder eine eingebettete Bibliothek wie SQLite sein. Auch eine in einer Datei gespeicherte Datenbank kann vollständige Abfrage- und Transaktionsfunktionen besitzen.

## Warum ist das wichtig?

- ermöglicht zentrale Datenverwaltung
- mehrere Benutzer können mit derselben Datenbank arbeiten
- der Zugriff kann geregelt werden
- unterstützt Sicherheit, Backup, Integrität und Leistung

## Typische Aufgaben eines Datenbanksystems

- Speicherung von Daten
- Abfrage
- Änderung
- Berechtigungsverwaltung
- Sicherung und Wiederherstellung
- Verwaltung des Mehrbenutzerbetriebs

## Datenbank, `DBMS`, Datenbanksystem - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Datenbank | strukturiert gespeicherte Daten |
| `DBMS` | Software, die die Daten verwaltet |
| Datenbanksystem | enger: Datenbank + `DBMS`; weiter: zusätzlich das betriebliche Umfeld |

## Wo begegnet man dem?

Typische Beispiele:

- Backend eines Webshops
- betriebliche Kundenverwaltung
- Lagerverwaltung
- Schüler- oder Mitarbeiterverwaltung
- Content-Management-Systeme

## Durchgearbeitetes Beispiel: Bibliotheksausleihe

In einer Bibliotheksanwendung gehören Tabellen wie `books` und `loans` zur Datenbank. Das MySQL-DBMS verarbeitet Abfragen, prüft Schlüssel und koordiniert gleichzeitige Änderungen. Die Anwendung zeigt das Formular, prüft die fachliche Berechtigung der angemeldeten Person und sendet die benötigte Anweisung.

Wollen zwei Schalter gleichzeitig dasselbe Exemplar verleihen, reicht das Schreiben in eine gemeinsame Datei allein nicht. Eine passend entworfene Transaktion und Datenbankregel machen überprüfbar, dass nur eine aktive Ausleihe entsteht. Das DBMS erfindet diese Geschäftsregel nicht selbst.

Das relationale Modell arbeitet mit Tabellen, Schlüsseln und Beziehungen. Dokument-, Schlüssel-Wert- und Graphdatenbanken bieten andere Strukturen. Entscheidend sind Abfragen, Datenbeziehungen und Konsistenzanforderungen, nicht allein die Bezeichnung SQL oder NoSQL.

## Prüfungstaugliche Formulierung

> Die Datenbank enthält strukturierte Daten, das DBMS verwaltet Zugriffe, Abfragen und Änderungen. Gemeinsam bilden sie den Kern des Datenbanksystems. Anwendungen und Betriebsumgebung bauen darauf auf.

## Schnelle Selbstkontrolle

1. Was ist ein Datenbanksystem?
2. Woraus besteht es typischerweise?
3. Was ist der Unterschied zwischen Datenbank und `DBMS`?
4. Warum ist zentrale Datenverwaltung wichtig?
5. Nenne zwei praktische Beispiele für Datenbanksysteme.

## Kurzantworten zur Selbstkontrolle

1. Enger: Datenbank und DBMS; weiter: einschließlich der betrieblichen Umgebung
2. Im Kern Datenbank und DBMS, umgeben von Anwendungen und Betriebsumgebung
3. Das eine sind die Daten, das andere ist die Verwaltungssoftware
4. Weil es einheitlichen und sicheren Zugriff bietet
5. Webshop, Kundenverwaltungssystem

## Quellen

1. Oracle - What Is a Database?  
   https://www.oracle.com/database/what-is-database/  
   Verwendung: offizielle, moderne Quelle zum Verständnis des Zusammenhangs zwischen Datenbank, `DBMS` und Datenbanksystem.

2. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Verwendung: offizielle Grundlagenquelle zur genaueren Definition relationaler Datenbanken und der Rolle des `DBMS`.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [SQLite: Appropriate Uses](https://www.sqlite.org/whentouse.html): Unterscheidung eingebetteter und Client-Server-Datenverwaltung
- [MySQL: Introduction to InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html): Transaktionen und die Rolle der InnoDB-Speicherengine

Geprüft: `2026-10-14`.
