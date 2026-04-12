# Schleifen

## Schneller visueller Überblick

| Schleifentyp | Wann gut? |
|---|---|
| `for` | wenn wir wissen, wie viele Wiederholungen nötig sind |
| `while` | wenn wir auf Basis einer Bedingung wiederholen |
| `do...while` | wenn die Schleife mindestens einmal laufen soll |
| `for...each`-artig | zum Durchlaufen von Elementen |

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

## Typische Schleifen

### `for`

Gut, wenn:

- wir zählen
- wir in einem bekannten Bereich arbeiten
- wir indexbasiert vorgehen

### `while`

Gut, wenn:

- wir vorher nicht wissen, wie viele Wiederholungen nötig sind
- solange eine Bedingung wahr ist

### `do...while`

Gut, wenn:

- der Schleifenkörper mindestens einmal sicher laufen soll

## Worauf muss man achten?

- die Abbruchbedingung muss korrekt sein
- die Schleife darf nicht endlos laufen
- der Zähler oder Zustand muss entsprechend aktualisiert werden

## Schleife und Rekursion: nicht verwechseln

| Begriff | Kern |
|---|---|
| Schleife | Wiederholung mit Kontrollstruktur |
| Rekursion | Wiederholung durch Selbstaufruf einer Funktion |

## Prüfungstaugliche Formulierung

> Eine Schleife ist eine Kontrollstruktur, die eine Anweisung oder einen Anweisungsblock mehrmals ausführt.  
> Die Ausführung wird in der Regel durch eine Bedingung, einen Zähler oder eine zu durchlaufende Elementfolge gesteuert.  
> Ziel der Schleifen ist die Reduzierung von Codewiederholung und die effiziente Behandlung wiederholender Aufgaben.

## Häufige Prüfungsfehler

- Die Abbruchbedingung nicht zu erwähnen.
- Den Unterschied zwischen `while` und `do...while` auszulassen.
- Zu glauben, dass eine Schleife immer aus einer bekannten Anzahl von Wiederholungen besteht.
- Die Gefahr einer Endlosschleife nicht zu nennen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche einer Schleife?
2. Wofür ist die `for`-Schleife gut?
3. Wann ist `while` besser?
4. Warum ist eine fehlerhafte Abbruchbedingung gefährlich?
5. Was ist der Unterschied zwischen Schleife und Rekursion?

## Kurzantworten zur Selbstkontrolle

1. Wiederholte Ausführung
2. Bei bekannter Wiederholungsanzahl oder Zählung
3. Wenn die Wiederholung bedingungsbasiert ist
4. Weil es zu einer Endlosschleife führen kann
5. Die Schleife ist eine Kontrollstruktur, die Rekursion ein Selbstaufruf

## Quellen

1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Verwendung: offizielle, moderne Quelle zur Funktionsweise und zu den Typen von Schleifen.

2. MDN - Control flow  
   https://developer.mozilla.org/en-US/docs/Glossary/Control_flow  
   Verwendung: Hintergrundquelle zum größeren Kontext der Kontrollstrukturen.

Abgerufen: `2026-04-09`
