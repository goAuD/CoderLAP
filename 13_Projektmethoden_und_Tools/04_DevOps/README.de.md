# DevOps

## Schneller visueller Überblick

| Traditioneller Betrieb | DevOps |
|---|---|
| Entwicklung und Betrieb in getrennten Silos | engere Zusammenarbeit |
| seltenere Releases | häufigere Releases |
| mehr manuelle Schritte | mehr Automatisierung |
| langsamere Rückkopplung | schnelleres Feedback |

## Was ist DevOps?

DevOps ist nicht nur ein Werkzeug und nicht nur `CI/CD`.

Sondern zusammen:

- Kultur
- Prozesse
- Praktiken
- Werkzeuge

Ziel ist es, dass das Team Software schneller und zuverlässiger liefert.

## Hauptelemente

- Zusammenarbeit von Entwicklung und Betrieb
- automatisierter Build, Test und Release
- Versionskontrolle
- Monitoring
- schnelle Fehlermeldung und Rückkopplung

## Warum ist das wichtig?

- kürzere Release-Zyklen
- bessere Qualität
- schnellere Fehlerbehebung
- größere Transparenz
- stabilere Systeme

## DevOps und CI/CD: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| DevOps | umfassendere Kultur und Betriebsmodell |
| CI/CD | ein Teil der wichtigen DevOps-Praktiken |

## Worauf muss man achten?

- DevOps ist nicht nur eine Pipeline.
- Lässt sich nicht allein durch Werkzeuge lösen.
- Kultur und Verantwortungsteilung sind ebenfalls nötig.
- Sicherheit, Monitoring und Betreibbarkeit gehören auch dazu.

## Vom Commit zum überprüften Betrieb

Eine kleine Korrektur kann diesen Weg gehen: Code-Review, automatisierter Test, identifizierbares Release-Paket, Prüfung in der Testumgebung und Zustandsprüfung nach der Produktivsetzung. Installiert wird dasselbe bereits geprüfte Paket; geheime Konfiguration gelangt separat und zugriffsgeschützt in die Umgebung.

CI unterstützt häufiges Zusammenführen und automatisiertes Prüfen von Änderungen. Bei Continuous Delivery ist die Version auslieferbar; eine manuelle Freigabe für Produktion bleibt möglich. Bei Continuous Deployment erfolgt auch die Produktivsetzung nach erfolgreichen Prüfungen automatisch. Die Abkürzung „CD“ sollte deshalb ausgeschrieben werden.

Nach erfolgreicher Installation beobachten wir den Dienst weiter: Funktionieren Anmeldung und zentrale Benutzeraufgabe? Datenbankänderungen benötigen einen eigenen Wiederherstellungsplan, weil das Zurückspielen alten Codes Daten nicht unbedingt zurücksetzt. Entwicklung und Betrieb lernen gemeinsam aus den Ergebnissen.

## Prüfungstaugliche Formulierung

> DevOps ist ein auf Zusammenarbeit von Entwicklung und Betrieb basierender Ansatz,
> der Kultur, Prozesse, Praktiken
> und Werkzeuge gleichermaßen umfasst.  
> Ziel ist es, dass Software schneller, zuverlässiger und mit höherem Automatisierungsgrad zu den Nutzern gelangt.  
> Zu den wichtigen Elementen von DevOps gehören z. B. Versionskontrolle,
> CI/CD, Infrastrukturautomatisierung, Monitoring
> und kontinuierliche Rückkopplung.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche an DevOps?
2. Warum geht es nicht nur um Werkzeuge?
3. Was ist der Zusammenhang mit CI/CD?
4. Warum unterstützt es schnellere Lieferung?
5. Nenne vier typische DevOps-Elemente.

## Kurzantworten zur Selbstkontrolle

1. Verbindung von Entwicklung und Betrieb
2. Weil auch Kultur und Prozesse nötig sind
3. CI/CD ist ein wichtiger Teil von DevOps
4. Weil es mehr Automatisierung und schnelles Feedback bietet
5. Git, CI/CD, Monitoring, Automatisierung

## Quellen

- [Microsoft Learn: What is DevOps?](https://learn.microsoft.com/en-us/devops/what-is-devops)  
  DevOps-Praktiken, kontinuierliche Integration und Bereitstellung.

- [Microsoft: Safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)  
  Prüfung nach der Bereitstellung und geplante Wiederherstellung.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Microsoft Learn - What is DevOps?  
   https://learn.microsoft.com/en-us/devops/what-is-devops  
   Verwendung: offizielle, gut strukturierte Definition und Lebenszyklus-Ansicht.

2. AWS - DevOps and AWS  
   https://aws.amazon.com/devops/  
   Verwendung: offizielle, praxisnahe Zusammenfassung zum Zusammenhang von DevOps-Kultur, Praktiken und Automatisierung.

Abgerufen: `2026-04-08`
