# Schreibtischtest

## Schneller visueller Überblick

```text
Eingabe angeben
    -> Schritte manuell nachverfolgen
    -> Werte der Variablen beobachten
    -> Ergebnis überprüfen
```

## Was bedeutet hier Schreibtischtest?

Das bedeutet typischerweise:

- man nimmt eine Eingabe
- verfolgt den Algorithmus Schritt für Schritt
- beobachtet die Werte der Variablen
- überprüft, ob das erwartete Ergebnis herauskommt

Häufig auch bezeichnet als:

- Dry Run
- Manual Tracing
- manuelle Überprüfung

## Wozu ist er gut?

- zum Erkennen einfacher logischer Fehler
- zum Verstehen von Schleifen und Verzweigungen
- zum Überprüfen von Algorithmen
- zum Lernen und zur Prüfungsvorbereitung

## Wann ist er besonders nützlich?

- bevor man das Programm tatsächlich ausführt
- wenn ein Algorithmus auf Papier vorgeführt werden muss
- wenn man die Logik schnell überprüfen will

## Worauf muss man achten?

- er zeigt nicht alle Laufzeitfehler
- er ersetzt nicht das Testen mit echten Testdaten
- er ersetzt nicht automatisierte Tests

## Schreibtischtest und Code Review: nicht verwechseln

| Begriff | Fokus |
|---|---|
| Schreibtischtest | manuelles Nachverfolgen eines Algorithmus oder Codeabschnitts |
| Code Review | fachliche Überprüfung durch eine andere Person |

## Eine Wertetabelle für eine Schleife

Verfolge den Code zunächst auf Papier und vergleiche erst danach mit der tatsächlichen Ausführung:

<!-- example:run -->
```javascript
function sum(values) {
  let total = 0;
  for (let i = 0; i < values.length; i++) {
    total += values[i];
  }
  return total;
}

console.log(sum([2, 4, 1]));
console.log(sum([]));
```

```text
7
0
```

| Schritt | i | Bedingung | total nach dem Schritt |
|---|---:|---|---:|
| Initialisierung | 0 | noch nicht geprüft | 0 |
| erste Prüfung und Addition | 0 | 0 < 3 wahr | 2 |
| zweite Prüfung und Addition | 1 | 1 < 3 wahr | 6 |
| dritte Prüfung und Addition | 2 | 2 < 3 wahr | 7 |
| vierte Bedingungsprüfung | 3 | 3 < 3 falsch | 7 |

Der Schleifenrumpf läuft dreimal, die Bedingung wird viermal geprüft. `i++` erhöht den Index nach dem Rumpf. Bei einer leeren Liste ist bereits die erste Bedingung falsch; der Anfangswert 0 wird zurückgegeben. Die manuelle Spur zeigt Grenzen, ersetzt aber keine gesonderte Prüfung von Umgebungsproblemen oder paralleler Ausführung.

## Prüfungstaugliche Formulierung

> Der Schreibtischtest ist eine manuelle logische Überprüfung,
> bei der das Programm oder der Algorithmus ohne Ausführung
> Schritt für Schritt nachverfolgt wird.  
> Dabei werden anhand von Eingaben, Verzweigungen, Schleifen und Variablenwerten die erwarteten Ergebnisse überprüft.  
> Dies ist eine gute Methode zur Früherkennung logischer Fehler, ersetzt aber nicht das eigentliche Testen.

## Schnelle Selbstkontrolle

1. Was ist das Wesen des Schreibtischtests?
2. Welche Fehler hilft er zu erkennen?
3. Warum ist er bei Algorithmen nützlich?
4. Warum reicht er allein nicht aus?
5. Was ist der Unterschied zum Code Review?

## Kurzantworten zur Selbstkontrolle

1. Manuelles logisches Nachverfolgen
2. Hauptsächlich logische Fehler
3. Weil er Schritte und Zustände sichtbar macht
4. Weil es keine tatsächliche Ausführung ist
5. Das eine ist ein manueller Dry Run, das andere eine fachliche Überprüfung

## Quellen

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Statisches und dynamisches Testen, Testentwurfsverfahren und Abdeckung.

- [MDN: for statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)  
  Reihenfolge von Initialisierung, Bedingung und Aktualisierung.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Verwendung: offizieller Hintergrund zum statischen Testen und reviewartigen Frühprüfungen.

2. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Verwendung: offizieller begrifflicher Hintergrund zu statischen Prüftechniken.

Anmerkung: Die Formulierung `Schreibtischtest` folgt hier
der in der Prüfungspraxis verwendeten Bedeutung
eines manuellen `Dry Run` / logischen Nachverfolgens.

Abgerufen: `2026-04-08`
