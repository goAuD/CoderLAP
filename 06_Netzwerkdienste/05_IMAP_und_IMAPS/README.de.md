# IMAP und IMAPS

## Schneller visueller Überblick

| Protokoll | Typischer Port | Hauptzweck |
|---|---|---|
| IMAP | `143` | serverseitige Postfachverwaltung |
| IMAPS | `993` | dasselbe verschlüsselt |

## Wozu dient IMAP?

IMAP funktioniert so, dass die E-Mails grundsätzlich auf dem Server bleiben und der Client:

- synchronisiert
- Ordner verwaltet
- Zustände abgleicht

Daher geeignet zum Beispiel für:

- gleichzeitige Nutzung von Laptop und Telefon
- parallele Nutzung mehrerer Clients

## Warum ist es oft besser als POP3?

Weil IMAP besser umgeht mit:

- mehreren Geräten
- gemeinsamem Zustand
- serverseitigen Ordnern
- Suche und Sortierung

## Was ist IMAPS?

IMAPS ist die verschlüsselte Nutzung von IMAP.

Das ist wichtig, weil dadurch:

- die Anmeldedaten geschützt sind
- der E-Mail-Verkehr verschlüsselt ist

## Worauf muss man achten?

IMAP:

- ist kein Sendeprotokoll
- ersetzt nicht SMTP

Zum Senden wird weiterhin typischerweise:

- `SMTP`

benötigt.

## Nicht verwechseln

| Begriff | Wofür? |
|---|---|
| IMAP | serverseitige Postfachsynchronisierung |
| IMAPS | IMAP verschlüsselt |
| POP3 | einfacheres Download-Modell |
| SMTP | E-Mail-Versand |

## Prüfungstaugliche Formulierung

> IMAP ist ein E-Mail-Protokoll zur Synchronisierung von auf dem Server gespeicherten E-Mails und Ordnern.  
> Bei der Nutzung mehrerer Geräte ist es im Allgemeinen vorteilhafter als POP3, da E-Mails und Zustände zentral auf dem Server bleiben.  
> IMAPS ist die mit TLS geschützte, sichere Variante von IMAP.

## Häufige Prüfungsfehler

- IMAP als Sendeprotokoll bezeichnen.
- Behaupten, dass IMAP die E-Mail immer vom Server löscht.
- Nicht wissen, warum es bei mehreren Geräten vorteilhaft ist.
- Die Ports vergessen.

## Schnelle Selbstkontrolle

1. Wozu dient IMAP?
2. Welcher Port ist der typische IMAP-Port?
3. Welcher Port ist der typische IMAPS-Port?
4. Ist für die Nutzung mit mehreren Geräten eher IMAP oder POP3 geeignet?
5. Reicht IMAP zum Senden?

## Kurzantworten zur Selbstkontrolle

1. Zur serverseitigen Postfachverwaltung und Synchronisierung
2. `143`
3. `993`
4. IMAP
5. Nein

## Quellen

1. RFC 9051 - IMAP4rev2  
   https://www.rfc-editor.org/rfc/rfc9051.html  
   Verwendung: moderne primäre Standardquelle für IMAP.

2. RFC 8314 - Cleartext Considered Obsolete: Use of TLS for Email Submission and Access  
   https://www.rfc-editor.org/rfc/rfc8314.html  
   Verwendung: moderne Empfehlung für verschlüsselten IMAP-Zugriff, einschließlich Port `993`.

3. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Verwendung: offizielles Portregister für die Ports `143` und `993`.

Abgerufen: `2026-04-08`
