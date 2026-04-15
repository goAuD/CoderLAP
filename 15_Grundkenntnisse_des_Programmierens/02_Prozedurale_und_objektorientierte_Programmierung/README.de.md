# Prozedurale und objektorientierte Programmierung

## Schneller visueller Überblick

| Aspekt | Prozedural | Objektorientiert |
|---|---|---|
| Haupteinheit | Prozedur / Funktion | Klasse / Objekt |
| Fokus | Was macht das Programm? | Welche Dinge gibt es im System? |
| Daten | werden oft separat behandelt | werden dem Objekt zugeordnet |
| Gute Wahl | kleinere, linearere Aufgaben | größere, komplexere Systeme |

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

## Nicht verwechseln

| Irrtum | Warum falsch? |
|---|---|
| OOP ist immer besser | nicht immer, hängt von der Aufgabe ab |
| prozedurale Programmierung ist veraltet | ist auch heute noch vielerorts nützlich |
| OOP = nur das Schlüsselwort class | die OOP-Denkweise umfasst mehr |

## Prüfungstaugliche Formulierung

> Die prozedurale Programmierung organisiert die Aufgabe als Abfolge von Operationen und Funktionen, während die  
> objektorientierte Programmierung die Elemente des Systems mit Objekten und Klassen modelliert.  
> Der prozedurale Ansatz konzentriert sich hauptsächlich auf die auszuführenden Schritte, der objektorientierte Ansatz  
> hingegen auf die Einheit von Daten und zugehörigen Operationen.  
> Beide Paradigmen sind nützlich, und die Wahl hängt von der Aufgabe ab.

## Häufige Prüfungsfehler

- OOP automatisch als in jeder Situation fortschrittlicher zu bezeichnen.
- Den prozeduralen Ansatz nur als "alten Stil" darzustellen.
- Die Beziehung zwischen Daten und Operationen nicht zu erwähnen.
- OOP nur auf Vererbung zu reduzieren.

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

1. Oracle Java Tutorials - Object-Oriented Programming Concepts  
   https://docs.oracle.com/javase/tutorial/java/concepts  
   Verwendung: offizielle Grundquelle zu den Hauptbegriffen der objektorientierten Denkweise.

2. Oracle - Lesson 8: Object-Oriented Programming  
   https://www.oracle.com/java/technologies/oop.html  
   Verwendung: kurzer, offizieller Überblick über die OOP-Grundidee und Sprachelemente.

Abgerufen: `2026-04-09`
