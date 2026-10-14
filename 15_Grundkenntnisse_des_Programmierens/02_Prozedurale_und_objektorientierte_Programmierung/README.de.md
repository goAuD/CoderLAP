# Prozedurale und objektorientierte Programmierung

## Schneller visueller Überblick

| Aspekt | Prozedural | Objektorientiert |
|---|---|---|
| Haupteinheit | Prozedur / Funktion | Klasse / Objekt |
| Fokus | Was macht das Programm? | Welche Dinge gibt es im System? |
| Daten | werden oft separat behandelt | werden dem Objekt zugeordnet |
| Organisationskriterium | klar getrennte Operationen | zusammengehöriger Zustand und Verhalten |

## Was ist prozedurale Programmierung?

Beim prozeduralen Ansatz besteht das Programm:

- aus einer Folge von Anweisungen
- wird in Funktionen oder Prozeduren gegliedert
- konzentriert sich auf Operationen mit Daten

Diese Denkweise steht nahe an Algorithmen:

- Eingabe
- Verarbeitung
- Ausgabe

## Was ist objektorientierte Programmierung?

Beim objektorientierten Ansatz modellieren wir die Elemente des Systems als Objekte.

Ein Objekt enthält typischerweise:

- Daten, also Zustand
- Operationen, also Methoden

Objekte werden in der Regel auf Basis von Klassen erstellt.

## Warum ist der Unterschied wichtig?

Weil man das Programm nicht auf dieselbe Weise organisiert.

### Beim prozeduralen Ansatz

- die Schrittfolge dominiert
- kann schnell überschaubar sein
- bei kleineren Aufgaben einfach

### Beim objektorientierten Ansatz

- die Elemente des Systems lassen sich besser modellieren
- die Erweiterbarkeit kann leichter sein
- bei größeren Projekten besser skalierbar

## Einfaches Beispiel

### Prozedurales Denken

```text
berechne_Gehalt()
drucke_Gehaltszettel()
speichere_in_Datei()
```

### Objektorientiertes Denken

```text
Mitarbeiter
  - Name
  - Gehalt
  - berechneGehalt()
```

## Den Ansatz auswählen

Die Organisation soll zu Daten, Operationen und erwarteten Änderungen passen. Ein Programm kann mehrere Paradigmen verwenden.

## Dieselbe Punktzahl auf zwei Arten organisieren

Aufgabe: Zu einer Punktzahl mit Startwert null kommen zunächst 3 und dann 2
Punkte. Das Beispiel setzt geprüfte, nichtnegative ganze Eingaben voraus und
läuft mit Node.js.

<!-- example:run -->

```javascript
function addPoints(score, points) {
  return score + points;
}
class Score {
  #value = 0;
  add(points) { this.#value += points; }
  get value() { return this.#value; }
}
let total = addPoints(0, 3);
total = addPoints(total, 2);
const score = new Score();
score.add(3);
score.add(2);
console.log(total, score.value);
```

```text
5 5
```

Die Funktion erhält den bisherigen Wert und gibt einen neuen zurück. Die
Klasseninstanz speichert ihren eigenen Zustand; `add` verändert ihn. `#value`
ist ein privates Feld. Der von außen lesbare Getter `value` erlaubt nur eine
Abfrage. Zwei `Score`-Instanzen hätten getrennte Punktzahlen. Für eine einfache
Berechnung genügt oft die Funktion; zusammengehöriger Zustand mit Operationen
kann für ein Objekt sprechen.

Die Auswahl folgt nicht allein aus der Programmgröße. Auch große Systeme können
aus modularen Funktionen bestehen. JavaScript erlaubt außerdem Objekte ohne
Klasse, etwa Objektliterale. Objekt und Klasse sind daher keine Synonyme.

## Prüfungstaugliche Formulierung

> Die prozedurale Programmierung organisiert die Aufgabe als Abfolge von Operationen und Funktionen, während die  
> objektorientierte Programmierung die Elemente des Systems mit Objekten und Klassen modelliert.  
> Der prozedurale Ansatz konzentriert sich hauptsächlich auf die auszuführenden Schritte, der objektorientierte Ansatz  
> hingegen auf die Einheit von Daten und zugehörigen Operationen.  
> Beide Paradigmen sind nützlich, und die Wahl hängt von der Aufgabe ab.

## Schnelle Selbstkontrolle

1. Was ist der Hauptfokus der prozeduralen Programmierung?
2. Was ist der Hauptfokus von OOP?
3. Was ist die Beziehung zwischen Klasse und Objekt?
4. Welcher Ansatz kann für kleinere Aufgaben einfacher sein?
5. Warum stimmt es nicht, dass es nur ein einziges gutes Paradigma gibt?

## Kurzantworten zur Selbstkontrolle

1. Die Operationen und Funktionen
2. Die Objekte und deren Zustand + Verhalten
3. Das Objekt ist eine Instanz der Klasse
4. Oft der prozedurale
5. Weil die Aufgabe bestimmt, welches vorteilhafter ist

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Using classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes): private Felder, Getter und Instanzzustand.


1. Oracle Java Tutorials - Object-Oriented Programming Concepts  
   https://docs.oracle.com/javase/tutorial/java/concepts  
   Verwendung: offizielle Grundquelle zu den Hauptbegriffen der objektorientierten Denkweise.

2. Oracle - Lesson 8: Object-Oriented Programming  
   https://www.oracle.com/java/technologies/oop.html  
   Verwendung: kurzer, offizieller Überblick über die OOP-Grundidee und Sprachelemente.

Abgerufen: `2026-04-09`
