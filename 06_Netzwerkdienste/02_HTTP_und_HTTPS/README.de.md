# HTTP und HTTPS

## Schneller visueller Überblick

| Protokoll | Vollständiger Name | Port | Schutz |
|---|---|---|---|
| HTTP | Hypertext Transfer Protocol | `80` | keine eingebaute Verschlüsselung |
| HTTPS | Hypertext Transfer Protocol Secure | `443` | durch TLS geschützt |

## Was ist HTTP?

HTTP - mit vollem Namen **Hypertext Transfer Protocol** - ist ein stateless, also zustandsloses Request-Response-Protokoll.

Der typische Ablauf:

1. Der Client sendet eine Anfrage
2. Der Server gibt eine Antwort
3. Die Antwort kann HTML, JSON, Bilder oder andere Inhalte enthalten

Beispiele für HTTP-Methoden:

- `GET`
- `POST`
- `PUT`
- `DELETE`

## Was ist HTTPS?

HTTPS - mit vollem Namen **Hypertext Transfer Protocol Secure** - bedeutet, dass der HTTP-Verkehr über TLS läuft.

Das bietet drei wichtige Dinge:

- Verschlüsselung
- Integritätsschutz
- Serverauthentifizierung

Daher schützt HTTPS den Datenverkehr zum Beispiel:

- gegen Abhören
- gegen einfache Manipulation
- hilft auch beim Schutz gegen gefälschte Server

## Warum ist das wichtig?

Weil heute in der Praxis im Web:

- bei Anmeldungen
- bei Formularen
- bei Zahlungen
- bei API-Aufrufen

HTTPS die Grunderwartung ist.

## Was kann HTTPS nicht?

Es bedeutet nicht automatisch vollständige Sicherheit.

Zum Beispiel löst es allein nicht:

- schwache Passwörter
- fehlerhafte Berechtigungsverwaltung
- Anwendungsfehler wie XSS oder SQL Injection

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| HTTP | Web-Request-Response-Protokoll |
| HTTPS | HTTP mit TLS geschützt |
| TLS | das die Verbindung schützende Sicherheitsprotokoll |
| SSL | alter, veralteter Vorgängername |

## Prüfungstaugliche Formulierung

> HTTP (Hypertext Transfer Protocol) ist das grundlegende Request-Response-Protokoll im Web.  
> HTTPS (Hypertext Transfer Protocol Secure) ist dasselbe Protokoll mit TLS-Schutz
> und gewährleistet daher die Verschlüsselung des Datenverkehrs,
> die Integrität und die Authentifizierung des Servers.  
> In der Praxis ist HTTPS bei modernen Webdiensten der Standard.

## Häufige Prüfungsfehler

- Sagen, dass HTTPS ein völlig anderes Protokoll als HTTP ist.
- HTTP für verschlüsselt halten.
- TLS und SSL im heutigen Sinne als Synonyme behandeln.
- Die Ports vergessen.

## Schnelle Selbstkontrolle

1. Was ist die Hauptaufgabe von HTTP?
2. Was ist der Unterschied zwischen HTTP und HTTPS?
3. Welcher Port ist der typische HTTP-Port?
4. Welcher Port ist der typische HTTPS-Port?
5. Löst HTTPS allein alle Anwendungsfehler?

## Kurzantworten zur Selbstkontrolle

1. Request-Response-Kommunikation im Web
2. HTTPS ist HTTP mit TLS-Schutz
3. `80`
4. `443`
5. Nein

## Quellen

1. RFC 9110 - HTTP Semantics  
   https://www.rfc-editor.org/rfc/rfc9110  
   Verwendung: primäre Standardquelle für die HTTP-Semantik.

2. RFC 9114 - HTTP/3  
   https://www.rfc-editor.org/rfc/rfc9114  
   Verwendung: für den Kontext moderner HTTP-Versionen und das Verständnis der heutigen HTTP-Familie.

3. MDN - Overview of HTTP  
   https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview  
   Verwendung: praktische, entwicklerfreundliche HTTP-Zusammenfassung.

4. MDN - HTTP  
   https://developer.mozilla.org/en-US/docs/Glossary/HTTP  
   Verwendung: kurze Definition für HTTP und HTTPS.

5. MDN - Transport Layer Security (TLS)  
   https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security  
   Verwendung: moderne Erklärung der Rolle von TLS hinter HTTPS.

6. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Verwendung: offizielles Portregister für die Ports `80` und `443`.

Abgerufen: `2026-04-08`
