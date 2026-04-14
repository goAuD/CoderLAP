# SOAP und WSDL

## Schneller visueller Überblick

| Begriff | Rolle |
|---|---|
| SOAP | XML-basierter Nachrichtenaustausch |
| WSDL | maschinenlesbare Beschreibung des Dienstes |

## Was ist SOAP?

`SOAP` (`Simple Object Access Protocol`) ist ein Protokoll
mit XML-basierter Nachrichtenstruktur
für die Kommunikation zwischen Systemen.

Merkmale:

- XML-basiert
- strukturierte Nachrichten
- formalerer und strenger Aufbau
- wird häufig bei Unternehmensintegrationen eingesetzt

Typische Elemente:

- Envelope
- Header
- Body

## Was ist WSDL?

`WSDL` (`Web Services Description Language`) beschreibt, wie ein Dienst genutzt werden kann.

Im Allgemeinen gibt sie an:

- welche Operationen verfügbar sind
- welche Nachrichten erwartet werden
- welche Antworten geliefert werden
- unter welcher Adresse der Dienst erreichbar ist
- über welche Bindung er genutzt werden kann

## Welche Beziehung besteht zwischen ihnen?

Im klassischen Modell:

- WSDL beschreibt den Dienst
- SOAP überträgt tatsächlich die XML-Nachrichten

Also:

- WSDL ist eher ein Vertrag
- SOAP ist eher eine Kommunikationsform

## Warum war das wichtig?

Weil es stark standardisierte und präzise Funktionsweise ermöglicht:

- formale Schnittstelle
- eindeutiger Vertrag
- gut handhabbar in Enterprise-Umgebungen
- Client- und serverseitiger Code kann mit Tools generiert werden

## Was ist der Nachteil?

- schwerer und "gesprächiger" als moderne, leichte HTTP+JSON-Lösungen
- XML ist länger und komplexer
- in vielen Fällen zu aufwendig für einfache Webintegrationen

## SOAP/WSDL und REST: nicht verwechseln

| Aspekt | SOAP/WSDL | REST |
|---|---|---|
| Datenaustausch | typischerweise XML | häufig JSON |
| Beschreibung | formaler Vertrag, WSDL | keine obligatorische einheitliche Beschreibungssprache |
| Stil | strenger | leichter, webnäher |

## Prüfungstaugliche Formulierung

> SOAP ist ein XML-basiertes Nachrichtenprotokoll, das für die Kommunikation von Web Services verwendet wird.  
> WSDL dient hingegen zur Beschreibung des Dienstes: es gibt die Operationen, Nachrichtentypen und Endpunkte an.  
> In klassischen Unternehmenssystemen traten SOAP und WSDL häufig gemeinsam auf,
> da sie einen präzisen, formalen Vertrag
> und standardisierte Kommunikation boten.

## Häufige Prüfungsfehler

- SOAP und WSDL als dasselbe bezeichnen.
- Behaupten, WSDL selbst sende die Daten.
- Die Rolle von XML nicht erwähnen.
- SOAP als typische Basislösung für moderne Frontend-APIs bezeichnen.

## Schnelle Selbstkontrolle

1. Welche Rolle hat SOAP?
2. Welche Rolle hat WSDL?
3. Welche Beziehung besteht zwischen ihnen?
4. Warum war es in Unternehmensumgebungen beliebt?
5. Worin unterscheidet es sich von REST?

## Kurzantworten zur Selbstkontrolle

1. XML-basierter Nachrichtenaustausch
2. Beschreibung des Dienstes
3. WSDL beschreibt, SOAP kommuniziert
4. Weil es formal und standardisiert ist
5. Schwerer und strenger, häufig XML-basiert

## Quellen

1. W3C - SOAP Version 1.2 Part 1: Messaging Framework (Second Edition)  
   https://www.w3.org/TR/soap12-part1/  
   Verwendung: offizieller SOAP-Standard zum Verständnis der Nachrichtenstruktur und Rolle.

2. W3C - Web Services Description Language (WSDL) Version 2.0 Part 0: Primer  
   https://www.w3.org/TR/wsdl20-primer/  
   Verwendung: offizielle, leichter verständliche Einführung in die Rolle von WSDL.

3. W3C - Web Services Architecture  
   https://www.w3.org/TR/ws-arch/wsa.pdf  
   Verwendung: zur Einordnung von SOAP/WSDL in den breiteren Web-Service-Kontext.

Abgerufen: `2026-04-08`
