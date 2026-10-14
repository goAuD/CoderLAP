# ERP-Systeme

## Schneller visueller Überblick

| ERP-Modul | Beispiel |
|---|---|
| Finanzen | Buchhaltung, Kosten |
| Beschaffung | Bestellung, Lieferant |
| Lager / Logistik | Bestandsverwaltung |
| HR | Mitarbeiterdaten |
| Produktion / Projekt | Planung, Ressourcen |

## Was ist das Wesen eines ERP?

Das Hauptziel eines `ERP` ist, dass die verschiedenen Bereiche eines Unternehmens:

- nicht isoliert voneinander arbeiten
- auf dieselben oder abgestimmte Daten zurückgreifen
- entlang transparenterer Prozesse arbeiten

## Warum ist das aus Datenbanksicht wichtig?

`ERP`-Systeme:

- verwalten viele verschiedene Geschäftsdaten
- erfordern ein integriertes Datenmodell
- nutzen starke Konsistenz- und Berechtigungsverwaltung
- basieren typischerweise auf transaktionalen Datenbanken

## Hauptvorteile

- einheitlichere Datenverwaltung
- weniger duplizierte Daten
- bessere Prozessintegration
- bessere Berichtsfähigkeit und Transparenz

## Mögliche Nachteile oder Herausforderungen

- Einführung kann komplex sein
- kann ein teures und langwieriges Projekt sein
- kann starke organisatorische Veränderung erfordern
- Anpassung und Migration können kompliziert sein

## ERP und `BIS` - nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| `BIS` | breiterer Begriff für betriebliches Informationssystem |
| `ERP` | integriertes Unternehmenssteuerungssystem |

`ERP` ist häufig einer der wichtigsten Bestandteile des `BIS`.

## Durchgearbeiteter ERP-Prozess: vom Einkauf zum Bestand

Ein Unternehmen bestellt zehn Netzwerkadapter. Der Einkauf erstellt die Bestellung anhand gemeinsamer Lieferanten- und Artikelstammdaten. Das Lager erfasst acht gelieferte Stück; zwei bleiben offen. Die Rechnung enthält zehn Stück. Der Abgleich von Bestellung, Wareneingang und Rechnung zeigt eine Abweichung. Der Prozess muss sie bearbeiten, statt einfach alle Module auf denselben Wert zu setzen.

Die gemeinsame Artikelkennung verbindet Einkauf, Bestand und Rechnungswesen. Berechtigungen bleiben dennoch unterschiedlich: Nicht jede Person im Lager darf Lieferanten-Bankdaten ändern oder Zahlungen freigeben.

Bei der Einführung werden doppelte Stammdaten bereinigt und Import, Schnittstellen sowie Schulung geplant. Ein sinnvoller Abnahmetest umfasst normale Bestellung, Teillieferung, Rückgabe und Korrektur fehlerhafter Daten. Bei Migrationen sind auch Mengen und abstimmbare Salden zu prüfen.

Ein integriertes ERP erfordert nicht zwingend eine einzige physische Datenbank. Entscheidend sind konsistente fachliche Kennungen und abgestimmte Abläufe. Fehler zwischen mehreren Systemen benötigen eindeutige Zustände, erneute Versuche und Abstimmung.

## Prüfungstaugliche Formulierung

> Ein `ERP`-System ist ein integriertes Unternehmenssteuerungssystem, das die Prozesse mehrerer Geschäftsbereiche wie  
> Finanzen, Beschaffung, Lager oder HR in einem gemeinsamen System verwaltet.  
> Ziel des `ERP` ist eine einheitliche Datenverwaltung, die Abstimmung der Prozesse und bessere Transparenz.  
> Aus Datenbanksicht basieren `ERP`-Systeme auf einer großen, integrierten und konsistent verwalteten Datenumgebung.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel eines `ERP`?
2. Welche Bereiche kann es zusammenfassen?
3. Warum ist integrierte Datenverwaltung dabei wichtig?
4. Was ist ein Vorteil?
5. Was ist eine typische Herausforderung bei der Einführung?

## Kurzantworten zur Selbstkontrolle

1. Die Integration der Unternehmensprozesse
2. Finanzen, Beschaffung, Lager, HR usw.
3. Weil die Bereiche mit denselben Daten arbeiten
4. Einheitlicherer Betrieb
5. Komplexe Einführung und Anpassung

## Quellen

1. Oracle - Enterprise Resource Planning (ERP)  
   https://www.oracle.com/erp/  
   Verwendung: offizielle, moderne Quelle zum Zweck und den typischen Modulen des ERP-Systems.

2. SAP - What is SAP Cloud ERP?  
   https://www.sap.com/products/erp.html  
   Verwendung: offizielle Quelle zur praktischen Darstellung der integrierten Unternehmensrolle von ERP.

Abgerufen: `2026-04-09`

### Geprüfte Quellen zur Ergänzung

- [SAP: What is ERP?](https://www.sap.com/resources/what-is-erp): integrierte Geschäftsbereiche und Einführungsaspekte
- [Oracle: Matching Invoice Lines](https://docs.oracle.com/en/cloud/saas/financials/25d/fappp/matching-invoice-lines.html): Abgleich von Bestellung, Wareneingang und Rechnung

Geprüft: `2026-10-14`.
