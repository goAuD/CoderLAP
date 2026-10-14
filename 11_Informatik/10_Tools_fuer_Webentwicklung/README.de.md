# Tools fuer Webentwicklung

## Schneller visueller Überblick

| Werkzeuggruppe | Wofür? | Beispiel |
|---|---|---|
| Editor / IDE | Code schreiben | VS Code |
| Browser DevTools | DOM, CSS, Netzwerk debuggen | Chrome DevTools |
| Versionskontrolle | Änderungen nachverfolgen | Git |
| Package Manager | Pakete installieren | npm |
| Lokale Laufzeit / Server | lokale Ausführung | Node.js, PHP, XAMPP, Laragon |
| Code-Qualitätstools | Einheitlichkeit, Fehler | ESLint, Prettier |

## Warum braucht man verschiedene Werkzeuge?

Weil Webentwicklung nicht nur aus Code-Schreiben besteht.

Typischer Workflow:

1. Code schreiben
2. lokal ausführen
3. im Browser prüfen
4. Fehler suchen
5. Versionen verfolgen
6. Pakete verwalten
7. Build oder Deployment vorbereiten

## Wichtige Werkzeugtypen

### 1. Code-Editor oder IDE

Aufgabe:

- Code schreiben
- Syntaxhervorhebung
- Dateiverwaltung
- Erweiterungen
- Fehleranzeigen

### 2. Browser-Entwicklerwerkzeuge

Aufgabe:

- HTML und DOM prüfen
- CSS-Regeln untersuchen
- JavaScript-Fehler beobachten
- Netzwerkanfragen analysieren
- Leistung überwachen

### 3. Versionskontrolle

Aufgabe:

- Änderungen nachverfolgen
- Wiederherstellbarkeit
- Unterstützung der Teamarbeit

### 4. Paketmanager

Aufgabe:

- Abhängigkeiten installieren
- Skripte ausführen
- Projektumgebung vereinheitlichen

### 5. Code-Qualitätswerkzeuge

Aufgabe:

- Fehler frühzeitig erkennen
- einheitliche Formatierung
- bessere Lesbarkeit

## Welches Werkzeug wofür in der Praxis?

| Situation | Nützliches Werkzeug |
|---|---|
| etwas wird nicht richtig angezeigt | DevTools |
| etwas ging nach einer Änderung kaputt | Git |
| eine Library fehlt | npm oder anderer Package Manager |
| der Code ist unordentlich | Formatter, Linter |
| lokal ausprobieren | lokaler Server / Laufzeit |

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Editor | hauptsächlich zum Bearbeiten dienendes Werkzeug |
| IDE | komplexere Entwicklungsumgebung |
| DevTools | in den Browser eingebaute Debugging-Werkzeuge |
| Git | Versionskontrollsystem |
| npm | JavaScript-Paketmanager und Sammlung von Ausführungstools |

## Worauf muss man achten?

- Ein Werkzeug ersetzt nicht gutes Verständnis.
- Zu viele Plugins oder Tools können unnötige Komplexität hinzufügen.
- Im Team braucht man eine einheitliche Toolchain.
- Versionskontrolle darf nicht weggelassen werden.

## Einen Fehler mit passenden Werkzeugen verfolgen

Angenommen, HTML erscheint, aber die Formatierung fehlt. Statt CSS auf Verdacht
zu ändern, suchen wir Belege:

1. In **Network** der DevTools laden wir die Seite neu. Eine `404`-Antwort auf
   die CSS-Anfrage deutet auf einen falschen Pfad oder eine fehlende Datei hin.
2. Ist die Datei angekommen, zeigt **Elements/Styles**, ob der Selektor passt
   und welche Regel ihn überstimmt. **Computed** zeigt den endgültigen Wert.
3. Die **Console** kann JavaScript-Laufzeitfehler melden. Eine leere Fehlerliste
   beweist aber weder ein korrektes Layout noch korrekte Geschäftslogik.
4. Eine in den DevTools erprobte Änderung wird in die Quelldatei übernommen.
   Eine vorübergehende Browseränderung geht normalerweise beim Neuladen verloren.

Ein Formatter vereinheitlicht die Form, ein Linter prüft Regeln, eine
Typprüfung untersucht Typverträge und ein Test überprüft konkretes Verhalten.
Die Werkzeuge ergänzen einander. Der Versionskontroll-Diff zeigt außerdem,
welche Änderung die Aufgabe tatsächlich gelöst hat.

In Node-Projekten unterstützen ein festgelegtes Lockfile und eine abgestimmte
Node-Version eine vergleichbare Umgebung. `npm ci` installiert Abhängigkeiten
sauber gemäß Lockfile und baut ein vorhandenes `node_modules` neu auf. Es ist
deshalb kein allgemeiner Reparaturbefehl für beliebige Browserfehler.

## Prüfungstaugliche Formulierung

> Für die Webentwicklung werden verschiedene Werkzeuge benötigt:
> ein Code-Editor zum Entwickeln,
> in den Browser eingebaute DevTools zum Debuggen,
> ein Versionskontrollsystem zum Nachverfolgen von Änderungen,
> ein Paketmanager zur Verwaltung von Abhängigkeiten
> sowie eine lokale Laufzeitumgebung
> und Code-Qualitätswerkzeuge für einen stabilen Workflow.

## Schnelle Selbstkontrolle

1. Wofür sind Browser-DevTools gut?
2. Warum ist Git wichtig?
3. Wofür ist ein Package Manager da?
4. Warum braucht man eine lokale Laufzeitumgebung?
5. Welche Rolle spielen Linter und Formatter?

## Kurzantworten zur Selbstkontrolle

1. Zum Debuggen und Analysieren
2. Zum Nachverfolgen von Änderungen und für Teamarbeit
3. Zur Verwaltung von Abhängigkeiten
4. Damit während der Entwicklung getestet werden kann
5. Sie sorgen für einheitlicheren und saubereren Code

## Quellen

Geprüft: `2026-10-14`.

- [Chrome: JavaScript debugging](https://developer.chrome.com/docs/devtools/javascript): beleggestützte Fehlersuche im Browser.
- [npm: npm ci](https://docs.npmjs.com/cli/commands/npm-ci/): Lockfile und saubere Installation.


1. Chrome for Developers - DevTools  
   https://developer.chrome.com/docs/devtools  
   Verwendung: offizielle Quelle zur Rolle der Browser-Entwicklerwerkzeuge.

2. Visual Studio Code - Documentation  
   https://code.visualstudio.com/docs  
   Verwendung: offizielle Werkzeugdokumentation zur Rolle des Editors/der IDE.

3. Git - Reference manual  
   https://git-scm.com/doc  
   Verwendung: offizielle Quelle zur Werkzeugseite der Versionskontrolle.

4. npm Docs  
   https://docs.npmjs.com/  
   Verwendung: offizielle Quelle zum Thema Paketverwaltung und Projektabhängigkeiten.

Abgerufen: `2026-04-08`
