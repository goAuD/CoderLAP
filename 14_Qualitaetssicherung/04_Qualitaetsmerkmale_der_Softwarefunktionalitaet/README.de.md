# Qualitätsmerkmale der Softwarefunktionalität

## Schneller visueller Überblick

| Teilbereich | Was bedeutet es? |
|---|---|
| functional completeness | alle erforderlichen Funktionen sind vorhanden |
| functional correctness | liefert korrekte Ergebnisse |
| functional appropriateness | unterstützt die Aufgabe gut |

## Was verstehen wir hier unter funktionaler Qualität?

Es reicht nicht, dass "eine Funktion vorhanden ist".

Gute Funktionalität bedeutet, dass:

- das System kann, was es soll
- es korrekt funktioniert
- es das Ziel auf brauchbare Weise unterstützt

## Die drei wichtigen Teilbereiche

### 1. Functional completeness

Die Vollständigkeit der benötigten Funktionen.

Frage:

- ist alles enthalten, was tatsächlich benötigt wird?

### 2. Functional correctness

Die Korrektheit des Systems.

Frage:

- liefert die Funktion genaue, korrekte Ergebnisse?

### 3. Functional appropriateness

Die Angemessenheit der Funktionen.

Frage:

- unterstützt die Lösung die Aufgabe des Benutzers tatsächlich gut?

## Beispiel

Bei einer Webshop-Warenkorbfunktion:

- **completeness**: Produkt hinzufügen, löschen, ändern möglich
- **correctness**: der Gesamtbetrag ist korrekt
- **appropriateness**: Rabatt und Versand lassen sich innerhalb der Kaufaufgabe berechnen

## Funktionalität und Benutzerfreundlichkeit: nicht verwechseln

| Begriff | Fokus |
|---|---|
| funktionale Qualität | was es kann und wie korrekt |
| Benutzerfreundlichkeit | wie einfach es zu benutzen ist |

Es gibt einen Zusammenhang, aber es ist nicht dasselbe.

## Vollständigkeit, Korrektheit und Angemessenheit getrennt prüfen

Ein Verleih benötigt neben Reservierung auch Verlängerung und Rücknahme. Fehlt eine dieser Funktionen, ist die funktionale Vollständigkeit unzureichend. Sind alle vorhanden, aber eine Rücknahme gibt das falsche Gerät frei, betrifft das die funktionale Korrektheit.

Angemessenheit betrachtet, wie die verfügbaren Funktionen die gezielte Aufgabenerledigung unterstützen. Eine Sammelrücknahme verarbeitet etwa die Geräte einer ganzen Klasse, ohne Hilfsberechnungen in einer externen Tabelle zu verlangen. Lesbarkeit des Knopfs und Erlernbarkeit gehören eher zur Interaktionsqualität, Antwortzeiten zur Leistungseffizienz.

Das Produktqualitätsmodell ISO/IEC 25010:2023 enthält neun Hauptmerkmale; Functional Suitability ist eines davon. Seine drei Untermerkmale bleiben Completeness, Correctness und Appropriateness. Die Gruppe Usability aus 2011 wird im Modell von 2023 durch Interaction Capability mit veränderten Einzelheiten abgelöst.

## Prüfungstaugliche Formulierung

> Die Qualität der Softwarefunktionalität drückt aus,
> ob das System die erforderlichen Funktionen vollständig,
> korrekt und in Bezug auf die Aufgabe angemessen bereitstellt.  
> In der ISO 25010-Terminologie gehört dies
> zum Bereich Functional Suitability,
> dessen Hauptbestandteile Functional Completeness,
> Functional Correctness und Functional Appropriateness sind.  
> Gute Software verfügt also nicht nur über viele Funktionen, sondern bietet diese auch präzise und zweckmäßig an.

## Schnelle Selbstkontrolle

1. Was bedeutet Functional Completeness?
2. Was bedeutet Functional Correctness?
3. Was bedeutet Functional Appropriateness?
4. Warum reichen viele Funktionen allein nicht aus?
5. Was ist der Unterschied zwischen funktionaler Qualität und Benutzerfreundlichkeit?

## Kurzantworten zur Selbstkontrolle

1. Das Vorhandensein aller erforderlichen Funktionen
2. Korrekte Funktionsweise und Ergebnisse
3. Gute Unterstützung der Aufgabe
4. Weil die Funktion fehlerhaft oder schlecht passend sein kann
5. Das eine prüft die Angemessenheit der Funktionen, das andere die einfache Bedienung

## Quellen

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html)  
  Offizielle Beschreibung des aktuellen Produktqualitätsmodells.

- [ISTQB: Advanced Level Test Analyst v4.0, Appendix A](https://istqb.org/?download_id=5745&sdm_process_download=1)  
  Offizielle prüfungsfachliche Gegenüberstellung der Qualitätsmerkmale von 2011 und 2023.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. ISO/IEC 25010:2023 - Product quality model  
   https://www.iso.org/standard/78176.html  
   Verwendung: offizielle Primärquelle zum Softwarequalitätsmodell.

2. AQCLab - Functional Suitability Evaluation and Certification - ISO/IEC 25000  
   https://aqclab.es/index.php/en/software-quality-evaluation-certification-iso-25000/functional-suitability-evaluation-certification-iso-25000  
   Verwendung: aktuelle, auf ISO 25000 bezogene erklärende Quelle zu den Untermerkmalen der `Functional Suitability`.

Abgerufen: `2026-04-08`
