# HTML5 Grundgeruest

## Gyors vizuális kép

```html
<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Lernwerkstatt</title>
  </head>
  <body>
    Willkommen!
  </body>
</html>
```

## Miért kell alapváz?

Mert ettől lesz a dokumentum:

- szabványos
- jobban értelmezhető a böngészőnek
- könnyebben karbantartható

## Mit csinál az egyes rész?

### `<!doctype html>`

Megmondja a böngészőnek, hogy modern HTML-dokumentumról van szó, és segít elkerülni a quirks mode-ot.

### `<html lang="...">`

Ez a gyökérelem.

A `lang` attribútum segít:

- a böngészőnek
- keresőknek
- akadálymentesítési eszközöknek

### `<head>`

Ide kerül:

- metaadat
- cím
- stíluslap-hivatkozás
- script vagy más technikai információ

### `<meta charset="utf-8">`

Megadja a karakterkódolást.

### `<meta name="viewport" ...>`

Különösen mobilon fontos, mert segíti a megfelelő skálázást és reszponzív működést.

### `<title>`

Az oldal címe, amely megjelenik:

- böngészőfülön
- keresőtalálatoknál is fontos lehet

### `<body>`

Ide kerül a látható tartalom.

## Miért "HTML5"?

A mai gyakorlatban ez a modern HTML-dokumentum alapformája.

Fontos:

- ma sokszor egyszerűen csak "HTML"-nek mondjuk
- de az ilyen alapváz a HTML5 korszak standard szerkezete

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| `head` | technikai és meta információk |
| `body` | látható tartalom |
| `title` | oldal címe, nem azonos a főcímmel (`h1`) |
| `doctype` | dokumentumtípus-jelölés, nem maga a tartalom |

## A vázból egy megnyitható oldal

A fenti váz mindkét nyelvi változatban német mintatartalmat használ, ezért
`lang="de"` a helyes nyelvjelölés. Magyar oldalon a tartalommal együtt ezt is
`hu` értékre módosítjuk. A képernyőolvasó kiejtéséhez ez lényeges.

A `body` tartalmát cseréljük erre a HTML-részletre, és a teljes dokumentumot
mentsük `index.html` néven, UTF-8-kódolással. Közvetlenül böngészőben megnyitható:

```html
<main>
  <h1>Lernwerkstatt</h1>
  <section aria-labelledby="loops-title">
    <h2 id="loops-title">Schleifen</h2>
    <p>Eine Schleife wiederholt Anweisungen.</p>
  </section>
</main>
```

A böngészőlap címe `Lernwerkstatt`, a dokumentum főcíme szintén `Lernwerkstatt`,
alatta egy `Schleifen` szakasz és egy mondat jelenik meg. A két cím két külön
elem; bármelyik szövege önállóan változtatható. A `main` a fő tartalmat jelöli,
a címsorok a szerkezetet adják, nem pusztán betűméretek.

A viewport-beállítás a mobilos méretezést alapozza meg, a rugalmas elrendezést
majd a CSS biztosítja. A kézi nagyítást hagyjuk elérhetőnek. A „HTML5” a katalógus
elnevezése; a folyamatosan karbantartott specifikáció a HTML Living Standard.

## Vizsgán jól használható megfogalmazás

> A HTML5 alapváz egy szabványos dokumentumszerkezet, amely `doctype`, `html`, `head` és `body` részekből áll.  
> A `head` rész tartalmazza a metaadatokat,
> például a karakterkódolást, a viewport beállítást és a címet,
> míg a `body` tartalmazza a felhasználó számára látható tartalmat.  
> A helyes alapváz segíti a szabványos működést, a mobilos megjelenést és a karbantarthatóságot.

## Gyors önellenőrzés

1. Mi a `doctype` feladata?
2. Mi van a `head` részben?
3. Mi van a `body` részben?
4. Mire jó a `meta charset`?
5. Mire jó a `viewport` meta?

## Rövid válaszok az önellenőrzéshez

1. Modern dokumentumként jelzi a HTML-t
2. Metaadatok és technikai információk
3. A látható tartalom
4. A karakterkódolás megadására
5. A mobilos és reszponzív megjelenés támogatására

## Források

Ellenőrizve: `2026-10-14`.

- [WHATWG: HTML Standard](https://html.spec.whatwg.org/): dokumentumszerkezet és a mai HTML-szabvány.


1. MDN - Doctype  
   https://developer.mozilla.org/en-US/docs/Glossary/Doctype  
   Használat: hivatalos forrás a `<!doctype html>` szerepéhez.

2. MDN - Understanding quirks and standards modes  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Quirks_mode_and_standards_mode  
   Használat: megmagyarázza, miért kell a `doctype`.

3. MDN - HTML basics  
   https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics  
   Használat: hivatalos HTML5 alapváz példa `head`, `body`, `charset`, `viewport` elemekkel.

4. WHATWG - HTML Standard  
   https://html.spec.whatwg.org/  
   Használat: elsődleges szabványforrás az elemek és a dokumentumszerkezet mögött.

Megnyitva: `2026-04-08`
