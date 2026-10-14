# Frameworks

## Gyors vizuális kép

| Eszköz | Mit ad? |
|---|---|
| library | kész funkciókat |
| framework | kész működési keretet és szabályokat is |

## Mi az a framework?

A framework segít abban, hogy egy adott típusú alkalmazást rendezett módon építsünk fel.

Gyakran ad:

- projektstruktúrát
- komponensmodellt
- routingot
- adatkezelési mintát
- tesztelési vagy build támogatást

## Miért jó?

- gyorsabb indulás
- kevesebb ismétlődő alapmunka
- egységesebb kód
- nagyobb projektnél jobb átláthatóság
- könnyebb csapatmunka

## Hol használunk frameworköket?

- frontend: pl. `Angular`, `React` ökoszisztéma, `Vue`
- backend: pl. `Spring`, `ASP.NET Core`, `Django`
- mobil: pl. `Flutter`, `React Native`

## Framework és library: ne keverd össze

| Fogalom | Lényeg |
|---|---|
| library | te hívod meg a funkcióit |
| framework | ő is meghatározza a működési keretet |

Erre gyakran azt mondják:

- library: "te hívod"
- framework: "ő hív téged" bizonyos pontokon

## Mire kell figyelni?

- A framework felgyorsít, de tanulási költsége van.
- Nem jó választás vakon divatból.
- Kisebb projekthez néha túl nehéz lehet.
- Ismerni kell a konvencióit, különben nehézkes lesz a fejlesztés.

## Ki irányítja a kérés feldolgozását?

Egy szerveroldali keretrendszerben a `GET /courses/15` útja például:

1. A router megtalálja a megfelelő végpontot, és kinyeri az `id` paramétert.
2. A middleware vagy filter elvégzi a közös feladatot, például a hitelesítést.
3. A saját kezelőfüggvény ellenőrzi a bemenetet és a kurzushoz való jogosultságot.
4. A szolgáltatás/adatelérési réteg betölti a kurzust.
5. A keretrendszer a visszaadott értéket JSON-ná vagy sablonból HTML-lé alakítja.

Az alkalmazás a kezelőt regisztrálja, de a kérés érkezésekor a keretrendszer
hívja meg. Ez a vezérlés megfordításának, az **inversion of controlnak** egy
példája. Egy külön dátumformázó library függvényét ezzel szemben a saját kódunk
hívja meg ott, ahol szüksége van rá. A határ nem pusztán a csomag mérete.

Választáskor ugyanarra a konkrét feladatra ellenőrizzük a dokumentációt,
támogatott futtatókörnyezetet, frissítési lehetőséget, licencet és a csapat
tudását. Egy statikus tájékoztatóhoz lehet, hogy elég a HTML/CSS, egy összetett
űrlapos rendszerhez a kész validálási és tesztelési eszközök sokat segítenek.
A keretrendszer beépített védelmeit is helyesen kell konfigurálni; nem dönti el
helyettünk, melyik tanuló melyik eredményt olvashatja.

## Vizsgán jól használható megfogalmazás

> A framework egy olyan keretrendszer,
> amely előre kialakított struktúrát, eszközöket és szabályokat
> biztosít az alkalmazásfejlesztéshez.  
> Előnye,
> hogy gyorsabb, egységesebb és jobban szervezett fejlesztést tesz lehetővé,
> különösen nagyobb projektek esetén.  
> A framework több, mint egy egyszerű library,
> mert nemcsak funkciókat ad,
> hanem a program felépítését és működési mintáját is befolyásolja.

## Gyors önellenőrzés

1. Mi a framework lényege?
2. Mi a különbség a libraryhoz képest?
3. Mondj két frontend és két backend példát.
4. Miért előnyös csapatmunkában?
5. Mi lehet a hátránya?

## Rövid válaszok az önellenőrzéshez

1. Kész szerkezetet és szabályokat ad
2. Többet irányít a működésből
3. Frontend: Angular, Vue. Backend: Spring, ASP.NET Core
4. Egységesebb fejlesztést ad
5. Tanulási és komplexitási többlet

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Server-side web frameworks](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks): routing, middleware, sablon és választási feltételek.


1. MDN - Server-side web frameworks  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Web_frameworks  
   Használat: keretrendszerek szerepe, választási szempontjai és webes kontextusa.

2. Spring - Web Applications  
   https://spring.io/web-applications/  
   Használat: példa egy elterjedt backend framework-ökoszisztémára.

3. ASP.NET Web Apps  
   https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps  
   Használat: példa egy modern .NET webes framework-családra.

Megnyitva: `2026-04-08`
