# Meta Elemente und Metadaten

## Schneller visueller Überblick

| Begriff | Bedeutung | Beispiel |
|---|---|---|
| Daten | der Inhalt selbst | ein Artikeltext |
| Metadaten | Daten über Daten | Titel, Beschreibung, Sprache, Kodierung |
| Meta-Element | HTML-Element zur Angabe von Metadaten | `<meta name="description" ...>` |

## Was sind Metadaten?

**Metadaten** sind ergänzende Informationen, die ein Dokument oder eine Ressource beschreiben.

Bei einer Webseite kann das zum Beispiel sein:

- der Titel der Seite
- eine kurze Beschreibung
- die Zeichenkodierung
- der Autor
- die Einstellung für die mobile Darstellung
- Signale für Suchmaschinen-Robots

Der Zweck von Metadaten ist nicht, dass der Benutzer sie als langen Text liest, sondern dass das System die Seite leichter interpretieren kann.

## Welche Rolle spielt das `<meta>`-Element?

Das `<meta>`-Element befindet sich im HTML-`head` und gibt Metadaten an, die andere Elemente nicht genauer ausdrücken.

Häufige Formen:

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="Kurze Beschreibung der Seite" />
<meta name="robots" content="index,follow" />
```

Wichtig:

- `charset` gibt an, welche Zeichenkodierung das Dokument verwendet
- `viewport` ist wichtig für die mobile Darstellung
- `description` ist oft nützlich für die Kurzbeschreibung in Suchergebnissen
- `robots` signalisiert, wie sich der Suchrobot verhalten soll

## Wofür sind sie in der Praxis nützlich?

### Für den Browser

- korrekte Zeichendarstellung
- gute mobile Ansicht
- korrekte technische Verarbeitung

### Für Suchmaschinen

- kurze Zusammenfassung der Seite
- Indexierungssignale
- bessere Interpretierbarkeit

### Für externe Systeme

- Vorschauen
- Teilen-Informationen
- strukturiertere Verarbeitung

## Meta-Element und Metadaten: nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Metadaten | allgemeine Informationen über das Dokument |
| `<meta>`-Element | ein konkretes HTML-Element, mit dem Metadaten angegeben werden |
| `title` | kein `<meta>`, sondern ein eigenes HTML-Element, trotzdem meta-artige Information |

## Worauf muss man achten?

- Die Meta-Beschreibung ersetzt keinen guten Inhalt.
- Die `description` allein bewirkt kein gutes Ranking.
- Ein falsches `charset` kann Zeichenfehler verursachen.
- Ein falsches `viewport` verschlechtert die Nutzbarkeit auf Mobilgeräten.
- Eine fehlerhafte `robots`-Einstellung kann dazu führen, dass die Seite nicht im Index erscheint.

## Prüfungstaugliche Formulierung

> Metadaten sind beschreibende Daten über das Dokument. In HTML werden sie häufig durch `<meta>`-Elemente im `head`-Teil angegeben.  
> Diese helfen dem Browser, Suchmaschinen und anderen Systemen bei der korrekten Verarbeitung der Seite, zum Beispiel bei der Zeichenkodierung, der mobilen Ansicht oder der Kurzbeschreibung der Seite.

## Häufige Prüfungsfehler

- Metadaten mit dem sichtbaren Inhalt verwechseln.
- Behaupten, dass alle Metadaten vom Benutzer gesehen werden.
- Die Rollen von `title` und `description` vermischen.
- Glauben, dass Meta-Tags allein für gutes SEO ausreichen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Metadaten?
2. Wo befindet sich das `<meta>`-Element normalerweise?
3. Wofür ist `charset` da?
4. Wofür ist `viewport` gut?
5. Warum genügen Meta-Tags allein nicht für SEO?

## Kurzantworten zur Selbstkontrolle

1. Hintergrundinformationen, die das Dokument beschreiben
2. Im HTML-`head`-Teil
3. Zur Angabe der Zeichenkodierung
4. Zur Steuerung der mobilen Darstellung
5. Weil auch Inhalt und technische Qualität zählen

## Quellen

1. MDN - `<meta>`: The metadata element  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta  
   Verwendung: Typen, Attribute und praktische Rolle des `<meta>`-Elements.

2. WHATWG HTML Standard - The `meta` element  
   https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element  
   Verwendung: offizieller HTML-Standard-Hintergrund zur Funktionsweise des Meta-Elements.

3. MDN - `<head>`: The Document Metadata element  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head  
   Verwendung: Kontext dazu, wo und in welcher Rolle Meta-Elemente erscheinen.

Abgerufen: `2026-04-08`
