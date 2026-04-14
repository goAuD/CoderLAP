# Zeichencodierung

## Schneller visueller Überblick

| Ebene | Was bedeutet das? |
|---|---|
| Zeichen | vom Menschen lesbares Symbol, z.B. `A`, `é`, `€` |
| Codepunkt | abstrakter Identifikator, z.B. Unicode `U+00E9` |
| Kodierung | wie es in Bytes gespeichert wird, z.B. `UTF-8` |

## Was ist Zeichenkodierung?

Die Zeichenkodierung ist eine Zuordnung zwischen **Text** und **Bytes**.

Wenn dieselbe Bytefolge mit einer anderen Kodierung gelesen wird, kann der Text fehlerhaft sein.

Daher ist es wichtig, dass:

- die Datei tatsächlich in dieser Kodierung gespeichert ist
- das System sie korrekt erkennt
- die Webseite dies eindeutig angibt

## Warum ist das im Web wichtig?

Weil das Ergebnis einer falschen Kodierung ist:

- unleserliche Zeichen
- "Zeichensalat"
- fehlerhafte Datenverarbeitung
- Such-, Anzeige- oder Exportprobleme

In HTML häufige Angabe:

```html
<meta charset="utf-8" />
```

## Was bedeutet `UTF-8`?

`UTF-8` ist eine Zeichenkodierungsform von Unicode.

Vorteile:

- die meisten Schriftsysteme der Welt können damit verarbeitet werden
- im Web standardmäßig und empfohlen
- kompatibel mit den ersten 128 ASCII-Zeichen

## Was muss man unterscheiden?

| Begriff | Bedeutung |
|---|---|
| Zeichensatz | welche Zeichen existieren |
| Codepunkt | der abstrakte Identifikator des Zeichens |
| Zeichenkodierung | wie das Zeichen in Bytes gespeichert wird |

Beispiel:

- das Zeichen `é` ist ein Symbol
- in Unicode gibt es dafür einen Codepunkt
- `UTF-8` bestimmt, welche Bytefolge es repräsentiert

## Warum genügt es nicht, "einfach nur Text zu speichern"?

Weil der Computer wissen muss:

- mit welcher Kodierung gespeichert wurde
- wie es zurückgelesen werden soll

Wenn das Speichern und Lesen nicht mit derselben Kodierung erfolgt, wird das Ergebnis fehlerhaft.

## Nicht verwechseln

| Begriff | Was es nicht bedeutet |
|---|---|
| Unicode | ist nicht dasselbe wie die konkrete Byte-Kodierung |
| UTF-8 | ist nicht der Name jeder Textkodierung |
| ASCII | ist nicht für alle Sprachen geeignet |

## Worauf muss man achten?

- Bei neuen Webprojekten ist `UTF-8` die standardmäßig gute Wahl.
- Die Datei und die Deklaration müssen auf dieselbe Kodierung eingestellt sein.
- Bei älteren Systemen können Legacy-Kodierungen gemischt auftreten.
- Beim Datenaustausch und bei Import/Export ist die korrekte Kodierung besonders wichtig.

## Prüfungstaugliche Formulierung

> Die Zeichenkodierung bestimmt, wie die Zeichen eines Textes in Form von Bytes repräsentiert werden.  
> Im Web ist die moderne und empfohlene Lösung UTF-8,
> weil damit Zeichen vieler Sprachen einheitlich verarbeitet werden können
> und fehlerhafte Zeichendarstellung vermieden wird.  
> Die typische Folge einer falschen Kodierung ist verzerrter oder unleserlicher Text.

## Häufige Prüfungsfehler

- Unicode und UTF-8 als dasselbe bezeichnen.
- Behaupten, dass ASCII für jeden Text ausreicht.
- Nicht erwähnen, dass Kodierung eine Byte-Interpretationsregel ist.
- Die `charset`-Angabe im Web vergessen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche der Zeichenkodierung?
2. Warum ist `UTF-8` wichtig?
3. Was passiert bei falscher Kodierung?
4. Was ist der Unterschied zwischen Unicode und UTF-8?
5. Wie gibt man die empfohlene Kodierung in HTML an?

## Kurzantworten zur Selbstkontrolle

1. Die Zuordnung zwischen Text und Bytes
2. Weil es modern, einheitlich und mehrsprachig ist
3. Fehlerhafte Zeichendarstellung
4. Unicode ist das abstrakte System, UTF-8 ist die konkrete Kodierung
5. `<meta charset="utf-8" />`

## Quellen

1. MDN - Character encoding  
   https://developer.mozilla.org/en-US/docs/Glossary/Character_encoding  
   Verwendung: kurze, präzise Definition des Begriffs Zeichenkodierung.

2. WHATWG - Encoding Standard  
   https://encoding.spec.whatwg.org/  
   Verwendung: offizieller, aktueller Standard der Web-Zeichenkodierungen.

3. W3C International - Choosing & applying a character encoding  
   https://www.w3.org/International/questions/qa-choosing-encodings.en  
   Verwendung: praktischer, offizieller Leitfaden zur richtigen Kodierungswahl, insbesondere bei `UTF-8`.

Abgerufen: `2026-04-08`
