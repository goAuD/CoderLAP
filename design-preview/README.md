# CoderLAP arculati előnézetek

Két összehasonlítható arculati irány a meglévő kezdőlaphoz és a `LAP-15-17`
(Schleifen) tananyaghoz. Ez külön előnézet; a produkciós sablonokat és a
Markdown-tananyagot nem módosítja.

## Tervezési alap

| | A: Műhely | B: Campus |
|---|---|---|
| Alap | `#f3f6fb` hűvös papír | `#211c35` szilva |
| Felület | `#ffffff` fehér | `#302943` padlizsán |
| Szöveg | `#1e3047` tinta | `#f7f3ff` törtfehér |
| Hangsúly | `#345ee8` kobaltkék | `#d4c5f9` levendula |
| Kiegészítő | `#f5c76c` sárga | `#ffc39f` barack |
| Halk szöveg | `#63738b` acélszürke | `#b5a8c8` mályvaszürke |

Mindkettő a repo helyi Manrope és Source Sans 3 betűit használja. A Manrope
adja a címek karakterét, a Source Sans 3 a hosszabb olvasnivaló ritmusát.
A monospace csak a valódi kódhoz tartozik. Balra zárt szövegek, 70 karakter
körüli olvasási szélesség, külön nyomtatási stílus.

```text
A: felső alkalmazásváltó
   témakörlista | rövid nyitás + kódábra
                kereső + témakörök

B: oldalsó alkalmazásváltó | nyitás + kiemelt tananyag
                          kereső + vízszintes témakörsorok

Tananyag: fejezetnavigáció | olvasófelület | kapcsolódó gyakorlás
Mobil: összehajtható navigáció, egyetlen olvasási oszlop
```

A hangsúly a tanuláson van: a fő vizuális elem egy ciklus működését mutatja.
Nincs kitalált tanulási statisztika vagy automatikus animáció. A regiszter
valódi témáit és a tananyag teljes DE/HU szövegét használjuk. A két irány
elrendezésben is különbözik, nem pusztán világos/sötét színváltozat.

## Indítás

A meglévő projektfüggőségekkel, a repo gyökeréből:

```powershell
python scripts/build_site.py
python design-preview/build.py
python -m http.server 8766 --bind 127.0.0.1 --directory dist
```

Előnézet: <http://127.0.0.1:8766/design-preview/studio-hu-home.html>.
Az előnézeti sávból váltható az irány, az oldaltípus és a DE/HU nyelv.
A német kezdőoldal: `studio-de-home.html`.

A `build.py` csak kézi indításra készíti el a `dist/design-preview/` mappát.
A rendes CI/build/deploy nem hívja. A többi tananyag linkje a változatlan
helyi alapoldalra vezet; új arculatot ebben a körben csak a két mintanézet kap.
A CoderQuiz/Coaster helyén a tervezett kapcsolatot bemutató párbeszédablak van,
mert a subdomainek ebben a munkában nem kerülnek kiadásra.

A kereső csak a helyi regisztert szűri. A tananyag jelölése kizárólag az
aktuális oldal munkamenetében él; az előnézet nem írja a produkciós haladást.
Nincs hálózati API, analitika vagy külső betűletöltés.

## Ellenőrzés és folytatás

- A meglévő 79 Python-teszt sikeres; a JavaScript szintaxisellenőrzése is sikeres.
- Mind a 8 nézetet ellenőriztük Chromiumban, 320, 390, 768 és 1440 pixeles
  szélességen. A teljes oldalon nincs vízszintes túllógás.
- Képi ellenőrzés történt az asztali és mobil kezdőlapokon, tananyagokon,
  valamint a nyomtatási CSS emulált nézetén.
- Kipróbálva: találatos és üres keresés, keresés törlése témakörváltáskor,
  DE/HU váltás, mobil tartalomjegyzék, jelölés és visszavonás, alkalmazásdialog.
- 1274 helyi link-, horgony- és betűfájl-hivatkozás ellenőrzése: 0 hiba.

A rendes build és egyes meglévő tesztek újraépítik a `dist/` könyvtárat.
Utánuk ismét futtatni kell a `python design-preview/build.py` parancsot.

Az előnézet nem teljes funkciómigráció: a produkciós haladáskezelés,
beállítások és többi tananyag változatlanul a jelenlegi felülethez tartozik.
A kiválasztott irány bevezetése külön feladat és külön PR lesz, a meglévő
funkciók megtartásával. Valódi iOS/Android eszközön és fizikai nyomtatón
ebben a körben nem történt ellenőrzés.
