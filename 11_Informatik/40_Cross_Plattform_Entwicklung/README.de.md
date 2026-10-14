# Cross Plattform Entwicklung

## Schneller visueller Überblick

| Ansatz | Wesentlich |
|---|---|
| nativ | für jede Plattform eine separate Lösung |
| Cross-Platform | gemeinsamer oder teilweise gemeinsamer Code |

## Warum ist das gut?

- weniger duplizierte Entwicklung
- schnellerer Markteintritt
- einfacher, mehrere Plattformen gleichzeitig zu unterstützen
- auch ein kleineres Team kann mehr abdecken

## Wo wird es eingesetzt?

- bei Mobile-Apps
- bei Desktop + Mobil-Kombinationen
- bei Multi-Device-Produkten

## Typische Technologien

- `Flutter`
- `React Native`
- `.NET MAUI`

## Welche Kompromisse gibt es?

- das volle native Erlebnis wird nicht immer erreicht
- bestimmte plattformspezifische Funktionen sind schwieriger
- Leistungsunterschiede können auftreten
- manchmal ist auch separater Plattformcode nötig

## Cross-Platform und responsives Web: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Cross-Platform-App-Entwicklung | Anwendung für mehrere Plattformen |
| responsives Web | eine Webseite passt sich an den Bildschirm an |

## Wann ist es eine gute Wahl?

- wenn mehrere Plattformen schnell abgedeckt werden müssen
- wenn Kosten und Entwicklungszeit stark zählen
- wenn der Großteil der Funktionen plattformunabhängig ist

## Wann ist es weniger gut?

- wenn sehr tiefe native Integration nötig ist
- wenn plattformspezifische UI der Schlüssel ist
- wenn maximale Leistung an erster Stelle steht

## Was teilen wir, und was prüfen wir je Plattform?

Punkteberechnung und Fragenmodell eines Quiz lassen sich gut teilen. Oberfläche,
lokaler Speicher, Benachrichtigungen und Zurücknavigation können dagegen je
Plattform unterschiedlich sein. Gemeinsame Regeln lassen sich von der Plattform-API
trennen:

```text
gemeinsame Quizlogik
  -> abstrakte Speicheroperation
     -> Web: Browser-Speicher
     -> Android/iOS: passende lokale Speicher-API
```

Dies ist eine illustrative Schichtung, keine Pflicht zu einem neuen Framework.
Zwei kleine, verständliche Plattformdateien können einfacher sein als eine
Riesenfunktion voller Bedingungen. React Native unterstützt beispielsweise
`.ios`- und `.android`-Dateivarianten; Aufrufer können dieselbe Schnittstelle nutzen.

| Prüfung | Warum auch bei derselben Funktion nötig? |
|---|---|
| Dateiname und Pfad | Groß-/Kleinschreibung kann je Dateisystem anders behandelt werden |
| UTF-8 und Zeilenenden | Exporte mit Umlauten und Texte aus verschiedenen Systemen |
| Zeitpunkt | Zeitzone und Sommerzeit beeinflussen die lokale Anzeige |
| verweigerte Berechtigung | auch ohne Kamera oder Benachrichtigung ist ein verständlicher Zustand nötig |
| Tastatur und Navigation | Bildschirmtastatur, Zurücknavigation und Desktop-Fokus unterscheiden sich |
| schwaches Gerät und Netzwerk | gemessen wird tatsächliche Leistung, nicht der Frameworkname |

Für Dateisystempfade verwenden wir in Node.js passende Werkzeuge aus `node:path`.
Eine HTTP-URL bauen wir dagegen nicht wie einen Dateisystempfad auf. Cross-Platform
ist nicht zwangsläufig langsam, nativ ist nicht automatisch schnell. Aufgabe,
Implementierung und Messung entscheiden. Auch eine Webapp kann auf mehreren
Plattformen laufen; responsives Design bezeichnet darin die Layoutanpassung,
nicht die Lösung sämtlicher Plattformunterschiede.

## Prüfungstaugliche Formulierung

> Ziel der Cross-Platform-Entwicklung ist es,
> aus einer gemeinsamen oder weitgehend gemeinsamen Codebasis
> Anwendungen für mehrere Plattformen erstellen zu können.
> Ihr Vorteil ist schnellere Entwicklung und weniger Duplikation,
> ihr Nachteil ist,
> dass in bestimmten Fällen Kompromisse beim nativen Erlebnis,
> bei der Leistung oder bei plattformspezifischen Funktionen nötig sind.
> Typische Beispiele sind Flutter, React Native und .NET MAUI.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche der Cross-Platform-Entwicklung?
2. Was ist ein Hauptvorteil?
3. Was ist ein Hauptnachteil?
4. Nenne drei typische Technologien.
5. Worin unterscheidet sie sich vom responsiven Web?

## Kurzantworten zur Selbstkontrolle

1. Wir entwickeln mit gemeinsamer Codebasis für mehrere Plattformen
2. Weniger Duplikation und schnellere Entwicklung
3. Kompromisse beim nativen Erlebnis oder bei Funktionen
4. Flutter, React Native, .NET MAUI
5. Cross-Platform unterstützt mehrere Plattformen; Responsive Design behandelt die Anpassung des Web-Layouts

## Quellen

Geprüft: `2026-10-14`.

- [React Native: Platform-specific code](https://reactnative.dev/docs/platform-specific-code): Umgang mit gemeinsamem und unterschiedlichem Plattformcode.
- [Node.js: Path](https://nodejs.org/api/path.html): Unterschiedliche Behandlung von Windows- und POSIX-Dateipfaden.


1. Flutter
   https://flutter.dev/
   Verwendung: offizielle Cross-Platform-Entwicklungsplattform.

2. React Native
   https://reactnative.dev/
   Verwendung: offizielle JavaScript/TypeScript-basierte Cross-Platform-Mobile-Technologie.

3. .NET MAUI
   https://dotnet.microsoft.com/en-us/apps/maui
   Verwendung: offizielle .NET-Multiplattform-Entwicklungsrichtung.

Abgerufen: `2026-04-08`
