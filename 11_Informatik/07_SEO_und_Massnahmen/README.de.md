# SEO und Massnahmen

## Schneller visueller Überblick

| Bereich | Was wird verbessert? | Beispiel |
|---|---|---|
| Inhalt | Relevanz, Nützlichkeit | präzise Antwort auf die Nutzerfrage |
| Struktur | Verständlichkeit | guter Titel, Zwischenüberschriften, logischer Seitenaufbau |
| Technik | Verarbeitbarkeit | indexierbares HTML, schnelle Ladezeit |
| Mobil | Nutzbarkeit | responsive Darstellung |
| interne Verlinkung | Navigation | logische Verlinkung innerhalb der Seite |

## Was ist SEO?

Suchmaschinen lesen nicht "wie Menschen", sondern versuchen, die Seite anhand technischer und inhaltlicher Signale zu verstehen.

Das Ziel von SEO:

- der Suchmaschine beim Verständnis der Seite zu helfen
- die qualitative organische Sichtbarkeit zu erhöhen
- bei den richtigen Suchanfragen zu erscheinen

Wichtig:

- SEO ist keine bezahlte Werbung
- SEO garantiert keinen ersten Platz
- SEO ist keine einzelne Einstellung, sondern inhaltliche und technische Arbeit zusammen

## Typische SEO-Maßnahmen

### Inhaltliche Seite

- eindeutige Seitentitel
- qualitativ hochwertiger, nützlicher Inhalt
- logische Überschriften: `h1`, `h2`, `h3`
- natürliche Verwendung von Schlüsselwörtern
- einzigartige Seitenbeschreibungen

### Technische Seite

- korrekte HTML-Struktur
- mobilfreundliche Darstellung
- schnelle Ladezeit
- gut durchsuchbare Linkstruktur
- passende Indexierungseinstellungen

### Organisatorische Seite

- eine Seite mit einem klaren Ziel
- klare URLs
- Vermeidung von doppeltem Inhalt
- aktueller Inhalt

## Was gilt heute als gute Praxis?

Die Grundlage von modernem SEO:

- für Menschen geschriebener, nützlicher Inhalt
- technisch gut erstellte Seite
- Vertrauenswürdigkeit und Transparenz

Daher ist es wichtig:

- nicht nur Schlüsselwörter zu häufen
- keine Inhalte zu verstecken
- keine künstlichen, qualitativ schwachen Seiten massenhaft zu erstellen

## Was darf man nicht verwechseln?

| Begriff | Bedeutung |
|---|---|
| SEO | organische Suchmaschinenoptimierung |
| SEA | bezahlte Suchmaschinenwerbung |
| meta description | kurze Beschreibung, nicht das Ranking selbst |
| Schlüsselwort | Signal zum Thema, kein Zauberwort |

## Worauf muss man als Entwickler achten?

- Der Seiteninhalt sollte indexierbar sein und nicht nur aus Bildern bestehen.
- Das HTML sollte semantisch geordnet sein.
- Die Überschriftenhierarchie sollte logisch sein.
- Die mobile Darstellung und die Leistung sollten nicht schwach sein.
- Suchroboter sollten nicht versehentlich ausgesperrt werden.

## Die Auffindbarkeit einer Themenseite prüfen

Eine öffentliche Seite „JavaScript-Schleifen“ beantwortet zuerst die Frage der
Lesenden mit einem verständlichen Beispiel. Anschließend prüfen wir die Technik:

1. Die Seite ist unter einer funktionierenden URL mit erfolgreicher HTTP-Antwort
   erreichbar.
2. Titel und Hauptüberschrift benennen das Thema genau. Interne Links verwenden
   aussagekräftige Texte wie „Kopfgesteuerte Schleifen“.
3. Inhalt ist mobil und per Tastatur nutzbar. Bilder erhalten bei Bedarf
   Textalternativen.
4. Bei mehreren URLs mit gleichem Inhalt kann `rel="canonical"` die bevorzugte
   Fassung angeben. Dies ist ein Signal an die Suchmaschine, keine Zugriffsregel
   und keine in jedem Fall verbindliche Entscheidung.

Eine Sitemap unterstützt das Entdecken von URLs, garantiert aber weder
Indexierung noch bessere Platzierung. Eine tatsächlich fehlende Seite sollte
`404` liefern, statt nur „nicht gefunden“ mit einer erfolgreichen `200`-Antwort
anzuzeigen. Google verwendet das `keywords`-Metaelement nicht als Rankingsignal.

Bei einer bewusst zugangsgeschützten Lernoberfläche ist die Auffindbarkeit
privater Materialien dagegen nicht das Ziel. Zunächst entscheiden wir, welche
Seiten öffentlich sein sollen, und richten danach die Indexierung aus. SEO ist
kein Grund, eine benötigte Zugriffskontrolle abzuschalten.

## Prüfungstaugliche Formulierung

> Das Ziel von SEO ist,
> dass die Webseite für Suchmaschinen technisch gut interpretierbar
> und für die Benutzer nützlich und gut nutzbar ist.  
> Zu den wichtigen Maßnahmen gehören qualitativ hochwertiger Inhalt,
> korrekte HTML-Struktur, eindeutige Titel, schnelle Ladezeit,
> mobilfreundliche Gestaltung und logische interne Verlinkung.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel von SEO?
2. Nenne drei technische SEO-Maßnahmen.
3. Warum ist die mobilfreundliche Gestaltung wichtig?
4. Was ist der Unterschied zwischen SEO und SEA?
5. Warum genügt es nicht, nur Schlüsselwörter zu platzieren?

## Kurzantworten zur Selbstkontrolle

1. Bessere organische Sichtbarkeit in Suchmaschinen
2. Gutes HTML, schnelle Seite, Indexierbarkeit
3. Weil ein großer Teil der Suche und Nutzung mobil stattfindet
4. SEO ist organisch, SEA ist bezahlt
5. Weil auch die Inhaltsqualität und die technische Umsetzung zählen

## Quellen

Geprüft: `2026-10-14`.

- [Google: SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide): Inhalt und technische Grundlagen.
- [Google: Special tags](https://developers.google.com/search/docs/crawling-indexing/special-tags): unterstützte Metadaten und keywords.


1. Google Search Central - SEO Starter Guide  
   https://developers.google.com/search/docs/fundamentals/seo-starter-guide  
   Verwendung: offizielle, aktuelle Grundprinzipien guter Suchmaschinenoptimierung.

2. Google Search Central - Search Essentials  
   https://developers.google.com/search/docs/essentials  
   Verwendung: offizielle Zusammenfassung dessen, was Google von indexierbaren und nützlichen Seiten erwartet.

3. Google Search Central - Documentation  
   https://developers.google.com/search/docs  
   Verwendung: modernes, von Google gepflegtes Entwicklermaterial zu den technischen und inhaltlichen Grundlagen von SEO.

Abgerufen: `2026-04-08`
