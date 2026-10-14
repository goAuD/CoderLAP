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
| aszinkron | a befejezés későbbi jelzéssel érkezik; önmagában nem tesz minden kódot nem blokkolóvá |
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

## Adatfolyam szűréssel és átalakítással

**Feladat:** az `1, 2, 3, 4` perces tanulási szakaszok közül csak a legalább
háromperceseket tartsuk meg, és másodpercben adjuk tovább. Ez valódi RxJS-példa.
Futtatásához külön gyakorló Node-projektben `rxjs@7.8.2` és egy `.mjs` fájl kell;
a CoderLAP használatához nem szükséges ezt a csomagot telepíteni.

```javascript
import { from, filter, map } from "rxjs";

from([1, 2, 3, 4]).pipe(
  filter((minutes) => minutes >= 3),
  map((minutes) => minutes * 60),
).subscribe({
  next: (seconds) => console.log(seconds),
  error: (error) => console.error(error.message),
  complete: () => console.log("done"),
});
```

```text
180
240
done
```

A `from` a bemeneti értékeket szolgáltatja, a `filter` megtartja a `3` és `4`
értéket, a `map` ezekből `180` és `240` másodpercet számít. A `subscribe` indítja
el ezt a forrást. A `next` az értékeket, az `error` a hibás lezárást, a `complete`
a sikeres befejezést kezeli. Ez az adatfolyam **szinkron**: a reaktív modell
önmagában nem jelent késleltetést vagy párhuzamos szálakat.

Egy billentyűeseményekből készített keresési folyam viszont időben érkező
értékeket kezelhet. Ilyenkor hasznos a gépelési szünet megvárása, a korábbi
elavult kérés eredményének elhagyása és a feliratkozás lezárása, amikor a felület
megszűnik. Gyors forrásnál a feldolgozási sebesség és a puffer mérete is számít.

A Reactive Manifesto a **teljes rendszerek** tulajdonságait írja le. Egy Observable
használatától önmagában még nem lesz a rendszer hibatűrő vagy rugalmasan skálázódó.

## Vizsgán jól használható megfogalmazás

> A reaktív programozás olyan fejlesztési megközelítés, amely adatfolyamokra, eseményekre és azok kezelésére épül.  
> A rendszer nemcsak utasításokat hajt végre sorban, hanem a beérkező változásokra és üzenetekre reagál.  
> Ez különösen hasznos aszinkron, valós idejű vagy skálázható rendszereknél.

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

Ellenőrizve: `2026-10-14`.

- [RxJS: Observable guide source](https://github.com/ReactiveX/rxjs/blob/7.8.2/docs_app/content/guide/observable.md): szinkron és aszinkron Observable, next/error/complete.
- [Reactive Manifesto](https://reactivemanifesto.org/): rendszerszintű reaktív tulajdonságok.


1. The Reactive Manifesto  
   https://reactivemanifesto.org/  
   Használat: a reaktív rendszerek alapelveinek hivatalos leírása.

2. ReactiveX  
   https://reactivex.io/  
   Használat: a reaktív programozás gyakorlati, esemény- és adatfolyam-alapú modelljének ismert hivatalos ökoszisztémája.

Megnyitva: `2026-04-08`
