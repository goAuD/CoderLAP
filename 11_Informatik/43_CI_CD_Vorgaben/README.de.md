# CI CD Vorgaben

## Schneller visueller Überblick

| Anforderung | Warum nötig? |
|---|---|
| obligatorische Tests | Filterung fehlerhaften Codes |
| geschützter Branch | kontrollierter Merge |
| Review und Approval | Qualität und Sicherheit |
| Umgebungsschutz | nicht alles geht sofort in Produktion |
| Protokollierung | Nachvollziehbarkeit |

## Typische CI/CD-Regeln

- obligatorischer Build und Test vor dem Merge
- geschützte Branches
- Required Status Checks
- obligatorisches Code Review
- Deployment Approval für bestimmte Umgebungen
- sichere Verwaltung von Secrets
- Rollback-Möglichkeit
- Versionierung und Protokollierung

## Warum sind die Regeln wichtig?

Weil Automatisierung allein nicht ausreicht.

Wenn es keine Governance gibt, dann:

- kann fehlerhafter Code durchkommen
- kann jemand direkt in Produktion Änderungen vornehmen
- gibt es keine Kontrolle oder Auditierbarkeit

## Typische Umgebungsprinzipien

| Umgebung | Typische Anforderung |
|---|---|
| Development | schnelles Testen |
| Staging | produktionsähnliche Prüfung |
| Production | starker Schutz, Freigabe, Monitoring |

## Worauf muss man achten?

- Für die Produktionsumgebung gelten strengere Regeln.
- Auch ein Pipeline-Fehler ist ein Risiko.
- Geheimnisse (`Secrets`) dürfen nicht im Code gespeichert werden.
- Auch das Zurückrollen muss geplant sein.
- Die Regeln sollen klar und konsequent eingehalten werden.

## Von konkreten Vorgaben zu überprüfbaren Nachweisen

Auch ein kleines Team kann kurze, überprüfbare Regeln haben. Das folgende
Beispiel beschreibt mögliche Vorgaben, nicht die derzeitigen Einstellungen
dieses Repositorys:

| Vorgabe | Woran lässt sich ihre Erfüllung erkennen? |
|---|---|
| Änderungen über PRs | Commit und zugehöriges Review sind nachvollziehbar |
| verpflichtender Test und Build | erfolgreiches Ergebnis gehört zur tatsächlich zusammenzuführenden Version |
| bekannte Abhängigkeits- und Werkzeugversionen | Lockfile und festgelegte Laufzeit |
| eingeschränkter Produktivzugriff | nur erlaubter Branch und Deployment-Identität haben Zugriff |
| nachvollziehbare Version | Commit, Artefakt, Zeitpunkt und Zielumgebung sind erfasst |
| geplante Wiederherstellung | Funktionsprüfung und erprobtes Wiederherstellungsverfahren |

**Auch CI führt Code aus.** Tests eines externen PR dürfen keine produktiven
Geheimnisse oder Schreibzugriff auf den Server erhalten. Nur der Deployment-
Schritt erhält die dafür nötigen minimalen Rechte. Externe GitHub Actions
lassen sich auf eine vollständige Commit-SHA festlegen. Das fixiert den Code,
ersetzt aber weder dessen Vertrauensprüfung noch spätere Updates. PR-Titel
und anderer externer Text bleiben Daten und werden nicht ungeprüft in Shellbefehle
eingesetzt.

Hinter einer grünen Prüfung muss wirkliche Arbeit stehen: Wir prüfen, ob Tests
tatsächlich liefen, durch Bedingungen übersprungen wurden oder Fehler ignoriert
wurden. Checkname, administrative Umgehungsmöglichkeiten und wirksame Regeln
bestimmen gemeinsam den Schutz. Logs enthalten notwendige Diagnosedaten,
keine Passwörter oder Tokens.

Die Vorgaben richten sich nach dem Projektrisiko. Eine statische Lernseite
und ein Zahlungsdienst brauchen nicht dieselben Deployment-Freigaben. Bei
beiden muss aber verständlich bleiben, was geprüft wurde, was ausgeliefert
wurde und wie sich ein Problem beheben lässt.

## Prüfungstaugliche Formulierung

> CI/CD-Vorgaben sind Regeln,
> die sicherstellen,
> dass der Prozess von Build, Test, Release und Deployment
> kontrolliert, sicher und nachvollziehbar abläuft.
> Dazu gehören beispielsweise obligatorische Statusprüfungen,
> geschützte Branches, Code Review, Deployment-Freigabe,
> Umgebungsschutz, sichere Verwaltung von Geheimnissen
> und Rollback-Möglichkeit.
> Diese Regeln sind deshalb wichtig, weil Automatisierung mit Kontrolle und Qualitätssicherung verbunden werden muss.

## Schnelle Selbstkontrolle

1. Was bedeuten CI/CD-Vorgaben?
2. Warum braucht man geschützte Branches?
3. Warum sind Required Status Checks wichtig?
4. Warum braucht man Deployment Approval?
5. Warum ist es gefährlich, Secrets im Code zu speichern?

## Kurzantworten zur Selbstkontrolle

1. Erwartungen, die den Pipeline-Betrieb regeln
2. Weil sie den Merge kontrollieren
3. Weil sie fehlerhaften Code blockieren können
4. Weil sie die Produktivstellung schützen
5. Weil es ein Sicherheitsrisiko ist

## Quellen

Geprüft: `2026-10-14`.

- [GitHub: Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use): Minimale Rechte, PR-Code, Geheimnisse und fixierte Action-Versionen.
- [GitHub: Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches): Verpflichtende Prüfungen und Umgehungsregeln.


1. GitHub Docs - About protected branches
   https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
   Verwendung: Branch Protection, obligatorisches Review und Status-Check-Regeln.

2. GitHub Docs - Deployments and environments
   https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
   Verwendung: Umgebungen, Environment Rules und Deployment-Schutz.

3. GitHub Docs - Reviewing deployments
   https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments
   Verwendung: Einfügen eines Freigabeprozesses vor dem Deployment.

4. GitHub Docs - About continuous integration
   https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration
   Verwendung: Grundlage der obligatorischen Prüfungslogik im CI-Teil.

Abgerufen: `2026-04-08`
