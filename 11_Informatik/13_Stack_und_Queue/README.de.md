# Stack und Queue

## Schneller visueller Überblick

| Datenstruktur | Funktionsweise | Grundoperationen |
|---|---|---|
| Stack | LIFO | `push`, `pop`, `peek` |
| Queue | FIFO | `enqueue`, `dequeue`, `peek` |

## Was ist ein Stack?

Der Stack ist eine Datenstruktur, bei der die Elemente übereinander "gestapelt" werden.

Typische Operationen:

- `push` = Element hinzufügen
- `pop` = oberstes Element entnehmen
- `peek` = oberstes Element ansehen

Daher funktioniert der Stack nach dem **LIFO**-Prinzip.

## Was ist eine Queue?

Die Queue ist eine Datenstruktur, bei der die Elemente in einer Reihe auf die Verarbeitung warten.

Typische Operationen:

- `enqueue` = Element ans Ende der Schlange stellen
- `dequeue` = Element vom Anfang der Schlange entnehmen
- `peek` = Anfang der Schlange ansehen

Daher funktioniert die Queue nach dem **FIFO**-Prinzip.

## Wo werden sie verwendet?

### Stack

- Verwaltung von Funktionsaufrufen
- Rückschritt oder Undo
- Prüfung von Klammern
- Tiefensuche

### Queue

- Aufgabenwarteschlangen
- Druckwarteschlange
- Nachrichtenverarbeitung
- Breitensuche

## Was ist der Unterschied zwischen Prinzip und Struktur?

| Begriff | Was bedeutet das? |
|---|---|
| LIFO / FIFO | Prinzip der Verarbeitungsreihenfolge |
| Stack / Queue | konkretes Datenstrukturmodell |

Also:

- LIFO/FIFO ist eher eine Regel
- Stack/Queue ist eher eine Struktur und ein Operationssatz

## Stack und Queue: nicht verwechseln

| Frage | Stack | Queue |
|---|---|---|
| welches Element kommt heraus? | das neueste | das älteste |
| Reihenfolge-Prinzip | LIFO | FIFO |
| typisches Bild | Stapel | Schlange |
| typische Operation | `push/pop` | `enqueue/dequeue` |

## Worauf muss man achten?

- Der Stack ist nicht identisch mit dem Call Stack - das ist nur eine konkrete Anwendung davon.
- Die Queue ist nicht nur eine Warteschlange, sondern die Grundlage vieler Verarbeitungsmodelle.
- In der Prüfung werden oft die Namen der Operationen oder zumindest ihre Funktionsweise verlangt.

## Prüfungstaugliche Formulierung

> Stack und Queue sind grundlegende Datenstrukturmodelle.  
> Der Stack funktioniert nach dem Stapelprinzip, daher wird das zuletzt eingefügte Element zuerst entnommen - also LIFO.  
> Die Queue funktioniert hingegen nach dem Schlangenprinzip, daher wird das am frühesten eingefügte Element zuerst verarbeitet - also FIFO.

## Häufige Prüfungsfehler

- Stack und Queue nur mit Alltagsbeispielen erklären, ohne Operationen.
- LIFO/FIFO nicht damit verknüpfen.
- Die Begriffe `push/pop` und `enqueue/dequeue` verwechseln.
- Behaupten, der Stack sei immer schneller oder besser.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche des Stacks?
2. Was ist das Wesentliche der Queue?
3. Welche Operationen sind typisch für den Stack?
4. Welche Operationen sind typisch für die Queue?
5. Was ist die Verbindung zwischen Stack und LIFO?

## Kurzantworten zur Selbstkontrolle

1. Stapelartige Speicherung, LIFO-Funktionsweise
2. Schlangenartige Speicherung, FIFO-Funktionsweise
3. `push`, `pop`, `peek`
4. `enqueue`, `dequeue`, `peek`
5. Der Stack funktioniert typischerweise nach dem LIFO-Prinzip

## Quellen

1. Oracle Java SE - `Deque` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Deque.html  
   Verwendung: offizielle Quelle für stack- und queue-artige Nutzung innerhalb derselben Abstraktion.

2. Oracle Java SE - `Queue` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Queue.html  
   Verwendung: Begriff und Grundoperationen der Queue.

3. MDN - Call stack  
   https://developer.mozilla.org/en-US/docs/Glossary/Call_stack  
   Verwendung: praktisches Beispiel für die Stack-Funktionsweise bei der Programmausführung.

Abgerufen: `2026-04-08`
