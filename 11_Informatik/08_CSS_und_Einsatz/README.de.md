# CSS und Einsatz

## Schneller visueller Überblick

| Technologie | Hauptrolle |
|---|---|
| HTML | Inhalt und Struktur |
| CSS | Aussehen und Layout |
| JavaScript | Verhalten und Interaktion |

## Was ist CSS?

CSS ist eine Stylesheet-Sprache, mit der wir festlegen, wie HTML-Elemente dargestellt werden.

Beispiel:

```css
body {
  font-family: Arial, sans-serif;
  color: #222;
}

h1 {
  color: #0a66c2;
}
```

Dies erzeugt keinen neuen Inhalt, sondern formatiert den bestehenden Inhalt.

## Wie funktioniert es?

Eine CSS-Regel besteht typischerweise aus drei Teilen:

- Selektor
- Eigenschaft
- Wert

Beispiel:

```css
p {
  color: red;
}
```

Hier:

- `p` = Selektor
- `color` = Eigenschaft
- `red` = Wert

## Wofür wird es verwendet?

### Formatierung

- Farben
- Schriftgröße
- Hintergrund
- Rahmen

### Layout

- `flexbox`
- `grid`
- Positionierung
- Margin und Padding

### Responsive Gestaltung

- Media Queries
- Anpassung von Mobil- und Desktop-Ansichten

### Einheitliches Erscheinungsbild

- gleiches Design auf mehreren Seiten
- zentrale Stilverwaltung

## Warum ist es vorteilhaft?

- trennt Inhalt von Darstellung
- leichter wartbar
- wiederverwendbar
- ermöglicht ein einheitliches Erscheinungsbild
- responsive Webseiten können damit erstellt werden

## CSS und HTML: nicht verwechseln

| Begriff | Aufgabe |
|---|---|
| HTML | beschreibt, was auf der Seite ist |
| CSS | beschreibt, wie es aussehen soll |
| JavaScript | beschreibt, wie es sich verhalten soll |

## Worauf muss man achten?

- Zu viele Inline-Styles führen zu schlechter Wartbarkeit.
- Schlecht aufgebaute Selektoren ergeben schwer handhabbares CSS.
- Es reicht nicht, nur "schön" zu sein: es muss auch benutzbar und übersichtlich sein.
- CSS ersetzt kein semantisches HTML.

## Prüfungstaugliche Formulierung

> CSS ist eine Stylesheet-Sprache zur Beschreibung des Erscheinungsbilds von Webseiten.  
> Mit ihr können HTML-Elemente formatiert,
> das Layout gesteuert
> und responsive, einheitliche Benutzeroberflächen gestaltet werden.  
> HTML liefert die Struktur, CSS das Erscheinungsbild und JavaScript die interaktive Funktionalität.

## Häufige Prüfungsfehler

- CSS als Programmiersprache bezeichnen.
- Die Rollen von HTML und CSS vertauschen.
- Responsive Darstellung nur an JavaScript binden.
- Nicht erwähnen, dass CSS auch für das Layout verantwortlich ist.

## Schnelle Selbstkontrolle

1. Was ist die Hauptaufgabe von CSS?
2. Woraus besteht eine CSS-Regel?
3. Wofür ist `flexbox` oder `grid` gut?
4. Warum ist die Trennung von Inhalt und Darstellung nützlich?
5. Worin unterscheidet sich CSS von JavaScript?

## Kurzantworten zur Selbstkontrolle

1. Steuerung des Erscheinungsbilds
2. Selektor, Eigenschaft, Wert
3. Für das Layout
4. Wegen leichterer Wartung und Einheitlichkeit
5. CSS formatiert, JavaScript gibt Verhalten

## Quellen

1. MDN - CSS: Cascading Style Sheets  
   https://developer.mozilla.org/en-US/docs/Web/CSS  
   Verwendung: Begriff, Hauptelemente und moderne Verwendung von CSS.

2. W3C - CSS Snapshot  
   https://www.w3.org/TR/CSS/  
   Verwendung: Standardüberblick über CSS-Module und ihre Rolle im Web.

3. MDN - Learn CSS  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics  
   Verwendung: praktischer Hintergrund zur grundlegenden Funktionsweise und Nutzung von CSS.

Abgerufen: `2026-04-08`
