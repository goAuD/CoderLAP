# Debugger

## Schneller visueller Überblick

| Funktion | Wofür gut? |
|---|---|
| Breakpoint | stoppt die Ausführung an einem Punkt |
| Step into / over | schrittweise Ausführung |
| Variable Inspection | Beobachtung von Variablenwerten |
| Call Stack | zeigt, wie wir hierher gelangt sind |

## Was ist ein Debugger?

Der Debugger ist ein Fehlersuch-Werkzeug.

Er hilft:

- die Programmausführung zu beobachten
- an kritischen Punkten anzuhalten
- den internen Zustand zu überprüfen
- den Kontrollfluss zu verstehen

## Wofür ist er in der Praxis gut?

Zum Beispiel wenn:

- das Programm ein falsches Ergebnis liefert
- es unerwartet stoppt
- eine Bedingung nicht so funktioniert wie erwartet
- eine Schleife zu oft oder endlos läuft

## Typische Debugger-Begriffe

### Breakpoint

Ein vorher festgelegter Haltepunkt.

### Step

Schrittweise Ausführung:

- Eintritt in eine Funktion
- nächster Schritt
- Weiterlaufen bis zum nächsten Breakpoint

### Watch

Überwachung bestimmter Variablen.

### Call Stack

Zeigt, über welche Aufrufkette wir zum aktuellen Punkt gelangt sind.

## Debugger und Logging: nicht verwechseln

| Begriff | Wofür gut? |
|---|---|
| Debugger | interaktive Ausführungsüberwachung |
| Logging | Protokollierung von Ereignissen und Zuständen |

Beides zusammen ist am nützlichsten.

## Beobachtungsaufgabe an einem korrekten Programm

Der folgende Code läuft in Node.js oder der Browserkonsole und summiert zwei
ganzzahlige Centbeträge. Speichere ihn als Datei und setze im Debugger des
Editors einen Breakpoint auf die Zeile `total += price`.

<!-- example:run -->

```javascript
function subtotal(prices) {
  let total = 0;
  for (const price of prices) {
    total += price;
  }
  return total;
}
console.log(subtotal([200, 350]));
```

```text
550
```

Beim ersten Halt gilt `total = 0`, `price = 200`; die markierte Zeile wurde noch
nicht ausgeführt. Nach einem Schritt ist `total = 200`. Beim zweiten Halt ist
`price = 350`, danach beträgt die Summe `550`. Im Watch-Feld lässt sich etwa
der Ausdruck `total` beobachten.

| Aktion | Was wird ausgeführt? |
|---|---|
| Step into | in den nächsten Funktionsaufruf hineinsteigen |
| Step over | den Aufruf ausführen, ohne seine Zeilen einzeln zu betreten |
| Step out | die aktuelle Funktion beenden und beim Aufrufer anhalten |
| Resume | bis zur nächsten Haltebedingung weiterlaufen |

Ein bedingter Breakpoint hält beispielsweise nur bei `price > 300` an. Das hilft
in langen Schleifen. Personenbezogene oder geheime Daten aus dem Debugger gehören
nicht automatisch ins Protokoll; für die Beobachtung genügen oft Datentypen oder
anonymisierte Beispieldaten.

## Prüfungstaugliche Formulierung

> Der Debugger ist ein Fehlersuch-Werkzeug, das es ermöglicht, die Programmausführung zu beobachten und zu steuern.  
> Mit ihm können Breakpoints gesetzt, der Code schrittweise ausgeführt, Variablenwerte beobachtet und die Aufrufkette  
> analysiert werden.  
> Das ist besonders nützlich zur Aufdeckung logischer Fehler und Laufzeitprobleme.

## Schnelle Selbstkontrolle

1. Was ist die Hauptaufgabe des Debuggers?
2. Wofür ist der Breakpoint gut?
3. Warum ist die schrittweise Ausführung nützlich?
4. Was zeigt der Call Stack?
5. Was ist der Unterschied zwischen Debugger und Logging?

## Kurzantworten zur Selbstkontrolle

1. Ausführungsüberwachung und Fehlersuche
2. Er stoppt das Programm an einem Punkt
3. Weil die tatsächliche Ausführung verfolgt werden kann
4. Die Aufrufkette
5. Das eine ist interaktiv, das andere ist Protokollierung

## Quellen

Geprüft: `2026-10-14`.

- [Chrome DevTools: Debug JavaScript](https://developer.chrome.com/docs/devtools/javascript): Schrittsteuerung, Breakpoint und Watch.


1. GDB - Debugging with GDB  
   https://sourceware.org/gdb/current/onlinedocs/gdb.pdf  
   Verwendung: offizielle Primärquelle zum Zweck und zu den Grundoperationen des Debuggers.

2. MDN - debugger statement  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger  
   Verwendung: veranschaulicht gut die praktische Rolle des Debuggers als Breakpoint-artiger Haltepunkt.

Abgerufen: `2026-04-09`
