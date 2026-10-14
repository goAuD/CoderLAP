# Aufbau einer Programmiersprache

## Schneller visueller Überblick

| Element | Frage |
|---|---|
| Syntax | Wie schreiben wir es korrekt? |
| Semantik | Was bedeutet die geschriebene Anweisung? |
| Typen | Welche Daten verarbeiten wir? |
| Operatoren | Welche Operationen führen wir aus? |
| Kontrollstrukturen | In welcher Reihenfolge läuft das Programm? |

## Woraus besteht eine Programmiersprache?

Eine Programmiersprache enthält typischerweise:

- **Schlüsselwörter**
- **Bezeichner**
- **Literale**
- **Datentypen**
- **Operatoren**
- **Anweisungen**
- **Kontrollstrukturen**
- häufig **Funktionen**, **Module** oder **Klassen**

## Syntax und Semantik

Dies ist einer der wichtigsten Unterschiede.

| Begriff | Bedeutung |
|---|---|
| Syntax | die korrekte Form und Schreibweise |
| Semantik | die Bedeutung und Funktionsweise der Anweisung |

Beispiel:

- etwas kann syntaktisch korrekt sein
- aber logisch oder semantisch falsch

## Typische Sprachelemente

### Schlüsselwörter

Zum Beispiel:

- `if`
- `while`
- `return`
- `class`

### Bezeichner

Das sind die Namen:

- Variablennamen
- Funktionsnamen
- Klassennamen

### Literale

Direkte Werte, zum Beispiel:

- `42`
- `"hello"`
- `true`

### Operatoren

Zum Beispiel:

- Addition
- Vergleich
- logische Operationen
- Zuweisung

## Woran muss man noch denken?

Zu einer Sprache gehört häufig:

- ein Standard oder eine Sprachreferenz
- ein Compiler oder Interpreter
- eine Standardbibliothek
- eine Laufzeitumgebung

## Einen Ausdruck in Bestandteile zerlegen

Aufgabe: Aus 250 Cent Stückpreis und der als Text gelieferten Menge `"3"`
berechnen wir den Gesamtpreis. Dieses Node.js-Beispiel verwendet eine feste,
gültige Eingabe. Bei Benutzereingaben prüfen wir nach der Umwandlung auch
Wertebereich und Ganzzahligkeit.

<!-- example:run -->

```javascript
const unitCents = 250;
const quantity = Number("3");
const totalCents = unitCents * quantity;
console.log(totalCents);
console.log(typeof quantity, quantity === 3);
```

```text
750
number true
```

| Codeteil | Sprachliche Rolle |
|---|---|
| `const` | Schlüsselwort für die Deklaration |
| `unitCents` | selbst gewählter Bezeichner |
| `250`, `"3"` | Zahlen- beziehungsweise Textliteral |
| `unitCents * quantity` | Ausdruck, der einen Wert liefert |
| `===` | strenger Gleichheitsvergleich |

Die Syntax bestimmt den Aufbau der Deklaration. Die Semantik beschreibt, welche
Operation `*` durchführt und welcher Wert entsteht. `Number` gehört zu den
eingebauten Sprachobjekten; `console` ist ein Dienst der Laufzeitumgebung. Das
`document`-Objekt des Browsers gehört beispielsweise nicht automatisch zu Node.js.

## Prüfungstaugliche Formulierung

> Der Aufbau einer Programmiersprache wird durch die Gesamtheit von Syntax, Semantik und Sprachelementen bestimmt.  
> Dazu gehören beispielsweise Schlüsselwörter, Bezeichner, Literale, Datentypen, Operatoren und Kontrollstrukturen.  
> Die Syntax bestimmt, wie der Code korrekt geschrieben werden muss, die Semantik hingegen, was er bedeutet und wie er
> sich bei der Ausführung verhält.

## Schnelle Selbstkontrolle

1. Was ist Syntax?
2. Was ist Semantik?
3. Welche Sprachelemente kennst du?
4. Was ist der Unterschied zwischen Schlüsselwort und Bezeichner?
5. Warum reicht es nicht, den Code nur "korrekt hinzuschreiben"?

## Kurzantworten zur Selbstkontrolle

1. Die korrekte Form und das Regelwerk
2. Die Bedeutung und Funktionsweise
3. Schlüsselwort, Bezeichner, Literal, Typ, Operator, Anweisung
4. Das Schlüsselwort ist ein reserviertes Sprachelement, der Bezeichner ist ein von uns vergebener Name
5. Weil es logisch noch fehlerhaft sein kann

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types): Literale, Deklarationen und Typumwandlung.


1. MDN - Syntax  
   https://developer.mozilla.org/en-US/docs/Glossary/Syntax  
   Verwendung: offizielle, gut verständliche Grundquelle zum Syntaxbegriff.

2. MDN - Grammar and types  
   https://developer.mozilla.org/docs/Web/JavaScript/Guide/Grammar_and_types  
   Verwendung: zeitgemäßer, strukturierter Überblick über typische Bausteine einer Programmiersprache.

Abgerufen: `2026-04-09`
