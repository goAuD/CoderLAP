# REST API

## Schneller visueller Überblick

| Element | Beispiel |
|---|---|
| Ressource | `users`, `orders`, `products` |
| URI | `/api/users/42` |
| Operation | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` |
| Antwort | häufig JSON |

## Was ist REST?

REST ist kein konkretes Protokoll, sondern ein Architekturstil.

Sein Kern ist, dass das System:

- mit Ressourcen arbeitet
- auf standardisierte Weise darauf zugreift
- die Kommunikation zustandslos sein soll

Das passt gut zur Natur des Webs und zur Funktionsweise von HTTP.

## Was ist eine REST API?

Eine API, die:

- webbasierte Ressourcen zugänglich macht
- sie mit URLs identifiziert
- Operationen mit HTTP-Methoden ausführt
- Antworten in einem standardisierten Format zurückgibt

Beispiele:

- `GET /api/products` = Produkte abrufen
- `GET /api/products/5` = ein Produkt abrufen
- `POST /api/products` = neues Produkt erstellen
- `DELETE /api/products/5` = löschen

## Wichtige REST-Merkmale

### 1. Ressourcenorientierung

Wir modellieren nicht "Befehle", sondern Ressourcen.

### 2. Stateless-Betrieb

Jede Anfrage ist für sich allein interpretierbar.

### 3. Einheitliche Schnittstelle

Die konsequente Verwendung von HTTP-Methoden und Statuscodes ist wichtig.

### 4. Schichtenarchitektur

Der Client muss nicht unbedingt wissen, welche Schichten zwischen ihm und dem Server liegen.

## REST und "einfaches HTTP API": nicht verwechseln

Nicht jede über HTTP funktionierende JSON-API wird automatisch REST.

Damit es REST-artig ist, braucht man:

- ein gutes Ressourcenmodell
- konsequente URIs
- korrekte HTTP-Semantik
- Stateless-Denkweise

## REST und SOAP: nicht verwechseln

| Aspekt | REST API | SOAP |
|---|---|---|
| Art | Architekturstil | Protokoll |
| Datenaustausch | häufig JSON | typischerweise XML |
| Einsatz | webnäher, leichter | strenger, formaler |

## Worauf muss man achten?

- `GET` sollte eine Abfrage sein und keine versteckte Änderung durchführen.
- HTTP-Statuscodes sollten konsequent verwendet werden.
- Endpointnamen sollten ressourcenbasiert sein.
- Die API sollte dokumentiert und vorhersagbar sein.

## Prüfungstaugliche Formulierung

> Eine REST API ist eine webbasierte Programmierungsschnittstelle, die den REST-Architekturprinzipien folgt.  
> Sie identifiziert Ressourcen mit URIs und führt Operationen mit standardisierten HTTP-Methoden aus.  
> Kennzeichnend sind der zustandslose Betrieb, die einheitliche Schnittstelle und der häufige JSON-basierte Datenaustausch.

## Häufige Prüfungsfehler

- REST als Protokoll bezeichnen.
- Behaupten, jede JSON-API sei REST.
- Den Stateless-Betrieb nicht erwähnen.
- Die Rolle der HTTP-Methoden auslassen.

## Schnelle Selbstkontrolle

1. Was ist der Kern von REST?
2. Was ist ein Hauptmerkmal einer REST API?
3. Wofür werden `GET` und `POST` typischerweise verwendet?
4. Warum ist der Stateless-Betrieb wichtig?
5. Was ist der Unterschied zwischen REST und SOAP?

## Kurzantworten zur Selbstkontrolle

1. Ressourcenbasierte, webnahe Architektur
2. Verwendung von URIs und HTTP-Methoden
3. `GET` ruft ab, `POST` erstellt
4. Weil jede Anfrage eigenständig interpretierbar ist
5. REST ist ein Stil, SOAP ein Protokoll

## Quellen

1. Roy Fielding - Architectural Styles and the Design of Network-based Software Architectures,  
   Chapter 5: Representational State Transfer (REST)  
   https://roy.gbiv.com/pubs/dissertation/rest_arch_style.htm  
   Verwendung: der originale REST-Architekturhintergrund.

2. MDN - REST  
   https://developer.mozilla.org/en-US/docs/Glossary/REST  
   Verwendung: kurze Entwicklerzusammenfassung des REST-Begriffs.

3. RFC 9110 - HTTP Semantics  
   https://www.rfc-editor.org/rfc/rfc9110  
   Verwendung: offizieller Standardhintergrund zu HTTP-Methoden und Semantik.

Abgerufen: `2026-04-08`
