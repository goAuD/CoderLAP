# Continuous Delivery und Deployment

## Schneller visueller Überblick

| Stufe | Wie weit ist es automatisch? |
|---|---|
| CI | Build und Test |
| Continuous Delivery | Build, Test, Paketierung, auslieferbarer Zustand |
| Continuous Deployment | nach Build und Test auch automatische Installation |

## Was ist Continuous Delivery?

Wesentlich:

- die Software ist kontinuierlich in einem Zustand, in dem sie ausgeliefert werden kann
- vor der Produktivstellung bleibt häufig ein kontrollierter, manueller Entscheidungspunkt

## Was ist Continuous Deployment?

Wesentlich:

- wenn die Pipeline-Bedingungen erfüllt sind
- installiert das System die neue Version automatisch in der Produktionsumgebung

Das erfordert hohe Automatisierung und großes Vertrauen in die Tests.

## Warum ist der Unterschied wichtig?

Weil in der Prüfung häufig genau das gefragt wird:

- Delivery = "immer auslieferbar"
- Deployment = "wird auch automatisch ausgeliefert"

## Vorteile

- schnellere Auslieferung
- Änderungen in kleineren Paketen
- weniger manuelle Fehler
- schnellerer Feedback-Zyklus

## Risiken

- bei schwacher Testabdeckung gefährlich
- bei schlechter Pipeline kann auch eine fehlerhafte Version durchgehen
- Rollback und Monitoring sind nötig

## Dieselbe Version vom Test in die Produktion bringen

**Beispiel:** Ein Paket `quiz-1.4.0` entsteht aus einem bekannten Commit. Die
Testumgebung erhält dieses Paket. Bei der Auslieferung wird dasselbe geprüfte
Artefakt produktiv installiert, nicht zufällig eine neu gebaute Variante mit
inzwischen veränderten Abhängigkeiten.

```text
Commit -> Build -> Tests -> versioniertes Artefakt -> Staging
  -> Prüfung -> [menschliche Freigabe] -> Produktion
```

Das kann **Continuous Delivery** sein: Die Installation ist automatisiert und
wiederholbar, über den produktiven Einsatzzeitpunkt entscheidet ein Mensch.
Bei **Continuous Deployment** entfällt nach den automatischen Prüfungen auch
diese menschliche Freigabestufe. Automatisches Deployment nach Staging allein
bedeutet noch keine automatische Produktivstellung.

| Begriff | In diesem Beispiel |
|---|---|
| Build | das Artefakt entsteht |
| Deployment | das Artefakt wird in der Zielumgebung installiert |
| Release | die Funktion wird für Benutzer verfügbar |
| Rollback | Wechsel auf eine vorherige funktionierende Version, soweit der Systemzustand es erlaubt |

Deployment und Release können durch Feature Flags getrennt werden: Code ist
bereits installiert, eine Funktion aber noch deaktiviert. Konfiguration und
Geheimnisse werden je Umgebung verwaltet, nicht in das an Clients gelieferte
Paket eingebaut.

Nach dem Deployment prüfen wir die wichtigsten Abläufe und beobachten
Fehlersignale. Eine gelöschte Datenbankspalte kommt durch Zurückkopieren der
alten Anwendung nicht zurück. Dafür braucht es vorausgeplante kompatible
Migrationen, erprobte Sicherungen und gegebenenfalls eine korrigierende neue
Version. Ein Rollbackplan berücksichtigt deshalb neben dem Code auch Daten
und Konfiguration.

## Prüfungstaugliche Formulierung

> Continuous Delivery bedeutet,
> dass die Software kontinuierlich in einem auslieferbaren Zustand gehalten wird,
> aber vor der endgültigen Produktivstellung
> noch eine manuelle Freigabe möglich ist.
> Continuous Deployment geht einen Schritt weiter:
> wenn alle Bedingungen der Pipeline erfüllt sind,
> wird die neue Version automatisch installiert.
> Der Hauptunterschied liegt in der menschlichen Freigabe: Bei Continuous Deployment folgt nach erfolgreichen automatischen Prüfungen keine separate manuelle Produktivfreigabe. Die technischen Installationsschritte können auch bei Continuous Delivery automatisiert sein.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Continuous Delivery?
2. Was ist das Wesentliche von Continuous Deployment?
3. Was ist der Hauptunterschied zwischen ihnen?
4. Warum ist gute Testabdeckung wichtig?
5. Warum braucht man einen Rollback-Plan?

## Kurzantworten zur Selbstkontrolle

1. Die Software wird immer in einem auslieferbaren Zustand gehalten
2. Es installiert auch automatisch
3. Bei Continuous Deployment folgt nach automatischen Prüfungen keine menschliche Produktivfreigabe je Version
4. Weil sonst eine fehlerhafte Version weitergehen kann
5. Damit man im Fehlerfall schnell zurückkehren kann

## Quellen

Geprüft: `2026-10-14`.

- [Microsoft: Continuous delivery](https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery): Auslieferbarer Zustand, Umgebungen und automatisierter Ablauf.
- [GitHub: Reviewing deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments): Konkrete menschliche Freigabestufe.


1. GitHub Docs - Continuous deployment
   https://docs.github.com/en/actions/get-started/continuous-deployment
   Verwendung: modernes, offizielles Beispiel für Deployment-Automatisierung.

2. Reviewing deployments - GitHub Docs
   https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments
   Verwendung: offizielles Beispiel, wie ein Freigabeschritt in die Auslieferung eingefügt werden kann.

3. Microsoft Learn - DevOps concepts for continuous delivery
   https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery
   Verwendung: offizielle Zusammenfassung des Continuous-Delivery-Konzepts von Microsoft.

Abgerufen: `2026-04-08`
