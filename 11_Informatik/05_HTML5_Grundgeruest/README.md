# HTML5 Grundgeruest

## Gyors vizuális kép

```html
<!doctype html>
<html lang="de">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Oldal címe</title>
  </head>
  <body>
    Tartalom
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

## Vizsgán jól használható megfogalmazás

> A HTML5 alapváz egy szabványos dokumentumszerkezet, amely `doctype`, `html`, `head` és `body` részekből áll.  
> A `head` rész tartalmazza a metaadatokat,
> például a karakterkódolást, a viewport beállítást és a címet,
> míg a `body` tartalmazza a felhasználó számára látható tartalmat.  
> A helyes alapváz segíti a szabványos működést, a mobilos megjelenést és a karbantarthatóságot.

## Gyakori vizsgahibák

- A `title` elemet a `body` részbe tenni.
- Azt hinni, hogy a `title` ugyanaz, mint a főcím (`h1`).
- Kihagyni a `doctype`-ot.
- Nem használni `charset` vagy `viewport` meta elemet modern oldalnál.

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
