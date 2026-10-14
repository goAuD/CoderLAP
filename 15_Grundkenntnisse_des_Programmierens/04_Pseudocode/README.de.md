# Pseudocode

## Schneller visueller Überblick

| Eigenschaft | Pseudocode |
|---|---|
| ausführbar? | nein |
| lesbar? | ja, das ist das Ziel |
| sprachabhängig? | nicht unbedingt |
| wofür gut? | Algorithmus-Entwurf und -Darstellung |

## Was ist Pseudocode?

Pseudocode ist eine Beschreibung, die:

- dem Programmcode ähnelt
- aber nicht streng an die Syntax einer bestimmten Sprache gebunden ist
- eher die Logik hervorhebt

Beispiel:

```text
LIES n
summe = 0
Schleife i = 1 bis n
  summe = summe + i
AUSGABE summe
```

## Warum ist das nützlich?

- damit lässt sich leicht ein Algorithmus entwerfen
- einfacher, eine Lösung zu besprechen
- man bleibt nicht bei sprachlichen Details hängen
- bei der Prüfung ein gut nutzbares Denkwerkzeug

## Pseudocode und echten Code: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Pseudocode | logische Beschreibung |
| Programmcode | konkrete, syntaktisch korrekte Umsetzung |

## Eigenschaften von gutem Pseudocode

- klar
- kurz
- logisch
- nachvollziehbar
- nicht zu technologie-abhängig

## Worauf muss man achten?

- nicht zu vage sein
- nicht mit konkreten sprachlichen Details vermischen, wenn nicht nötig
- die Reihenfolge der Schritte soll eindeutig sein

## Vom Pseudocode zur überprüfbaren Lösung

Aufgabe: Wir suchen das Maximum einer Liste endlicher Zahlen. Für eine leere
Liste lautet das Ergebnis „kein Wert“. Zuerst die sprachunabhängige Beschreibung:

```text
WENN die Liste leer ist: GIB kein Wert ZURÜCK
groesster = erstes Element
FÜR JEDES weitere Element:
  WENN Element größer als groesster:
    groesster = Element
GIB groesster ZURÜCK
```

Die entsprechende, eigenständig ausführbare JavaScript-Umsetzung:

<!-- example:run -->

```javascript
function maximum(values) {
  if (values.length === 0) return null;
  let largest = values[0];
  for (let i = 1; i < values.length; i++) {
    if (values[i] > largest) largest = values[i];
  }
  return largest;
}
console.log(maximum([-5, -2, -7]));
console.log(maximum([]));
```

```text
-2
null
```

Der Startwert ist `-5`, beim zweiten Element wird er zu `-2`; das dritte ändert
ihn nicht. Der Start mit dem ersten tatsächlichen Element funktioniert auch bei
negativen Zahlen. `null` steht hier vereinbarungsgemäß für „kein Ergebnis“, nicht
für die Zahl null. Bei der Umsetzung entscheiden wir bewusst über die
Indexierung (ab `0`), die Rückgabe und den leeren Fall. Pseudocode hat keine
einzige verbindliche Syntax. Deshalb verwenden wir unsere Schreibweise
einheitlich und kennzeichnen das Ende eines Zweigs durch Einrückung oder ein Abschlusswort.

## Prüfungstaugliche Formulierung

> Pseudocode ist eine codeähnliche, aber nicht ausführbare Beschreibung, die die Logik eines Algorithmus oder  
> Programmteils darstellt.  
> Sein Zweck ist es, sprachunabhängig und gut lesbar eine Lösung zu entwerfen oder zu erklären.  
> Pseudocode ist besonders nützlich bei der Darstellung von Algorithmen und bei Prüfungsaufgaben.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Pseudocode?
2. Warum ist er sprachunabhängig?
3. Wofür wird er verwendet?
4. Was ist der Unterschied zwischen Pseudocode und echtem Code?
5. Was macht guten Pseudocode aus?

## Kurzantworten zur Selbstkontrolle

1. Logische Beschreibung eines Algorithmus
2. Weil er nicht an die Regeln einer konkreten Sprache gebunden ist
3. Für Entwurf und Erklärung
4. Pseudocode ist nicht ausführbar
5. Klar und nachvollziehbar

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Pseudocode](https://developer.mozilla.org/en-US/docs/Glossary/Pseudocode): sprachunabhängige Beschreibung und Notation.


1. MDN - Pseudocode  
   https://developer.mozilla.org/en-US/docs/Glossary/Pseudocode  
   Verwendung: zeitgemäße, offizielle Begriffsdefinition zur Rolle von Pseudocode.

2. MDN - Algorithm  
   https://developer.mozilla.org/en-US/docs/Glossary/Algorithm  
   Verwendung: ergänzender Hintergrund zur Klärung der Beziehung zwischen Algorithmus und Pseudocode.

Abgerufen: `2026-04-09`
