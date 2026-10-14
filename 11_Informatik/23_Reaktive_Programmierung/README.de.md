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
| asynchron | Abschluss wird später signalisiert; dadurch wird nicht automatisch jeder Code nicht blockierend |
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

## Einen Datenstrom filtern und umwandeln

**Aufgabe:** Von Lernabschnitten mit `1, 2, 3, 4` Minuten behalten wir nur jene
ab drei Minuten und geben sie in Sekunden weiter. Dies ist ein tatsächliches
RxJS-Beispiel. Zum Ausführen benötigt ein separates Node-Übungsprojekt
`rxjs@7.8.2` und eine `.mjs`-Datei. Für die Nutzung von CoderLAP ist keine
Installation dieses Pakets erforderlich.

```javascript
import { from, filter, map } from "rxjs";

from([1, 2, 3, 4]).pipe(
  filter((minutes) => minutes >= 3),
  map((minutes) => minutes * 60),
).subscribe({
  next: (seconds) => console.log(seconds),
  error: (error) => console.error(error.message),
  complete: () => console.log("done"),
});
```

```text
180
240
done
```

`from` liefert die Eingabewerte. `filter` behält `3` und `4`, `map` berechnet
daraus `180` und `240` Sekunden. `subscribe` startet diese Quelle. `next`
verarbeitet Werte, `error` einen fehlerhaften Abschluss und `complete` das
erfolgreiche Ende. Dieser Datenstrom läuft **synchron**. Das reaktive Modell
bedeutet allein weder Verzögerung noch parallele Threads.

Ein Suchstrom aus Tastatureingaben verarbeitet dagegen über die Zeit eintreffende
Werte. Dabei können das Abwarten einer Eingabepause, das Verwerfen veralteter
Suchergebnisse und das Beenden der Subscription beim Entfernen der Oberfläche
sinnvoll sein. Bei einer schnellen Quelle sind Verarbeitungsgeschwindigkeit
und Puffergröße ebenfalls relevant.

Das Reactive Manifesto beschreibt Eigenschaften **ganzer Systeme**. Allein durch
die Verwendung eines Observable wird ein System noch nicht ausfallsicher oder
elastisch skalierbar.

## Prüfungstaugliche Formulierung

> Reaktive Programmierung ist ein Entwicklungsansatz, der auf Datenströmen, Ereignissen und deren Verarbeitung basiert.
> Das System führt nicht nur Anweisungen der Reihe nach aus, sondern reagiert auf eingehende Änderungen und Nachrichten.
> Das ist besonders nützlich bei asynchronen, Echtzeit- oder skalierbaren Systemen.

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

Geprüft: `2026-10-14`.

- [RxJS: Observable guide source](https://github.com/ReactiveX/rxjs/blob/7.8.2/docs_app/content/guide/observable.md): synchrone und asynchrone Observables, next/error/complete.
- [Reactive Manifesto](https://reactivemanifesto.org/): reaktive Eigenschaften auf Systemebene.


1. The Reactive Manifesto
   https://reactivemanifesto.org/
   Verwendung: offizielle Beschreibung der Grundprinzipien reaktiver Systeme.

2. ReactiveX
   https://reactivex.io/
   Verwendung: bekanntes offizielles Ökosystem des ereignis- und datenstrombasierten Modells der reaktiven Programmierung.

Abgerufen: `2026-04-08`
