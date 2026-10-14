# CMS

## Gyors vizuális kép

| Rész | Feladat |
|---|---|
| admin felület | tartalmak kezelése |
| adatbázis | tartalom és beállítások tárolása |
| sablon / theme | megjelenés |
| plugin / modul | extra funkciók |
| jogosultságkezelés | ki mit szerkeszthet |

## Mi az a CMS?

A CMS olyan szoftverrendszer, amely segít a tartalmak központi kezelésében.

Ez azt jelenti, hogy a felhasználó általában:

- belép egy admin felületre
- új oldalt vagy bejegyzést hoz létre
- képet tölt fel
- szerkeszti a szöveget
- közzéteszi a tartalmat

anélkül, hogy a teljes HTML-, CSS- vagy backend-kódot kézzel kellene írnia.

## Hogyan működik?

Egy tipikus CMS-ben a tartalom és a megjelenés részben elválik egymástól.

### Tartalom

- szöveg
- képek
- médiafájlok
- cikkek
- oldalak

### Megjelenítés

- sablon
- theme
- layout

### Funkcióbővítés

- plugin
- modul
- bővítmény

## Miért hasznos?

- gyorsabb tartalomkezelés
- nem fejlesztők számára is használható
- könnyebb frissítés
- több felhasználó együtt tud dolgozni
- jogosultságok kezelhetők
- nagyobb oldalaknál is áttekinthetőbb működés

## Hol használják?

Gyakori területek:

- vállalati weboldal
- híroldal
- blog
- webshop háttérrendszer része
- intranet
- oktatási vagy információs portál

## CMS és egyedi fejlesztés: ne keverd össze

| Megoldás | Előny | Hátrány |
|---|---|---|
| CMS | gyors indulás, könnyebb tartalomkezelés | a választott rendszer kereteihez kell igazodni |
| egyedi fejlesztés | célzott testreszabhatóság | a közös alapfunkciókat is meg kell valósítani |

## Mit kell fejlesztőként látni?

A CMS nem "varázsdoboz", hanem egy platform.

Fejlesztőként gyakran ezekkel dolgozunk:

- sablonkészítés
- plugin fejlesztés
- adatstruktúrák kialakítása
- jogosultságok finomhangolása
- SEO és teljesítmény javítása
- frissítések és biztonság

## Mire kell figyelni?

- A túl sok plugin instabilitást okozhat.
- A CMS-t rendszeresen frissíteni kell.
- A sablon és a tartalom ne legyen túl szorosan összekötve.
- A jogosultságkezelést nem szabad lazán venni.
- Nem minden projekthez CMS a legjobb választás.

## Tartalommodell és szerkesztői folyamat

Egy iskolai hírhez például `cím`, `bevezető`, `törzsszöveg`, `nyelv` és
`publikálási állapot` tartozik. Ezek szerkeszthető mezők. A sablon dönti el,
hogyan jelenjenek meg a honlapon; egy arculatváltás ezért nem kívánja meg
az összes hír újraírását.

Egy lehetséges munkafolyamat:

1. A szerző piszkozatot hoz létre és képet csatol szöveges alternatívával.
2. A szerkesztő az előnézetben ellenőrzi a tartalmat és a nyelvi változatot.
3. A publikálásra jogosult személy közzéteszi. A mentés és a publikálás
   ebben a folyamatban két külön lépés.
4. Későbbi módosításkor a verzióelőzményből visszakereshető az előző szöveg.

A TYPO3 Workspaces például ellenőrzési szakaszokat és verziózást ad ehhez.
A szerkesztőnek nem kell adminisztrátori jog a bővítmények telepítéséhez.
Mentéskor a tartalom mellett a médiát és a rendszer helyreállításához szükséges
beállításokat is figyelembe vesszük.

Hagyományos CMS-nél a rendszer a megjelenítést is kezelheti. Headless CMS-nél
API-n adja a tartalmat külön frontendeknek. Egy CMS használhat fájlos tárolást
is; az adatbázis a fenti tipikus felépítés része, nem a fogalom kötelező feltétele.
Az egyedi fejlesztés és a CMS együtt is alkalmazható, például saját modul révén.

## Vizsgán jól használható megfogalmazás

> A CMS, vagyis Content Management System olyan rendszer,
> amely lehetővé teszi digitális tartalmak létrehozását,
> szerkesztését, tárolását és közzétételét.  
> Előnye, hogy nem csak fejlesztők tudják használni,
> ugyanakkor bővíthető sablonokkal, modulokkal
> és jogosultságkezeléssel.  
> Tipikus felhasználása például vállalati weboldalak, blogok és portálok üzemeltetése.

## Gyors önellenőrzés

1. Mi a CMS fő feladata?
2. Miért előnyös egy CMS?
3. Melyek a tipikus részei?
4. Miben különbözik az egyedi fejlesztéstől?
5. Milyen kockázat lehet túl sok plugin esetén?

## Rövid válaszok az önellenőrzéshez

1. Tartalmak kezelése és publikálása
2. Gyorsabb és könnyebben használható
3. Admin felület, adatbázis, theme, plugin, jogosultságkezelés
4. Kész tartalomkezelési alapot ad; az egyedi igényekhez konfiguráció vagy fejlesztés kellhet
5. Instabilitás és biztonsági probléma

## Források

Ellenőrizve: `2026-10-14`.

- [TYPO3: Workspaces](https://docs.typo3.org/c/typo3/cms-workspaces/main/en-us/): verziók és szerkesztői jóváhagyás.


1. MDN - CMS  
   https://developer.mozilla.org/en-US/docs/Glossary/CMS  
   Használat: rövid, tiszta technikai definíció a CMS fogalmára.

2. WordPress.com - What Is a Content Management System and How to Choose the Best CMS for Your Needs  
   https://wordpress.com/go/tutorials/what-is-a-cms/  
   Használat: gyakorlati magyarázat arra, hogyan működik egy CMS és milyen fő részei vannak.

3. Drupal.org - Drupal CMS  
   https://www.drupal.org/drupal-cms  
   Használat: hivatalos, modern példa arra, hogyan jelenik meg a CMS mint valódi platform a gyakorlatban.

Megnyitva: `2026-04-08`
