# Variable und Konstante

## Schneller visueller Überblick

| Begriff | Merkmal |
|---|---|
| Variable | kann einen neuen Wert erhalten |
| Konstante | Ziel ist eine feste Bindung oder ein fester Wert |

## Was ist eine Variable?

Eine Variable:

- speichert oder bezeichnet einen Wert
- hat einen Namen
- kann sich während der Programmausführung ändern

Beispiel:

```text
punktzahl = 10
punktzahl = punktzahl + 5
```

## Was ist eine Konstante?

Eine Konstante ist ein benanntes Element, dessen Wert oder Bindung nicht geändert werden soll.

Das kann sein:

- ein tatsächlich konstanter Wert
- oder je nach Sprache eine Bindung, die nicht neu zugewiesen werden kann

## Warum ist es nützlich, Konstanten zu verwenden?

- zeigt eine klarere Absicht
- verringert die Chance auf versehentliches Überschreiben
- macht den Code lesbarer
- bei der Wartung einfacher, feste Werte an einer Stelle zu ändern

## Wichtige moderne Präzisierung

In vielen Sprachen macht `const` oder eine ähnliche Lösung:

- das gesamte Objekt nicht unbedingt vollständig unveränderlich
- beschränkt eher die Bindung oder Neuzuweisung

Das kann bei der Prüfung Bonuspunkte bringen, wenn man es gut formuliert.

## Variable und Konstante: nicht verwechseln

| Aspekt | Variable | Konstante |
|---|---|---|
| Neuzuweisung | ja | in der Regel nein |
| Rolle | zur Laufzeit veränderliche Daten | feste Werte oder fixierte Bindung |
| Lesbarkeit | allgemein | verdeutlicht die Absicht |

## Bindung und Objektzustand getrennt verfolgen

Aufgabe: Wir zählen einen Versuch und tragen ein abgeschlossenes Thema in ein
Profil ein. Im Node.js-Beispiel erlaubt `let` eine Neuzuweisung; `const` fixiert die Bindung.

<!-- example:run -->

```javascript
let attempts = 0;
attempts += 1;
const profile = { name: "Ada", completed: 0 };
profile.completed += 1;
console.log(attempts, profile.completed);
const settings = Object.freeze({ maxAttempts: 3 });
console.log(settings.maxAttempts, Object.isFrozen(settings));
```

```text
1 1
3 true
```

`profile` verweist weiterhin auf dasselbe Objekt, während sich dessen Eigenschaft
`completed` ändert. `const` macht dieses Objekt also nicht unveränderlich. Ein
neues Objekt derselben Bindung `profile` zuzuweisen ist hingegen nicht erlaubt.
Wenn zwei Variablen auf dasselbe Objekt verweisen, sehen beide die Änderung einer Eigenschaft.

`Object.freeze` friert die eigenen Eigenschaften des angegebenen Objekts ein.
Das wirkt **flach**: Darin referenzierte weitere Objekte müssen gesondert
behandelt werden. Eine Konstante im Quelltext ist außerdem kein Geheimnis:
Ein an den Browser ausgelieferter API-Schlüssel wird durch `const` nicht vor
dem Besucher geschützt.

## Prüfungstaugliche Formulierung

> Eine Variable ist ein Programmierelement, dessen Wert sich während der Programmausführung ändern kann.  
> Eine Konstante hingegen ist ein Element, dessen Wert oder Bindung nicht geändert werden soll.  
> Die Verwendung von Konstanten erhöht die Lesbarkeit des Codes und verringert das Risiko versehentlicher Fehler, obwohl
> das genaue Verhalten je nach Sprache unterschiedlich sein kann.

## Schnelle Selbstkontrolle

1. Was ist eine Variable?
2. Was ist eine Konstante?
3. Warum ist es gut, Konstanten zu verwenden?
4. Warum muss man bei der Aussage "sie ändert sich nicht" vorsichtig formulieren?
5. In welchem Fall verwenden wir typischerweise Konstanten?

## Kurzantworten zur Selbstkontrolle

1. Ein Element mit zur Laufzeit veränderbarem Wert
2. Ein als fest gedachter Wert oder eine feste Bindung
3. Weil es saubereren und sichereren Code ergibt
4. Weil die genaue Regel je nach Sprache unterschiedlich ist
5. Für feste Konfigurations- oder konstante Werte

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze): flache Unveränderlichkeit.


1. MDN - const  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const  
   Verwendung: offizielle, moderne Quelle zur genauen Interpretation der konstanten Bindung.

2. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Verwendung: Hintergrundquelle zu den Grundbegriffen von Variablen und Werten.

Abgerufen: `2026-04-09`
