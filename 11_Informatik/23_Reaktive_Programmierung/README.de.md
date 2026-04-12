# Reaktive Programmierung

## Schneller visueller Überblick

| Klassische Sichtweise | Reaktive Sichtweise |
|---|---|
| ich frage und warte | ein Ereignis kommt, ich reagiere |
| direkte Aufrufe | Datenströme, Nachrichten |
| häufig blockierende Arbeitsweise | asynchrone Arbeitsweise im Vordergrund |

## Was ist das Wesentliche der reaktiven Programmierung?

In der reaktiven Programmierung gibt es häufig:

- eine Datenquelle oder Ereignisquelle
- Änderungen "fließen" durch das System
- andere Komponenten abonnieren diese und reagieren darauf

Typische Situationen:

- Behandlung von UI-Events
- Echtzeitdaten
- asynchrone Operationen
- nachrichtengesteuerte Architektur

## Wo ist das nützlich?

- Frontend-Interaktionen
- Event-driven Backends
- Streaming-Systeme
- hochbelastete, skalierbare Dienste

## Hauptmerkmale reaktiver Systeme

Der reaktiven Denkweise werden häufig diese Eigenschaften zugeordnet:

- `Responsive` = schnelle Antwort
- `Resilient` = Fehlertoleranz
- `Elastic` = flexible Skalierung
- `Message Driven` = nachrichtengesteuerte Arbeitsweise

## Reaktiv und asynchron: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| asynchron | nicht blockierend, Ergebnis kommt später |
| reaktiv | auf Ereignissen und Datenströmen basierende Denkweise |

Asynchrones Arbeiten ist häufig Teil reaktiver Systeme, aber nicht dasselbe.

## Was ist der Vorteil?

- bessere Reaktionsfähigkeit
- effizientere Ressourcennutzung
- besser handhabbare Parallelität
- bessere Skalierbarkeit bei größeren Systemen

## Worauf muss man achten?

- Die Denkweise der reaktiven Programmierung kann anfangs schwieriger sein.
- Fehlerbehandlung und Zustandsverwaltung können komplexer werden.
- Nicht jedes kleine Projekt erfordert ein reaktives Modell.

## Prüfungstaugliche Formulierung

> Reaktive Programmierung ist ein Entwicklungsansatz, der auf Datenströmen, Ereignissen und deren Verarbeitung basiert.
> Das System führt nicht nur Anweisungen der Reihe nach aus, sondern reagiert auf eingehende Änderungen und Nachrichten.
> Das ist besonders nützlich bei asynchronen, Echtzeit- oder skalierbaren Systemen.

## Häufige Prüfungsfehler

- Reaktive Programmierung einfach als "schnelle Programmierung" bezeichnen.
- Reaktiv und asynchron vollständig gleichsetzen.
- Ereignisse und Datenströme nicht erwähnen.
- Kein praktisches Beispiel nennen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche der reaktiven Programmierung?
2. In welchen Situationen ist sie nützlich?
3. Was ist der Zusammenhang mit asynchronem Arbeiten?
4. Welche vier Merkmale hebt das Reactive Manifesto hervor?
5. Was kann die Schwierigkeit sein?

## Kurzantworten zur Selbstkontrolle

1. Auf Ereignisse und Datenströme reagierende Arbeitsweise
2. UI, Streaming, Backend-Integration, Echtzeitsysteme
3. Sie gehen häufig zusammen, sind aber nicht dasselbe
4. Responsive, Resilient, Elastic, Message Driven
5. Komplexeres Modell und Fehlerbehandlung

## Quellen

1. The Reactive Manifesto
   https://reactivemanifesto.org/
   Verwendung: offizielle Beschreibung der Grundprinzipien reaktiver Systeme.

2. ReactiveX
   https://reactivex.io/
   Verwendung: bekanntes offizielles Ökosystem des ereignis- und datenstrombasierten Modells der reaktiven Programmierung.

Abgerufen: `2026-04-08`
