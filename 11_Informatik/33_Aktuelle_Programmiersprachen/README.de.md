# Aktuelle Programmiersprachen

## Schneller visueller Überblick

| Sprache | Typische Stärke |
|---|---|
| JavaScript / TypeScript | Web-Frontend und viele Backends |
| Python | Automatisierung, Backend, Daten, AI |
| Java | Enterprise, Backend |
| C# | .NET, Web, Unternehmensentwicklung |
| PHP | klassisches und modernes Web-Backend |
| Kotlin | Android und Backend |
| Swift | Apple-Plattformen |
| Dart | Flutter |

## Was bedeutet "aktuell"?

Nicht "neu", sondern, dass:

- die Sprache heute noch weit verbreitet verwendet wird
- ein aktives Ökosystem vorhanden ist
- aktuelle Dokumentation, Tooling und Community existieren
- sie eine realistische Wahl für neue Projekte ist

## Anhand welcher Kriterien gilt eine Sprache heute als wichtig?

- wie stark sie in der Praxis verwendet wird
- in wie vielen Entwicklungsbereichen sie auftaucht
- wie aktiv ihr Ökosystem ist
- ob es moderne Frameworks und Werkzeuge dafür gibt
- wie leicht man damit Fachkräfte findet und im Team arbeiten kann

## Typische Hauptgruppen 2026

### Web und Internet

- `JavaScript`
- `TypeScript`
- `PHP`
- `Java`
- `C#`
- `Python`

### Mobil

- `Kotlin`
- `Swift`
- `Dart`
- `JavaScript` / `TypeScript` in Cross-Platform-Umgebungen

### Allgemein und Backend

- `Python`
- `Java`
- `C#`
- `Go`
- `PHP`

## Warum gibt es keine einzige "beste" Sprache?

Weil die Wahl davon abhängt:

- für welche Plattform man entwickelt
- welches Team daran arbeitet
- welche Leistung benötigt wird
- welches Ökosystem vorteilhaft ist
- an welches bestehende System man sich anpassen muss

## Worauf muss man in der Prüfung achten?

Wenn die Frage "aktuelle Sprachen" lautet, sollte man:

- nicht nur eine nennen
- sie an Bereiche knüpfen
- zeigen, dass heute mehrere Hauptrichtungen gleichzeitig vorhanden sind

## Sprache, Laufzeit und Framework haben verschiedene Aufgaben

| Element | Was ist es? | Beispiel für den Zusammenhang |
|---|---|---|
| JavaScript | Programmiersprache auf Grundlage des ECMAScript-Standards | läuft beispielsweise in Node.js oder im Browser |
| Node.js | JavaScript-Laufzeitumgebung | etwa für serverseitigen Code |
| TypeScript | Sprache auf JavaScript-Basis mit statischer Typprüfung | Typangaben bleiben normalerweise nicht im ausgeführten JavaScript |
| React / Angular | UI-Library / Webframework | Werkzeuge für JavaScript- oder TypeScript-Projekte |

**Illustrativer TypeScript-Quelltext**, beispielsweise im TypeScript Playground
übersetzbar:

```typescript
function greet(name: string): string {
  return `Hallo ${name}`;
}
console.log(greet("Ada"));
```

Die JavaScript-Fassung ohne Typangaben läuft eigenständig in Node.js:

<!-- example:run -->

```javascript
function greet(name) {
  return `Hallo ${name}`;
}
console.log(greet("Ada"));
```

```text
Hallo Ada
```

`name: string` hilft während der Entwicklung, Aufrufe zu prüfen. JSON aus dem
Netzwerk muss trotzdem zur Laufzeit geprüft werden: Ein TypeScript-Typ wandelt
externe Daten weder um noch bestätigt er ihre Gültigkeit. Typprüfung, Tests
und Eingabevalidierung beantworten unterschiedliche Fragen.

**Begründete Wahl:** Bei der Erweiterung eines Formulars auf einer kleinen
bestehenden PHP-Seite kann das Beibehalten einer gepflegten PHP-Umgebung einfach
sein. Für Android-spezifische Gerätefunktionen können Kotlin und die Plattform-API
passen. Unterstützte Versionen, Teamwissen, Betrieb und Aufgabe sind aussagekräftiger
als eine einzelne Beliebtheitsrangliste. Die Aufzählung hier ist weder vollständig
noch eine Rangfolge.

## Prüfungstaugliche Formulierung

> Mit Stand `14. Oktober 2026` zählen zu den aktuellen Programmiersprachen jene,
> die heute noch weit verbreitet und aktiv unterstützt werden.
> In der Web-, Mobil- und Unternehmensentwicklung
> sind beispielsweise JavaScript, TypeScript, Python, Java,
> C#, PHP, Kotlin und Swift besonders wichtig.
> Es gibt keine einzige "beste" Sprache, die Wahl hängt immer von der Aufgabe, der Plattform und dem Ökosystem ab.

## Schnelle Selbstkontrolle

1. Was bedeutet hier "aktuell"?
2. Nenne mindestens fünf heute relevante Sprachen.
3. Welche sind in der Mobilentwicklung wichtig?
4. Warum gibt es keine einzige beste Sprache?
5. Welche Rolle spielt das Ökosystem?

## Kurzantworten zur Selbstkontrolle

1. Heute noch weit verbreitet und unterstützt
2. Zum Beispiel JavaScript, TypeScript, Python, Java, C#
3. Kotlin, Swift, Dart
4. Weil es von der Aufgabe abhängt
5. Es bestimmt die Nutzbarkeit und die Entwicklungsumgebung

## Quellen

Geprüft: `2026-10-14`.

- [TypeScript Handbook: The Basics](https://www.typescriptlang.org/docs/handbook/2/basic-types.html): Typprüfung und Entfernen von Typangaben beim Übersetzen.
- [Android Developers: Kotlin-first](https://developer.android.com/kotlin/first): Beispiel einer aufgaben- und plattformabhängigen Sprachwahl.


1. Stack Overflow Developer Survey 2025 - Technology
   https://survey.stackoverflow.co/2025/technology/
   Verwendung: historische Momentaufnahme der Nutzung unter den Befragten von 2025, keine vollständige Marktrangliste oder Bestätigung des heutigen Supports.

2. TypeScript
   https://www.typescriptlang.org/
   Verwendung: offizielle Quelle des in der modernen Webentwicklung wichtigen TypeScript.

3. Python Documentation
   https://docs.python.org/3/
   Verwendung: offizielle Quelle des aktuellen, aktiv unterstützten Python-Ökosystems.

4. Oracle Java
   https://www.oracle.com/java/
   Verwendung: offizieller Einstiegspunkt des Java-Ökosystems.

5. .NET Languages
   https://dotnet.microsoft.com/en-us/languages
   Verwendung: offizielle Quelle des modernen .NET- und C#-Sprachökosystems.

Abgerufen: `2026-04-08`
