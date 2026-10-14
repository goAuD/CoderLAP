# HTML5 Grundgeruest

## Schneller visueller Überblick

```html
<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Lernwerkstatt</title>
  </head>
  <body>
    Willkommen!
  </body>
</html>
```

## Warum braucht man ein Grundgerüst?

Weil das Dokument dadurch:

- standardkonform wird
- für den Browser besser interpretierbar ist
- leichter wartbar wird

## Was macht jeder Teil?

### `<!doctype html>`

Teilt dem Browser mit, dass es sich um ein modernes HTML-Dokument handelt, und hilft, den Quirks-Mode zu vermeiden.

### `<html lang="...">`

Das ist das Wurzelelement.

Das `lang`-Attribut hilft:

- dem Browser
- Suchmaschinen
- Barrierefreiheitstools

### `<head>`

Hier kommen:

- Metadaten
- Titel
- Stylesheet-Verweise
- Scripts oder andere technische Informationen

### `<meta charset="utf-8">`

Gibt die Zeichenkodierung an.

### `<meta name="viewport" ...>`

Besonders auf Mobilgeräten wichtig, da es die richtige Skalierung und responsive Darstellung unterstützt.

### `<title>`

Der Seitentitel, der erscheint:

- im Browser-Tab
- kann auch bei Suchergebnissen wichtig sein

### `<body>`

Hier kommt der sichtbare Inhalt.

## Warum "HTML5"?

In der heutigen Praxis ist dies die moderne Grundform eines HTML-Dokuments.

Wichtig:

- heute sagt man oft einfach nur "HTML"
- aber dieses Grundgerüst ist die Standardstruktur der HTML5-Ära

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| `head` | technische und Meta-Informationen |
| `body` | sichtbarer Inhalt |
| `title` | Seitentitel, nicht identisch mit der Hauptüberschrift (`h1`) |
| `doctype` | Dokumenttyp-Deklaration, nicht der Inhalt selbst |

## Vom Gerüst zur aufrufbaren Seite

Das obige Gerüst verwendet in beiden Sprachfassungen deutsche Beispielinhalte.
Daher passt `lang="de"`. Bei ungarischem Inhalt wird auch die Sprachangabe auf
`hu` geändert. Dies ist etwa für die Aussprache eines Screenreaders wichtig.

Ersetzen wir den Inhalt von `body` durch folgenden HTML-Ausschnitt und speichern
das vollständige Dokument als UTF-8-Datei `index.html`. Es lässt sich direkt im
Browser öffnen:

```html
<main>
  <h1>Lernwerkstatt</h1>
  <section aria-labelledby="loops-title">
    <h2 id="loops-title">Schleifen</h2>
    <p>Eine Schleife wiederholt Anweisungen.</p>
  </section>
</main>
```

Der Browsertab heißt `Lernwerkstatt`. Im Dokument erscheinen die Hauptüberschrift
`Lernwerkstatt`, darunter der Abschnitt `Schleifen` und ein Satz. Die beiden
Titel sind unterschiedliche Elemente und können unabhängig geändert werden.
`main` kennzeichnet den Hauptinhalt. Überschriften beschreiben die Gliederung
und nicht nur eine Schriftgröße.

Die Viewport-Einstellung schafft die Grundlage für mobile Größenverhältnisse;
das flexible Layout liefert anschließend CSS. Manuelles Zoomen bleibt möglich.
„HTML5“ ist die Bezeichnung im Prüfungskatalog. Die laufend gepflegte
Spezifikation heißt HTML Living Standard.

## Prüfungstaugliche Formulierung

> Das HTML5-Grundgerüst ist eine standardkonforme Dokumentstruktur,
> die aus `doctype`, `html`, `head` und `body` besteht.  
> Der `head`-Teil enthält Metadaten wie die Zeichenkodierung,
> die Viewport-Einstellung und den Titel,
> während der `body` den für den Benutzer sichtbaren Inhalt enthält.  
> Das korrekte Grundgerüst unterstützt standardkonformes Verhalten, mobile Darstellung und Wartbarkeit.

## Schnelle Selbstkontrolle

1. Was ist die Aufgabe des `doctype`?
2. Was befindet sich im `head`-Teil?
3. Was befindet sich im `body`-Teil?
4. Wofür ist `meta charset` gut?
5. Wofür ist das `viewport`-Meta gut?

## Kurzantworten zur Selbstkontrolle

1. Kennzeichnet das HTML als modernes Dokument
2. Metadaten und technische Informationen
3. Der sichtbare Inhalt
4. Zur Angabe der Zeichenkodierung
5. Zur Unterstützung der mobilen und responsiven Darstellung

## Quellen

Geprüft: `2026-10-14`.

- [WHATWG: HTML Standard](https://html.spec.whatwg.org/): Dokumentstruktur und aktueller HTML-Standard.


1. MDN - Doctype  
   https://developer.mozilla.org/en-US/docs/Glossary/Doctype  
   Verwendung: offizielle Quelle zur Rolle von `<!doctype html>`.

2. MDN - Understanding quirks and standards modes  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode  
   Verwendung: erklärt, warum der `doctype` nötig ist.

3. MDN - HTML basics  
   https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics  
   Verwendung: offizielles HTML5-Grundgerüst-Beispiel mit `head`, `body`, `charset`, `viewport`-Elementen.

4. WHATWG - HTML Standard  
   https://html.spec.whatwg.org/  
   Verwendung: primäre Standardquelle für die Elemente und die Dokumentstruktur.

Abgerufen: `2026-04-08`
