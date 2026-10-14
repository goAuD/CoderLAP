# SSL

## Schneller visueller Überblick

| Begriff | Heutige Situation |
|---|---|
| SSL 2.0 / 3.0, TLS 1.0 / 1.1 | veraltet, für eine zeitgemäße Sicherheitskonfiguration ungeeignet |
| TLS 1.2 | bei bestehenden Systemen mit geeigneter Konfiguration noch im Einsatz |
| TLS 1.3 | bevorzugte aktuelle Version |
| "SSL certificate" | umgangssprachlich, aber technisch ungenau |

## Was war SSL?

SSL war eine ältere Familie von Sicherheitsprotokollen, die den Schutz der Netzwerkverbindung zum Ziel hatte.

Ihre Aufgabe war ähnlich der des heutigen TLS:

- Verschlüsselung
- Integrität
- Authentifizierung

## Warum verwenden wir es heute nicht mehr?

Weil die alten SSL-Versionen:

- schwache oder veraltete Lösungen enthalten
- bekannte Sicherheitsprobleme haben

Daher ist in modernen Systemen der richtige Ansatz:

- `TLS`

## Was ist der Zusammenhang mit HTTPS?

HTTPS bedeutet heute in der Praxis:

- HTTP mit TLS

und nicht "HTTP mit SSL" im modernen, genauen Sinne.

## Warum ist es wichtig, das klar zu sehen?

Weil bei Prüfungen häufig vorkommt:

- "Was ist SSL?"
- "Was ist der Unterschied zwischen SSL und TLS?"

Der Kern einer guten Antwort:

- SSL ist ein historischer Begriff
- TLS ist das heutige korrekte, moderne Protokoll

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| SSL | altes, veraltetes Sicherheitsprotokoll |
| TLS | die heutige, moderne Lösung |
| HTTPS | HTTP mit TLS geschützt |
| Zertifikat | Teil der Authentifizierungskette, nicht das Protokoll selbst |

## Durchgearbeitetes Beispiel: Was prüft der Browser?

Für `https://shop.example.org` erwartet der Client ein zum Namen passendes, zeitlich gültiges Zertifikat und eine vertrauenswürdige Zertifikatskette. Im Handshake entstehen die Schlüssel für den Schutz des Datenverkehrs. Das Zertifikat ist öffentlich; den dazugehörigen privaten Schlüssel schützt der Server. Für große Mengen von Anwendungsdaten wird symmetrische Verschlüsselung verwendet.

Ist das Zertifikat abgelaufen oder auf einen anderen Namen ausgestellt, wird die Ursache behoben. Das Abschalten der Zertifikatsprüfung ersetzt keine korrekte Konfiguration. Ein gültiges Zertifikat kann die Berechtigung über die Domain belegen, bestätigt aber beispielsweise keine redliche Geschäftstätigkeit eines Onlineshops.

**Stand 2026-10-14:** RFC 9852 verlangt für neue Protokolle, die TLS einsetzen, TLS 1.3 als Vorgabe. TLS 1.2 kann als begründete Kompatibilitätsoption erhalten bleiben. Das bedeutet nicht, dass an einem einzigen Stichtag jede bestehende TLS-1.2-Verbindung automatisch unbrauchbar wird.

## Prüfungstaugliche Formulierung

> SSL steht für Secure Sockets Layer, ist aber heute bereits eine veraltete Technologie.  
> In modernen Systemen wird stattdessen TLS verwendet, daher ist HTTPS eigentlich HTTP mit TLS-Schutz.  
> Im Alltag ist das Wort "SSL" noch häufig geblieben, aber technisch ist TLS der korrekte heutige Begriff.

## Schnelle Selbstkontrolle

1. Wofür steht die Abkürzung SSL?
2. Wird SSL heute noch als moderne Empfehlung verwendet?
3. Was ist das heutige korrekte moderne Äquivalent?
4. Was bedeutet im Alltag häufig "SSL certificate"?
5. Baut HTTPS heute auf SSL oder TLS auf?

## Kurzantworten zur Selbstkontrolle

1. Secure Sockets Layer
2. Nein
3. TLS
4. Meistens ein TLS-Zertifikat
5. TLS

## Quellen

1. RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3  
   https://www.rfc-editor.org/rfc/rfc8446  
   Verwendung: primäre Standardquelle für das heutige moderne TLS.

2. MDN - TLS  
   https://developer.mozilla.org/en-US/docs/Glossary/TLS  
   Verwendung: kurze, moderne technische Erklärung der Rolle von TLS.

3. MDN - SSL  
   https://developer.mozilla.org/en-US/docs/Glossary/SSL  
   Verwendung: knappe Zusammenfassung, dass SSL ein historischer Begriff ist und heute TLS korrekt ist.

4. MDN - Transport Layer Security (TLS)  
   https://developer.mozilla.org/en-US/docs/Web/Security/Transport_Layer_Security  
   Verwendung: praktischer Hintergrund zur Funktionsweise von TLS und zur Websicherheit.

Abgerufen: `2026-04-08`

### Geprüfte Quellen zur Ergänzung

- [RFC 9325: Secure TLS use](https://www.rfc-editor.org/rfc/rfc9325.html): Versionen und sichere Konfiguration.
- [RFC 9852: New protocols and TLS 1.3](https://www.rfc-editor.org/rfc/rfc9852.html): Änderung von 2026 für neue Protokolle.

Geprüft: `2026-10-14`.
