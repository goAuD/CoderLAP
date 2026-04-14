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

## Prüfungstaugliche Formulierung

> JSON ist ein leichtes, textbasiertes Datenaustauschformat,
> das Daten mithilfe von Schlüssel-Wert-Paaren und Arrays beschreibt.  
> Es wird häufig in Web-APIs verwendet,
> weil es einfach, gut lesbar
> und von vielen Programmiersprachen leicht verarbeitbar ist.  
> In Standard-JSON müssen zum Beispiel Schlüssel in Anführungszeichen stehen,
> und Kommentare sind nicht verwendbar.

## Häufige Prüfungsfehler

- JSON als Programmiersprache bezeichnen.
- Es mit einem JavaScript-Objekt vollständig gleichsetzen.
- Kommentierte oder lockere Syntax als Standard-JSON bezeichnen.
- Die Verwendung in APIs nicht erwähnen.

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
