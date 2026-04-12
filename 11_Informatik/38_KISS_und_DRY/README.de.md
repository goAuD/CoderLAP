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

## Prüfungstaugliche Formulierung

> Das KISS-Prinzip besagt, dass die Lösung einfach und gut verständlich sein soll, wobei unnötige Komplexität vermieden wird.
> Das DRY-Prinzip besagt, dass dieselbe Logik nicht unnötig an mehreren Stellen wiederholt werden soll, sondern in eine gemeinsame Abstraktion oder Funktion ausgelagert werden soll.
> In guter Entwicklung sollten beide Prinzipien gemeinsam und im Gleichgewicht angewendet werden.

## Häufige Prüfungsfehler

- KISS mit "minimalistischem Design" verwechseln.
- DRY als erzwungene Zusammenfassung jeder kleinen Ähnlichkeit interpretieren.
- Nicht über das Gleichgewicht sprechen.
- Copy-Paste als wartbare Lösung bezeichnen.

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

1. DevIQ - Keep It Simple
   https://deviq.com/principles/keep-it-simple/
   Verwendung: kurze, fachliche Erklärung des KISS-Prinzips.

2. DevIQ - Don't Repeat Yourself
   https://deviq.com/principles/dont-repeat-yourself/
   Verwendung: offizielle fachliche Beschreibung des DRY-Prinzips.

3. DevIQ - Once and Only Once
   https://deviq.com/principles/once-and-only-once/
   Verwendung: ergänzende Erklärung zum DRY-Prinzip.

Abgerufen: `2026-04-08`
