# Variablenarten, Datentypen, Definitionen

## Schneller visueller Überblick

| Begriff | Bedeutung |
|---|---|
| Variable | über einen Namen erreichbare Daten |
| Datentyp | Zahl, Text, logischer Wert usw. |
| Deklaration | wir sagen, dass sie existiert |
| Initialisierung | wir geben einen Anfangswert |

## Was ist eine Variable?

Eine Variable ist ein Programmierelement, das:

- auf einen Wert verweist
- einen Namen hat
- während der Programmausführung verwendet werden kann

Je nach Sprache kann die Variable:

- direkt einen Wert speichern
- oder auf ein Objekt / einen Speicherbereich verweisen

## Was ist ein Datentyp?

Der Datentyp bestimmt:

- welche Art von Daten wir speichern
- welche Operationen darauf ausgeführt werden können
- worauf man formell achten muss

## Typische Datentypen

| Typ | Beispiel |
|---|---|
| Ganzzahl | `42` |
| Gleitkommazahl | `3.14` |
| Logisch | `true`, `false` |
| Zeichen / Text | `'A'`, `"hello"` |
| Zusammengesetzter Typ | Liste, Array, Objekt |

## Variablenarten kurz gefasst

Das kann auf verschiedene Weisen interpretiert werden:

- einfache und zusammengesetzte Datentypen
- lokale und globale Variablen
- veränderbare und nicht veränderbare Bindungen

Da die konkreten Details je nach Sprache unterschiedlich sind, sollte man bei der Prüfung den begrifflichen Kern sicher
beherrschen.

## Deklaration, Definition, Initialisierung

Dies ist eine wichtige Unterscheidung bei der Prüfung.

| Begriff | Einfache Bedeutung |
|---|---|
| Deklaration | wir geben den Namen / die Existenz der Variable an |
| Definition | tatsächliche Festlegung der Entität; genaue Bedeutung ist sprachabhängig |
| Initialisierung | Vergabe eines Anfangswerts |

Anmerkung:

- die genaue sprachliche Bedeutung kann zwischen `C`, `JavaScript`, `Python` oder anderen Sprachen unterschiedlich sein
- bei der Prüfung ist die Grundidee das Wichtige

## Warum ist der Datentyp wichtig?

- hilft Fehler zu vermeiden
- bestimmt die Operationen
- kann den Speicherverbrauch und das Verhalten beeinflussen

## Präzisierung am JavaScript-Beispiel

`let count;` erzeugt die Bindung; nach Ausführung der Deklaration hat sie den
Wert `undefined`. Das folgende `count = 3` ist eine Zuweisung. Bei
`const enabled = true` erfolgen Deklaration und Initialisierung gemeinsam.
Die genaue Bedeutung von „Definition“ hängt von der Sprache ab; der Begriff ist
kein allgemeines Synonym für Zuweisung.

<!-- example:run -->

```javascript
let count;
console.log(typeof count);
count = 3;
const enabled = true;
const label = "3";
console.log(typeof count, typeof enabled, typeof label);
console.log(count === Number(label));
console.log(Number.isFinite(Number("unknown")));
```

```text
undefined
number boolean string
true
false
```

Das Beispiel läuft in Node.js. In JavaScript sind `3` und `3.14` beide `number`;
es gibt keinen separaten allgemeinen `int`-Typ. `bigint`, etwa `3n`, ist ein
eigener Ganzzahltyp. Gemeinsames Rechnen mit `number` erfordert bewusste
Konvertierung. Text ist `string`, wahr/falsch ist `boolean`. `null` kann einen
bewusst gewählten leeren Wert ausdrücken, `undefined` beispielsweise einen
fehlenden Wert.

Bei dynamischer Typisierung kann eine Variable später einen Wert anderen Typs
erhalten; die Werte besitzen trotzdem Typen. `Number("unknown")` ergibt `NaN`,
daher folgt auf Konvertierung eine Prüfung. `Number.isFinite` akzeptiert weder
Unendlichkeit noch `NaN`. Für Geldbeträge eignen sich ganze Cent oder ein
geeignetes Dezimalverfahren besser als binäre Gleitkommarechnung ohne festgelegte Rundung.

## Prüfungstaugliche Formulierung

> Eine Variable ist ein mit einem Namen versehenes Programmierelement, das einen Wert oder einen darauf zeigenden  
> Verweis bezeichnet.  
> Der Datentyp bestimmt, welche Art von Daten wir verarbeiten und welche Operationen darauf ausgeführt werden können.  
> In der Programmierung ist es wichtig, Deklaration, Definition und Initialisierung zu unterscheiden, auch wenn deren
> genaue Bedeutung je nach Sprache unterschiedlich sein kann.

## Schnelle Selbstkontrolle

1. Was ist eine Variable?
2. Was ist ein Datentyp?
3. Nenne vier grundlegende Datentypen.
4. Was ist Initialisierung?
5. Warum kann die genaue Terminologie je nach Sprache unterschiedlich sein?

## Kurzantworten zur Selbstkontrolle

1. Über einen Namen erreichbare Daten oder Verweis
2. Die Beschreibung der Art der Daten
3. Ganzzahl, Gleitkomma, logisch, Text
4. Vergabe eines Anfangswerts
5. Weil die Sprachen sie unterschiedlich definieren

## Quellen

Geprüft: `2026-10-14`.

- [MDN: JavaScript data types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures): sprachspezifische Typen und Konvertierung.


1. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Verwendung: offizielle, moderne Quelle zu Datentypen und Variablengrundlagen.

2. MDN - Statements and declarations  
   https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements  
   Verwendung: gut nutzbarer Hintergrund zum Verständnis von Deklaration und Sprachstrukturen.

Abgerufen: `2026-04-09`
