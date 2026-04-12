# Einheiten Bit und Byte

## Schneller visueller Überblick

| Einheit  | Bezeichnung | Bedeutung      | Mögliche Werte |
| -------- | ----------- | -------------- | -------------- |
| **Bit**  | `b`         | 1 Binärziffer  | `0` oder `1`   |
| **Byte** | `B`         | 8 Bit zusammen | `0-255`        |

### Zusammenhang

| Ausdruck | Bedeutung                                                  |
| -------- | ---------------------------------------------------------- |
| `1 Bit`  | ein einzelner Binärwert                                    |
| `4 Bit`  | halbes Byte, entspricht oft 1 Hexadezimalziffer            |
| `8 Bit`  | `1 Byte`                                                   |
| `2^8`    | `256`, so viele verschiedene Werte kann ein Byte speichern |

## Was ist ein Bit?

**Bit** ist die Abkürzung für `binary digit`.  
Es ist der grundlegendste Baustein von Computerdaten.

Ein Bit kann nur zwei Zustände ausdrücken:

- `0`
- `1`

Das kann zum Beispiel Folgendes bedeuten:

- ja / nein
- ein / aus
- wahr / falsch
- vorhanden / nicht vorhanden

Einfaches Beispiel:

- eine Lampe **ausgeschaltet** = `0`
- eine Lampe **eingeschaltet** = `1`

## Was ist ein Byte?

Ein **Byte** besteht aus 8 Bit.

Da jedes Bit zwei mögliche Werte haben kann, ergeben 8 Bit zusammen:

`2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 2^8 = 256`

Daher kann ein Byte **256 verschiedene Muster** darstellen.

Beispiele für Byte-Werte:

- `00000000` = `0`
- `00000001` = `1`
- `11111111` = `255`

Hexadezimal wird ein Byte häufig so dargestellt:

- `00`
- `2D`
- `7F`
- `FF`

Ein Byte kann also:

- eine kleine Zahl speichern
- einen Zeichencode speichern
- Teil eines größeren Datenwerts sein

## Warum sind Bit und Byte wichtig?

Weil in der digitalen Welt praktisch alle Daten daraus aufgebaut sind:

- Text
- Bilder
- Ton
- Video
- Programmcode
- Datenbanken

Wer den Unterschied zwischen Bit und Byte versteht, versteht leichter:

- Dateigrößen
- Speicherverbrauch
- Netzwerkgeschwindigkeit
- Zeichenkodierung
- Binäre und hexadezimale Darstellung

## Wo begegnet man ihnen in der Praxis?

### 1. Dateigröße und Speicherplatz

Diese werden in der Regel in **Byte** gemessen:

- `25 B`
- `4 KB`
- `12 MB`
- `256 GB`

Zum Beispiel:

- eine kurze Textdatei kann einige Hundert Byte groß sein
- ein Bild kann mehrere Megabyte groß sein
- eine SSD kann mehrere Hundert Gigabyte haben

### 2. Datenübertragungsgeschwindigkeit

Diese wird häufig in **Bit pro Sekunde** angegeben:

- `Mbps` = Megabit pro Sekunde
- `Gbps` = Gigabit pro Sekunde

Beispiel:

- `100 Mbps` Internetgeschwindigkeit ist nicht dasselbe wie `100 MB/s`

Denn:

- `1 B = 8 b`

deshalb:

- `100 MB/s = 800 Mb/s`

Das ist einer der wichtigsten praktischen Unterschiede.

### 3. Zeichen und Text

Früher galt oft, dass ein Zeichen ungefähr einem Byte entsprach, aber heute stimmt das **nicht immer**.

Bei modernen Kodierungen, zum Beispiel `UTF-8`:

- manche Zeichen sind `1 Byte`
- andere Zeichen sind `2-4 Byte`

Deshalb ist die Aussage falsch, dass:

> 1 Zeichen immer 1 Byte ist.

## `b` und `B`: nicht verwechseln

| Bezeichnung | Bedeutung |
| ----------- | --------- |
| `b`         | Bit       |
| `B`         | Byte      |

