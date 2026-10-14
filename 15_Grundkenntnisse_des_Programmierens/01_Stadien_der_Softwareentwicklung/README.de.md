# Stadien der Softwareentwicklung

## Schneller visueller Überblick

| Phase | Hauptfrage |
|---|---|
| Planung / Anforderungserhebung | Was muss erstellt werden? |
| Anforderungen | Was genau wird erwartet? |
| Entwurf / Design | Wie soll es funktionieren? |
| Implementierung | Wie schreiben wir es? |
| Testen | Funktioniert es korrekt? |
| Einführung | Kann es in Betrieb genommen werden? |
| Wartung | Wie verbessern und pflegen wir es weiter? |

## Warum gibt es Phasen?

Weil eine ernsthaftere Software nicht sicher erstellt werden kann, indem jemand einfach sofort anfängt zu tippen.

Die Aufteilung in Phasen hilft:

- Missverständnisse zu reduzieren
- Zeit und Kosten besser einzuschätzen
- Fehler frühzeitig zu erkennen
- Verantwortlichkeiten zu klären

## Typische Phasen im Detail

### 1. Anforderungserhebung und Problemverständnis

Hier klären wir:

- was das Problem ist
- wer die Benutzer sind
- was das Ziel ist
- welche Einschränkungen bestehen

### 2. Anforderungsanalyse

Hier wird aus der vagen Anforderung eine konkrete Erwartung.

Zum Beispiel:

- welche Funktionen benötigt werden
- mit welchen Daten das System arbeitet
- welche nicht-funktionalen Anforderungen bestehen

### 3. Entwurf

Hier entscheiden wir:

- wie der Aufbau aussehen soll
- welche Technologien wir verwenden
- mit welchem Datenmodell wir arbeiten
- wie wir das System aufteilen

### 4. Implementierung

Hier geschieht:

- die Programmierung
- die Erstellung der Module
- die Erzeugung der ersten funktionierenden Versionen

### 5. Testen

Hier überprüfen wir:

- ob das System das tut, was es soll
- ob Fehler vorhanden sind
- ob die Teile korrekt zusammenwirken

### 6. Einführung

Hier wird das System in Betrieb genommen:

- Installation
- Übergabe
- Konfiguration
- eventuelle Datenmigration

### 7. Wartung und Weiterentwicklung

Dies ist oft die längste Phase.

Dazu gehört:

- Fehlerbehebung
- Sicherheitsupdates
- Einbau neuer Funktionen
- Leistungsverbesserung

## Lebenszyklus und tägliche Entwicklung: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Softwareentwicklungsphasen | die großen Schritte des gesamten Prozesses |
| tägliche Entwicklerarbeit | konkrete Aufgaben, Codierung, Review, Test, Fehlerbehebung |

## Worauf muss man bei der Prüfung achten?

- nicht nur die Codierung erwähnen
- auch Testen und Wartung nennen
- die Phasen nicht mit konkreten Methoden wie `Scrum` oder dem Wasserfallmodell verwechseln

## Eine Anforderung durch den Lebenszyklus verfolgen

Wir entwickeln eine Kursanmeldung. Der Wunsch lautet: „Man soll sich anmelden
können.“ Daraus wird eine überprüfbare Anforderung: Eine Person darf sich pro
Termin einmal anmelden; die Bestätigung erscheint erst nach erfolgreicher Speicherung.

| Phase | Überprüfbares Ergebnis |
|---|---|
| Analyse | Kapazität, Berechtigungen und Akzeptanzkriterien |
| Entwurf | Oberflächenentwurf, Datenmodell, gleichzeitige Anmeldungen |
| Implementierung | Speicherung und verständliche Rückmeldung |
| Test | freier Platz, voller Termin, wiederholter Klick |
| Einführung | erprobte Installation, Sicherung und Wiederherstellungsplan |
| Wartung | Verbesserung aus Rückmeldungen, anschließend erneuter Test |

Die Phasen beschreiben Tätigkeiten, keine zwingend einmalige Reihenfolge. Bei
iterativer Entwicklung durchläuft eine kleine Funktion diese Tätigkeiten mehrfach.
Testfälle lassen sich bereits mit den Anforderungen planen. Validierung fragt,
ob wir das tatsächliche Problem der Benutzer lösen. Verifizierung prüft, ob die
Lösung die festgelegten Anforderungen erfüllt. Dafür können unterschiedliche
Nachweise erforderlich sein: ein Benutzertest beziehungsweise ein Test anhand
der Spezifikation.

## Prüfungstaugliche Formulierung

> Die Softwareentwicklung besteht aus mehreren aufeinander aufbauenden Phasen.  
> Die typischen Schritte sind Anforderungserhebung, Anforderungsanalyse, Entwurf, Implementierung, Testen, Einführung  
> und Wartung.  
> Der Zweck dieser Aufteilung ist, die Entwicklung übersichtlicher, kontrollierbarer und sicherer zu machen.

## Schnelle Selbstkontrolle

1. Warum wird die Softwareentwicklung in Phasen unterteilt?
2. Was geschieht während der Anforderungsanalyse?
3. Was ist das Hauptziel der Entwurfsphase?
4. Warum endet der Prozess nicht mit der Fertigstellung des Programms?
5. Welche sind die wichtigsten Hauptphasen?

## Kurzantworten zur Selbstkontrolle

1. Damit sie übersichtlicher und handhabbarer wird
2. Wir konkretisieren die Erwartungen
3. Die technische Lösung festzulegen
4. Weil es noch eingeführt und gewartet werden muss
5. Anforderung, Analyse, Entwurf, Implementierung, Test, Einführung, Wartung

## Quellen

Geprüft: `2026-10-14`.

- [IBM: Software Development Lifecycle](https://www.ibm.com/think/topics/sdlc): Lebenszyklus und Rückkopplung; das Kursbeispiel ist eigenständig.


1. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Verwendung: moderner, offizieller Überblick über die Hauptphasen der Softwareentwicklung.

2. Atlassian - SDLC  
   https://www.atlassian.com/en/agile/software-development/sdlc  
   Verwendung: praxisnahe, leicht verständliche Zusammenfassung der Hauptschritte des Software-Lebenszyklus.

Abgerufen: `2026-04-09`
