# Klassen

## Schneller visueller Überblick

| Begriff | Bedeutung |
|---|---|
| Klasse | Vorlage / Bauplan |
| Objekt | konkrete Instanz der Klasse |
| Attribut | Daten oder Eigenschaft |
| Methode | zur Klasse gehörende Operation |

## Was ist eine Klasse?

Die Klasse beschreibt:

- welche Eigenschaften ein Objekt hat
- welche Operationen es ausführen kann

Beispiel:

```text
Klasse: Car
  Attribute: color, speed
  Methoden: start(), brake()
```

## Warum ist das wichtig?

- ordnet die Programmstruktur
- hilft bei der Modellierung realer oder geschäftlicher Begriffe
- unterstützt die Wiederverwendbarkeit
- trennt Verantwortlichkeiten besser

## Klasse und Objekt: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Klasse | Vorlage |
| Objekt | konkretes Element, das auf Basis der Vorlage erstellt wird |

## Typische Elemente

- Attribute
- Methoden
- Konstruktor
- Sichtbarkeitsregeln, z.B. `public`, `private`

## Warum hängt es mit der Systementwicklung zusammen?

Weil mit Klassen:

- Komponenten besser geplant werden können
- klarere Verantwortungsbereiche definiert werden können
- eine erweiterbare Struktur geschaffen werden kann

## Konstruktor, Instanzmitglied und statisches Mitglied

Wir erzeugen zwei Themen, markieren aber nur das erste als abgeschlossen.
Das vollständige Beispiel läuft in Node.js.

<!-- example:run -->

```javascript
class Topic {
  static created = 0;
  constructor(title) {
    if (typeof title !== "string" || title.trim() === "") {
      throw new TypeError("Nonempty title required");
    }
    this.title = title;
    this.completed = false;
    Topic.created += 1;
  }
  complete() { this.completed = true; }
}
const first = new Topic("Loops");
const second = new Topic("Functions");
first.complete();
console.log(first.completed, second.completed, Topic.created);
```

```text
true false 2
```

`new Topic(...)` erzeugt eine Instanz und ruft den Konstruktor auf. Dieser prüft
den Titel und setzt den Anfangszustand. `this` bezeichnet die aktuelle Instanz.
`title` und `completed` gehören jeweils einer Instanz. `static created` gehört
dagegen zur Klasse; wir lesen den Wert mit `Topic.created`.

Der Zähler misst Erzeugungen in diesem Prozess, nicht Themen in einer Datenbank
und auch nicht die Zahl noch lebender Objekte. Die öffentlichen Felder dienen
hier der Anschaulichkeit. Zum Schutz von Gültigkeitsregeln können private Felder
und prüfende Methoden verwendet werden; JavaScript kennzeichnet private Felder
mit `#` und nicht mit dem Schlüsselwort `private`.

## Prüfungstaugliche Formulierung

> Die Klasse ist einer der Grundbegriffe der objektorientierten Programmierung, die die Eigenschaften und Operationen  
> eines Objekttyps beschreibt.  
> Die Klasse ist ein Plan oder eine Vorlage, aus der konkrete Objekte instanziiert werden können.  
> Mit ihrer Hilfe lässt sich das Programm besser strukturieren, und Elemente der realen Welt oder Geschäftsbegriffe
> können gut modelliert werden.

## Schnelle Selbstkontrolle

1. Was ist eine Klasse?
2. Was ist ein Objekt?
3. Welche Elemente kann eine Klasse haben?
4. Warum sind Klassen nützlich?
5. Worin unterscheiden sich Klasse und Objekt?

## Kurzantworten zur Selbstkontrolle

1. Vorlage oder Bauplan
2. Eine Instanz der Klasse
3. Attribute, Methoden, Konstruktor
4. Weil sie das System strukturieren
5. Das eine ist die Vorlage, das andere eine konkrete Instanz

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes): Konstruktor, static und Instanzmitglieder.


1. MDN - Using classes  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes  
   Verwendung: moderne, offizielle Quelle zum Begriff und den Elementen der Klasse.

2. Python Docs - Classes  
   https://docs.python.org/3/tutorial/classes.html  
   Verwendung: offizielle, gut nachvollziehbare Quelle zur Rolle von Klassen und Instanzen.

Abgerufen: `2026-04-09`
