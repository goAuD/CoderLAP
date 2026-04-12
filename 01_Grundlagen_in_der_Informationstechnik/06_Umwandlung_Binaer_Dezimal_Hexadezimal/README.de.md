# Umwandlung zwischen Binär-, Dezimal- und Hexadezimalzahlen

## Schneller visueller Überblick

| Zahlensystem | Basis | Typische Zeichen |
| ------------ | ----: | ---------------- |
| binär        |   `2` | `0, 1`           |
| dezimal      |  `10` | `0-9`            |
| hexadezimal  |  `16` | `0-9, A-F`       |

### Schlüsselzusammenhang

| Hex | Binär  |
| --- | ------ |
| `0` | `0000` |
| `1` | `0001` |
| `2` | `0010` |
| `3` | `0011` |
| `4` | `0100` |
| `5` | `0101` |
| `6` | `0110` |
| `7` | `0111` |
| `8` | `1000` |
| `9` | `1001` |
| `A` | `1010` |
| `B` | `1011` |
| `C` | `1100` |
| `D` | `1101` |
| `E` | `1110` |
| `F` | `1111` |

Das ist eine der nützlichsten Prüfungstabellen.

## 1. Binär → Dezimal

Methode:

- jeden Stellenwert mit der entsprechenden Potenz von `2` multiplizieren
- die Ergebnisse addieren

### Beispiel

`101101₂`

Aufgeschlüsselt:

- `1 × 2^5 = 32`
- `0 × 2^4 = 0`
- `1 × 2^3 = 8`
- `1 × 2^2 = 4`
- `0 × 2^1 = 0`
- `1 × 2^0 = 1`

Insgesamt:

- `32 + 8 + 4 + 1 = 45`

Also:

- `101101₂ = 45₁₀`

## 2. Dezimal → Binär

Methode:

- durch `2` teilen
- die Reste notieren
- die Reste von unten nach oben lesen

### Beispiel

`45₁₀`

| Division | Quotient | Rest |
| -------- | -------: | ---: |
| `45 / 2` |     `22` |  `1` |
| `22 / 2` |     `11` |  `0` |
| `11 / 2` |      `5` |  `1` |
| `5 / 2`  |      `2` |  `1` |
| `2 / 2`  |      `1` |  `0` |
| `1 / 2`  |      `0` |  `1` |

Von unten nach oben:

- `101101`

Also:

- `45₁₀ = 101101₂`

## 3. Binär → Hexadezimal

Methode:

- von rechts beginnend die Binärzahl in `4-Bit-Gruppen` aufteilen
- bei Bedarf links mit Nullen auffüllen
- jede `4-Bit-Gruppe` durch eine Hexadezimalziffer ersetzen

### Beispiel

`1101111010₂`

In Vierergruppen:

- `0011 0111 1010`

Umgewandelt:

- `0011 = 3`
- `0111 = 7`
- `1010 = A`

Also:

- `1101111010₂ = 37A₁₆`

## 4. Hexadezimal → Binär

Methode:

- jede Hexadezimalziffer durch die entsprechende `4-Bit-Binärform` ersetzen

### Beispiel

`7B₁₆`

Umwandlung:

- `7 = 0111`
- `B = 1011`

Also:

- `7B₁₆ = 01111011₂`

## 5. Dezimal → Hexadezimal

Methode:

- durch `16` teilen
- Reste notieren
- die Reste von unten nach oben lesen

### Beispiel

`123₁₀`

| Division   | Quotient | Rest |
| ---------- | -------: | ---: |
| `123 / 16` |      `7` | `11` |
| `7 / 16`   |      `0` |  `7` |

`11` in hexadezimal:

- `B`

Von unten nach oben:

- `7B`

Also:

- `123₁₀ = 7B₁₆`

## 6. Hexadezimal → Dezimal

Methode:

- die Ziffern mit den entsprechenden Potenzen von `16` multiplizieren
- das Ergebnis addieren

### Beispiel

`2F₁₆`

wobei:

- `2 = 2`
- `F = 15`

Berechnung:

- `2 × 16^1 = 32`
- `15 × 16^0 = 15`

Insgesamt:

- `32 + 15 = 47`

Also:

- `2F₁₆ = 47₁₀`

## Warum ist die Umwandlung Binär ↔ Hexadezimal wichtig?

Weil das die schnellste praktische Verbindung ist:

- `1 Hexadezimalziffer = 4 Bit`

Daher ist bei:

- Speicheradressen
- Fehlercodes
- Farben
- Bytewerten

die hexadezimale Darstellung sehr praktisch.

## Prüfungstaugliche Formulierung

> Die Umwandlung zwischen Binär-, Dezimal- und Hexadezimalzahlen basiert auf dem Stellenwertsystem.  
> Von Binär nach Dezimal rechnet man mit Potenzen von 2, von Dezimal nach Binär teilt man durch 2 und liest die Reste rückwärts.  
> Zwischen Hexadezimal und Binär ist die Umwandlung besonders einfach, weil eine Hexadezimalziffer genau 4 Bit entspricht.

## Häufige Prüfungsfehler

- Die Reste bei der Divisionsmethode in der falschen Richtung zu lesen.
- Zu vergessen, dass `A-F` den Werten `10-15` entsprechen.
- Binärzahlen nicht von links nach rechts, sondern mit falschen Stellenwerten zu interpretieren.
- Die Binärzahl nicht in `4-Bit-Blöcke` aufzuteilen, bevor man sie hexadezimal umwandelt.
- Die `0`-Stellenwerte bei der Berechnung auszulassen.

## Schnelle Selbstkontrolle

1. Wie viel ist `1010₂` dezimal?
2. Wie viel ist `13₁₀` binär?
3. Wie viel ist `1111₂` hexadezimal?
4. Wie viel ist `A₁₆` binär?
5. Wie viel ist `FF₁₆` dezimal?

## Kurzantworten zur Selbstkontrolle

1. `10`
2. `1101`
3. `F`
4. `1010`
5. `255`

## Quellen

1. MDN - parseInt()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt  
   Verwendung: Zahlensystembasis (`Radix`) und Interpretation von Zahlen verschiedener Basen.

2. MDN - Number.prototype.toString()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString  
   Verwendung: Zahlendarstellung in verschiedenen Basen und Umwandlungsbeispiele.

3. Microsoft Learn - Literals in Q#  
   https://learn.microsoft.com/en-us/azure/quantum/user-guide/language/expressions/valueliterals  
   Verwendung: offizielle Beispiele für Binär-, Oktal-, Dezimal- und Hexadezimalnotationen.

4. Oracle - Binary Literals  
   https://docs.oracle.com/javase/8/docs/technotes/guides/language/binary-literals.html  
   Verwendung: Binär- und Hexadezimaldarstellung in praktischen Programmierbeispielen.

5. IBM Docs - ASCII and Hex Equivalents  
   https://www.ibm.com/docs/en/iis/11.7.0?topic=reference-ascii-hex-equivalents  
   Verwendung: konkrete Entsprechungstabelle für Binär-, Oktal-, Dezimal- und Hexadezimalwerte.

Abgerufen: `2026-04-08`
