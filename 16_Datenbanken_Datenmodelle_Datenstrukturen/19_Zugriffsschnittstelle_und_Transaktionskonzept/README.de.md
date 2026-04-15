# Zugriffsschnittstelle und Transaktionskonzept

## Schneller visueller Überblick

```text
Anwendung
    -> Zugriffsschnittstelle / Treiber / API
    -> DBMS
    -> Datenbank

Transaktion:
    BEGIN
      Operation 1
      Operation 2
    COMMIT oder ROLLBACK
```

## Was ist eine Zugriffsschnittstelle?

Das ist die technische Schicht, über die eine Anwendung mit der Datenbank kommuniziert.

Typische Beispiele:

- `JDBC`
- `ODBC`
- `ADO.NET`
- ORM oder Datenzugriffsschichten

Ihre Aufgaben:

- Verbindung herstellen
- SQL-Befehle senden
- Ergebnisse empfangen
- Fehler behandeln

## Was ist eine Transaktion?

Eine Transaktion ist eine Einheit aus mehreren Datenbankoperationen, die:

- gemeinsam ausgeführt wird
- oder gemeinsam fehlschlägt

Beispiel:

- Bestellung erfassen
- Lagerbestand verringern

Wenn das eine gelingt und das andere nicht, könnte das System in einen fehlerhaften Zustand geraten - deshalb braucht
man eine Transaktion.

## Grundbegriffe

| Begriff | Bedeutung |
|---|---|
| `BEGIN` | Transaktion starten |
| `COMMIT` | Änderungen festschreiben |
| `ROLLBACK` | Änderungen zurücknehmen |

## Warum ist das Transaktionskonzept wichtig?

- bewahrt die Konsistenz
- reduziert die Gefahr teilweise ausgeführter Operationen
- ist die Grundlage zuverlässiger Geschäftsprozesse

## Schnittstelle und Transaktion - nicht verwechseln

| Begriff | Rolle |
|---|---|
| Zugriffsschnittstelle | technische Verbindung zwischen Anwendung und DB |
| Transaktion | logische Operationseinheit in der Datenverarbeitung |

## ACID kurz zusammengefasst

Bei der Prüfung kann das Extrapunkte bringen:

- `Atomicity`
- `Consistency`
- `Isolation`
- `Durability`

Man muss es nicht immer ausführlich erklären, aber es ist gut zu wissen, dass dies die klassischen Qualitätsprinzipien
von Transaktionen sind.

## Prüfungstaugliche Formulierung

> Die Zugriffsschnittstelle stellt sicher, dass eine Anwendung sich mit der Datenbank verbinden, SQL-Befehle senden  
> und Ergebnisse zurückerhalten kann.  
> Das Transaktionskonzept bedeutet, dass zusammengehörige Datenbankoperationen als Einheit behandelt werden, die  
> entweder vollständig ausgeführt oder im Fehlerfall zurückgerollt werden können.  
> Das ist die Grundlage einer zuverlässigen und konsistenten Datenverarbeitung.

## Häufige Prüfungsfehler

- Die Schnittstelle mit der Datenbank selbst gleichsetzen.
- Die Transaktion als einfache Abfrage bezeichnen.
- Die Rolle von `COMMIT` und `ROLLBACK` nicht erwähnen.
- Nicht erwähnen, dass das Ziel die Wahrung der Konsistenz ist.

## Schnelle Selbstkontrolle

1. Was ist eine Zugriffsschnittstelle?
2. Was ist eine Transaktion?
3. Wozu dient `COMMIT`?
4. Wozu dient `ROLLBACK`?
5. Warum ist es wichtig, mehrere Operationen als Einheit zu behandeln?

## Kurzantworten zur Selbstkontrolle

1. Verbindungsschicht zwischen Anwendung und Datenbank
2. Einheit zusammengehörender Datenbankoperationen
3. Zum Festschreiben der Änderungen
4. Zum Zurücknehmen fehlgeschlagener Operationen
5. Weil so die Daten konsistent bleiben

## Quellen

1. Oracle - JDBC Basics  
   https://docs.oracle.com/javase/tutorial/jdbc/basics/index.html  
   Verwendung: offizielle Quelle zur Funktionsweise einer typischen Datenbankzugriffsschnittstelle.

2. Microsoft Learn - Local Transactions  
   https://learn.microsoft.com/en-us/dotnet/framework/data/adonet/local-transactions  
   Verwendung: offizielle, gut verständliche Quelle zur programmatischen Behandlung von Transaktionen.

3. PostgreSQL - Transactions  
   https://www.postgresql.org/docs/current/tutorial-transactions.html  
   Verwendung: offizieller Hintergrund zur Grundlogik von `BEGIN`, `COMMIT`, `ROLLBACK`.

Abgerufen: `2026-04-09`
