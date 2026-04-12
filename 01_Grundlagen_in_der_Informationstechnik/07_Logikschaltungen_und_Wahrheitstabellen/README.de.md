# Logikschaltungen und Wahrheitstabellen

## Schneller visueller Überblick

### NOT

| A   | NOT A |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

### AND

| A   | B   | A AND B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 0       |
| 1   | 0   | 0       |
| 1   | 1   | 1       |

### OR

| A   | B   | A OR B |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |

### XOR

| A   | B   | A XOR B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

## Was ist eine logische Schaltung?

Ein digitales Schaltungselement oder eine logische Operation, die aus binären Eingaben eine binäre Ausgabe erzeugt.

Einfach gesagt:

- Eingabe: `0` oder `1`
- Regel: logische Operation
- Ausgabe: `0` oder `1`

## Was ist eine Wahrheitstabelle?

Eine Wahrheitstabelle listet alle möglichen Eingabekombinationen auf und gibt für jede Zeile die Ausgabe an.

Bei zwei Eingaben gibt es insgesamt:

- `4` Kombinationen

nämlich:

- `00`
- `01`
- `10`
- `11`

Bei einer Eingabe:

- `2` Kombinationen

## 1. NOT

**NOT** ist eine logische Operation mit einem Eingang.

Aufgabe:

- die Eingabe umkehren

Regel:

- `0` → `1`
- `1` → `0`

Bedeutung:

- Negation
- Invertierung

Einfaches Beispiel:

- System aktiviert = `1`
- nach NOT deaktiviert = `0`

## 2. AND

**AND** bedeutet:

- nur dann `1`, wenn **beide** Eingaben `1` sind

Schlüsselwort:

- **und**

Praktischer Gedanke:

- zwei Bedingungen müssen gleichzeitig erfüllt sein

Beispiel:

- Benutzer ist angemeldet = `1`
- hat Berechtigung = `1`
- Zugriff = `1`

Wenn eine davon fehlt:

- ist die Ausgabe `0`

## 3. OR

**OR** bedeutet:

- dann `1`, wenn **mindestens eine** Eingabe `1` ist

Schlüsselwort:

- **oder**

Beispiel:

- Alarm wird ausgelöst, wenn die Tür offen **oder** das Fenster offen ist

Nur dann `0`, wenn beide Eingaben `0` sind.

## 4. XOR

**XOR** bedeutet:

- exklusives Oder

Regel:

- dann `1`, wenn die beiden Eingaben **unterschiedlich** sind
- dann `0`, wenn die beiden Eingaben **gleich** sind

Also:

- `0, 1` → `1`
- `1, 0` → `1`
- `0, 0` → `0`
- `1, 1` → `0`

XOR ist besonders wichtig zum Beispiel bei:

- Paritätsprüfung
- einfachen Addiererschaltungen
- bestimmten Verschlüsselungsoperationen

## Wie kann man es sich schnell merken?

### AND

- beide müssen wahr sein

### OR

- mindestens eines muss wahr sein

### XOR

- genau eines ist wahr
- oder anders gesagt: die beiden Eingaben sind unterschiedlich

### NOT

- kehrt den Wert um

## Notationen

Manchmal begegnet man auch folgenden Formen:

| Operation | Wortform        | Häufige Kurzform |
| --------- | --------------- | ---------------- |
| NOT       | Negation        | `NOT A`          |
| AND       | Und             | `A AND B`        |
| OR        | Oder            | `A OR B`         |
| XOR       | Exklusives Oder | `A XOR B`        |

In mathematischen oder programmtechnischen Umgebungen können andere Zeichen vorkommen, aber bei der Prüfung ist die textuelle Interpretation am wichtigsten.

## Wofür werden sie verwendet?

- in digitalen Schaltungen
- in Steuerungsbedingungen
- in der Programmierung bei logischen Entscheidungen
- bei Bitoperationen
- bei der Fehlerprüfung

## Prüfungstaugliche Formulierung

> Logische Schaltungen arbeiten mit binären Eingaben, die Signale haben also den Wert 0 oder 1.  
> Die Wahrheitstabelle zeigt, welche Ausgabe zu allen möglichen Eingabekombinationen gehört.  
> AND ergibt nur dann 1, wenn beide Eingaben 1 sind. OR ergibt 1, wenn mindestens eine Eingabe 1 ist. XOR ergibt 1, wenn die beiden Eingaben unterschiedlich sind. NOT invertiert eine einzelne Eingabe.

## Häufige Prüfungsfehler

- OR und XOR zu verwechseln.
- Zu sagen, dass AND auch dann `1` ergibt, wenn nur eine Eingabe `1` ist.
- Zu vergessen, dass NOT nur einen Eingang hat.
- Die Wahrheitstabelle falsch auszufüllen.
- Nicht zu erkennen, dass das Wesentliche von XOR die Unterschiedlichkeit ist.

## Schnelle Selbstkontrolle

1. Wann ergibt AND eine `1` als Ausgabe?
2. Wann ergibt OR eine `0` als Ausgabe?
3. Wann ergibt XOR eine `1` als Ausgabe?
4. Was macht NOT?
5. Wie viele Zeilen hat eine Wahrheitstabelle mit zwei Eingaben?

## Kurzantworten zur Selbstkontrolle

1. Nur dann, wenn beide Eingaben `1` sind
2. Nur dann, wenn beide Eingaben `0` sind
3. Dann, wenn die beiden Eingaben unterschiedlich sind
4. Kehrt die Eingabe um
5. `4` Zeilen

## Quellen

1. Analog Devices - Logic Gate  
   https://www.analog.com/en/resources/glossary/logic-gate.html  
   Verwendung: Definitionen von Logikgattern und Wahrheitstabellen für AND, OR, XOR, NOT.

2. Analog Devices - XOR Gate  
   https://www.analog.com/en/resources/glossary/xor-gate.html  
   Verwendung: genaue Funktionsweise von XOR und typische praktische Anwendung.

3. Texas Instruments Education - Using Boolean Logic on the TI-83 Plus and TI-84 Plus Family  
   https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/product-usage/34774  
   Verwendung: praktische, überprüfbare Beschreibung von Boolean-Operationen (`and`, `or`, `xor`, `not`).

Abgerufen: `2026-04-08`
