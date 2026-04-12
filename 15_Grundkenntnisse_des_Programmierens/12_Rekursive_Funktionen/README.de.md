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

## Prüfungstaugliche Formulierung

> Eine rekursive Funktion ist eine Funktion, die sich selbst aufruft, um ein kleineres Teilproblem zu lösen.  
> Für die korrekte Funktionsweise ist immer ein Basisfall und ein rekursiver Fall erforderlich.  
> Die Rekursion ist besonders nützlich bei hierarchischen oder Aufteilungsproblemen, kann aber bei zu tiefen Aufrufen Ressourcenprobleme verursachen.

## Häufige Prüfungsfehler

- Den Basisfall auszulassen.
- Zu behaupten, dass Rekursion immer besser als eine Schleife ist.
- Die Stack-Nutzung nicht zu erwähnen.
- Rekursion mit einem einfachen Funktionsaufruf zu verwechseln.

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

1. MDN - Recursion  
   https://developer.mozilla.org/en-US/docs/Glossary/Recursion  
   Verwendung: moderne, offizielle Begriffsquelle zu den Grundlagen der Rekursion.

2. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Verwendung: ergänzende offizielle Erklärung zur praktischen Funktionsweise rekursiver Funktionen.

Abgerufen: `2026-04-09`
