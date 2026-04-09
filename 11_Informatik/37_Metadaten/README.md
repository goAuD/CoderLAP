# Metadaten

## Lényeg 30 másodpercben

A **metaadat** olyan adat, amely **más adatot ír le**.

Röviden:

- nem maga a fő tartalom
- hanem a tartalomról szóló leíró információ

Példák:

- fájl neve, mérete, létrehozási ideje
- kép felbontása
- dokumentum szerzője
- weboldal leírása

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

## Vizsgán jól használható megfogalmazás

> A metaadat olyan adat, amely más adatot ír le.  
> Nem maga a fő tartalom, hanem annak kiegészítő leírása, például cím, szerző, dátum, fájlméret vagy weboldal-leírás.  
> A metaadatok fontosak a rendszerezés, keresés, megjelenítés és automatizált feldolgozás szempontjából.

## Gyakori vizsgahibák

- A metaadatot csak a webre leszűkíteni.
- A metaadatot összekeverni a tényleges tartalommal.
- Nem megemlíteni a fájl-, adatbázis- vagy média példákat.
- A `<meta>` elemet magával a fogalommal azonosnak venni.

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
