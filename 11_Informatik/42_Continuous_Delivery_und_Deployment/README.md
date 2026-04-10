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
- a rendszer automatikusan telepíti az új verziót a célkörnyezetbe

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

## Vizsgán jól használható megfogalmazás

> A Continuous Delivery azt jelenti, hogy a szoftver folyamatosan kiadható állapotban van, de a végső éles kiadás előtt még lehet manuális jóváhagyás.  
> A Continuous Deployment ennél tovább megy: ha a pipeline minden feltétele teljesül, a rendszer automatikusan telepíti az új verziót.  
> A két fogalom közötti fő különbség tehát az, hogy deployment esetén az élesbe juttatás is automatizált.

## Gyakori vizsgahibák

- A deliveryt és deploymentet ugyanannak nevezni.
- Nem megemlíteni a manuális jóváhagyás lehetőségét delivery esetén.
- Azt hinni, hogy automation nélkül is ugyanaz a fogalom.
- Nem beszélni a tesztelés és rollback fontosságáról.

## Gyors önellenőrzés

1. Mi a Continuous Delivery lényege?
2. Mi a Continuous Deployment lényege?
3. Mi a fő különbség köztük?
4. Miért fontos a jó tesztelés?
5. Miért kell rollback terv?

## Rövid válaszok az önellenőrzéshez

1. Mindig kiadható állapotban tartja a szoftvert
2. Automatikusan telepít is
3. A deployment az élesbe jutást is automatizálja
4. Mert különben hibás verzió mehet tovább
5. Hogy hiba esetén gyorsan vissza lehessen állni

## Források

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
