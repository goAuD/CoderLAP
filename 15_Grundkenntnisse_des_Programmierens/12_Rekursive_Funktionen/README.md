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

## A hívások visszatérése is része a megoldásnak

Feladat: a `0..12` tartomány egész számainak faktoriálisa. A tudatos korlát
rövid hívási láncot és pontos egész eredményt ad. A JavaScript-példa Node.js-ben fut.

<!-- example:run -->

```javascript
function factorial(n) {
  if (!Number.isInteger(n) || n < 0 || n > 12) {
    throw new RangeError("n must be an integer from 0 to 12");
  }
  if (n === 0) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(4));
console.log(factorial(0));
```

```text
24
1
```

| Hívás | Mire vár? | Visszaadott érték |
|---|---|---|
| `factorial(0)` | semmire, alapeset | `1` |
| `factorial(1)` | `1 * factorial(0)` | `1` |
| `factorial(2)` | `2 * factorial(1)` | `2` |
| `factorial(3)` | `3 * factorial(2)` | `6` |
| `factorial(4)` | `4 * factorial(3)` | `24` |

A hívások lefelé `4, 3, 2, 1, 0` sorrendben keletkeznek, az eredmények visszafelé
épülnek fel. Minden hívásnak saját `n` paramétere van. Az alapeset mellett azt is
igazoljuk, hogy a következő hívás közelebb kerül hozzá. A példában az egész `n`
mindig eggyel csökken. Idő és hívási verem: `O(n)`. Iteratív megoldás ugyanezt
egy akkumulátorral, `O(1)` segédmemóriával megoldhatja. Közvetett rekurzió is
létezik, amikor egy függvény más függvényen keresztül jut vissza saját magához.

## Vizsgán jól használható megfogalmazás

> A rekurzív függvény olyan függvény, amely önmagát hívja meg egy kisebb részprobléma megoldására.  
> A helyes működéshez mindig szükség van alapesetre és rekurzív esetre.  
> A rekurzió különösen hasznos hierarchikus vagy felosztásos problémáknál, de túl mély hívás esetén erőforrásgondokat is
> okozhat.

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

Ellenőrizve: `2026-10-14`.

- [MDN: Recursion](https://developer.mozilla.org/en-US/docs/Glossary/Recursion): alapeset, hívási verem és visszatérés.


1. MDN - Recursion  
   https://developer.mozilla.org/en-US/docs/Glossary/Recursion  
   Használat: modern, hivatalos fogalmi forrás a rekurzió alapjához.

2. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Használat: kiegészítő, hivatalos magyarázat a rekurzív függvények gyakorlati működéséhez.

Megnyitva: `2026-04-09`
