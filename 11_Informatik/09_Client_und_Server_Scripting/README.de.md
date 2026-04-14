# Client und Server Scripting

## Schneller visueller Überblick

| Typ | Wo läuft es? | Wofür ist es gut? |
|---|---|---|
| Client-side Scripting | im Browser | Formularvalidierung, Interaktion, DOM-Manipulation |
| Server-side Scripting | auf dem Server | Datenverarbeitung, Datenbankzugriff, Autorisierung |

## Was ist clientseitiges Scripting?

Dieser Code läuft im Browser des Benutzers.

Typischerweise:

- `JavaScript`
- DOM-Manipulation
- Verarbeitung von Klicks
- Formularvalidierung
- dynamische Oberflächen

Vorteile:

- schnelle Rückmeldung an den Benutzer
- interaktives Erlebnis
- weniger Seitenneuladungen

Einschränkungen:

- läuft in der Umgebung des Benutzers
- kann nicht als vollständig vertrauenswürdig betrachtet werden
- sensible Daten und endgültige Prüfungen dürfen nicht nur hier bleiben

## Was ist serverseitiges Scripting?

Dieser Code läuft auf dem Webserver.

Typische Aufgaben:

- Geschäftslogik
- Datenbankabfragen
- Anmeldung und Berechtigungsverwaltung
- Bestellverarbeitung
- Erzeugung von API-Antworten

Typische Technologien:

- `PHP`
- `Node.js`
- `Python`
- `Java`
- `.NET`

## Der Weg einer einfachen Anfrage

1. Der Browser sendet eine HTTP-Anfrage.
2. Der serverseitige Code verarbeitet sie.
3. Bei Bedarf wird eine Datenbank verwendet.
4. Der Server sendet HTML, JSON oder eine andere Antwort.
5. Der clientseitige Code zeigt dies an oder verarbeitet es weiter.

## Warum braucht man beides?

Weil die Rollen unterschiedlich sind.

### Clientseite

- Benutzererlebnis
- visuelle Dynamik
- sofortige Reaktion

### Serverseite

- zentrale Datenverwaltung
- Sicherheit
- Ausführung von Geschäftsregeln
- gleichzeitige Bedienung mehrerer Benutzer

## Nicht verwechseln

| Begriff | Was bedeutet das? |
|---|---|
| Client-side | läuft im Browser |
| Server-side | läuft auf dem Server |
| dynamische Seite | kann sowohl client- als auch serverseitig dynamisch sein |
| Validierung | clientseitig als Komfort, serverseitig als obligatorische Endprüfung |

## Worauf muss man achten?

- Clientseitige Prüfung allein ist keine Sicherheit.
- Auf dem Server muss die Eingabe immer erneut geprüft werden.
- Eine gute Webanwendung nutzt in der Regel beide Seiten.
- Das Gleichgewicht zwischen Benutzererlebnis und Sicherheit ist wichtig.

## Prüfungstaugliche Formulierung

> Clientseitiges Scripting läuft im Browser des Benutzers
> und ist hauptsächlich
> für die interaktive Funktionalität der Oberfläche verantwortlich.  
> Serverseitiges Scripting läuft auf dem Server
> und übernimmt die Geschäftslogik, die Datenverwaltung,
> die Authentifizierung und die Erzeugung der Antwort.  
> Eine moderne Webanwendung verwendet typischerweise beide Ansätze gemeinsam.

## Häufige Prüfungsfehler

- Behaupten, dass jedes JavaScript nur clientseitig sein kann.
- Clientseitige Validierung als ausreichende Sicherheitslösung betrachten.
- Die dynamische Seite ausschließlich als serverseitigen Begriff bezeichnen.
- Die Datenbank- und Berechtigungsverwaltung auf der Serverseite nicht erwähnen.

## Schnelle Selbstkontrolle

1. Wo läuft clientseitiges Scripting?
2. Wo läuft serverseitiges Scripting?
3. Warum muss die Eingabe auch serverseitig geprüft werden?
4. Nenne zwei clientseitige und zwei serverseitige Aufgaben.
5. Kann eine Seite auf beiden Seiten dynamisch sein?

## Kurzantworten zur Selbstkontrolle

1. Im Browser
2. Auf dem Server
3. Weil der Client nicht vollständig vertrauenswürdig ist
4. Client: DOM, Formularvalidierung. Server: Datenbank, Authentifizierung
5. Ja

## Quellen

1. MDN - Introduction to the server side  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction  
   Verwendung: Rolle und Stelle der serverseitigen Verarbeitung im Web-Request-Response-Modell.

2. MDN - Client-side web APIs  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction  
   Verwendung: clientseitige Funktionsweise, browserseitige Programmierumgebung und Interaktion.

3. Node.js - Introduction to Node.js  
   https://nodejs.org/en/learn/getting-started/introduction-to-nodejs  
   Verwendung: offizielles Beispiel und Funktionsmodell für serverseitiges JavaScript.

Abgerufen: `2026-04-08`
