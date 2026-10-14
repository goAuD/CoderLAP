# Pflichtenheft

## Gyors vizuális kép

| Dokumentum | Fő kérdése |
|---|---|
| `Lastenheft` | mit és miért kell megoldani |
| `Pflichtenheft` | hogyan lesz megoldva |

## Mi a Pflichtenheft?

A `Pflichtenheft` a megoldás megvalósítási leírása.

Általában tartalmazza:

- a megvalósítási koncepciót
- funkcionális és technikai részleteket
- rendszerhatárokat
- interfészeket
- minőségi elvárásokat
- ütemezési vagy átadási szempontokat

## Miért fontos?

- egyértelműsíti a megoldás módját
- csökkenti a félreértést a megrendelő és kivitelező között
- alapot ad a fejlesztéshez, teszteléshez és átvételhez

## Mikor készül?

Tipikusan:

1. először elkészül a `Lastenheft`
2. utána a megvalósító oldal kidolgozza a `Pflichtenheft`-et
3. ezt egyeztetik és jóváhagyják
4. ezután indul a részletes megvalósítás

## Mit ne keverj össze?

| Fogalom | Jelentés |
|---|---|
| `Lastenheft` | a megrendelői elvárások összessége |
| `Pflichtenheft` | a megvalósítás részletes terve |

## Mire kell figyelni?

- ne legyen túl homályos
- technikailag legyen követhető
- fedje le a megrendelői elvárásokat
- legyen egyeztetett és ellenőrizhető

## Követelményből megvalósítási leírás

A Lastenheft K-03 igénye: a jogosult ügyintéző tudja letölteni az adott napi foglalásokat. A Pflichtenheft ehhez rögzíti például a dátumválasztó működését, a szerveroldali jogosultság-ellenőrzést és a CSV oszlopait: foglalási azonosító és időpont. A fájl UTF-8 kódolású, a nem szükséges személyes adatok kimaradnak.

Az elfogadási próba egy előkészített napon három foglalást használ. A kimenetnek pontosan e három sort kell tartalmaznia; másik nap adatai nem jelennek meg. Jogosulatlan felhasználó közvetlen kérése sem adhat exportot. Így ugyanahhoz az igényazonosítóhoz kapcsolódik a megoldás és az ellenőrzés.

A jóváhagyott változatot azonosítani kell. Új oszlop kérésekor áttekintik az adatvédelmi, tesztelési és időbeli hatást, majd frissítik az elfogadott leírást. A részletezettség a projekttől függ; nem minden fejlesztés kíván egyetlen, előre teljesen lezárt nagy dokumentumot.

## Vizsgán jól használható megfogalmazás

> A Pflichtenheft a megvalósítás részletes leírása,
> amely azt rögzíti, hogy a megrendelő által megadott követelményeket
> hogyan fogják teljesíteni.  
> Jellemzően a kivitelező vagy fejlesztő oldal dolgozza ki a Lastenheft alapján.  
> Fontos szerepe, hogy technikailag egyértelmű alapot adjon a fejlesztéshez, teszteléshez és későbbi átvételhez.

## Gyors önellenőrzés

1. Mi a Pflichtenheft fő célja?
2. Milyen kérdésre válaszol?
3. Melyik dokumentum után készül?
4. Ki dolgozza ki tipikusan?
5. Miért fontos a fejlesztésnél?

## Rövid válaszok az önellenőrzéshez

1. A megvalósítás leírása
2. Arra, hogy hogyan oldjuk meg
3. A Lastenheft után
4. A megvalósító / kivitelező oldal
5. Mert technikai alapot ad a munkához

## Források

- [IREB: CPRE Glossary](https://cpre.ireb.org/en/downloads-and-resources/glossary)  
  Követelményfajták, elfogadási feltételek és nyomon követhetőség.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. IHK Frankfurt am Main - Software-Erstellungsvertrag  
   https://www.frankfurt-main.ihk.de/recht/mustervertraege/software-erstellungsvertrag-5199364  
   Használat: hivatalos IHK-forrás, amely a Pflichtenheft tartalmát és szerződéses szerepét mutatja be.

2. Wikipedia - Pflichtenheft  
   https://de.wikipedia.org/wiki/Pflichtenheft  
   Használat: DIN 69901 és VDI hivatkozásokkal alátámasztott,
   jól strukturált összefoglaló a Pflichtenheft fogalmáról,
   tartalmáról és gyakorlati alkalmazásáról.

Megnyitva: `2026-04-08`
