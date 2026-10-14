# HTML und XML

## Schneller visueller Überblick

| Sprache | Wofür? | Beispiel |
|---|---|---|
| HTML | Struktur und Inhalt von Webseiten | Überschrift, Absatz, Link |
| XML | strukturierte Speicherung / Austausch von Daten | Konfiguration, Datenbeschreibung, Nachricht |

## Was ist HTML?

Die `HyperText Markup Language` ist die grundlegende Auszeichnungssprache des Webs.

Ihre Aufgabe:

- festzulegen, was die Überschrift ist
- was der Absatz ist
- was die Liste ist
- was der Link ist
- was die Tabelle ist

Also:

- sie gibt dem Webinhalt Struktur und Bedeutung

## Was ist XML?

Die `eXtensible Markup Language` ist eine allgemeine Auszeichnungssprache, die:

- zur Beschreibung von Daten verwendet wird
- in der auch eigene Tags definiert werden können

Beispiel für XML-artige Logik:

- Bestelldaten oder eine Konfiguration können strukturiert beschrieben werden

## Was ist der Hauptunterschied?

### HTML in der Praxis

- verwendet vordefinierte Elemente
- wird von Browsern zur Darstellung interpretiert

### XML in der Praxis

- verwendet eine freier gestaltbare Struktur
- dient hauptsächlich nicht der Darstellung, sondern der Datenbeschreibung

## Warum ist das wichtig?

Weil es eine häufige Prüfungsfrage ist:

- welche Sprache wofür dient
- wann welche verwendet wird

## Wo begegnen wir ihnen heute?

### HTML

- auf jeder klassischen Webseite

### XML

- in Konfigurationen
- in Dokumentformaten
- in bestimmten Webservices
- im standardisierten Datenaustausch

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| HTML | Inhalt und Dokumentstruktur im Web |
| XML | strukturierte Datenbeschreibung |
| CSS | Formatierung der HTML-Darstellung |
| JSON | ein anderes Datenaustauschformat, keine Auszeichnungssprache |

## Wohlgeformtes Dokument und gültige Daten

Dies ist ein vollständiges XML-Dokument mit UTF-8-Kodierung:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<course id="15">
  <title>Code &amp; Practice</title>
  <lessons>20</lessons>
</course>
```

Das einzige Wurzelelement ist `course`. Start- und Endnamen stimmen auch in
der Großschreibung überein, die Elemente sind korrekt verschachtelt und der
Attributwert steht in Anführungszeichen. Der verarbeitete Titel lautet
`Code & Practice`, denn `&amp;` steht für ein `&`. Der Text von `lessons` ist `20`;
dadurch wird er noch nicht automatisch zu einer geprüften ganzen Zahl.

**Wohlgeformtheit** bedeutet, dass die XML-Strukturregeln erfüllt sind. Ein Schema
kann zusätzlich verlangen, dass `lessons` eine nichtnegative ganze Zahl und
`title` verpflichtend ist. Ein Dokument kann wohlgeformt sein und trotzdem das
gewählte Schema verletzen. Geschäftsregeln, etwa die Existenz der Kurs-ID,
können weitere Prüfungen erfordern.

Bei HTML nutzt der Browser die festgelegte Bedeutung von `h1`, `p` oder `button`.
XML bietet eine allgemeine Syntax. Die Bedeutung der Elementnamen legt die
Anwendung oder ein XML-basiertes Format fest. SVG ist beispielsweise XML-basiert
und beschreibt Grafiken. XML ist deshalb nicht auf den Datenaustausch zwischen
Datenbanken beschränkt.

## Prüfungstaugliche Formulierung

> HTML und XML sind beides Auszeichnungssprachen, die jedoch für unterschiedliche Zwecke eingesetzt werden.  
> HTML dient zur Beschreibung von Inhalt und Struktur von Webseiten,
> während XML zur Beschreibung
> und zum Austausch strukturierter Daten verwendet wird.  
> HTML arbeitet mit vordefinierten Elementen, XML ermöglicht eine flexiblere Datenstruktur.

## Schnelle Selbstkontrolle

1. Wofür wird HTML verwendet?
2. Wofür wird XML verwendet?
3. Was ist der wichtigste Unterschied?
4. Bei welcher Sprache steht die darstellbare Dokumentstruktur im Vordergrund?
5. Bei welcher Sprache steht die strukturierte Datenbeschreibung im Vordergrund?

## Kurzantworten zur Selbstkontrolle

1. Für Struktur und Inhalt von Webseiten
2. Für die Beschreibung strukturierter Daten
3. HTML fokussiert auf Dokumente, XML auf Daten
4. Bei HTML
5. Bei XML

## Quellen

Geprüft: `2026-10-14`.

- [W3C: XML 1.0](https://www.w3.org/TR/xml/): Wohlgeformtheit, Wurzelelement, Referenzen und Gültigkeit.


1. MDN - HTML basics  
   https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics  
   Verwendung: offizielle HTML-Grundquelle zum Verständnis von Dokumentstruktur und Webrolle.

2. MDN - XML  
   https://developer.mozilla.org/en-US/docs/Glossary/XML  
   Verwendung: offizielle, knappe und präzise XML-Begriffsklärung.

3. W3C - Extensible Markup Language (XML) 1.0  
   https://www.w3.org/TR/xml/  
   Verwendung: primäre Standardquelle für XML.

4. WHATWG - HTML Standard  
   https://html.spec.whatwg.org/  
   Verwendung: primärer lebender Standard für HTML.

Abgerufen: `2026-04-08`
