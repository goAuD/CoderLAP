# Protokollieren technischer Arbeiten

## Gyors vizuális kép

| Kérdés                | Mit kell rögzíteni?         |
| --------------------- | --------------------------- |
| ki?                   | felelős személy             |
| mikor?                | dátum, idő                  |
| hol?                  | rendszer, környezet, eszköz |
| mit?                  | végrehajtott tevékenység    |
| miért?                | cél vagy indok              |
| mi lett az eredmény?  | siker, hiba, eltérés        |
| mi a következő lépés? | teendő, eszkaláció, lezárás |

## Miért kell protokollálni?

Mert a technikai munkák gyakran:

- összetettek
- több emberhez kötődnek
- utólag visszanézendők
- hibakereséshez kapcsolódnak
- audit vagy átadás szempontjából fontosak

## Mire jó a jó protokoll?

- visszakövethetőség
- átláthatóság
- hibakeresés
- felelősségek tisztázása
- tudásátadás
- minőségbiztosítás

## Mit kell egy technikai protokollnak tartalmaznia?

## 1. Alapadatok

- dátum
- idő
- készítő neve
- érintett rendszer / eszköz
- verzió vagy környezet

## 2. Feladat leírása

Röviden:

- mi volt a feladat
- miért történt a beavatkozás

## 3. Végrehajtott lépések

Dokumentálni kell:

- milyen lépések történtek
- milyen sorrendben
- milyen eszközökkel vagy parancsokkal

## 4. Eredmény

Meg kell adni:

- sikerült vagy nem
- mi változott
- van-e eltérés
- milyen állapotban maradt a rendszer

## 5. Hibák és megfigyelések

Például:

- hibaüzenet
- rendellenes működés
- kockázat
- ismert korlát

## 6. Következő lépések

- további javítás
- eszkaláció
- újratesztelés
- lezárás

## Jó technikai protokoll jellemzői

- pontos
- rövid, de nem hiányos
- tényszerű
- időrendben követhető
- más számára is érthető

## Mire kell figyelni?

- ne csak azt írd le, hogy „javítva”
- legyen benne konkrétum
- legyen világos az eredmény
- hiba esetén legyen bizonyíték vagy azonosító
- ne utólag emlékezetből legyen összerakva

## Egyszerű példa

### Feladat

Nyomtató hálózati beállításának javítása

### Protokoll

- Dátum: `2026-04-08`
- Felelős: `Minta Béla`
- Eszköz: `HP hálózati nyomtató`
- Környezet: `iroda 2, VLAN 10`
- Tevékenység: IP-cím ellenőrzése és újrakonfigurálása
- Lépések:
  - jelenlegi IP ellenőrzése
  - hibás gateway megállapítása
  - új hálózati beállítás megadása
  - tesztnyomtatás
- Eredmény: tesztnyomtatás sikeres
- Következő lépés: felhasználói teszt

## Hol használják?

- szervizelésnél
- telepítésnél
- konfigurációnál
- tesztelésnél
- hibajavításnál
- rolloutnál
- átadásnál

## Vizsgán jól használható megfogalmazás

> A technikai munkák protokollálása azt jelenti, hogy a műszaki tevékenységeket visszakövethető módon dokumentáljuk.  
> Egy jó protokoll tartalmazza a dátumot, a felelőst,
> az érintett rendszert, a végrehajtott lépéseket, az eredményt,
> az esetleges hibákat és a következő lépéseket.  
> Ez fontos a hibakereséshez, az átadáshoz, az ellenőrizhetőséghez és a csapatmunkához.

## Gyakori vizsgahibák

- Túl rövid, semmitmondó bejegyzések.
- Nincs dátum vagy felelős.
- Nincs eredmény vagy lezárás.
- Nem különül el a tény és a vélemény.
- A protokollból nem derül ki, mi történt valójában.

## Gyors önellenőrzés

1. Miért fontos a technikai munkák protokollálása?
2. Milyen alapadatokat kell rögzíteni?
3. Mit kell írni az eredmény részbe?
4. Miért fontosak a következő lépések?
5. Mi jellemzi a jó technikai protokollt?

## Rövid válaszok az önellenőrzéshez

1. Visszakövethetőség és hibakeresés miatt
2. Dátum, idő, felelős, érintett rendszer / környezet
3. Mi lett a beavatkozás eredménye
4. Mert megmutatják, hogyan folytatódik vagy zárul a feladat
5. Pontos, érthető, tényszerű és követhető

## Források

1. ISTQB CTFL Syllabus v3.1.1  
   https://istqb.org/wp-content/uploads/2024/11/ISTQB-CTFL_Syllabus_2018_v3.1.1.pdf  
   Használat: test execution logging és work products mint strukturált technikai naplózás.

2. Azure DevOps Test Plans - Manage test runs  
   https://learn.microsoft.com/en-us/azure/devops/test/test-runs  
   Használat: hivatalos példa arra, milyen metaadatokat és eredményeket érdemes rögzíteni.

3. Planning the Deployment - Microsoft Learn  
   https://learn.microsoft.com/en-us/iis/web-hosting/installing-infrastructure-components/planning-the-deployment  
   Használat: checklist-szemlélet, lépések, monitoring és team training mint dokumentálandó elemek.

Megnyitva: `2026-04-08`
