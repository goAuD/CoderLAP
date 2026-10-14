# Test von Datenbankfeldern

## Schneller visueller Überblick

| Was wird getestet? | Beispiel |
|---|---|
| Datentyp | in ein Zahlenfeld darf kein Text |
| Länge | es darf kein zu langer Wert gespeichert werden |
| Pflichtfeld | funktioniert `NOT NULL`? |
| Eindeutigkeit | `UNIQUE`-Feld darf nicht dupliziert werden |
| Wertebereich | Preis darf nicht negativ sein |

## Was bedeutet das Testen eines Datenbankfeldes?

Wir prüfen, ob das Feld:

- den richtigen Datentyp akzeptiert
- korrekte Werte annimmt
- fehlerhafte oder gefährliche Werte ablehnt
- mit der Spezifikation und den Einschränkungen übereinstimmt

## Typische Prüfungen

### Pflichtfeld

- ist SQL NULL erlaubt; leerer Text benötigt eine eigene Regel

### Längenprüfung

- erlaubt es zu lange Daten

### Formatprüfung

- ist das Format von E-Mail, Datum, Code, Postleitzahl korrekt

### Wertebereichsprüfung

- liegt eine Zahl oder ein Datum innerhalb eines gültigen Bereichs

### Eindeutigkeit

- ist ein duplizierter Wert erlaubt oder verboten

## Warum ist das wichtig?

- schützt die Datenqualität
- reduziert die Anzahl fehlerhafter Datensätze
- verbessert die Sicherheit
- verhindert spätere Datenverarbeitungsprobleme

## Es muss mit korrekten und fehlerhaften Eingaben getestet werden

Guter Punkt bei der Prüfung:

- wir probieren nicht nur "gute" Daten aus
- es sollen auch Grenzwerte und fehlerhafte Eingaben dabei sein

## Test von Datenbankfeldern und UI-Test: nicht verwechseln

| Begriff | Fokus |
|---|---|
| UI-Test | das Verhalten der Oberfläche |
| Datenfeldtest | die Gültigkeit und Speicherung der Daten |

## NULL, leerer Text und null sind unterschiedliche Fälle

`NOT NULL` verbietet den SQL-Wert `NULL`. Die Zahl `0`, leerer Text (`''`) und
Text aus Leerzeichen sind andere Werte. Ob sie zulässig sind, entscheidet eine
eigene Regel. Ein Produktname könnte nach Entfernen äußerer Leerzeichen
beispielsweise 1..80 Zeichen enthalten müssen.

| Eingabe für den Namen | Erwartung laut diesem Vertrag |
|---|---|
| `"Ada"` | akzeptieren |
| `NULL`, `""`, `"   "` | ablehnen |
| 80 Zeichen | akzeptieren |
| 81 Zeichen | ablehnen, nicht still kürzen |
| `"Őrség"` | korrekt speichern und unverändert zurücklesen |

In MySQL 8.4 ist etwa `price DECIMAL(8,2) NOT NULL CHECK (price >= 0)` ein
**Ausschnitt einer Spaltendefinition**, kein eigenständiges SQL-Programm.
`CHECK` allein kann eine wegen `NULL` unbekannte Bedingung akzeptieren, deshalb
kommt die Pflichtangabe hinzu. Wir testen die tatsächliche Datenbankversion und
den SQL-Modus, nicht nur die Oberfläche. Zeichen- und Bytelänge können abweichen;
deshalb sind Akzente wichtige Testdaten. Neben Eingabevalidierung benötigen wir
gesondert parametrisierte SQL-Anweisungen, Berechtigungsprüfung und geeignete Ausgabekodierung.

## Prüfungstaugliche Formulierung

> Beim Testen von Datenbankfeldern prüfen wir, ob die Felder den Erwartungen hinsichtlich Datentyp, Pflichtangabe,  
> Länge, Wertebereich, Format und Eindeutigkeit entsprechen.  
> Es ist wichtig, nicht nur mit korrekten, sondern auch mit fehlerhaften Eingaben, Grenzwerten und unerwarteten  
> Eingaben zu testen.  
> Das Ziel ist die Sicherstellung von Datenqualität, Konsistenz und Sicherheit.

## Schnelle Selbstkontrolle

1. Was muss bei einem Datenbankfeld geprüft werden?
2. Warum ist das Testen mit fehlerhaften Eingaben wichtig?
3. Was ist ein Grenzwerttest hier?
4. Wofür ist die Eindeutigkeitsprüfung da?
5. Warum ist der serverseitige und datenbankbezogene Schutz auch wichtig?

## Kurzantworten zur Selbstkontrolle

1. Typ, Länge, Pflicht, Wertebereich, Format, Eindeutigkeit
2. Weil das System auch diese verarbeiten können muss
3. Das Testen im Bereich des erlaubten Minimums und Maximums
4. Zur Vermeidung von Duplikaten
5. Weil clientseitige Prüfung umgangen werden kann

## Quellen

Geprüft: `2026-10-14`.

- [MySQL: NULL values](https://dev.mysql.com/doc/refman/8.4/en/working-with-null.html): Unterschied zwischen NULL, leerem Text und null.
- [MySQL: CHECK constraints](https://dev.mysql.com/doc/refman/8.4/en/create-table-check-constraints.html): CHECK und UNKNOWN.
- [OWASP: Input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html): Validierung und getrennte Schutzmaßnahmen.


1. OWASP Input Validation Cheat Sheet  
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html  
   Verwendung: offizielle Quelle zu den korrekten Prinzipien der Input-Validierung, einschließlich syntaktischer und
   semantischer Validierung.

2. PostgreSQL - Constraints  
   https://www.postgresql.org/docs/current/ddl-constraints.html  
   Verwendung: offizieller Hintergrund zu den feldbezogenen Einschränkungen, z.B. `NOT NULL`, `UNIQUE`, `CHECK`,
   `FOREIGN KEY`.

Abgerufen: `2026-04-09`
