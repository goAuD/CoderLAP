# Datenminimierung

## Schneller visueller Überblick

| Zweck | Beispiel notwendiger Daten | Entwurfsentscheidung |
|---|---|---|
| Newsletter zustellen | E-Mail-Adresse | nur für Zustellung und Einwilligungsnachweis erforderliche Daten |
| Paket zustellen | Name, Lieferadresse | die Zustellung begründet die Adressangabe |
| Benutzereinstellung speichern | interne Kontokennung, Einstellung | kein vollständiges Kundenprofil in die Einstellungstabelle kopieren |
| Fehler untersuchen | Fehlercode, erforderliche technische Umgebung | persönliche Formularinhalte aus Protokollen weglassen |

## Wo steht das in der GDPR?

Die Datenminimierung ist mit **Art. 5 Abs. 1 lit. c)** der GDPR verknüpft.

Kern:

- die Daten müssen
  - dem Zweck angemessen sein
  - erheblich sein
  - auf das für den Zweck Notwendige beschränkt sein

## Was bedeutet das in der Praxis?

Wenn beispielsweise ein Webshop nur Warenlieferungen durchführt, kann in der Regel Folgendes gerechtfertigt sein:

- Name
- Lieferadresse
- Kontaktdaten

In der Regel **nicht** gerechtfertigt sind zum Beispiel:

- Familienstand
- religiöse Überzeugung
- persönliche Interessen

wenn diese für die Abwicklung der Bestellung nicht erforderlich sind.

## Beispiele

### 1. Newsletter-Anmeldung

Wenn jemand nur einen Newsletter abonniert, kann in der Regel Folgendes ausreichen:

- E-Mail-Adresse

Nicht unbedingt erforderlich:

- Wohnadresse
- Geburtsdatum
- Telefonnummer

### 2. Stellenbewerbung

Es dürfen nur Daten abgefragt werden, die für die Auswahl gerechtfertigt sind.

### 3. Kundenregistrierung

Es sollte nicht zu viele Pflichtfelder geben, wenn diese für die Dienstleistung nicht erforderlich sind.

## Datenminimierung und Zweckbindung

Die beiden Begriffe hängen zusammen, sind aber nicht dasselbe.

| Begriff | Was bedeutet er? |
|---|---|
| Zweckbindung | für die Datenverarbeitung braucht es einen klaren Zweck |
| Datenminimierung | nur die für den Zweck notwendigen Daten dürfen verarbeitet werden |

## Datenminimierung und Aufbewahrungsfrist

Datenminimierung begrenzt Umfang und Detailgrad auf das für den Zweck Erforderliche
(Art. 5 Abs. 1 lit. c). Die Dauer regelt der eigenständige Grundsatz der
**Speicherbegrenzung** (Art. 5 Abs. 1 lit. e). Beide wirken zusammen:
angemessene Datenmengen werden nur so lange wie begründet verarbeitet.

## Warum ist das wichtig?

Weil weniger verarbeitete Daten bedeuten:

- geringeres Risiko
- einfacherer Schutz
- geringeres Missbrauchspotenzial
- leichtere Einhaltung der GDPR

## Ein Formular begründet entwerfen

Für eine Reparaturbuchung verwenden wir Name, Kontaktmöglichkeit, Gerätetyp und Termin.
Eine Ausweiskopie ist für diese Buchung nicht erforderlich. Erfolgt die Rückmeldung
per E-Mail, muss eine zusätzliche Telefonnummer als Pflichtfeld gesondert begründet werden.

Die Entscheidung lässt sich knapp festhalten: **Feld → Zweck → Erforderlichkeit → Zugriff → Löschung**.
Für die Fehlerbeschreibung reichen vielleicht einige Kategorien statt eines Freitexts.
Brauchen wir Freitext, erklären wir, dass keine Passwörter oder sensiblen Angaben
über andere Personen eingetragen werden sollen. Die Bezeichnung „optional“ allein
rechtfertigt nicht jede zusätzliche Datenerhebung.

Auch der Server verarbeitet nur zugelassene Felder; das Protokoll speichert nicht
automatisch die vollständige Anfrage. Tests verwenden künstliche Daten.
Für einen späteren Export gilt dieselbe Auswahl: Der Empfänger erhält die für
seine Aufgabe erforderlichen Daten, nicht automatisch die gesamte Tabelle.

Quelle: [EDPB: Verarbeitungsgrundsätze](https://www.edpb.europa.eu/sme/learn-the-basics/data-protection-basics_en),
Art. 5 und 25 DSGVO. Die Buchung ist eine eigene Entwurfsübung. Geprüft: 2026-10-14.

## Prüfungstaugliche Formulierung

> Die Datenminimierung ist ein Grundsatz der GDPR.
> Sie besagt, dass nur personenbezogene Daten verarbeitet werden dürfen,
> die für den jeweiligen Verarbeitungszweck notwendig, angemessen und erheblich sind.
> In der Praxis bedeutet das, dass keine unnötigen Daten erhoben werden dürfen
> während die Aufbewahrungsdauer nach dem eigenständigen Grundsatz der Speicherbegrenzung festgelegt wird.

## Schnelle Selbstkontrolle

1. Was bedeutet Datenminimierung?
2. Warum darf man keine unnötigen Daten erheben?
3. Was ist der Zusammenhang zwischen Zweck und Datenminimierung?
4. Gilt dieser Grundsatz nur für die Erhebung?
5. Nenne ein gutes praktisches Beispiel.

## Kurzantworten zur Selbstkontrolle

1. Es dürfen nur die notwendigen personenbezogenen Daten verarbeitet werden
2. Weil die GDPR dies verbietet, wenn die Daten für den Zweck nicht erforderlich sind
3. Die Notwendigkeit muss immer anhand des Zwecks beurteilt werden
4. Nein, auch der Datenumfang bei Verwendung und Weitergabe ist begrenzt; die Dauer regelt ein eigener Grundsatz
5. Für einen Newsletter kann allein die E-Mail-Adresse ausreichen

## Quellen

1. EUR-Lex - Regulation (EU) 2016/679
   https://eur-lex.europa.eu/eli/reg/2016/679/oj
   Verwendung: Art. 5(1)(c) - data minimisation als primäre Rechtsquelle.

2. USP - Datenschutz: allgemeine Informationen
   https://www.usp.gv.at/it-geistiges-eigentum/datenschutz/allgemeine-informationen.html
   Verwendung: österreichische, an Unternehmen gerichtete offizielle Erklärung zu Datenverarbeitungsgrundsätzen.

3. Datenschutzbehörde - Was ist Datenschutz?
   https://dsb.gv.at/rechte-pflichten/was-ist-datenschutz
   Verwendung: österreichische behördliche Übersicht über personenbezogene Daten und Datenschutzgrundsätze.

Abgerufen: `2026-04-08`
