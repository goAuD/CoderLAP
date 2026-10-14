# Qualitätsmerkmale der Softwarefunktionalität

## Gyors vizuális kép

| Részterület | Mit jelent? |
|---|---|
| functional completeness | minden szükséges funkció megvan |
| functional correctness | helyes eredményt ad |
| functional appropriateness | jól támogatja a feladat elvégzését |

## Mit értünk itt funkcionalitási minőségen?

Nem elég, hogy “van funkció”.

A jó funkcionalitás azt jelenti, hogy:

- a rendszer tudja, amit kell
- jól működik
- használható módon támogatja a célt

## A három fontos részterület

### 1. Functional completeness

A szükséges funkciók teljessége.

Kérdés:

- benne van minden, amire valóban szükség van?

### 2. Functional correctness

A rendszer helyessége.

Kérdés:

- a funkció pontos, helyes eredményt ad?

### 3. Functional appropriateness

A funkciók alkalmassága.

Kérdés:

- a megoldás tényleg jól segíti a felhasználó feladatát?

## Példa

Egy webshop kosárfunkciónál:

- **completeness**: lehet terméket hozzáadni, törölni, módosítani
- **correctness**: a végösszeg helyes
- **appropriateness**: a kedvezmény és a szállítás számítása is a vásárlási feladat részeként elvégezhető

## Funkcionalitás és használhatóság: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| funkcionalitási minőség | mit tud és mennyire helyesen |
| használhatóság | mennyire könnyű használni |

Van köztük kapcsolat, de nem ugyanaz.

## Teljesség, helyesség és alkalmasság külön vizsgálva

Egy kölcsönzőnek a foglalás mellett hosszabbítás és visszavétel is szükséges. Ha ezek közül valamelyik hiányzik, a funkcionális teljesség nem megfelelő. Ha mindegyik létezik, de a visszavétel téves eszközt tesz szabaddá, a funkcionális helyesség sérül.

Az alkalmasság azt nézi, mennyire támogatja a funkciók készlete a feladat célzott elvégzését. Például a csoportos visszavétel egy teljes osztály eszközeit kezeli, és nem kíván külső táblázatban végzett segédszámítást. A gomb olvashatósága és a kezelés megtanulhatósága inkább az interakció minőségéhez, a válaszidő a teljesítményhez tartozik.

Az ISO/IEC 25010:2023 termékminőségi modelljében kilenc fő jellemző szerepel; a functional suitability csak az egyik. A három aljellemző továbbra is completeness, correctness és appropriateness. A 2011-es kiadás usability csoportjának helyét a 2023-as modellben az interaction capability fogalom veszi át, módosított részletekkel.

## Vizsgán jól használható megfogalmazás

> A szoftver funkcionalitásának minősége azt fejezi ki,
> hogy a rendszer a szükséges funkciókat teljes körűen,
> helyesen és a feladat szempontjából megfelelő módon biztosítja-e.  
> Az ISO 25010 terminológiájában ez a functional suitability területéhez kapcsolódik,
> amelynek fő részei a functional completeness,
> functional correctness és functional appropriateness.  
> Egy jó szoftver tehát nemcsak sok funkcióval rendelkezik, hanem azokat pontosan és célszerűen is nyújtja.

## Gyors önellenőrzés

1. Mit jelent a functional completeness?
2. Mit jelent a functional correctness?
3. Mit jelent a functional appropriateness?
4. Miért nem elég önmagában sok funkció?
5. Mi a különbség a funkcionalitási minőség és a használhatóság között?

## Rövid válaszok az önellenőrzéshez

1. Minden szükséges funkció megléte
2. Helyes működés és eredmény
3. A feladat jó támogatása
4. Mert a funkció lehet hibás vagy rosszul illeszkedő
5. Az egyik a funkciók megfelelőségét, a másik a könnyű használatot nézi

## Források

- [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html)  
  A jelenlegi termékminőségi modell hivatalos leírása.

- [ISTQB: Advanced Level Test Analyst v4.0, Appendix A](https://istqb.org/?download_id=5745&sdm_process_download=1)  
  A 2011-es és a 2023-as minőségi jellemzők hivatalos vizsgaszakmai összevetése.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. ISO/IEC 25010:2023 - Product quality model  
   https://www.iso.org/standard/78176.html  
   Használat: hivatalos elsődleges forrás a szoftverminőségi modellhez.

2. AQCLab - Functional Suitability Evaluation and Certification - ISO/IEC 25000  
   https://aqclab.es/index.php/en/software-quality-evaluation-certification-iso-25000/functional-suitability-evaluation-certification-iso-25000  
   Használat: korszerű, ISO 25000-hoz kapcsolódó magyarázó forrás a `functional suitability` aljellemzőihez.

Megnyitva: `2026-04-08`
