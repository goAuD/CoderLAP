# Schutz von Client PCs

## Schneller visueller Überblick

| Schutzmaßnahme | Warum nötig? |
|---|---|
| Updates | Behebung von Fehlern und Schwachstellen |
| Virenschutz | Erkennung und Blockierung von Malware |
| Firewall | Filterung von Netzwerkverbindungen |
| MFA | Stärkung des Kontoschutzes |
| Benutzereinschränkung | geringerer Schaden bei Fehlern oder Angriffen |
| Backup | Wiederherstellung nach Datenverlust |

## Wovor muss der Client-Rechner geschützt werden?

Typische Risiken:

- Malware
- Phishing
- schwaches oder wiederverwendetes Passwort
- veraltete Software
- unbefugter Zugriff
- Datenverlust

## Welche sind die wichtigsten Schutzmaßnahmen?

### 1. Regelmäßig aktualisieren

Aktualisiert werden müssen:

- Betriebssystem
- Browser
- Anwendungen
- Sicherheitssoftware

Das reduziert die Anzahl ausnutzbarer Fehler.

### 2. Malware-Schutz verwenden

Erforderlich:

- ein aktueller Viren- und Bedrohungsschutz

Das kann helfen bei:

- Erkennung bekannter Schadsoftware
- Blockierung verdächtigen Verhaltens

### 3. Firewall eingeschaltet lassen

Die clientseitige Firewall:

- filtert die Netzwerkverbindungen
- reduziert die Angriffsfläche

### 4. Starkes Passwort + MFA

Grundregel:

- langes, einzigartiges Passwort
- möglichst ein Passwortmanager
- wo möglich, MFA

### 5. Nicht ständig mit Admin-Rechten arbeiten

Für die tägliche Nutzung ist besser:

- ein normales Benutzerkonto

### 6. Auf Phishing und Downloads achten

Nicht:

- verdächtige Anhänge öffnen
- auf ungeprüfte Links klicken
- Programme aus unbekannten Quellen installieren

### 7. Backup

Wenn doch etwas passiert:

- ist ein gutes Backup einer der wichtigsten Rettungsanker

## Was kann kein einzelnes Werkzeug allein leisten?

Weder das Antivirus, noch die Firewall, noch MFA reichen allein aus.

Ein guter Schutz:

- besteht aus mehreren Schichten

## Abnahme eines Lern-Laptops

Ein Rechner ist erst dann vorbereitet, wenn das Prüfergebnis nachvollziehbar ist. Prüfe den tatsächlichen Aktualisierungsstand von Betriebssystem und Browser, die unterstützte Version und erforderliche Neustarts. Firmware und installierte Anwendungen gehören ebenfalls ins Inventar. Bei ausgelaufenem Support sind Ablösung oder dokumentierte vorübergehende Schutzmaßnahmen zu planen.

Nutze im Alltag ein Standardkonto, automatische Bildschirmsperre und bei Bedarf Laufwerksverschlüsselung. Diese schützt vor allem Daten auf einem verlorenen, gesperrten Gerät; Malware in einer bereits angemeldeten Sitzung hält sie nicht auf. Der Wiederherstellungsschlüssel muss auch verfügbar sein, wenn der Laptop selbst ausfällt.

Beim Konto helfen einzigartiges Passwort, Passwortmanager und MFA zusammen. Korrekt verwendete FIDO/WebAuthn-Authentifizierung kann phishing-resistent sein; manuell eingegebene Einmalcodes sind es normalerweise nicht. Prüfe auch die Wiederherstellungsmöglichkeit für das Konto.

Stelle abschließend ein Beispieldokument in einen separaten Ordner wieder her und öffne es. Bei Verdacht auf eine Infektion sollten Netzwerkisolation und Meldung an den Betrieb vor unkontrollierten Bereinigungsversuchen stehen. So sinkt das Risiko weiterer Ausbreitung und des Verlusts von Belegen.

## Prüfungstaugliche Formulierung

> Der Schutz des Client-PCs muss in mehreren Schichten umgesetzt werden.  
> Dazu gehören regelmäßige Updates, aktueller Malware-Schutz,
> die lokale Firewall, starke Passwörter und MFA,
> eingeschränkte Berechtigungen, Bewusstsein gegen Phishing
> und regelmäßige Datensicherung.  
> Kein einzelnes Werkzeug reicht für sich allein aus, daher ist ein mehrschichtiger Schutz erforderlich.

## Schnelle Selbstkontrolle

1. Nenne fünf grundlegende Schutzmaßnahmen für Client-PCs.
2. Warum sind Updates wichtig?
3. Warum ist MFA nützlich?
4. Warum sollte man nicht ständig mit Admin-Rechten arbeiten?
5. Warum ist ein Backup wichtig, auch wenn es einen Antivirus gibt?

## Kurzantworten zur Selbstkontrolle

1. Updates, Antivirus, Firewall, starkes Passwort, MFA, eingeschränkte Rechte, Backup
2. Weil sie Schwachstellen beheben
3. Weil es über das Passwort hinaus zusätzlichen Schutz bietet
4. Weil bei Fehlern oder Angriffen der Schaden größer ist
5. Weil es bei Datenverlust und Ransomware eine Wiederherstellungsmöglichkeit bietet

## Quellen

1. CISA - Secure Yourself & Your Family  
   https://www.cisa.gov/secure-our-world/secure-yourself-your-family  
   Verwendung: offizielle, allgemeine Cyber-Hygiene-Grundquelle für Client-Schutz.

2. CISA - Update Software  
   https://www.cisa.gov/secure-our-world/update-software  
   Verwendung: zur Bedeutung schneller und regelmäßiger Updates.

3. CISA - Recognize and Report Phishing  
   https://www.cisa.gov/secure-our-world/recognize-and-report-phishing  
   Verwendung: für das Benutzerbewusstsein gegen Phishing.

4. CISA - More Than a Password  
   https://www.cisa.gov/mfa  
   Verwendung: Rolle von MFA beim Kontoschutz.

5. Microsoft Support - Windows Security App Overview  
   https://support.microsoft.com/en-us/office/windows-security-app-overview-ae70cc96-a9cd-4443-a210-e41cb973d3a6  
   Verwendung: Überblick über moderne Windows-Client-Schutzkomponenten.

6. Microsoft Support - Virus and Threat Protection in the Windows Security App  
   https://support.microsoft.com/en-us/windows/virus-and-threat-protection-in-the-windows-security-app-1362f4cd-d71a-b52a-0b66-c2820032b65e  
   Verwendung: praktische Seite des aktuellen Endpunktschutzes und der Bedrohungsverwaltung.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html): Authentifizierungsfaktoren und Phishing-Resistenz
- [CISA: StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide): getrennte, verschlüsselte Sicherungen und geprüfte Wiederherstellung

Geprüft: `2026-10-14`.
