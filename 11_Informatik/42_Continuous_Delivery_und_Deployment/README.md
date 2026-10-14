# Continuous Delivery und Deployment

## Gyors vizuális kép

| Szint | Meddig automatikus? |
|---|---|
| CI | build és teszt |
| Continuous Delivery | build, teszt, csomagolás, kiadható állapot |
| Continuous Deployment | build, teszt után automatikus telepítés is |

## Mi a Continuous Delivery?

Lényege:

- a szoftver folyamatosan olyan állapotban van, hogy kiadható legyen
- az éles kiadás előtt gyakran marad egy kontrollált, emberi döntési pont

## Mi a Continuous Deployment?

Lényege:

- ha a pipeline feltételei teljesülnek
- a rendszer automatikusan telepíti az új verziót az éles környezetbe

Ez nagy automatizáltságot és nagy bizalmat igényel a tesztekben.

## Miért fontos a különbség?

Mert vizsgán gyakran ezt kérdezik:

- delivery = "mindig kiadható"
- deployment = "automatikusan ki is adja"

## Előnyök

- gyorsabb szállítás
- kisebb csomagokban történő változás
- kevesebb manuális hiba
- gyorsabb visszajelzési ciklus

## Kockázatok

- gyenge tesztelés mellett veszélyes
- rossz pipeline esetén hibás verzió is kijuthat
- kell rollback és monitorozás

## Ugyanaz a kiadás menjen a tesztből az éles rendszerbe

**Példa:** elkészül egy `quiz-1.4.0` nevű csomag, ismert commitból. A tesztkörnyezet
ezt a csomagot kapja meg. A kiadáskor ugyanennek az ellenőrzött artifactnak
az éles telepítése történik, nem egy új, közben megváltozott függőségekből
véletlenszerűen újraépített változaté.

```text
commit -> build -> tesztek -> verziózott artifact -> staging
  -> ellenőrzés -> [emberi kiadási döntés] -> production
```

Ez **Continuous Delivery** lehet: a telepítés automatizált és ismételhető,
de az éles kiadás időpontjáról ember dönt. **Continuous Deployment** esetén
a megfelelő automatikus ellenőrzések után ez az emberi kiadási kapu is elmarad.
Attól, hogy stagingre automatikusan telepítünk, még nem lesz automatikus az
éles kiadás.

| Fogalom | Ebben a példában |
|---|---|
| build | létrejön az artifact |
| deployment | az artifact a célkörnyezetbe kerül |
| release | a funkciót elérhetővé tesszük a felhasználóknak |
| rollback | korábbi működő változatra váltunk, ha a rendszer állapota ezt megengedi |

Deployment és release feature flaggel szétválasztható: a kód már települt,
de egy funkció még nincs bekapcsolva. A konfigurációt és titkokat környezetenként
kezeljük, nem építjük az ügyfélnek küldött csomagba.

Telepítés után rövid működési próbával és a hibajelzések figyelésével ellenőrizzük
a rendszert. Egy adatbázis-oszlop törlését a régi alkalmazás visszamásolása nem
fordítja vissza. Ilyenkor előre tervezett, kompatibilis migráció, kipróbált mentés
és szükség esetén javító új kiadás kell. A rollback terv tehát a kód mellett az
adatok és konfiguráció állapotát is figyelembe veszi.

## Vizsgán jól használható megfogalmazás

> A Continuous Delivery azt jelenti,
> hogy a szoftver folyamatosan kiadható állapotban van,
> de a végső éles kiadás előtt még lehet manuális jóváhagyás.  
> A Continuous Deployment ennél tovább megy:
> ha a pipeline minden feltétele teljesül,
> a rendszer automatikusan telepíti az új verziót.  
> A fő különbség az emberi kiadási döntés: Continuous Deployment esetén a sikeres automatikus ellenőrzések után nincs külön manuális élesítési kapu. A telepítés technikai lépései Continuous Delivery mellett is lehetnek automatizáltak.

## Gyors önellenőrzés

1. Mi a Continuous Delivery lényege?
2. Mi a Continuous Deployment lényege?
3. Mi a fő különbség köztük?
4. Miért fontos a jó tesztelés?
5. Miért kell rollback terv?

## Rövid válaszok az önellenőrzéshez

1. Mindig kiadható állapotban tartja a szoftvert
2. Automatikusan telepít is
3. Continuous Deploymentnél az automatikus ellenőrzések után nincs kiadásonkénti emberi élesítési kapu
4. Mert különben hibás verzió mehet tovább
5. Hogy hiba esetén gyorsan vissza lehessen állni

## Források

Ellenőrizve: `2026-10-14`.

- [Microsoft: Continuous delivery](https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery): szállítható állapot, környezetek és automatizált folyamat.
- [GitHub: Reviewing deployments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments): konkrét emberi jóváhagyási kapu.


1. GitHub Docs - Continuous deployment  
   https://docs.github.com/en/actions/get-started/continuous-deployment  
   Használat: a deployment automatizálás modern, hivatalos példája.

2. Reviewing deployments - GitHub Docs  
   https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments  
   Használat: hivatalos példa arra, hogyan illeszthető jóváhagyási lépés a szállításba.

3. Microsoft Learn - DevOps concepts for continuous delivery  
   https://learn.microsoft.com/en-us/devops/deliver/what-is-continuous-delivery  
   Használat: a continuous delivery fogalmának hivatalos, Microsoft-féle összefoglalója.

Megnyitva: `2026-04-08`
