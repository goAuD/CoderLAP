# Funktionsprinzip Mail Server

## Schneller visueller Überblick

| Akteur | Aufgabe |
|---|---|
| Benutzer / MUA | schreibt und liest E-Mails |
| Mail Submission Server | der Client liefert hier die E-Mail ein |
| Mail Transfer Server | leitet an andere Server weiter |
| Mailbox Server | speichert eingehende E-Mails |

## Wie wird eine E-Mail versendet?

Typischer Ablauf:

1. Der Benutzer schreibt die E-Mail im Client
2. Der Client sendet die E-Mail per SMTP an den Server
3. Der Server leitet die E-Mail an den Mailserver der Empfängerdomain weiter
4. Der Server des Empfängers speichert die E-Mail

## Wie liest der Empfänger die E-Mail?

Das E-Mail-Programm des Empfängers verbindet sich mit dem Server und synchronisiert die E-Mails typischerweise:

- mit `IMAP`
- oder lädt sie mit `POP3` herunter

## Warum reicht SMTP allein nicht?

Weil SMTP grundsätzlich:

- für das Senden und Weiterleiten von E-Mails gedacht ist

Nicht dafür geeignet:

- komfortable Postfachsynchronisierung
- serverseitige Ordnerverwaltung von E-Mails

Daher gibt es zusätzlich:

- `IMAP`
- `POP3`

## Warum ist das wichtig?

Weil bei Prüfungen häufig gefragt wird:

- welches Protokoll wofür gedacht ist
- wie eine E-Mail von A nach B gelangt

## Nicht verwechseln

| Begriff | Wofür? |
|---|---|
| SMTP | E-Mail-Versand und Weiterleitung |
| IMAP | Synchronisierung von am Server gespeicherten E-Mails |
| POP3 | Herunterladen von E-Mails |

## Durchgearbeiteter Weg: Annas Nachricht an Bela

Anna schreibt von `anna@example.org` an `bela@example.net`. Ihr Client verwendet den Submission-Server ihres Anbieters. Der Anbieter bestimmt das Zustellziel anhand der DNS-`MX`-Einträge von `example.net`. Ein kleinerer MX-Präferenzwert wird bevorzugt; der Eintrag enthält einen Servernamen und nicht unmittelbar das Postfach.

Bei einem vorübergehenden Fehler kann der sendende Server die Nachricht in eine Warteschlange legen und später erneut zustellen. Eine erfolgreiche Annahme bedeutet nicht, dass Bela schon gelesen hat. Das Postfach wird per IMAP-Client oder Webmail geöffnet. Zwischen Browser und Webmail-Anwendung wird gewöhnlich HTTPS verwendet.

Das sichtbare `From`-Feld und der Absender des Transportumschlags sind getrennte Angaben. Ein angezeigter Absendername beweist für sich allein keine Identität. TLS schützt einzelne Verbindungsabschnitte; für Ende-zu-Ende-Inhaltsverschlüsselung wird eine zusätzliche Lösung wie S/MIME benötigt.

## Prüfungstaugliche Formulierung

> Das E-Mail-System besteht aus mehreren Komponenten.  
> Der Benutzer schreibt und liest E-Mails mit einem Client,
> das Einliefern und Weiterleiten erfolgt per SMTP,
> und für den Zugriff auf eingehende E-Mails dient typischerweise IMAP oder POP3.  
> Der Mailserver speichert also nicht nur, sondern empfängt, leitet weiter und stellt auch zu.

## Schnelle Selbstkontrolle

1. Welches Protokoll wird typischerweise zum E-Mail-Versand verwendet?
2. Welche beiden werden typischerweise zum E-Mail-Lesen verwendet?
3. Was ist der Unterschied zwischen SMTP und IMAP?
4. Kann eine E-Mail über mehrere Server laufen?
5. Wozu dient der Mailbox-Server?

## Kurzantworten zur Selbstkontrolle

1. SMTP
2. IMAP und POP3
3. SMTP sendet, IMAP verwaltet und synchronisiert das Postfach
4. Ja
5. Zum Speichern und Bereitstellen der E-Mails

## Quellen

1. RFC 5321 - Simple Mail Transfer Protocol  
   https://datatracker.ietf.org/doc/html/RFC5321  
   Verwendung: primäre Standardquelle für SMTP.

2. RFC 6409 - Message Submission for Mail  
   https://www.rfc-editor.org/rfc/rfc6409.html  
   Verwendung: für die heutige Rolle der clientseitigen Einlieferung (`submission`).

3. RFC 9051 - IMAP4rev2  
   https://www.rfc-editor.org/rfc/rfc9051.html  
   Verwendung: moderne IMAP-Grunddefinition und Verständnis der serverseitigen Postfachverwaltung.

4. RFC 1939 - POP3  
   https://www.rfc-editor.org/rfc/rfc1939.html  
   Verwendung: klassische Grunddefinition von POP3.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [RFC 5321: SMTP](https://www.rfc-editor.org/rfc/rfc5321.html): MX-Zustellung und Antwortklassen.
- [RFC 8551: S/MIME](https://www.rfc-editor.org/rfc/rfc8551.html): Verschlüsselung und Signatur des Nachrichteninhalts.

Geprüft: `2026-10-14`.
