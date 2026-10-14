# Meta Elemente und Metadaten

## Gyors vizuális kép

| Fogalom | Jelentés | Példa |
|---|---|---|
| adat | maga a tartalom | egy cikk szövege |
| metaadat | adat az adatról | cím, leírás, nyelv, kódolás |
| meta elem | HTML elem metaadat közlésére | `<meta name="description" ...>` |

## Mi az a metaadat?

A **metaadat** olyan kiegészítő információ, amely egy dokumentumot vagy erőforrást ír le.

Weboldalnál ez lehet például:

- az oldal címe
- rövid leírása
- karakterkódolása
- szerzője
- mobilos megjelenítési beállítása
- keresőrobotoknak adott jelzés

A metaadat célja nem az,
hogy a felhasználó hosszú szövegként elolvassa,
hanem hogy a rendszer könnyebben értelmezze az oldalt.

## Mi a szerepe a `<meta>` elemnek?

A `<meta>` elem a HTML `head` részében található, és olyan metaadatokat ad meg, amelyeket más elemek nem fejeznek ki pontosabban.

Gyakori formák:

```html
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="Rovid leiras az oldalrol" />
<meta name="robots" content="index,follow" />
```

Fontos:

- a `charset` azt mondja meg, milyen karakterkódolást használ a dokumentum
- a `viewport` a mobilos megjelenítéshez fontos
- a `description` gyakran a keresési találatok rövid leírásánál hasznos
- a `robots` azt jelzi, hogyan viselkedjen a keresőrobot

## Mire jók a gyakorlatban?

### Böngészőnek

- helyes karaktermegjelenítés
- jó mobilnézet
- helyes technikai feldolgozás

### Keresőmotoroknak

- az oldal rövid összefoglalása
- indexelési jelzések
- jobb értelmezhetőség

### Külső rendszereknek

- előnézetek
- megosztási információk
- strukturáltabb feldolgozás

## Meta elem és metaadat: ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| metaadat | általános információ a dokumentumról |
| `<meta>` elem | egy konkrét HTML elem, amellyel metaadatot közlünk |
| `title` | nem `<meta>`, hanem külön HTML elem, mégis meta jellegű információ |

## Mire kell figyelni?

- A meta leírás nem helyettesíti a jó tartalmat.
- A `description` önmagában nem varázsol jó helyezést.
- A hibás `charset` karakterhibát okozhat.
- A rossz `viewport` mobilon rontja a használhatóságot.
- A `robots` hibás beállítása miatt az oldal akár ki is maradhat az indexből.

## Melyik adatot ki használja?

Egy oldal fejlécének elemei külön feladatokat látnak el:

| Jelölés | Értelmező és feladat |
|---|---|
| `meta charset="utf-8"` | a böngésző helyesen dekódolja a fájl bájtjait |
| `meta name="description"` | rövid összefoglaló, amelyből a kereső kivonatot készíthet |
| `meta name="robots" content="noindex"` | az ezt követő keresőrobot ne vegye indexbe az oldalt |
| `html lang="de"` | a dokumentum nyelve, például a képernyőolvasó számára |
| `title` | dokumentumcím, például a böngészőlap felirata |

Az utolsó két sor metaadatot hordoz, de nem `meta` elem. A `charset` deklarációt
a `head` elejére tesszük; a HTML-előírás szerint teljes egészében az első
1024 bájton belül kell lennie. A tényleges fájlkódolás is UTF-8 legyen.

Egy privát tananyag hozzáférését bejelentkezés vagy más szerveroldali
jogosultság-ellenőrzés védi. A `noindex` keresőutasítás, nem hozzáférési korlát.
A `robots.txt` tiltása a feltérképezést szabályozza: ha a robot nem olvashatja
az oldalt, a rajta lévő `noindex` jelölést sem látja. Ezért a két beállítás
nem felcserélhető. A `description` szövegét pedig a kereső nem köteles szó szerint
megjeleníteni; az adott kereséshez más oldalszöveget is kiválaszthat.

## Vizsgán jól használható megfogalmazás

> A metaadat a dokumentumról szóló leíró adat.
> HTML-ben ezt gyakran a `head` részben elhelyezett `<meta>` elemek adják meg.  
> Ezek a böngészőnek, keresőmotoroknak és más rendszereknek
> segítenek az oldal helyes feldolgozásában,
> például a karakterkódolás, a mobilnézet
> vagy az oldal rövid leírása terén.

## Gyors önellenőrzés

1. Mi a metaadat lényege?
2. Hol helyezkedik el általában a `<meta>` elem?
3. Mire való a `charset`?
4. Mire jó a `viewport`?
5. Miért nem elég csak meta tageket írni SEO-hoz?

## Rövid válaszok az önellenőrzéshez

1. A dokumentumot leíró háttér-információ
2. A HTML `head` részében
3. A karakterkódolás megadására
4. A mobilos megjelenítés vezérlésére
5. Mert a tartalom és a technikai minőség is számít

## Források

Ellenőrizve: `2026-10-14`.

- [WHATWG: Metadata](https://html.spec.whatwg.org/dev/semantics.html): karakterkódolás és metaelemek.
- [Google Search Central: Robots meta tag](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag): indexelési utasítások és feltérképezés.


1. MDN - `<meta>`: The metadata element  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta  
   Használat: a `<meta>` elem típusai, attribútumai és gyakorlati szerepe.

2. WHATWG HTML Standard - The `meta` element  
   https://html.spec.whatwg.org/multipage/semantics.html#the-meta-element  
   Használat: hivatalos HTML-szabványi háttér a meta elem működéséhez.

3. MDN - `<head>`: The Document Metadata element  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head  
   Használat: kontextus ahhoz, hogy a metaelemek hol és milyen szerepben jelennek meg.

Megnyitva: `2026-04-08`
