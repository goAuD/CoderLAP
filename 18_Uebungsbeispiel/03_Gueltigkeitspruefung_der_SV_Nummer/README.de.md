# Gueltigkeitspruefung der SV-Nummer

## Schneller visueller Überblick

```text
L L L P T T M M J J

L L L   = Laufnummer
P       = Prüfziffer
T T M M J J = Geburtsdatum oder fingiertes Datum
```

## Offizielle Prüfziffer-Logik

Gemäß der offiziellen österreichischen Beschreibung:

- Die Gewichte der drei Laufnummer-Ziffern: `3`, `7`, `9`
- Die Gewichte des `TTMMJJ`-Teils: `5`, `8`, `4`, `2`, `1`, `6`
- Der Rest der Summe `mod 11` ergibt die Prüfziffer
- Wenn der Rest `10` ist, kann die Nummer in dieser Form nicht verwendet werden

## Was sollte man in der Lösung prüfen?

- Nur Ziffern enthalten
- `10` Ziffern lang
- Prüfziffer stimmt
- Der Datumsteil ist zumindest formal plausibel

## Beispiele aus der PDF

### Gültig

- `4422 180599`
- `3567 010705`
- `5884 050902`

### Ungültig

- `2511 010100`
- `5255 121299`
- `4999 070700`

## Prüfungstaugliche Formulierung

> Bei der Gültigkeitsprüfung der österreichischen `SV-Nr` müssen das Format der Nummer und die offizielle Prüfziffer-Logik überprüft werden.  
> Die ersten drei Laufnummer-Ziffern und der `TTMMJJ`-Teil werden mit bestimmten Gewichten multipliziert, und dann wird der Rest der Summe bei Division durch `11` mit der Prüfziffer an der `4.` Position verglichen.  
> Wenn die Prüfung nicht übereinstimmt, ist die Nummer ungültig.

## Häufige Prüfungsfehler

- Falsche Ziffernpositionen für die Multiplikation verwenden.
- Die Prüfziffer von der falschen Stelle ablesen.
- Die Leerzeichen vor der Verarbeitung nicht entfernen.
- Nicht mit den in der PDF angegebenen Beispielnummern testen.

## Quellen

1. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135  
   Verwendung: Primäre offizielle Quelle für die Prüfziffer-Logik.

2. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Verwendung: Für die Beispielnummern und die Aufgabenerwartung.

Abgerufen: `2026-04-09`
