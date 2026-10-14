# Stadien der Softwareentwicklung

## Gyors vizuális kép

| Szakasz | Fő kérdés |
|---|---|
| tervezés / igényfelmérés | mit kell elkészíteni? |
| követelmények | pontosan mit várnak el? |
| tervezés / design | hogyan fog működni? |
| implementáció | hogyan írjuk meg? |
| tesztelés | helyesen működik? |
| bevezetés | használatba vehető? |
| karbantartás | hogyan javítjuk és fejlesztjük tovább? |

## Miért vannak szakaszok?

Mert egy komolyabb szoftvert nem lehet biztonságosan úgy elkészíteni, hogy valaki azonnal elkezd gépelni.

A szakaszokra bontás segít:

- csökkenteni a félreértéseket
- jobban becsülni az időt és költséget
- korábban észrevenni a hibákat
- tisztázni a felelősségeket

## Tipikus szakaszok részletesebben

### 1. Igényfelmérés és problémaértés

Itt azt tisztázzuk:

- mi a probléma
- kik a felhasználók
- mi a cél
- milyen korlátok vannak

### 2. Követelményelemzés

Itt lesz a homályos igényből konkrét elvárás.

Például:

- milyen funkciók kellenek
- milyen adatokkal dolgozik a rendszer
- milyen nem funkcionális elvárások vannak

### 3. Tervezés

Itt döntjük el:

- milyen lesz a felépítés
- milyen technológiákat használunk
- milyen adatmodellel dolgozunk
- hogyan osztjuk fel a rendszert

### 4. Implementáció

Itt történik:

- a programozás
- a modulok elkészítése
- az első működő változatok előállítása

### 5. Tesztelés

Itt ellenőrizzük:

- azt csinálja-e a rendszer, amit kell
- vannak-e hibák
- jól működnek-e együtt a részek

### 6. Bevezetés

Itt kerül használatba:

- telepítés
- átadás
- konfigurálás
- esetleges adatátvitel

### 7. Karbantartás és továbbfejlesztés

Ez sokszor a leghosszabb szakasz.

Ide tartozik:

- hibajavítás
- biztonsági frissítés
- új funkciók beépítése
- teljesítményjavítás

## Életciklus és napi fejlesztés: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| szoftverfejlesztési szakaszok | a teljes folyamat nagy lépései |
| napi fejlesztői munka | konkrét feladatok, kódolás, review, teszt, hibajavítás |

## Mire kell figyelni vizsgán?

- ne csak a kódolást említsd
- a tesztelést és karbantartást is mondd ki
- ne keverd össze a szakaszokat a konkrét módszertanokkal, például `Scrum`-mal vagy vízesésmodellel

## Egy követelmény végigkövetése

Egy tanfolyamhoz férőhelyfoglalást készítünk. Az igény: „lehessen jelentkezni”.
Ebből mérhető követelmény lesz: egy felhasználó egy alkalomra egyszer jelentkezhet,
és a visszaigazolás csak sikeres mentés után jelenhet meg.

| Szakasz | Ellenőrizhető eredmény |
|---|---|
| Elemzés | férőhelykorlát, jogosultságok és elfogadási feltételek |
| Tervezés | felületterv, adatmodell, az egyidejű foglalások kezelése |
| Implementáció | mentés és érthető visszajelzés |
| Teszt | szabad hely, betelt alkalom, ismételt kattintás |
| Bevezetés | kipróbált telepítés, mentés és visszaállítási terv |
| Karbantartás | felhasználói visszajelzésből javítás, majd ismételt teszt |

A szakaszok tevékenységeket jelölnek, nem kötelező egyszeri sorozatot. Iteratív
fejlesztésben egy kisebb funkció többször végigjárhatja őket. A teszteseteket már
a követelménynél megtervezhetjük. A validálás azt kérdezi, hogy a felhasználó
valódi problémáját oldjuk-e meg; a verifikálás azt, hogy a megadott elvárásokat
teljesíti-e a megoldás. A kettőhöz eltérő bizonyíték is tartozhat: felhasználói
próba, illetve specifikáció alapján végrehajtott teszt.

## Vizsgán jól használható megfogalmazás

> A szoftverfejlesztés több egymásra épülő szakaszból áll.  
> A tipikus lépések az igényfelmérés, követelményelemzés, tervezés, implementáció, tesztelés, bevezetés és  
> karbantartás.  
> Ennek a felosztásnak az a célja, hogy a fejlesztés átláthatóbb, ellenőrizhetőbb és biztonságosabb legyen.

## Gyors önellenőrzés

1. Miért bontjuk szakaszokra a szoftverfejlesztést?
2. Mi történik a követelményelemzés során?
3. Mi a tervezési szakasz fő célja?
4. Miért nem ér véget a folyamat a program elkészítésével?
5. Melyek a legfontosabb fő szakaszok?

## Rövid válaszok az önellenőrzéshez

1. Hogy átláthatóbb és kezelhetőbb legyen
2. Pontosítjuk az elvárásokat
3. Meghatározzuk a technikai megoldást
4. Mert még bevezetni és karbantartani is kell
5. Igény, követelmény, tervezés, implementáció, teszt, bevezetés, karbantartás

## Források

Ellenőrizve: `2026-10-14`.

- [IBM: Software Development Lifecycle](https://www.ibm.com/think/topics/sdlc): életciklus és visszacsatolás; a tanfolyamos példa saját.


1. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Használat: modern, hivatalos áttekintés a szoftverfejlesztés fő szakaszairól.

2. Atlassian - SDLC  
   https://www.atlassian.com/en/agile/software-development/sdlc  
   Használat: gyakorlati, könnyen követhető összefoglaló a szoftver életciklusának fő lépéseiről.

Megnyitva: `2026-04-09`
