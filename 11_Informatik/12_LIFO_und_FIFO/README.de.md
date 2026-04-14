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

## Prüfungstaugliche Formulierung

> LIFO und FIFO sind Verarbeitungsprinzipien,
> die bestimmen, in welcher Reihenfolge Elemente entnommen oder verarbeitet werden.  
> Bei LIFO kommt das zuletzt eingefügte Element zuerst heraus, bei FIFO das am frühesten eingefügte.  
> Die typische Umsetzung von LIFO ist der Stack, die von FIFO die Queue.

## Häufige Prüfungsfehler

- Die beiden Abkürzungen vertauschen.
- Nur auf Englisch auflösen, ohne es zu erklären.
- Kein informatisches Beispiel nennen.
- Glauben, dass beide für denselben Zweck dienen.

## Schnelle Selbstkontrolle

1. Was bedeutet LIFO?
2. Was bedeutet FIFO?
3. Welche Datenstruktur gehört eher zum Stack?
4. Welche Datenstruktur gehört eher zur Queue?
5. Nenne je ein Beispiel für beide.

## Kurzantworten zur Selbstkontrolle

1. Last In, First Out
2. First In, First Out
3. LIFO
4. FIFO
5. LIFO: Aufruf-Stack. FIFO: Druckwarteschlange

## Quellen

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
