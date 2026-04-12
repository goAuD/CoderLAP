# Redundanz in Datenbanken

## Schneller visueller Überblick

| Situation | Folge |
|---|---|
| dieselben Daten in mehreren Tabellen / Zeilen wiederholt | höhere Fehlerwahrscheinlichkeit |
| ein Datum ändert sich, aber nicht überall | Widerspruch entsteht |
| gut normalisiertes Modell | weniger unnötige Wiederholung |

## Was ist Redundanz?

Von Redundanz spricht man, wenn ein Datum:

- mit derselben Bedeutung
- an mehreren Stellen
- unnötig wiederholt wird

Beispiel:

Wenn die Adresse eines Kunden in jeder Bestellzeile vollständig erneut gespeichert wird, ist das typische Redundanz.

## Warum ist das ein Problem?

- verbraucht mehr Speicherplatz
- schwieriger zu warten
- leicht widersprüchliche Daten entstehen
- kann zu Update-, Insert- und Delete-Anomalien führen

## Typische Anomalien

### Update-Anomalie

Dieselben Daten müssen an vielen Stellen geändert werden.

### Insert-Anomalie

Man kann etwas nicht speichern, ohne gleichzeitig andere überflüssige Daten erfassen zu müssen.

### Delete-Anomalie

Beim Löschen eines Datensatzes gehen unbeabsichtigt andere wichtige Informationen verloren.

## Ist Redundanz immer schlecht?

Nicht unbedingt.

Manchmal wird sie bewusst in Kauf genommen:

- aus Performancegründen
- bei Reporting oder Data Warehouse
- für schnelleres Lesen

Bei der Prüfung ist es eine gute Antwort, wenn man sagt:

- unnötige Redundanz sollte vermieden werden
- aber in bestimmten Situationen kann kontrollierte Redundanz gerechtfertigt sein

## Redundanz und wiederholte Daten - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| sinnvolle Wiederholung | zum Beispiel mehrere Bestellungen desselben Kunden |
| Redundanz | unnötige erneute Speicherung derselben Information |

## Prüfungstaugliche Formulierung

> Redundanz in einer Datenbank bedeutet, dass dieselbe Information unnötig an mehreren Stellen gespeichert wird.  
> Das erhöht den Speicherbedarf und kann zu Dateninkonsistenzen führen, zum Beispiel wenn eine Änderung nicht an allen Stellen durchgeführt wird.  
> Eines der Ziele des relationalen Datenbankentwurfs ist die Reduzierung unnötiger Redundanz, zum Beispiel durch Normalisierung.

## Häufige Prüfungsfehler

- Redundanz an sich immer als Fehler bezeichnen.
- Die Gefahr der Inkonsistenz nicht erwähnen.
- Mit natürlichem Mehrfachvorkommen verwechseln.
- Den Zusammenhang mit der Normalisierung weglassen.

## Schnelle Selbstkontrolle

1. Was ist Datenredundanz?
2. Warum ist sie gefährlich?
3. Was ist eine Update-Anomalie?
4. Wie kann Redundanz reduziert werden?
5. Kann Redundanz manchmal gerechtfertigt sein?

## Kurzantworten zur Selbstkontrolle

1. Unnötige Wiederholung derselben Information
2. Weil sie zu Fehlern und Widersprüchen führen kann
3. Wenn dieselben Daten an mehreren Stellen geändert werden müssen
4. Durch gutes Design und Normalisierung
5. Ja, zum Beispiel aus Performancegründen

## Quellen

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Verwendung: offizielle, gut verwendbare Quelle zum Verständnis des Zusammenhangs zwischen Redundanz und relationalem Entwurf.

2. Microsoft Learn - Description of the database normalization basics  
   https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/access/database-normalization-description  
   Verwendung: offizieller Hintergrund zur Reduzierung von Redundanz und zum Zweck der Normalisierung.

Abgerufen: `2026-04-09`
