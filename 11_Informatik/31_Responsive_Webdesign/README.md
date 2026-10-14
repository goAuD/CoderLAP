# Responsive Webdesign

## Gyors vizuális kép

| Eszköz | Mi történik? |
|---|---|
| mobil | egyoszlopos, egyszerűbb elrendezés |
| tablet | köztes tördelés |
| desktop | több oszlop, nagyobb tér |

## Mi a responsive webdesign lényege?

Nem külön oldalt készítünk minden eszközre, hanem ugyanazt az oldalt úgy tervezzük meg, hogy:

- átrendeződjön
- átméreteződjön
- olvasható maradjon
- kezelhető maradjon

## Milyen technikák tartoznak ide?

- rugalmas layout
- relatív méretek
- média lekérdezések (`media queries`)
- rugalmas képek és médiaelemek
- breakpointok

## Miért fontos?

- sokféle eszközről nyitják meg az oldalt
- jobb felhasználói élményt ad
- nincs szükség külön mobil oldalra
- karbantarthatóbb

## Responsive és mobile first: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| responsive webdesign | a felület alkalmazkodik a képernyőhöz |
| mobile first | tervezési stratégia, amely mobilról indul |

Tehát:

- a responsive egy technikai-tervezési eredmény
- a mobile first egy tervezési irány

## Mire kell figyelni?

- Nem elég csak összezsugorítani az oldalt.
- A tartalmi prioritás is változhat kisebb kijelzőn.
- A menük, táblázatok és képek külön figyelmet igényelnek.
- A teljesítmény mobilon is kritikus.

## Kidolgozott példa: témakártyák rugalmas rácsban

**Feladat és környezet:** mentsd a teljes példát UTF-8 HTML-fájlba, nyisd meg
modern böngészőben, majd változtasd az ablak szélességét. Mindhárom téma minden
méretben elérhető marad.

```html
<!doctype html>
<html lang="de">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Themenübersicht</title>
<style>
  .topics {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
    gap: 1rem;
  }
  .topics > article { min-width: 0; border: 1px solid; padding: 1rem; }
  .topics pre { overflow-x: auto; }
  * { box-sizing: border-box; }
</style>
<main>
  <h1>Themen</h1>
  <div class="topics">
    <article><h2>Schleifen</h2><p>Wiederholungen verstehen.</p></article>
    <article><h2>Funktionen</h2><p>Aufgaben aufteilen.</p></article>
    <article><h2>Datenbanken</h2><p>Daten verknüpfen.</p></article>
  </div>
</main>
</html>
```

`auto-fit` annyi oszlopot hoz létre, amennyi elfér. A kártya kívánt minimuma
`16rem`, de a `min(100%, 16rem)` nagyon keskeny helyen sem kér a konténernél
szélesebb oszlopot. Az `1fr` a megmaradó helyet egyenlően osztja szét.
`16px` gyökér-betűmérettel és a `.topics` **belső szélességét** mérve:

| Szabad szélesség | Eredmény | Indoklás |
|---|---|---|
| 360px | egy oszlop | két 256px-es kártya és egy 16px-es rés nem fér el |
| 600px | két oszlop | két kártya és egy rés elfér, három még nem |
| 1000px | három oszlop | három kártya és két rés elfér |

Itt külön media query nélkül is reszponzív a rács. Töréspontot akkor választunk,
amikor a tartalom indokolja, nem egy konkrét telefon neve alapján. A hosszú
kód helyben görgethető; `min-width: 0` engedi a rácselem zsugorodását. Képeknél
a `max-width: 100%; height: auto` őrzi az arányt, de a letöltendő fájl méretét
önmagában nem csökkenti. Ellenőrizd a hosszú német címeket, a nagyított szöveget
és azt is, hogy a teljes oldalnak ne keletkezzen indokolatlan vízszintes görgetése.

## Vizsgán jól használható megfogalmazás

> A responsive webdesign olyan tervezési és fejlesztési megközelítés,
> amelynek célja,
> hogy ugyanaz a weboldal különböző kijelzőméreteken is jól használható legyen.  
> Ehhez rugalmas elrendezést, media query-ket, breakpointokat és alkalmazkodó tartalmi megjelenítést használunk.  
> Előnye, hogy nem kell külön mobil és desktop oldalt fenntartani.

## Gyors önellenőrzés

1. Mi a responsive webdesign lényege?
2. Miért előnyös?
3. Milyen technikák segítik?
4. Mi a különbség a mobile firsthez képest?
5. Miért kell a tartalmi prioritással is foglalkozni?

## Rövid válaszok az önellenőrzéshez

1. Az oldal több kijelzőhöz alkalmazkodik
2. Jobb használhatóságot és kevesebb külön oldalt ad
3. Media query, breakpoint, rugalmas layout
4. A responsive eredmény, a mobile first stratégia
5. Mert kis kijelzőn más a hely és a figyelem

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Responsive web design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design): rugalmas layout, tartalomhoz igazított töréspont és képek.
- [web.dev: Macro layouts](https://web.dev/learn/design/macro-layouts): automatikusan alkalmazkodó Grid-megoldások.


1. MDN - Responsive design  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design  
   Használat: a responsive webdesign technikai alapjainak fejlesztői összefoglalója.

2. MDN - Responsive Web Design (RWD)  
   https://developer.mozilla.org/en-US/docs/Glossary/Responsive_web_design  
   Használat: rövid, pontos fogalmi definíció.

3. web.dev - Learn Design  
   https://web.dev/learn/design/  
   Használat: modern többeszközös webtervezési irányelvek.

Megnyitva: `2026-04-08`
