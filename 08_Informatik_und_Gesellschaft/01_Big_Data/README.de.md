# Big Data

## Schneller visueller Überblick

| Merkmal | Bedeutung |
|---|---|
| Volume | sehr große Datenmenge |
| Velocity | schneller Datenfluss |
| Variety | vielfältige Formate und Quellen |
| Value | geschäftlicher oder gesellschaftlicher Nutzen |

## Was ist Big Data?

Big Data bedeutet nicht einfach "viele Daten".

Es bedeutet vielmehr, dass die Daten:

- zu groß
- zu schnell
- zu vielfältig

sind, als dass sie mit herkömmlichen Lösungen immer einfach verarbeitet werden könnten.

## Woher können große Datenmengen stammen?

Beispiele:

- soziale Medien
- Kauftransaktionen
- Sensoren
- GPS-Signale
- Bilder, Videos
- Maschinenprotokolle

## Warum ist das wichtig?

Weil gute Datenanalyse helfen kann:

- bessere Entscheidungen zu treffen
- Prozesse zu optimieren
- Muster zu erkennen
- Fehler oder Betrug zu entdecken
- personalisierte Dienstleistungen anzubieten

## Welche Risiken gibt es?

- Datenschutzrisiko
- fehlerhafte oder verzerrte Daten
- übermäßige Überwachung
- diskriminierende Entscheidungen
- schwierige Datenqualitätskontrolle

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Big Data | Verarbeitung großer, schneller, vielfältiger Daten |
| Datenbank | strukturiertes Speichersystem für Daten |
| AI / Machine Learning | Methode zur Datenanalyse, nicht dasselbe wie Big Data selbst |

## Durchgearbeitetes Beispiel: von Datenmengen zur Entscheidung

In einem fiktiven Werk senden 1000 Sensoren je einen Datensatz von 100 Byte pro Sekunde. Der Rohdatenstrom beträgt `1000 × 100 = 100 000 B/s`, täglich also `8 640 000 000 B` beziehungsweise `8,64 GB`. Indizes, Kopien und Netzwerk-Header sind noch nicht enthalten. Die Zahl allein macht daraus kein Big-Data-Problem: Geschwindigkeit, Verarbeitungsfrist und unterschiedliche Formate zählen ebenfalls.

Vor der Analyse prüfen wir Zeitstempel, Einheiten und fehlende Messungen. Millionen falscher Sensorwerte werden durch ihre Menge nicht zuverlässig. Diesen Zuverlässigkeitsaspekt bezeichnet man häufig als `Veracity`. `3V`, `4V` und `5V` sind unterschiedliche Erklärungsmodelle, keine einzige verbindliche Liste.

Eine mögliche Entscheidung ist die Kontrolle eines Lagers bei zunehmender Vibration. Das Muster liefert einen Hinweis; die Ursache muss fachlich überprüft werden.

## Prüfungstaugliche Formulierung

> Big Data bezeichnet die Verarbeitung und Analyse großer Mengen von Daten,
> die schnell entstehen und aus vielfältigen Quellen stammen.  
> Der Begriff wird häufig mit den Merkmalen `Volume`, `Velocity` und `Variety` beschrieben.  
> Der Vorteil besteht darin, dass wertvolle Informationen gewonnen werden können,
> gleichzeitig birgt es jedoch Risiken in Bezug auf Datenschutz, Qualität und Ethik.

## Schnelle Selbstkontrolle

1. Was bedeutet `Volume`?
2. Was bedeutet `Velocity`?
3. Was bedeutet `Variety`?
4. Nenne zwei Big-Data-Datenquellen.
5. Nenne einen Vorteil und ein Risiko.

## Kurzantworten zur Selbstkontrolle

1. Große Datenmenge
2. Schnelle Datenentstehung / schneller Datenfluss
3. Vielfältige Daten und Quellen
4. Zum Beispiel Sensoren und Transaktionen
5. Vorteil: bessere Entscheidungsunterstützung; Risiko: Datenschutzproblem

## Quellen

- [NIST: Big data](https://csrc.nist.gov/topics/technologies/big-data)  
  Skalierbare Architektur und Big-Data-Merkmale.

- [NIST: The real challenge of Big Data](https://www.nist.gov/baldrige/real-challenge-big-data)  
  Veracity und Datenqualität; keine feste Byte-Schwelle.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. NIST - Big Data Interoperability Framework: Volume 1, Definitions  
   https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2  
   Verwendung: offizielle NIST-Definition und primäre Quelle für die Grundbegriffe von Big Data.

2. European Commission - Big data  
   https://digital-strategy.ec.europa.eu/en/policies/big-data  
   Verwendung: EU-Zusammenfassung über die wirtschaftliche und gesellschaftliche Rolle von Big Data.

Abgerufen: `2026-04-08`
