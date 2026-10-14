# Programmiersprachen fuer mobile Apps und Internet

## Gyors vizuális kép

| Terület | Tipikus nyelvek |
|---|---|
| Android | `Kotlin`, részben `Java` |
| iOS | `Swift` |
| cross-platform mobil | `Dart`, `JavaScript` / `TypeScript`, `C#` |
| web frontend | `JavaScript`, `TypeScript` |
| web backend | `PHP`, `Java`, `C#`, `Python`, `JavaScript` |

## Mobilappokhoz használt nyelvek

### Natív Android

- `Kotlin`
- bizonyos esetekben `Java`

### Natív iOS

- `Swift`

### Cross-platform

- `Dart` `Flutter` környezetben
- `JavaScript` / `TypeScript` `React Native` környezetben
- `C#` `.NET MAUI` környezetben

## Internetes alkalmazásokhoz használt nyelvek

### Frontend

- `JavaScript`
- `TypeScript`

### Backend

- `PHP`
- `Java`
- `C#`
- `Python`
- `JavaScript` / `Node.js`

## Natív és cross-platform: ne keverd össze

| Megközelítés | Előny | Hátrány |
|---|---|---|
| natív | jobb platformintegráció | külön fejlesztés platformonként |
| cross-platform | közös kódbázis | lehetnek kompromisszumok |

## Mire kell figyelni?

- A nyelv önmagában nem minden, a framework és eszközlánc is számít.
- Mobilnál fontos a platformhoz illeszkedés.
- Internetes alkalmazásnál szét kell választani a frontendet és a backendet.
- Vizsgán érdemes kategóriákban gondolkodni, nem összevissza felsorolni.

## Egy szolgáltatás, többféle kliens

**Példa:** egy tanuló ugyanazt a témát jelöli megtanultnak Androidon, iPhone-on
vagy weben. A felület nyelve eltérhet, az adatcsere szerződése közös lehet.
A következő csak elképzelt API-szerződés, nem a jelenlegi oldal működése:

```http
PUT /api/me/progress/LAP-15-17 HTTP/1.1
Content-Type: application/json

{"completed":true}
```

A szerver a hitelesített munkamenetből állapítja meg, kinek a haladása változik;
a kliens által megadott tetszőleges felhasználóazonosító nem jogosultsági
bizonyíték. Az alkalmazásba nem építünk közvetlen adatbázis-jelszót. A mobilkliens
és a böngésző egyaránt szerveroldali API-n keresztül dolgozhat.

| Réteg | Egy lehetséges megoldás | Mit kell még megoldani? |
|---|---|---|
| Android-felület | Kotlin | platformnavigáció, jogosultságkérések, életciklus |
| iPhone-felület | Swift | platformnavigáció, jogosultságkérések, életciklus |
| közös mobilkód | Flutter/Dart vagy React Native/TypeScript | a platformonként eltérő részek és mindkét platform tesztje |
| webes felület | HTML/CSS és JavaScript | böngésző, billentyűzet, reszponzivitás |
| backend | például PHP vagy Java | hozzáférés, validálás, adatkezelés |

A TypeScriptet a szokásos webes eszközlánc JavaScriptre fordítja; a Node.js
futtatókörnyezet, nem külön nyelv. A cross-platform kódmegosztás mértéke
feladattól függ. Kamera, értesítés, offline állapot és bejelentkezés esetén
különösen fontos a tényleges eszközön végzett ellenőrzés. Egy PWA további
webes lehetőség, amelynek képességeit az adott böngésző és operációs rendszer
támogatása határozza meg.

## Vizsgán jól használható megfogalmazás

> Mobilappok és internetes alkalmazások fejlesztéséhez többféle programozási nyelvet használunk.  
> Natív Android fejlesztésben a Kotlin, natív iOS fejlesztésben a Swift jellemző.  
> Cross-platform mobilmegoldásoknál például a Dart `Flutter`-rel,
> illetve a JavaScript vagy TypeScript `React Native`-val használható.  
> Internetes alkalmazásoknál a frontend oldalon
> főleg JavaScript és TypeScript,
> a backend oldalon pedig például PHP, Java, C# vagy Python terjedt el.

## Gyors önellenőrzés

1. Melyik nyelv jellemző Androidra?
2. Melyik nyelv jellemző iOS-re?
3. Mondj két cross-platform mobilos irányt.
4. Melyik nyelvek jellemzők web frontendhez?
5. Melyik nyelvek jellemzők backendhez?

## Rövid válaszok az önellenőrzéshez

1. Kotlin
2. Swift
3. Flutter/Dart és React Native/JS-TS
4. JavaScript és TypeScript
5. Például PHP, Java, C#, Python

## Források

Ellenőrizve: `2026-10-14`.

- [Android Developers: Kotlin-first](https://developer.android.com/kotlin/first): Android-fejlesztési irány.
- [Apple: Swift](https://developer.apple.com/swift/): Swift és az Apple platformok.
- [React Native: Platform-specific code](https://reactnative.dev/docs/platform-specific-code): megosztott és platformfüggő kód elkülönítése.


1. Android Developers - Kotlin for Android  
   https://developer.android.com/kotlin/first  
   Használat: hivatalos Android-forrás a Kotlin kiemelt szerepéhez.

2. Apple - Swift  
   https://developer.apple.com/swift/  
   Használat: hivatalos forrás a Swift iOS-fejlesztési szerepéhez.

3. Flutter  
   https://flutter.dev/  
   Használat: hivatalos cross-platform mobil- és többplatformos fejlesztési forrás.

4. React Native  
   https://reactnative.dev/  
   Használat: hivatalos forrás a JavaScript/TypeScript-alapú mobilfejlesztéshez.

5. .NET MAUI  
   https://dotnet.microsoft.com/en-us/apps/maui  
   Használat: hivatalos forrás a C#-alapú cross-platform app fejlesztéshez.

Megnyitva: `2026-04-08`
