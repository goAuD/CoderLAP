# Cross Plattform Entwicklung

## Gyors vizuális kép

| Megközelítés | Lényege |
|---|---|
| natív | minden platformra külön megoldás |
| cross-platform | közös vagy részben közös kód |

## Miért jó?

- kevesebb duplikált fejlesztés
- gyorsabb piacra jutás
- könnyebb több platformot egyszerre támogatni
- kisebb csapat is többet lefedhet

## Hol használják?

- mobilappoknál
- desktop + mobil kombinációknál
- többeszközös termékeknél

## Tipikus technológiák

- `Flutter`
- `React Native`
- `.NET MAUI`

## Milyen kompromisszumok vannak?

- nem mindig érjük el a teljes natív élményt
- bizonyos platformspecifikus funkciók nehezebbek
- teljesítménybeli eltérések előfordulhatnak
- néha külön platformkód is kell

## Cross-platform és reszponzív web: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| cross-platform app fejlesztés | több platformra készülő alkalmazás |
| reszponzív web | egy weboldal alkalmazkodik a képernyőhöz |

## Mikor jó választás?

- ha több platformot kell gyorsan lefedni
- ha a költség és fejlesztési idő erősen számít
- ha a funkciók nagy része platformfüggetlen

## Mikor kevésbé jó?

- ha nagyon mély natív integráció kell
- ha platformspecifikus UI a kulcs
- ha a maximális teljesítmény elsődleges

## Mit osztunk meg, és mit ellenőrzünk platformonként?

Egy kvíz pontszámítása és a kérdések adatmodellje jól megosztható. A képernyő,
a helyi tárolás, az értesítés és a vissza gomb viselkedése viszont platformonként
eltérhet. Érdemes a közös szabályt a platform API-jától elválasztani:

```text
gemeinsame Quizlogik
  -> abstrakte Speicheroperation
     -> Web: Browser-Speicher
     -> Android/iOS: passende lokale Speicher-API
```

Ez szemléltető rétegzés, nem kötelező új framework. Két kis, világos
platformfüggő fájl egyszerűbb lehet, mint egy mindent feltételes ágakkal kezelő
óriásfüggvény. React Native például `.ios` és `.android` fájlváltozatokat is
kezel, így a hívó közös felületet használhat.

| Ellenőrzés | Miért kell ugyanannál a funkciónál is? |
|---|---|
| fájlnév és útvonal | kis- és nagybetűk kezelése fájlrendszerenként eltérhet |
| UTF-8 és sortörés | ékezetes export és különböző rendszerekből érkező szöveg |
| időpont | időzóna és nyári időszámítás befolyásolja a helyi megjelenítést |
| jogosultság megtagadása | a kamera vagy értesítés nélkül is érthető állapot kell |
| billentyűzet és navigáció | a mobil billentyűzet, visszalépés és desktop-fókusz eltér |
| gyenge eszköz és kapcsolat | valós teljesítményt mérünk, nem a framework nevét |

Node.js-ben fájlrendszerutakhoz a `node:path` platformnak megfelelő eszközeit
használjuk; egy HTTP-URL-t viszont nem fájlrendszerútként állítunk össze.
A cross-platform megoldás nem szükségszerűen lassú, és a natív megoldás sem
automatikusan gyors. A konkrét terhelés, implementáció és mérés dönt. Egy webapp
is lehet több platformon használható; a reszponzivitás ezen belül az elrendezés
alkalmazkodását jelenti, nem az összes platformkülönbség megoldását.

## Vizsgán jól használható megfogalmazás

> A cross-platform fejlesztés célja,
> hogy egy közös vagy nagyrészt közös kódbázisból
> több platformra is tudjunk alkalmazást készíteni.  
> Előnye a gyorsabb fejlesztés és a kisebb duplikáció,
> hátránya pedig az,
> hogy bizonyos esetekben kompromisszumot kell kötni
> a natív élmény, a teljesítmény
> vagy a platformspecifikus funkciók terén.  
> Tipikus példák a Flutter, a React Native és a .NET MAUI.

## Gyors önellenőrzés

1. Mi a cross-platform fejlesztés lényege?
2. Mi az egyik fő előnye?
3. Mi az egyik fő hátránya?
4. Mondj három tipikus technológiát.
5. Miben más, mint a reszponzív web?

## Rövid válaszok az önellenőrzéshez

1. Több platformra közös kódbázissal fejlesztünk
2. Kisebb duplikáció és gyorsabb fejlesztés
3. Kompromisszum a natív élmény vagy funkciók terén
4. Flutter, React Native, .NET MAUI
5. A cross-platform több platform támogatása, a responsive ennek webes elrendezési kérdését kezeli

## Források

Ellenőrizve: `2026-10-14`.

- [React Native: Platform-specific code](https://reactnative.dev/docs/platform-specific-code): közös és eltérő platformkód kezelése.
- [Node.js: Path](https://nodejs.org/api/path.html): Windows- és POSIX-fájlutak eltérő kezelése.


1. Flutter  
   https://flutter.dev/  
   Használat: hivatalos cross-platform fejlesztési platform.

2. React Native  
   https://reactnative.dev/  
   Használat: hivatalos JavaScript/TypeScript-alapú cross-platform mobilos technológia.

3. .NET MAUI  
   https://dotnet.microsoft.com/en-us/apps/maui  
   Használat: hivatalos .NET-es többplatformos fejlesztési irány.

Megnyitva: `2026-04-08`
