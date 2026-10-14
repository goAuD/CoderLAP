# Continuous Integration

## Gyors vizuális kép

| Lépés | Mi történik? |
|---|---|
| commit / PR | új kód érkezik |
| pipeline indul | automatikus ellenőrzés fut |
| build + test | visszajelzést kapunk a buildről és a vizsgált viselkedésről |
| visszajelzés | gyorsan látszik a hiba |

## Mi a CI célja?

- minél hamarabb észrevenni az integrációs hibákat
- megelőzni, hogy sok külön fejlesztés későn akadjon össze
- automatizálni az alapellenőrzéseket

## Tipikus CI-feladatok

- build
- unit test
- lint
- statikus ellenőrzés
- csomagolás

## Miért jó?

- gyorsabb hibafelismerés
- stabilabb közös kód
- kevesebb "nálam működik" probléma
- könnyebb csapatmunka

## CI és CD: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| CI | kód rendszeres integrálása és automatikus ellenőrzése |
| CD | a szállítás vagy telepítés további automatizálása |

## Mire kell figyelni?

- A CI nem csak automatikus build.
- A teszteknek gyorsnak és megbízhatónak kell lenniük.
- A pipeline akkor hasznos, ha tényleg megállítja a hibás kódot.
- Érdemes kötelező ellenőrzéseket használni merge előtt.

## Egy változás útja a közös kódig

**Példa:** a pontszámítás megváltozik, a másik fejlesztő pedig az eredményt
megjelenítő képernyőt módosítja. Külön-külön mindkét branch működhet, mégis
eltérhetnek az elvárt adatmezők. A gyakori integrálás és a két részt együtt
ellenőrző teszt hamar megmutatja ezt az eltérést. A hetekig külön tartott
branchek napi automatikus buildje önmagában nem oldja meg az integrációt.

Egy **példabeli Node-projektben**, amelyben a `lint`, `test` és `build` scriptek
már szerepelnek a `package.json` fájlban, a CI lépései lehetnek:

```text
1. a vizsgált commit tiszta checkoutja
2. a rögzített Node-verzió beállítása
3. npm ci
4. npm run lint
5. npm test
6. npm run build
7. teszteredmények és build-artifact megőrzése
```

Az `npm ci` meglévő lockfile-ból telepít, és eltérés esetén nem írja át csendben
a függőséglistát. Ez javítja a megismételhetőséget; a platformot, futtatókörnyezetet
és külső szolgáltatásokat ettől még rögzíteni vagy ellenőrizni kell. A scriptek
itt egy tanulópélda részei, nem másolhatók automatikusan bármely repositoryba.

| Esemény | Helyes következő lépés |
|---|---|
| a teszt elvárt mezője hiányzik | az ellenőrzés sikertelen, a tesztelt kód javítása és új futtatás szükséges |
| új commit érkezik a PR-ba | az új tartalmat kell ellenőrizni |
| a célbranch közben változik | az együttműködést az aktuális célállapottal is vizsgáljuk |
| teszt néha ok nélkül piros | a bizonytalanság okát kivizsgáljuk, a puszta újrafuttatás nem javítás |

A cache gyorsíthat, de nem helyettesíti a helyes függőségeket vagy tesztet.
A pipeline eredménye csak a ténylegesen lefutott ellenőrzésekre bizonyíték.
A hibajelzést megőrző kilépési kód és a kötelező merge-ellenőrzés kapcsolja
össze a visszajelzést a csapat munkafolyamatával.

## Vizsgán jól használható megfogalmazás

> A Continuous Integration célja,
> hogy a fejlesztők gyakran integrálják a kódjukat a közös rendszerbe,
> és az integrációt automatikus ellenőrzések kövessék.  
> Ilyenkor jellemzően build, teszt és más kódminőségi ellenőrzések futnak le.  
> A CI legnagyobb előnye, hogy gyorsan kiderülnek az integrációs hibák, így stabilabb marad a projekt.

## Gyors önellenőrzés

1. Mi a CI lényege?
2. Milyen lépések futnak tipikusan a CI-ben?
3. Miért hasznos csapatmunkában?
4. Mi a különbség a CI és a CD között?
5. Miért fontos a gyors visszajelzés?

## Rövid válaszok az önellenőrzéshez

1. Gyakori integráció és automatikus ellenőrzés
2. Build, teszt, lint
3. Mert hamar kiderülnek az összeakadások
4. A CI ellenőriz, a CD továbbviszi a szállítást/telepítést
5. Mert olcsóbb korán javítani

## Források

Ellenőrizve: `2026-10-14`.

- [GitHub: Continuous integration](https://docs.github.com/en/actions/get-started/continuous-integration): gyakori integráció és automatizált visszajelzés.
- [npm: npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/): lockfile-alapú telepítés és eltérések kezelése.


1. GitHub Docs - About continuous integration  
   https://docs.github.com/en/actions/automating-builds-and-tests/about-continuous-integration  
   Használat: a CI fogalmának hivatalos, modern leírása.

2. GitHub Docs - Understanding GitHub Actions  
   https://docs.github.com/en/actions/get-started/understand-github-actions  
   Használat: gyakorlati példa arra, hogyan valósul meg CI pipeline modern eszközzel.

3. GitLab Docs - CI/CD  
   https://docs.gitlab.com/ee/ci/  
   Használat: másik nagy, hivatalos CI/CD platform szemléltető forrásként.

Megnyitva: `2026-04-08`
