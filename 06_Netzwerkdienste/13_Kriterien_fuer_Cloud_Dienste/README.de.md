# Kriterien fuer Cloud Dienste

## Schneller visueller Überblick

| Aspekt | Warum wichtig? |
|---|---|
| Security | Schutz der Daten und Systeme |
| SLA / Availability | wie verfügbar der Dienst ist |
| Data Location | wo die Daten liegen |
| Costs | wie und zu welchem Preis abgerechnet wird |
| Lock-in | wie schwer es ist, später zu wechseln |

## Welche Hauptaspekte sollte man betrachten?

### 1. Sicherheit

Fragen:

- wie die Daten geschützt werden
- ob Verschlüsselung vorhanden ist
- welche Berechtigungsverwaltung verfügbar ist

### 2. Datenschutz und Compliance

Fragen:

- ob es den rechtlichen Anforderungen entspricht
- wo die Daten gespeichert werden
- welche vertraglichen und datenschutzrechtlichen Bedingungen gelten

### 3. Verfügbarkeit

Fragen:

- ob ein SLA vorhanden ist
- welches Ausfallrisiko besteht
- welche Redundanz- und Backup-Möglichkeiten verfügbar sind

### 4. Kosten

Fragen:

- nutzungsbasiert oder mit Festpreis
- welche Zusatzkosten anfallen
- wie der Preis skaliert

### 5. Leistung und Skalierung

Fragen:

- ob es die Last bewältigt
- wie schnell skaliert werden kann
- ob eine geeignete Region nahe den Benutzern vorhanden ist

### 6. Integration und Portabilität

Fragen:

- ob es gut an bestehende Systeme angebunden werden kann
- wie einfach die Migration ist
- wie groß das Vendor-Lock-in-Risiko ist

## Was ist Shared Responsibility?

Ein wichtiges Cloud-Grundprinzip:

- Sicherheit ist nicht nur Sache des Dienstleisters

Die Verantwortung teilt sich zwischen Dienstleister und Kunde auf.

Das kann je nach Modell variieren:

- bei IaaS verbleibt mehr beim Kunden
- bei SaaS übernimmt der Dienstleister mehr Aufgaben

## Prüfungstaugliche Formulierung

> Bei der Auswahl eines Cloud-Dienstes muss man nicht nur Funktionalität und Preis betrachten,
> sondern auch Sicherheit, Compliance, Datenstandort, Verfügbarkeit,
> Kostenmodell, Skalierbarkeit und das Vendor-Lock-in-Risiko.  
> Darüber hinaus ist es wichtig, das Shared-Responsibility-Modell zu verstehen,
> also dass sich die Sicherheitsverantwortung
> zwischen Dienstleister und Kunde aufteilt.

## Häufige Prüfungsfehler

- Nur aufgrund des Preises entscheiden.
- Glauben, dass in der Cloud alle Sicherheitsaufgaben beim Dienstleister liegen.
- Datenstandort und Compliance nicht erwähnen.
- Das Vendor-Lock-in-Problem vergessen.

## Schnelle Selbstkontrolle

1. Nenne mindestens fünf Auswahlkriterien für Cloud-Dienste.
2. Warum ist der Datenstandort wichtig?
3. Was ist ein SLA?
4. Was ist Vendor Lock-in?
5. Was bedeutet Shared Responsibility?

## Kurzantworten zur Selbstkontrolle

1. Zum Beispiel Sicherheit, Datenschutz, SLA, Kosten, Skalierbarkeit
2. Weil es rechtliche, datenschutzrechtliche und leistungsbezogene Auswirkungen haben kann
3. Service Level Agreement - Dienstleistungsvereinbarung
4. Schwieriger oder teurer Wechsel zu einem anderen Anbieter
5. Die Verantwortung teilt sich zwischen Dienstleister und Kunde auf

## Quellen

1. NIST SP 800-146 - Cloud Computing Synopsis and Recommendations  
   https://csrc.nist.gov/pubs/sp/800/146/final  
   Verwendung: offizielle, strukturierte Quelle für Cloud-Auswahl- und Risikoaspekte.

2. NIST SP 800-145 - The NIST Definition of Cloud Computing  
   https://csrc.nist.gov/pubs/sp/800/145/final  
   Verwendung: offizielle Definition der Grundmodelle und des Dienstcharakters.

3. AWS - Shared Responsibility Model  
   https://aws.amazon.com/compliance/shared-responsibility-model/  
   Verwendung: praktische, moderne Veranschaulichung der geteilten Verantwortung.

4. Google Cloud - Global Locations  
   https://cloud.google.com/about/locations  
   Verwendung: für praktische Aspekte zu Datenstandort, Region und geografischer Platzierung.

5. Microsoft - Service Level Agreements (SLA) for Online Services  
   https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services?lang=1  
   Verwendung: offizielles Beispiel für Verfügbarkeit und SLA-Aspekte.

Abgerufen: `2026-04-08`
