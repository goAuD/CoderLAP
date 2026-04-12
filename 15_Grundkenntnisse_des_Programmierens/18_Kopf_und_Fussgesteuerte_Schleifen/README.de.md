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

## Prüfungstaugliche Formulierung

> Die kopfgesteuerte Schleife prüft die Bedingung vor der Ausführung des Schleifenkörpers, daher kann es vorkommen, dass die Schleife kein einziges Mal durchläuft.  
> Die fußgesteuerte Schleife hingegen prüft die Bedingung nach dem Schleifenkörper, sodass er mindestens einmal sicher ausgeführt wird.  
> Der Unterschied zwischen den beiden Typen liegt hauptsächlich in der minimalen Ausführungsanzahl und im Ort der Bedingungsprüfung.

## Häufige Prüfungsfehler

- Den Unterschied zwischen `while` und `do...while` nicht zu kennen.
- Zu behaupten, dass beide gleich funktionieren.
- Die garantierte einmalige Ausführung nicht zu erwähnen.
- Die Begriffe kopfgesteuert und fußgesteuert zu vertauschen.

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

1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Verwendung: offizielle Quelle zur Funktionsweise von `while` und `do...while`.

2. MDN - Control flow and error handling  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling  
   Verwendung: ergänzender Hintergrund zum Verständnis der Unterschiede zwischen Kontrollstrukturen.

Abgerufen: `2026-04-09`
