# Wichtige Datentypen und Datenstrukturen

## Schneller visueller Überblick

| Begriff | Beispiel |
|---|---|
| Datentyp | `int`, `string`, `boolean`, `float` |
| Datenstruktur | Array, Liste, Stack, Queue, Dictionary, Objekt |

## Was ist ein Datentyp?

Der Datentyp bestimmt:

- welchen Wert wir speichern
- welche Operationen darauf ausgeführt werden können
- wie das System die Daten interpretiert

## Wichtige Datentypen

### Ganzzahl

Beispiel:

- `5`
- `-12`

### Gleitkommazahl

Beispiel:

- `3.14`

### Logisch

Beispiel:

- `true`
- `false`

### Text / Zeichenkette

Beispiel:

- `"hello"`

## Was ist eine Datenstruktur?

Die Datenstruktur beschreibt, wie wir Daten so organisieren, dass:

- sie leicht zu verwalten sind
- Suche, Änderung oder Traversierung effizient sind

## Wichtige Datenstrukturen

| Datenstruktur | Wofür geeignet? |
|---|---|
| Array | indizierbare Elementfolge; erlaubte Elementtypen sind sprachabhängig |
| Liste | geordnete Elementfolge |
| Stack | `LIFO`-Logik |
| Queue | `FIFO`-Logik |
| Dictionary / Map | schlüssel-wertbasierte Speicherung |
| Objekt | Organisation zusammengehöriger Daten und Operationen |

## Warum sind sie wichtig?

- ohne den richtigen Datentyp macht das Programm leicht Fehler
- mit guter Datenstruktur entsteht eine schnellere und sauberere Lösung
- sie beeinflussen Speicherverbrauch und Leistung

## Datentyp und Datenstruktur: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Datentyp | eine Datenart |
| Datenstruktur | organisierte Zusammenstellung von Daten |

## Die Datenstruktur passend zur Operation wählen

Aufgabe: Abgeschlossene Themen zählen wir einmal; ihre Titel suchen wir über
Kennungen. Ausführbare Lösung in Node.js:

<!-- example:run -->

```javascript
const completed = new Set(["LAP-15-01", "LAP-15-01", "LAP-15-02"]);
const titles = new Map([["LAP-15-01", "Lifecycle"], ["LAP-15-02", "Paradigms"]]);
console.log(completed.size);
console.log(completed.has("LAP-15-02"));
console.log(titles.get("LAP-15-01"));
```

```text
2
true
Lifecycle
```

`Set` speichert eindeutige Werte, deshalb erhöht das wiederholte `LAP-15-01`
die Anzahl nicht. `Map` liefert einen Wert anhand eines Schlüssels. Sind auch
Lernreihenfolge und Wiederholungen wichtig, können wir Übungsereignisse in einem
separaten Array speichern. Die benötigte Operation begründet die Wahl:
Reihenfolge, Eindeutigkeit oder Suche nach Schlüssel.

„Geordnet“ bedeutet bei einer Liste, dass die Elemente eine Reihenfolge haben,
nicht automatisch aufsteigende Sortierung. Ein JavaScript-`Array` kann verschiedene
Typen enthalten; gleichartige Elemente sind eine Bedingung der jeweiligen Sprache
oder des konkreten Speichertyps. Typen umfassen auch zusammengesetzte Typen.
Datentyp und Datenstruktur sind deshalb keine sich ausschließenden Kategorien.

## Prüfungstaugliche Formulierung

> Der Datentyp bestimmt, welche Art von Daten wir verarbeiten, zum Beispiel Ganzzahl, Text oder logischen Wert.  
> Die Datenstruktur beschreibt hingegen, wie wir Daten organisieren und speichern, zum Beispiel in einem Array, einer  
> Liste, einem Stack oder als Schlüssel-Wert-Paare.  
> Die Wahl des richtigen Datentyps und der richtigen Datenstruktur ist wichtig für die korrekte Funktion und Leistung
> des Programms.

## Schnelle Selbstkontrolle

1. Was ist ein Datentyp?
2. Was ist eine Datenstruktur?
3. Nenne vier wichtige Datentypen.
4. Nenne vier wichtige Datenstrukturen.
5. Warum ist die richtige Wahl wichtig?

## Kurzantworten zur Selbstkontrolle

1. Die Beschreibung der Art der Daten
2. Die organisierte Form der Daten
3. Ganzzahl, Gleitkommazahl, logisch, Text
4. Array, Liste, Stack, Queue
5. Weil es Korrektheit und Leistung beeinflusst

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Keyed collections](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Keyed_collections): Auswahl von Map und Set.


1. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Verwendung: offizielle, moderne Quelle zu den grundlegenden Datentypen.

2. Python Docs - Data Structures  
   https://docs.python.org/3/tutorial/datastructures.html  
   Verwendung: offizielle, gut strukturierte Quelle zur Veranschaulichung gängiger Datenstrukturen.

Abgerufen: `2026-04-09`
