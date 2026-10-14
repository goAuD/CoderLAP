# Personenbezogene und sensible Daten

## Gyors vizuális kép

| Adattípus | Példa | Védelmi szint |
|---|---|---|
| személyes adat | név, e-mail, IP-cím | védett |
| különleges kategóriájú személyes adat | egészségügyi adat, egyedi azonosítást szolgáló biometria, vallás | fokozottan védett |
| bűnügyi adat | büntetőítéletre vagy bűncselekményre vonatkozó adat | külön szabályok alá esik |

## Mi a személyes adat?

A GDPR szerint személyes adat:

- minden olyan információ
- amely egy természetes személyhez kapcsolható
- közvetlenül vagy közvetve azonosíthatóvá teszi őt

Nem csak a név számít személyes adatnak.

Személyes adat lehet például:

- e-mail-cím
- ügyfélazonosító
- rendszám
- IP-cím
- helyadat
- fénykép

## Mi számít különleges kategóriájú adatnak?

A GDPR 9. cikke külön kezeli a fokozottan védett adatokat.

Ide tartozhat például:

- faji vagy etnikai származás
- politikai vélemény
- vallási vagy világnézeti meggyőződés
- szakszervezeti tagság
- genetikai adat
- biometrikus adat egyedi azonosítás céljából
- egészségügyi adat
- szexuális életre vagy szexuális irányultságra vonatkozó adat

Fontos:

- ezek kezelése főszabály szerint **tilos**
- a 6. cikk szerinti jogalap mellett a 9. cikk (2) bekezdésének megfelelő kivétel is szükséges

## Mi a helyzet a bűnügyi adatokkal?

A büntetőítéletekre és bűncselekményekre vonatkozó adatok nem ugyanazok, mint a különleges kategóriájú adatok.

Ezekre a GDPR **10. cikke** vonatkozik.

A két kategóriához eltérő jogszabályhely tartozik:

- **Art. 9** = különleges kategóriák
- **Art. 10** = büntetőítéletek és bűncselekményekhez kapcsolódó adatok

## Miért fontos ez?

Mert nem mindegy:

- milyen adatot gyűjtünk
- milyen jogalapon kezeljük
- mennyire szigorú védelem kell
- kell-e külön tájékoztatás vagy kifejezett hozzájárulás

Példa:

- név + e-mail egy webshopnál: személyes adat
- orvosi lelet vagy betegségtörténet: különleges kategóriájú személyes adat

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| személyes adat | bármely, személyhez köthető információ |
| különleges kategóriájú személyes adat | fokozottan védett személyes adat |
| anonim adat | már nem köthető személyhez |
| álnevesített adat | még visszaköthető lehet, ezért továbbra is adatvédelmi szabály alá eshet |

## Besorolási feladat: név helyett azonosító

Egy gyakorló adatbázisban `Anna` helyett `user-42` szerepel, de egy külön táblában
megmarad az összerendelés. Ez **álnevesítés**, nem teljes anonimizálás: az összerendelést
ismerő adatkezelő vissza tudja azonosítani az érintettet. Az összerendelő táblát külön
hozzáféréssel védjük, és az álnevesített adathalmazt is személyes adatként kezeljük.

Az anonim adatnál az azonosítás az észszerűen valószínű eszközökkel sem lehetséges.
A név törlése önmagában ehhez kevés lehet: ritka munkakör, pontos születési dátum
és kis település együtt visszavezethet valakihez. Az azonosíthatóságot a környezetben
rendelkezésre álló további információval együtt vizsgáljuk.

Egy egyszerű profilfotó lehet személyes adat, de nem automatikusan a 9. cikk szerinti
biometrikus különleges adat. Egy személy egyedi felismerésére készített és használt
arcfelismerési sablon már más helyzet. A jelszó biztonsági szempontból érzékeny,
de önmagában nem a 9. cikk felsorolt különleges adatkategóriáinak egyike.

**Következtetés:** a technikai védelem igényét nem csak a jogi kategória neve határozza meg.
Egy hétköznapi elérhetőségből is lehet komoly kár, ha veszélyeztetett személyhez tartozik.

Forrás: [DSB: különleges adatkategóriák](https://dsb.gv.at/faqs/besondere-datenkategorien),
GDPR 4., 6., 9., 10. cikk és (26), (51) preambulumbekezdés.
Ellenőrizve: 2026-10-14.

## Vizsgán jól használható megfogalmazás

> Személyes adat minden olyan információ, amely egy azonosított vagy azonosítható természetes személyre vonatkozik.  
> A különleges kategóriájú személyes adatok,
> például az egészségügyi vagy egyedi azonosításra kezelt biometrikus adatok,
> fokozott védelem alatt állnak, és kezelésük főszabály szerint tilos,
> csak meghatározott kivételek mellett megengedett.  
> A büntetőítéletekre és bűncselekményekre vonatkozó adatok külön, a GDPR 10. cikke szerinti szabályozás alá tartoznak.

## Gyors önellenőrzés

1. Mi a személyes adat?
2. Mondj három példát személyes adatra.
3. Mi tartozik a különleges kategóriájú adatok közé?
4. Melyik GDPR-cikk foglalkozik a különleges kategóriákkal?
5. Ugyanaz-e a bűnügyi adat és a különleges kategóriájú adat?

## Rövid válaszok az önellenőrzéshez

1. Személyhez köthető információ
2. Név, e-mail-cím, IP-cím
3. Például egészségügyi adat, egyedi azonosításra kezelt biometrikus adat, vallási meggyőződés
4. A 9. cikk
5. Nem, a bűnügyi adatot külön a 10. cikk szabályozza

## Források

1. EUR-Lex - Regulation (EU) 2016/679  
   https://eur-lex.europa.eu/eli/reg/2016/679/oj  
   Használat: a személyes adat, a különleges kategóriák és a bűnügyi adatok elsődleges jogforrása.

2. Datenschutzbehörde - Besondere Datenkategorien  
   https://dsb.gv.at/faqs/besondere-datenkategorien  
   Használat: osztrák hatósági összefoglaló a korábban "sensible Daten"-nek nevezett adatkategóriákról.

3. Datenschutzbehörde - Ihre Rechte als betroffene Person  
   https://dsb.gv.at/rechte-pflichten/ihre-rechte-als-betroffene-person  
   Használat: hatósági definíciók a személyes adatra és az érintett fogalmára.

4. oesterreich.gv.at - Datenschutz  
   https://www.oesterreich.gv.at/de/lexicon/D/Seite.991455  
   Használat: osztrák kormányzati áttekintés gyakorlati példákkal személyes adatokra.

Megnyitva: `2026-04-08`
