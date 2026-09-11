# Schleifen

## Schneller visueller Überblick

| Schleifentyp | Wann gut? |
|---|---|
| `for` | wenn wir wissen, wie viele Wiederholungen nötig sind |
| `while` | wenn wir auf Basis einer Bedingung wiederholen |
| `do...while` | wenn die Schleife mindestens einmal laufen soll |
| `for...of` in JavaScript | zum Verarbeiten der Werte einer iterierbaren Folge |

## Was ist eine Schleife?

Das Wesentliche einer Schleife ist:

- man muss denselben Code nicht mehrfach hinschreiben
- das Programm wiederholt die Operation
- solange eine Bedingung erfüllt ist
- oder bis alle Elemente durchlaufen sind

## Warum ist das wichtig?

- ergibt kürzeren und saubereren Code
- leichter wartbar
- ermöglicht effizientere Lösungen bei wiederholenden Operationen

## Ausgearbeitete Beispiele in JavaScript

Jeder Codeblock läuft eigenständig: Speichere ihn beispielsweise als `beispiel.js`
und starte ihn mit `node beispiel.js` in einer installierten Node.js-Umgebung.
`console.log` schreibt in die Ausgabe. Sage zuerst das Ergebnis voraus und führe
den Code anschließend aus.

### Zählen mit `for`

Aufgabe: Gib die Zahlen 1, 2 und 3 jeweils in einer eigenen Zeile aus.

```javascript
for (let number = 1; number <= 3; number++) {
  console.log(number);
}
```

Ausgabe:

```text
1
2
3
```

Der Kopf enthält Startwert (`let number = 1`), Fortsetzungsbedingung
(`number <= 3`) und Aktualisierung (`number++`). Der Startwert wird einmal gesetzt;
die Bedingung wird vor jedem Durchlauf, die Aktualisierung nach jedem Schleifenkörper
ausgeführt.

| `number` bei der Prüfung | `number <= 3` | Was passiert? |
|---|---|---|
| 1 | wahr | 1 ausgeben, dann auf 2 erhöhen |
| 2 | wahr | 2 ausgeben, dann auf 3 erhöhen |
| 3 | wahr | 3 ausgeben, dann auf 4 erhöhen |
| 4 | falsch | Ausführung nach der Schleife fortsetzen |

### Zustand verfolgen mit `while`

Aufgabe: Starte mit drei verbleibenden Runden und verringere ihre Anzahl nach
jeder Runde.

```javascript
let remaining = 3;
while (remaining > 0) {
  console.log(remaining);
  remaining--;
}
```

Ausgabe:

```text
3
2
1
```

`remaining` verändert sich im Schleifenkörper. Bei 0 ist die Bedingung falsch,
und die Schleife endet. `while` lässt sich auch verwenden, wenn der Startzustand
etwa aus einem Funktionsparameter stammt: Über die Fortsetzung entscheidet
immer der aktuelle Zustand.

### Zeitpunkt der Prüfung: `while` und `do...while`

Aufgabe: Beobachte die Anzahl der Durchläufe, wenn die Bedingung bereits zu
Beginn falsch ist. `runs++` zählt jeweils einen Durchlauf.

```javascript
let runs = 0;
while (runs < 0) {
  runs++;
}
console.log(runs);

runs = 0;
do {
  runs++;
} while (runs < 0);
console.log(runs);
```

Ausgabe:

```text
0
1
```

`while` prüft zuerst; hier entstehen 0 Durchläufe. `do...while` führt zuerst den
Schleifenkörper aus und prüft anschließend; hier entsteht 1 Durchlauf. Das Beispiel
macht gezielt diese beiden Prüfzeitpunkte sichtbar.

### Werte durchlaufen mit `for...of`

Aufgabe: Addiere die Punkte eines Arrays mit drei Elementen.

```javascript
const scores = [3, 5, 7];
let total = 0;
for (const score of scores) {
  total += score;
}
console.log(total);
```

Ausgabe:

```text
15
```

`score` erhält nacheinander die Werte 3, 5 und 7. Die Summe entwickelt sich als
0 → 3 → 8 → 15. Bei einem leeren Array gibt es 0 Durchläufe; die Summe bleibt 0.

## Schleife und Rekursion im Vergleich

| Begriff | Kern |
|---|---|
| Schleife | Wiederholung mit Kontrollstruktur |
| Rekursion | Wiederholung durch Selbstaufruf einer Funktion |

## Prüfungstaugliche Formulierung

> Eine Schleife ist eine Kontrollstruktur, die eine Anweisung oder einen Anweisungsblock mehrmals ausführt.  
> Die Ausführung wird in der Regel durch eine Bedingung, einen Zähler oder eine zu durchlaufende Elementfolge  
> gesteuert.  
> Ziel der Schleifen ist die Reduzierung von Codewiederholung und die effiziente Behandlung wiederholender Aufgaben.

## Schnelle Selbstkontrolle

1. Wie oft läuft der Schleifenkörper im ersten Beispiel, und wie oft wird die Bedingung geprüft?
2. Welchen Wert hat `remaining` am Ende des `while`-Beispiels?
3. Warum eignet sich `do...while` für eine Operation, die auf jeden Fall einmal ausgeführt wird?
4. Was gibt das Summenbeispiel aus, wenn `scores` den Wert `[]` hat?
5. Welche Operation wiederholt die Arbeit bei Rekursion?

## Kurzantworten zur Selbstkontrolle

1. 3 Durchläufe und 4 Bedingungsprüfungen, zuletzt beim Wert 4.
2. 0; dann ist die Bedingung `remaining > 0` falsch.
3. Der Schleifenkörper steht vor der ersten Prüfung und läuft deshalb mindestens einmal.
4. 0: Die Summe beginnt bei 0, und es gibt kein zu verarbeitendes Element.
5. Der Selbstaufruf der Funktion; bei einer Schleife wiederholt die Kontrollstruktur den Schleifenkörper.

## Quellen

1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Verwendung: offizielle, moderne Quelle zur Funktionsweise und zu den Typen von Schleifen.

2. MDN - Control flow  
   https://developer.mozilla.org/en-US/docs/Glossary/Control_flow  
   Verwendung: Hintergrundquelle zum größeren Kontext der Kontrollstrukturen.

Abgerufen: `2026-09-11`
