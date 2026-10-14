# Coding Standards und Code Konventionen

## Schneller visueller Überblick

| Bereich | Beispiel |
|---|---|
| Namensgebung | `camelCase`, `PascalCase` |
| Formatierung | Einrückung, Zeilenumbruch |
| Struktur | Dateiaufbau, Funktionsgröße |
| Qualität | Linter, Formatter, Regeln |

## Warum ist das wichtig?

- Code ist leichter zu lesen
- Teamarbeit wird einheitlicher
- weniger Missverständnisse
- einfacheres Review
- bessere Wartbarkeit

## Standard und Konvention: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Coding Standard | formaleres, erwartetes Regelwerk |
| Code Convention | etablierte gemeinsame Gewohnheit oder Richtlinie |

In der Praxis verschwimmen sie oft, aber das Wesentliche ist gleich: der Code soll konsistent sein.

## Welche Bereiche betrifft es?

- Variablennamen
- Klassennamen
- Dateistruktur
- Kommentierung
- Fehlerbehandlung
- Import-Sortierung
- Whitespace und Einrückung

## Wie setzt man es durch?

- Team Agreement
- Code Review
- Linter
- Formatter
- `.editorconfig`
- CI-Prüfungen

## Warum ist es nicht nur eine "Schönheitsfrage"?

Weil schlecht vereinheitlichter Code:

- das Team verlangsamt
- die Fehlerwahrscheinlichkeit erhöht
- das Onboarding erschwert

## Ein kleines Team mit überprüfbaren Vereinbarungen

**Beispiel:** Das Team verwendet für JavaScript zwei Leerzeichen Einrückung,
UTF-8-Dateien und LF-Zeilenenden. Eine `.editorconfig` im Repository-Wurzelordner
kann dies festhalten:

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true

[*.js]
indent_style = space
indent_size = 2
```

Ein Editor mit EditorConfig-Unterstützung sucht vom geöffneten Dokument nach
oben nach Konfigurationen; `root = true` beendet diese Suche. Für eine `.js`-Datei
gelten sowohl der allgemeine als auch der JavaScript-Abschnitt. Die Datei
allein führt keine CI-Prüfung aus und korrigiert keine Geschäftslogik.

| Werkzeug oder Regel | Welche Aussage liefert es? | Konkretes Beispiel |
|---|---|---|
| Formatter | vereinbartes Format | einheitliche Einrückung und Umbrüche |
| Linter | Einhaltung aktivierter Regeln | ungenutzte Variable oder nicht definierter Name |
| Typprüfung | Beziehungen gemäß beschriebenen Typen | ungeeignetes Argument für einen Zahlenparameter |
| Test | erwartetes Verhalten für bestimmte Eingaben | 0 Minuten ergeben 0 Sekunden |
| Review | menschliche Bewertung von Absicht und Umsetzung | Sind Datenverarbeitung und Änderungsgrund nachvollziehbar? |

Namen sollen auch Einheiten ausdrücken: `durationSeconds` oder `priceCents`
sind genauer als ein einzelnes `value`. Ein Kommentar erklärt bevorzugt einen
nicht offensichtlichen Grund, statt die Anweisung zu wiederholen. Formatänderungen
lassen sich von Verhaltensänderungen trennen, damit der Diff übersichtlich bleibt.
Stilfragen werden einmal in der gemeinsamen Konfiguration geklärt; danach kann
sich das Review auf die Aufgabe konzentrieren. Ein grünes Lintergebnis beweist
nicht die allgemeine Korrektheit.

## Prüfungstaugliche Formulierung

> Coding Standards und Code Conventions sind gemeinsame Regeln, die den Quellcode einheitlicher und besser lesbar machen.
> Dazu gehören zum Beispiel Namensgebung, Formatierung, Struktur, Kommentierung und die Nutzung von Codequalitätsregeln.
> Diese sind besonders bei Teamarbeit wichtig, weil sie Review, Wartung und Zusammenarbeit erleichtern.

## Schnelle Selbstkontrolle

1. Warum sind Code-Konventionen wichtig?
2. Welche Bereiche können sie regeln?
3. Was ist die Rolle des Linters?
4. Was ist die Rolle des Formatters?
5. Warum unterstützen sie das Code Review?

## Kurzantworten zur Selbstkontrolle

1. Sie sorgen für einheitlicheren und lesbareren Code
2. Namensgebung, Formatierung, Struktur usw.
3. Er zeigt Regelverstöße und Fehler an
4. Er formatiert den Code einheitlich
5. Weil weniger Rauschen bleibt und das Wesentliche besser sichtbar ist

## Quellen

Geprüft: `2026-10-14`.

- [EditorConfig](https://editorconfig.org/): Dateibezogene Konfiguration und Suchreihenfolge.
- [ESLint: Core concepts](https://eslint.org/docs/latest/use/core-concepts/): Regelbasierte statische Prüfung.
- [Prettier: Prettier vs. Linters](https://prettier.io/docs/comparison): Rolle von Formatierung und Qualitätsregeln.


1. EditorConfig
   https://editorconfig.org/
   Verwendung: Werkzeug zur projektweiten Vereinheitlichung von Formatierungskonventionen.

2. PEP 8 - Style Guide for Python Code
   https://peps.python.org/pep-0008/
   Verwendung: bekanntes offizielles Styleguide-Beispiel einer Programmiersprache.

3. Microsoft Learn - C# coding conventions
   https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions
   Verwendung: offizielles Beispiel für die praktische Anwendung von Code-Konventionen.

4. typescript-eslint shared configs
   https://typescript-eslint.io/users/configs/
   Verwendung: moderner TypeScript-Regelungs- und Linting-Kontext.

Abgerufen: `2026-04-08`
