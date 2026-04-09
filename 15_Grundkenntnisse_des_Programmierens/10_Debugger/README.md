# Debugger

## Lényeg 30 másodpercben

A **debugger** olyan eszköz, amellyel futás közben meg lehet figyelni, hol és miért hibázik a program.

Röviden:

- meg lehet állítani a programot
- lépésenként lehet végrehajtani
- meg lehet nézni a változók értékét
- könnyebb megtalálni a hibák okát

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

## Vizsgán jól használható megfogalmazás

> A debugger egy hibakereső eszköz, amely lehetővé teszi a program futásának megfigyelését és vezérlését.  
> Segítségével breakpointokat állíthatunk be, lépésenként futtathatjuk a kódot, megfigyelhetjük a változók értékét és elemezhetjük a hívási láncot.  
> Ez különösen hasznos logikai hibák és futás közbeni problémák feltárásában.

## Gyakori vizsgahibák

- A debugger-t egyszerű hibaüzenet-olvasásnak tekinteni.
- Nem megemlíteni a breakpointot.
- Összekeverni a debugger-t a compilerrel.
- Elfelejteni a változófigyelés és call stack szerepét.

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

1. GDB - Debugging with GDB  
   https://sourceware.org/gdb/current/onlinedocs/gdb.pdf  
   Használat: hivatalos, elsődleges forrás a debugger céljához és alapműveleteihez.

2. MDN - debugger statement  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/debugger  
   Használat: jól szemlélteti a debugger gyakorlati szerepét breakpoint-szerű megállási pontként.

Megnyitva: `2026-04-09`
