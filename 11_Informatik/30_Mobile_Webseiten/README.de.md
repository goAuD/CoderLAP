# Mobile Webseiten

## Schneller visueller Überblick

| Wichtiger Aspekt | Beispiel |
|---|---|
| kleines Display | einfacheres Layout |
| Berührung | größere Buttons |
| Mobilnetz | schnelleres Laden |
| Lesbarkeit | angemessene Schriftgröße |

## Was zählt als mobile Webseite?

Eine Seite, die:

- auch auf dem Handy lesbar ist
- in normaler Größe lesbar ist und bei Bedarf vergrößert werden kann
- die Navigation leicht mit dem Finger bedient werden kann
- die Leistung akzeptabel ist

## Alter und moderner Ansatz

| Ansatz | Bedeutung |
|---|---|
| separate mobile Seite | z.B. `m.beispiel.at` |
| responsive Seite | dieselbe Seite passt sich an |

In der Praxis wird heute in der Regel die **responsive** Lösung empfohlen.

## Worauf muss man bei mobilen Seiten achten?

- kleiner Bildschirm
- Nutzung per Berührung
- wechselnde Netzwerkqualität
- kürzere Aufmerksamkeitsspanne
- schnelles Laden

## Typische gute Lösungen

- größere klickbare Flächen
- einfachere Navigation
- gut umbrechender Inhalt
- optimierte Bilder
- kürzere, auf den Punkt gebrachte Oberfläche

## Mobile Website und native App: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| mobile Webseite | läuft im Browser |
| native Mobilapp | auf dem Betriebssystem installierte Anwendung |

## Auf Mobilgeräten einen echten Ablauf prüfen

Ein Anmeldeformular wird nicht nur in einem schmalen Fenster geprüft. Auch mit
eingeblendeter Bildschirmtastatur müssen Feld, Fehlermeldung und Absenden
erreichbar bleiben. Wir durchlaufen die Aufgabe im Hoch- und Querformat sowie
mit vergrößertem Text. Manuelles Zoomen wird im Viewport nicht deaktiviert.

Die Zielgrößenanforderung von WCAG 2.2 AA geht grundsätzlich von `24 × 24`
CSS-Pixeln aus, mit definierten Abstands- und weiteren Ausnahmen. Für angenehme
Touch-Bedienung wählen wir häufig größere Ziele, etwa `44 × 44` CSS-Pixel.
Das ist eine Gestaltungsentscheidung und keine auf allen Geräten gleiche
physische Größe. Für Hilfen per Hover braucht es auch einen Touch- und Tastaturweg.

Displayausschnitte und den unteren Systembereich können wir in CSS berücksichtigen:

```css
.site-footer {
  padding-block-end: max(1rem, env(safe-area-inset-bottom, 0px));
}
```

Dieser Browser-CSS-Ausschnitt lässt mindestens `1rem` Platz und berücksichtigt
einen gegebenenfalls größeren unteren sicheren Bereich. Sein tatsächlicher
Wert hängt von Gerät und Viewport-Einstellung ab. Schwebende Buttons werden
zusätzlich geprüft, damit sie keinen Inhalt verdecken.

Bei langsamem Netz helfen passend kleine Bilder, reservierter Bildplatz und
verständliche Ladezustände. Installierbarkeit allein macht eine Anwendung
nicht nativ: Auch eine PWA kann installiert werden und basiert weiterhin auf
Webtechnologien.

## Prüfungstaugliche Formulierung

> Eine mobile Webseite ist eine Weboberfläche,
> die speziell für die gute Nutzung
> auf Telefonen und anderen kleinen Bildschirmen gestaltet wird.
> Wichtige Aspekte sind gute Lesbarkeit, berührungsfreundliche Bedienung,
> schnelles Laden und ein an den kleinen Bildschirm angepasstes Layout.
> In der modernen Praxis wird dies meist mit responsive Webdesign umgesetzt.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel einer mobilen Webseite?
2. Warum ist schnelles Laden wichtig?
3. Warum braucht man größere Berührungsflächen?
4. Was ist der Unterschied zwischen mobiler Webseite und nativer App?
5. Was ist die heutige typische Umsetzungsart?

## Kurzantworten zur Selbstkontrolle

1. Gute Nutzbarkeit im mobilen Browser
2. Weil es im Mobilnetz und auf dem Handy besonders zählt
3. Weil man mit dem Finger bedient
4. Die mobile Website läuft in einer Webumgebung; die native App baut auf dem Anwendungsmodell der Plattform auf. Auch eine Web-PWA kann installiert sein.
5. Responsive Webdesign

## Quellen

Geprüft: `2026-10-14`.

- [W3C: Target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): 24 CSS-Pixel und Ausnahmen der Anforderung.
- [MDN: env()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env): Umgebungsvariablen für sichere Bildschirmbereiche.


1. MDN - Responsive design
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
   Verwendung: Grundlagen der mobilfreundlichen Webgestaltung.

2. web.dev - Learn Design
   https://web.dev/learn/design/
   Verwendung: moderner, von Google gepflegter Leitfaden für mobiles und Multi-Device-Webdesign.

3. MDN - Responsive Web Design (RWD)
   https://developer.mozilla.org/en-US/docs/Glossary/Responsive_web_design
   Verwendung: kurze, präzise Definition des responsiven Ansatzes.

Abgerufen: `2026-04-08`
