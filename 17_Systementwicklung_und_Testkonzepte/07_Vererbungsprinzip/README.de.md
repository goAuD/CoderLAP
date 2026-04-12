# Vererbungsprinzip

## Schneller visueller Überblick

```text
Vehicle
  -> Car
  -> Bike
```

## Was ist das Wesentliche der Vererbung?

Wenn mehrere Klassen gemeinsame Eigenschaften oder Operationen haben, können diese in einer Elternklasse organisiert werden.

Beispiel:

- `Vehicle` Klasse: `speed`, `move()`
- `Car` Klasse: erbt diese und kann noch eigene Elemente haben

## Warum ist sie nützlich?

- reduziert Codewiederholung
- hilft, gemeinsame Logik herauszuziehen
- macht das Modell besser organisierbar

## Mögliche Gefahren

- zu tiefe Vererbungshierarchie
- schwierigere Übersichtlichkeit
- falsche Verallgemeinerungen
- starrere Struktur

Daher ist es bei der Prüfung gut, wenn man sagt:

- Vererbung ist nützlich, aber nicht für alles das beste Werkzeug

## Vererbung und Komposition: kurzer Unterschied

| Begriff | Grundidee |
|---|---|
| Vererbung | "eine speziellere Variante von etwas" |
| Komposition | "besteht aus Teilen" |

## Was wird typischerweise vererbt?

- Attribute
- Methoden
- allgemeines Verhalten

Aber die abgeleitete Klasse kann:

- erweitern
- ändern
- die Funktionsweise einzelner Elemente überschreiben

## Prüfungstaugliche Formulierung

> Die Vererbung ist eines der Grundprinzipien der objektorientierten Programmierung, das es ermöglicht, dass eine Klasse Eigenschaften und Operationen von einer anderen Klasse übernimmt.  
> Dies unterstützt die Wiederverwendbarkeit und das Herausziehen gemeinsamen Verhaltens.  
> Allerdings kann übermäßige oder schlecht geplante Vererbung zu einem komplexen und schwer wartbaren System führen.

## Häufige Prüfungsfehler

- Vererbung als Grundlage jeder OOP-Lösung bezeichnen.
- Die Wiederverwendbarkeit nicht erwähnen.
- Die möglichen Nachteile auslassen.
- Vererbung mit Klasseninstanziierung verwechseln.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche der Vererbung?
2. Warum ist sie nützlich?
3. Was kann ihr Nachteil sein?
4. Was ist der Unterschied zwischen Eltern- und abgeleiteter Klasse?
5. Was ist der Unterschied zwischen Vererbung und Komposition in Kürze?

## Kurzantworten zur Selbstkontrolle

1. Übernahme gemeinsamer Eigenschaften und Operationen
2. Weil sie Wiederholung reduziert und ein besser organisiertes Modell ergibt
3. Sie kann eine zu komplexe Hierarchie verursachen
4. Die abgeleitete übernimmt und erweitert
5. Das eine ist "is-a", das andere eher "has-a"

## Quellen

1. MDN - Inheritance and the prototype chain  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain  
   Verwendung: offizielle, moderne Quelle zum allgemeinen Grundprinzip der Vererbung.

2. Python Docs - Inheritance  
   https://docs.python.org/3/tutorial/classes.html#inheritance  
   Verwendung: offizielle, klare Quelle zur praktischen Funktionsweise der Vererbung.

Abgerufen: `2026-04-09`
