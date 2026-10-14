# Standardbibliothek

## Schneller visueller Überblick

| Standard-Library-Bereich | Beispiel |
|---|---|
| Textverarbeitung | String-Operationen |
| Dateiverwaltung | Lesen, Schreiben |
| Datum und Zeit | Zeitverarbeitung |
| Datenstrukturen | Listen, Dictionaries, Collections |
| Mathematische Operationen | Berechnungen |

## Was ist eine Standard Library?

Die meisten allgemeinen Programmiersprachen und Laufzeitumgebungen bieten Basisbibliotheken, deren Umfang je nach Plattform unterschiedlich ist.

Dieses bietet typischerweise:

- Grundoperationen
- häufig verwendete Werkzeuge
- gut dokumentierte, gemeinsame Lösungen

## Warum ist das wichtig?

- beschleunigt die Entwicklung
- reduziert die Anzahl überflüssiger eigener Lösungen
- oft besser getestet und stabiler als die selbst geschriebene Alternative
- kann zu einheitlicherem Code führen

## Wofür ist sie in der Praxis gut?

Zum Beispiel:

- Dateien verwalten
- Datums- und Zeitwerte berechnen
- Netzwerkoperationen durchführen
- Daten transformieren
- mit Collections arbeiten

## Standard Library und externes Paket: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Standard Library | Grundbestandteil der Sprache oder ihr offizielles Paket |
| externe Bibliothek | separat installiertes, externes Paket |

## Warum ist es nicht gut, alles selbst zu schreiben?

- langsamer
- kann fehlerhafter sein
- schwerer zu warten
- man dupliziert unnötig das, was bereits fertig und gut gelöst existiert

## Auch den Vertrag einer eingebauten Operation lesen

Aufgabe: Zahlen aufsteigend sortieren, ohne die Eingabe zu verändern, danach
die sortierten Werte verdoppeln. Das Beispiel läuft in Node.js und modernen Browserkonsolen.

<!-- example:run -->

```javascript
const values = [20, 3, 100];
const sorted = [...values].sort((a, b) => a - b);
console.log(JSON.stringify(sorted));
console.log(JSON.stringify(values));
console.log(JSON.stringify(sorted.map(value => value * 2)));
```

```text
[3,20,100]
[20,3,100]
[6,40,200]
```

`sort` verändert das bearbeitete Array; deshalb kopieren wir zuerst.
`(a, b) => a - b` liefert den numerischen Vergleich: Bei negativem Ergebnis kommt
`a` zuerst. `map` erzeugt aus den Rückgabewerten des Callbacks ein neues Array.
In der Dokumentation prüfen wir somit nicht nur die Eingabe, sondern auch
Rückgabe, Seiteneffekte und Voraussetzungen.

Bei JavaScript gehören `Array`, `Math` und `JSON` zur Sprache. DOM und
Dateiauswahldialog des Browsers sind Plattformdienste; `node:fs` gehört zur
Node.js-Basisbibliothek. Nicht jede Umgebung stellt dieselben APIs bereit.
Ein externes Paket ist sinnvoll, wenn es eine konkrete Lücke schließt. Zuerst
prüfen wir vorhandene Werkzeuge, Kompatibilität und Wartungsaufwand.

## Prüfungstaugliche Formulierung

> Die Standard Library ist die Sammlung von standardmäßigen Funktionen, Modulen und Klassen, die zur  
> Programmiersprache gehören.  
> Ihr Zweck ist es, dass der Entwickler häufige Aufgaben mit fertigen Lösungen umsetzen kann, zum Beispiel  
> Dateiverwaltung, Datenverarbeitung, Textverarbeitung oder mathematische Operationen.  
> Die Verwendung der Standard Library ermöglicht eine schnellere, einheitlichere und zuverlässigere Entwicklung.

## Schnelle Selbstkontrolle

1. Was ist eine Standard Library?
2. Warum ist sie nützlich?
3. Nenne drei typische Bereiche, die sie abdecken kann.
4. Was ist der Unterschied zwischen Standard Library und externem Paket?
5. Warum lohnt es sich nicht, alles selbst neu zu schreiben?

## Kurzantworten zur Selbstkontrolle

1. Die offizielle Basisbibliothek der Sprache
2. Weil sie schnellere und zuverlässigere Entwicklung ermöglicht
3. Dateiverwaltung, Datum, Datenstrukturen
4. Die eine ist standardmäßig vorhanden, die andere separat installiert
5. Weil es langsamer und fehleranfälliger sein kann

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Array.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort): numerische Sortierung und Eingabeänderung.


1. Python Docs - The Python Standard Library  
   https://docs.python.org/3/library/index.html  
   Verwendung: offizielle Primärquelle zum Begriff der Standard Library.

2. MDN - Standard built-in objects  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects  
   Verwendung: offizielles, modernes Beispiel dafür, wie eine eingebaute Basisbibliothek einer Sprache in der Praxis aussieht.

Abgerufen: `2026-04-09`
