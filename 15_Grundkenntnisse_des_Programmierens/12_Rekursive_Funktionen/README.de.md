# Rekursive Funktionen

## Schneller visueller Überblick

```text
funktion(n)
    -> wenn Basisfall, stopp
    -> sonst ruft sich selbst mit kleinerem Problem auf
```

## Was ist das Wesentliche der Rekursion?

Von Rekursion sprechen wir, wenn eine Funktion:

- sich selbst aufruft
- mit einem kleineren oder einfacheren Teilproblem
- solange, bis ein Basisfall erreicht wird

## Die zwei Pflichtteile der Rekursion

| Teil | Warum nötig? |
|---|---|
| Basisfall | stoppt den Vorgang |
| Rekursiver Fall | zerlegt das Problem weiter |

Wenn kein guter Basisfall vorhanden ist, entsteht leicht eine endlose Rekursion.

## Einfaches Beispiel

Fakultät:

```text
fact(0) = 1
fact(n) = n * fact(n - 1)
```

Hier:

- Basisfall: `n = 0`
- rekursiver Schritt: `fact(n - 1)`

## Wann ist das nützlich?

- bei Baum- oder hierarchischen Strukturen
- bei Teile-und-Herrsche-Algorithmen
- bei der Umsetzung mathematischer Definitionen

## Vorteile

- kann knapp und elegant sein
- passt gut zu bestimmten Problemen
- bleibt nahe an der natürlichen Struktur des Problems

## Nachteile

- kann schwerer nachzuvollziehen sein
- verwendet den Stack
- kann bei zu tiefer Aufrufkette Fehler verursachen
- manchmal langsamer oder speicherintensiver als Iteration

## Rekursion und Schleife: nicht verwechseln

| Begriff | Kern |
|---|---|
| Schleife | Wiederholung mit Kontrollstruktur |
| Rekursion | Wiederholung durch Selbstaufruf einer Funktion |

Viele Aufgaben lassen sich auf beide Arten lösen, aber nicht immer gleich gut.

## Auch das Zurückkehren der Aufrufe gehört zur Lösung

Aufgabe: die Fakultät ganzer Zahlen aus `0..12`. Die bewusst gewählte Grenze
ergibt kurze Aufrufketten und exakt darstellbare ganze Ergebnisse. Das
JavaScript-Beispiel läuft in Node.js.

<!-- example:run -->

```javascript
function factorial(n) {
  if (!Number.isInteger(n) || n < 0 || n > 12) {
    throw new RangeError("n must be an integer from 0 to 12");
  }
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(4));
console.log(factorial(0));
```

```text
24
1
```

| Aufruf | Worauf wartet er? | Rückgabewert |
|---|---|---|
| `factorial(0)` | auf nichts, Basisfall | `1` |
| `factorial(1)` | `1 * factorial(0)` | `1` |
| `factorial(2)` | `2 * factorial(1)` | `2` |
| `factorial(3)` | `3 * factorial(2)` | `6` |
| `factorial(4)` | `4 * factorial(3)` | `24` |

Die Aufrufe entstehen abwärts in der Reihenfolge `4, 3, 2, 1, 0`; ihre Ergebnisse
werden rückwärts aufgebaut. Jeder Aufruf besitzt seinen eigenen Parameter `n`.
Zusätzlich zum Basisfall begründen wir, warum sich der nächste Aufruf diesem
nähert: Die ganze Zahl `n` sinkt hier stets um eins. Laufzeit und Aufrufstapel
betragen `O(n)`. Eine iterative Lösung kann dieselbe Aufgabe mit einem Akkumulator
und `O(1)` Zusatzspeicher lösen. Es gibt auch indirekte Rekursion: Eine Funktion
ruft sich über eine andere Funktion erneut auf.

## Prüfungstaugliche Formulierung

> Eine rekursive Funktion ist eine Funktion, die sich selbst aufruft, um ein kleineres Teilproblem zu lösen.  
> Für die korrekte Funktionsweise ist immer ein Basisfall und ein rekursiver Fall erforderlich.  
> Die Rekursion ist besonders nützlich bei hierarchischen oder Aufteilungsproblemen, kann aber bei zu tiefen Aufrufen
> Ressourcenprobleme verursachen.

## Schnelle Selbstkontrolle

1. Was ist eine rekursive Funktion?
2. Was ist die Rolle des Basisfalls?
3. Was ist die Rolle des rekursiven Falls?
4. Worin unterscheidet sie sich von einer Schleife?
5. Welches Risiko kann bestehen?

## Kurzantworten zur Selbstkontrolle

1. Eine Funktion, die sich selbst aufruft
2. Sie stoppt den Vorgang
3. Sie zerlegt das Problem weiter
4. Die Rekursion wiederholt durch Selbstaufruf
5. Zu tiefe Aufrufkette und hohe Stack-Nutzung

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Recursion](https://developer.mozilla.org/en-US/docs/Glossary/Recursion): Basisfall, Aufrufstapel und Rückkehr.


1. MDN - Recursion  
   https://developer.mozilla.org/en-US/docs/Glossary/Recursion  
   Verwendung: moderne, offizielle Begriffsquelle zu den Grundlagen der Rekursion.

2. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Verwendung: ergänzende offizielle Erklärung zur praktischen Funktionsweise rekursiver Funktionen.

Abgerufen: `2026-04-09`
