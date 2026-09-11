# Suchalgorithmen: sequentiell / binaer

## Schneller visueller Überblick

| Algorithmus | Voraussetzung | Typische Zeitkomplexität |
|---|---|---|
| sequenziell / linear | keine sortierte Liste nötig | `O(n)` |
| binär | sortierte Liste erforderlich | `O(log n)` |

## Was ist die sequenzielle Suche?

Die sequenzielle Suche:

- untersucht die Elemente der Reihe nach
- geht weiter, bis der gesuchte Wert gefunden wird
- oder die Liste zu Ende ist

Vorteil:

- sehr einfach
- kein sortierter Datensatz erforderlich

Nachteil:

- kann bei großen Listen langsam sein

## Was ist die binäre Suche?

Die binäre Suche ist nur bei **sortierten** Daten anwendbar.

Schritte:

1. das mittlere Element anschauen
2. mit dem gesuchten Wert vergleichen
3. entscheiden, ob links oder rechts weitergesucht werden muss
4. den verbleibenden Teil erneut halbieren

Deshalb kann sie viel schneller sein.

## Ausgearbeitete Beispiele in JavaScript

Aufgabe: Suche die 42 im Zahlenarray `[5, 11, 19, 42, 70]`.
Die Funktionen liefern den **Index** des gefundenen Elements. Die Indizierung
beginnt bei 0; die 42 hat daher Index 3. Endet die Suche ohne Treffer, lautet
das Ergebnis `-1`. Die Beispiele arbeiten mit endlichen Zahlen und lassen das
Array unverändert. Jeder JavaScript-Block läuft eigenständig, beispielsweise
mit `node beispiel.js` in einer installierten Node.js-Umgebung.

### Lineare Suche: Element für Element

```javascript
function linearSearch(values, target) {
  for (let index = 0; index < values.length; index++) {
    if (values[index] === target) {
      return index;
    }
  }
  return -1;
}

console.log(linearSearch([5, 11, 19, 42, 70], 42));
console.log(linearSearch([5, 11, 19, 42, 70], 8));
```

Ausgabe:

```text
3
-1
```

Die Suche prüft zuerst 5, dann 11, 19 und 42. `return index` beendet beim Treffer
die gesamte Funktion. Bei der Suche nach 8 werden alle fünf Elemente untersucht;
anschließend wird `return -1` nach der Schleife ausgeführt. Bei mehrfach gleichen
Werten liefert diese Variante den Index des ersten Vorkommens.

### Binäre Suche: den Suchbereich halbieren

Voraussetzung: `values` ist **aufsteigend sortiert**; gleiche Werte sind erlaubt.
Die Funktion setzt diese Sortierung voraus. `left` und `right` sind der erste
und letzte Index des verbleibenden Bereichs, jeweils einschließlich der Grenze.

```javascript
function binarySearch(values, target) {
  let left = 0;
  let right = values.length - 1;
  while (left <= right) {
    const middle = left + Math.floor((right - left) / 2);
    if (values[middle] === target) {
      return middle;
    }
    if (values[middle] < target) {
      left = middle + 1;
    } else {
      right = middle - 1;
    }
  }
  return -1;
}

console.log(binarySearch([5, 11, 19, 42, 70], 42));
console.log(binarySearch([5, 11, 19, 42, 70], 8));
```

Ausgabe:

```text
3
-1
```

| Schritt bei der Suche nach 42 | `left` | `right` | `middle` | Entscheidung |
|---|---|---|---|---|
| 1. | 0 | 4 | 2 | 19 ist kleiner als 42, daher `left = 3` |
| 2. | 3 | 4 | 3 | der mittlere Wert ist 42, Rückgabe von Index 3 |

`Math.floor` rundet ab und liefert einen ganzzahligen Index. Mit `+ 1` oder
`- 1` wird das bereits verglichene mittlere Element im nächsten Durchlauf
ausgeschlossen; so schrumpft der Bereich laufend. Bei `left > right` ist er leer,
und das Ergebnis lautet `-1`. Bei leerer Eingabe gilt das bereits bei der ersten
Bedingungsprüfung. Bei wiederholten Werten liefert diese Variante einen passenden
Index; die Suche nach dem ersten Vorkommen benötigt eine angepasste Suchvariante.

## Wann welche?

### Sequenzielle Suche

- bei kleinen Datenmengen
- bei unsortierten Daten
- als schnell implementierbare Lösung

### Binäre Suche

- bei größeren Datensätzen
- wenn die Daten sortiert sind
- wenn viele Suchvorgänge durchgeführt werden müssen

## Sortierung und Gesamtaufwand

Der Vorteil der binären Suche gilt für ein bereits sortiertes, indizierbares
Array. Muss zunächst sortiert werden, gehören diese Kosten zum Gesamtaufwand.
Für eine einzelne Suche ist der lineare Durchlauf oft einfacher; bei vielen
Suchvorgängen kann sich die Sortierung lohnen. Die binäre Suche verschiebt hier
Indexgrenzen in einem Array; ein binärer Baum ist eine eigene Datenstruktur
aus Knoten.

## Prüfungstaugliche Formulierung

> Die sequenzielle Suche untersucht die Elemente der Reihe nach, bis sie den gesuchten Wert findet oder das Listenende  
> erreicht.  
> Die binäre Suche hingegen halbiert stets den Suchbereich und ist daher schneller, aber nur bei sortierten Daten  
> anwendbar.  
> Der wichtigste Unterschied zwischen den beiden Algorithmen liegt im Funktionsprinzip und in der Sortierungsvoraussetzung.

## Schnelle Selbstkontrolle

1. Was bedeutet der Rückgabewert 3 in den Beispielen?
2. Welches Element prüft die binäre Suche im gegebenen Array mit fünf Elementen zuerst?
3. Warum wird `left = middle + 1` gesetzt, wenn der mittlere Wert kleiner als der gesuchte ist?
4. Was liefern die Funktionen bei einem leeren Array?
5. Warum sollten auch die Kosten einer vorherigen Sortierung berücksichtigt werden?

## Kurzantworten zur Selbstkontrolle

1. Den Index: Die 42 steht an vierter Stelle, also bei Index 3.
2. Die 19 bei Index 2.
3. In einem sortierten Array sind die Mitte und alle Werte links davon zu klein; der nächste Kandidat liegt direkt rechts von der Mitte.
4. `-1`, weil kein Element untersucht werden kann.
5. Zum Gesamtaufwand gehören Sortierung und Suchvorgänge zusammen; für eine einzelne Suche kann ein linearer Durchlauf günstiger sein.

## Quellen

1. NIST DADS - linear search  
   https://xlinux.nist.gov/dads/HTML/linearSearch.html  
   Verwendung: offizielle Definition und Komplexitätshintergrund zur sequenziellen Suche.

2. NIST DADS - binary search  
   https://xlinux.nist.gov/dads/HTML/binarySearch.html  
   Verwendung: offizielle Definition und Funktionshintergrund zur binären Suche.

Abgerufen: `2026-09-11`
