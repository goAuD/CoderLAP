# Protokollieren technischer Arbeiten

## Schneller visueller Überblick

| Frage                        | Was muss festgehalten werden?   |
| ---------------------------- | ------------------------------- |
| wer?                         | verantwortliche Person          |
| wann?                        | Datum, Uhrzeit                  |
| wo?                          | System, Umgebung, Gerät         |
| was?                         | durchgeführte Tätigkeit         |
| warum?                       | Ziel oder Begründung            |
| was war das Ergebnis?        | Erfolg, Fehler, Abweichung      |
| was ist der nächste Schritt? | Maßnahme, Eskalation, Abschluss |

## Warum muss protokolliert werden?

Weil technische Arbeiten häufig:

- komplex sind
- mehrere Personen betreffen
- nachträglich überprüft werden müssen
- mit der Fehlersuche zusammenhängen
- für Audits oder Übergaben wichtig sind

## Wozu ist ein gutes Protokoll gut?

- Nachvollziehbarkeit
- Transparenz
- Fehlersuche
- Klärung von Verantwortlichkeiten
- Wissensübergabe
- Qualitätssicherung

## Was muss ein technisches Protokoll enthalten?

## 1. Grunddaten

- Datum
- Uhrzeit
- Name des Erstellers
- betroffenes System / Gerät
- Version oder Umgebung

## 2. Aufgabenbeschreibung

Kurz:

- was war die Aufgabe
- warum wurde eingegriffen

## 3. Durchgeführte Schritte

Dokumentiert werden muss:

- welche Schritte durchgeführt wurden
- in welcher Reihenfolge
- mit welchen Werkzeugen oder Befehlen

## 4. Ergebnis

Es muss angegeben werden:

- ob es erfolgreich war oder nicht
- was sich geändert hat
- ob es Abweichungen gibt
- in welchem Zustand das System verblieben ist

## 5. Fehler und Beobachtungen

Zum Beispiel:

- Fehlermeldung
- ungewöhnliches Verhalten
- Risiko
- bekannte Einschränkung

## 6. Nächste Schritte

- weitere Reparatur
- Eskalation
- erneutes Testen
- Abschluss

## Merkmale eines guten technischen Protokolls

- genau
- kurz, aber nicht lückenhaft
- sachlich
- chronologisch nachvollziehbar
- auch für andere verständlich

## Worauf muss man achten?

- schreibe nicht nur „behoben"
- es muss konkrete Angaben enthalten
- das Ergebnis muss klar sein
- bei Fehlern muss ein Nachweis oder eine Kennung vorhanden sein
- es sollte nicht nachträglich aus dem Gedächtnis zusammengestellt werden

## Einfaches Beispiel

### Aufgabe

Reparatur der Netzwerkeinstellungen des Druckers

### Protokoll

- Datum: `2026-04-08`
- Verantwortlich: `Minta Béla`
- Gerät: `HP Netzwerkdrucker`
- Umgebung: `Büro 2, VLAN 10`
- Tätigkeit: Überprüfung und Neukonfiguration der IP-Adresse
- Schritte:
  - aktuelle IP-Adresse überprüft
  - fehlerhaftes Gateway festgestellt
  - neue Netzwerkeinstellung eingegeben
  - Testdruck durchgeführt
- Ergebnis: Testdruck erfolgreich
- Nächster Schritt: Benutzertest

## Wo wird es verwendet?

- bei der Wartung
- bei der Installation
- bei der Konfiguration
- beim Testen
- bei der Fehlerbehebung
- beim Rollout
- bei der Übergabe

## Ein überprüfbarer Nachweis eines Eingriffs

Das Protokoll einer Aktualisierung einer Lernwebsite kann Folgendes enthalten:

| Feld | Fiktives Beispiel |
| --- | --- |
| Änderung | CHG-17, freigegebene Fehlerkorrektur |
| Zeitpunkt | 2026-10-14 09:15, Europe/Vienna |
| Vorher / nachher | 1.4.1 / 1.4.2 mit den Commit-Kennungen der Releases |
| Prüfung | Startseite, Suche und ein Thema geöffnet; Verweis auf das Testprotokoll |
| Rückführung | Speicherort des vorigen Releases und Verweis auf das erprobte Verfahren |
| Abschluss | 09:25, Bestätigung der verantwortlichen Person; nächste Kontrolle um 10:00 |

„Vermutlich ein Netzwerkproblem“ ist eine Hypothese. „Um 09:18 endete die Anfrage mit einer Zeitüberschreitung“ ist eine Beobachtung. Wir halten beides getrennt fest. Passwörter, vollständige Zugriffstoken und unnötige personenbezogene Daten gehören nicht in das Protokoll. Zugriff und Aufbewahrung der Nachweise werden ebenfalls geregelt, damit die nächste Person sicher weiterarbeiten kann.

## Prüfungstaugliche Formulierung

> Technische Arbeiten zu protokollieren bedeutet, die technischen Tätigkeiten nachvollziehbar zu dokumentieren.  
> Ein gutes Protokoll enthält das Datum, den Verantwortlichen,
> das betroffene System, die durchgeführten Schritte, das Ergebnis,
> eventuelle Fehler und die nächsten Schritte.  
> Das ist wichtig für die Fehlersuche, die Übergabe, die Überprüfbarkeit und die Teamarbeit.

## Schnelle Selbstkontrolle

1. Warum ist das Protokollieren technischer Arbeiten wichtig?
2. Welche Grunddaten müssen festgehalten werden?
3. Was muss im Ergebnisteil stehen?
4. Warum sind die nächsten Schritte wichtig?
5. Was zeichnet ein gutes technisches Protokoll aus?

## Kurzantworten zur Selbstkontrolle

1. Wegen Nachvollziehbarkeit und Fehlersuche
2. Datum, Uhrzeit, Verantwortlicher, betroffenes System / Umgebung
3. Was das Ergebnis des Eingriffs war
4. Weil sie zeigen, wie die Aufgabe fortgesetzt oder abgeschlossen wird
5. Genau, verständlich, sachlich und nachvollziehbar

## Quellen

- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)  
  Ereignisdaten und auszuschließende sensible Daten.

Quellen der Ergänzung geprüft: `2026-10-14`.

1. ISTQB CTFL Syllabus v4.0.1  
   https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Verwendung: test execution logging und work products als strukturierte technische Protokollierung.

2. Azure DevOps Test Plans - Manage test runs  
   https://learn.microsoft.com/en-us/azure/devops/test/test-runs  
   Verwendung: offizielles Beispiel dafür, welche Metadaten und Ergebnisse festgehalten werden sollten.

3. Planning the Deployment - Microsoft Learn  
   https://learn.microsoft.com/en-us/iis/web-hosting/installing-infrastructure-components/planning-the-deployment  
   Verwendung: Checklisten-Ansatz, Schritte, Monitoring und Team-Training als zu dokumentierende Elemente.

Abgerufen: `2026-04-08`
