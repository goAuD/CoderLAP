# Automatisierung von Tests

## Schneller visueller Überblick

| Vorteil | Einschränkung |
|---|---|
| schnelle Wiederholung | anfängliche Einführungskosten |
| häufiger Regressionstest | muss gewartet werden |
| in CI integrierbar | bei schlechter Planung instabil möglich |

## Was ist Testautomatisierung?

Bei der Testautomatisierung führen:

- Skripte
- Testframeworks
- CI-Systeme

die Tests durch und oft auch die Auswertung der Ergebnisse.

## Warum ist sie nützlich?

- derselbe Test kann schnell erneut ausgeführt werden
- sehr gut für Regressionstests
- reduziert manuelle, wiederkehrende Arbeit
- lässt sich leicht in einen `CI`-Prozess einbinden

## Was sollte automatisiert werden?

Typischerweise:

- häufig wiederholte Tests
- stabile Funktionen
- Regressionsprüfungen
- Grundprüfungen nach dem Build

## Was lohnt sich eventuell nicht zu automatisieren?

- sehr schnell ändernde UI anfangs
- einmalige oder seltene Prüfungen
- Tests, die stark auf menschliche Beurteilung angewiesen sind

## Risiken

- die Tests selbst können fehlerhaft sein
- sie haben Wartungskosten
- bei schlechter Isolation können flaky Tests entstehen
- sie können ein falsches Sicherheitsgefühl geben, wenn keine gute Teststrategie vorhanden ist

## Testautomatisierung und vollständige Qualitätssicherung: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Testautomatisierung | maschinelle Durchführung bestimmter Tests |
| Qualitätssicherung | breiterer Prozess mit mehreren Elementen |

## Typische Werkzeuge und Umgebungen

- Unit-Test-Frameworks
- browserbasierte Testautomatisierung
- `CI`-Systeme
- Reporting-Werkzeuge

## Prüfungstaugliche Formulierung

> Bei der Testautomatisierung werden bestimmte Tests automatisch durch Werkzeuge und Skripte ausgeführt.  
> Dies ist besonders nützlich bei wiederkehrenden, Regressions- oder in `CI` integrierbaren Tests, da es eine schnellere und häufiger durchführbare Prüfung ermöglicht.  
> Allerdings lässt sich nicht jeder Test sinnvoll automatisieren, und auch die Wartung automatisierter Tests erfordert Ressourcen.

## Häufige Prüfungsfehler

- Behaupten, dass alle Tests automatisiert werden müssen.
- Die Wartungskosten nicht erwähnen.
- Testautomatisierung mit dem gesamten QA gleichsetzen.
- Den Zusammenhang mit `CI` auslassen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche der Testautomatisierung?
2. Welche Tests eignen sich besonders dafür?
3. Was ist ein Hauptvorteil?
4. Was ist ein Hauptnachteil?
5. Warum ist der Zusammenhang mit `CI` wichtig?

## Kurzantworten zur Selbstkontrolle

1. Automatische Durchführung von Tests mit Werkzeugen
2. Häufig wiederholte und Regressionstests
3. Schnelle Wiederholung
4. Wartungskosten
5. Weil so bei jeder Änderung der Code automatisch geprüft werden kann

## Quellen

1. Selenium - Overview of Test Automation  
   https://www.selenium.dev/documentation/test_practices/overview/  
   Verwendung: offizielle, moderne Quelle zu Zweck, Vorteilen und Einschränkungen der Testautomatisierung.

2. GitHub Docs - About continuous integration with GitHub Actions  
   https://docs.github.com/en/actions/about-github-actions/about-continuous-integration-with-github-actions  
   Verwendung: offizielle Quelle dazu, wie sich Testautomatisierung in den `CI`-Prozess einfügt.

3. ISTQB CTFL Overview  
   https://test.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/  
   Verwendung: offizieller Hintergrund zu Vorteilen und Risiken der Testautomatisierung aus Testsicht.

Abgerufen: `2026-04-09`
