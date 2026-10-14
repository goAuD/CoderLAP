# DevOps

## Gyors vizuális kép

| Hagyományos működés | DevOps |
|---|---|
| fejlesztés és üzemeltetés külön silókban | szorosabb együttműködés |
| ritkább kiadás | gyakoribb kiadás |
| több kézi lépés | több automatizálás |
| lassabb visszacsatolás | gyorsabb feedback |

## Mi az a DevOps?

A DevOps nem csak eszköz, és nem csak `CI/CD`.

Hanem együtt:

- kultúra
- folyamatok
- gyakorlatok
- eszközök

Célja, hogy a csapat gyorsabban és megbízhatóbban szállítson szoftvert.

## Fő elemei

- fejlesztés és üzemeltetés együttműködése
- automatizált build, teszt és release
- verziókezelés
- monitorozás
- gyors hibajelzés és visszacsatolás

## Miért fontos?

- rövidebb kiadási ciklusok
- jobb minőség
- gyorsabb javítás
- nagyobb átláthatóság
- stabilabb rendszerek

## DevOps és CI/CD: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| DevOps | tágabb kultúra és működési modell |
| CI/CD | fontos DevOps-gyakorlatok egy része |

## Mire kell figyelni?

- A DevOps nem csak pipeline.
- Eszközökkel önmagában nem oldható meg.
- Kultúra és felelősségmegosztás is kell hozzá.
- Biztonság, monitoring és üzemeltethetőség is része.

## A committól az ellenőrzött működésig

Egy apró javítás útja lehet: kódreview, automatikus teszt, azonosítható kiadási csomag, tesztkörnyezeti próba, majd élesítés utáni állapotellenőrzés. Ugyanazt a már ellenőrzött csomagot telepítjük; a titkos konfiguráció külön, jogosultságokkal védve kerül a környezetbe.

A CI a változások gyakori összeillesztését és automatikus ellenőrzését támogatja. Continuous delivery esetén a változat kiadásra kész, de az élesítéshez lehet kézi jóváhagyás. Continuous deployment esetén a sikeres ellenőrzések után a kiadás is automatikus. A „CD” rövidítést ezért érdemes feloldani.

A telepítés sikere után is figyeljük a szolgáltatást: működik-e a belépés és a fő felhasználói művelet? Adatbázis-változtatásnál külön helyreállítási terv kell, mert a régi kód visszarakása nem feltétlenül állítja helyre az adatokat. A fejlesztés és az üzemeltetés együtt tanul a tapasztalatból.

## Vizsgán jól használható megfogalmazás

> A DevOps a fejlesztés és üzemeltetés együttműködésére épülő szemlélet,
> amely kultúrát, folyamatokat, gyakorlatokat
> és eszközöket egyaránt magában foglal.  
> Célja, hogy a szoftver gyorsabban, megbízhatóbban és nagyobb automatizáltsággal jusson el a felhasználókhoz.  
> A DevOps fontos elemei közé tartozik például a verziókezelés,
> a CI/CD, az infrastruktúra automatizálása,
> a monitorozás és a folyamatos visszacsatolás.

## Gyors önellenőrzés

1. Mi a DevOps lényege?
2. Miért nem csak eszközökről szól?
3. Mi a kapcsolata a CI/CD-vel?
4. Miért segíti a gyorsabb szállítást?
5. Mondj négy tipikus DevOps-elemet.

## Rövid válaszok az önellenőrzéshez

1. Fejlesztés és üzemeltetés összekapcsolása
2. Mert kultúra és folyamat is kell hozzá
3. A CI/CD a DevOps egyik fontos része
4. Mert több automatizálást és gyors feedbacket ad
5. Git, CI/CD, monitoring, automatizálás

## Források

- [Microsoft Learn: What is DevOps?](https://learn.microsoft.com/en-us/devops/what-is-devops)  
  DevOps-gyakorlatok, folyamatos integráció és szállítás.

- [Microsoft: Safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)  
  Telepítés utáni ellenőrzés és megtervezett helyreállítás.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Microsoft Learn - What is DevOps?  
   https://learn.microsoft.com/en-us/devops/what-is-devops  
   Használat: hivatalos, jól strukturált meghatározás és életciklus-szemlélet.

2. AWS - DevOps and AWS  
   https://aws.amazon.com/devops/  
   Használat: hivatalos, gyakorlati összefoglaló a DevOps kultúra, gyakorlatok és automatizálás kapcsolatáról.

Megnyitva: `2026-04-08`
