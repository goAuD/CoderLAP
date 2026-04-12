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
- teilt die übrigen Elemente in zwei Teile
- auf eine Seite kommen die kleineren, auf die andere die größeren
- sortiert dann die Teile rekursiv

Das ist typischerweise ein viel schnellerer Ansatz.

## Einfacher Funktionsunterschied

### Bubble Sort

```text
Vergleich benachbarter Elemente
-> Tausch
-> erneuter Durchlauf
```

### Quick Sort

```text
Pivot auswählen
-> Aufteilung in kleineren / größeren Teil
-> rekursive Sortierung
```

## Effizienz kurz gefasst

| Algorithmus | Typische Zeitkomplexität |
|---|---|
| Bubble Sort | typischerweise `O(n^2)` |
| Quick Sort | typischerweise `O(n log n)` |

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

> Bubble Sort ist ein einfacher Sortieralgorithmus, der die Liste durch wiederholtes Vergleichen und Tauschen benachbarter Elemente sortiert.  
> Quick Sort hingegen teilt die Daten um ein Pivot-Element auf und sortiert die Teile rekursiv.  
> Quick Sort ist in der Praxis in der Regel deutlich effizienter, während Bubble Sort eher zu Lernzwecken nützlich ist.

## Häufige Prüfungsfehler

- Zu behaupten, dass Bubble Sort schnell ist.
- Die Rolle des Pivots bei Quick Sort nicht zu erwähnen.
- Zu vergessen, dass Quick Sort häufig rekursiv ist.
- Das Funktionsprinzip mit der exakten Code-Implementierung zu verwechseln.

## Schnelle Selbstkontrolle

1. Wie funktioniert Bubble Sort?
2. Was ist der Pivot bei Quick Sort?
3. Welcher ist in der Regel schneller?
4. Warum wird Bubble Sort trotzdem gelehrt?
5. Welche Denkweise erfordert Quick Sort?

## Kurzantworten zur Selbstkontrolle

1. Er sortiert durch Vertauschen benachbarter Elemente
2. Ein ausgewähltes Element, um das die Liste aufgeteilt wird
3. In der Regel Quick Sort
4. Weil er einfach und anschaulich ist
5. Aufteilungs- und rekursives Denken

## Quellen

1. NIST DADS - bubble sort  
   https://xlinux.nist.gov/dads/HTML/bubblesort.html  
   Verwendung: offizielle Definition und Komplexitätshintergrund zu `Bubble Sort`.

2. NIST DADS - quicksort  
   https://xlinux.nist.gov/dads/HTML/quicksort.html  
   Verwendung: offizielle Definition und Leistungshintergrund zu `Quick Sort`.

Abgerufen: `2026-04-09`
