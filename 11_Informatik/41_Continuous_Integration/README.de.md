# Continuous Integration

## Schneller visueller Überblick

| Schritt | Was passiert? |
|---|---|
| Commit / PR | neuer Code kommt an |
| Pipeline startet | automatische Prüfung läuft |
| Build + Test | es wird klar, ob es funktioniert |
| Feedback | Fehler werden schnell sichtbar |

## Was ist das Ziel von CI?

- Integrationsfehler so früh wie möglich erkennen
- verhindern, dass viele separate Entwicklungen erst spät zusammenstoßen
- Grundprüfungen automatisieren

## Typische CI-Aufgaben

- Build
- Unit Test
- Lint
- statische Prüfung
- Paketierung

## Warum ist das gut?

- schnellere Fehlererkennung
- stabilerer gemeinsamer Code
- weniger "bei mir funktioniert es"-Probleme
- einfachere Teamarbeit

## CI und CD: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| CI | regelmäßige Integration von Code und automatische Prüfung |
| CD | weitere Automatisierung der Auslieferung oder Installation |

## Worauf muss man achten?

- CI ist nicht nur automatischer Build.
- Die Tests müssen schnell und zuverlässig sein.
- Die Pipeline ist dann nützlich, wenn sie fehlerhaften Code tatsächlich stoppt.
- Es empfiehlt sich, obligatorische Prüfungen vor dem Merge zu verwenden.

## Prüfungstaugliche Formulierung

> Ziel von Continuous Integration ist, dass die Entwickler ihren Code häufig in das gemeinsame System integrieren und die Integration von automatischen Prüfungen begleitet wird.
> Dabei laufen typischerweise Build, Test und andere Codequalitätsprüfungen ab.
> Der größte Vorteil von CI ist, dass Integrationsfehler schnell erkannt werden und das Projekt dadurch stabiler bleibt.

## Häufige Prüfungsfehler

- CI mit Deployment verwechseln.
- Automatische Tests nicht erwähnen.
- Denken, dass CI nur für große Projekte nötig ist.
- Die Rolle des schnellen Feedbacks weglassen.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche von CI?
2. Welche Schritte laufen typischerweise in der CI?
3. Warum ist es bei Teamarbeit nützlich?
4. Was ist der Unterschied zwischen CI und CD?
5. Warum ist schnelles Feedback wichtig?

## Kurzantworten zur Selbstkontrolle

1. Häufige Integration und automatische Prüfung
2. Build, Test, Lint
3. Weil Zusammenstöße früh erkannt werden
4. CI prüft, CD treibt die Auslieferung/Installation weiter
5. Weil es günstiger ist, früh zu korrigieren

## Quellen

1. GitHub Docs - About continuous integration
   https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration
   Verwendung: offizielle, moderne Beschreibung des CI-Konzepts.

2. GitHub Docs - Understanding GitHub Actions
   https://docs.github.com/en/actions/get-started/understand-github-actions
   Verwendung: praktisches Beispiel, wie eine CI-Pipeline mit modernen Werkzeugen umgesetzt wird.

3. GitLab Docs - CI/CD
   https://docs.gitlab.com/ee/ci/
   Verwendung: weitere große offizielle CI/CD-Plattform als anschauliche Quelle.

Abgerufen: `2026-04-08`
