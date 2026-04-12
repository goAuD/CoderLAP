# SSL

## Schneller visueller Überblick

| Begriff | Heutige Situation |
|---|---|
| SSL 2.0 / 3.0 | veraltet, nicht empfohlen |
| TLS 1.2 / 1.3 | modern, in Verwendung |
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

## Prüfungstaugliche Formulierung

> SSL steht für Secure Sockets Layer, ist aber heute bereits eine veraltete Technologie.  
> In modernen Systemen wird stattdessen TLS verwendet, daher ist HTTPS eigentlich HTTP mit TLS-Schutz.  
> Im Alltag ist das Wort "SSL" noch häufig geblieben, aber technisch ist TLS der korrekte heutige Begriff.

## Häufige Prüfungsfehler

- Sagen, dass SSL heute noch der zeitgemäße Standard ist.
- TLS und SSL als genau dasselbe betrachten.
- Das Zertifikat mit dem gesamten Protokoll verwechseln.
- Glauben, dass SSL nur bei Webseiten existiert.

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
