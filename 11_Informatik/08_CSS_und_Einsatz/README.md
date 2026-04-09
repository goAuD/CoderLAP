# CSS und Einsatz

## Lényeg 30 másodpercben

A **CSS** (`Cascading Style Sheets`) a weboldal megjelenését írja le.

Ezzel szabályozzuk például:

- színeket
- betűket
- méreteket
- térközöket
- elrendezést
- reszponzív viselkedést

Röviden:

- a HTML a tartalom és szerkezet
- a CSS a megjelenés és layout

## Gyors vizuális kép

| Technológia | Fő szerep |
|---|---|
| HTML | tartalom és struktúra |
| CSS | kinézet és elrendezés |
| JavaScript | viselkedés és interakció |

## Mi az a CSS?

A CSS egy stílusleíró nyelv, amellyel megmondjuk, hogyan jelenjenek meg a HTML-elemek.

Példa:

```css
body {
  font-family: Arial, sans-serif;
  color: #222;
}

h1 {
  color: #0a66c2;
}
```

Ez nem új tartalmat hoz létre, hanem a meglévő tartalmat formázza.

## Hogyan működik?

A CSS szabály jellemzően három részből áll:

- szelektor
- tulajdonság
- érték

Példa:

```css
p {
  color: red;
}
```

Itt:

- `p` = szelektor
- `color` = tulajdonság
- `red` = érték

## Mire használjuk?

### Formázásra

- színek
- betűméret
- háttér
- keret

### Elrendezésre

- `flexbox`
- `grid`
- pozicionálás
- margó és padding

### Reszponzív kialakításra

- media query-k
- mobil és desktop nézetek igazítása

### Egységes megjelenésre

- több oldalon ugyanaz a design
- központi stíluskezelés

## Miért előnyös?

- elválasztja a tartalmat a megjelenéstől
- könnyebb karbantartani
- újrahasznosítható
- egységes arculat adható vele
- reszponzív weboldalak építhetők

## CSS és HTML: ne keverd össze

| Fogalom | Feladat |
|---|---|
| HTML | leírja, mi van az oldalon |
| CSS | leírja, hogyan nézzen ki |
| JavaScript | leírja, hogyan viselkedjen |

## Mire kell figyelni?

- A túl sok inline stílus rossz karbantarthatóságot okoz.
- A rosszul felépített szelektorok nehezen kezelhető CSS-t eredményeznek.
- Nem elég csak "szépnek" lennie: használhatónak és áttekinthetőnek is kell lennie.
- A CSS nem helyettesíti a szemantikus HTML-t.

## Vizsgán jól használható megfogalmazás

> A CSS a weboldalak megjelenésének leírására szolgáló stílusnyelv.  
> Segítségével formázhatjuk a HTML-elemeket, szabályozhatjuk az elrendezést, és kialakíthatunk reszponzív, egységes felhasználói felületeket.  
> A HTML a szerkezetet, a CSS a megjelenést, a JavaScript pedig az interaktív működést adja.

## Gyakori vizsgahibák

- A CSS-t programozási nyelvnek nevezni.
- A HTML és CSS szerepét felcserélni.
- A reszponzív megjelenítést csak JavaScripthez kötni.
- Nem megemlíteni, hogy a CSS a layoutért is felel.

## Gyors önellenőrzés

1. Mi a CSS fő feladata?
2. Miből áll egy CSS-szabály?
3. Mire jó a `flexbox` vagy a `grid`?
4. Miért hasznos a tartalom és megjelenés szétválasztása?
5. Miben különbözik a CSS a JavaScript-től?

## Rövid válaszok az önellenőrzéshez

1. A megjelenés szabályozása
2. Szelektor, tulajdonság, érték
3. Elrendezésre
4. Könnyebb karbantartás és egységesség miatt
5. A CSS formáz, a JavaScript viselkedést ad

## Források

1. MDN - CSS: Cascading Style Sheets  
   https://developer.mozilla.org/en-US/docs/Web/CSS  
   Használat: a CSS fogalma, fő elemei és modern használata.

2. W3C - CSS Snapshot  
   https://www.w3.org/TR/CSS/  
   Használat: szabványi áttekintés a CSS modulokról és a webes szerepükről.

3. MDN - Learn CSS  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics  
   Használat: gyakorlati háttér a CSS alapvető működéséhez és felhasználásához.

Megnyitva: `2026-04-08`
