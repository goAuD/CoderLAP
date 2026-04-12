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

- lebt nur innerhalb einer Funktion oder Prozedur
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

## Prüfungstaugliche Formulierung

> Der Gültigkeitsbereich von Variablen bestimmt, in welchen Teilen des Programms eine bestimmte Variable erreichbar ist.  
> Man kann zum Beispiel von globalem, lokalem und blockbezogenem Scope sprechen.  
> Die korrekte Scope-Handhabung ist wichtig für die Fehlervermeidung, die Übersichtlichkeit und die Wartbarkeit.

## Häufige Prüfungsfehler

- Den Gültigkeitsbereich mit der Lebensdauer zu verwechseln.
- Zu behaupten, dass eine globale Variable immer gut ist, weil sie "überall sichtbar ist".
- Die Vorteile des lokalen Scopes nicht zu erwähnen.
- Scope und Datentyp zu vermischen.

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

1. MDN - Scope  
   https://developer.mozilla.org/en-US/docs/Glossary/Scope  
   Verwendung: offizielle, knappe Grundquelle zum Scope-Begriff.

2. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Verwendung: ergänzender Hintergrund zur praktischen Interpretation von Funktions- und lokalem Scope.

Abgerufen: `2026-04-09`
