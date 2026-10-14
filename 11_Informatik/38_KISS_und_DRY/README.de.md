# KISS und DRY

## Schneller visueller Überblick

| Prinzip | Wesentlich |
|---|---|
| KISS | suche die einfachste, verständliche Lösung |
| DRY | reduziere Duplikation, fasse gemeinsame Logik zusammen |

## Was ist KISS?

Das KISS-Prinzip besagt, dass die Lösung:

- einfach sein soll
- gut verständlich sein soll
- frei von unnötiger Komplexität sein soll

Das bedeutet nicht, dass sie primitiv sein soll, sondern dass man:

- nicht überplanen soll
- keine unbegründeten Abstraktionen einführen soll
- kein Problem im Voraus lösen soll, das noch gar nicht existiert

## Was ist DRY?

Das DRY-Prinzip besagt, dass Logik nicht unnötig an mehreren Stellen wiederholt werden soll.

Wenn dieselbe Regel an mehreren Stellen vorkommt, entsteht leicht:

- Fehlerpotenzial
- schwierige Wartung
- inkonsistentes Verhalten

## Warum sind sie zusammen wichtig?

Weil guter Code gleichzeitig:

- einfach ist
- nicht unnötig wiederholt

Aber Achtung:

- DRY übertrieben kann manchmal zu überkomplizierter Abstraktion führen

Daher ist Gleichgewicht nötig.

## Praktische Beispiele

### KISS-Beispiel

Eine einfache `if`-Lösung kann besser sein als ein überplantes Muster-System, wenn das Problem klein ist.

### DRY-Beispiel

Wenn dieselbe Berechnung oder Validierung an drei Stellen vorkommt, lohnt es sich, sie in eine gemeinsame Funktion auszulagern.

## KISS und DRY: nicht verwechseln

| Prinzip | Worauf achtet es? |
|---|---|
| KISS | Reduzierung von Komplexität |
| DRY | Reduzierung von Wiederholung |

## Worauf muss man achten?

- Zu viele Abstraktionen können das KISS-Prinzip verletzen.
- Copy-Paste verstößt typischerweise gegen das DRY-Prinzip.
- Nicht jede Ähnlichkeit ist eine echte Duplikation.
- Manchmal ist eine kleine Wiederholung verständlicher als eine schlechte Abstraktion.

## Dasselbe Wissen gehört an einen gemeinsamen Ort

DRY bedeutet **Don't Repeat Yourself**. Es minimiert nicht die Zahl der
Tastenanschläge, sondern vermeidet mehrere unabhängig veränderbare Umsetzungen
derselben Regel. KISS wird üblicherweise als **Keep It Simple, Stupid**, höflicher
auch als **Keep It Simple and Straightforward** ausgeschrieben. Gemeint ist
begründete Einfachheit, nicht möglichst kurzer Code.

**Eigene Übungsregel, keine offizielle LAP-Punktegrenze:** Bei einem Quiz mit
zehn Punkten ist das Ergebnis ab 6 Punkten erfolgreich. Ergebnisansicht und
Zusammenfassung verwenden dieselbe Regel. Die gemeinsame Funktion läuft in Node.js:

<!-- example:run -->

```javascript
function isPassingScore(score) {
  if (!Number.isInteger(score) || score < 0 || score > 10) {
    throw new RangeError("score must be an integer from 0 to 10");
  }
  return score >= 6;
}

console.log(isPassingScore(5));
console.log(isPassingScore(6));
console.log(isPassingScore(10));
```

```text
false
true
true
```

5 liegt unterhalb, 6 genau auf der Grenze und 10 am erlaubten Maximum. Ändert
sich die Regel, ändern wir diese Funktion und die erwarteten Testwerte. Der
Name erklärt die Absicht, die Bedingung ist direkt lesbar. Dafür brauchen wir
noch keine allgemeine Regel-Engine oder Vererbungshierarchie.

Auch eine Liste könnte gerade 6 Karten pro Seite anzeigen. Das ist aber eine
andere Regel mit einem anderen Änderungsgrund. Wir koppeln sie nicht nur wegen
derselben Zahl an die Quizgrenze. Notwendige Sicherheitsprüfungen in Client
und Server entfallen ebenfalls nicht zur „Duplikationsvermeidung“: Der Server
prüft seine Eingaben immer selbst. **YAGNI** ergänzt diese Sicht: Wir bauen
die nachweislich benötigte Fähigkeit und erfüllen dabei die aktuellen
Anforderungen vollständig.

## Prüfungstaugliche Formulierung

> Das KISS-Prinzip besagt,
> dass die Lösung einfach und gut verständlich sein soll,
> wobei unnötige Komplexität vermieden wird.
> Das DRY-Prinzip besagt,
> dass dieselbe Logik nicht unnötig an mehreren Stellen wiederholt werden soll,
> sondern in eine gemeinsame Abstraktion
> oder Funktion ausgelagert werden soll.
> In guter Entwicklung sollten beide Prinzipien gemeinsam und im Gleichgewicht angewendet werden.

## Schnelle Selbstkontrolle

1. Was bedeutet KISS?
2. Was bedeutet DRY?
3. Warum ist Duplikation gefährlich?
4. Warum kann übermäßige Abstraktion ein Problem sein?
5. Wie hängen die beiden Prinzipien zusammen?

## Kurzantworten zur Selbstkontrolle

1. Halte die Lösung einfach
2. Wiederhole die Logik nicht unnötig
3. Weil sie Fehler und schwierige Wartung verursacht
4. Weil sie die Verständlichkeit verschlechtert
5. Zusammen helfen sie bei sauberem Code

## Quellen

Geprüft: `2026-10-14`.

- [The Pragmatic Programmer: Tips](https://pragprog.com/tips/): Autorenquelle für DRY sowie einfache, veränderbare Lösungen.


1. DevIQ - Keep It Simple
   https://deviq.com/principles/keep-it-simple/
   Verwendung: kurze, fachliche Erklärung des KISS-Prinzips.

2. DevIQ - Don't Repeat Yourself
   https://deviq.com/principles/dont-repeat-yourself/
   Verwendung: ergänzende fachliche Erklärung des DRY-Prinzips, keine Norm.

3. DevIQ - Once and Only Once
   https://deviq.com/principles/once-and-only-once/
   Verwendung: ergänzende Erklärung zum DRY-Prinzip.

Abgerufen: `2026-04-08`
