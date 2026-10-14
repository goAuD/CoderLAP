# Wasserfallmodell Aufbau

## Schneller visueller Überblick

`Anforderungen -> Entwurf -> Implementierung -> Test -> Einführung -> Wartung`

## Was ist das Wesentliche am Wasserfallmodell?

Dass eine Phase möglichst abgeschlossen wird, bevor man zur nächsten übergeht.

Daher ist das Modell:

- gut strukturiert
- stark dokumentationsorientiert
- weniger flexibel in veränderlichen Umgebungen

## Typische Phasen

### 1. Anforderungen

- was das System können muss

### 2. Entwurf

- wie die Lösung aufgebaut sein wird

### 3. Implementierung

- die eigentliche Entwicklung

### 4. Verifikation / Test

- Überprüfung, ob alles korrekt funktioniert

### 5. Einführung und Wartung

- Inbetriebnahme und Fehlerbehebung

## Warum war es lange beliebt?

- einfach verständlich
- leicht zu kommunizieren
- gut dokumentierbar
- kann bei stabilen, vorab bekannten Anforderungen funktionieren

## Wasserfall und agil: nicht verwechseln

| Aspekt | Wasserfall | Agil |
|---|---|---|
| Aufbau | linear | iterativ |
| Änderungsmanagement | schwieriger | flexibler |
| Feedback | später | häufiger |

## Was wird zwischen den Phasen übergeben?

Bei einem Konverter für ein festgelegtes Rechnungsformat entstehen in der Anforderungsphase Feldbeschreibungen und vereinbarte Ein-/Ausgabebeispiele. Der Entwurf beschreibt Verarbeitungsschritte und Fehlermeldungen. Nach der Implementierung prüfen Tests die Umwandlung mit diesen Beispielen; dokumentierte Installation und Übergabe folgen.

Am Phasenübergang halten wir fest, wer das Ergebnis freigibt und welche Version die Grundlage bildet. Kommt später ein Pflichtfeld hinzu, wird die Auswirkung untersucht: Welche Anforderung, welcher Entwurf, welcher Code und welcher Test ändern sich? Eine Rückkehr ist möglich, erfordert aber abgestimmte Änderungskontrolle.

Die Phasenfolge verbietet weder frühe Dokumentenreviews noch das vorgezogene Planen von Tests. Dadurch lassen sich missverständliche Regeln bereits vor der Implementierung klären.

## Prüfungstaugliche Formulierung

> Das Wasserfallmodell ist ein lineares Softwareprozessmodell,
> bei dem die Hauptphasen der Entwicklung
> typischerweise nacheinander ablaufen.  
> Typische Phasen sind Anforderungsanalyse, Entwurf, Implementierung, Test, Einführung und Wartung.  
> Der Vorteil ist die übersichtliche Struktur,
> der Nachteil ist, dass es weniger flexibel ist,
> wenn sich die Anforderungen im Laufe des Projekts ändern.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche am Wasserfallmodell?
2. Welche typischen Phasen hat es?
3. Warum ist es leicht verständlich?
4. Bei welchem Projekttyp kann es eine gute Wahl sein?
5. Was ist der Hauptunterschied zum agilen Ansatz?

## Kurzantworten zur Selbstkontrolle

1. Aufeinanderfolgende, lineare Phasen
2. Anforderung, Entwurf, Entwicklung, Test, Einführung
3. Weil es eine klare Reihenfolge hat
4. Bei Projekten mit stabilen Anforderungen
5. Das Wasserfallmodell ist weniger flexibel

## Quellen

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Testaktivitäten im Entwicklungslebenszyklus und frühe Prüfung.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Atlassian - What is the Waterfall methodology?  
   https://www.atlassian.com/agile/project-management/waterfall-methodology  
   Verwendung: moderne, gut strukturierte Zusammenfassung des Wasserfallmodells und seiner typischen Phasen.

2. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Verwendung: offizieller, aktueller Hintergrund zum Vergleich linearer und iterativer Modelle.

Abgerufen: `2026-04-08`
