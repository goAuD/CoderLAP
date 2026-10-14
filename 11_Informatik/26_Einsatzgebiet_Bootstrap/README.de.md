# Einsatzgebiet Bootstrap

## Schneller visueller Überblick

| Wofür gut? | Beispiel |
|---|---|
| Grid und Breakpoints | responsives Spaltensystem |
| fertige UI-Elemente | Button, Navbar, Modal |
| Utility-Klassen | Spacing, Display, Flex |
| schneller Einstieg | auch mit wenig eigenem CSS verwendbar |

## Was ist die Hauptrolle von Bootstrap?

Das Ziel von Bootstrap ist, dass man schnell:

- ein geordnetes Layout bauen kann
- einheitlich aussehende Komponenten verwenden kann
- die Seite responsiv gestalten kann

## Wann ist es nützlich?

- wenn schnell eine funktionierende Oberfläche gebraucht wird
- wenn Einheitlichkeit wichtig ist
- wenn man bei kleinen oder mittleren Projekten nicht alles von Grund auf bauen will
- für Admin- oder interne Systeme
- für MVP- oder Prototyp-Erstellung

## Typische Elemente

- Grid-System
- Breakpoints
- Formularelemente
- Navbar
- Modal
- Utility-Klassen

## Vorteile

- schnelle Entwicklung
- viele fertige Elemente
- gute Dokumentation
- responsive Grundlagen
- weit verbreitet und bekannt

## Nachteile

- leicht entsteht ein "Bootstrap-Look"
- zu viele fertige Klassen können unübersichtlich werden
- bei individuellem Design sind viele Überschreibungen nötig

## Bootstrap und CSS: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| CSS | allgemeine Stilsprache |
| Bootstrap | auf CSS und Komponenten aufbauendes Framework |

## Eine und zwei Spalten aus demselben HTML

**Umgebung:** HTML-Seite mit geladenem Bootstrap-5.3-CSS. Für diesen Ausschnitt
wird kein JavaScript benötigt. CSS kann lokal ausgeliefert werden; ein CDN
ist keine Voraussetzung.

```html
<div class="container">
  <div class="row g-3">
    <section class="col-12 col-md-6">
      <h2 class="h4">Programmieren</h2>
      <p>Schleifen und Funktionen üben.</p>
    </section>
    <section class="col-12 col-md-6">
      <h2 class="h4">Netzwerke</h2>
      <p>Adressen und Protokolle verstehen.</p>
    </section>
  </div>
</div>
```

`container` bildet den Inhaltsrahmen, `row` eine Rasterzeile und `g-3` die Abstände.
`col-12` belegt die gesamte Breite des zwölfspaltigen Rasters. `col-md-6` belegt
ab dem Bootstrap-5.3-Breakpoint `md`, also `768px` Viewportbreite, sechs Spalten.
Die Themen stehen deshalb schmal untereinander und breiter in zwei gleich großen
Spalten. Die Klasse `h4` verändert nur die Darstellung; das Element bleibt eine
Überschrift der Ebene `h2`.

Ein einfaches Raster funktioniert durch CSS. Ein Modal oder eine aufklappende
Interaktion benötigt auch die passende JavaScript-Komponente. Bootstrap 5 hat
keine jQuery-Abhängigkeit. Beschriftung, Kontrast und Tastaturbedienung bleiben
beim Einbau der Komponenten Entwicklungsaufgaben. Ein eigenes Erscheinungsbild
wird über gemeinsame Variablen und dokumentierte Anpassungspunkte gepflegt,
statt jeden Button separat zu überschreiben.

## Prüfungstaugliche Formulierung

> Bootstrap ist ein verbreitetes Frontend-Framework,
> das ein responsives Layout, fertige UI-Komponenten
> und Utility-Klassen für eine schnellere Oberflächenentwicklung bereitstellt.
> Besonders nützlich ist es bei Prototypen, Admin-Oberflächen und Projekten,
> bei denen ein schnelles, einheitliches Erscheinungsbild wichtig ist.
> Sein Vorteil ist die Geschwindigkeit und die fertige Komponentensammlung,
> sein Nachteil kann das schablonenartige Aussehen
> und die schwierigere Umsetzung eines individuellen Designs sein.

## Schnelle Selbstkontrolle

1. Wofür verwenden wir Bootstrap?
2. Was ist einer der größten Vorteile?
3. Was kann ein Nachteil sein?
4. Wofür dient das Grid-System?
5. Für welche Projekte ist es eine gute Wahl?

## Kurzantworten zur Selbstkontrolle

1. Für schnellen, einheitlichen Frontend-Aufbau
2. Es bietet fertige Komponenten und eine responsive Grundlage
3. Es kann ein schablonenhaftes Aussehen ergeben
4. Für responsives Layout
5. Für Prototypen, Admin-Oberflächen, schnelle Entwicklung

## Quellen

- [Bootstrap: Migration to v5](https://getbootstrap.com/docs/5.3/migration/#javascript): Entfernung der jQuery-Abhängigkeit in Version 5. Geprüft: `2026-10-14`.

Geprüft: `2026-10-14`.

- [Bootstrap 5.3: Grid](https://getbootstrap.com/docs/5.3/layout/grid/): 12 Spalten, row und md-Breakpoint.
- [Bootstrap 5.3: Accessibility](https://getbootstrap.com/docs/5.3/getting-started/accessibility/): Voraussetzungen barrierefreier Komponentennutzung.


1. Bootstrap 5.3 - Introduction
   https://getbootstrap.com/docs/5.3/getting-started/introduction/
   Verwendung: Zweck, Aufbau und Hauptteile von Bootstrap.

2. Bootstrap 5.3 - Breakpoints
   https://getbootstrap.com/docs/5.3/layout/breakpoints/
   Verwendung: responsive Nutzung und Breakpoint-Logik.

3. Bootstrap 5.3 - Grid system
   https://getbootstrap.com/docs/5.3/layout/grid/
   Verwendung: praktische Rolle des Layouts und des Rastersystems.

Abgerufen: `2026-04-08`
