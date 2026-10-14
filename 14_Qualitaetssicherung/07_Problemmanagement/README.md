# Problemmanagement

## Gyors vizuális kép

```text
Incidens / ismétlődő hiba
    -> okok vizsgálata
    -> gyökérok meghatározása
    -> tartós megoldás
    -> megelőzés
```

## Mi az a problem management?

Ez egy olyan folyamat, amely:

- azonosítja egy vagy több incidens tényleges vagy lehetséges okait
- megvizsgálja az okokat
- megkeresi a gyökérokot
- tartós javítást vagy megelőző intézkedést kezdeményez

## Miért fontos?

- csökkenti az ismétlődő hibákat
- javítja a szolgáltatás stabilitását
- csökkenti az üzemeltetési terhelést
- segít tanulni a korábbi hibákból

## Problem és incident: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| incident | gyors helyreállítás, szolgáltatás-visszaállítás |
| problem | kiváltó ok feltárása és megelőzés |

Egy incidenst gyorsan kezelni kell, a problem management pedig azt vizsgálja, miért történt meg.

## Tipikus lépések

- probléma azonosítása
- adatok és minták gyűjtése
- gyökérokelemzés
- workaround vagy végleges megoldás
- dokumentálás és tanulságok

## Visszatérő tárhelyriasztás okának vizsgálata

A szolgáltatás leáll, mert megtelt a lemez. Az incidenskezelés első feladata a szolgáltatás biztonságos helyreállítása, a szükséges bizonyítékok megőrzésével. A problem management azt kutatja, miért nőtt korlátlanul a tárhelyhasználat.

A mérések szerint egy importáló hibás kérése ugyanazt az üzenetet ismétli, a naplón nincs forgatás, és a riasztás túl későn szól. Több közreható ok van. A tartós intézkedés az importáló javítása, méretezett naplóforgatás és korábbi kapacitásriasztás. Mindegyikhez felelőst és ellenőrzési időpontot rendelünk. A naplózást egyszerűen kikapcsolni elveszítené a későbbi vizsgálat lehetőségét.

A kerülőmegoldás, workaround átmenetileg enyhíti a hatást, de nem feltétlenül szünteti meg az okot. Az elemzésnek nem kell több azonos incidensre várnia: egyetlen súlyos eset vagy előre felismert lehetséges ok is indokolhatja. A tanulság a rendszer javítására, nem egy ember hibáztatására irányul.

## Vizsgán jól használható megfogalmazás

> A problem management célja a problémák kiváltó okának feltárása és a hasonló hibák jövőbeni megelőzése.  
> Nemcsak a tünetek gyors kezelésére koncentrál, hanem a háttérben álló okok elemzésére is.  
> Ezért a problem management fontos része a tartós minőségjavításnak és a stabil működésnek.

## Gyors önellenőrzés

1. Mi a problem management fő célja?
2. Mi a különbség közte és az incident management között?
3. Miért fontos a gyökérok keresése?
4. Milyen előnye van hosszú távon?
5. Mi lehet a folyamat eredménye?

## Rövid válaszok az önellenőrzéshez

1. A kiváltó ok feltárása és megelőzés
2. Az incident gyors helyreállítást céloz, a problem az okot keresi
3. Mert így megelőzhető az ismétlődés
4. Stabilabb működés és kevesebb visszatérő hiba
5. Workaround, végleges javítás vagy megelőző intézkedés

## Források

- [Atlassian: Problem and incident management](https://www.atlassian.com/incident-management/devops/incident-vs-problem-management)  
  Egy vagy több incidens tényleges vagy lehetséges okának kezelése.

- [Google SRE: Postmortem culture](https://sre.google/sre-book/postmortem-culture/)  
  Több közreható ok és nyomon követhető, hibáztatásmentes intézkedések.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Atlassian - Problem management in Jira Service Management  
   https://www.atlassian.com/software/jira/service-management/product-guide/getting-started/problem-management  
   Használat: modern, hivatalos összefoglaló a problem management céljáról és működéséről.

2. Atlassian - Problem management vs. incident management  
   https://www.atlassian.com/incident-management/devops/incident-vs-problem-management  
   Használat: jól használható forrás a problem és incident management különbségének tisztázásához.

Megnyitva: `2026-04-08`
