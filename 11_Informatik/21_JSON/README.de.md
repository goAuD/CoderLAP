# JSON

## Schneller visueller Überblick

| Typ | Beispiel |
|---|---|
| Objekt | `{ "name": "Anna" }` |
| Array | `[1, 2, 3]` |
| Schlüssel-Wert | `"age": 21` |

## Was ist JSON?

JSON ist ein sprachunabhängiges Datenaustauschformat,
das aus der JavaScript-Objektnotation hervorgegangen ist,
aber heute von vielen Programmiersprachen verwendet wird.

Es wird häufig eingesetzt bei:

- Antworten von REST APIs
- Konfigurationen
- Datenaustausch zwischen Frontend und Backend
- dateibasierten Datenstrukturen

## Grundaufbau

Die zwei grundlegenden Strukturelemente von JSON sind:

- Objekt
- Array

Beispiel:

```json
{
  "id": 42,
  "name": "Anna",
  "active": true,
  "roles": ["user", "editor"]
}
```

## Welche Werttypen sind möglich?

- String
- Number
- Object
- Array
- Boolean
- `null`

## Warum ist es beliebt?

- einfach
- gut lesbar
- breit unterstützt
- leicht zu parsen
- in Webumgebungen sehr praktisch

## JSON und JavaScript-Objekt: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| JSON | striktes Datenaustauschformat |
| JavaScript-Objekt | Datenstruktur der Programmiersprache |

Wichtige Unterschiede:

- JSON ist Text
- Schlüssel müssen in Anführungszeichen stehen
- Kommentare sind nicht Teil von Standard-JSON

## Worauf muss man achten?

- In Standard-JSON gibt es keine Kommentare.
- Ein überflüssiges Trailing Comma ist nicht erlaubt.
- JSON ist an sich nur Daten, kein Verhalten.
- Bei fehlerhafter Syntax schlägt die Verarbeitung fehl.

## JSON und XML: nicht verwechseln

| Aspekt | JSON | XML |
|---|---|---|
| Art | leichtes Datenaustauschformat | Auszeichnungssprache |
| Lesbarkeit | oft einfacher | oft ausführlicher |
| typisches heutiges Web-API | sehr häufig | seltener, aber kommt noch vor |

## Parsen, prüfen und serialisieren

**Aufgabe:** Zu einem Thema wird eine ganzzahlige Punktzahl von `0..5` eingelesen.
JSON-Syntax und Anwendungsanforderung sind getrennte Prüfungen. In Node.js ausführbar:

<!-- example:run -->

```javascript
function parseProgress(text) {
  const value = JSON.parse(text);
  if (value === null || Array.isArray(value) || typeof value !== "object" ||
      typeof value.topic !== "string" || !Number.isInteger(value.score) ||
      value.score < 0 || value.score > 5) {
    throw new Error("Invalid progress");
  }
  return { topic: value.topic, score: value.score };
}
const progress = parseProgress('{"topic":"loops","score":4}');
console.log(progress.topic, progress.score + 1);
console.log(JSON.stringify(progress));
for (const text of ['null', '{"topic":"loops","score":"4"}']) {
  try {
    parseProgress(text);
  } catch (error) {
    console.log(error.message);
  }
}
```

```text
loops 5
{"topic":"loops","score":4}
Invalid progress
Invalid progress
```

`JSON.parse` erzeugt aus Text einen Laufzeitwert. `JSON.stringify` übernimmt die
umgekehrte Richtung. Die Punktzahl ist eine addierbare Zahl. `"4"` ist hingegen
ein String und wird vom gewählten Vertrag abgelehnt. `null` ist gültiges JSON,
aber nicht der erwartete Datensatz. Wir verarbeiten Daten, statt sie mit `eval`
als Code auszuführen.

Der oberste JSON-Wert muss kein Objekt oder Array sein; auch eine Zahl, ein
Wahrheitswert oder `null` sind möglich. Objektschlüssel und Texte verwenden
doppelte Anführungszeichen. `undefined`, Funktionen und `BigInt` sind keine
JSON-Werttypen. Das Übertragungsformat eines Datums wird gesondert vereinbart,
häufig als String im ISO-Format.

Die Zahlendarstellung der empfangenden Sprache kann die Genauigkeit begrenzen.
Große exakte Identifikatoren werden daher häufig als String übertragen.
Schlüsselnamen sollen innerhalb eines Objekts eindeutig sein, da Systeme
wiederholte Namen unterschiedlich behandeln können.

## Prüfungstaugliche Formulierung

> JSON ist ein leichtes, textbasiertes Datenaustauschformat,
> das Daten mithilfe von Schlüssel-Wert-Paaren und Arrays beschreibt.  
> Es wird häufig in Web-APIs verwendet,
> weil es einfach, gut lesbar
> und von vielen Programmiersprachen leicht verarbeitbar ist.  
> In Standard-JSON müssen zum Beispiel Schlüssel in Anführungszeichen stehen,
> und Kommentare sind nicht verwendbar.

## Schnelle Selbstkontrolle

1. Wofür wird JSON häufig verwendet?
2. Was sind die zwei grundlegenden Strukturelemente?
3. Was ist der Unterschied zwischen JSON und einem JavaScript-Objekt?
4. Kann es Kommentare in Standard-JSON geben?
5. Warum ist es im Web beliebt?

## Kurzantworten zur Selbstkontrolle

1. Für den Datenaustausch
2. Objekt und Array
3. JSON ist ein Textformat, das Objekt ist eine Laufzeit-Datenstruktur
4. Nein
5. Weil es einfach und breit unterstützt ist

## Quellen

Geprüft: `2026-10-14`.

- [IETF: JSON RFC8259](https://www.rfc-editor.org/rfc/rfc8259): Werttypen, eindeutige Schlüssel und Interoperabilität.
- [MDN: JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse): vom Text zum Laufzeitwert.


1. RFC 8259 - The JavaScript Object Notation (JSON) Data Interchange Format  
   https://www.rfc-editor.org/rfc/rfc8259  
   Verwendung: die offizielle, standardisierte Beschreibung von JSON.

2. MDN - JSON  
   https://developer.mozilla.org/en-US/docs/Glossary/JSON  
   Verwendung: kurze, entwicklerfreundliche Definition und Kontext.

3. ECMA-404 - The JSON Data Interchange Syntax  
   https://ecma-international.org/publications-and-standards/standards/ecma-404/  
   Verwendung: Standardhintergrund zur JSON-Syntax.

Abgerufen: `2026-04-08`
