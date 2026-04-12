# Einschraenkungen bei Benutzerkonten

## Schneller visueller Überblick

| Kontotyp | Wofür geeignet? | Risiko |
|---|---|---|
| Standard User | tägliche Nutzung | geringer |
| Administrator | Systemeingriffe, Installation | höher |

## Warum müssen Berechtigungen eingeschränkt werden?

Wenn ein Benutzer oder Programm zu viele Rechte erhält:

- kann es größeren Schaden anrichten
- kann es leichter Systemeinstellungen ändern
- hat bei Malware auch der Angreifer mehr Zugriff

## Was ist der Standard-User-Ansatz?

Das sicherere Grundprinzip:

- der Benutzer erledigt die tägliche Arbeit mit normalen Rechten
- Admin-Rechte werden nur mit separater Genehmigung oder einem separaten Admin-Konto verwendet

Das reduziert:

- die Anzahl versehentlicher Fehler
- die Auswirkung von Schadcode

## Welche Rolle spielt UAC?

`User Account Control` (`UAC`) ist ein Schutzelement von Windows.

Aufgabe:

- anzeigen, wenn eine Aktion höhere Berechtigungen anfordert
- verhindern, dass alles automatisch mit Admin-Rechten läuft

## Gute Praktiken

- separates Admin-Konto und separates Alltagskonto verwenden
- Admin-Rechte nur bei Bedarf
- UAC eingeschaltet lassen
- unbekannte Programme nicht mit erhöhten Rechten ausführen

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Standard User | eingeschränkter Alltagsbenutzer |
| Admin Account | Konto mit hohen Berechtigungen |
| UAC | Mechanismus zur Erhöhungsgenehmigung |
| Least Privilege | nur die minimal nötigen Rechte vergeben |

## Prüfungstaugliche Formulierung

> Das Ziel der Einschränkung von Benutzerkonten ist die Umsetzung des Prinzips der geringsten Berechtigung.  
> Für die tägliche Arbeit ist es ratsam, ein Standard-User-Konto zu verwenden und nur bei Bedarf auf Admin-Ebene zu erhöhen.  
> Das reduziert das Ausmaß von Fehlern, unbefugten Systemänderungen und durch Malware verursachten Schäden.

## Häufige Prüfungsfehler

- Sagen, dass jeder Admin sein sollte, weil es einfacher ist.
- UAC mit dem Admin-Konto selbst verwechseln.
- Das Least-Privilege-Prinzip nicht erwähnen.
- Glauben, dass die Benutzereinschränkung nur unbequem ist, aber keinen Sicherheitsvorteil bringt.

## Schnelle Selbstkontrolle

1. Warum ist der Standard User für die tägliche Nutzung gut?
2. Was ist das Least-Privilege-Prinzip?
3. Wofür ist UAC zuständig?
4. Warum ist die ständige Admin-Nutzung gefährlich?
5. Was ist die gute Praxis bei Admin-Rechten?

## Kurzantworten zur Selbstkontrolle

1. Weil die Möglichkeit für Schäden geringer ist
2. Nur die minimal nötigen Berechtigungen vergeben
3. Zur Kontrolle von Aktionen mit erhöhten Berechtigungen
4. Weil bei Fehlern oder Malware der Schaden größer ist
5. Nur bei Bedarf, mit separatem oder temporärem Admin-Recht verwenden

## Quellen

1. Microsoft Learn - User Account Control  
   https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/  
   Verwendung: offizielle Windows-Quelle zur Rolle von UAC und Berechtigungserhöhung.

2. Microsoft Learn - How User Account Control works  
   https://learn.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works  
   Verwendung: detailliertere Beschreibung der Standard-User-Grundfunktion und des Erhöhungsprozesses.

3. Microsoft Learn - Local Accounts  
   https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts  
   Verwendung: Microsoft-Empfehlung, dass für die tägliche Arbeit nicht der integrierte Admin-Ansatz der Standard sein sollte.

4. CISA - Zero Trust  
   https://www.cisa.gov/topics/cybersecurity-best-practices/zero-trust  
   Verwendung: offizielle CISA-Quelle zur modernen Sicherheitsbedeutung des Least-Privilege-Prinzips.

Abgerufen: `2026-04-08`
