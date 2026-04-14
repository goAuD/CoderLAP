# Backup Prinzipien

## Schneller visueller Überblick

| Typ | Was wird gesichert? | Vorteil | Nachteil |
|---|---|---|---|
| Full | alles | einfacher Restore | zeit- und speicherintensiv |
| Incremental | seit der letzten Sicherung geänderte Daten | schneller, kleiner | Restore komplexer |
| Differential | seit der letzten Vollsicherung geänderte Daten | Restore einfacher als bei Incremental | Größe kann wachsen |

## Welche sind die wichtigsten Backup-Grundsätze?

### 1. Regelmäßigkeit

Ein Backup ist nur dann etwas wert, wenn:

- es regelmäßig erstellt wird

### 2. Mehrere Kopien

Gute Praxis:

- nicht nur eine einzige Kopie haben

Dafür gibt es ein bekanntes Prinzip:

- `3-2-1`

das heißt:

- mindestens 3 Kopien
- 2 verschiedene Datenträger
- 1 separate / Offsite-Kopie

### 3. Restore-Test

Es reicht nicht, dass die Sicherung "gelaufen" ist.

Man muss prüfen:

- ob sie tatsächlich wiederhergestellt werden kann

### 4. Getrennte Aufbewahrung

Die Sicherung sollte nicht immer auf dem gleichen System oder im gleichen Raum sein.

### 5. Geeigneter Sicherungstyp

Nicht für alles ist der gleiche Typ am besten.

## Was ist ein Full Backup?

Ein Full Backup:

- sichert alles

Vorteil:

- einfache Wiederherstellung

Nachteil:

- mehr Zeit und Speicherplatz

## Was ist ein Incremental Backup?

Ein Incremental Backup:

- sichert nur die seit der letzten Sicherung geänderten Daten

Vorteil:

- schneller
- weniger Speicherplatz nötig

Nachteil:

- beim Restore können mehr Schritte nötig sein

## Was ist ein Differential Backup?

Ein Differential Backup:

- sichert immer die seit der letzten Vollsicherung geänderten Daten

Vorteil:

- Restore kann einfacher sein als beim Incremental

Nachteil:

- wird mit der Zeit größer als das Incremental

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Backup | Sicherung zur Wiederherstellung |
| Sync | Abgleich der Inhalte zweier Orte, nicht immer ein echtes Backup |
| Archive | längerfristige Aufbewahrung, nicht unbedingt für schnellen Restore |

## Prüfungstaugliche Formulierung

> Zu den Backup-Grundsätzen gehören regelmäßige Sicherung,
> Aufbewahrung in mehreren Kopien und getrennt,
> sowie regelmäßiges Testen der Wiederherstellung.  
> Das Full Backup sichert alle Daten,
> das Incremental nur die seit der letzten Sicherung geänderten Daten,
> und das Differential die seit der letzten Vollsicherung geänderten Daten.  
> Das passende Sicherungsprinzip muss anhand des Wiederherstellungsbedarfs, der Zeit und des Speicherplatzes gewählt werden.

## Häufige Prüfungsfehler

- Sync als Backup bezeichnen.
- Den Unterschied zwischen Full, Incremental und Differential nicht kennen.
- Glauben, dass "Backup wurde erstellt" gleichbedeutend mit Restore-Bereitschaft ist.
- Das 3-2-1-Prinzip nicht erwähnen.

## Schnelle Selbstkontrolle

1. Was ist ein Full Backup?
2. Was ist ein Incremental Backup?
3. Was ist ein Differential Backup?
4. Was ist der Kern des 3-2-1-Prinzips?
5. Ist Sync dasselbe wie Backup?

## Kurzantworten zur Selbstkontrolle

1. Vollständige Sicherung aller Daten
2. Sicherung nur der seit der letzten Sicherung geänderten Daten
3. Sicherung der seit der letzten Vollsicherung geänderten Daten
4. Mehrere Kopien, mehrere Medien, eine separierte Kopie
5. Nein

## Quellen

1. BSI - Datensicherung - wie geht das?  
   https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datensicherung-und-Datenverlust/Datensicherung-wie-geht-das/datensicherung-wie-geht-das.html  
   Verwendung: verständliche, offizielle Erklärung zu Full und Incremental Backup.

2. BSI - CON.3 Datensicherungskonzept (Edition 2023)  
   https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3  
   Verwendung: primäre Quelle für Backup-Grundsätze, Restore-Test und sicheren Sicherungsprozess.

3. CISA - Back Up Business Data  
   https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data  
   Verwendung: moderne, offizielle Zusammenfassung zur 3-2-1-Regel und zur Bedeutung des Testens.

4. CISA - Back Up Government Data  
   https://www.cisa.gov/audiences/state-local-tribal-and-territorial-government/secure-us-sltt/back-government-data  
   Verwendung: weiteres offizielles praktisches Beispiel mit Restore- und Rollback-Aspekten.

Abgerufen: `2026-04-08`
