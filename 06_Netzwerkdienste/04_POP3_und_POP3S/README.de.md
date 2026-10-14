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

## Durchgearbeiteter Fall: Wo bleibt die Nachricht?

Ein Client lädt per POP3 drei Nachrichten herunter. Das Herunterladen erzwingt nicht automatisch das Löschen: Der Client kann eine Kopie auf dem Server belassen. `DELE` markiert eine Nachricht zum Löschen, die Aktualisierungsphase nach einem regulären `QUIT` führt die Löschung aus. Die Aufbewahrungsregeln des Anbieters sind eine zusätzliche Frage.

Hat der Laptop die Nachricht bereits vom Server entfernt, kann ein später verbundenes Telefon sie dort nicht mehr herunterladen. Lokal gespeicherte Nachrichten benötigen ein eigenes Backup. Für gemeinsame Lesestatus und Ordner auf zwei Geräten ist daher normalerweise IMAP geeigneter.

Bei POP3S beginnt auf Port `995` sofort TLS. Auf Port `110` kann die Erweiterung `STLS` auf TLS umstellen. Vor dem Senden von Anmeldedaten muss der Client erfolgreiches TLS mit gültigem Zertifikat verlangen; eine Portnummer allein ist keine vollständige Sicherheitseinstellung.

## Prüfungstaugliche Formulierung

> POP3 ist ein E-Mail-Protokoll zum Herunterladen eingehender E-Mails.  
> Aufgrund seines einfachen Modells eignet es sich primär zum lokalen Herunterladen,
> während IMAP für die Synchronisierung über mehrere Geräte
> oft die bessere Wahl ist.  
> POP3S ist die mit TLS geschützte Variante von POP3 und daher sicherer.

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
4. Bei POP3S beginnt TLS sofort; POP3 auf Port 110 kann bei Unterstützung und verpflichtender Nutzung durch STLS geschützt werden
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

### Geprüfte Quellen zur Ergänzung

- [RFC 1939: POP3](https://www.rfc-editor.org/rfc/rfc1939.html): Abruf, Löschmarkierung und UPDATE-Zustand.
- [RFC 2595: TLS with IMAP, POP3 and ACAP](https://www.rfc-editor.org/rfc/rfc2595.html): POP3-STLS-Mechanismus, zusammen mit aktuellen TLS-Vorgaben zu lesen.

Geprüft: `2026-10-14`.
