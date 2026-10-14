# IaaS PaaS SaaS

## Schneller visueller Überblick

| Modell | Was bekommt man? | Wofür hat man mehr eigene Verantwortung? |
|---|---|---|
| IaaS | VM, Netzwerk, Speicher | Gast-OS, Anwendung, Daten, Berechtigungen |
| PaaS | Laufzeitplattform | Anwendungscode, Abhängigkeiten, Daten, Berechtigungen |
| SaaS | fertige Anwendung | Konten, Freigaben, Daten- und Aufbewahrungseinstellungen |

## Was ist IaaS?

`Infrastructure as a Service` bedeutet, dass der Dienstleister grundlegende Infrastruktur bereitstellt:

- virtuelle Maschine
- Netzwerk
- Speicherplatz

Der Kunde muss in der Regel mehr selbst verwalten, zum Beispiel:

- Betriebssystem
- Anwendung
- Konfiguration

## Was ist PaaS?

Bei `Platform as a Service` stellt der Dienstleister eine höherstufige Umgebung bereit.

Zum Beispiel:

- Anwendungsplattform
- Datenbankplattform
- Entwicklerplattform

Dabei kümmert sich der Kunde weniger um die Grundinfrastruktur.

## Was ist SaaS?

`Software as a Service` bedeutet fertige Anwendung.

Zum Beispiel:

- Online-E-Mail
- Online-Office-Paket
- Cloud-Projektmanagement-Tool

Hier nutzt der Benutzer typischerweise:

- die fertige Software und verwaltet eigene Konten, Daten und Freigaben

## Warum ist das wichtig?

Weil sich unterscheiden:

- die Betriebsverantwortung
- die Konfigurationstiefe
- die Flexibilität
- das Maß an Kontrolle

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| IaaS / PaaS / SaaS | Servicemodelle |
| Private / Public / Hybrid | Deployment-Modelle |

## Durchgearbeitetes Beispiel: dieselbe Verwaltungsaufgabe

**IaaS:** Wir erhalten eine virtuelle Maschine und installieren OS und Anwendung. Updates des Gastbetriebssystems gehören zu unseren Aufgaben. **PaaS:** Der Anbieter betreibt wesentliche Teile der Laufzeitumgebung, wir stellen Anwendungscode bereit und konfigurieren Zugriffe. **SaaS:** Wir arbeiten mit einer fertigen Verwaltungsanwendung und haben üblicherweise weniger Freiheit für eigene Funktionen.

In allen drei Fällen entscheiden wir, wer auf unsere Daten zugreifen darf. Eine irrtümliche Freigabe für alle wird nicht dadurch richtig, dass der Anbieter die Server wartet.

Die Tabelle zeigt typische Zuständigkeiten. Der konkrete Vertrag muss klären, wer sichert, bis zu welchem Zeitpunkt wiederhergestellt werden kann, wer einzelne Abhängigkeiten aktualisiert und wie Daten exportiert werden. Das Servicemodell ist eine andere Einteilungsachse als Private/Public.

## Prüfungstaugliche Formulierung

> IaaS, PaaS und SaaS sind die Servicemodelle der Cloud.  
> Bei IaaS stellt der Dienstleister hauptsächlich Infrastruktur bereit,
> bei PaaS bietet er eine Plattform zum Betrieb von Anwendungen,
> und bei SaaS nutzt der Benutzer fertige Software.  
> Je höherstufig der Dienst, desto weniger technische Betriebsaufgaben verbleiben in der Regel beim Kunden.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von IaaS?
2. Was ist PaaS?
3. Was ist SaaS?
4. Bei welchem erhält der Benutzer eine fertige Anwendung?
5. Bei welchem verbleiben mehr eigene Betriebsaufgaben: IaaS oder SaaS?

## Kurzantworten zur Selbstkontrolle

1. Infrastruktur als Dienst
2. Plattform als Dienst
3. Software als Dienst
4. Bei SaaS
5. Bei IaaS

## Quellen

1. NIST SP 800-145 - The NIST Definition of Cloud Computing  
   https://csrc.nist.gov/pubs/sp/800/145/final  
   Verwendung: primäre Definitionen von IaaS, PaaS und SaaS.

2. AWS - What is Cloud Computing?  
   https://aws.amazon.com/what-is-cloud-computing/  
   Verwendung: praktische Beispiele und moderne Interpretation eines Dienstleisters.

3. AWS - Shared Responsibility Model  
   https://aws.amazon.com/compliance/shared-responsibility-model/  
   Verwendung: veranschaulicht gut, wie sich die Verantwortung mit der Abstraktionsebene des Dienstes ändert.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [Microsoft: Shared responsibility](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility): konkrete Zuständigkeiten bei IaaS/PaaS/SaaS.

Geprüft: `2026-10-14`.
