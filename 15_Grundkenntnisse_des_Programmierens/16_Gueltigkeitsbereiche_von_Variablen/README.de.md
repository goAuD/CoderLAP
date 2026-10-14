# Gueltigkeitsbereiche von Variablen

## Schneller visueller Überblick

| Scope-Typ | Wo erreichbar? |
|---|---|
| global | in großen Teilen des Programms |
| lokal / funktionsbezogen | nur innerhalb einer Funktion |
| blockbezogen | nur in einem bestimmten Block, z.B. innerhalb von `if` oder einer Schleife |

## Was ist ein Gültigkeitsbereich?

Der Gültigkeitsbereich bedeutet:

- wo die Variable erstellt wurde
- welche Codeteile darauf zugreifen können
- wo sie sicher verwendet werden kann

## Warum ist das wichtig?

- hilft Namenskollisionen zu vermeiden
- verringert die Chance auf versehentliches Überschreiben
- macht das Programm übersichtlicher
- erleichtert die Fehlersuche

## Typische Scopes

### Global

- von vielen Stellen aus erreichbar
- kann bequem erscheinen
- kann aber die Fehleranfälligkeit erhöhen

### Lokal

- der Name ist innerhalb einer Funktion oder Prozedur sichtbar
- besser kontrollierbar

### Blockbezogen

- ist nur innerhalb eines bestimmten `{}`-Blocks sichtbar
- in modernen Sprachen und bei modernen Sprachelementen häufig

## Gültigkeitsbereich und Lebensdauer: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Gültigkeitsbereich | wo die Variable erreichbar ist |
| Lebensdauer | wie lange die Variable existiert |

Die beiden hängen zusammen, sind aber nicht dasselbe.

## Warum sind zu viele globale Variablen problematisch?

- es wird schwieriger, den Programmzustand zu verfolgen
- leichter, sie versehentlich zu ändern
- schwächt den modularen Aufbau

## Gültigkeitsbereich und Lebensdauer mit einer Closure

Das folgende Node.js-Beispiel erzeugt zwei unabhängige Zähler:

<!-- example:run -->

```javascript
function createCounter() {
  let count = 0;
  return function next() {
    count += 1;
    return count;
  };
}
const first = createCounter();
const second = createCounter();
console.log(first(), first(), second());
```

```text
1 2 1
```

`count` ist direkt nur in der erzeugenden Funktion und deren innerer Funktion
sichtbar. Die zurückgegebene Funktion `next` behält Zugriff auf ihre Umgebung;
das nennen wir **Closure**. Die ersten beiden Aufrufe erhöhen denselben Zähler.
`second` stammt aus einer eigenen Erzeugung und beginnt deshalb bei 1.

`createCounter` ist bereits zurückgekehrt, der innere Zustand bleibt über die
zurückgegebene Funktion dennoch erreichbar. Das zeigt den Unterschied zwischen
Gültigkeitsbereich und Lebensdauer. In JavaScript haben `let` und `const`
Block-Scope, `var` hat Funktions-Scope. Ein innerer Bereich darf äußere Namen
verwenden; eine gleichnamige innere Deklaration verdeckt den äußeren Namen.
In einem ES-Modul gehört eine Variable auf oberster Ebene zum Modul und ist
nicht automatisch eine globale Variable aller anderen Dateien.

## Prüfungstaugliche Formulierung

> Der Gültigkeitsbereich von Variablen bestimmt, in welchen Teilen des Programms eine bestimmte Variable erreichbar  
> ist.  
> Man kann zum Beispiel von globalem, lokalem und blockbezogenem Scope sprechen.  
> Die korrekte Scope-Handhabung ist wichtig für die Fehlervermeidung, die Übersichtlichkeit und die Wartbarkeit.

## Schnelle Selbstkontrolle

1. Was bedeutet der Gültigkeitsbereich einer Variable?
2. Was ist der Unterschied zwischen globalem und lokalem Scope?
3. Warum ist es gefährlich, viele globale Variablen zu verwenden?
4. Was ist der blockbezogene Scope?
5. Was ist der Unterschied zwischen Scope und Lebensdauer?

## Kurzantworten zur Selbstkontrolle

1. Wo die Variable erreichbar ist
2. Die eine ist von vielen Stellen sichtbar, die andere nur lokal
3. Weil es schwerer zu verfolgen und leichter zu überschreiben ist
4. Wenn die Variable nur in einem bestimmten Block erreichbar ist
5. Das eine ist die Sichtbarkeit, das andere die Existenzdauer

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures): lexikalische Umgebung und erhaltener Zustand.


1. MDN - Scope  
   https://developer.mozilla.org/en-US/docs/Glossary/Scope  
   Verwendung: offizielle, knappe Grundquelle zum Scope-Begriff.

2. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Verwendung: ergänzender Hintergrund zur praktischen Interpretation von Funktions- und lokalem Scope.

Abgerufen: `2026-04-09`
