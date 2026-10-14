# LIFO und FIFO

## Schneller visueller Überblick

| Prinzip | Bedeutung | Typische Datenstruktur | Alltagsbeispiel |
|---|---|---|---|
| LIFO | letztes rein, erstes raus | Stack | Teller übereinander |
| FIFO | erstes rein, erstes raus | Queue | Schlange stehen |

## Was ist LIFO?

Beim LIFO-Prinzip wird das Element zuerst verarbeitet oder entnommen, das **zuletzt** hinzugefügt wurde.

Beispiel:

1. du legst `A` hinein
2. du legst `B` hinein
3. du legst `C` hinein
4. bei der Entnahme kommt zuerst `C`

Das ist typisches **Stack**-Verhalten.

## Was ist FIFO?

Beim FIFO-Prinzip wird das Element zuerst verarbeitet, das **am frühesten** hinzugefügt wurde.

Beispiel:

1. du legst `A` hinein
2. du legst `B` hinein
3. du legst `C` hinein
4. bei der Entnahme kommt zuerst `A`

Das ist typisches **Queue**-Verhalten.

## Wo tritt es in der Informatik auf?

### LIFO

- Funktionsaufruf-Stack
- Rückschritt-Mechanismen
- Undo-artige Lösungen

### FIFO

- Druckwarteschlange
- Nachrichtenwarteschlange
- Aufgabenverarbeitung in Reihenfolge des Eingangs
- Warteschlangen

## Warum ist das wichtig?

Weil die Verarbeitungsreihenfolge:

- die Funktionsweise des Programms bestimmt
- Auswirkungen auf die Korrektheit hat
- die Leistung und das Benutzererlebnis beeinflusst

Wenn das falsche Prinzip gewählt wird, kann das System logisch fehlerhaft sein.

## LIFO und FIFO: nicht verwechseln

| Frage | LIFO | FIFO |
|---|---|---|
| welches Element kommt zuerst? | das neueste | das älteste |
| typische Struktur | Stack | Queue |
| Hauptbild | Stapel | Schlange |

## Worauf muss man achten?

- LIFO und FIFO sind keine konkrete Programmiersprache, sondern Funktionsprinzipien.
- Dieselbe Datenstruktur kann in bestimmten Fällen auf verschiedene Weisen verwendet werden.
- In der Prüfung wird oft auch ein Beispiel verlangt, nicht nur die Auflösung.

## Einfügen und Entnehmen im Wechsel

**Aufgabe:** `A` und danach `B` kommen an. Ein Element wird entnommen, dann kommt
`C` hinzu, anschließend wird der Speicher geleert. Dies zeigt die Regel besser
als eine bloß umgedrehte Liste. Eigenständig in Node.js ausführbar:

<!-- example:run -->

```javascript
const lifo = [];
const fifo = [];
for (const task of ["A", "B"]) {
  lifo.push(task);
  fifo.push(task);
}
console.log(lifo.pop(), fifo.shift());
lifo.push("C");
fifo.push("C");
console.log(lifo.pop(), fifo.shift());
console.log(lifo.pop(), fifo.shift());
console.log(lifo.length, fifo.length);
```

```text
B A
C B
A C
0 0
```

Zuerst verlässt bei LIFO `B`, bei FIFO dagegen `A` die Struktur. Das neue `C`
liegt oben auf dem Stapel und ist dort sofort als Nächstes dran. In der Queue
steht es hinter `B`. Somit ist die LIFO-Reihenfolge `B, C, A`, die
FIFO-Reihenfolge `A, B, C`.

Die Reihenfolge beschreibt die **Auswahl der Elemente**. Bei mehreren parallelen
Verarbeitern kann trotz FIFO-Entnahme eine später gestartete kurze Aufgabe früher
fertig sein. Eine Prioritätswarteschlange verwendet wiederum eine andere
Auswahlregel. Nicht jeder Bibliothekstyp mit „Queue“ im Namen ist streng FIFO.

## Prüfungstaugliche Formulierung

> LIFO und FIFO sind Verarbeitungsprinzipien,
> die bestimmen, in welcher Reihenfolge Elemente entnommen oder verarbeitet werden.  
> Bei LIFO kommt das zuletzt eingefügte Element zuerst heraus, bei FIFO das am frühesten eingefügte.  
> Die typische Umsetzung von LIFO ist der Stack, die von FIFO die Queue.

## Schnelle Selbstkontrolle

1. Was bedeutet LIFO?
2. Was bedeutet FIFO?
3. Welches Reihenfolgeprinzip gehört zum Stack?
4. Welches Reihenfolgeprinzip gehört zur FIFO-Queue?
5. Nenne je ein Beispiel für beide.

## Kurzantworten zur Selbstkontrolle

1. Last In, First Out
2. First In, First Out
3. LIFO
4. FIFO
5. LIFO: Aufruf-Stack. FIFO: Druckwarteschlange

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Array.shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift): Entnahme am Anfang und verändertes Array.
- [Oracle: Queue](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Queue.html): FIFO und andere Reihenfolgen bei Queues.


1. Oracle Java SE - `Deque` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Deque.html  
   Verwendung: offizielle Quelle dafür, dass ein Deque sowohl als LIFO-Stack als auch als FIFO-Queue verwendet werden kann.

2. Oracle Java SE - `Queue` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Queue.html  
   Verwendung: offizielle Quelle zum allgemeinen Funktionsprinzip der Queue.

3. MDN - Call stack  
   https://developer.mozilla.org/en-US/docs/Glossary/Call_stack  
   Verwendung: praktisches, webbezogenes Beispiel für LIFO-Verhalten bei der Programmausführung.

Abgerufen: `2026-04-08`
