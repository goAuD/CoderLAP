# Rekursive Funktionen

## Gyors vizuális kép

```text
függvény(n)
    -> ha alapeset, megáll
    -> különben hívja önmagát kisebb problémával
```

## Mi a rekurzió lényege?

Rekurzióról akkor beszélünk, ha egy függvény:

- saját magát hívja
- egy kisebb vagy egyszerűbb részproblémával
- addig, amíg el nem ér egy alapesetet

## A rekurzió két kötelező része

| Rész | Miért kell? |
|---|---|
| alapeset | megállítja a folyamatot |
| rekurzív eset | tovább bontja a problémát |

Ha nincs jó alapeset, könnyen végtelen rekurzió lesz.

## Egyszerű példa

Faktoriális:

```text
fact(0) = 1
fact(n) = n * fact(n - 1)
```

Itt:

- az alapeset: `n = 0`
- a rekurzív lépés: `fact(n - 1)`

## Mikor hasznos?

- fa- vagy hierarchikus szerkezeteknél
- felosztásos algoritmusoknál
- matematikai definíciók megvalósításánál

## Előnyök

- tömör és elegáns lehet
- jól illik bizonyos problémákhoz
- közel marad a probléma természetes szerkezetéhez

## Hátrányok

- nehezebb lehet követni
- stacket használ
- túl mély hívási láncnál hibát okozhat
- néha lassabb vagy memóriaigényesebb, mint az iteráció

## Rekurzió és ciklus: ne keverd össze

| Fogalom | Lényeg |
|---|---|
| ciklus | ismétlés vezérlési szerkezettel |
| rekurzió | ismétlés önhívó függvénnyel |

Sok feladat megoldható mindkét módon, de nem mindig ugyanolyan jól.

## Vizsgán jól használható megfogalmazás

> A rekurzív függvény olyan függvény, amely önmagát hívja meg egy kisebb részprobléma megoldására.  
> A helyes működéshez mindig szükség van alapesetre és rekurzív esetre.  
> A rekurzió különösen hasznos hierarchikus vagy felosztásos problémáknál, de túl mély hívás esetén erőforrásgondokat is okozhat.

## Gyakori vizsgahibák

- Kihagyni az alapesetet.
- Azt állítani, hogy a rekurzió mindig jobb, mint a ciklus.
- Nem megemlíteni a stackhasználatot.
- A rekurziót sima függvényhívással összekeverni.

## Gyors önellenőrzés

1. Mi a rekurzív függvény?
2. Mi az alapeset szerepe?
3. Mi a rekurzív eset szerepe?
4. Miben különbözik a ciklustól?
5. Milyen kockázata lehet?

## Rövid válaszok az önellenőrzéshez

1. Olyan függvény, ami önmagát hívja
2. Leállítja a folyamatot
3. Tovább bontja a problémát
4. A rekurzió önhívással ismétel
5. Túl mély hívási lánc és nagy stackhasználat

## Források

1. MDN - Recursion  
   https://developer.mozilla.org/en-US/docs/Glossary/Recursion  
   Használat: modern, hivatalos fogalmi forrás a rekurzió alapjához.

2. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Használat: kiegészítő, hivatalos magyarázat a rekurzív függvények gyakorlati működéséhez.

Megnyitva: `2026-04-09`
