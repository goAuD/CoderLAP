# SMTP und SMTPS

## Schneller visueller Überblick

| Protokoll / Verwendung | Typischer Port | Hauptzweck |
|---|---|---|
| SMTP relay | `25` | Weiterleitung zwischen Servern |
| message submission | `587` | E-Mail-Einlieferung vom Client |
| implicit TLS submission / "SMTPS" | `465` | verschlüsselte Einlieferung |

## Wozu dient SMTP?

SMTP dient zum:

- Einliefern von E-Mails
- Weiterleiten von E-Mails
- serverseitigen Verwalten des Zustellwegs

Beispiele:

- Der Client sendet die E-Mail an seinen eigenen Anbieter
- Ein Server leitet die E-Mail an den Server des Empfängers weiter

## Warum gibt es mehrere Ports?

Weil die Aufgabe nicht dieselbe ist:

- `25` = klassische Server-zu-Server-Kommunikation
- `587` = clientseitige Submission
- `465` = verschlüsselte Submission, historisch auch als `SMTPS` bekannt

## Was ist SMTPS?

Auf Prüfungsniveau ist es sinnvoll, so zu formulieren:

- `SMTPS` bezieht sich auf die verschlüsselte SMTP-Nutzung

Wichtige Präzisierung:

- in der heutigen Standardwelt sind `SMTP over TLS` oder `message submission over implicit TLS` die genaueren Bezeichnungen

## Worauf muss man achten?

SMTP:

- ist kein Postfach-Leseprotokoll
- ist nicht zur Ordnersynchronisierung gedacht

Dafür werden weiterhin:

- `IMAP`
- `POP3`

verwendet.

## Nicht verwechseln

| Begriff | Wofür? |
|---|---|
| SMTP | Versand und Weiterleitung |
| SMTPS | verschlüsselte SMTP-artige Einlieferung |
| IMAP | Postfachsynchronisierung |
| POP3 | E-Mails herunterladen |

## Prüfungstaugliche Formulierung

> SMTP ist das Protokoll zum Senden und Weiterleiten von E-Mails.  
> Für die clientseitige E-Mail-Einlieferung wird heute häufig Port `587` verwendet,
> für verschlüsselte Submission ist auch Port `465` verbreitet.  
> SMTP dient nicht zum Lesen von E-Mails, dafür werden typischerweise IMAP oder POP3 verwendet.

## Häufige Prüfungsfehler

- SMTP als Leseprotokoll bezeichnen.
- Die Rollen der Ports `25`, `587` und `465` verwechseln.
- Glauben, dass `SMTPS` in jedem Kontext ein eigenes Protokoll ist.
- Vergessen, dass heute verschlüsselte Einlieferung erwartet wird.

## Schnelle Selbstkontrolle

1. Wozu dient SMTP?
2. Welcher Port ist der klassische SMTP-Relay-Port?
3. Welcher Port ist der typische Submission-Port?
4. Welcher Port wird häufig mit SMTPS assoziiert?
5. Verwenden wir SMTP zum Lesen von E-Mails?

## Kurzantworten zur Selbstkontrolle

1. Zum Senden und Weiterleiten
2. `25`
3. `587`
4. `465`
5. Nein

## Quellen

1. RFC 5321 - Simple Mail Transfer Protocol  
   https://datatracker.ietf.org/doc/html/RFC5321  
   Verwendung: primäre Standardquelle für SMTP.

2. RFC 6409 - Message Submission for Mail  
   https://www.rfc-editor.org/rfc/rfc6409.html  
   Verwendung: für die Rolle der clientseitigen E-Mail-Einlieferung (`587`).

3. RFC 8314 - Cleartext Considered Obsolete: Use of TLS for Email Submission and Access  
   https://www.rfc-editor.org/rfc/rfc8314.html  
   Verwendung: moderne Empfehlung für verschlüsselte E-Mail-Einlieferung, einschließlich Port `465`.

4. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Verwendung: offizielles Portregister für die Ports `25`, `465` und `587`.

Abgerufen: `2026-04-08`
