# Metadaten

## Gyors vizuális kép

| Adat | Metaadat |
|---|---|
| fénykép | dátum, felbontás, GPS-adat |
| dokumentum | cím, szerző, nyelv |
| weboldal | description, charset, robots |
| adatbázistábla | oszlopnév, adattípus |

## Mi a metaadat szerepe?

A metaadat segít:

- azonosítani az adatot
- rendszerezni
- keresni benne
- feldolgozni
- automatizáltan értelmezni

## Hol találkozunk vele?

### Fájloknál

- létrehozási dátum
- fájlméret
- formátum

### Weben

- oldal címe
- leírása
- karakterkódolás
- robots információ

### Adatbázisokban

- mezőnevek
- adattípusok
- kulcsok

## Metaadat és HTML meta elem: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| metaadat | általános fogalom |
| `<meta>` elem | egy konkrét HTML-megoldás metaadat megadására |

Tehát a HTML `meta` elem csak egy speciális eszköz a metaadatok egyik fajtájához.

## Miért fontos?

- jobb kereshetőség
- jobb automatizált feldolgozás
- jobb rendszerezés
- pontosabb adatkezelés

## Mire kell figyelni?

- A metaadat is lehet érzékeny adat.
- A hibás metaadat félrevezető lehet.
- A hiányos metaadat rontja a kereshetőséget és feldolgozhatóságot.

## Kidolgozott eset: egy tananyag és a leíró adatai

A tananyag szövege elmagyarázza a ciklust. A következő szemléltető JSON pedig
a tananyaghoz tartozó katalógusbejegyzés; nem az oldal jelenlegi registry-sémája:

```json
{
  "id": "LAP-15-17",
  "title": "Schleifen",
  "language": "de",
  "modified": "2026-10-14",
  "format": "text/markdown"
}
```

Ebből a kereső címet, a nyelvválasztó nyelvet, a frissítési lista dátumot kap.
Az állandó azonosító akkor is használható maradhat, ha a megjelenített cím
változik. Az ISO-formátumú dátum géppel rendezhető, de itt csak napot jelöl;
pontos időponthoz időzónát vagy UTC-eltolást is rögzítenénk.

| Metaadattípus | Példa | Mit segít? |
|---|---|---|
| leíró | cím, téma, nyelv | megtalálás és azonosítás |
| technikai | médiatípus, felbontás, kódolás | feldolgozás és megjelenítés |
| adminisztratív | licenc, jogosultság, változat | felhasználás és kezelés |
| szerkezeti | fejezetek sorrendje és kapcsolata | összetett anyag összeállítása |

A HTTP `Content-Type: application/json` a küldött reprezentációt írja le;
nem bizonyítja, hogy a törzs valóban megfelel az alkalmazás sémájának. Hasonlóan
egy fájl neve, kiterjesztése és a feltöltő által küldött típusjelzés nem elegendő
biztonsági ellenőrzés. A metaadatot és a tényleges tartalmat együtt vizsgáljuk.

Megosztás előtt nézzük meg, nem kerül-e személyes helyadat a fényképbe vagy
szerzőnév a dokumentumba. A GPS-metaadat eltávolítása nem tünteti el a képen
látható címet vagy arcot. Metaadatból sem tárolunk többet a szükségesnél.

## Vizsgán jól használható megfogalmazás

> A metaadat olyan adat, amely más adatot ír le.  
> Nem maga a fő tartalom, hanem annak kiegészítő leírása, például cím, szerző, dátum, fájlméret vagy weboldal-leírás.  
> A metaadatok fontosak a rendszerezés, keresés, megjelenítés és automatizált feldolgozás szempontjából.

## Gyors önellenőrzés

1. Mi a metaadat lényege?
2. Mondj három különböző metaadat-példát.
3. Miért hasznos a metaadat?
4. Mi a különbség a metaadat és a HTML `<meta>` elem között?
5. Mi lehet a metaadat kockázata?

## Rövid válaszok az önellenőrzéshez

1. Más adatot leíró adat
2. Szerző, dátum, felbontás
3. Kereséshez, rendszerezéshez, feldolgozáshoz
4. A metaadat általános fogalom, a `<meta>` egy HTML-eszköz
5. Érzékeny információt is hordozhat

## Források

Ellenőrizve: `2026-10-14`.

- [W3C: DCAT 3](https://www.w3.org/TR/vocab-dcat-3/): katalógusok és leíró metaadatok.
- [MDN: Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type): HTTP-reprezentáció típusjelölése.
- [Apple: Manage location metadata in Photos](https://support.apple.com/en-gb/guide/personal-safety/ips0d7a5df82/1.0/web/1.0): helyadatok kezelése megosztáskor.


1. MDN - Metadata  
   https://developer.mozilla.org/en-US/docs/Glossary/Metadata  
   Használat: rövid, tiszta technikai definíció a metaadat fogalmára.

2. MDN - Web page metadata  
   https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/The_head_metadata_in_HTML  
   Használat: a metaadat webes megjelenésének gyakorlati magyarázata.

3. MDN - `<meta>` element  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta  
   Használat: a HTML-ben használt metaadatközlés technikai alapja.

Megnyitva: `2026-04-08`
