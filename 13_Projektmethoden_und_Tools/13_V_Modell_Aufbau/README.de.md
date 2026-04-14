# V-Modell Aufbau

## Schneller visueller Überblick

```text
Anforderungen        ->        Abnahmetest
Systementwurf        ->        Systemtest
Architektur / Design ->        Integrationstest
Modulentwurf         ->        Modultest
            Implementierung
```

## Was ist das Wesentliche am V-Modell?

Die V-Form zeigt, dass:

- die Entwicklung nach unten hin immer detaillierter wird
- nach der Implementierung auf der rechten Seite die Überprüfung stattfindet
- jeder Planungsstufe eine Teststufe zugeordnet werden kann

Das ist die klassische, in Prüfungen häufig erwartete Grundlogik.  
Das offizielle `V-Modell XT` erweitert dies um Projektsteuerungs-, Qualitätssicherungs- und Änderungsmanagementelemente.

## Typischer Aufbau

### Linke Seite

- Anforderungsdefinition
- Systementwurf
- Detailentwurf

### Unten

- Implementierung / Codierung

### Rechte Seite

- Modultest
- Integrationstest
- Systemtest
- Abnahmetest

## Warum ist dieser Aufbau wichtig?

- man muss bereits früh an das Testen denken
- es lässt sich besser nachvollziehen, was woraus folgt
- in regulierten Umgebungen gut einsetzbar

## V-Modell und Wasserfallmodell: nicht verwechseln

| Begriff | Art |
|---|---|
| Wasserfallmodell | lineare Phasen nacheinander |
| V-Modell | linearer Charakter + Zuordnung von Entwicklung und Test |

## Prüfungstaugliche Formulierung

> Das V-Modell ist ein Prozessmodell, bei dem Entwicklungs- und Testaktivitäten einander zugeordnet sind.  
> Auf der linken Seite befinden sich die Anforderungen und der Entwurf,
> unten die Implementierung
> und auf der rechten Seite die zugehörigen Teststufen.  
> Der Hauptvorteil des Modells ist, dass das Testen bereits in der frühen Planungsphase Gewicht bekommt.

## Häufige Prüfungsfehler

- Das V-Modell als völlig identisch mit dem Wasserfallmodell betrachten.
- Die Zuordnung der Teststufen nicht erwähnen.
- Nur die V-Form beschreiben, nicht aber ihre Bedeutung.
- Die zentrale Rolle der Implementierung auslassen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche am V-Modell?
2. Was steht auf der linken Seite?
3. Was steht auf der rechten Seite?
4. Warum ist die Zuordnung des Testens wichtig?
5. Was bietet das V-Modell mehr als das Wasserfallmodell?

## Kurzantworten zur Selbstkontrolle

1. Die Zuordnung von Entwicklungs- und Testschritten
2. Anforderungen und Entwurf
3. Die entsprechenden Teststufen
4. Weil es die Überprüfung planbarer macht
5. Es betont die Zuordnung zum Testen besonders

## Quellen

1. V-Modell XT Bund 2.0 - Gesamt PDF  
   https://download.gsb.bund.de/BundesCIO/V-Modell_XT_Bund/V-Modell-XT-Bund-2.0-Gesamt.pdf  
   Verwendung: offizielle, primäre Quelle zum Aufbau und zu den Begriffen des V-Modells.

2. Einstieg in das V-Modell XT Bund  
   https://download.gsb.bund.de/BundesCIO/V-Modell_XT_Bund/V-Modell%20XT%20Bund-2.0-HTML/1431a155da001978.html  
   Verwendung: kürzere, offizielle Überblickseinführung in die Logik des Modells.

Abgerufen: `2026-04-08`
