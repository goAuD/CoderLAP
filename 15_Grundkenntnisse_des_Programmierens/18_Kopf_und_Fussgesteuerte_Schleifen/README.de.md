# Kopf- und fussgesteuerte Schleifen

## Schneller visueller Überblick

| Typ | Ort der Bedingung | Minimale Ausführung |
|---|---|---|
| kopfgesteuert | am Anfang der Schleife | `0` |
| fußgesteuert | am Ende der Schleife | `1` |

## Was ist eine kopfgesteuerte Schleife?

Dabei wird vom Programm:

- zuerst die Bedingung geprüft
- und erst danach der Schleifenkörper ausgeführt

Typisches Beispiel:

- `while`

## Was ist eine fußgesteuerte Schleife?

Dabei wird vom Programm:

- zuerst der Schleifenkörper ausgeführt
- erst danach die Bedingung geprüft

Typisches Beispiel:

- `do...while`

## Warum ist dieser Unterschied wichtig?

Weil nicht dasselbe passiert, wenn die Bedingung sofort falsch ist.

### Bei der kopfgesteuerten Schleife

- kann sie kein einziges Mal laufen

### Bei der fußgesteuerten Schleife

- wird der Schleifenkörper mindestens einmal sicher ausgeführt

## Einfaches Beispiel

Aufgabe: Daten einlesen, solange sie nicht korrekt sind.

Wenn mindestens eine Eingabe sicher benötigt wird, ist die fußgesteuerte Logik oft natürlicher.

## Nach der ersten Verarbeitung prüfen

Die Eingabe ersetzen wir hier durch ein vorgegebenes, **nicht leeres** Array
endlicher ganzer Zahlen. Wir lesen, bis ein Wert mindestens 1 ist oder die Liste
endet. So gibt es keine interaktive Wartezeit; das Beispiel läuft reproduzierbar in Node.js.

<!-- example:run -->

```javascript
function readAtLeastOnce(inputs) {
  let position = 0;
  let value;
  do {
    value = inputs[position];
    position += 1;
  } while (value < 1 && position < inputs.length);
  return { value, attempts: position };
}
console.log(JSON.stringify(readAtLeastOnce([0, -2, 4])));
console.log(JSON.stringify(readAtLeastOnce([7])));
```

```text
{"value":4,"attempts":3}
{"value":7,"attempts":1}
```

Im ersten Fall sind nach `0` und `-2` weitere Daten vorhanden. `4` ist gültig,
daher erfolgen drei Lesevorgänge. Bei `[7]` genügt einer. Sind alle Werte kleiner
als 1, beendet die Prüfung auf das Listenende den Ablauf nach dem letzten Wert.
Der Aufrufer muss dann weiterhin prüfen, ob das Ergebnis zulässig ist. Für eine
leere Liste braucht man vorher eine Leerheitsprüfung oder eine kopfgesteuerte Verarbeitung.

Die Bedingung von `do...while` ist eine **Fortsetzungsbedingung**: Bei wahr wird
wiederholt. Die Pseudocode-Schreibweise `repeat ... until` beendet dagegen bei
wahr. Bei der Übertragung beachten wir deshalb die Bedeutung der Bedingung und
nicht nur deren Position.

## Prüfungstaugliche Formulierung

> Die kopfgesteuerte Schleife prüft die Bedingung vor der Ausführung des Schleifenkörpers, daher kann es vorkommen,  
> dass die Schleife kein einziges Mal durchläuft.  
> Die fußgesteuerte Schleife hingegen prüft die Bedingung nach dem Schleifenkörper, sodass er mindestens einmal sicher  
> ausgeführt wird.  
> Der Unterschied zwischen den beiden Typen liegt hauptsächlich in der minimalen Ausführungsanzahl und im Ort der Bedingungsprüfung.

## Schnelle Selbstkontrolle

1. Was ist eine kopfgesteuerte Schleife?
2. Was ist eine fußgesteuerte Schleife?
3. Welche kann null Mal durchlaufen?
4. Welche läuft mindestens einmal?
5. Warum ist dieser Unterschied wichtig?

## Kurzantworten zur Selbstkontrolle

1. Die, die die Bedingung am Anfang prüft
2. Die, die die Bedingung am Ende prüft
3. Die kopfgesteuerte
4. Die fußgesteuerte
5. Weil sie je nach Ausgangsbedingung unterschiedliches Verhalten zeigt

## Quellen

Geprüft: `2026-10-14`.

- [MDN: do...while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while): Fortsetzungsbedingung und erste Ausführung.


1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Verwendung: offizielle Quelle zur Funktionsweise von `while` und `do...while`.

2. MDN - Control flow and error handling  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling  
   Verwendung: ergänzender Hintergrund zum Verständnis der Unterschiede zwischen Kontrollstrukturen.

Abgerufen: `2026-04-09`
