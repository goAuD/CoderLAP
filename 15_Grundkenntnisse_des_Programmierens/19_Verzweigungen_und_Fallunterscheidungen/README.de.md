# Verzweigungen und Fallunterscheidungen

## Schneller visueller Überblick

```text
Bedingung?
    ja   -> ein Zweig
    nein -> anderer Zweig
```

## Was ist eine Verzweigung?

Das Wesentliche einer Verzweigung:

- das Programm macht nicht immer dasselbe
- es wählt auf Basis einer Bedingung
- verschiedene Anweisungen können ausgeführt werden

## Typische Formen

### `if`

Bei einer Bedingung wird etwas ausgeführt.

### `if / else`

Zwei mögliche Zweige.

### `else if`-Kette

Mehrere Bedingungen können nacheinander geprüft werden.

### `switch / case`

Auswahl aus mehreren konkreten Fällen.

## Wann ist `switch` gut?

- wenn wir denselben Wert mit mehreren möglichen Fällen vergleichen
- wenn wir die Verzweigungen übersichtlicher darstellen wollen

## Worauf muss man achten?

- die Bedingungen müssen eindeutig sein
- die Reihenfolge kann eine Rolle spielen
- auch der Standard- oder "keiner davon"-Fall muss behandelt werden

## Verzweigung und Schleife: nicht verwechseln

| Begriff | Wofür? |
|---|---|
| Verzweigung | Entscheidung |
| Schleife | Wiederholung |

## Prüfungstaugliche Formulierung

> Mit Verzweigungen und Fallunterscheidungen kann das Programm auf Basis von Bedingungen zwischen verschiedenen Ausführungszweigen wählen.  
> Die häufigste Lösung ist `if / else`, für die Behandlung mehrerer konkreter Fälle wird oft `switch / case` verwendet.  
> Diese Kontrollstrukturen dienen der Umsetzung der Entscheidungslogik.

## Häufige Prüfungsfehler

- Die Verzweigung als Schleife zu bezeichnen.
- `switch` als für alles geeignet darzustellen.
- Den Standardfall nicht zu erwähnen.
- Die Bedeutung der Reihenfolge der Bedingungen zu vergessen.

## Schnelle Selbstkontrolle

1. Wofür dient die Verzweigung?
2. Wann verwenden wir `if / else`?
3. Wann kann `switch / case` übersichtlicher sein?
4. Warum ist der Standardzweig wichtig?
5. Was ist der Unterschied zwischen Verzweigung und Schleife?

## Kurzantworten zur Selbstkontrolle

1. Zur Behandlung von Entscheidungssituationen
2. Wenn wir auf Basis einer Bedingung zwischen zwei oder mehr Wegen wählen
3. Wenn wir mehrere konkrete Fälle untersuchen
4. Weil auch unerwartete Fälle behandelt werden müssen
5. Die eine entscheidet, die andere wiederholt

## Quellen

1. MDN - Control flow and error handling  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling  
   Verwendung: offizielle, ausführliche Quelle zur Funktionsweise von `if`, `else`, `switch` und anderen Verzweigungen.

2. MDN - Control flow  
   https://developer.mozilla.org/en-US/docs/Glossary/Control_flow  
   Verwendung: ergänzende Quelle zur allgemeinen Rolle von Entscheidungsstrukturen.

Abgerufen: `2026-04-09`
