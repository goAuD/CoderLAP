# Einsatzgebiet Bootstrap

## Gyors vizuális kép

| Mire jó? | Példa |
|---|---|
| grid és breakpoints | reszponzív oszloprendszer |
| kész UI-elemek | gomb, navbar, modal |
| utility classok | spacing, display, flex |
| gyors indulás | kevés saját CSS-sel is használható |

## Mi a Bootstrap fő szerepe?

A Bootstrap célja, hogy gyorsan lehessen:

- rendezett layoutot építeni
- egységes kinézetű komponenseket használni
- reszponzívan kialakítani az oldalt

## Mikor hasznos?

- ha gyorsan kell működő felület
- ha fontos az egységesség
- ha kis vagy közepes projektnél nem akarsz mindent nulláról felépíteni
- admin vagy belső rendszerekhez
- MVP vagy prototípus készítéshez

## Tipikus elemei

- grid rendszer
- breakpointok
- form elemek
- navbar
- modal
- utility classok

## Előnyei

- gyors fejlesztés
- sok kész elem
- jó dokumentáció
- reszponzív alapok
- széles körben ismert

## Hátrányai

- könnyen "bootstrapos" kinézet lesz
- túl sok kész osztály átláthatatlanná válhat
- egyedi designnál sok felülírás kellhet

## Bootstrap és CSS: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| CSS | általános stílusnyelv |
| Bootstrap | CSS-re és komponensekre épülő keretrendszer |

## Egy és két oszlop ugyanabból a HTML-ből

**Környezet:** HTML-oldal, betöltött Bootstrap 5.3 CSS-sel. A részlethez JavaScript
nem szükséges. A CSS helyi fájlból is kiszolgálható; CDN használata nem feltétel.

```html
<div class="container">
  <div class="row g-3">
    <section class="col-12 col-md-6">
      <h2 class="h4">Programmieren</h2>
      <p>Schleifen und Funktionen üben.</p>
    </section>
    <section class="col-12 col-md-6">
      <h2 class="h4">Netzwerke</h2>
      <p>Adressen und Protokolle verstehen.</p>
    </section>
  </div>
</div>
```

A `container` a tartalom keretét adja, a `row` rácssort készít, a `g-3` a réseket
állítja. A `col-12` a 12 oszlopos rács egész szélességét használja. A `col-md-6`
a Bootstrap 5.3 `md` töréspontjától, `768px` viewportszélességtől hat oszlopot
foglal. Így keskeny nézetben egymás alatt, tágabban két egyforma oszlopban
jelennek meg a témák. A `h4` osztály csak megjelenés; az elem továbbra is `h2`
szintű címsor marad.

Egy egyszerű rács CSS-ből működik, egy modal vagy lenyíló interakció a megfelelő
JavaScript-komponenst is igényli. A Bootstrap 5-nek nincs jQuery-függősége.
A komponensek használatánál a címkézés, kontraszt és billentyűzetes kezelés
továbbra is fejlesztői feladat. Saját arculatot közös változókkal és a dokumentált
testreszabási pontokon érdemes kialakítani, nem minden gombot külön átírva.

## Vizsgán jól használható megfogalmazás

> A Bootstrap egy elterjedt frontend keretrendszer,
> amely reszponzív layoutot, kész UI-komponenseket
> és utility classokat biztosít a gyorsabb felületfejlesztéshez.  
> Különösen hasznos prototípusok, adminfelületek és olyan projektek esetén, ahol fontos a gyors, egységes megjelenés.  
> Előnye a gyorsaság és a kész komponenskészlet, hátránya lehet a sablonos kinézet és az egyedi design nehezebb kialakítása.

## Gyors önellenőrzés

1. Mire használjuk a Bootstrapot?
2. Mi az egyik legnagyobb előnye?
3. Mi lehet a hátránya?
4. Mire való a grid rendszer?
5. Milyen projektekhez jó választás?

## Rövid válaszok az önellenőrzéshez

1. Gyors, egységes frontend építésre
2. Kész komponenseket és reszponzív alapot ad
3. Sablonos kinézetet eredményezhet
4. Reszponzív elrendezésre
5. Prototípushoz, admin felülethez, gyors fejlesztéshez

## Források

- [Bootstrap: Migration to v5](https://getbootstrap.com/docs/5.3/migration/#javascript): a jQuery-függőség megszüntetése az 5-ös főverzióban. Ellenőrizve: `2026-10-14`.

Ellenőrizve: `2026-10-14`.

- [Bootstrap 5.3: Grid](https://getbootstrap.com/docs/5.3/layout/grid/): 12 oszlop, row és md breakpoint.
- [Bootstrap 5.3: Accessibility](https://getbootstrap.com/docs/5.3/getting-started/accessibility/): a komponensek akadálymentes használatának feltételei.


1. Bootstrap 5.3 - Introduction  
   https://getbootstrap.com/docs/5.3/getting-started/introduction/  
   Használat: a Bootstrap célja, felépítése és fő részei.

2. Bootstrap 5.3 - Breakpoints  
   https://getbootstrap.com/docs/5.3/layout/breakpoints/  
   Használat: reszponzív használat és breakpoint logika.

3. Bootstrap 5.3 - Grid system  
   https://getbootstrap.com/docs/5.3/layout/grid/  
   Használat: a layout és rácsrendszer gyakorlati szerepe.

Megnyitva: `2026-04-08`
