# POP3 und POP3S

## Schneller visueller Überblick

| Protokoll | Typischer Port | Hauptzweck |
|---|---|---|
| POP3 | `110` | E-Mails herunterladen |
| POP3S | `995` | E-Mails verschlüsselt herunterladen |

## Wozu dient POP3?

POP3 dient dazu, dass der Client:

- sich mit dem Server verbindet
- die E-Mails herunterlädt

Traditionell ist das POP3-Modell eher so:

- "Lade die E-Mail vom Server auf meinen Rechner herunter"

Daher einfach, aber bei mehreren Geräten weniger komfortabel.

## Worauf muss man achten?

POP3 ist im Allgemeinen weniger geeignet für:

- Synchronisierung zwischen mehreren Geräten
- serverseitige Ordnerverwaltung
- komplexe E-Mail-Workflows

Dafür ist oft `IMAP` besser geeignet.

## Was ist POP3S?

POP3S ist die verschlüsselte Nutzung von POP3.

Das bedeutet:

- die Verbindung ist über TLS geschützt
- Anmeldedaten und Verkehr werden nicht im Klartext übertragen

## Warum ist Verschlüsselung wichtig?

Weil bei E-Mail sensible Daten betroffen sein können:

- das Passwort
- der Inhalt der E-Mail
- der Anhang

Daher ist heute eine verschlüsselte Verbindung die erwartete Lösung.

## Nicht verwechseln

| Begriff | Wofür? |
|---|---|
| POP3 | E-Mails herunterladen |
| POP3S | POP3 verschlüsselt |
| IMAP | serverseitige Synchronisierung |
| SMTP | Versand und Weiterleitung |

## Prüfungstaugliche Formulierung

> POP3 ist ein E-Mail-Protokoll zum Herunterladen eingehender E-Mails.  
> Aufgrund seines einfachen Modells eignet es sich primär zum lokalen Herunterladen, während IMAP für die Synchronisierung über mehrere Geräte oft die bessere Wahl ist.  
> POP3S ist die mit TLS geschützte Variante von POP3 und daher sicherer.

## Häufige Prüfungsfehler

- POP3 als Sendeprotokoll bezeichnen.
- POP3S mit SMTPS verwechseln.
- Nicht wissen, dass POP3 eher ein Download-orientiertes Modell ist.
- Die Bedeutung der Verschlüsselung vergessen.

## Schnelle Selbstkontrolle

1. Wozu dient POP3?
2. Welcher Port gehört typischerweise zu POP3?
3. Welcher Port gehört typischerweise zu POP3S?
4. Was ist der Hauptunterschied zwischen POP3 und POP3S?
5. Welches ist für die Synchronisierung über mehrere Geräte oft besser: POP3 oder IMAP?

## Kurzantworten zur Selbstkontrolle

1. Zum Herunterladen eingehender E-Mails
2. `110`
3. `995`
4. POP3S ist verschlüsselt
5. IMAP

## Quellen

1. RFC 1939 - Post Office Protocol - Version 3  
   https://www.rfc-editor.org/rfc/rfc1939.html  
   Verwendung: primäre Standardquelle für POP3.

2. RFC 8314 - Cleartext Considered Obsolete: Use of TLS for Email Submission and Access  
   https://www.rfc-editor.org/rfc/rfc8314.html  
   Verwendung: moderne Empfehlung für verschlüsselten E-Mail-Zugriff, einschließlich Port `995`.

3. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Verwendung: offizielles Portregister für die Ports `110` und `995`.

Abgerufen: `2026-04-08`
