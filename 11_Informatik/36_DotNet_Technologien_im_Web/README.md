# DotNet Technologien im Web

## Gyors vizuális kép

| Technológia | Szerep |
|---|---|
| ASP.NET Core | modern webes alapplatform |
| Web API | HTTP/REST backend |
| Blazor | C# alapú web UI-fejlesztés |
| SignalR | valós idejű kommunikáció |

## Mire használják a .NET-et a weben?

- backend szolgáltatásokra
- REST API-k készítésére
- vállalati webalkalmazásokra
- valós idejű webes funkciókra
- bizonyos esetekben teljes webes UI megoldásokra is

## Mi a fő modern irány?

A mai központi irány a `.NET` és `ASP.NET Core`, mert:

- modern
- cross-platform
- nagy teljesítményű
- jó toolinggal rendelkezik

## Fontos webes technológiák .NET-ben

### ASP.NET Core

- webappok és API-k alapja

### Web API

- szerveroldali végpontok
- frontend vagy külső rendszerek kiszolgálása

### Blazor

- C#-alapú komponensmodell webes UI-hoz

### SignalR

- valós idejű kommunikáció
- chat, élő frissítés, push jellegű megoldások

## .NET és Java: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| .NET | Microsoft ökoszisztéma, jellemzően C#-val |
| Java | külön platform és ökoszisztéma |

## Mire kell figyelni?

- A modern webes .NET fő iránya az `ASP.NET Core`.
- A régebbi `ASP.NET` és a mai `ASP.NET Core` nem ugyanaz.
- Vizsgán érdemes megemlíteni az API, webapp és valós idejű kommunikáció szerepét is.

## Minimális HTTP-végpont és a futtatás helye

**Környezet:** ASP.NET Core 10 üres webprojekt, telepített .NET 10 SDK-val,
a websablon alapértelmezett implicit importjaival. A következő a teljes
`Program.cs` tartalma; a projektfájl és az SDK továbbra is szükséges.
Indítás után az alkalmazás által kiírt helyi címen kérd le az `/api/course`
útvonalat. A várt eredmény `200 OK`, JSON médiatípus és az alábbi adattartalom:

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/api/course", () => new { id = 15, title = "Schleifen" });

app.Run();
```

```json
{"id":15,"title":"Schleifen"}
```

A `CreateBuilder` összeállítja az alkalmazás szolgáltatásait és konfigurációját.
A `MapGet` egy GET-útvonalhoz rendel kezelőt. Az objektumot a framework JSON-ná
alakítja; az `app.Run()` elindítja a kiszolgálást. A példa rögzített, nyilvános
adatot szolgáltat, nem kész hitelesített adatbázis-API.

| Blazor-mód | Hol történik az interakcióhoz tartozó .NET-kód futása? |
|---|---|
| Static Server | a szerver HTML-t készít; nincs automatikus interaktív Blazor-kezelés |
| Interactive Server | szerveren, a böngészővel valós idejű kapcsolaton át |
| Interactive WebAssembly | a letöltött kliensalkalmazásban, a böngészőben |
| Interactive Auto | kezdetben szerveren, későbbi látogatásnál a letöltött kliensben is |

Ezért a „Blazorban minden C# a szerveren fut” és a „Blazor mindig WebAssembly”
állítás sem írja le az összes módot. Kliensoldali kódba nem kerülhet szervertitok;
a szerver továbbra is ellenőrzi az API-jogosultságokat. SignalR élő kapcsolatot
segít kezelni, nem azonos egy bezárt alkalmazásnak küldött operációsrendszeres
push értesítéssel. A modern .NET és ASP.NET Core több platformot támogat;
a régi, Windows-központú .NET Framework ettől külön termékvonal.

## Vizsgán jól használható megfogalmazás

> A .NET webes technológiái közé tartoznak azok a megoldások,
> amelyekkel webalkalmazásokat, backendeket és API-kat
> fejleszthetünk a Microsoft ökoszisztémában.  
> A mai fő irány az ASP.NET Core, amely modern, cross-platform és nagy teljesítményű alapot ad.  
> Ehhez kapcsolódik például a Web API, a Blazor és a SignalR is.

## Gyors önellenőrzés

1. Mi a mai fő .NET-es webes platform?
2. Mire való a Web API?
3. Mire való a SignalR?
4. Miért fontos a Blazor?
5. Miért erős a .NET weben?

## Rövid válaszok az önellenőrzéshez

1. ASP.NET Core
2. HTTP végpontok és API-k készítésére
3. Valós idejű kommunikációra
4. C#-alapú webes UI fejlesztést ad
5. Mert modern, gyors és jó ökoszisztémája van

## Források

Ellenőrizve: `2026-10-14`.

- [Microsoft: ASP.NET Core APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/apis?view=aspnetcore-10.0): Minimal API és HTTP-kezelő.
- [Microsoft: Blazor render modes](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/render-modes?view=aspnetcore-10.0): szerveroldali és kliensoldali végrehajtás.


1. ASP.NET Web Apps  
   https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps  
   Használat: a .NET webes ökoszisztéma hivatalos áttekintése.

2. ASP.NET documentation  
   https://learn.microsoft.com/en-us/aspnet/core/?view=aspnetcore-10.0  
   Használat: a modern ASP.NET Core hivatalos dokumentációja.

3. Blazor  
   https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor  
   Használat: hivatalos forrás a C#-alapú webes UI technológiához.

4. SignalR  
   https://dotnet.microsoft.com/en-us/apps/aspnet/signalr  
   Használat: hivatalos forrás a valós idejű webes kommunikációhoz.

Megnyitva: `2026-04-08`
