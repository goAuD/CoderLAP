# Erste drei Normalformen

## Schneller visueller Überblick

| Normalform | Kern |
|---|---|
| `1NF` | keine Wiederholungsgruppen, ein Wert pro Zelle |
| `2NF` | keine partielle Abhängigkeit bei zusammengesetztem Schlüssel |
| `3NF` | keine transitive Abhängigkeit zwischen Nicht-Schlüsselfeldern |

## Warum ist Normalisierung nötig?

Weil sie hilft:

- Redundanz zu reduzieren
- Dateninkonsistenzen zu vermeiden
- die Wartung zu erleichtern

## `1NF` - Erste Normalform

In einem Feld soll nur **ein einziger atomarer Wert** stehen.

Nicht gut ist zum Beispiel:

- mehrere Telefonnummern in einem Feld, durch Komma getrennt

## `2NF` - Zweite Normalform

Die Tabelle soll in `1NF` sein, und jedes Nicht-Schlüsselfeld soll vom **gesamten Schlüssel** abhängen.

Das ist besonders bei zusammengesetzten Schlüsseln wichtig.

Wenn ein Feld nur von einem Teil des Schlüssels abhängt, muss es in eine eigene Tabelle ausgelagert werden.

## `3NF` - Dritte Normalform

Die Tabelle soll in `2NF` sein, und die Nicht-Schlüsselfelder **dürfen nicht von anderen Nicht-Schlüsselfeldern abhängen**.

Das heißt:

- die Nicht-Schlüsselfelder sollen vom Schlüssel abhängen
- nicht voneinander

## Einfaches Beispiel

Wenn in einer `Products`-Tabelle Folgendes steht:

- `ProductID`
- `SRP`
- `Discount`

und `Discount` von `SRP` abhängt und nicht direkt vom Schlüssel, dann kann das eine Verletzung der `3NF` sein.

## Worauf muss man bei der Prüfung achten?

- nicht nur die Definition nennen, sondern auch das Ziel
- bei der `2NF` ist der zusammengesetzte Schlüssel wichtig
- bei der `3NF` ist die transitive Abhängigkeit das Schlüsselwort

## Prüfungstaugliche Formulierung

> Die ersten drei Normalformen gehören zu den Grundprinzipien des relationalen Datenbankentwurfs.  
> Die erste Normalform besagt, dass in einem Feld nur ein Wert stehen darf; die zweite Normalform schließt partielle  
> Abhängigkeiten bei zusammengesetzten Schlüsseln aus; die dritte Normalform verbietet, dass Nicht-Schlüsselfelder von  
> anderen Nicht-Schlüsselfeldern abhängen.  
> Diese Regeln reduzieren die Redundanz und verbessern die Datenkonsistenz.

## Häufige Prüfungsfehler

- `1NF` nur als "geordnete Tabelle" bezeichnen.
- Bei der `2NF` den zusammengesetzten Schlüssel weglassen.
- `3NF` mit `2NF` verwechseln.
- Die transitive Abhängigkeit nicht erwähnen.

## Schnelle Selbstkontrolle

1. Was ist der Kern der `1NF`?
2. Wann ist die `2NF` besonders wichtig?
3. Was verbietet die `3NF`?
4. Warum ist Normalisierung sinnvoll?
5. Was ist eine transitive Abhängigkeit in Kurzform?

## Kurzantworten zur Selbstkontrolle

1. Ein Wert pro Feld
2. Bei zusammengesetzten Schlüsseln
3. Abhängigkeiten von Nicht-Schlüsselfeldern untereinander
4. Weil sie Redundanz und Fehler reduziert
5. Wenn ein Nicht-Schlüsselfeld von einem anderen Nicht-Schlüsselfeld abhängt

## Quellen

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Verwendung: offizielle, gut verständliche Erklärung der ersten drei Normalformen.

2. Microsoft Learn - Description of the database normalization basics  
   https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/access/database-normalization-description  
   Verwendung: offizieller Hintergrund zum Zweck der Normalisierung und zur praktischen Interpretation von `1NF`, `2NF`,
   `3NF`.

Abgerufen: `2026-04-09`
