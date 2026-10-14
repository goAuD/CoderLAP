# Webservices

## Schneller visueller Überblick

| Akteur | Aufgabe |
|---|---|
| Anbieter | stellt die Funktion oder Daten bereit |
| Client / Requester | ruft den Dienst auf |
| Schnittstelle | bestimmt, wie der Dienst genutzt werden kann |
| Nachricht | die Daten, die gesendet oder empfangen werden |

## Was ist ein Web Service?

Ein Web Service ist ein Softwaredienst,
der über ein Netzwerk erreichbar ist
und auf bestimmte Weise kommuniziert werden kann.

Häufige Eigenschaften:

- hat eine Adresse oder einen Endpunkt
- hat eine Aufrufmethode
- hat ein Datenaustauschformat
- hat eine Art Vertrag oder Beschreibung

## Wofür werden sie verwendet?

- Verknüpfung verschiedener Systeme
- Datenaustausch
- Nutzung externer Dienste
- Integration zwischen Unternehmenssystemen
- Verbindung von Mobile App und Backend

## In welcher Form begegnen wir ihnen?

In der Praxis häufig:

- `SOAP`-basierter Web Service
- `REST`-artiges Web-API

Daher überschneiden sich die Begriffe Web Service und API teilweise, sind aber nicht vollständig identisch.

## Web Service und API: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| API | allgemeine Programmierungsschnittstelle |
| Web Service | über Netzwerk mit Webtechnologien erreichbarer Dienst |

Jeder Web Service kann als API betrachtet werden, aber nicht jede API ist ein Web Service.

## Typische Bestandteile

- Endpoint
- Protokoll
- Nachrichtenformat
- Aufrufregeln
- Fehlerbehandlung
- Sicherheitslösungen

## Warum ist das wichtig?

Weil moderne Softwaresysteme selten vollständig für sich allein stehen.

Der Web Service ermöglicht, dass:

- separate Komponenten zusammenarbeiten
- wiederverwendbare Funktionen bereitgestellt werden
- servicebasierte Systeme gebaut werden können

## Ein Dienstaufruf besteht aus mehr als einer URL

Eine Lernanwendung möchte den Kurs mit ID `15` lesen. Ein möglicher HTTP-Vertrag
liefert auf `GET /api/courses/15` den Status `200` mit Kursdaten und bei
unbekannter ID `404`. Die Schnittstellenbeschreibung legt dies fest. Die URL
ist ein Beispiel und kein funktionierender öffentlicher Dienst.

Der Aufrufer muss mehrere Ergebnisse behandeln:

| Fall | Aufgabe des Clients |
|---|---|
| gültige erfolgreiche Antwort | erwartete Datenstruktur prüfen und anzeigen |
| fehlende Berechtigung | verständlicher Hinweis statt endloser Wiederholung |
| Verbindungsabbruch oder Zeitüberschreitung | Warten beenden und gegebenenfalls erneuten Versuch anbieten |
| Überlastung | begrenzte, verzögerte Wiederholung gemäß API-Regeln |

Einen Leseaufruf zu wiederholen hat ein anderes Risiko als das erneute Anlegen
einer Bestellung. War das Anlegen erfolgreich und ging nur die Antwort verloren,
kann eine blinde Wiederholung duplizieren. Dafür kann der Vertrag eine eindeutige
Anfragekennung und Duplikationsschutz vorsehen. Eine Zeitüberschreitung beweist
also nicht, dass der Server nichts ausgeführt hat.

Der Dienst kann auch in einem internen Netz laufen. HTTPS schützt die
Übertragung. Identifikation und Berechtigungsprüfung für jede Ressource sind
zusätzliche Aufgaben.

## Prüfungstaugliche Formulierung

> Ein Web Service ist ein über das Netzwerk erreichbarer Dienst,
> der von anderen Programmen auf geregelte Weise aufgerufen werden kann.  
> Sein Hauptzweck ist die Kommunikation und Integration zwischen Systemen.  
> In der Praxis nutzt er typischerweise ein Webprotokoll
> und ein strukturiertes Nachrichtenformat,
> zum Beispiel SOAP oder REST-basierte HTTP-Kommunikation.

## Schnelle Selbstkontrolle

1. Was ist der Hauptzweck eines Web Service?
2. Wer nutzt ihn typischerweise?
3. Warum ist er bei der Integration von Systemen wichtig?
4. Welche Beziehung hat er zur API?
5. Nenne zwei häufige Ansätze.

## Kurzantworten zur Selbstkontrolle

1. Maschinelle Kommunikation zwischen Systemen
2. Andere Programme und Systeme
3. Weil er geregelten Datenaustausch ermöglicht
4. Ein Web Service ist eine spezielle, über Netzwerk erreichbare Art von API
5. SOAP und REST

## Quellen

Geprüft: `2026-10-14`.

- [IETF: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): Antwortstatus, Wiederholung und Idempotenz.


1. W3C - Web Services Architecture  
   https://www.w3.org/TR/ws-arch/wsa.pdf  
   Verwendung: offizieller begrifflicher Hintergrund zur Web-Services-Architektur und ihren Akteuren.

2. MDN - API  
   https://developer.mozilla.org/en-US/docs/Glossary/API  
   Verwendung: Klärung des API-Begriffs, um den Web Service richtig einordnen zu können.

3. W3C - Web Services Description Language (WSDL) Version 2.0 Part 0: Primer  
   https://www.w3.org/TR/wsdl20-primer/  
   Verwendung: praktischer Kontext zum klassischen Web-Service-Ökosystem.

Abgerufen: `2026-04-08`
