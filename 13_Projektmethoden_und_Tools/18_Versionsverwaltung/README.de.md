# Versionsverwaltung

## Schneller visueller Überblick

| Begriff | Bedeutung |
|---|---|
| Repository | der Speicherort des Projekts |
| Commit | gespeichertes Änderungspaket |
| Branch | separater Entwicklungszweig |
| Merge | Zusammenführung von Zweigen |

## Was ist Versionsverwaltung?

Ein Versionsverwaltungssystem verfolgt:

- wann eine Änderung stattgefunden hat
- wer die Änderung vorgenommen hat
- was sich geändert hat
- wie man frühere Zustände vergleichen oder wiederherstellen kann

## Warum ist das wichtig?

- grundlegend für Teamarbeit
- reduziert das Risiko verlorener Arbeit
- unterstützt die Fehlersuche
- macht das Ausprobieren neuer Entwicklungen sicherer

## Zentralisiertes und verteiltes System

| Typ | Merkmal |
|---|---|
| zentralisiert | die Hauptversion liegt auf einem zentralen Server |
| verteilt | jeder Entwickler kann eine vollständige Kopie haben |

`Git` ist ein verteiltes Versionsverwaltungssystem.

## Typische Grundoperationen

- Klonen
- Ändern
- Commit
- Branch erstellen
- Merge
- Pull / Push

## Versionsverwaltung und Backup: nicht verwechseln

| Begriff | Wozu? |
|---|---|
| Versionsverwaltung | Verfolgung von Änderungen und Zusammenarbeit |
| Backup | Sicherungskopie gegen Datenverlust |

Ein Versionsverwaltungssystem ist nützlich, aber nicht dasselbe wie eine vollständige Backup-Strategie.

## Arbeitsverzeichnis, Staging und Commit

In Git verändert sich eine bearbeitete Datei zunächst im Arbeitsverzeichnis. Die Staging Area enthält die für den nächsten Commit vorbereiteten Änderungen. Ein Commit speichert den ausgewählten Zustand in der lokalen Historie; erst ein gesonderter Push überträgt ihn in das Remote-Repository.

Diese Befehle zeigen die Unterschiede in einem bereits geöffneten Übungsrepository und ändern keine Dateien:

```bash
git status --short
git diff
git diff --staged
git log -3 --oneline
```

`git diff` zeigt noch nicht vorgemerkte Änderungen, `git diff --staged` die für den nächsten Commit vorbereitete Differenz. Wurde dieselbe Zeile auf zwei Zweigen unterschiedlich geändert, kann ein Merge-Konflikt entstehen. Dann müssen die Absichten zusammengeführt und das Ergebnis geprüft werden.

In gemeinsam genutzter Historie wird die Wirkung eines fehlerhaften Commits häufig mit einem neuen Gegen-Commit (`git revert`) aufgehoben. `.gitignore` entfernt weder bereits verfolgte Dateien noch Historie; ein versehentlich geteilter geheimer Schlüssel muss gesondert widerrufen werden.

## Prüfungstaugliche Formulierung

> Versionsverwaltung bedeutet die Nachverfolgung und Verwaltung von Änderungen an Dateien, insbesondere am Quellcode.  
> Damit lässt sich nachvollziehen, wer was und wann geändert hat,
> und es besteht die Möglichkeit, frühere Zustände wiederherzustellen
> und die Arbeit mehrerer Entwickler zu koordinieren.  
> In der modernen Softwareentwicklung ist Git eines der verbreitetsten verteilten Versionsverwaltungssysteme.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche an der Versionsverwaltung?
2. Wozu dient ein `Commit`?
3. Was ist die Rolle eines `Branch`?
4. Warum ist sie bei Teamarbeit nützlich?
5. Warum ist sie nicht dasselbe wie ein Backup?

## Kurzantworten zur Selbstkontrolle

1. Die Nachverfolgung und Verwaltung von Änderungen
2. Zum Festhalten von Änderungen
3. Zum Erstellen eines separaten Entwicklungszweigs
4. Weil sie bei der Zusammenarbeit und Konfliktlösung hilft
5. Weil sie einen anderen Zweck hat als die Datensicherung

## Quellen

- [Git: Recording changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)  
  Staging, Diff, Commit und Grenzen von Ignore-Regeln.

- [Git: git-revert](https://git-scm.com/docs/git-revert)  
  Gegen-Commit ohne Umschreiben der Historie.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Git - About Version Control  
   https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control  
   Verwendung: primäre, offizielle Grundquelle zum Begriff der Versionsverwaltung.

2. Atlassian - What is version control?  
   https://www.atlassian.com/git/tutorials/what-is-version-control  
   Verwendung: moderne, praxisnahe Zusammenfassung zur Funktionsweise und den Vorteilen von VCS.

Abgerufen: `2026-04-08`
