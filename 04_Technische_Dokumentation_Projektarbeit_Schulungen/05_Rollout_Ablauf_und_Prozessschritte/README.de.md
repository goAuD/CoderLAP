# Roll-out Ablauf und Prozessschritte

## Schneller visueller Überblick

| Phase        | Was bedeutet es?                                    |
| ------------ | --------------------------------------------------- |
| Planung      | Ziele, Beteiligte, Zeitplan                         |
| Vorbereitung | Umgebung, Berechtigungen, Backups                   |
| Pilot        | Erprobung in kleinerem Kreis                        |
| Rollout      | tatsächliche Einführung                             |
| Überprüfung  | Betrieb, Monitoring, Fehler                         |
| Übergabe     | Wissensübergabe, Dokumentation                      |
| Abnahme      | Bestätigung, dass das System übernommen werden kann |
| Rollback     | Rückführung, wenn der Rollout nicht erfolgreich ist |

## Was ist das Ziel eines Rollouts?

Dass das neue System oder die Änderung:

- sicher
- geplant
- überprüfbar

in die produktive Umgebung überführt wird.

## Typischer Rollout-Ablauf

## 1. Planung

Zuerst muss festgelegt werden:

- was eingeführt wird
- wen es betrifft
- wann es stattfindet
- welche Risiken bestehen
- was als erfolgreiche Einführung gilt

## 2. Vorbereitung

Dazu kann gehören:

- Vorbereitung der Umgebung
- Berechtigungen
- Versionsprüfung
- Testen
- Überprüfung der Sicherheitsanforderungen
- Backup-Erstellung

## 3. Pilot oder stufenweise Einführung

In vielen Fällen bekommt nicht sofort jeder das neue System.

Vorteil:

- Probleme werden früher erkannt
- das Risiko ist geringer

## 4. Tatsächlicher Rollout

Das ist die eigentliche Produktiveinführung:

- Installation
- Konfiguration
- Aktivierung
- Umstellung des Dienstes

## 5. Überprüfung und Monitoring

Nach dem Rollout muss beobachtet werden:

- ob alles gestartet ist
- ob der Dienst funktioniert
- ob es Fehler gibt
- ob eingegriffen werden muss

## 6. Schulung und Support

Wichtig kann sein:

- Benutzerinformation
- Schulung
- Kurzanleitung
- Vorbereitung von Helpdesk oder Support

## 7. Übergabe und Abnahme

Dazu gehört:

- Übergabe der Dokumentation
- Klärung der Verantwortlichkeiten
- Rückmeldung des Kunden oder Auftraggebers
- formelle oder informelle Abnahme

## Wichtige Rollout-Elemente laut Themenkatalog

## 1. Sicherheitsanforderungen

Überprüft werden muss zum Beispiel:

- Berechtigungen
- Zugriff
- Datenschutz
- Verschlüsselung, falls erforderlich
- Protokollierung

## 2. Abbruch und Rückführung / Rollback

Wenn der Rollout fehlschlägt:

- muss es einen Plan zur Rückführung geben
- muss auf einen früheren Zustand zurückgekehrt werden können

Das ist besonders wichtig bei kritischen Systemen.

## 3. Datenmigration / Konvertierung

Wenn Daten übertragen werden müssen:

- muss das Format überprüft werden
- muss das Ergebnis nach der Migration validiert werden
- muss mit dem Risiko von Datenverlust gerechnet werden

## 4. Anwenderschulung

Die Benutzer müssen vorbereitet werden auf:

- neue Oberfläche
- neue Prozesse
- neue Regeln

## 5. Übergabe

Bei der Übergabe muss klar sein:

- wer für das System verantwortlich ist
- wo die Dokumentation ist
- wie der Support abläuft

## 6. Abnahme

Die Abnahme bedeutet, dass der Auftraggeber oder Verantwortliche bestätigt:

- dass das System vereinbarungsgemäß übernommen werden kann

## Worauf muss man achten?

- es muss immer einen Plan geben
- es muss einen Pilot oder Testlauf geben
- eine Rollback-Möglichkeit muss vorhanden sein
- vor der Datenmigration muss ein Backup erstellt werden
- Kommunikation und Schulung dürfen nicht vergessen werden

## Prüfungstaugliche Formulierung

> Ein Rollout ist die geplante Einführung eines neuen Systems oder einer Anwendung in die Produktivumgebung.  
> Der Ablauf umfasst typischerweise Planung, Vorbereitung, Pilot,
> eigentliche Einführung, Überprüfung, Schulung, Übergabe und Abnahme.  
> Wichtige Bestandteile sind die Berücksichtigung der Sicherheitsanforderungen,
> die Datenmigration sowie die Rollback-Möglichkeit für den Fall,
> dass die Einführung nicht gelingt.

## Häufige Prüfungsfehler

- Den Rollout nur als Installation betrachten.
- Die Rollback-Möglichkeit nicht erwähnen.
- Die Benutzerschulung auslassen.
- Nicht an die Datenmigration denken.
- Den Unterschied zwischen Übergabe und Abnahme nicht erkennen.

## Schnelle Selbstkontrolle

1. Was ist das Ziel eines Rollouts?
2. Warum ist der Pilot wichtig?
3. Was ist die Rolle des Rollbacks?
4. Warum ist die Überprüfung der Datenmigration kritisch?
5. Warum braucht es eine Benutzerschulung?

## Kurzantworten zur Selbstkontrolle

1. Sichere und geplante Einführung
2. Weil er das Risiko in kleinerem Kreis reduziert
3. Er ermöglicht die Rückführung bei fehlgeschlagener Einführung
4. Weil sonst Datenverlust oder fehlerhafte Daten entstehen können
5. Weil die Benutzer das neue System bedienen können müssen

## Quellen

1. Planning the Deployment - Microsoft Learn  
   https://learn.microsoft.com/en-us/iis/web-hosting/installing-infrastructure-components/planning-the-deployment  
   Verwendung: Rollout-Planung, Checkliste, Umgebung, Monitoring, Schulung der Teammitglieder.

2. Use Advisor for Teams roll out - Microsoft Learn  
   https://learn.microsoft.com/en-us/microsoftteams/use-advisor-teams-roll-out  
   Verwendung: Rollout-Schritte, Beteiligte, Vorbereitung, stufenweise Einführung.

3. Cloud Update - Microsoft 365 Apps admin center  
   https://learn.microsoft.com/en-us/microsoft-365-apps/admin-center/cloud-update  
   Verwendung: Rollout-Wellen, Pilot sowie Rückzugs- / Rollback-Möglichkeiten.

4. Migration best practices - Microsoft Entra architecture  
   https://learn.microsoft.com/de-de/entra/architecture/migration-best-practices  
   Verwendung: Best Practices für Migration und stufenweise Umstellung.

Abgerufen: `2026-04-08`
