# Java Technologien im Web

## Schneller visueller Überblick

| Technologie | Rolle |
|---|---|
| Servlet | Verarbeitung von HTTP-Anfragen |
| JSP / Jakarta Pages | gepflegte serverseitige Vorlagentechnologie |
| Spring Boot | moderne Java-Backend- und Webapp-Entwicklung |
| Jakarta EE | Enterprise-Java-Plattform |

## Wofür wird Java im Web verwendet?

- Erstellung von Backend-APIs
- Umsetzung von Geschäftslogik
- für größere Unternehmenssysteme
- für skalierbare serverseitige Anwendungen

## Historische und moderne Schichten

### Klassische, weiterhin gepflegte Grundlagen

- `Servlet`
- `JSP`

Diese serverseitigen Technologien existieren weiterhin; ihre Rolle und Nutzung hängen vom Projekt ab.

### Heutige typische Richtungen

- `Spring Boot`
- `Jakarta EE`
- REST-APIs
- Microservice-basierte Backends

## Warum ist Java im Web stark?

- stabiles, ausgereiftes Ökosystem
- in vielen Unternehmensumgebungen bewährt
- gute Framework-Unterstützung
- starkes Tooling und große Community

## Java und JavaScript: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| Java | allgemeine Programmiersprache, starke Backend-Präsenz |
| JavaScript | primär Web-Scripting-Sprache, Frontend und heute auch viel Backend |

## Worauf muss man achten?

- Die Webrolle von Java ist hauptsächlich auf der Backend-Seite stark.
- `JSP` wird als Jakarta Pages weiterhin gepflegt; die passende Ansichtstechnologie hängt vom Projekt ab.
- In der Prüfung sollte man ältere und heutige Technologien getrennt besprechen.

## Der Weg einer Java-Webanfrage und die heutige Rolle von Servlet

```text
Browser: GET /api/course
  -> Webserver / Servlet-Container
  -> Spring-Controller
  -> Java-Objekt
  -> JSON-Antwort
```

**Illustrativer Controller:** Er gehört in das Paket `example.learning` eines
bereits angelegten Spring-Boot-Web-MVC-Projekts mit kompatiblem JDK. Der
Component-Scan muss dieses Paket erreichen; die übliche JSON-Serialisierung
muss konfiguriert sein. Allein ist dies noch kein startfähiges Projekt.
Für `GET /api/course` erwarten wir `200 OK` mit dem folgenden JSON-Inhalt:

```java
package example.learning;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CourseController {
    public record Course(int id, String title) {}

    @GetMapping("/api/course")
    public Course course() {
        return new Course(15, "Schleifen");
    }
}
```

```json
{"id":15,"title":"Schleifen"}
```

`GetMapping` verbindet den Pfad mit der Methode. Wegen `RestController`
serialisiert das Framework den zurückgegebenen Record als Antwortdaten.
Der Browser erhält JSON und führt keine Java-Klasse aus. Das Beispiel liefert
feste öffentliche Daten, ohne Datenbank, Anmeldung oder Berechtigungsprüfung.

Servlet ist nicht nur eine historische Grundlage: Jakarta Servlet ist eine
weiterentwickelte serverseitige API. JSP heißt heute **Jakarta Pages** und ist
ebenfalls eine gepflegte Spezifikation; aus einer Vorlage entsteht ein Servlet.
Je nach Aufgabe wählen wir eine solche Serveransicht oder eine JSON-API mit
getrenntem Frontend. Spring Web MVC baut auf Servlet auf, aber nicht jede
Java-Weblösung verwendet Servlet.

Seit Jakarta EE 9 heißen die betroffenen Unternehmens-APIs `jakarta.*` statt
`javax.*`. Beim Migrieren älterer Abhängigkeiten prüfen wir deshalb Quelltext,
Server und Libraries gemeinsam. Nicht alle `javax.*`-Pakete von Java SE wurden
umbenannt. Auch ein gut strukturierter Monolith kann ein geeignetes Java-Backend
sein; Java verlangt keine Aufteilung in Microservices.

## Prüfungstaugliche Formulierung

> Die Web-Technologien von Java dienen hauptsächlich
> der Entwicklung serverseitiger Anwendungen,
> Backend-Services und Unternehmens-Websysteme.
> Zu den klassischen Grundlagen gehören Servlet und JSP,
> während in der modernen Praxis Spring Boot und Jakarta EE
> zu den wichtigsten Richtungen zählen.
> Java ist besonders stark in den Bereichen Stabilität, Skalierbarkeit und Enterprise-Einsatz.

## Schnelle Selbstkontrolle

1. Wofür wird Java im Web verwendet?
2. Welche sind die klassischen Java-Web-Grundlagen?
3. Welche sind die modernen Richtungen?
4. Warum ist Java im Enterprise-Bereich stark?
5. Was ist der Unterschied zwischen Java und JavaScript?

## Kurzantworten zur Selbstkontrolle

1. Hauptsächlich für Backend- und serverseitige Webentwicklung
2. Servlet und JSP
3. Spring Boot und Jakarta EE
4. Wegen des stabilen Ökosystems und der guten Skalierbarkeit
5. Zwei verschiedene Sprachen mit unterschiedlichen Hauptrollen

## Quellen

Geprüft: `2026-10-14`.

- [Spring: Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/): Controller, JSON-Antwort und Voraussetzungen eines vollständigen Beispielprojekts.
- [Jakarta Servlet](https://jakarta.ee/specifications/servlet/): Aktive Servlet-Spezifikation.
- [Jakarta Pages](https://jakarta.ee/specifications/pages/): Gepflegter Name und Funktionsweise von JSP.
- [Jakarta EE FAQ](https://jakarta.ee/about/faq/): Namespace-Wechsel mit EE 9.


1. Oracle Java
   https://www.oracle.com/java/
   Verwendung: offizielle Plattformquelle von Java.

2. Spring - Web Applications
   https://spring.io/web-applications/
   Verwendung: modernes Java-Web-Entwicklungsökosystem.

3. Spring Guide - Serving Web Content
   https://spring.io/guides/gs/serving-web-content/
   Verwendung: praktisches Beispiel einer Java-basierten Webanwendung.

4. Jakarta EE Learn
   https://jakarta.ee/learn/
   Verwendung: offizieller Enterprise-Java-Web-Hintergrund.

Abgerufen: `2026-04-08`
