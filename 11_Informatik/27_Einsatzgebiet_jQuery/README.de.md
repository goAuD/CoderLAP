# Einsatzgebiet jQuery

## Schneller visueller Überblick

| Ältere typische Verwendung | Beispiel |
|---|---|
| DOM-Manipulation | Elemente auswählen und ändern |
| Ereignisbehandlung | Klick, Formular-Ereignis |
| Ajax | Serveraufruf ohne Seitenaktualisierung |
| Animation | einfache Effekte |

## Wofür wurde jQuery verwendet?

Am häufigsten:

- zum Auswählen von HTML-Elementen
- zum Ändern des DOM
- zur Ereignisbehandlung
- für Ajax-Aufrufe
- für einfache UI-Effekte

Es wurde populär, weil es viele frühe browserübergreifende Probleme vereinfachte.

## Warum war es eine große Sache?

Weil natives JavaScript früher:

- umständlicher war
- in verschiedenen Browsern unterschiedlich funktionierte
- mehr Code für das gleiche Ergebnis benötigte

jQuery machte dies lange Zeit viel einfacher.

## Wie sieht es heute aus?

Stand: `14. Oktober 2026`.

- moderne Browser lösen viele frühere jQuery-Aufgaben auch mit nativen APIs
- jQuery ist weiterhin gepflegt und wird in bestehenden Websites und CMS eingesetzt

## Wann trifft man es noch an?

- in Legacy-Webseiten
- in alten Admin-Oberflächen
- in CMS-Templates
- bei kleineren, schnell zusammengesetzten Frontend-Aufgaben

## jQuery und JavaScript: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| JavaScript | Programmiersprache |
| jQuery | JavaScript-Library |

## Dieselbe Aufgabe mit jQuery und nativer DOM-API

**Browserumgebung:** Das folgende HTML befindet sich bereits auf der Seite,
JavaScript läuft danach. Die erste Lösung benötigt geladenes jQuery:

```html
<button id="ready" type="button">Bereit</button>
<p id="status" role="status"></p>
```

```javascript
$("#ready").on("click", () => {
  $("#status").text("Die Übung kann beginnen.");
});
```

Nach Aktivieren des Buttons lautet der Absatz `Die Übung kann beginnen.`.
`$` wählt Elemente aus, `on` verbindet ein Ereignis und `text` setzt Text.
Die getrennte Alternative ohne jQuery für dieselbe Aufgabe lautet:

```javascript
document.querySelector("#ready").addEventListener("click", () => {
  document.querySelector("#status").textContent = "Die Übung kann beginnen.";
});
```

Wir verwenden eine der beiden JavaScript-Varianten. Textdaten werden mit `text`
oder `textContent` angezeigt, weil beide sie nicht als HTML interpretieren.
Baut ein Projekt bereits auf jQuery und getesteten Plugins auf, kann deren
Wartung sinnvoll sein. Für einen einzelnen solchen Button genügt auch die
Browser-API ohne zusätzliche Abhängigkeit.

**Stand 2026-10-14:** jQuery ist kein eingestelltes Projekt. Version 4.0.0 wurde
offiziell am 17. Januar 2026 veröffentlicht. Bei einem Hauptversionswechsel
prüfen wir Kompatibilität und Plugins. Die Existenz des Projekts bedeutet nicht,
dass beliebige ältere Versionen sicher oder für jeden modernen Browser nötig sind.

## Prüfungstaugliche Formulierung

> jQuery ist eine JavaScript-Library,
> die DOM-Manipulation, Ereignisbehandlung
> und Ajax-basierte Kommunikation vereinfacht.
> Historisch spielte es eine sehr wichtige Rolle in der Webentwicklung,
> besonders bei der Bewältigung browserübergreifender Kompatibilitätsprobleme.
> Heute ist seine Rolle geringer, aber in alten Systemen und bei einfacheren Webaufgaben kommt es immer noch vor.

## Schnelle Selbstkontrolle

1. Was ist jQuery?
2. Wofür wurde es am häufigsten verwendet?
3. Warum wurde es populär?
4. Wie sieht es heute aus?
5. Worin unterscheidet es sich von JavaScript?

## Kurzantworten zur Selbstkontrolle

1. Eine JavaScript-Library
2. Für DOM, Ereignisse, Ajax-Behandlung
3. Weil es die browserübergreifende Webentwicklung vereinfachte
4. Gepflegte Library; ihr Bedarf hängt vom Projekt und den verfügbaren nativen APIs ab
5. JavaScript ist eine Sprache, jQuery eine darauf aufbauende Library

## Quellen

Geprüft: `2026-10-14`.

- [jQuery: 4.0.0 release](https://blog.jquery.com/2026/01/17/jquery-4-0-0/): Wartungsstatus und Hauptversionswechsel.
- [jQuery: text()](https://api.jquery.com/text/): Textänderung im DOM.


1. jQuery official site
   https://jquery.com/
   Verwendung: offizielle Beschreibung, wofür jQuery gedacht ist.

2. jQuery API Documentation
   https://api.jquery.com/
   Verwendung: offizielle Referenz der Hauptfunktionen von jQuery.

3. Stack Overflow Developer Survey 2025 - Web frameworks and technologies
   https://survey.stackoverflow.co/2025/technology/
   Verwendung: historische Nutzungsumfrage von 2025; den heutigen Supportstatus prüfen wir anhand der offiziellen Veröffentlichung.

Abgerufen: `2026-04-08`
