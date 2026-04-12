# Zahlensysteme in der IT

## Schneller visueller Überblick

| Zahlensystem | Basis | Verwendete Ziffern | Gleiches Beispiel |
| ------------ | ----: | ------------------ | ----------------- |
| binär        |   `2` | `0, 1`             | `101010₂`         |
| oktal        |   `8` | `0-7`              | `52₈`             |
| dezimal      |  `10` | `0-9`              | `42₁₀`            |
| hexadezimal  |  `16` | `0-9, A-F`         | `2A₁₆`            |

Alle vier Zahlen können denselben Wert darstellen:

- `42`

## Was ist ein Zahlensystem?

Ein Zahlensystem ist ein Regelwerk dafür, wie Mengen mit Ziffern dargestellt werden.

Das Wesentliche am Stellenwertsystem:

- jede Position hat ein anderes Gewicht
- dieses Gewicht ergibt sich aus den Potenzen der Basis

Beispiel im Dezimalsystem:

`542` =

- `5 × 10^2`
- `4 × 10^1`
- `2 × 10^0`

## 1. Dezimalsystem

Das ist das alltägliche, von Menschen am häufigsten verwendete System.

Basis:

- `10`

Ziffern:

- `0-9`

Beispiel:

`347` =

- `3 × 10^2`
- `4 × 10^1`
- `7 × 10^0`

## 2. Binärsystem

Die Grundlage der Informatik ist das Binärsystem, weil digitale Schaltungen von Natur aus mit zwei Zuständen arbeiten:

- `0`
- `1`

Basis:

- `2`

Beispiel:

`1011₂` =

- `1 × 2^3`
- `0 × 2^2`
- `1 × 2^1`
- `1 × 2^0`

Das ergibt dezimal:

- `8 + 0 + 2 + 1 = 11`

## 3. Oktalsystem

Die Basis des Oktalsystems:

- `8`

Ziffern:

- `0-7`

Heute wird es seltener verwendet, aber man begegnet ihm noch zum Beispiel:

- in älteren Systemen
- bei Berechtigungsangaben
- in systemnahen technischen Umgebungen

Beispiel:

`17₈` =

- `1 × 8^1 + 7 × 8^0 = 15₁₀`

## 4. Hexadezimalsystem

Basis:

- `16`

Ziffern:

- `0-9`
- `A, B, C, D, E, F`

wobei:

- `A = 10`
- `B = 11`
- `C = 12`
- `D = 13`
- `E = 14`
- `F = 15`

Beispiel:

`2A₁₆` =

- `2 × 16^1 + 10 × 16^0`
- `32 + 10 = 42`

## Warum ist das Hexadezimalsystem wichtig?

Weil es sehr gut zur binären Welt passt:

- `1 Hexadezimalziffer = 4 Bit`

Daher lassen sich lange Binärfolgen viel kürzer hexadezimal schreiben.

Beispiel:

- binär: `11111111`
- hexadezimal: `FF`

## Wo werden diese in der IT verwendet?

### Dezimal

- alltägliches Rechnen
- Benutzeroberflächen
- Geschäftsdaten

### Binär

- Bits
- Prozessoren
- Speicher
- systemnahe Abläufe

### Oktal

- einige System- und Berechtigungsangaben
- spezielle technische Umgebungen

### Hexadezimal

- Speicheradressen
- Fehlercodes
- Farbcodes, zum Beispiel in CSS
- kurze Darstellung von Bytes
- übersichtliche Darstellung von Binärdaten

## Häufige Notationen in der Programmierung

Viele Sprachen und Werkzeuge verwenden Präfixe:

- `0b1010` = binär
- `0o52` = oktal
- `42` = dezimal
- `0x2A` = hexadezimal

Das kann je nach Sprache variieren, aber die Grundidee ist dieselbe.

## Prüfungstaugliche Formulierung

> In der Informatik werden am häufigsten das Binär-, Oktal-, Dezimal- und Hexadezimalsystem verwendet.  
> Das Binärsystem hat die Basis 2 und verwendet daher nur die Ziffern 0 und 1.  
> Das Dezimalsystem hat die Basis 10, es ist das alltägliche Zahlensystem.  
> Das Hexadezimalsystem hat die Basis 16 und ist deshalb wichtig, weil es Binärdaten gut komprimiert: eine Hexadezimalziffer entspricht 4 Bit.

## Häufige Prüfungsfehler

- Zu vergessen, dass hexadezimal auch `A-F` als Ziffern enthält.
- Zu sagen, dass die Basis des Oktalsystems `16` ist.
- Nicht zu wissen, dass das Binärsystem nur `0` und `1` verwendet.
- Nicht zu erkennen, dass dieselbe Zahl in verschiedenen Zahlensystemen anders aussieht.
- Nicht zu wissen, warum die hexadezimale Notation praktisch ist.

## Schnelle Selbstkontrolle

1. Welches Zahlensystem hat die Basis `2`?
2. Welches Zahlensystem verwendet die Zeichen `0-9` und `A-F`?
3. Wie viel ist `2A₁₆` dezimal?
4. Welches Zahlensystem wird hauptsächlich für die Logik digitaler Hardware verwendet?
5. Warum ist das Hexadezimalsystem nützlich?

## Kurzantworten zur Selbstkontrolle

1. Das **Binärsystem**
2. Das **Hexadezimalsystem**
3. `42`
4. Das **Binärsystem**
5. Weil es Binärdaten kompakt darstellt und `1 Hexadezimalziffer = 4 Bit`

## Quellen

1. Microsoft Learn - Literals in Q#  
   https://learn.microsoft.com/en-us/azure/quantum/user-guide/language/expressions/valueliterals  
   Verwendung: moderne, offizielle Beispiele für binäre, oktale, dezimale und hexadezimale Notationen.

2. Oracle - Binary Literals (Java SE 7+)  
   https://docs.oracle.com/javase/8/docs/technotes/guides/language/binary-literals.html  
   Verwendung: praktische Verwendung von Binär- und Hexadezimaldarstellung in der Programmierung.

3. MDN - parseInt()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt  
   Verwendung: der Begriff `Radix`, Zahlensysteme und gültige Ziffern.

4. MDN - Number.prototype.toString()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString  
   Verwendung: Zahlenumwandlung und Darstellung in verschiedenen Basen in der Programmierung.

5. IBM Docs - ASCII and Hex Equivalents  
   https://www.ibm.com/docs/en/iis/11.7.0?topic=reference-ascii-hex-equivalents  
   Verwendung: Übersicht der Entsprechungen zwischen Binär, Oktal, Dezimal und Hexadezimal.

Abgerufen: `2026-04-08`
