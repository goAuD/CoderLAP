# Einsatzgebiet AngularJS

## Schneller visueller Überblick

| Frage | Antwort |
|---|---|
| Wofür wurde es verwendet? | für dynamische Webanwendungen |
| Wann war es stark? | in der frühen SPA-Welle |
| Aktueller Status? | Legacy-Technologie |
| Für neue Projekte? | nicht empfohlen |

## Wofür wurde AngularJS verwendet?

Typischerweise:

- `single-page application` (`SPA`)
- dynamische Formulare
- Datenbindung
- clientseitiges Routing
- komplexere Admin- oder Geschäftsoberflächen

AngularJS wurde damals populär, weil es:

- dynamische Oberflächen einfacher machte
- Datenbindung und Dependency Injection bot
- den Frontend-Code strukturierter machte

## Warum war es historisch wichtig?

Weil es in der frühen modernen Frontend-Ära ein großer Schritt war:

- weniger manuelle DOM-Manipulation
- modulareres Denken
- stärkere clientseitige Logik

## Wie sieht es heute aus?

Stand: `14. Oktober 2026`.

- AngularJS gilt als alte Technologie
- die offizielle Unterstützung wurde bereits eingestellt
- stattdessen sind das aktiv unterstützte `Angular` oder andere moderne Frameworks üblich

## Wann trifft man es noch an?

- in alten Unternehmenssystemen
- in Legacy-Admin-Oberflächen
- in Projekten, die noch nicht migriert wurden

In solchen Fällen ist die Aufgabe häufig nicht Neuentwicklung, sondern:

- Wartung
- Fehlerbehebung
- schrittweise Ablösung

## AngularJS und Angular: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| AngularJS | alt, 1.x-Linie, nicht mehr unterstützt |
| Angular | neuer, aktiv unterstütztes Framework |

## Eine ältere Vorlage erkennen

Das folgende **Lesebeispiel** zeigt AngularJS-1.x-Syntax. Es würde nur in einer
Umgebung mit bereits geladenem AngularJS funktionieren. Es ist keine eigenständige
HTML-Demo und kein Anlass, die nicht mehr unterstützte Bibliothek in einem neuen
Projekt zu installieren.

```html
<div ng-app>
  <label for="legacy-name">Name</label>
  <input id="legacy-name" ng-model="name">
  <p>Hallo {{ name }}</p>
</div>
```

`ng-app` kennzeichnet den Anwendungsbereich. `ng-model` verbindet den Feldwert
mit dem Modellwert `name`. Das Framework wertet `{{ name }}` aus. Gibt die
Person `Anna` ein, wird der Absatz zu `Hallo Anna`. Dafür ist keine eigene
`textContent`-Änderung nötig.

Das zeigt den Vorteil von Data Binding. Das clientseitige Modell befindet sich
aber weiterhin in der Umgebung der Benutzer. Der Server muss Eingaben und
Berechtigungen unabhängig prüfen.

Bei Wartung erfassen wir zunächst Routen, Formulare, Abhängigkeiten und
API-Verträge. Wichtige Verhaltensweisen werden durch Tests festgehalten.
Danach lässt sich die Oberfläche schrittweise ablösen. Das heutige Angular ist
ein anderes, komponentenbasiertes Framework. Der Umstieg ist nicht nur eine
Erhöhung der AngularJS-Paketversion. Für den Prüfungskatalog erkennen und
erklären wir die ältere Technik. Unterstützungsentscheidungen richten sich
jedoch nach dem Herstellerlebenszyklus.

## Prüfungstaugliche Formulierung

> AngularJS ist ein älteres JavaScript-basiertes Frontend-Framework,
> das hauptsächlich für dynamische Single-Page-Webanwendungen verwendet wurde.
> Historisch spielte es eine wichtige Rolle
> bei der Entstehung der modernen Frontend-Entwicklung,
> aber die offizielle Unterstützung endete im Januar 2022.
> Daher wird es für neue Projekte heute nicht mehr empfohlen, man trifft es eher bei der Wartung alter Systeme an.

## Schnelle Selbstkontrolle

1. Wofür wurde AngularJS verwendet?
2. Was ist sein Status heute?
3. Was ist der Unterschied zwischen AngularJS und Angular?
4. Wo kann es noch vorkommen?
5. Wird es für neue Projekte empfohlen?

## Kurzantworten zur Selbstkontrolle

1. Für dynamische SPAs
2. Legacy, nicht mehr unterstützt
3. AngularJS ist alt, Angular ist modern und unterstützt
4. In alten Unternehmenssystemen
5. Nein

## Quellen

Geprüft: `2026-10-14`.

- [AngularJS: official status](https://angularjs.org/): offizielles Supportende seit Januar 2022 und Data Binding.
- [Angular: overview](https://angular.dev/overview): heutiges Angular als separates komponentenbasiertes Framework.


1. AngularJS official site
   https://angularjs.org/
   Verwendung: offizieller Status und Beschreibung der Rolle von AngularJS;
   die Hauptseite zeigt klar an,
   dass die Unterstützung im Januar 2022 endete.

2. Stack Overflow Developer Survey 2025 - Technology
   https://survey.stackoverflow.co/2025/technology/
   Verwendung: historische Nutzungsumfrage von 2025. Quelle für den Supportstatus ist die offizielle AngularJS-Seite.

Abgerufen: `2026-04-08`
