# Algorithmus

## Schneller visueller Überblick

```text
Eingabe
    -> Verarbeitungsschritte
    -> Ergebnis
```

## Was ist ein Algorithmus?

Ein Algorithmus:

- besteht aus einer endlichen Anzahl von Schritten
- ist klar definiert
- ist ausführbar
- führt zu einem Ergebnis

In der Programmierung ist der Algorithmus die Logik der Lösung.  
Das Programm ist dessen konkrete sprachliche Umsetzung.

## Typische Eigenschaften eines Algorithmus

| Eigenschaft | Bedeutung |
|---|---|
| Eindeutigkeit | jeder Schritt ist klar |
| Endlichkeit | er läuft nicht ewig |
| Eingabe | es kann Daten geben, mit denen er arbeitet |
| Ausgabe | er liefert ein Ergebnis |
| Wiederholbarkeit | er kann erneut ausgeführt werden |

## Warum ist das wichtig?

- hilft bei der Strukturierung des Problems
- kann unabhängig von der Programmiersprache beschrieben werden
- verschiedene Lösungen können damit verglichen werden
- ist die Grundlage eines effizienten Programms

## Algorithmus und Programm: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Algorithmus | die logische Beschreibung der Lösung |
| Programm | der konkrete Code des Algorithmus in einer Sprache |

Derselbe Algorithmus kann in mehreren Sprachen geschrieben werden.

## Einfaches Beispiel

Aufgabe: Zahlen von `1` bis `n` summieren.

Algorithmus:

1. starte mit Summe `0`
2. gehe von `1` bis `n` durch
3. addiere jeweils die aktuelle Zahl zur Summe
4. gib am Ende die Summe zurück

## Effizienz kurz gefasst

Es zählt nicht nur, ob es funktioniert, sondern auch:

- wie schnell es ist
- wie viel Speicher es verbraucht
- wie es sich bei großen Datenmengen verhält

Deshalb sprechen wir auch vom Vergleich von Algorithmen.

## Eingabebedingung, Ablaufspur und Ergebnis

Wir setzen die Summierung in JavaScript um. Der Vertrag lautet: `n` ist eine
ganze Zahl von `0..1000`; das Ergebnis ist die Summe von `1..n`. Die Grenze
sorgt in diesem Lernbeispiel für kurze Laufzeit und exakt darstellbare ganze Ergebnisse.

<!-- example:run -->

```javascript
function sumTo(n) {
  if (!Number.isInteger(n) || n < 0 || n > 1000) {
    throw new RangeError("n must be an integer from 0 to 1000");
  }
  let sum = 0;
  for (let i = 1; i <= n; i++) sum += i;
  return sum;
}
console.log(sumTo(4));
console.log(sumTo(0));
```

```text
10
0
```

Für `n = 4` nimmt die Summe die Werte `1`, `3`, `6`, `10` an. Vor der Schleife
ist sie null, nach jedem Durchlauf die Summe aller bisher verarbeiteten Zahlen.
Diese Aussage hilft, die Korrektheit zu begründen. Bei `n = 0` gibt es keinen
Durchlauf; die leere Summe ist sinnvoll als null definiert. Die Laufvariable
wächst und die Obergrenze ist endlich, daher endet die Ausführung für gültige Eingaben.

Die Schleife führt `n` Additionen aus: Zeitbedarf `O(n)`, zusätzlicher Speicher
`O(1)`. Für diese Summe lässt sich auch `n * (n + 1) / 2` mit einer festen Anzahl
von Operationen berechnen. Das nutzt eine mathematische Eigenschaft dieser
konkreten Aufgabe; nicht jede Schleife lässt sich durch eine solche Formel ersetzen.

## Prüfungstaugliche Formulierung

> Ein Algorithmus ist eine eindeutige, endliche Schrittfolge, die zur Lösung eines bestimmten Problems dient.  
> Er verarbeitet Eingaben und liefert ein Ergebnis zurück.  
> In der Programmierung ist der Algorithmus die Logik der Lösung, die später in einer konkreten Programmiersprache
> umgesetzt wird.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche eines Algorithmus?
2. Worin unterscheidet er sich vom Programm?
3. Warum ist Eindeutigkeit wichtig?
4. Was bedeutet endlich?
5. Warum ist es nützlich, dieselbe Aufgabe mit mehreren Algorithmen zu betrachten?

## Kurzantworten zur Selbstkontrolle

1. Eine eindeutige Lösungsschrittfolge
2. Der Algorithmus ist Logik, das Programm ist konkreter Code
3. Damit er auf gleiche Weise ausgeführt werden kann
4. Dass die Schrittfolge endet
5. Weil ihre Effizienz unterschiedlich sein kann

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Algorithm](https://developer.mozilla.org/en-US/docs/Glossary/Algorithm): Algorithmusbegriff; eigenständiges Summierungsbeispiel.


1. MDN - Algorithm  
   https://developer.mozilla.org/en-US/docs/Glossary/Algorithm  
   Verwendung: moderne, knappe Begriffsdefinition zum Algorithmus.

2. NIST CSRC Glossary - Algorithm  
   https://csrc.nist.gov/glossary/term/algorithm  
   Verwendung: offizieller Definitionshintergrund zum Algorithmusbegriff.

Abgerufen: `2026-04-09`
