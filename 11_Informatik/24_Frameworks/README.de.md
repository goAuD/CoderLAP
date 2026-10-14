# Frameworks

## Schneller visueller Überblick

| Werkzeug | Was bietet es? |
|---|---|
| Library | fertige Funktionen |
| Framework | fertigen Arbeitsrahmen und Regeln dazu |

## Was ist ein Framework?

Ein Framework hilft dabei, eine bestimmte Art von Anwendung strukturiert aufzubauen.

Es bietet häufig:

- Projektstruktur
- Komponentenmodell
- Routing
- Datenverarbeitungsmuster
- Test- oder Build-Unterstützung

## Warum ist das gut?

- schnellerer Einstieg
- weniger sich wiederholende Grundarbeit
- einheitlicherer Code
- bessere Übersichtlichkeit bei größeren Projekten
- einfachere Teamarbeit

## Wo verwenden wir Frameworks?

- Frontend: z.B. `Angular`, `React`-Ökosystem, `Vue`
- Backend: z.B. `Spring`, `ASP.NET Core`, `Django`
- Mobil: z.B. `Flutter`, `React Native`

## Framework und Library: nicht verwechseln

| Begriff | Wesentlich |
|---|---|
| Library | du rufst ihre Funktionen auf |
| Framework | es bestimmt auch den Arbeitsrahmen |

Dazu sagt man häufig:

- Library: "du rufst sie"
- Framework: "es ruft dich" an bestimmten Stellen

## Worauf muss man achten?

- Ein Framework beschleunigt, hat aber Lernkosten.
- Keine gute Wahl blind aus Trend.
- Für kleinere Projekte kann es manchmal zu schwer sein.
- Man muss seine Konventionen kennen, sonst wird die Entwicklung mühsam.

## Wer steuert die Verarbeitung einer Anfrage?

In einem serverseitigen Framework kann `GET /courses/15` folgenden Weg nehmen:

1. Der Router findet den Endpunkt und liest den Parameter `id` aus.
2. Middleware oder Filter erledigen gemeinsame Aufgaben, etwa Authentifizierung.
3. Der eigene Handler prüft Eingabe und Berechtigung für den Kurs.
4. Die Service-/Datenzugriffsschicht lädt den Kurs.
5. Das Framework verwandelt den Rückgabewert in JSON oder erzeugt HTML aus einem
   Template.

Die Anwendung registriert ihren Handler; beim Eintreffen der Anfrage ruft das
Framework ihn auf. Dies ist ein Beispiel für **Inversion of Control**, die
Umkehrung der Steuerung. Eine Datumsformatierungsfunktion aus einer Library ruft
dagegen unser eigener Code an der benötigten Stelle auf. Die Unterscheidung
hängt nicht einfach von der Paketgröße ab.

Bei der Auswahl vergleichen wir für dieselbe konkrete Aufgabe Dokumentation,
unterstützte Laufzeit, Aktualisierungsmöglichkeiten, Lizenz und Teamwissen.
Für eine statische Informationsseite kann HTML/CSS genügen. Bei komplexen
Formularsystemen helfen fertige Validierungs- und Testwerkzeuge. Integrierte
Schutzfunktionen müssen trotzdem richtig konfiguriert werden. Das Framework
entscheidet nicht selbst, welche Person welches Lernergebnis lesen darf.

## Prüfungstaugliche Formulierung

> Ein Framework ist ein Rahmenwerk,
> das eine vorgefertigte Struktur, Werkzeuge und Regeln
> für die Anwendungsentwicklung bereitstellt.
> Der Vorteil ist,
> dass es eine schnellere, einheitlichere und besser organisierte Entwicklung ermöglicht,
> besonders bei größeren Projekten.
> Ein Framework ist mehr als eine einfache Library,
> weil es nicht nur Funktionen bereitstellt,
> sondern auch den Aufbau und die Arbeitsweise des Programms beeinflusst.

## Schnelle Selbstkontrolle

1. Was ist das Wesentliche eines Frameworks?
2. Was ist der Unterschied zur Library?
3. Nenne zwei Frontend- und zwei Backend-Beispiele.
4. Warum ist es bei Teamarbeit vorteilhaft?
5. Was kann der Nachteil sein?

## Kurzantworten zur Selbstkontrolle

1. Es bietet fertige Struktur und Regeln
2. Es steuert mehr von der Arbeitsweise
3. Frontend: Angular, Vue. Backend: Spring, ASP.NET Core
4. Es bietet einheitlichere Entwicklung
5. Lern- und Komplexitätsmehraufwand

## Quellen

Geprüft: `2026-10-14`.

- [MDN: Server-side web frameworks](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks): Routing, Middleware, Templates und Auswahlkriterien.


1. MDN - Server-side web frameworks
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks
   Verwendung: Rolle von Frameworks, Auswahlkriterien und Webkontext.

2. Spring - Web Applications
   https://spring.io/web-applications/
   Verwendung: Beispiel eines verbreiteten Backend-Framework-Ökosystems.

3. ASP.NET Web Apps
   https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps
   Verwendung: Beispiel einer modernen .NET-Web-Framework-Familie.

Abgerufen: `2026-04-08`
