# Call By Value und Call By Reference

## Schneller visueller Überblick

| Modus | Was passiert? |
|---|---|
| `call by value` | der Parameter erhält eine Kopie des Werts, auch eines Objektreferenzwerts |
| `call by reference` | der Parameter bezeichnet die Variable des Aufrufers |

## Was ist `call by value`?

Dabei erhält die Funktion:

- eine Kopie des Parameterwerts
- eine Neuzuweisung des Parameters verändert die Variable des Aufrufers nicht; Änderungen gemeinsam erreichter Objekte sind eine eigene Frage

Vorteil:

- Änderungen der lokalen Parameterbindung sind von der Aufrufervariablen getrennt

## Was ist `call by reference`?

Dabei arbeitet die Funktion:

- nicht mit einer einfachen Kopie
- sondern erhält Zugriff so, dass auch die Originaldaten geändert werden können

Vorteil:

- in bestimmten Situationen effizienter
- ermöglicht direktere Änderungen

## Warum muss man vorsichtig formulieren?

Weil moderne Sprachen nicht immer rein das eine oder das andere implementieren.

Zum Beispiel:

- einige Sprachen verwenden nur Wertübergabe, aber mit Referenztypen
- andere unterstützen auch echte Referenzübergabe

Bei der Prüfung muss man daher das Grundprinzip gut verstehen:

- Kopie oder direkterer Zugriff auf das Original

## Wann ist das relevant?

- beim Entwurf von Funktionen
- beim Verständnis von Seiteneffekten
- bei der Fehlersuche
- im Hinblick auf Leistung und Speicher

## Seiteneffekt: Schlüsselbegriff

Wenn eine Funktion die von außen erhaltenen Daten verändert, kann das ein Seiteneffekt sein.

Daher ein guter Prüfungssatz:

- `call by reference`-artiges Verhalten kann stärkere Seiteneffekte verursachen

## JavaScript: Der übergebene Wert kann eine Objektreferenz sein

JavaScript übergibt Argumente als Werte. Bei einem Objekt wird der Referenzwert
kopiert; Aufrufer und Funktion können dadurch dasselbe Objekt erreichen. Das
ist keine Referenzübergabe der Variable des Aufrufers.

<!-- example:run -->

```javascript
function change(number, record) {
  number = 99;
  record.count = 2;
  record = { count: 99 };
  console.log(number, record.count);
}
let number = 1;
const record = { count: 1 };
change(number, record);
console.log(number, record.count);
```

```text
99 99
1 2
```

Im Node.js-Beispiel verändert das lokale `number = 99` die äußere Variable
`number` nicht. `record.count = 2` verändert dagegen das gemeinsam erreichte
Objekt, sodass der Aufrufer ebenfalls 2 sieht. `record = { count: 99 }` bindet
nur den lokalen Parameter an ein anderes Objekt. Der Aufrufer verweist weiterhin
auf das ursprüngliche Objekt.

Bei echter Referenzübergabe kann der Parameter die Variable des Aufrufers selbst
bezeichnen, etwa ausdrücklich mit `ref` in C#. Ob Objekteigenschaften veränderbar
sind, ist eine eigene Frage. Im Funktionsvertrag halten wir deshalb fest, ob
die Funktion das erhaltene Objekt verändert oder ein neues Ergebnis erzeugt.

## Prüfungstaugliche Formulierung

> Bei `call by value` wird der übergebene Wert kopiert; eine Neuzuweisung des Parameters verändert die Variable des Aufrufers nicht.  
> Bei `call by reference` greift die Funktion über eine Referenz auf die Daten zu, daher kann auch der Originalwert  
> geändert werden.  
> Die genaue Implementierung kann je nach Programmiersprache unterschiedlich sein, aber der grundlegende Unterschied
> liegt zwischen Kopie und direkterem Zugriff.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von `call by value`?
2. Was ist das Wesentliche von `call by reference`?
3. Warum ist das bei Funktionen wichtig?
4. Was ist ein Risiko der referenzbasierten Änderung?
5. Warum muss man bei der Verallgemeinerung zwischen Sprachen vorsichtig sein?

## Kurzantworten zur Selbstkontrolle

1. Der Parameter erhält eine Kopie des übergebenen Werts, auch bei Objektreferenzwerten
2. Der Parameter bezeichnet die Variable des Aufrufers
3. Weil es die Änderbarkeit und Fehler beeinflusst
4. Unerwarteter Seiteneffekt
5. Weil die genaue Implementierung unterschiedlich sein kann

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions): JavaScript-Wertübergabe und Objektänderung.
- [Microsoft: Method parameters](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters): echter ref-Parameter.


1. Microsoft Learn - Method Parameters (C#) - Pass by value and pass by reference  
   https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters  
   Verwendung: offizielle, gut verständliche Quelle zum grundlegenden Unterschied der beiden Parameterübergabemodi.

2. Oracle - Pass-By-Value Example  
   https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html  
   Verwendung: offizielle Quelle dafür, dass die sprachliche Implementierung und der allgemeine begriffliche Unterschied
   nicht immer dasselbe sind.

Abgerufen: `2026-04-09`
