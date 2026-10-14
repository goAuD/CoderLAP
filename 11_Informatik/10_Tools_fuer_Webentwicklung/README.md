# Tools fuer Webentwicklung

## Gyors vizuális kép

| Eszközcsoport | Mire való? | Példa |
|---|---|---|
| editor / IDE | kódírás | VS Code |
| browser devtools | DOM, CSS, hálózat hibakeresése | Chrome DevTools |
| verziókezelés | változások követése | Git |
| package manager | csomagok telepítése | npm |
| local runtime / server | helyi futtatás | Node.js, PHP, XAMPP, Laragon |
| code quality tools | egységesség, hibák | ESLint, Prettier |

## Miért van szükség különféle eszközökre?

Mert a webfejlesztés nem csak kódírásból áll.

Tipikus munkafolyamat:

1. kód írása
2. helyi futtatás
3. böngészős ellenőrzés
4. hibakeresés
5. verziókövetés
6. csomagok kezelése
7. build vagy deploy előkészítése

## Fontos eszköztípusok

### 1. Kódszerkesztő vagy IDE

Feladata:

- kódírás
- szintaxiskiemelés
- fájlkezelés
- bővítmények
- hibajelzések

### 2. Böngésző fejlesztői eszközök

Feladata:

- HTML és DOM ellenőrzése
- CSS szabályok vizsgálata
- JavaScript hibák megfigyelése
- hálózati kérések elemzése
- teljesítmény figyelése

### 3. Verziókezelés

Feladata:

- változások nyomon követése
- visszaállíthatóság
- csapatmunka támogatása

### 4. Csomagkezelő

Feladata:

- függőségek telepítése
- script-ek futtatása
- projektkörnyezet egységesítése

### 5. Kódszabályozó eszközök

Feladata:

- hibák korai észlelése
- egységes formázás
- jobb olvashatóság

## Melyik mire jó a gyakorlatban?

| Helyzet | Hasznos eszköz |
|---|---|
| valami nem jól jelenik meg | DevTools |
| valami elromlott egy módosítás után | Git |
| hiányzik egy library | npm vagy más package manager |
| rendezetlen a kód | formatter, linter |
| helyben akarod kipróbálni | local server / runtime |

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| editor | főleg szerkesztésre szolgáló eszköz |
| IDE | komplexebb fejlesztői környezet |
| DevTools | böngészőbe épített hibakereső eszközök |
| Git | verziókezelő rendszer |
| npm | JavaScript-csomagkezelő és futtatási eszközök gyűjtője |

## Mire kell figyelni?

- Az eszköz nem helyettesíti a jó megértést.
- A túl sok plugin vagy tool fölösleges bonyolultságot adhat.
- Csapatban egységes toolchain kell.
- A verziókezelést nem szabad kihagyni.

## Egy hiba útja az eszközökön át

Tegyük fel, hogy egy oldal HTML-je megjelenik, de a formázása eltűnt.
Nem találomra írunk át CSS-t, hanem bizonyítékot keresünk:

1. A DevTools **Network** nézetében újratöltjük az oldalt. A CSS-kérés `404`
   válasza rossz útvonalra vagy hiányzó fájlra utal.
2. Ha a fájl megérkezett, az **Elements/Styles** megmutatja, illeszkedik-e a
   szelektor, és melyik szabály írja felül. A **Computed** a végső értéket mutatja.
3. A **Console** futásidejű JavaScript-hibát jelezhet, de a hibamentes konzol
   önmagában nem bizonyítja, hogy az elrendezés vagy az üzleti logika helyes.
4. A DevToolsban kipróbált javítást átvezetjük a forrásfájlba. A böngészőben
   végzett ideiglenes módosítás normál esetben újratöltéskor elveszik.

A formatter egységesíti a formát, a linter szabályokat ellenőriz, a típusellenőrző
típusszerződéseket vizsgál, a teszt konkrét viselkedést ellenőriz. Ezek egymást
kiegészítő eszközök. Verziókezelésnél a diff alapján azt is meg tudjuk mondani,
pontosan melyik változás oldotta meg a feladatot.

Node-projektben a rögzített lockfájl és az egyeztetett Node-verzió segíti az
azonos környezetet. Az `npm ci` a lockfájlhoz igazodó tiszta függőségtelepítés;
a meglévő `node_modules` könyvtárat újraépíti, ezért nem általános javítóparancs
minden böngészőhibára.

## Vizsgán jól használható megfogalmazás

> A webfejlesztéshez többféle eszköz szükséges:
> kódszerkesztő a fejlesztéshez,
> böngészőbe épített DevTools a hibakereséshez,
> verziókezelő a változások követéséhez,
> csomagkezelő a függőségek kezeléséhez,
> valamint helyi futtatási környezet
> és kódminőségi eszközök a stabil munkafolyamathoz.

## Gyors önellenőrzés

1. Mire jó a böngésző DevTools?
2. Miért fontos a Git?
3. Mire való egy package manager?
4. Miért kell helyi futtatási környezet?
5. Mi a linter és formatter szerepe?

## Rövid válaszok az önellenőrzéshez

1. Hibakeresésre és elemzésre
2. A változások követésére és csapatmunkára
3. Függőségek kezelésére
4. Hogy fejlesztés közben tesztelhessünk
5. Egységesebb és tisztább kódot adnak

## Források

Ellenőrizve: `2026-10-14`.

- [Chrome: JavaScript debugging](https://developer.chrome.com/docs/devtools/javascript): bizonyítékalapú hibakeresés és böngészős eszközök.
- [npm: npm ci](https://docs.npmjs.com/cli/commands/npm-ci/): lockfájl és tiszta telepítés.


1. Chrome for Developers - DevTools  
   https://developer.chrome.com/docs/devtools  
   Használat: hivatalos forrás a böngésző fejlesztői eszközeinek szerepéhez.

2. Visual Studio Code - Documentation  
   https://code.visualstudio.com/docs  
   Használat: hivatalos fejlesztői eszköz-dokumentáció a szerkesztő/IDE szerepéhez.

3. Git - Reference manual  
   https://git-scm.com/doc  
   Használat: hivatalos forrás a verziókezelés eszközoldalához.

4. npm Docs  
   https://docs.npmjs.com/  
   Használat: hivatalos forrás a csomagkezelés és projektfüggőségek témájához.

Megnyitva: `2026-04-08`
