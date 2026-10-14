# Private Public Hybrid Cloud

## Schneller visueller Überblick

| Modell | Wesentliches |
|---|---|
| Private Cloud | Cloud zur ausschließlichen Nutzung durch eine Organisation |
| Public Cloud | für die allgemeine Öffentlichkeit angebotene Cloud |
| Hybrid Cloud | Private + Public gemeinsam |

## Was ist eine Private Cloud?

Eine Private Cloud ist eine Cloud-Umgebung, die:

- für die ausschließliche Nutzung durch eine Organisation bereitgestellt wird
- stärker kontrolliert wird
- häufig auf internen oder dedizierten Ressourcen aufbaut

Vorteil kann sein:

- größere Kontrolle
- Erfüllung spezieller Compliance- oder Datenschutzanforderungen

## Was ist eine Public Cloud?

Bei der Public Cloud:

- steht das Angebot der allgemeinen Öffentlichkeit mit passendem Vertrag und Konto offen
- sind die Ressourcen über das Netzwerk erreichbar
- ist der Dienst typischerweise flexibel erweiterbar

Typische Beispiele:

- AWS
- Microsoft Azure
- Google Cloud

## Was ist eine Hybrid Cloud?

Hybrid Cloud bedeutet, dass:

- eigenständige Cloud-Umgebungen, etwa Private und Public Cloud, durch Technik für Daten- oder Anwendungsportabilität verbunden werden

Zum Beispiel:

- sensible Daten bleiben in der Private-Umgebung
- die skalierende Webanwendung läuft in der Public Cloud

## Warum ist das wichtig?

Weil die Wahl des richtigen Modells abhängen kann von:

- Kosten
- Kontrollbedarf
- Datenschutz
- bestehender Infrastruktur

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Private Cloud | stärker der Organisation zugeordnete Cloud-Umgebung |
| Public Cloud | öffentliche Cloud eines Dienstleisters |
| Hybrid Cloud | Kombination mehrerer Modelle |
| On-Premises | lokal betriebenes System, nicht unbedingt Cloud |

## Eigentümer, Standort und Nutzung sind getrennte Fragen

Eine Private Cloud kann von einem externen Unternehmen in dessen Rechenzentrum betrieben werden, solange die Umgebung einer Organisation exklusiv dient. On-Premises beschreibt den Standort, Private/Public das Nutzungsmodell. Eine Public Cloud macht Kundendaten und virtuelle Maschinen nicht automatisch öffentlich zugänglich.

**Durchgearbeiteter Fall:** Eine Schule hält ihre Übungsdatenbank in einer Private Cloud und erweitert über eine kontrollierte Verbindung die Anwendungskapazität mit Public-Cloud-Ressourcen. Verbindung und portable Arbeitslast bilden hier den hybriden Betrieb. Ein lokaler Dateiserver neben einem unabhängigen SaaS-Abonnement belegt für sich noch keine Hybrid Cloud nach NIST.

NIST nennt außerdem die **Community Cloud**: Sie dient einer bestimmten Gemeinschaft von Organisationen mit gemeinsamen Anforderungen. Die drei Modelle im Titel sind somit nicht die gesamte Einteilung.

## Prüfungstaugliche Formulierung

> Private, Public und Hybrid Cloud sind die Deployment-Modelle der Cloud.  
> Die Private Cloud ist eine an eine Organisation gebundene Umgebung
> mit größerer Kontrolle,
> die Public Cloud ist ein Angebot für die allgemeine Öffentlichkeit,
> und die Hybrid Cloud ist eine Kombination davon.  
> Bei der Wahl sind Kosten, Flexibilität, Sicherheit und Compliance wichtige Aspekte.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche der Private Cloud?
2. Was ist das Wesentliche der Public Cloud?
3. Was ist eine Hybrid Cloud?
4. Ist Public/Private/Hybrid ein Deployment-Modell oder ein Servicemodell?
5. Nenne zwei Auswahlkriterien.

## Kurzantworten zur Selbstkontrolle

1. Cloud-Umgebung zur ausschließlichen Nutzung durch eine Organisation
2. für die allgemeine Öffentlichkeit angebotene Cloud
3. Technisch verbundene Kombination eigenständiger Cloud-Umgebungen
4. Deployment-Modell
5. Zum Beispiel Kosten und Compliance

## Quellen

1. NIST SP 800-145 - The NIST Definition of Cloud Computing  
   https://csrc.nist.gov/pubs/sp/800/145/final  
   Verwendung: primäre Definitionen der Deployment-Modelle (`private`, `public`, `hybrid`).

2. NIST SP 800-146 - Cloud Computing Synopsis and Recommendations  
   https://csrc.nist.gov/pubs/sp/800/146/final  
   Verwendung: praktischer Hintergrund zu Vorteilen und Risiken der Deployment-Modelle.

3. AWS - What is a Public Cloud?  
   https://aws.amazon.com/what-is/public-cloud/  
   Verwendung: verständliche, aktuelle Public-Cloud-Zusammenfassung.

4. AWS - What is Hybrid Cloud?  
   https://aws.amazon.com/what-is/hybrid-cloud/  
   Verwendung: praktische Erklärung zu Hybrid-Cloud-Nutzungsmustern.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [NIST SP 800-145](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf): Cloudbegriff und Bereitstellungsmodelle.

Geprüft: `2026-10-14`.
