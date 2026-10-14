# Continuous Integration

## Schneller visueller Überblick

| Schritt | Was passiert? |
|---|---|
| Commit / PR | neuer Code kommt an |
| Pipeline startet | automatische Prüfung läuft |
| Build + Test | Feedback zu Build und geprüftem Verhalten |
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

## Der Weg einer Änderung in den gemeinsamen Code

**Beispiel:** Eine Person ändert die Punkteberechnung, eine andere die
Ergebnisansicht. Beide Branches können für sich funktionieren und trotzdem
unterschiedliche Datenfelder erwarten. Häufiges Integrieren und ein Test beider
Teile zeigen diese Abweichung früh. Tägliche automatische Builds wochenlang
getrennter Branches lösen das Integrationsproblem allein nicht.

Für ein **beispielhaftes Node-Projekt**, dessen `package.json` bereits die
Scripte `lint`, `test` und `build` enthält, könnte CI so ablaufen:

```text
1. sauberer Checkout des geprüften Commits
2. festgelegte Node-Version einrichten
3. npm ci
4. npm run lint
5. npm test
6. npm run build
7. Testergebnisse und Build-Artefakt aufbewahren
```

`npm ci` installiert aus einem vorhandenen Lockfile und schreibt bei Abweichungen
nicht still die Abhängigkeitsliste um. Das verbessert die Wiederholbarkeit;
Plattform, Laufzeit und externe Dienste müssen trotzdem festgelegt oder geprüft
werden. Die Scripte gehören hier zu einem Lernbeispiel und passen nicht
automatisch zu jedem Repository.

| Ereignis | Passender nächster Schritt |
|---|---|
| erwartetes Datenfeld fehlt im Test | Prüfung schlägt fehl, der getestete Code muss korrigiert und erneut geprüft werden |
| neuer Commit kommt in den PR | neuer Inhalt muss geprüft werden |
| Zielbranch ändert sich inzwischen | Zusammenspiel mit dem aktuellen Zielzustand prüfen |
| Test ist gelegentlich ohne klare Ursache rot | Ursache untersuchen; erneutes Starten allein ist keine Korrektur |

Ein Cache beschleunigt, ersetzt aber keine korrekten Abhängigkeiten oder Tests.
Das Ergebnis belegt nur tatsächlich ausgeführte Prüfungen. Ein Exitcode, der
Fehler sichtbar hält, und verpflichtende Merge-Prüfungen verbinden das Feedback
mit dem Arbeitsablauf des Teams.

## Prüfungstaugliche Formulierung

> Ziel von Continuous Integration ist,
> dass die Entwickler ihren Code häufig in das gemeinsame System integrieren
> und die Integration von automatischen Prüfungen begleitet wird.
> Dabei laufen typischerweise Build, Test und andere Codequalitätsprüfungen ab.
> Der größte Vorteil von CI ist, dass Integrationsfehler schnell erkannt werden und das Projekt dadurch stabiler bleibt.

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

Geprüft: `2026-10-14`.

- [GitHub: Continuous integration](https://docs.github.com/en/actions/get-started/continuous-integration): Häufige Integration und automatisiertes Feedback.
- [npm: npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/): Lockfile-basierte Installation und Umgang mit Abweichungen.


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
