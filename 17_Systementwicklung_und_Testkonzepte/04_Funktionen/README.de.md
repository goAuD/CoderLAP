# Funktionen

## Schneller visueller Überblick

```text
Eingabe
    -> Funktion verarbeitet
    -> Rückgabewert
```

## Was ist eine Funktion?

Eine Funktion:

- erfüllt eine konkrete Aufgabe
- kann mehrfach aufgerufen werden
- reduziert Codewiederholung
- erleichtert Testen und Wartung

## Die Hauptelemente einer Funktion

| Element | Bedeutung |
|---|---|
| Name | identifiziert die Funktion |
| Parameter | Eingabedaten |
| Rumpf | die auszuführende Logik |
| Rückgabewert | das Ergebnis |

## Warum sind Funktionen wichtig?

- sie strukturieren das Programm besser
- sie trennen Verantwortlichkeiten
- sie machen Logik wiederverwendbar
- sie erleichtern die Fehlersuche

## Prozedur und Funktion: nicht verwechseln

Dieser Unterschied kommt bei der Prüfung häufig vor:

| Begriff | Einfache Erklärung |
|---|---|
| Funktion | gibt in der Regel einen Wert zurück |
| Prozedur | führt eher eine Operation aus, ohne oder ohne betonten Rückgabewert |

In modernen Sprachen ist dieser Unterschied manchmal weniger scharf, aber die Grundidee ist nach wie vor nützlich.

## Eigenschaften einer guten Funktion

- ihr Zweck soll klar sein
- sie soll nicht zu viel auf einmal tun
- sie soll eindeutige Parameter erhalten
- sie soll ein gut interpretierbares Ergebnis liefern

## Parameter, Argument und Rückgabe

Wir berechnen den Preis einer Bestellposition in ganzen Cent. Das vollständige
Node.js-Beispiel verlangt nichtnegative ganze Eingaben und ein sicher als ganze
Zahl darstellbares Ergebnis.

<!-- example:run -->

```javascript
function totalCents(unitCents, quantity = 1) {
  if (!Number.isSafeInteger(unitCents) || unitCents < 0 ||
      !Number.isSafeInteger(quantity) || quantity < 0) {
    throw new RangeError("Nonnegative integer inputs required");
  }
  const total = unitCents * quantity;
  if (!Number.isSafeInteger(total)) throw new RangeError("Total is too large");
  return total;
}
console.log(totalCents(250, 3));
console.log(totalCents(250));
console.log(totalCents(250, 0));
```

```text
750
250
0
```

In der Deklaration sind `unitCents` und `quantity` **Parameter**. Im Aufruf
`totalCents(250, 3)` sind `250` und `3` die **Argumente**, also die konkreten
übergebenen Werte. Fehlt das zweite Argument, gilt der Standardwert 1. Eine
ausdrücklich übergebene 0 bleibt hingegen 0. `return` liefert das Ergebnis und
beendet den Aufruf; `console.log` zeigt lediglich den vom Aufrufer erhaltenen Wert.

Die Berechnung verändert keinen äußeren Zustand. Eine solche Funktion lässt
sich mit gleichen Eingaben einfach prüfen. Es gibt auch anonyme Funktionen,
etwa als Callback. Ohne ausdrückliches `return` gibt eine gewöhnliche
JavaScript-Funktion `undefined` zurück; auch das ist festgelegtes Sprachverhalten.

## Prüfungstaugliche Formulierung

> Eine Funktion ist ein aufrufbarer, wiederverwendbarer Programmteil für eine bestimmte Aufgabe; sie kann benannt oder anonym sein.  
> Sie kann Parameter erhalten, diese verarbeiten und gibt häufig einen Rückgabewert zurück.  
> Der Einsatz von Funktionen verbessert die Programmstruktur, reduziert Codewiederholung und erleichtert die Wartung.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche einer Funktion?
2. Welche Hauptteile hat sie?
3. Warum ist sie im Programm nützlich?
4. Was ist der Unterschied zwischen Funktion und Prozedur?
5. Was macht eine gute Funktion aus?

## Kurzantworten zur Selbstkontrolle

1. Eine wiederverwendbare logische Einheit
2. Name, Parameter, Rumpf, Rückgabewert
3. Weil sie strukturiert und Wiederholung reduziert
4. Die Funktion gibt typischerweise ein Ergebnis zurück
5. Klar, zielgerichtet und gut parametrisiert

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions): Parameter, Argument und Rückgabe.


1. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Verwendung: offizielle, moderne Quelle zum Grundbegriff der Funktionen.

2. Python Docs - Defining Functions  
   https://docs.python.org/3/tutorial/controlflow.html#defining-functions  
   Verwendung: offizielle, gut lesbare ergänzende Quelle zum Begriff der Parameter und Rückgabe.

Abgerufen: `2026-04-09`
