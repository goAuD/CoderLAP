# CMS

## Gyors vizuális kép

| Elem | Szerep |
|---|---|
| admin felület | tartalom kezelése |
| adatbázis | tartalom, felhasználók, beállítások tárolása |
| theme / sablon | megjelenítés |
| plugin / modul | funkcióbővítés |

## Mi az a CMS?

A `CMS` célja, hogy a tartalomkezelés:

- ne csak fejlesztők számára legyen lehetséges
- strukturáltan történjen
- több felhasználó együtt tudjon dolgozni

Tipikus feladatai:

- oldalak és cikkek kezelése
- médiafájlok kezelése
- jogosultságkezelés
- publikálás
- kategóriák, metaadatok kezelése

## Mi köze van az adatbázisokhoz?

Egy tipikus `CMS` sok adatot adatbázisban tárol:

- cikkek és oldalak tartalma
- felhasználók
- szerepkörök
- menük
- beállítások
- plugin- vagy moduladatok

Vagyis a `CMS` gyakran **adatbázisra épülő alkalmazásrendszer**.

## Miért fontos ezt itt ismerni?

Mert jó példa arra, hogyan kapcsolódik össze:

- adatmodell
- adatbázis
- alkalmazáslogika
- felhasználói felület

## `CMS` és `DBMS`: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| `CMS` | tartalomkezelő alkalmazás |
| `DBMS` | adatbáziskezelő szoftver |

Egy `CMS` gyakran használ egy `DBMS`-t a háttérben.

## Gyakorlati példák

- `WordPress`
- `Drupal`
- `Joomla`

## Kidolgozott munkafolyamat: egy tananyag publikálása

Egy szerkesztő új cikket készít a CMS adminfelületén. A piszkozatot előnézetben ellenőrzi, egy megfelelő jogosultságú személy jóváhagyja, majd publikálják. A látogató a frontendben a közzétett változatot látja. Egy korábbi verzió visszaállítása és az automatikus publikálási idő olyan funkció, amelynek támogatását a konkrét CMS-ben kell ellenőrizni.

A **TYPO3** szintén CMS. A backend a szerkesztési és adminisztrációs felület, a frontend a látogatók által használt webhely. A témasablon a megjelenést, a bővítmény külön funkciót ad; egyik sem azonos magával a tárolt tartalommal.

Üzemeltetési példában az adatbázis-dump mellé szükség lehet a feltöltött képekre, konfigurációra és a kompatibilis kód/bővítményverziókra is. Egy adatbázis sikeres visszatöltése még nem bizonyítja, hogy a cikk képei és az egész oldal működnek. Átadáskor egy tartalom létrehozását, jogosultságát, publikálását és visszaállítását is próbáld végig.

Léteznek fájlalapú és statikus kimenetet készítő CMS-ek is. A CMS-fogalomhoz tehát nem kötelező külön adatbázis-kiszolgáló.

## Vizsgán jól használható megfogalmazás

> A `CMS`, vagyis Content Management System olyan alkalmazásrendszer, amely digitális tartalmak létrehozását,  
> szerkesztését, tárolását és közzétételét támogatja.  
> A háttérben sok esetben adatbázist használ a tartalom, felhasználók, jogosultságok és beállítások kezelésére.  
> Ezért a `CMS` jó példa arra, hogyan használ egy alkalmazás adatbázist strukturált információk kezelésére.

## Gyors önellenőrzés

1. Mi a `CMS` fő célja?
2. Miért kapcsolódik az adatbázisokhoz?
3. Mi a különbség `CMS` és `DBMS` között?
4. Mondj két tipikus `CMS`-t.
5. Milyen adatokat tárolhat a háttérben?

## Rövid válaszok az önellenőrzéshez

1. Tartalmak kezelése és publikálása
2. Mert gyakran adatbázisban tárolja az adatokat
3. Az egyik alkalmazás, a másik adatbáziskezelő szoftver
4. WordPress, Drupal
5. Tartalom, felhasználók, jogosultságok, beállítások

## Források

1. MDN - CMS  
   https://developer.mozilla.org/en-US/docs/Glossary/CMS  
   Használat: rövid, tiszta technikai definíció a CMS fogalmához.

2. Drupal.org - Drupal CMS  
   https://new.drupal.org/drupal-cms  
   Használat: hivatalos, modern példa arra, hogyan működik a CMS mint valódi platform.

3. WordPress.com - What Is a CMS?  
   https://wordpress.com/go/tutorials/what-is-a-cms/  
   Használat: gyakorlati magyarázat a CMS fő részeihez és működéséhez.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [TYPO3: Concepts](https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/Concepts/Index.html): backend/frontend és a CMS szerkezete
- [MDN: CMS](https://developer.mozilla.org/en-US/docs/Glossary/CMS): a tartalomkezelés fogalma

Ellenőrizve: `2026-10-14`.
