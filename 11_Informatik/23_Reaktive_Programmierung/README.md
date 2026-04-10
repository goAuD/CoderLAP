# Reaktive Programmierung

## Gyors vizuális kép

| Klasszikus szemlélet | Reaktív szemlélet |
|---|---|
| kérdezek és várok | esemény érkezik, reagálok |
| közvetlen hívások | adatfolyamok, üzenetek |
| blokkoló működés gyakori | aszinkron működés hangsúlyos |

## Mi a reaktív programozás lényege?

A reaktív programozásban gyakran:

- van egy adatforrás vagy eseményforrás
- a változások "folynak" a rendszeren
- más komponensek ezekre feliratkoznak és reagálnak

Tipikus helyzetek:

- UI-események kezelése
- valós idejű adatok
- aszinkron műveletek
- üzenetvezérelt architektúra

## Hol hasznos?

- frontend interakciók
- event-driven backendek
- streaming jellegű rendszerek
- nagy terhelésű, skálázandó szolgáltatások

## A reaktív rendszerek fő jellemzői

A reaktív szemlélethez gyakran ezeket a tulajdonságokat társítják:

- `Responsive` = gyors válasz
- `Resilient` = hibatűrés
- `Elastic` = rugalmas skálázódás
- `Message Driven` = üzenetvezérelt működés

## Reaktív és aszinkron: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| aszinkron | nem blokkoló, később érkező eredmény |
| reaktív | eseményekre és adatfolyamokra épülő szemlélet |

Az aszinkron működés gyakran része a reaktív rendszereknek, de nem ugyanaz.

## Mi az előnye?

- jobb válaszkészség
- hatékonyabb erőforrás-használat
- jobban kezelhető párhuzamosság
- nagyobb rendszereknél jobb skálázhatóság

## Mire kell figyelni?

- A reaktív programozás gondolkodásmódja nehezebb lehet kezdetben.
- A hibakezelés és állapotkezelés bonyolultabbá válhat.
- Nem minden kis projekt igényel reaktív modellt.

## Vizsgán jól használható megfogalmazás

> A reaktív programozás olyan fejlesztési megközelítés, amely adatfolyamokra, eseményekre és azok kezelésére épül.  
> A rendszer nemcsak utasításokat hajt végre sorban, hanem a beérkező változásokra és üzenetekre reagál.  
> Ez különösen hasznos aszinkron, valós idejű vagy skálázható rendszereknél.

## Gyakori vizsgahibák

- A reaktív programozást egyszerűen csak "gyors programozásnak" nevezni.
- A reaktív és az aszinkron fogalmat teljesen azonosnak venni.
- Nem megemlíteni az eseményeket és adatfolyamokat.
- Nem mondani rá gyakorlati példát.

## Gyors önellenőrzés

1. Mi a reaktív programozás lényege?
2. Milyen helyzetekben hasznos?
3. Mi a kapcsolat az aszinkron működéssel?
4. Melyik négy jellemzőt emeli ki a Reactive Manifesto?
5. Mi lehet a nehézsége?

## Rövid válaszok az önellenőrzéshez

1. Eseményekre és adatfolyamokra reagáló működés
2. UI, streaming, backend integráció, valós idejű rendszerek
3. Gyakran együtt járnak, de nem ugyanazok
4. Responsive, Resilient, Elastic, Message Driven
5. Bonyolultabb modell és hibakezelés

## Források

1. The Reactive Manifesto  
   https://reactivemanifesto.org/  
   Használat: a reaktív rendszerek alapelveinek hivatalos leírása.

2. ReactiveX  
   https://reactivex.io/  
   Használat: a reaktív programozás gyakorlati, esemény- és adatfolyam-alapú modelljének ismert hivatalos ökoszisztémája.

Megnyitva: `2026-04-08`
