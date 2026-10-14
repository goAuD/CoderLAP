# Metadaten

## Schneller visueller Überblick

| Daten | Metadaten |
|---|---|
| Foto | Datum, Auflösung, GPS-Daten |
| Dokument | Titel, Autor, Sprache |
| Webseite | Description, Charset, Robots |
| Datenbanktabelle | Spaltenname, Datentyp |

## Was ist die Rolle von Metadaten?

Metadaten helfen:

- Daten zu identifizieren
- zu systematisieren
- darin zu suchen
- zu verarbeiten
- automatisiert zu interpretieren

## Wo begegnen wir ihnen?

### Bei Dateien

- Erstellungsdatum
- Dateigröße
- Format

### Im Web

- Seitentitel
- Beschreibung
- Zeichenkodierung
- Robots-Informationen

### In Datenbanken

- Feldnamen
- Datentypen
- Schlüssel

## Metadaten und HTML-Meta-Element: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Metadaten | allgemeiner Begriff |
| `<meta>`-Element | eine konkrete HTML-Lösung zur Angabe von Metadaten |

Das HTML-`meta`-Element ist also nur ein spezielles Werkzeug für eine Art von Metadaten.

## Warum ist das wichtig?

- bessere Durchsuchbarkeit
- bessere automatisierte Verarbeitung
- bessere Systematisierung
- genauere Datenverarbeitung

## Worauf muss man achten?

- Metadaten können auch sensible Daten sein.
- Falsche Metadaten können irreführend sein.
- Fehlende Metadaten verschlechtern die Durchsuchbarkeit und Verarbeitbarkeit.

## Durchgearbeitetes Beispiel: Lerninhalt und seine Beschreibung

Der Lerntext erklärt eine Schleife. Das folgende illustrative JSON beschreibt
den zugehörigen Katalogeintrag, nicht das derzeitige Registry-Schema der Website:

```json
{
  "id": "LAP-15-17",
  "title": "Schleifen",
  "language": "de",
  "modified": "2026-10-14",
  "format": "text/markdown"
}
```

Die Suche erhält den Titel, die Sprachwahl die Sprache und die Änderungsliste
das Datum. Eine stabile ID kann erhalten bleiben, wenn sich der angezeigte
Titel ändert. Das ISO-formatierte Datum ist maschinell sortierbar, beschreibt
hier aber nur einen Tag. Für einen genauen Zeitpunkt würden wir auch Zeitzone
oder UTC-Offset festhalten.

| Art von Metadaten | Beispiel | Nutzen |
|---|---|---|
| beschreibend | Titel, Thema, Sprache | Auffinden und Identifizieren |
| technisch | Medientyp, Auflösung, Kodierung | Verarbeitung und Darstellung |
| administrativ | Lizenz, Berechtigung, Version | Nutzung und Verwaltung |
| strukturell | Reihenfolge und Beziehungen von Kapiteln | Zusammensetzen komplexer Inhalte |

HTTP `Content-Type: application/json` beschreibt die übertragene Repräsentation.
Das bestätigt noch nicht, dass der Inhalt dem Anwendungsschema entspricht.
Ebenso reichen Dateiname, Endung und der vom Hochladenden angegebene Typ nicht
als Sicherheitsprüfung. Wir prüfen Metadaten zusammen mit dem tatsächlichen
Inhalt.

Vor dem Teilen prüfen wir, ob ein Foto persönliche Ortsdaten oder ein Dokument
einen Autorennamen enthält. Das Entfernen von GPS-Metadaten entfernt keine im
Bild sichtbare Adresse oder Person. Auch bei Metadaten speichern wir nur,
was für den Zweck gebraucht wird.

## Prüfungstaugliche Formulierung

> Metadaten sind Daten, die andere Daten beschreiben.
> Nicht der Hauptinhalt selbst, sondern seine ergänzende Beschreibung,
> zum Beispiel Titel, Autor, Datum, Dateigröße oder Webseitenbeschreibung.
> Metadaten sind wichtig für die Systematisierung, Suche, Darstellung und automatisierte Verarbeitung.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Metadaten?
2. Nenne drei verschiedene Metadaten-Beispiele.
3. Warum sind Metadaten nützlich?
4. Was ist der Unterschied zwischen Metadaten und dem HTML-`<meta>`-Element?
5. Was kann das Risiko von Metadaten sein?

## Kurzantworten zur Selbstkontrolle

1. Daten, die andere Daten beschreiben
2. Autor, Datum, Auflösung
3. Für Suche, Systematisierung, Verarbeitung
4. Metadaten sind ein allgemeiner Begriff, `<meta>` ist ein HTML-Werkzeug
5. Sie können auch sensible Informationen enthalten

## Quellen

Geprüft: `2026-10-14`.

- [W3C: DCAT 3](https://www.w3.org/TR/vocab-dcat-3/): Kataloge und beschreibende Metadaten.
- [MDN: Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type): Typangabe einer HTTP-Repräsentation.
- [Apple: Manage location metadata in Photos](https://support.apple.com/en-gb/guide/personal-safety/ips0d7a5df82/1.0/web/1.0): Umgang mit Ortsdaten beim Teilen.


1. MDN - Metadata
   https://developer.mozilla.org/en-US/docs/Glossary/Metadata
   Verwendung: kurze, klare technische Definition des Begriffs Metadaten.

2. MDN - Web page metadata
   https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML
   Verwendung: praktische Erklärung des Auftretens von Metadaten im Web.

3. MDN - `<meta>` element
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta
   Verwendung: technische Grundlage der Metadatenübermittlung in HTML.

Abgerufen: `2026-04-08`
