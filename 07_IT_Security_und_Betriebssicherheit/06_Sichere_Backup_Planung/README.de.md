# Sichere Backup Planung

## Schneller visueller Überblick

| Frage | Warum wichtig? |
|---|---|
| Was sichern wir? | damit keine kritischen Daten übersehen werden |
| Wie oft? | das Ausmaß des Datenverlusts hängt auch davon ab |
| Wohin sichern wir? | Sicherheit und Wiederherstellung |
| Wurde es getestet? | funktioniert der Restore tatsächlich |
| Wer ist verantwortlich? | klare Verantwortlichkeit muss bestehen |

## Was muss zuerst entschieden werden?

### 1. Was muss gesichert werden?

Nicht alles hat die gleiche Priorität.

Kritisch können beispielsweise sein:

- Kundendaten
- Dokumente
- Datenbank
- Konfiguration
- E-Mails
- Projektdateien

### 2. Wie schnell muss wiederhergestellt werden?

Hier kommen zwei wichtige Begriffe ins Spiel:

- `RPO` = wie viel Datenverlust ist akzeptabel
- `RTO` = wie viel Ausfallzeit ist akzeptabel

Für die Prüfung reicht es, so zu verstehen:

- `RPO` = wie viel können wir verlieren
- `RTO` = in welcher Zeit muss es wieder laufen

### 3. Wie oft soll gesichert werden?

Das hängt ab von:

- der Wichtigkeit der Daten
- der Häufigkeit der Änderungen
- dem akzeptablen Datenverlust

## Wie sieht ein guter Backup-Plan aus?

Er enthält:

- die zu sichernden Systeme und Daten
- den Sicherungszeitplan
- den verwendeten Sicherungstyp
- den Speicherort
- Verschlüsselungs- und Zugriffsregeln
- die Aufbewahrungsdauer
- den Restore-Prozess
- die verantwortlichen Personen

## Warum ist ein Restore-Test nötig?

Weil ein nicht getestetes Backup leicht nur Scheinsicherheit sein kann.

Getestet werden muss:

- ob es wiederherstellbar ist
- ob es unbeschädigt ist
- ob die Wiederherstellung schnell genug ist

## Warum sollte es auch eine getrennt aufbewahrte Sicherung geben?

Wenn die Sicherung immer am selben Ort wie die Originaldaten liegt:

- Feuer
- Diebstahl
- Ransomware
- Hardwareausfall

können beides gleichzeitig zerstören.

Daher ist wichtig:

- getrennte Aufbewahrung
- möglichst eine Offline- oder isolierte Kopie

## Prüfungstaugliche Formulierung

> Die Grundlage einer sicheren Backup-Planung ist die Festlegung, was gesichert werden muss, wie oft, mit welcher Zielzeit die Wiederherstellung erfolgen soll, wo die Sicherungen aufbewahrt werden und wie die Wiederherstellbarkeit überprüft wird.  
> Ein guter Backup-Plan enthält den Sicherungszeitplan, die Verantwortlichkeiten, die Aufbewahrungsdauer, die Zugriffsregeln und die Restore-Tests.  
> Die Sicherungen müssen auch getrennt vom Originalsystem verfügbar sein.

## Häufige Prüfungsfehler

- Statt eines Backup-Plans nur ein einzelnes Tool oder Programm erwähnen.
- Den Restore-Test weglassen.
- Nicht zwischen kritischen und weniger kritischen Daten unterscheiden.
- Die RPO/RTO-Logik nicht erwähnen.
- Die Sicherung am selben Ort wie das Originalsystem aufbewahren.

## Schnelle Selbstkontrolle

1. Was sind die zwei wichtigsten geschäftlichen Fragen beim Backup?
2. Was bedeutet RPO?
3. Was bedeutet RTO?
4. Warum ist ein Restore-Test nötig?
5. Warum ist eine getrennte Aufbewahrung der Sicherung sinnvoll?

## Kurzantworten zur Selbstkontrolle

1. Was sichern wir, und wie schnell muss wiederhergestellt werden
2. Wie viel Datenverlust ist akzeptabel
3. Wie viel Ausfallzeit ist akzeptabel
4. Damit die Wiederherstellung sicher funktioniert
5. Weil ein lokaler Vorfall oder Ransomware nicht alles gleichzeitig zerstört

## Quellen

1. CISA - Back Up Business Data  
   https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data  
   Verwendung: moderne, offizielle Backup-Planungsquelle, mit separater Erwähnung von RPO/RTO und Recovery-Test.

2. BSI - Datensicherung - wie geht das?  
   https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datensicherung-und-Datenverlust/Datensicherung-wie-geht-das/datensicherung-wie-geht-das.html  
   Verwendung: verständliche Zusammenfassung von Backup-Logik und Sicherungsmethoden.

3. BSI - CON.3 Datensicherungskonzept (Edition 2023)  
   https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3  
   Verwendung: primäre, strukturierte Quelle für die sichere Backup-Planung.

Abgerufen: `2026-04-08`
