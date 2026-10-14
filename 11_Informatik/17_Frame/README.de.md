# Frame

## Schneller visueller Überblick

| Begriff | Status | Wofür? |
|---|---|---|
| `frame` | veraltet | alte Aufteilung in mehrere Rahmen |
| `frameset` | veraltet | Dokument mit Rahmen |
| `iframe` | heute noch in Verwendung | Einbettung einer anderen Seite innerhalb der Seite |

## Was war das alte Frame-System?

Bei der klassischen `frame`-basierten HTML-Lösung
wurde eine Seite in mehrere separate Teile aufgeteilt,
die jeweils eigene Dokumente luden.

Das schien früher für Navigation und Seitenaufteilung nützlich, verursachte aber viele Probleme:

- schlechte Benutzbarkeit
- umständliches Setzen von Lesezeichen
- schwächere Suchmaschinenfreundlichkeit
- Barrierefreiheitsprobleme
- kompliziertere Handhabung

Daher gilt dies im modernen Web nicht mehr als gute Praxis.

## Was ist ein `iframe`?

Das `iframe` (`inline frame`) ist ein HTML-Element, das ein anderes Dokument in die aktuelle Seite einbettet.

Typische Beispiele:

- Videoeinbettung
- Karteneinbettung
- externes Widget
- Dokumentansicht

Beispiel:

```html
<iframe src="https://example.com" title="Beispiel"></iframe>
```

## Warum muss man es vorsichtig verwenden?

Weil das `iframe` nützlich, aber keine kostenlose Lösung ist.

Risiken und Aspekte:

- Sicherheit
- Leistung
- Handhabung unterschiedlicher Inhaltsquellen
- Barrierefreiheit
- responsive Darstellung

Daher ist häufig die Verwendung von `sandbox` und anderen einschränkenden Attributen wichtig.

## Wann ist es eine gute Wahl?

- wenn ein externer Dienst eingebettet werden muss
- wenn isolierter Inhalt angezeigt werden soll
- wenn zu Integrationszwecken eine fertige Komponente kommt

## Wann ist es keine gute Wahl?

- wenn die gesamte Seitenstruktur darauf aufgebaut würde
- wenn es mit einfachem HTML/CSS lösbar wäre
- wenn die Leistung oder Benutzbarkeit durch den eingebetteten Inhalt leidet

## Frame und iframe: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| `frame` | alte, veraltete Rahmenlösung |
| `frameset` | das alte Rahmenaufteilungselement |
| `iframe` | modernes Einbettungselement |

## Einbetten mit minimalen Berechtigungen

Dieser HTML-Ausschnitt lässt sich lokal öffnen und lädt keinen externen Dienst:

```html
<iframe
  title="Isolierte Textvorschau"
  sandbox
  srcdoc="<p>Nur lesen</p>">
</iframe>
```

Im Rahmen erscheint `Nur lesen`. `title` beschreibt den Zweck für assistive
Technologien. `srcdoc` enthält hier festen Beispieltext. Für eingefügtes
Benutzer-HTML ist zusätzlich eine sichere Inhaltsbehandlung erforderlich.
Ein leeres `sandbox` aktiviert Einschränkungen, etwa das Verbot von Skripten
und Formularübermittlung. Nur tatsächlich benötigte Fähigkeiten werden erlaubt.

Die Kombination von `allow-scripts` und `allow-same-origin` kann bei Inhalten
derselben Herkunft die Isolation unterlaufen. Der Server der eingebetteten
Seite kann mit dem Header `Content-Security-Policy: frame-ancestors` festlegen,
wer sie einbetten darf. Ein HTML-Attribut auf der einbettenden Seite kann diese
Vorgabe nicht aufheben.

Das frühere vollständige `frameset`-Layout wird durch CSS Grid/Flexbox und normale
Navigation ersetzt. `iframe` dient zum Einbetten eines separaten Dokuments und
ist kein allgemeiner Nachfolger der alten Seitenaufteilung. Bei externen
Einbettungen prüfen wir außerdem Datenübertragung und Ladekosten.

## Prüfungstaugliche Formulierung

> Der Frame-Begriff bedeutete im alten HTML Seiten,
> die in mehrere Rahmen aufgeteilt waren,
> aber diese Lösung gilt heute als veraltet.  
> Zum Einbetten eines anderen Dokuments kann im modernen Web das `iframe` verwendet werden,
> mit dem ein anderes Dokument in die aktuelle Seite eingebettet werden kann.  
> Das `iframe` kann zum Beispiel für Videos oder externe Dienste nützlich sein,
> muss aber hinsichtlich Sicherheit
> und Benutzbarkeit umsichtig eingesetzt werden.

## Schnelle Selbstkontrolle

1. Was ist der Unterschied zwischen `frame` und `iframe`?
2. Warum gilt das alte Frame-System als veraltet?
3. Wofür kann `iframe` verwendet werden?
4. Warum muss man auf Sicherheit achten?
5. Nenne zwei typische Einbettungsbeispiele.

## Kurzantworten zur Selbstkontrolle

1. `frame` ist alt und veraltet, `iframe` ist ein modernes Einbettungselement
2. Weil es schlechtere Benutzbarkeit und technische Probleme verursacht
3. Zur Einbettung einer anderen Seite oder externer Inhalte
4. Weil externer Inhalt in die Seite kommt
5. Video und Karte

## Quellen

Geprüft: `2026-10-14`.

- [MDN: iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe): sandbox, srcdoc, Beschriftung und Herkunft.
- [MDN: frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/frame-ancestors): der Inhaltsserver kann Einbettung begrenzen.


1. MDN - `<iframe>`: The Inline Frame element  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe  
   Verwendung: moderne, offizielle Entwicklerreferenz für `iframe`.

2. WHATWG HTML Standard - The `iframe` element  
   https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-iframe-element  
   Verwendung: Standardhintergrund zur Funktionsweise von `iframe`.

3. MDN - `<frameset>`  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset  
   Verwendung: offizielle Darstellung des veralteten Status des alten Frame-Systems.

Abgerufen: `2026-04-08`
