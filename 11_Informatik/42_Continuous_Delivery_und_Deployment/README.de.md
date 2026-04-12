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
- installiert das System die neue Version automatisch in der Zielumgebung

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

## Prüfungstaugliche Formulierung

> Continuous Delivery bedeutet, dass die Software kontinuierlich in einem auslieferbaren Zustand gehalten wird, aber vor der endgültigen Produktivstellung noch eine manuelle Freigabe möglich ist.
> Continuous Deployment geht einen Schritt weiter: wenn alle Bedingungen der Pipeline erfüllt sind, wird die neue Version automatisch installiert.
> Der Hauptunterschied zwischen den beiden Begriffen ist also, dass bei Deployment auch die Produktivstellung automatisiert ist.

## Häufige Prüfungsfehler

- Delivery und Deployment gleichsetzen.
- Die Möglichkeit der manuellen Freigabe bei Delivery nicht erwähnen.
- Glauben, dass ohne Automatisierung derselbe Begriff gilt.
- Nicht über die Wichtigkeit von Tests und Rollback sprechen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von Continuous Delivery?
2. Was ist das Wesentliche von Continuous Deployment?
3. Was ist der Hauptunterschied zwischen ihnen?
4. Warum ist gute Testabdeckung wichtig?
5. Warum braucht man einen Rollback-Plan?

## Kurzantworten zur Selbstkontrolle

1. Die Software wird immer in einem auslieferbaren Zustand gehalten
2. Es installiert auch automatisch
3. Deployment automatisiert auch die Produktivstellung
4. Weil sonst eine fehlerhafte Version weitergehen kann
5. Damit man im Fehlerfall schnell zurückkehren kann

## Quellen

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
