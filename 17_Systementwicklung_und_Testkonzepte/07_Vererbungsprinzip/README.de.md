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

## Gleiche Operation, überschriebene Umsetzung

Im folgenden Node.js-Beispiel spezialisieren wir die Umwandlung einer Nachricht in Text:

<!-- example:run -->

```javascript
class Message {
  constructor(text) { this.text = text; }
  render() { return this.text; }
}
class UrgentMessage extends Message {
  render() { return `! ${super.render()}`; }
}
for (const message of [new Message("Ready"), new UrgentMessage("Save")]) {
  console.log(message.render());
}
```

```text
Ready
! Save
```

`extends` verbindet die Klassen. `UrgentMessage` übernimmt das Verhalten des
Konstruktors und überschreibt `render`. `super.render()` ruft die Umsetzung
der Elternklasse auf. Die Schleife ruft bei beiden Objekten gleichartig
`render()` auf und erhält unterschiedliche Ergebnisse: Das ist polymorphes Verhalten.

Der Vertrag gegenüber dem Aufrufer bleibt erhalten: `render` liefert Text.
Vererbung wählen wir, wenn die abgeleitete Klasse sinnvoll anstelle der
Elternklasse einsetzbar ist. Gehört zu einer Nachricht ein Protokollierungsdienst,
ist das eine „hat eine“-Beziehung; dafür eignet sich eher eine übergebene
Komponente. Gemeinsame Codezeilen allein rechtfertigen noch keine Vererbungshierarchie.

## Prüfungstaugliche Formulierung

> Die Vererbung ist eines der Grundprinzipien der objektorientierten Programmierung, das es ermöglicht, dass eine  
> Klasse Eigenschaften und Operationen von einer anderen Klasse übernimmt.  
> Dies unterstützt die Wiederverwendbarkeit und das Herausziehen gemeinsamen Verhaltens.  
> Allerdings kann übermäßige oder schlecht geplante Vererbung zu einem komplexen und schwer wartbaren System führen.

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

Geprüft: `2026-10-14`.

- [MDN: Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes): extends, super und Überschreiben von Methoden.


1. MDN - Inheritance and the prototype chain  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain  
   Verwendung: offizielle, moderne Quelle zum allgemeinen Grundprinzip der Vererbung.

2. Python Docs - Inheritance  
   https://docs.python.org/3/tutorial/classes.html#inheritance  
   Verwendung: offizielle, klare Quelle zur praktischen Funktionsweise der Vererbung.

Abgerufen: `2026-04-09`
