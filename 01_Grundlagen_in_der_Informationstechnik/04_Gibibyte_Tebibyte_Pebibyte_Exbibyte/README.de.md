# Gibibyte, Tebibyte, Pebibyte, Exbibyte

## Schneller visueller Überblick

| Einheit  | Bezeichnung | Faktor |                       In Byte |
| -------- | ----------- | -----: | ----------------------------: |
| Gibibyte | `GiB`       | `2^30` |             `1 073 741 824 B` |
| Tebibyte | `TiB`       | `2^40` |         `1 099 511 627 776 B` |
| Pebibyte | `PiB`       | `2^50` |     `1 125 899 906 842 624 B` |
| Exbibyte | `EiB`       | `2^60` | `1 152 921 504 606 846 976 B` |

### Eselsbrücke

Die binären Einheiten basieren auf `2^10 = 1024`:

- `1 TiB = 1024 GiB`
- `1 PiB = 1024 TiB`
- `1 EiB = 1024 PiB`

## Warum wurden diese Einheiten eingeführt?

Digitale Systeme arbeiten von Natur aus **binär**,
daher basieren Speicher und viele interne technische Berechnungen
tatsächlich auf Potenzen von `2`.

Lange Zeit wurden in der Praxis die Bezeichnungen `KB`, `MB`, `GB` auch für Werte verwendet, die in Wirklichkeit:

- `1024`
- `1024^2`
- `1024^3`

basierten.

Das führte zu Missverständnissen, weshalb genauere binäre Bezeichnungen eingeführt wurden:

- `KiB`
- `MiB`
- `GiB`
- `TiB`
- `PiB`
- `EiB`

## Was bedeutet der Name?

Die binären Präfixe entstanden,
indem zum ersten Teil des entsprechenden SI-Präfixes `bi` hinzugefügt wurde,
was auf das Wort `binary` verweist.

Beispiele:

- `Giga` → `Gibi`
- `Tera` → `Tebi`
- `Peta` → `Pebi`
- `Exa` → `Exbi`

In der Bezeichnung erscheint daher das zusätzliche `i`:

- `GB` vs `GiB`
- `TB` vs `TiB`

## GiB und GB: der wichtigste Unterschied

| Einheit | Typ     | Wert        |
| ------- | ------- | ----------- |
| `GB`    | dezimal | `10^9 Byte` |
| `GiB`   | binär   | `2^30 Byte` |

In Zahlen:

- `1 GB = 1 000 000 000 Byte`
- `1 GiB = 1 073 741 824 Byte`

Also ist `GiB` größer als `GB`.

Dasselbe gilt bei größeren Einheiten:

- `TiB > TB`
- `PiB > PB`
- `EiB > EB`

## Wo begegnet man ihnen in der Praxis?

### 1. Betriebssysteme und Speicher

RAM, Cache und viele interne Speicherbegriffe sind von Natur aus
in der binären Welt angesiedelt,
daher sind hier binäre Einheiten logischer.

### 2. Systemtools und technische Dokumentation

In Fachdokumentationen wird die genaue Kennzeichnung immer wichtiger:

- `GB` wenn dezimal
- `GiB` wenn binär

### 3. Abweichungen bei Speicheranzeigen

Ein Hersteller kann einen Datenträger als `1 TB` angeben,
während das Betriebssystem die Größe nach binärer Logik anzeigt.
Dadurch kann der Benutzer die Kapazität als kleiner empfinden,
obwohl er in Wirklichkeit nur eine andere Einheit sieht.

## Schnelle Beispiele

### Beispiel 1

`1 GiB` =

- `2^30 Byte`
- `1 073 741 824 Byte`

### Beispiel 2

`2 TiB` =

- `2 × 2^40 Byte`
- `2 199 023 255 552 Byte`

### Beispiel 3

`1 PiB` =

- `2^50 Byte`
- `1 125 899 906 842 624 Byte`

## Zusammenhang mit den kleineren binären Einheiten

Vollständige Kette:

- `1 KiB = 2^10 B`
- `1 MiB = 2^20 B`
- `1 GiB = 2^30 B`
- `1 TiB = 2^40 B`
- `1 PiB = 2^50 B`
- `1 EiB = 2^60 B`

## Prüfungstaugliche Formulierung

> Gibibyte, Tebibyte, Pebibyte und Exbibyte sind binäre Datengrößeneinheiten.  
> Sie basieren auf Potenzen von 2, daher gilt zum Beispiel
> 1 GiB = 2^30 Byte, 1 TiB = 2^40 Byte.  
> GiB, TiB, PiB und EiB sind nicht identisch mit den dezimalen Einheiten GB, TB, PB und EB.  
> Die binären Präfixe wurden eingeführt,
> damit der Unterschied zwischen 1000er-
> und 1024er-basierter Berechnung eindeutig ist.

## Häufige Prüfungsfehler

- `GiB` und `GB` zu verwechseln.
- Zu sagen, dass `1 GiB = 1 000 000 000 Byte`.
- Zu vergessen, dass der binäre Schritt `1024` ist, nicht `1000`.
- Nicht zu wissen, warum in der Bezeichnung ein `i` steht.
- Zu glauben, dass binäre Präfixe SI-Präfixe sind.

## Schnelle Selbstkontrolle

1. Wie viel ist `1 GiB` in Byte?
2. Wie viel ist `1 TiB` in Byte?
3. Was ist größer: `1 GB` oder `1 GiB`?
4. Warum wurde die Bezeichnung `GiB` eingeführt?
5. Wie viel ist `1 EiB` in Byte?

## Kurzantworten zur Selbstkontrolle

1. `1 073 741 824 Byte`
2. `1 099 511 627 776 Byte`
3. `1 GiB` ist größer
4. Damit der Unterschied zwischen binären und dezimalen Einheiten eindeutig ist
5. `1 152 921 504 606 846 976 Byte`

## Quellen

1. NIST - Definitions of the SI units: The binary prefixes  
   https://physics.nist.gov/cgi-bin/cuu/Info/Units/binary.html  
   Verwendung: offizielle Definition der binären Präfixe und Vergleich mit SI-Präfixen.

2. NIST CSRC Glossary - gibibyte  
   https://csrc.nist.gov/glossary/term/gibibyte  
   Verwendung: `GiB = 2^30 Byte`.

3. NIST CSRC Glossary - tebibyte  
   https://csrc.nist.gov/glossary/term/tebibyte  
   Verwendung: `TiB = 2^40 Byte`.

4. NIST CSRC Glossary - pebibyte  
   https://csrc.nist.gov/glossary/term/pebibyte  
   Verwendung: `PiB = 2^50 Byte`.

5. NIST CSRC Glossary - exbibyte  
   https://csrc.nist.gov/glossary/term/eib  
   Verwendung: `EiB = 2^60 Byte`.

6. NIST SP 811  
   https://physics.nist.gov/cuu/pdf/sp811.pdf  
   Verwendung: NIST-Standard-Hintergrund zu binären Präfixen.

Abgerufen: `2026-04-08`
