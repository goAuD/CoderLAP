# Schreibtischtest

## Gyors vizuális kép

```text
Bemenet megadása
    -> lépések kézi követése
    -> változók értékeinek figyelése
    -> eredmény ellenőrzése
```

## Mit jelent itt a Schreibtischtest?

Ez tipikusan azt jelenti, hogy:

- veszünk egy bemenetet
- lépésről lépésre végigkövetjük az algoritmust
- figyeljük a változók értékeit
- ellenőrizzük, hogy a várt eredmény jön-e ki

Gyakran nevezik:

- dry run-nak
- manual tracingnek
- kézi ellenőrzésnek

## Mire jó?

- egyszerű logikai hibák felismerésére
- ciklusok és elágazások megértésére
- algoritmusok ellenőrzésére
- tanulásra és vizsgafelkészülésre

## Mikor hasznos különösen?

- mielőtt még lefuttatnánk a programot
- ha egy algoritmust papíron kell bemutatni
- ha gyorsan akarjuk ellenőrizni a logikát

## Mit nem tud?

- nem mutat meg minden futási hibát
- nem váltja ki a valós tesztadatokkal végzett tesztelést
- nem helyettesíti az automatizált teszteket

## Schreibtischtest és code review: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| Schreibtischtest | egy algoritmus vagy kódrészlet kézi végigkövetése |
| code review | másik ember szakmai átnézése |

## Változókövetési táblázat egy ciklushoz

Először papíron kövesd végig a kódot, csak utána hasonlítsd össze a valódi futással:

<!-- example:run -->
```javascript
function sum(values) {
  let total = 0;
  for (let i = 0; i < values.length; i++) {
    total += values[i];
  }
  return total;
}

console.log(sum([2, 4, 1]));
console.log(sum([]));
```

```text
7
0
```

| Lépés | i | Feltétel | total a lépés után |
|---|---:|---|---:|
| inicializálás | 0 | még nem vizsgáltuk | 0 |
| első vizsgálat és hozzáadás | 0 | 0 < 3 igaz | 2 |
| második vizsgálat és hozzáadás | 1 | 1 < 3 igaz | 6 |
| harmadik vizsgálat és hozzáadás | 2 | 2 < 3 igaz | 7 |
| negyedik feltételvizsgálat | 3 | 3 < 3 hamis | 7 |

A ciklusmag háromszor fut, a feltételt négyszer vizsgáljuk. Az `i++` a ciklusmag után növeli az indexet. Üres listánál az első feltétel rögtön hamis, így a kezdő 0 tér vissza. Ez a kézi követés megmutatja a határokat, de a környezeti hibákat vagy a párhuzamos futás következményeit külön kell vizsgálni.

## Vizsgán jól használható megfogalmazás

> A Schreibtischtest egy kézi logikai ellenőrzés,
> amely során a programot vagy algoritmust futtatás nélkül,
> lépésről lépésre végigkövetjük.  
> Ilyenkor a bemenetek, elágazások, ciklusok és változóértékek alapján ellenőrizzük, hogy helyes eredmény várható-e.  
> Ez jó módszer a korai logikai hibák felismerésére, de nem helyettesíti a tényleges tesztelést.

## Gyors önellenőrzés

1. Mi a Schreibtischtest lényege?
2. Milyen hibákat segít felismerni?
3. Miért hasznos algoritmusoknál?
4. Miért nem elég önmagában?
5. Mi a különbség közte és a code review között?

## Rövid válaszok az önellenőrzéshez

1. Kézi logikai végigkövetés
2. Főleg logikai hibákat
3. Mert láthatóvá teszi a lépéseket és állapotokat
4. Mert nem valódi futtatás
5. Az egyik kézi dry run, a másik szakmai átnézés

## Források

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Statikus és dinamikus tesztelés, teszttervezési technikák és lefedettség.

- [MDN: for statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)  
  Inicializálás, feltétel és léptetés sorrendje.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos háttér a statikus teszteléshez és review-jellegű korai ellenőrzésekhez.

2. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Használat: hivatalos fogalmi háttér a statikus ellenőrzési technikákhoz.

Megjegyzés: a `Schreibtischtest` megfogalmazása itt
a vizsgagyakorlatban használt,
kézi `dry run` / logikai végigkövetés értelmezését követi.

Megnyitva: `2026-04-08`
