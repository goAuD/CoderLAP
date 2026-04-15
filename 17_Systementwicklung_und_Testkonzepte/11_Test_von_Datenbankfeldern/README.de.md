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

- darf es leer bleiben oder nicht

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

## Prüfungstaugliche Formulierung

> Beim Testen von Datenbankfeldern prüfen wir, ob die Felder den Erwartungen hinsichtlich Datentyp, Pflichtbereich,  
> Länge, Wertebereich, Format und Eindeutigkeit entsprechen.  
> Es ist wichtig, nicht nur mit korrekten, sondern auch mit fehlerhaften Eingaben, Grenzwerten und unerwarteten  
> Eingaben zu testen.  
> Das Ziel ist die Sicherstellung von Datenqualität, Konsistenz und Sicherheit.

## Häufige Prüfungsfehler

- Nur korrekte Daten testen.
- Grenzwerte nicht erwähnen.
- Den Feldtest ausschließlich als Oberflächenprüfung behandeln.
- Die Prüfung von Eindeutigkeit und Format auslassen.

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

1. OWASP Input Validation Cheat Sheet  
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html  
   Verwendung: offizielle Quelle zu den korrekten Prinzipien der Input-Validierung, einschließlich syntaktischer und
   semantischer Validierung.

2. PostgreSQL - Constraints  
   https://www.postgresql.org/docs/current/ddl-constraints.html  
   Verwendung: offizieller Hintergrund zu den feldbezogenen Einschränkungen, z.B. `NOT NULL`, `UNIQUE`, `CHECK`,
   `FOREIGN KEY`.

Abgerufen: `2026-04-09`
