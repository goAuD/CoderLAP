# Pflichtenheft

## Schneller visueller Überblick

| Dokument | Hauptfrage |
|---|---|
| `Lastenheft` | was und warum gelöst werden muss |
| `Pflichtenheft` | wie es gelöst wird |

## Was ist das Pflichtenheft?

Das `Pflichtenheft` ist die Umsetzungsbeschreibung der Lösung.

Es enthält typischerweise:

- das Umsetzungskonzept
- funktionale und technische Details
- Systemgrenzen
- Schnittstellen
- Qualitätsanforderungen
- Zeitplan- oder Übergabeaspekte

## Warum ist das wichtig?

- verdeutlicht die Art der Lösung
- reduziert Missverständnisse zwischen Auftraggeber und Auftragnehmer
- bildet die Grundlage für Entwicklung, Test und Abnahme

## Wann wird es erstellt?

Typischerweise:

1. zuerst wird das `Lastenheft` erstellt
2. danach erarbeitet die umsetzende Seite das `Pflichtenheft`
3. dieses wird abgestimmt und genehmigt
4. danach beginnt die detaillierte Umsetzung

## Was darf man nicht verwechseln?

| Begriff | Bedeutung |
|---|---|
| `Lastenheft` | die Gesamtheit der Auftraggeberanforderungen |
| `Pflichtenheft` | der detaillierte Umsetzungsplan |

## Worauf muss man achten?

- nicht zu vage sein
- technisch nachvollziehbar sein
- die Auftraggeberanforderungen abdecken
- abgestimmt und überprüfbar sein

## Von der Anforderung zur Umsetzungsspezifikation

Die Anforderung K-03 im Lastenheft lautet: Berechtigte Sachbearbeiter können Buchungen eines ausgewählten Tages herunterladen. Das Pflichtenheft beschreibt dazu beispielsweise Datumsauswahl, serverseitige Berechtigungsprüfung und CSV-Spalten: Buchungskennung und Uhrzeit. Die Datei verwendet UTF-8; nicht benötigte personenbezogene Daten entfallen.

Für die Abnahme werden an einem vorbereiteten Tag drei Buchungen angelegt. Die Ausgabe muss genau diese drei Zeilen enthalten, ohne Buchungen anderer Tage. Auch eine direkte Anfrage eines unberechtigten Benutzers darf keinen Export liefern. Anforderung, Lösung und Prüfung sind über dieselbe Kennung verbunden.

Die freigegebene Version muss erkennbar sein. Bei einer zusätzlichen Spalte prüft man Auswirkungen auf Datenschutz, Tests und Termin und aktualisiert anschließend die vereinbarte Beschreibung. Der Detaillierungsgrad hängt vom Projekt ab; nicht jede Entwicklung benötigt ein einziges, im Voraus vollständig abgeschlossenes Großdokument.

## Prüfungstaugliche Formulierung

> Das Pflichtenheft ist die detaillierte Beschreibung der Umsetzung,
> die festhält, wie die vom Auftraggeber vorgegebenen Anforderungen erfüllt werden.  
> Typischerweise wird es von der Auftragnehmer- bzw. Entwicklerseite auf Basis des Lastenhefts erarbeitet.  
> Seine wichtige Rolle besteht darin, eine technisch eindeutige Grundlage für Entwicklung, Test und spätere Abnahme zu bieten.

## Schnelle Selbstkontrolle

1. Was ist der Hauptzweck des Pflichtenhefts?
2. Welche Frage beantwortet es?
3. Nach welchem Dokument wird es erstellt?
4. Wer erarbeitet es typischerweise?
5. Warum ist es für die Entwicklung wichtig?

## Kurzantworten zur Selbstkontrolle

1. Die Beschreibung der Umsetzung
2. Die Frage, wie wir es lösen
3. Nach dem Lastenheft
4. Die umsetzende / ausführende Seite
5. Weil es eine technische Grundlage für die Arbeit bietet

## Quellen

- [IREB: CPRE Glossary](https://cpre.ireb.org/en/downloads-and-resources/glossary)  
  Anforderungsarten, Akzeptanzkriterien und Nachverfolgbarkeit.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. IHK Frankfurt am Main - Software-Erstellungsvertrag  
   https://www.frankfurt-main.ihk.de/recht/mustervertraege/software-erstellungsvertrag-5199364  
   Verwendung: offizielle IHK-Quelle, die den Inhalt und die vertragliche Rolle des Pflichtenhefts darstellt.

2. Wikipedia - Pflichtenheft  
   https://de.wikipedia.org/wiki/Pflichtenheft  
   Verwendung: gut strukturierte Zusammenfassung des Pflichtenheft-Begriffs,
   Inhalts und der praktischen Anwendung,
   gestützt auf DIN 69901 und VDI-Referenzen.

Abgerufen: `2026-04-08`
