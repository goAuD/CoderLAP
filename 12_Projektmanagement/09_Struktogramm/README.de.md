# Struktogramm

## Schneller visueller Überblick

| Element | Was zeigt es? |
|---|---|
| untereinanderliegende Blöcke | Reihenfolge der Schritte |
| geteilter Block | Verzweigung |
| sich wiederholender Block | Schleife |

## Was ist ein Struktogramm?

Das Struktogramm dient der anschaulichen Darstellung von Algorithmen.

Es hilft dabei:

- die Programmlogik zu überblicken
- die Funktionsweise noch vor dem Codeschreiben zu planen
- in Lehre und Dokumentation die Steuerung gut darzustellen

## Worin unterscheidet es sich vom Flowchart?

Das Struktogramm baut stärker auf die Logik der **strukturierten Programmierung** auf.

Deshalb:

- weniger „pfeil-verzweigend"
- eher aus ineinander verschachtelten Blöcken aufgebaut

## Wann ist es nützlich?

- beim Lehren von Algorithmen
- bei der Planung einfacherer Programmlogik
- bei der Darstellung von Programmier-Grundbegriffen

## Struktogramm und Flowchart: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Struktogramm | blockbasiertes, strukturiertes Algorithmusdiagramm |
| Flowchart | Ablaufdiagramm mit Pfeilen, Ablauf von Schritten und Entscheidungen |

## Von den Blöcken zum ausführbaren Algorithmus

Die Bezeichnung Nassi-Shneiderman verweist auf die Autoren Isaac Nassi und Ben Shneiderman. Das Diagramm beschreibt den Kontrollfluss durch verschachtelte Blöcke statt durch separate Verbindungspfeile. Eine Sequenz besteht aus Schritten untereinander; der Schleifenrahmen enthält wiederholte Aktionen, darin trennt eine Verzweigung zwei Alternativen.

Aufgabe: Die positiven Elemente einer Zahlenliste addieren. Die äußere Sequenz des Struktogramms lautet: Summe auf null setzen, Liste durchlaufen, Ergebnis zurückgeben. In der Schleife steht die Entscheidung `value > 0`; bei wahr wird addiert, bei falsch nichts ausgeführt. Dazu passt dieser Code:

<!-- example:run -->
```javascript
function sumPositive(values) {
  let sum = 0;
  for (const value of values) {
    if (value > 0) {
      sum += value;
    }
  }
  return sum;
}

console.log(sumPositive([-2, 3, 5]));
console.log(sumPositive([]));
```

```text
8
0
```

Bei `[-2, 3, 5]` beträgt die Summe nacheinander 0, 3 und 8. Bei einer leeren Liste läuft die Schleife kein einziges Mal, das Ergebnis bleibt 0. Zeichnung und Code müssen diese Fälle gleich beschreiben.

## Prüfungstaugliche Formulierung

> Ein Struktogramm ist eine blockbasierte, strukturierte Darstellung eines Algorithmus oder einer Programmlogik.  
> Mit seiner Hilfe lassen sich die Reihenfolge der Schritte,
> Verzweigungen und Schleifen gut veranschaulichen,
> weshalb es besonders bei der Planung
> und Vermittlung von Algorithmen nützlich ist.  
> Im Gegensatz zum Flowchart verwendet es eher ineinander verschachtelte Strukturen
> und steht der Denkweise der strukturierten Programmierung näher.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche am Struktogramm?
2. Wofür wird es verwendet?
3. Warum wird es auch Nassi-Shneiderman-Diagramm genannt?
4. Worin unterscheidet es sich vom Flowchart?
5. Welche logischen Elemente kann es gut darstellen?

## Kurzantworten zur Selbstkontrolle

1. Strukturiertes Algorithmusdiagramm
2. Zur Planung und Darstellung von Algorithmen
3. Nach den Autoren Isaac Nassi und Ben Shneiderman
4. Es ist blockbasierter und strukturierter
5. Sequenz, Verzweigung, Schleife

## Quellen

- [Structorizer: User Guide](https://help.structorizer.fisch.lu/index.php?menu=44&page=)  
  Strukturierte Steuerungsdiagramme und daraus abgeleitete Programmlogik.

- [Ben Shneiderman: Publications](https://www.cs.umd.edu/~ben/publications.html)  
  Bibliografischer Nachweis der Originalveröffentlichung von Nassi und Shneiderman aus 1973.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Structorizer User Guide  
   https://help.structorizer.fisch.lu/index.php?menu=66&page=  
   Verwendung: dediziertes, offizielles Werkzeug und Dokumentation für Nassi-Shneiderman-Diagramme.

2. inf-schule - Bausteine von Algorithmen  
   https://inf-schule.de/algorithmen/grundlagen/algorithmusbegriff/bausteine  
   Verwendung: zuverlässige Bildungsquelle, die Struktogramm und Flussdiagramm nebeneinander zeigt.

Abgerufen: `2026-04-08`
