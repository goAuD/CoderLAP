# ASCII-Tabellen

## Schneller visueller Überblick

| Zeichen | Dezimalcode | Hex |
|---|---|---|
| `A` | `65` | `41` |
| `a` | `97` | `61` |
| `0` | `48` | `30` |
| Leerzeichen | `32` | `20` |

## Was ist die Rolle der ASCII-Tabelle?

Die ASCII-Tabelle hilft zu verstehen:

- wie aus einem Zeichen eine Zahl wird
- wie der Computer Text speichert
- wie bestimmte Umwandlungen auf niedrigerer Ebene funktionieren

In der Programmierung kann sie nützlich sein, zum Beispiel:

- bei der Untersuchung von Zeichencodes
- bei einfacher Textverarbeitung
- bei der Interpretation von Protokollen und Dateiformaten

## Welche Zeichen sind enthalten?

### Steuerzeichen

Zum Beispiel:

- Zeilenumbruch
- Tab
- Wagenrücklauf

### Druckbare Zeichen

Zum Beispiel:

- Buchstaben
- Ziffern
- Satzzeichen

## ASCII und Unicode: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| ASCII | 7 Bit, 128 Zeichen |
| Unicode | viel größerer Zeichensatz |

Die meisten modernen Systeme verwenden heute Unicode, aber die Grundlagen von ASCII sind weiterhin wichtig.

## Warum ist das heute noch nützlich?

- viele technische Dokumentationen bauen darauf auf
- zeigt gut die Grundlogik der Zeichencodes
- in der Programmierung begegnen wir häufig ASCII-kompatiblen Begriffen

## Zeichencode und Zahlenwert in der Praxis

Ausführbares Node.js-Beispiel: `"7"` ist Text aus einer Ziffer. Wir betrachten
den Code und nutzen danach den zusammenhängenden ASCII-Ziffernbereich für den Zahlenwert.

<!-- example:run -->

```javascript
const digit = "7";
const code = digit.codePointAt(0);
console.log(code);
console.log(code - "0".codePointAt(0));
console.log(String.fromCodePoint(65));
console.log("\n".codePointAt(0));
```

```text
55
7
A
10
```

`55` ist der Code des Zeichens `7`, während `7` dessen Zahlenwert ist. Die
Subtraktion liefert nur für ein zuvor geprüftes Zeichen aus `"0".."9"` einen
sinnvollen Ziffernwert. Für allgemeine Textumwandlung verwenden wir geeignete
Konvertierungsfunktionen zusammen mit Eingabeprüfung.

LF (`10`, hex `0A`) und CR (`13`, hex `0D`) sind verschiedene Steuerzeichen.
Das bei Windows-Textdateien häufige CRLF besteht aus zwei Zeichen. `codePointAt`
liefert einen Unicode-Codepunkt; im Bereich `0..127` stimmt dieser mit ASCII
überein. `ő` und Emoji gehören nicht zu ASCII. Zur Interpretation der Bytes einer
Textdatei müssen wir zusätzlich deren Zeichenkodierung kennen.

## Prüfungstaugliche Formulierung

> Die ASCII-Tabelle zeigt die numerischen Codes, die den Zeichen des ASCII-Zeichensatzes zugeordnet sind.  
> ASCII ist eine 7-Bit-Zeichenkodierung, die 128 Zeichen umfasst, darunter Steuerzeichen und druckbare Zeichen.  
> Obwohl heute hauptsächlich Unicode-basierte Systeme verwendet werden, bleibt ASCII von grundlegender Bedeutung für das
> Verständnis der Zeichenkodierung.

## Schnelle Selbstkontrolle

1. Wie viele Zeichen deckt ASCII ab?
2. Warum ist eine ASCII-Tabelle nützlich?
3. Nenne zwei Beispiele für ASCII-Codes.
4. Was ist der Unterschied zwischen ASCII und Unicode?
5. Warum ist ASCII auch heute noch wichtig?

## Kurzantworten zur Selbstkontrolle

1. `128`
2. Weil sie die Zeichen-Code-Zuordnung zeigt
3. `A = 65`, `0 = 48`
4. Unicode ist ein viel größerer Zeichensatz
5. Weil viele Grundbegriffe darauf aufbauen

## Quellen

Geprüft: `2026-10-14`.

- [MDN: String.codePointAt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt): Unicode-Codepunkte abfragen.
- [IETF RFC 20](https://www.ietf.org/rfc/rfc20.txt): ASCII-Codewerte, LF und CR.


1. MDN - ASCII  
   https://developer.mozilla.org/en-US/docs/Glossary/ASCII  
   Verwendung: moderne, offizielle Zusammenfassung zum ASCII-Begriff.

2. IETF RFC 20  
   https://www.ietf.org/rfc/rfc20.txt  
   Verwendung: historische Primärquelle zum ASCII-Zeichensatz.

Abgerufen: `2026-04-09`
