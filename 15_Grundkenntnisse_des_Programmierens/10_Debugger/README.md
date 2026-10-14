# Debugger

## Gyors vizuális kép

| Funkció | Mire jó? |
|---|---|
| breakpoint | megállítja a futást egy ponton |
| step into / over | lépésenkénti végrehajtás |
| variable inspection | változóértékek megfigyelése |
| call stack | megmutatja, honnan jutottunk ide |

## Mi az a debugger?

A debugger egy hibakereső eszköz.

Segít:

- megfigyelni a program futását
- megállni kritikus pontokon
- ellenőrizni a belső állapotot
- megérteni a vezérlési utat

## Mire jó a gyakorlatban?

Például ha:

- a program rossz eredményt ad
- váratlanul leáll
- egy feltétel nem úgy működik, ahogy vártuk
- egy ciklus túl sokszor vagy végtelenül fut

## Tipikus debugger-fogalmak

### Breakpoint

Előre beállított megállási pont.

### Step

Lépésenkénti futtatás:

- belépés függvénybe
- soron következő lépés
- továbbfutás a következő breakpointig

### Watch

Bizonyos változók figyelése.

### Call stack

Megmutatja, milyen hívási láncon keresztül jutottunk az aktuális pontra.

## Debugger és logolás: ne keverd össze

| Fogalom | Mire jó? |
|---|---|
| debugger | interaktív futásfigyelés |
| logolás | események és állapotok naplózása |

A kettő együtt a leghasznosabb.

## Megfigyelési feladat helyes programon

A következő Node.js-ben vagy böngészőkonzolban futtatható kód két egész
centértéket összegez. Mentsd fájlba, és a szerkesztő debuggerével tegyél
breakpointot a `total += price` sorra.

<!-- example:run -->

```javascript
function subtotal(prices) {
  let total = 0;
  for (const price of prices) {
    total += price;
  }
  return total;
}
console.log(subtotal([200, 350]));
```

```text
550
```

Az első megálláskor `total = 0`, `price = 200`; a kiemelt sor még nem futott le.
Egy lépés után `total = 200`. A második megálláskor `price = 350`, utána a
végösszeg `550`. A Watch mezőben például a `total` kifejezést figyelhetjük.

| Művelet | Mit hajt végre? |
|---|---|
| Step into | belép a következő függvényhívásba |
| Step over | végrehajtja a hívást, de nem járja be soronként |
| Step out | befejezi az aktuális függvényt, majd a hívónál áll meg |
| Resume | továbbfut a következő megállási feltételig |

A feltételes breakpoint csak például `price > 300` esetén állítja meg a futást.
Ez hosszú ciklusban hasznos. A hibakeresőben látott személyes vagy titkos adatot
nem másoljuk automatikusan naplóba; a megfigyeléshez elég lehet a típus vagy egy
személytelenített próbaadat.

## Vizsgán jól használható megfogalmazás

> A debugger egy hibakereső eszköz, amely lehetővé teszi a program futásának megfigyelését és vezérlését.  
> Segítségével breakpointokat állíthatunk be, lépésenként futtathatjuk a kódot, megfigyelhetjük a változók értékét és  
> elemezhetjük a hívási láncot.  
> Ez különösen hasznos logikai hibák és futás közbeni problémák feltárásában.

## Gyors önellenőrzés

1. Mi a debugger fő feladata?
2. Mire jó a breakpoint?
3. Miért hasznos a step-by-step futtatás?
4. Mit mutat a call stack?
5. Mi a különbség debugger és logolás között?

## Rövid válaszok az önellenőrzéshez

1. A futás megfigyelése és hibakeresés
2. Megállítja a programot egy ponton
3. Mert követhető a valódi futás
4. A hívások láncát
5. Az egyik interaktív, a másik naplózás

## Források

Ellenőrizve: `2026-10-14`.

- [Chrome DevTools: Debug JavaScript](https://developer.chrome.com/docs/devtools/javascript): léptetés, breakpoint és Watch.


1. GDB - Debugging with GDB  
   https://sourceware.org/gdb/current/onlinedocs/gdb.pdf  
   Használat: hivatalos, elsődleges forrás a debugger céljához és alapműveleteihez.

2. MDN - debugger statement  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger  
   Használat: jól szemlélteti a debugger gyakorlati szerepét breakpoint-szerű megállási pontként.

Megnyitva: `2026-04-09`
