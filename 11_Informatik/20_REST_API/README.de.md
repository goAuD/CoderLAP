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

- `GET` soll Lesen anfordern; begleitende Protokollierung ist möglich, fachliche Änderungen gehören nicht in diese Operation.
- HTTP-Statuscodes sollten konsequent verwendet werden.
- Endpointnamen sollten ressourcenbasiert sein.
- Die API sollte dokumentiert und vorhersagbar sein.

## HTTP-Vertrag und tatsächlicher Clientcode

Die Operationen einer möglichen Kurs-API unterscheiden wir so:

| Methode | Absicht und Wiederholung |
|---|---|
| `GET /courses/15` | lesen; der Client fordert keine fachliche Zustandsänderung an |
| `POST /courses` | hier anlegen; Wiederholung kann mehrere Datensätze erzeugen |
| `PUT /courses/15` | Zielzustand festlegen/ersetzen; idempotent |
| `PATCH /courses/15` | teilweise ändern; Idempotenz hängt von der Operation ab |
| `DELETE /courses/15` | entfernen; Wiederholung derselben Absicht ist idempotent |

Idempotenz betrifft die **beabsichtigte Wirkung**, nicht identische Antworten.
Ein zweites Löschen kann beispielsweise `404` liefern, während der Kurs weiterhin
fehlt. Bei erfolgreichem Anlegen sind `201` und `Location` üblich, bei Erfolg
ohne Antwortinhalt `204`. `401` betrifft Authentifizierung, `403` verweigerten
Zugriff. Jede Ressource benötigt serverseitige Berechtigungsprüfung.

**Browserbeispiel:** Es setzt einen funktionierenden gleichnamigen Endpunkt
`/api/courses/15` derselben Herkunft voraus, der mit `200` das JSON
`{"id":15,"title":"Schleifen"}` liefert. Ohne diesen Dienst ist es keine
eigenständige Demo. Erwartete Konsolenausgabe: `Schleifen`.

```javascript
async function loadCourse() {
  const response = await fetch("/api/courses/15", {
    headers: { Accept: "application/json" },
    signal: AbortSignal.timeout(5000),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const course = await response.json();
  if (course === null || typeof course !== "object" ||
      course.id !== 15 || typeof course.title !== "string") {
    throw new Error("Unexpected course data");
  }
  return course.title;
}
loadCourse().then(console.log).catch((error) => console.error(error.message));
```

`fetch` lehnt sein Promise allein wegen einer `404`-Antwort nicht ab. Deshalb
prüfen wir `ok`. Nach dem JSON-Parsing prüfen wir auch die erwarteten Daten.
Die Wartezeit ist auf fünf Sekunden begrenzt. Der Fehlerpfad behandelt Netz-,
HTTP- und Verarbeitungsfehler.

Zu REST gehören außerdem Cachefähigkeit, Client-Server-Trennung und eine
einheitliche Schnittstelle. Dazu zählen Ressourcenrepräsentationen und Links
zu möglichen nächsten Schritten. Code-on-Demand ist eine optionale REST-Bedingung.
Zustandslos bedeutet nicht, dass der Server keine Datenbank besitzt. Eine Anfrage
soll ohne verborgenes Wissen über vorherige Clientanfragen interpretierbar sein.

## Prüfungstaugliche Formulierung

> Eine REST API ist eine webbasierte Programmierungsschnittstelle, die den REST-Architekturprinzipien folgt.  
> Sie identifiziert Ressourcen mit URIs und führt Operationen mit standardisierten HTTP-Methoden aus.  
> Kennzeichnend sind der zustandslose Betrieb, die einheitliche Schnittstelle und der häufige JSON-basierte Datenaustausch.

## Schnelle Selbstkontrolle

1. Was ist der Kern von REST?
2. Was ist ein Hauptmerkmal einer REST API?
3. Wofür werden `GET` und `POST` typischerweise verwendet?
4. Warum ist der Stateless-Betrieb wichtig?
5. Was ist der Unterschied zwischen REST und SOAP?

## Kurzantworten zur Selbstkontrolle

1. Ressourcenbasierte, webnahe Architektur
2. Verwendung von URIs und HTTP-Methoden
3. `GET` liest, `POST` fordert Verarbeitung gemäß Ressourcenvertrag an, etwa das Anlegen
4. Weil jede Anfrage eigenständig interpretierbar ist
5. REST ist ein Stil, SOAP ein Protokoll

## Quellen

Geprüft: `2026-10-14`.

- [Fielding: REST](https://roy.gbiv.com/pubs/dissertation/rest_arch_style.htm): REST-Bedingungen und einheitliche Schnittstelle.
- [IETF: HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html): Methoden, Idempotenz und Status.
- [MDN: Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch): HTTP- und Verarbeitungsfehler unterscheiden.


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
