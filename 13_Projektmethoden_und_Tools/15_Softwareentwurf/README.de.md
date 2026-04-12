# Softwareentwurf

## Schneller visueller Überblick

| Frage | Antwort des Softwareentwurfs |
|---|---|
| woraus besteht das System? | Komponenten, Module |
| wie hängen sie zusammen? | Schnittstellen, Datenfluss |
| wo speichern wir die Daten? | Datenmodell, Datenbank |
| wie wird es gut erweiterbar? | Architektur und Trennung der Verantwortlichkeiten |

## Was ist ein Softwareentwurf?

Der Softwareentwurf ist der Schritt zwischen Anforderungen und Implementierung.

Hier wird unter anderem entschieden:

- welche Architektur verwendet wird
- in welche Module das System aufgeteilt wird
- welche Schnittstellen es geben wird
- wie die Daten verwaltet werden
- wie Testbarkeit und Wartbarkeit unterstützt werden

## Warum ist das wichtig?

- reduziert das Chaos während der Entwicklung
- unterstützt die Teamarbeit
- verbessert die Erweiterbarkeit
- erleichtert Fehlersuche und Änderungen

## Typische Entwurfselemente

- Architektur
- Schichten oder Komponenten
- Datenmodell
- APIs und Schnittstellen
- Platzierung der Geschäftslogik
- Fehlerbehandlung
- Sicherheits- und Performance-Aspekte

## Anforderung, Entwurf, Implementierung: nicht verwechseln

| Begriff | Fokus |
|---|---|
| Anforderung | was das System können muss |
| Softwareentwurf | wie wir es aufbauen |
| Implementierung | die konkrete Umsetzung im Code |

## Prüfungstaugliche Formulierung

> Der Softwareentwurf ist der Plan für die technische Umsetzung der Anforderungen.  
> Er legt den Aufbau des Systems, die Komponenten, die Schnittstellen, die Datenverarbeitung und die wichtigen Entwurfsentscheidungen fest.  
> Sein Ziel ist es, dass die Entwicklung übersichtlich, erweiterbar und wartbar ist.

## Häufige Prüfungsfehler

- Den Softwareentwurf mit der Anforderungsspezifikation verwechseln.
- Glauben, dass es bereits die Codierung selbst ist.
- Die Rolle von Architektur und Schnittstellen auslassen.
- Nur an die Oberfläche denken und nicht an das gesamte System.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche am Softwareentwurf?
2. Warum braucht man ihn vor dem Codieren?
3. Welche Elemente enthält er üblicherweise?
4. Was ist der Unterschied zwischen Anforderung und Entwurf?
5. Wie unterstützt er die Wartbarkeit?

## Kurzantworten zur Selbstkontrolle

1. Die vorherige Planung der technischen Umsetzung
2. Weil er Struktur und Richtung gibt
3. Architektur, Module, Schnittstellen, Datenverarbeitung
4. Die Anforderung beantwortet das Was, der Entwurf das Wie
5. Durch bessere Trennung und Übersichtlichkeit

## Quellen

1. Microsoft Learn - Architecture styles  
   https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/  
   Verwendung: moderne, offizielle Quelle zur Rolle von Architektur, Schichten und Entwurfs-Trade-offs.

2. Atlassian Confluence - UML diagram template  
   https://www.atlassian.com/software/confluence/templates/uml-diagram  
   Verwendung: praxisnahe Quelle zur visuellen Dokumentation und zu Systemdiagrammen im Softwareentwurf.

Abgerufen: `2026-04-08`
