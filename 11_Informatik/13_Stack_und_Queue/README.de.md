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

## Wozu dienen die Operationen? Klammerpaare prüfen

**Aufgabe:** runde Klammern eines Textes sollen ausgeglichen sein. Jede öffnende
Klammer legt ein Element ab, jede schließende nimmt eines heraus. Andere Zeichen
ignoriert diese einfache Prüfung. Sie ist kein vollständiger JavaScript-Parser
und wertet weder Anführungszeichen noch Kommentare aus. Ausführung: Node.js.

<!-- example:run -->

```javascript
function balancedParentheses(text) {
  const stack = [];
  for (const character of text) {
    if (character === "(") stack.push(character);
    if (character === ")") {
      if (stack.length === 0) return false;
      stack.pop();
    }
  }
  return stack.length === 0;
}
console.log(balancedParentheses("(a + (b))"));
console.log(balancedParentheses(")("));
console.log(balancedParentheses("((a)"));
console.log(balancedParentheses(""));
```

```text
true
false
false
true
```

Im ersten Beispiel beträgt die Stapeltiefe an den Klammern `1, 2, 1, 0`.
`)(` wird sofort abgelehnt, weil aus einem leeren Stack entnommen werden müsste.
Bei `((a)` bleibt eine Öffnung übrig. Der leere Text enthält keine ungepaarten
Klammern, deshalb ist das Ergebnis wahr. Die Laufzeit wächst proportional zur
Textlänge; der Stack speichert höchstens die gleichzeitig offenen Klammern.

Für eine Queue gilt ein anderer Vertrag: `peek` liest nur, `dequeue` entfernt
ein Element. Für eine leere Struktur dokumentieren wir Rückgabewert oder
Ausnahme. JavaScripts `shift()` liefert bei einem leeren Array `undefined`.
Beim Entfernen am Arrayanfang müssen Indizes neu zugeordnet werden. Für stark
beanspruchte Warteschlangen können Ringpuffer oder passende Bibliothekstypen
geeigneter sein. Das FIFO-Prinzip allein legt die Operationskosten nicht fest.

## Prüfungstaugliche Formulierung

> Stack und Queue sind grundlegende Datenstrukturmodelle.  
> Der Stack funktioniert nach dem Stapelprinzip,
> daher wird das zuletzt eingefügte Element zuerst entnommen - also LIFO.  
> Die Queue funktioniert hingegen nach dem Schlangenprinzip,
> daher wird das am frühesten eingefügte Element zuerst verarbeitet - also FIFO.

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

Geprüft: `2026-10-14`.

- [MDN: Array.shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift): leeres Array und Neuzuordnung der Indizes.
- [MDN: Call stack](https://developer.mozilla.org/en-US/docs/Glossary/Call_stack): eine konkrete Anwendung des Stacks.


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
