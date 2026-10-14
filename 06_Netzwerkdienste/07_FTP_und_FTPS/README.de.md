# FTP und FTPS

## Schneller visueller Überblick

| Protokoll | Typischer Port | Schutz |
|---|---|---|
| FTP | `21` | keine angemessene moderne Verschlüsselung |
| FTPS | `21` oder `990` | TLS-Schutz |

## Was ist FTP?

FTP ist ein klassisches Protokoll zur Dateiübertragung.

Merkmale:

- separate Steuer- und Datenverbindung
- alte, aber an vielen Stellen noch bekannte Technologie

Häufige Verwendung:

- Webhosting-Upload
- Dateien zwischen Server und Client verschieben

## Was ist das Problem mit dem einfachen FTP?

Bei einfachem FTP können der Datenverkehr und die Authentifizierungsdaten leicht abgehört werden.

Daher aus heutiger Sicht:

- allein nicht als angemessen sicher zu betrachten

## Was ist FTPS?

FTPS ist die mit TLS geschützte Variante von FTP.

Zwei typische Betriebsmodi:

- explicit TLS
- implicit TLS

Auf Prüfungsniveau reicht es zu wissen:

- FTPS ist sicherer als einfaches FTP, weil die Verbindung verschlüsselt werden kann

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| FTP | Dateiübertragung ohne Verschlüsselung |
| FTPS | FTP mit TLS |
| SFTP | ein SSH-basiertes anderes Protokoll, nicht dasselbe wie FTPS |

## Warum ist das wichtig?

Weil viele verwechseln:

- `FTPS`
- `SFTP`

Dabei sind das nicht dasselbe.

## Durchgearbeitete Fehlereingrenzung: Anmeldung geht, Auflisten nicht

Bei FTP sind Steuer- und Datenverbindung getrennt. Daher kann nach erfolgreicher Anmeldung die Verzeichnisliste noch an einer Firewall scheitern. Im aktiven Modus beginnt der Server die Datenverbindung zum Client. Im passiven Modus verbindet sich der Client mit dem vom Server genannten Datenport; Server-Firewall und NAT-Konfiguration müssen diesen Weg berücksichtigen.

Bei explizitem FTPS beginnt `AUTH TLS` normalerweise auf Steuerport `21` den geschützten Betrieb. Der Schutz der Datenverbindung wird gesondert eingestellt, beispielsweise mit `PROT P`. Verschlüsselte Anmeldung allein beweist noch keine Verschlüsselung der Dateidaten. Implizites FTPS startet gewöhnlich auf `990` direkt mit TLS.

Im Test wird eine harmlose Beispieldatei hoch- und heruntergeladen; Inhalt und Zertifikat werden geprüft. SFTP ist dagegen ein anderes Protokoll über SSH, gewöhnlich auf Port `22`. Aus einer FTPS-Konfiguration wird deshalb durch bloßes Ändern des Ports noch keine SFTP-Konfiguration.

## Prüfungstaugliche Formulierung

> FTP ist ein klassisches Dateiübertragungsprotokoll zwischen Client und Server.  
> Einfaches FTP bietet keine angemessene moderne Verschlüsselung,
> daher ist FTPS die sicherere Alternative,
> die die Verbindung mit TLS schützt.  
> FTPS ist nicht dasselbe wie das SSH-basierte SFTP.

## Schnelle Selbstkontrolle

1. Wozu dient FTP?
2. Welcher Port ist der typische FTP-Port?
3. Was ist der Hauptunterschied zwischen FTP und FTPS?
4. Sind FTPS und SFTP dasselbe?
5. Warum ist einfaches FTP problematisch?

## Kurzantworten zur Selbstkontrolle

1. Zur Dateiübertragung
2. `21`
3. FTPS verwendet TLS
4. Nein
5. Weil es keine angemessene moderne Verschlüsselung hat

## Quellen

1. RFC 959 - File Transfer Protocol  
   https://www.rfc-editor.org/rfc/rfc959  
   Verwendung: klassische primäre Standardquelle für FTP.

2. RFC 4217 - Securing FTP with TLS  
   https://www.rfc-editor.org/rfc/rfc4217  
   Verwendung: primäre Standardquelle für FTPS.

3. MDN - FTP  
   https://developer.mozilla.org/en-US/docs/Glossary/FTP  
   Verwendung: kurze, moderne technische Zusammenfassung zu FTP und dessen Sicherheitskontext.

4. IANA - Service Name and Transport Protocol Port Number Registry  
   https://www.iana.org/assignments/service-names-port-numbers  
   Verwendung: offizielles Portregister für die Ports `21` und `990`.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [RFC 4217: Securing FTP with TLS](https://www.rfc-editor.org/rfc/rfc4217): getrennter Schutz von Steuer- und Datenkanal.
- [RFC 959: FTP](https://www.rfc-editor.org/rfc/rfc959): aktive und passive Datenverbindung.

Geprüft: `2026-10-14`.
