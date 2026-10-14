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

## Zeichen, Codeeinheit und Byte: drei unterschiedliche Längen

**Aufgabe:** Den Text `Aő🙂` in UTF-8-Bytes kodieren und zurücklesen.
Das Beispiel läuft in aktuellem Node.js und in der Browserkonsole:

<!-- example:run -->

```javascript
const text = "Aő🙂";
const bytes = new TextEncoder().encode(text);
console.log(text.length, [...text].length, bytes.length);
console.log([...bytes].map((byte) => byte.toString(16).padStart(2, "0")).join(" "));
console.log(new TextDecoder("utf-8", { fatal: true }).decode(bytes));
console.log("é" === "é");
console.log("é" === "é".normalize("NFC"));
```

```text
4 3 7
41 c5 91 f0 9f 99 82
Aő🙂
false
true
```

Der Text besteht aus drei Unicode-Codepunkten. JavaScripts `length` zählt
jedoch UTF-16-Codeeinheiten. Das Emoji benötigt zwei, daher ist das Ergebnis `4`.
In UTF-8 belegt `A` ein Byte, `ő` zwei und das Emoji vier, zusammen `7`.
`TextEncoder` erzeugt UTF-8; der Decoder stellt daraus den Text wieder her.
`fatal: true` fordert bei ungültigen Eingabebytes eine Ausnahme statt eines
Ersatzzeichens.

`é` kann aus einem Codepunkt oder aus `e` und einem kombinierenden Akzent bestehen.
Die letzten beiden Zeilen zeigen: Rohzeichenfolgen können verschieden sein und
nach NFC-Normalisierung übereinstimmen. Die Anzahl sichtbarer Zeichen kann sogar
von der Codepunktanzahl abweichen, etwa bei zusammengesetzten Emojis.

Die Schriftart ist eine andere Ebene. Auch bei korrekten Bytes kann ein Zeichen
fehlen, wenn die Schrift keinen passenden Glyphen enthält. Ein Wechsel der
Zeichenkodierung löst dieses Darstellungsproblem nicht.

## Prüfungstaugliche Formulierung

> Die Zeichenkodierung bestimmt, wie die Zeichen eines Textes in Form von Bytes repräsentiert werden.  
> Im Web ist die moderne und empfohlene Lösung UTF-8,
> weil damit Zeichen vieler Sprachen einheitlich verarbeitet werden können
> und fehlerhafte Zeichendarstellung vermieden wird.  
> Die typische Folge einer falschen Kodierung ist verzerrter oder unleserlicher Text.

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

Geprüft: `2026-10-14`.

- [MDN: TextEncoder](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder): Erzeugen von UTF-8-Bytes.
- [WHATWG: Encoding](https://encoding.spec.whatwg.org/): Dekodierung und Fehlerbehandlung.
- [MDN: String.normalize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize): Unicode-Normalisierung.


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
