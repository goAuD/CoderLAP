# Schreibtischtest

## Lényeg 30 másodpercben

A **Schreibtischtest** alatt vizsgakörnyezetben általában egy **kézi logikai ellenőrzést** értünk: a program futtatása nélkül végiggondoljuk, mi történne a kóddal vagy algoritmussal.

Röviden:

- fejben vagy papíron követjük a lépéseket
- korán észrevehetők logikai hibák
- nem helyettesíti a valódi futtatást és tesztelést

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

## Vizsgán jól használható megfogalmazás

> A Schreibtischtest egy kézi logikai ellenőrzés, amely során a programot vagy algoritmust futtatás nélkül, lépésről lépésre végigkövetjük.  
> Ilyenkor a bemenetek, elágazások, ciklusok és változóértékek alapján ellenőrizzük, hogy helyes eredmény várható-e.  
> Ez jó módszer a korai logikai hibák felismerésére, de nem helyettesíti a tényleges tesztelést.

## Gyakori vizsgahibák

- A Schreibtischtestet valódi programfuttatásnak nevezni.
- Nem megemlíteni a kézi, lépésenkénti ellenőrzést.
- Azt állítani, hogy minden hibatípust feltár.
- Összekeverni a code review-val.

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

1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos háttér a statikus teszteléshez és review-jellegű korai ellenőrzésekhez.

2. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Használat: hivatalos fogalmi háttér a statikus ellenőrzési technikákhoz.

Megjegyzés: a `Schreibtischtest` megfogalmazása itt a vizsgagyakorlatban használt, kézi `dry run` / logikai végigkövetés értelmezését követi.

Megnyitva: `2026-04-08`
