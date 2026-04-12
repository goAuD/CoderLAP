# Gigabyte, Terabyte, Petabyte, Exabyte

## Schneller visueller Überblick

| Einheit  | Bezeichnung |  Faktor |                       In Byte |
| -------- | ----------- | ------: | ----------------------------: |
| Gigabyte | `GB`        |  `10^9` |             `1 000 000 000 B` |
| Terabyte | `TB`        | `10^12` |         `1 000 000 000 000 B` |
| Petabyte | `PB`        | `10^15` |     `1 000 000 000 000 000 B` |
| Exabyte  | `EB`        | `10^18` | `1 000 000 000 000 000 000 B` |

### Einfache Eselsbrücke

Jeder neue Schritt:

- `× 1000`

Also:

- `1 TB = 1000 GB`
- `1 PB = 1000 TB`
- `1 EB = 1000 PB`

## Was bedeuten diese Einheiten?

Diese Maßeinheiten dienen dazu, sehr große Datenmengen kürzer und übersichtlicher darzustellen.

Zum Beispiel:

- ein kleines Dokument ist einige `KB`
- ein Bild ist einige `MB`
- ein Film oder Spiel ist mehrere `GB`
- ein größerer Datenträger ist mehrere `TB`
- Unternehmens- oder Cloud-Datenmengen können den `PB`- oder `EB`-Bereich erreichen

## Warum sind sie dezimal (Basis 10)?

Die Namen `Giga`, `Tera`, `Peta`, `Exa` stammen von den **SI-Präfixen**.

Das bedeutet:

- `Giga = 10^9`
- `Tera = 10^12`
- `Peta = 10^15`
- `Exa = 10^18`

Daher wachsen die Einheiten `GB`, `TB`, `PB`, `EB` **nicht in 1024er-**, sondern in **1000er-Schritten**.

## Wo werden sie in der Praxis verwendet?

### 1. Speicherangaben von Herstellern und Marketing

Festplattenhersteller verwenden häufig dezimale Einheiten.

Beispiel:

- `1 TB` SSD = `1 000 000 000 000 Byte`

Das ist technisch korrekt, wird aber oft mit binären Einheiten verwechselt.

### 2. Cloud-Dienste und Rechenzentren

Bei großen Datenmengen kommen häufig vor:

- `TB`
- `PB`
- `EB`

Zum Beispiel:

- Backup-Systeme
- Log-Speicherung
- Videoplattformen
- KI-Datensätze

### 3. Netzwerk- und Geschäftskommunikation

In Berichten, Verträgen und Dienstbeschreibungen werden ebenfalls häufig dezimale Einheiten verwendet.

## GB und GiB: nicht verwechseln

| Einheit | Bedeutung         |             Wert in Byte |
| ------- | ----------------- | -----------------------: |
| `GB`    | Gigabyte, dezimal | `10^9 = 1 000 000 000 B` |
| `GiB`   | Gibibyte, binär   | `2^30 = 1 073 741 824 B` |

Dasselbe gilt bei größeren Einheiten:

| Dezimal | Binär |
| ------- | ----- |
| `TB`    | `TiB` |
| `PB`    | `PiB` |
| `EB`    | `EiB` |

Dieser Unterschied ist wichtig, weil dieselbe Festplatte je nachdem,
ob das System dezimale oder binäre Einheiten verwendet,
unterschiedlich groß angezeigt werden kann.

## Schnelle Beispiele

### Beispiel 1

`2 TB` =

- `2 × 10^12 B`
- `2 000 000 000 000 Byte`

### Beispiel 2

`3 PB` =

- `3 × 10^15 B`
- `3 000 000 000 000 000 Byte`

### Beispiel 3

`1 EB` =

- `10^18 B`
- `1 000 000 000 000 000 000 Byte`

## Warum ist das prüfungsrelevant?

Weil hier oft abgefragt wird:

- korrekte Bedeutung der Maßeinheiten
- `B` als Byte
- der Unterschied zwischen dezimalen und binären Präfixen
- die scheinbare Abweichung bei Speicherangaben

## Prüfungstaugliche Formulierung

> Gigabyte, Terabyte, Petabyte und Exabyte sind dezimale Byte-Einheiten zur Bezeichnung großer Datenmengen.  
> Sie basieren auf SI-Präfixen und wachsen daher in 1000er-Schritten.  
> Zum Beispiel: 1 GB = 10^9 Byte, 1 TB = 10^12 Byte, 1 PB = 10^15 Byte, 1 EB = 10^18 Byte.  
> Wichtig: Diese sind nicht identisch mit den binären Einheiten GiB, TiB, PiB und EiB.

## Häufige Prüfungsfehler

- Zu sagen, dass `1 GB = 1024 MB`.
- Die Bedeutung von `GB` und `GiB` zu verwechseln.
- Zu vergessen, dass `B` hier Byte bedeutet.
- Zu glauben, dass jedes Betriebssystem den Speicher gleich anzeigt.
- Nicht zu wissen, dass `Giga`, `Tera`, `Peta`, `Exa` SI-Präfixe sind.

## Schnelle Selbstkontrolle

1. Wie viel ist `1 GB` in Byte?
2. Wie viel ist `1 TB` in Byte?
3. Ist `GB` zehnerbasisert oder zweierbasisert?
4. Was ist der Unterschied zwischen `GB` und `GiB`?
5. Wie viel ist `1 EB` in Byte?

## Kurzantworten zur Selbstkontrolle

1. `1 000 000 000 Byte`
2. `1 000 000 000 000 Byte`
3. **Zehnerbasisert**
4. `GB` ist dezimal (`10^9`), `GiB` ist binär (`2^30`)
5. `1 000 000 000 000 000 000 Byte`

## Quellen

1. BIPM - SI prefixes  
   https://www.bipm.org/en/measurement-units/si-prefixes  
   Verwendung: offizielle Werte der SI-Präfixe `Giga`, `Tera`, `Peta`, `Exa`.

2. SI Brochure - BIPM  
   https://www.bipm.org/en/publications/si-brochure/  
   Verwendung: offizielle Hintergrundregeln der SI-Präfixe.

3. NIST IR 8289 - Quantities and Units for Software Product Measurements  
   https://doi.org/10.6028/NIST.IR.8289  
   Verwendung: technische Verwendung der Bezeichnung `Byte` und `B`.

4. NIST - Definitions of the SI units: The binary prefixes  
   https://physics.nist.gov/cgi-bin/cuu/Info/Units/binary.html  
   Verwendung: klare Trennung von dezimalen und binären Datengrößen.

Abgerufen: `2026-04-08`
