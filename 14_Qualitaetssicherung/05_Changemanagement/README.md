# Changemanagement

## Gyors vizuális kép

```text
Változtatási igény
    -> értékelés
    -> jóváhagyás
    -> bevezetés
    -> ellenőrzés / visszajelzés
```

## Mi az a change management?

Ez egy folyamat arra, hogy a változások:

- átláthatók legyenek
- ne okozzanak felesleges kiesést
- megfelelően legyenek dokumentálva
- kontrolláltan kerüljenek be a rendszerbe

## Miért fontos?

- csökkenti az üzemzavar esélyét
- segít felmérni a kockázatot
- támogatja a felelősségek tisztázását
- megkönnyíti a visszakövethetőséget

## Tipikus lépések

- változtatási igény rögzítése
- hatásvizsgálat
- prioritás és kockázat meghatározása
- jóváhagyás
- megvalósítás
- utólagos ellenőrzés

## Mire kell figyelni?

- legyen világos, mit változtatunk
- legyen ismert a kockázat
- legyen rollback vagy vészforgatókönyv
- legyen kommunikáció az érintettek felé

## Change management és problem management: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| change management | változások kontrollált bevezetése |
| problem management | hibák és kiváltó okok feltárása, megelőzés |

## Adatbázis-változtatás ellenőrizhető lépésekben

Egy új mező szükséges a foglalásokhoz. A változtatási kérés megadja a célt, az érintett alkalmazásverziót, a várható zárolást és azt, hogyan működik együtt a régi és az új kód. Tesztkörnyezetben ellenőrizzük a migrációt és a helyreállítás eljárását; a mentés megléte önmagában még nem bizonyítja a visszaállíthatóságot.

A bevezetési tervben szerepel a felelős, az időablak, a siker ellenőrzése és az a feltétel, amikor megállunk. Ha a változtatás adatot töröl vagy átalakít, a régi program visszatelepítése nem feltétlenül elég. Ilyenkor adat-helyreállítás vagy előre haladó javítás is szükséges lehet, ismert adatvesztési kockázattal.

A jóváhagyás arányos a kockázattal. Egy előre engedélyezett, ismételhető kis változásnak lehet egyszerűbb útja; egy sürgős javításnak is kell felelőse, dokumentációja és utólagos ellenőrzése. Ez a téma a technikai változásbevezetésről szól; a munkatársak változásra felkészítése kapcsolódó, külön feladat.

## Vizsgán jól használható megfogalmazás

> A change management célja,
> hogy a rendszert érintő változtatások tervezetten,
> jóváhagyott módon és kockázatkezeléssel történjenek.  
> Segítségével csökkenthető a kiesések, hibák és nem kívánt mellékhatások esélye.  
> A folyamat tipikusan tartalmazza a változtatási igény rögzítését,
> értékelését, jóváhagyását,
> végrehajtását és utólagos ellenőrzését.

## Gyors önellenőrzés

1. Mi a change management fő célja?
2. Miért fontos a kockázatértékelés?
3. Milyen lépések szoktak benne lenni?
4. Miért kell előre kidolgozott helyreállítási terv?
5. Miben különbözik a problem managementtől?

## Rövid válaszok az önellenőrzéshez

1. Kontrollált változásbevezetés
2. Mert a változás hibát vagy kiesést okozhat
3. Rögzítés, értékelés, jóváhagyás, bevezetés, ellenőrzés
4. Hogy probléma esetén ismert, tesztelt eljárással lehessen helyreállítani; adatváltozásnál ez több lehet a régi kód visszarakásánál.
5. Az egyik változást kezel, a másik okokat és ismétlődő hibákat

## Források

- [Atlassian: Change management](https://support.atlassian.com/jira-service-management-cloud/docs/what-is-change-management/)  
  Kontrollált technikai változtatások és kockázatalapú folyamat.

- [Microsoft: Safe deployments](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments)  
  Tesztelt bevezetés és helyreállítás, adatváltozások figyelembevételével.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Atlassian Support - What is change management?  
   https://support.atlassian.com/jira-service-management-cloud/docs/what-is-change-management/  
   Használat: modern, hivatalos összefoglaló a change management céljáról és előnyeiről.

2. Atlassian - Jira Service Management features  
   https://support.atlassian.com/jira-service-management-cloud/docs/get-to-know-the-main-jira-service-management-features/  
   Használat: hivatalos háttér az ITSM gyakorlatok, köztük a change management elhelyezéséhez.

Megnyitva: `2026-04-08`
