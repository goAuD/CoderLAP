# Problemmanagement

## Schneller visueller Überblick

```text
Incident / wiederkehrender Fehler
    -> Ursachenuntersuchung
    -> Bestimmung der Grundursache
    -> dauerhafte Lösung
    -> Prävention
```

## Was ist Problem Management?

Es ist ein Prozess, der:

- tatsächliche oder mögliche Ursachen eines oder mehrerer Incidents identifiziert
- die Ursachen untersucht
- die Grundursache ermittelt
- eine dauerhafte Behebung oder vorbeugende Maßnahme einleitet

## Warum ist das wichtig?

- reduziert wiederkehrende Fehler
- verbessert die Stabilität des Services
- verringert die Betriebsbelastung
- hilft, aus früheren Fehlern zu lernen

## Problem und Incident: nicht verwechseln

| Begriff | Fokus |
|---|---|
| Incident | schnelle Wiederherstellung, Servicewiederherstellung |
| Problem | Aufdeckung der Grundursache und Prävention |

Ein Incident muss schnell behandelt werden, das Problem Management untersucht hingegen, warum es passiert ist.

## Typische Schritte

- Problem identifizieren
- Daten und Muster sammeln
- Grundursachenanalyse
- Workaround oder endgültige Lösung
- Dokumentation und Lessons Learned

## Die Ursache wiederkehrender Speicherprobleme untersuchen

Der Dienst fällt aus, weil die Festplatte voll ist. Incident Management stellt zunächst den Dienst sicher wieder her und bewahrt notwendige Nachweise. Problem Management untersucht, warum der Speicherverbrauch unbegrenzt gewachsen ist.

Messungen zeigen: Ein fehlerhafter Import wiederholt dieselbe Meldung, die Logs werden nicht rotiert und die Warnung kommt zu spät. Es gibt mehrere beitragende Ursachen. Dauerhafte Maßnahmen sind die Importkorrektur, passend begrenzte Logrotation und frühere Kapazitätswarnungen. Jede erhält Zuständigkeit und Prüftermin. Einfaches Abschalten der Logs würde spätere Untersuchungsmöglichkeiten verlieren lassen.

Ein Workaround lindert Auswirkungen vorläufig, beseitigt aber nicht unbedingt die Ursache. Die Analyse muss nicht auf mehrere gleiche Incidents warten: Auch ein einzelner schwerer Fall oder eine vorab erkannte mögliche Ursache kann sie rechtfertigen. Die Erkenntnisse verbessern das System, statt einer Person die Schuld zuzuweisen.

## Prüfungstaugliche Formulierung

> Ziel des Problem Managements ist die Aufdeckung der Grundursache von Problemen
> und die Prävention ähnlicher Fehler in der Zukunft.  
> Es konzentriert sich nicht nur auf die schnelle Behandlung von Symptomen,
> sondern auch auf die Analyse der zugrunde liegenden Ursachen.  
> Daher ist das Problem Management ein wichtiger Bestandteil der nachhaltigen Qualitätsverbesserung und des stabilen Betriebs.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel des Problem Managements?
2. Was ist der Unterschied zum Incident Management?
3. Warum ist die Suche nach der Grundursache wichtig?
4. Welchen Vorteil hat es langfristig?
5. Was kann das Ergebnis des Prozesses sein?

## Kurzantworten zur Selbstkontrolle

1. Aufdeckung der Grundursache und Prävention
2. Das Incident Management zielt auf schnelle Wiederherstellung, das Problem Management sucht die Ursache
3. Weil so Wiederholungen verhindert werden können
4. Stabilerer Betrieb und weniger wiederkehrende Fehler
5. Workaround, endgültige Behebung oder vorbeugende Maßnahme

## Quellen

- [Atlassian: Problem and incident management](https://www.atlassian.com/incident-management/devops/incident-vs-problem-management)  
  Umgang mit tatsächlichen oder möglichen Ursachen eines oder mehrerer Incidents.

- [Google SRE: Postmortem culture](https://sre.google/sre-book/postmortem-culture/)  
  Mehrere beitragende Ursachen und nachverfolgbare Maßnahmen ohne Schuldzuweisung.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Atlassian - Problem management in Jira Service Management  
   https://www.atlassian.com/software/jira/service-management/product-guide/getting-started/problem-management  
   Verwendung: moderne, offizielle Zusammenfassung zu Zweck und Funktionsweise des Problem Managements.

2. Atlassian - Problem management vs. incident management  
   https://www.atlassian.com/incident-management/devops/incident-vs-problem-management  
   Verwendung: gut nutzbare Quelle zur Klärung des Unterschieds zwischen Problem und Incident Management.

Abgerufen: `2026-04-08`