Das ist nicht nur ein orthografisches Detail, sondern kann einen **achtfachen Unterschied** bedeuten.

Beispiel:

- `8 b = 1 B`
- `10 MB` = `80 Mb`

Bei Prüfungen wird das sehr oft verwechselt.

## Schnelle Beispiele

| Beispiel           | Bedeutung                                  |
| ------------------ | ------------------------------------------ |
| `1 Bit`            | `0` oder `1`                               |
| `1 Byte`           | 8 Bit                                      |
| `1 Byte`           | 256 mögliche Werte                         |
| `64-Bit`-Prozessor | Architektur, die mit 64-Bit-Daten arbeitet |
| `100 Mbps`         | Netzwerkgeschwindigkeit in Bit angegeben   |
| `20 MB` Datei      | Dateigröße in Byte-basierter Einheit       |

## Worauf muss man achten

- **Bit** und **Byte** sind nicht dasselbe.
- Das Verwechseln von `b` und `B` kann zu ernsthaften Fehlern führen.
- Ein **Byte ist heute in der Praxis 8 Bit**, aber historisch gab es auch abweichende Lösungen.
- Nicht jedes Zeichen passt in 1 Byte.
- Die größeren Einheiten (`KB`, `MB`, `GB` bzw. `KiB`, `MiB`, `GiB`) gehören zu einem eigenen Themenbereich.

## Prüfungstaugliche Formulierung

> Das Bit ist die kleinste Einheit der digitalen Information, sein Wert kann 0 oder 1 sein.  
> Ein Byte besteht aus 8 Bit und kann daher 256 verschiedene Werte darstellen.  
> Bytes werden hauptsächlich zur Messung von Speicherplatz und Dateigrößen
> verwendet, während Bits häufig bei Datenübertragungsgeschwindigkeiten
> vorkommen.  
> Ein wichtiger Unterschied ist, dass `b` für Bit und `B` für Byte steht.

## Häufige Prüfungsfehler

- Zu sagen, dass Bit und Byte dasselbe sind.
- Zu vergessen, dass `1 Byte = 8 Bit`.
- Die Bezeichnungen `b` und `B` zu verwechseln.
- Zu behaupten, dass jedes Zeichen immer 1 Byte ist.
- Dieses Thema mit den Themen `KB / MB / GB` und `KiB / MiB / GiB` zu vermischen.

## Schnelle Selbstkontrolle

1. Was ist ein Bit?
2. Aus wie vielen Bits besteht ein Byte?
3. Wie viele verschiedene Werte kann ein Byte annehmen?
4. Was wird häufiger für Dateigrößen verwendet: Bit oder Byte?
5. Was bedeutet `b` und was bedeutet `B`?
6. Warum sind `100 Mbps` und `100 MB/s` nicht dasselbe?

## Kurzantworten zur Selbstkontrolle

1. Die kleinste Einheit digitaler Information, Wert `0` oder `1`
2. **8 Bit**
3. **256**
4. **Byte**
5. `b` = Bit, `B` = Byte
6. Weil `1 Byte = 8 Bit`, daher ist `100 MB/s = 800 Mbps`

## Quellen

1. NIST IR 8289 - Quantities and Units for Software Product Measurements  
   https://doi.org/10.6028/NIST.IR.8289  
   Verwendung: technische Verwendung der Bezeichnung `Byte` und `B`.

2. NIST - Definitions of the SI units: The binary prefixes  
   https://physics.nist.gov/cgi-bin/cuu/Info/Units/binary.html  
   Verwendung: klare Trennung von dezimalen und binären Datengrößen.

3. MDN Web Docs - UTF-8  
   https://developer.mozilla.org/en-US/docs/Glossary/UTF-8  
   Verwendung: Klärung, warum ein Zeichen mehrere Bytes umfassen kann.

4. W3C - Character encodings: Essential concepts  
   https://www.w3.org/International/articles/definitions-characters/index.en  
   Verwendung: Grundbegriffe zu Zeichen und Bytes.

Abgerufen: `2026-04-08`
