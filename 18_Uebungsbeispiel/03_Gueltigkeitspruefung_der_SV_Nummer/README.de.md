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

- Nach Entfernen erlaubten Leerraums nur Ziffern enthalten
- Laufnummer zwischen `100–999`
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

## Schritt für Schritt: Prüfziffer von 4422 180599

Die vierte Ziffer ist `2`; mit ihr vergleichen wir den berechneten Rest.
Die gewichtete Summe der übrigen Ziffern lautet:

```text
4×3 + 4×7 + 2×9 + 1×5 + 8×8 + 0×4 + 5×2 + 9×1 + 9×6
= 200
200 mod 11 = 2
```

Das folgende eigenständig in Node.js ausführbare Beispiel lässt die vierte Stelle
durch das Gewicht null aus. Dieser Teil prüft **Format und Prüfziffer**;
den Datumsteil prüft eine eigene Funktion der vollständigen Musterlösung.

<!-- example:run -->
```javascript
function hasMatchingCheckDigit(rawValue) {
  const digits = rawValue.replace(/\s/g, "");
  if (!/^[1-9]\d{9}$/.test(digits)) return false;
  const weights = [3, 7, 9, 0, 5, 8, 4, 2, 1, 6];
  const sum = [...digits].reduce((total, digit, index) => {
    return total + Number(digit) * weights[index];
  }, 0);
  const remainder = sum % 11;
  return remainder !== 10 && remainder === Number(digits[3]);
}

console.log(hasMatchingCheckDigit("4422 180599"));
console.log(hasMatchingCheckDigit("2511 010100"));
console.log(hasMatchingCheckDigit("4422x180599"));
```

```text
true
false
false
```

Erlaubten Leerraum entfernen wir; Buchstaben und andere falsche Zeichen bleiben erhalten,
damit die Formatprüfung sie erkennt. Die erste Ziffer der Laufnummer ist nicht null.
Beim Rest `10` gibt es keine passende einstellige Prüfziffer.

## Datumsteil und Grenzen der Prüfung

Bei üblichen Monaten `01–12` prüfen wir auf einen möglichen Kalendertag.
Die offizielle Beschreibung erlaubt auch fingierte Monate (`13, 14, 15, …`).
Eine allgemeine Geburtstagsprüfung ersetzt deshalb nicht die SV-Logik.
Das zweistellige Jahr enthält kein Jahrhundert. Die Musterlösung prüft die kalendarische
Möglichkeit mit einem Jahr aus 1900 und 2000, bestimmt aber kein Alter.

Auch mit passender Prüfziffer und zulässigem Datumsteil stellen wir nur **formale Übereinstimmung** fest.
Die tatsächliche Vergabe und den Versicherungsschutz prüft diese Offline-Aufgabe nicht.

Quellen: unten angeführtes Dachverband-Dokument, Kapitel D.61, Seiten 40–41;
[Sozialversicherung: Aufbau der Versicherungsnummer](https://www.sozialversicherung.gv.at/cdscontent/?contentid=10007.820902).
Geprüft: `2026-10-14`.

## Prüfungstaugliche Formulierung

> Bei der Gültigkeitsprüfung der österreichischen `SV-Nr` müssen das Format der Nummer und die offizielle  
> Prüfziffer-Logik überprüft werden.  
> Die ersten drei Laufnummer-Ziffern und der `TTMMJJ`-Teil werden mit bestimmten Gewichten multipliziert, und dann  
> wird der Rest der Summe bei Division durch `11` mit der Prüfziffer an der `4.` Position verglichen.  
> Wenn die Prüfung nicht übereinstimmt, ist die Nummer ungültig.

## Schnelle Selbstkontrolle

1. An welcher Position steht die Prüfziffer?
2. Was geschieht beim Rest zehn?
3. Warum behandeln wir den Datumsteil gesondert?

## Kurzantworten zur Selbstkontrolle

1. An vierter Stelle, in JavaScript Index 3.
2. Für diese Ziffernfolge gibt es keine verwendbare einstellige Prüfziffer.
3. Fingierte Monate sind möglich, und das zweistellige Jahr enthält kein Jahrhundert.

## Quellen

1. Dachverband der österreichischen Sozialversicherung - offizielle Beschreibung der Versicherungsnummer  
   https://www.sozialversicherung.at/cdscontent/load?contentid=10008.796428&version=1750403135  
   Verwendung: Primäre offizielle Quelle für die Prüfziffer-Logik.

2. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Verwendung: Für die Beispielnummern und die Aufgabenerwartung.

Abgerufen: `2026-04-09`
