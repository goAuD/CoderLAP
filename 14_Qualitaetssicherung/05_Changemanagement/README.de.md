# Changemanagement

## Schneller visueller Überblick

```text
Änderungsanforderung
    -> Bewertung
    -> Genehmigung
    -> Einführung
    -> Überprüfung / Rückmeldung
```

## Was ist Change Management?

Es ist ein Prozess, damit Änderungen:

- transparent sind
- keine unnötigen Ausfälle verursachen
- ordnungsgemäß dokumentiert werden
- kontrolliert in das System eingeführt werden

## Warum ist das wichtig?

- reduziert die Wahrscheinlichkeit von Betriebsstörungen
- hilft bei der Risikobewertung
- unterstützt die Klärung von Verantwortlichkeiten
- erleichtert die Nachvollziehbarkeit

## Typische Schritte

- Erfassung der Änderungsanforderung
- Auswirkungsanalyse
- Festlegung von Priorität und Risiko
- Genehmigung
- Umsetzung
- Nachträgliche Überprüfung

## Worauf muss man achten?

- es muss klar sein, was geändert wird
- das Risiko muss bekannt sein
- es muss einen Rollback oder Notfallplan geben
- die Betroffenen müssen informiert werden

## Change Management und Problem Management: nicht verwechseln

| Begriff | Fokus |
|---|---|
| Change Management | kontrollierte Einführung von Änderungen |
| Problem Management | Aufdeckung von Fehlern und Ursachen, Prävention |

## Eine Datenbankänderung in überprüfbaren Schritten

Für Buchungen wird ein zusätzliches Feld benötigt. Der Änderungsantrag nennt Zweck, betroffene Anwendungsversion, mögliche Sperrzeiten und Zusammenspiel von altem und neuem Code. Migration und Wiederherstellung werden in einer Testumgebung geprüft; ein vorhandenes Backup allein beweist noch keine erfolgreiche Wiederherstellbarkeit.

Der Einführungsplan enthält Zuständigkeit, Zeitfenster, Erfolgskontrolle und Abbruchkriterium. Löscht oder transformiert die Änderung Daten, reicht das erneute Installieren alten Codes möglicherweise nicht. Dann können Datenwiederherstellung oder Vorwärtskorrektur mit bekanntem Datenverlustrisiko nötig sein.

Die Freigabe richtet sich nach dem Risiko. Für eine vorab autorisierte, wiederholbare kleine Änderung kann ein einfacher Ablauf genügen; auch eine dringende Korrektur braucht Verantwortliche, Dokumentation und Nachkontrolle. Dieses Thema behandelt technische Änderungen. Beschäftigte auf veränderte Arbeitsweisen vorzubereiten ist eine damit verbundene eigene Aufgabe.

## Prüfungstaugliche Formulierung

> Ziel des Change Managements ist es,
> dass Änderungen am System geplant, genehmigt
> und mit Risikomanagement durchgeführt werden.  
> Dadurch kann die Wahrscheinlichkeit von Ausfällen, Fehlern und unerwünschten Nebenwirkungen reduziert werden.  
> Der Prozess umfasst typischerweise die Erfassung, Bewertung, Genehmigung,
> Durchführung und nachträgliche Überprüfung
> der Änderungsanforderung.

## Schnelle Selbstkontrolle

1. Was ist das Hauptziel des Change Managements?
2. Warum ist die Risikobewertung wichtig?
3. Welche Schritte sind typischerweise enthalten?
4. Warum wird vorab ein Wiederherstellungsplan benötigt?
5. Worin unterscheidet es sich vom Problem Management?

## Kurzantworten zur Selbstkontrolle

1. Kontrollierte Einführung von Änderungen
2. Weil Änderungen Fehler oder Ausfälle verursachen können
3. Erfassung, Bewertung, Genehmigung, Einführung, Überprüfung
4. Für eine bekannte, geprüfte Wiederherstellung; bei Datenänderungen kann mehr als alter Code nötig sein.
5. Das eine verwaltet Änderungen, das andere Ursachen und wiederkehrende Fehler

## Quellen

- [Atlassian: Change management](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-change-management/)  
  Kontrollierte technische Änderungen und risikobasierter Ablauf.

- [Microsoft: Safe deployments](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)  
  Geprüfte Einführung und Wiederherstellung unter Berücksichtigung von Datenänderungen.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. Atlassian Support - What is change management?  
   https://support.atlassian.com/jira-service-management-cloud/docs/what-is-change-management/  
   Verwendung: moderne, offizielle Zusammenfassung zu Zweck und Vorteilen des Change Managements.

2. Atlassian - Jira Service Management features  
   https://support.atlassian.com/jira-service-management-cloud/docs/get-to-know-the-main-jira-service-management-features/  
   Verwendung: offizieller Hintergrund zur Einordnung der ITSM-Praktiken, einschließlich Change Management.

Abgerufen: `2026-04-08`
