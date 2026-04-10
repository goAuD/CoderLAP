# Continuous Integration

## Gyors vizuális kép

| Lépés | Mi történik? |
|---|---|
| commit / PR | új kód érkezik |
| pipeline indul | automatikus ellenőrzés fut |
| build + test | kiderül, hogy működik-e |
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

## Vizsgán jól használható megfogalmazás

> A Continuous Integration célja, hogy a fejlesztők gyakran integrálják a kódjukat a közös rendszerbe, és az integrációt automatikus ellenőrzések kövessék.  
> Ilyenkor jellemzően build, teszt és más kódminőségi ellenőrzések futnak le.  
> A CI legnagyobb előnye, hogy gyorsan kiderülnek az integrációs hibák, így stabilabb marad a projekt.

## Gyakori vizsgahibák

- A CI-t összekeverni a deploymenttel.
- Nem megemlíteni az automatikus teszteket.
- Azt gondolni, hogy a CI csak nagy projektekhez kell.
- A gyors visszajelzés szerepét kihagyni.

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
