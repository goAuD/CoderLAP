# Sortieralgorithmen: Bubblesort / Quicksort

## Schneller visueller Überblick

| Algorithmus | Grundprinzip | Typische Leistung |
|---|---|---|
| Bubble Sort | Vertauschen benachbarter Elemente | schwach bei großen Listen |
| Quick Sort | Aufteilung um Pivot, dann rekursive Sortierung | in der Regel schnell |

## Was ist Bubble Sort?

`Bubble Sort` funktioniert so:

- geht die Liste durch
- vergleicht benachbarte Elemente
- tauscht sie, wenn sie in falscher Reihenfolge sind
- wiederholt dies, bis kein Tausch mehr nötig ist

Das ist einfach und gut lehrbar, aber bei großen Datenmengen nicht effizient.

## Was ist Quick Sort?

Die Grundidee von `Quick Sort`:

- wählt ein Element, das ist der `Pivot`
- gruppiert die Elemente im Verhältnis zum Pivot
- zwischen kleineren und größeren Elementen stehen die pivotgleichen Werte
- sortiert dann die Teile rekursiv

Das ist typischerweise ein viel schnellerer Ansatz.

## Ausgearbeitete Beispiele in JavaScript

Aufgabe: Sortiere die Zahlen des Arrays `[4, 2, 4, 1]` aufsteigend.
Die Beispiele erwarten ein Array endlicher Zahlen und liefern ein neues sortiertes
Array; die Eingabe bleibt unverändert. Jeder JavaScript-Block lässt sich in eine
eigene Datei kopieren und beispielsweise mit `node beispiel.js` in einer
installierten Node.js-Umgebung ausführen.

### Bubble Sort: benachbarte Elemente vergleichen

```javascript
function bubbleSort(values) {
  const result = [...values];
  for (let end = result.length - 1; end > 0; end--) {
    let swapped = false;
    for (let index = 0; index < end; index++) {
      if (result[index] > result[index + 1]) {
        const previous = result[index];
        result[index] = result[index + 1];
        result[index + 1] = previous;
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
  return result;
}

console.log(JSON.stringify(bubbleSort([4, 2, 4, 1])));
```

Ausgabe:

```text
[1,2,4,4]
```

`[...values]` erstellt eine Kopie. Die innere Schleife untersucht zwei benachbarte
Zahlen: Ist die linke größer, tauscht sie beide mithilfe der temporären Variablen
`previous`. `JSON.stringify` stellt das Array als einheitlichen Text dar.

| Durchlauf | Anfangszustand | Zustand am Ende |
|---|---|---|
| 1., `end = 3` | `[4, 2, 4, 1]` | `[2, 4, 1, 4]` |
| 2., `end = 2` | `[2, 4, 1, 4]` | `[2, 1, 4, 4]` |
| 3., `end = 1` | `[2, 1, 4, 4]` | `[1, 2, 4, 4]` |

Jeder Durchlauf bringt das größte Element des untersuchten Bereichs an dessen
Ende. Deshalb wird die Grenze `end` um eins verringert. Erfolgt in einem ganzen
Durchlauf kein Tausch, ist das Array bereits sortiert; `break` beendet die äußere
Schleife. Bei leeren und einelementigen Arrays wird die Kopie direkt zurückgegeben.

### Quick Sort: Aufteilung und Rekursion

Diese Lernvariante sammelt kleinere, gleiche und größere Werte in drei getrennten
Arrays. Die Gruppe gleicher Elemente erhält auch mehrfach vorkommende Zahlen.

```javascript
function quickSort(values) {
  if (values.length <= 1) {
    return [...values];
  }
  const pivot = values[0];
  const smaller = [];
  const equal = [];
  const larger = [];
  for (const value of values) {
    if (value < pivot) {
      smaller.push(value);
    } else if (value > pivot) {
      larger.push(value);
    } else {
      equal.push(value);
    }
  }
  return [...quickSort(smaller), ...equal, ...quickSort(larger)];
}

console.log(JSON.stringify(quickSort([4, 2, 4, 1])));
```

