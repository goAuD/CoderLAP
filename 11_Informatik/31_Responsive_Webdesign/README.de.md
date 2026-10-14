# Responsive Webdesign

## Schneller visueller Überblick

| Gerät | Was passiert? |
|---|---|
| Mobil | einspaltiges, einfacheres Layout |
| Tablet | mittlerer Umbruch |
| Desktop | mehrere Spalten, mehr Platz |

## Was ist das Wesentliche von Responsive Webdesign?

Wir erstellen keine separate Seite für jedes Gerät, sondern gestalten dieselbe Seite so, dass sie:

- sich umordnet
- sich anpasst
- lesbar bleibt
- bedienbar bleibt

## Welche Techniken gehören dazu?

- flexibles Layout
- relative Maße
- Media Queries (`media queries`)
- flexible Bilder und Medienelemente
- Breakpoints

## Warum ist das wichtig?

- die Seite wird von vielen verschiedenen Geräten aufgerufen
- es bietet eine bessere Benutzererfahrung
- keine separate mobile Seite nötig
- besser wartbar

## Responsive und Mobile First: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Responsive Webdesign | die Oberfläche passt sich an den Bildschirm an |
| Mobile First | Designstrategie, die vom Mobilgerät ausgeht |

Also:

- Responsive ist ein technisch-gestalterisches Ergebnis
- Mobile First ist eine Designrichtung

## Worauf muss man achten?

- Es reicht nicht, die Seite einfach zusammenzuschrumpfen.
- Die inhaltliche Priorität kann sich auf kleinerem Bildschirm ändern.
- Menüs, Tabellen und Bilder erfordern besondere Aufmerksamkeit.
- Die Leistung ist auch auf Mobilgeräten kritisch.

## Durchgerechnetes Beispiel: Themenkarten in einem flexiblen Raster

**Aufgabe und Umgebung:** Speichere das vollständige Beispiel als UTF-8-HTML,
öffne es in einem modernen Browser und ändere die Fensterbreite. Alle drei
Themen bleiben bei jeder Breite erreichbar.

```html
<!doctype html>
<html lang="de">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Themenübersicht</title>
<style>
  .topics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
    gap: 1rem;
  }
  .topics > article { min-width: 0; border: 1px solid; padding: 1rem; }
  .topics pre { overflow-x: auto; }
  * { box-sizing: border-box; }
</style>
<main>
  <h1>Themen</h1>
  <div class="topics">
    <article><h2>Schleifen</h2><p>Wiederholungen verstehen.</p></article>
    <article><h2>Funktionen</h2><p>Aufgaben aufteilen.</p></article>
    <article><h2>Datenbanken</h2><p>Daten verknüpfen.</p></article>
  </div>
</main>
</html>
```

`auto-fit` erzeugt so viele Spalten, wie hineinpassen. Die gewünschte
Mindestbreite ist `16rem`; `min(100%, 16rem)` verlangt bei sehr wenig Platz aber
keine breitere Spalte als den Container. `1fr` verteilt den übrigen Platz
gleichmäßig. Bei `16px` Wurzelschriftgröße und gemessener **innerer Breite**
von `.topics` gilt:

| Verfügbare Breite | Ergebnis | Begründung |
|---|---|---|
| 360px | eine Spalte | zwei Karten mit 256px und eine Lücke mit 16px passen nicht |
| 600px | zwei Spalten | zwei Karten und eine Lücke passen, drei Karten noch nicht |
| 1000px | drei Spalten | drei Karten und zwei Lücken passen |

Dieses Raster ist auch ohne eigene Media Query responsiv. Breakpoints wählen
wir nach dem Inhalt, nicht nach einem bestimmten Telefonnamen. Langer Code
scrollt lokal; `min-width: 0` lässt das Rasterelement schrumpfen. Bei Bildern
erhält `max-width: 100%; height: auto` das Seitenverhältnis, verkleinert aber
nicht die heruntergeladene Datei. Prüfe lange deutsche Überschriften,
vergrößerte Schrift und dass die ganze Seite nicht unnötig horizontal scrollt.

## Prüfungstaugliche Formulierung

> Responsive Webdesign ist ein Design- und Entwicklungsansatz,
> dessen Ziel es ist,
> dass dieselbe Webseite auf verschiedenen Bildschirmgrößen gut nutzbar ist.
> Dafür verwenden wir flexibles Layout, Media Queries, Breakpoints und adaptive Inhaltsdarstellung.
> Der Vorteil ist, dass keine separaten Mobil- und Desktop-Seiten gepflegt werden müssen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Responsive Webdesign?
2. Warum ist es vorteilhaft?
3. Welche Techniken unterstützen es?
4. Was ist der Unterschied zu Mobile First?
5. Warum muss man sich auch mit der Inhaltspriorität beschäftigen?

## Kurzantworten zur Selbstkontrolle

1. Die Seite passt sich an mehrere Bildschirme an
2. Bessere Nutzbarkeit und weniger separate Seiten
3. Media Query, Breakpoint, flexibles Layout
4. Responsive ist das Ergebnis, Mobile First die Strategie
5. Weil auf kleinem Bildschirm Platz und Aufmerksamkeit anders sind

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Responsive web design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design): Flexible Layouts, inhaltsabhängige Breakpoints und Bilder.
- [web.dev: Macro layouts](https://web.dev/learn/design/macro-layouts): Automatisch anpassbare Grid-Layouts.


1. MDN - Responsive design
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
   Verwendung: Entwicklerzusammenfassung der technischen Grundlagen von Responsive Webdesign.

2. MDN - Responsive Web Design (RWD)
   https://developer.mozilla.org/en-US/docs/Glossary/Responsive_web_design
   Verwendung: kurze, präzise begriffliche Definition.

3. web.dev - Learn Design
   https://web.dev/learn/design/
   Verwendung: moderne Multi-Device-Webdesign-Richtlinien.

Abgerufen: `2026-04-08`
