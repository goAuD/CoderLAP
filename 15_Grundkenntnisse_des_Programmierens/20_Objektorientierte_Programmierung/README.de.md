# Objektorientierte Programmierung

## Schneller visueller Überblick

| Begriff | Bedeutung |
|---|---|
| Klasse | Vorlage oder Plan |
| Objekt | konkrete Instanz der Klasse |
| Attribut | Daten des Objekts |
| Methode | Operation des Objekts |

## Was ist die Grundidee von OOP?

Das Programm wird nicht nur als Schrittfolge, sondern als System zusammenwirkender Objekte betrachtet.

Ein Objekt:

- besitzt Daten
- kann Operationen ausführen
- kann mit anderen Objekten in Beziehung stehen

## Die Hauptbegriffe von OOP

### Klasse und Objekt

- die Klasse ist ein Muster oder Plan
- das Objekt ist deren konkrete Instanz

### Encapsulation

Das Zusammenschließen von Daten und zugehörigen Operationen.  
Hilft dabei, dass nicht alles von überall beliebig geändert werden kann.

### Inheritance

Eine Klasse kann Eigenschaften und Verhalten von einer anderen erben.

### Polymorphism

Dieselbe Operation kann bei verschiedenen Objekten unterschiedlich umgesetzt werden.

### Abstraction

Die wesentlichen Dinge werden hervorgehoben, unnötige Details werden verborgen.

## Warum ist das nützlich?

- reale oder geschäftliche Entitäten lassen sich besser modellieren
- Erweiterung kann leichter sein
- kann die Wiederverwendbarkeit verbessern
- kann bei größeren Systemen eine übersichtlichere Struktur bieten

## Aber kein Allheilmittel

OOP ist auch nicht für alles perfekt.

Probleme können entstehen, wenn:

- wir überplanen
- die Klassenhierarchie unnötig verkomplizieren
- die Verantwortlichkeiten schlecht wählen

## OOP und prozeduraler Ansatz

| Aspekt | Prozedural | OOP |
|---|---|---|
| Hauptfokus | Schritte | Objekte |
| Organisation | Funktionen / Prozeduren | Klassen / Objekte |
| Daten und Operationen | oft getrennt | zusammen behandelt |

## Verantwortung und gültiger Zustand eines Objekts

Aufgabe: In einer Übung zählen wir alle Antworten und die richtigen Antworten.
Die Klasse sorgt dafür, dass es nie mehr richtige als gesamte Antworten gibt.
Das vollständige JavaScript-Beispiel läuft in Node.js.

<!-- example:run -->

```javascript
class PracticeSession {
  #answered = 0;
  #correct = 0;
  answer(isCorrect) {
    if (typeof isCorrect !== "boolean") throw new TypeError("Boolean required");
    this.#answered += 1;
    if (isCorrect) this.#correct += 1;
  }
  summary() {
    return `${this.#correct}/${this.#answered}`;
  }
}
const first = new PracticeSession();
const second = new PracticeSession();
first.answer(true);
first.answer(false);
console.log(first.summary(), second.summary());
```

```text
1/2 0/0
```

Die Methode `answer` verändert die privaten Felder gemeinsam und akzeptiert
nur boolesche Eingaben. Das ist der praktische Nutzen der Kapselung: den
gültigen Zustand des Objekts erhalten. `summary` fragt nur ab. Der Zustand der
zweiten Instanz bleibt unabhängig.

Die Abstraktion zeigt die von außen nutzbaren Operationen und verbirgt die
Speicherdetails der beiden Zähler. Vererbung ist hier nicht nötig. Enthält eine
Übung später mehrere Fragen, modellieren wir „eine Übung hat Fragen“ durch
Zusammensetzung (Komposition). Vererbung benötigt eine „ist eine Art von“-Beziehung
und tatsächliche Ersetzbarkeit. Bei Polymorphie kann die gleichnamige Operation
`checkAnswer` verschiedener Fragetypen eine Antwort auf unterschiedliche Weise prüfen.

## Prüfungstaugliche Formulierung

> Die objektorientierte Programmierung ist ein Programmierparadigma, in dem das System mit Objekten modelliert wird.  
> Objekte enthalten Zustand und Verhalten und werden in der Regel auf Basis von Klassen erstellt.  
> Die wichtigen Begriffe von OOP sind Klasse, Objekt, Encapsulation, Inheritance, Polymorphism und Abstraction.  
> Der Hauptvorteil ist die bessere Modellierbarkeit und Wartbarkeit, besonders bei komplexeren Systemen.

## Schnelle Selbstkontrolle

1. Was ist eine Klasse?
2. Was ist ein Objekt?
3. Was bedeutet Encapsulation?
4. Was bedeutet Polymorphism?
5. Welcher Vorteil kann OOP haben?

## Kurzantworten zur Selbstkontrolle

1. Plan oder Vorlage
2. Die Instanz der Klasse
3. Zusammenschließen von Daten und Operationen
4. Dieselbe Operation kann auf verschiedene Weisen umgesetzt werden
5. Bessere Modellierbarkeit und Wartbarkeit

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements): private Felder und sprachlich erzwungener Zugriff.


1. Oracle Java Tutorials - Object-Oriented Programming Concepts  
   https://docs.oracle.com/javase/tutorial/java/concepts  
   Verwendung: offizielle Primärquelle zu den OOP-Grundbegriffen.

2. MDN - Working with objects  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects  
   Verwendung: moderne, gut lesbare Quelle zur praktischen Interpretation von Objekten, Eigenschaften und Methoden.

Abgerufen: `2026-04-09`
