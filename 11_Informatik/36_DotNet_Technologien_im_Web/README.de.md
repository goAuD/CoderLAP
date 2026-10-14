# DotNet Technologien im Web

## Schneller visueller Überblick

| Technologie | Rolle |
|---|---|
| ASP.NET Core | moderne Web-Basisplattform |
| Web API | HTTP/REST-Backend |
| Blazor | C#-basierte Web-UI-Entwicklung |
| SignalR | Echtzeitkommunikation |

## Wofür wird .NET im Web verwendet?

- für Backend-Dienste
- für die Erstellung von REST-APIs
- für Unternehmens-Webanwendungen
- für Echtzeit-Webfunktionen
- in bestimmten Fällen auch für vollständige Web-UI-Lösungen

## Was ist die heutige Hauptrichtung?

Die heutige zentrale Richtung ist `.NET` und `ASP.NET Core`, weil es:

- modern ist
- Cross-Platform ist
- hohe Leistung bietet
- über gutes Tooling verfügt

## Wichtige Web-Technologien in .NET

### ASP.NET Core

- Grundlage für Webapps und APIs

### Web API

- serverseitige Endpunkte
- Bedienung von Frontend oder externen Systemen

### Blazor

- C#-basiertes Komponentenmodell für Web-UI

### SignalR

- Echtzeitkommunikation
- Chat, Live-Updates, Push-ähnliche Lösungen

## .NET und Java: nicht verwechseln

| Begriff | Bedeutung |
|---|---|
| .NET | Microsoft-Ökosystem, typischerweise mit C# |
| Java | separate Plattform und Ökosystem |

## Worauf muss man achten?

- Die moderne Web-.NET-Hauptrichtung ist `ASP.NET Core`.
- Das ältere `ASP.NET` und das heutige `ASP.NET Core` sind nicht dasselbe.
- In der Prüfung sollte man auch die Rolle von API, Webapp und Echtzeitkommunikation erwähnen.

## Ein minimaler HTTP-Endpunkt und der Ausführungsort

**Umgebung:** Leeres ASP.NET-Core-10-Webprojekt, installiertes .NET-10-SDK und
die standardmäßigen impliziten Imports der Webvorlage. Der folgende Code ist
die vollständige `Program.cs`; Projektdatei und SDK werden weiterhin benötigt.
Rufe nach dem Start `/api/course` unter der ausgegebenen lokalen Adresse auf.
Erwartet werden `200 OK`, der JSON-Medientyp und dieser Dateninhalt:

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/api/course", () => new { id = 15, title = "Schleifen" });

app.Run();
```

```json
{"id":15,"title":"Schleifen"}
```

`CreateBuilder` stellt Dienste und Konfiguration zusammen. `MapGet` verbindet
einen GET-Pfad mit einem Handler. Das Framework serialisiert das Objekt als
JSON, `app.Run()` startet die Verarbeitung. Das Beispiel liefert feste,
öffentliche Daten und ist keine fertige authentifizierte Datenbank-API.

| Blazor-Modus | Wo läuft der .NET-Code für die Interaktion? |
|---|---|
| Static Server | Server erzeugt HTML; keine automatische interaktive Blazor-Verarbeitung |
| Interactive Server | auf dem Server über eine Echtzeitverbindung zum Browser |
| Interactive WebAssembly | in der heruntergeladenen Clientanwendung im Browser |
| Interactive Auto | zuerst auf dem Server, bei späteren Besuchen auch im heruntergeladenen Client |

Deshalb beschreiben weder „Bei Blazor läuft alles C# auf dem Server“ noch
„Blazor ist immer WebAssembly“ alle Modi. Servergeheimnisse gehören nicht in
Clientcode; API-Berechtigungen prüft weiterhin der Server. SignalR unterstützt
aktive Echtzeitverbindungen und ist nicht dasselbe wie eine Betriebssystem-
Push-Benachrichtigung an eine geschlossene Anwendung. Modernes .NET und ASP.NET
Core unterstützen mehrere Plattformen. Das ältere, Windows-orientierte
.NET Framework ist eine getrennte Produktlinie.

## Prüfungstaugliche Formulierung

> Zu den Web-Technologien von .NET gehören jene Lösungen,
> mit denen Webanwendungen, Backends und APIs
> im Microsoft-Ökosystem entwickelt werden können.
> Die heutige Hauptrichtung ist ASP.NET Core, das eine moderne, plattformübergreifende und leistungsstarke Grundlage bietet.
> Dazu gehören beispielsweise auch Web API, Blazor und SignalR.

## Schnelle Selbstkontrolle

1. Was ist die heutige Haupt-.NET-Webplattform?
2. Wofür dient Web API?
3. Wofür dient SignalR?
4. Warum ist Blazor wichtig?
5. Warum ist .NET im Web stark?

## Kurzantworten zur Selbstkontrolle

1. ASP.NET Core
2. Für die Erstellung von HTTP-Endpunkten und APIs
3. Für Echtzeitkommunikation
4. Es ermöglicht C#-basierte Web-UI-Entwicklung
5. Weil es modern, schnell ist und ein gutes Ökosystem hat

## Quellen

Geprüft: `2026-10-14`.

- [Microsoft: ASP.NET Core APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/apis?view=aspnetcore-10.0): Minimal API und HTTP-Handler.
- [Microsoft: Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0): Serverseitige und clientseitige Ausführung.


1. ASP.NET Web Apps
   https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps
   Verwendung: offizieller Überblick über das .NET-Web-Ökosystem.

2. ASP.NET documentation
   https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-10.0
   Verwendung: offizielle Dokumentation des modernen ASP.NET Core.

3. Blazor
   https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor
   Verwendung: offizielle Quelle zur C#-basierten Web-UI-Technologie.

4. SignalR
   https://dotnet.microsoft.com/en-us/apps/aspnet/signalr
   Verwendung: offizielle Quelle zur Echtzeit-Webkommunikation.

Abgerufen: `2026-04-08`