Ausgabe:

```text
[1,2,4,4]
```

Der erste Pivot ist 4: `smaller = [2, 1]`, `equal = [4, 4]`, `larger = []`.
Im Teil `[2, 1]` ist der Pivot 2; es entstehen `[1]`, `[2]` und `[]`.
Leere und einelementige Teile sind bereits sortiert: Das ist der **Basisfall**.
Das Zusammenfügen liefert zuerst `[1, 2]`, dann `[1, 2, 4, 4]`.

Der Pivot und die pivotgleichen Elemente gehen in keinen weiteren rekursiven
Aufruf ein. So wird der bearbeitete Teil kleiner. Diese anschauliche Variante
legt zusätzliche Arrays an; es gibt auch direkt im Eingabearray arbeitende
Quick-Sort-Varianten. Hier dient das erste Element als Pivot: Bei bereits
sortierten, unterschiedlichen Werten kann das unausgewogene Aufteilungen und
`O(n^2)` Laufzeit ergeben. Bei großen Eingaben begrenzt auch die Größe des
Aufrufstapels der Laufzeitumgebung die Rekursionstiefe.

## Effizienz kurz gefasst

| Algorithmus | Typische Zeitkomplexität |
|---|---|
| Bubble Sort | allgemein und im schlechtesten Fall `O(n^2)`; obige Variante bei sortierter Eingabe `O(n)` |
| Quick Sort | durchschnittlich `O(n log n)` bei entsprechender Eingabeverteilung oder Pivotwahl; schlechtestenfalls `O(n^2)` |

Anmerkung:

- der Worst-Case von `Quick Sort` kann `O(n^2)` sein
- in der Praxis ist er aber in der Regel deutlich besser als `Bubble Sort`

## Wann sollte man was wissen?

### Bubble Sort

- gut zum Lernen
- leicht zu verstehen
- für reale Projekte bei größeren Daten selten ideal

### Quick Sort

- wichtiger klassischer Algorithmus
- schnell
- erfordert Rekursion und Aufteilungsdenken

## Prüfungstaugliche Formulierung

> Bubble Sort ist ein einfacher Sortieralgorithmus, der die Liste durch wiederholtes Vergleichen und Tauschen  
> benachbarter Elemente sortiert.  
> Quick Sort hingegen teilt die Daten um ein Pivot-Element auf und sortiert die Teile rekursiv.  
> Quick Sort ist in der Praxis in der Regel deutlich effizienter, während Bubble Sort eher zu Lernzwecken nützlich ist.

## Schnelle Selbstkontrolle

1. Warum darf `end` nach jedem Bubble-Sort-Durchlauf kleiner werden?
2. Was bewirkt `swapped = false` am Ende eines ganzen Durchlaufs?
3. In welche Gruppe kommen die beiden 4er im Quick-Sort-Beispiel?
4. Was ist der Basisfall der Rekursion, und warum wird er erreicht?
5. Was liefern beide Funktionen für `[]` und `[7]`?

## Kurzantworten zur Selbstkontrolle

1. Das größte Element des untersuchten Bereichs steht danach an seiner endgültigen Position.
2. `break` beendet die Sortierung, weil alle untersuchten Nachbarpaare passend geordnet sind.
3. In `equal`; beide Vorkommen bleiben erhalten.
4. Ein Array mit höchstens einem Element. Die kleinere und größere Gruppe sind jeweils kürzer als der ursprüngliche Teil.
5. Neue Arrays `[]` beziehungsweise `[7]`; die Eingabe bleibt unverändert.

## Quellen

1. NIST DADS - bubble sort  
   https://xlinux.nist.gov/dads/HTML/bubblesort.html  
   Verwendung: offizielle Definition und Komplexitätshintergrund zu `Bubble Sort`.

2. NIST DADS - quicksort  
   https://xlinux.nist.gov/dads/HTML/quicksort.html  
   Verwendung: offizielle Definition und Leistungshintergrund zu `Quick Sort`.

Abgerufen: `2026-09-11`
