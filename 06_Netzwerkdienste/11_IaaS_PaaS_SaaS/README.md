# IaaS PaaS SaaS

## Lényeg 30 másodpercben

Az `IaaS`, `PaaS` és `SaaS` a cloud **szolgáltatási modelljei**.

Röviden:

- `IaaS` = infrastruktúrát kapsz
- `PaaS` = platformot kapsz fejlesztéshez / futtatáshoz
- `SaaS` = kész szoftvert használsz

## Gyors vizuális kép

| Modell | Mit kapsz? | Mire van több saját felelősség? |
|---|---|---|
| IaaS | VM, hálózat, tárhely | sok mindenre |
| PaaS | futtatási platform | kevesebbre |
| SaaS | kész alkalmazás | még kevesebbre |

## Mi az IaaS?

Az `Infrastructure as a Service` azt jelenti, hogy a szolgáltató alap infrastruktúrát ad:

- virtuális gépet
- hálózatot
- tárhelyet

Az ügyfélnek általában több dolgot kell kezelnie, például:

- operációs rendszert
- alkalmazást
- konfigurációt

## Mi a PaaS?

A `Platform as a Service` esetén a szolgáltató magasabb szintű környezetet ad.

Például:

- alkalmazásfuttató platform
- adatbázis-platform
- fejlesztői platform

Ilyenkor az ügyfél kevesebbet foglalkozik az alap infrastruktúrával.

## Mi a SaaS?

A `Software as a Service` kész alkalmazást jelent.

Például:

- online levelezés
- online irodai csomag
- felhős projektmenedzsment-eszköz

Itt a felhasználó tipikusan:

- csak használja a kész szoftvert

## Miért fontos?

Mert más lesz:

- az üzemeltetési felelősség
- a konfiguráció mélysége
- a rugalmasság
- a kontroll mértéke

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| IaaS / PaaS / SaaS | szolgáltatási modellek |
| private / public / hybrid | deployment modellek |

## Vizsgán jól használható megfogalmazás

> Az IaaS, PaaS és SaaS a cloud szolgáltatási modelljei.  
> IaaS esetén a szolgáltató főleg infrastruktúrát ad, PaaS esetén platformot biztosít az alkalmazások futtatásához, SaaS esetén pedig kész szoftvert használ a felhasználó.  
> Minél magasabb szintű a szolgáltatás, általában annál kevesebb technikai üzemeltetési feladat marad az ügyfélnél.

## Gyakori vizsgahibák

- Összekeverni a deployment modellekkel.
- Azt mondani, hogy a SaaS-nál nincs semmilyen ügyféloldali felelősség.
- Az IaaS-t és a PaaS-t ugyanannak tekinteni.
- Nem felismerni, hogy a kontroll és a felelősség mértéke modellenként változik.

## Gyors önellenőrzés

1. Mi az IaaS lényege?
2. Mi az a PaaS?
3. Mi az a SaaS?
4. Melyiknél kap a felhasználó kész alkalmazást?
5. Melyiknél marad több saját üzemeltetési feladat: IaaS vagy SaaS?

## Rövid válaszok az önellenőrzéshez

1. Infrastruktúra szolgáltatásként
2. Platform szolgáltatásként
3. Szoftver szolgáltatásként
4. A SaaS-nál
5. Az IaaS-nál

## Források

1. NIST SP 800-145 - The NIST Definition of Cloud Computing  
   https://csrc.nist.gov/pubs/sp/800/145/final  
   Használat: az IaaS, PaaS és SaaS elsődleges definíciói.

2. AWS - What is Cloud Computing?  
   https://aws.amazon.com/what-is-cloud-computing/  
   Használat: gyakorlati példák és modern szolgáltatói értelmezés.

3. AWS - Shared Responsibility Model  
   https://aws.amazon.com/compliance/shared-responsibility-model/  
   Használat: jól szemlélteti, hogy a felelősség hogyan változik a szolgáltatás absztrakciós szintjével.

Megnyitva: `2026-04-08`
