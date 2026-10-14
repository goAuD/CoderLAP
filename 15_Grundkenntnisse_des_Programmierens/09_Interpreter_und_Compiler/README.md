# Interpreter und Compiler

## Gyors vizuális kép

| Eszköz | Alapötlet |
|---|---|
| interpreter | a kódot közvetlenebbül értelmezi és hajtja végre |
| compiler | a kódot más formára, gyakran gépi kódra fordítja |

## Mi az a compiler?

A compiler:

- beolvassa a forráskódot
- elemzi a nyelvi szerkezetet
- lefordítja egy másik formára

Ez lehet:

- gépi kód
- bájtkód
- vagy valamilyen köztes reprezentáció

## Mi az az interpreter?

Az interpreter a kódot közvetlenebb módon dolgozza fel, és a futtatás szorosabban kapcsolódik az értelmezéshez.

Ez sokszor:

- rugalmasabb fejlesztést tesz lehetővé
- gyors kipróbálást támogat
- de nem ugyanúgy működik, mint egy klasszikus előre fordító compiler

## A modern valóság: nem mindig fekete-fehér

Ma sok platform:

- fordít is
- értelmez is
- vagy `JIT`-et, azaz futás közbeni fordítást használ

Ezért vizsgán az alapelvet kell tudni, nem egy leegyszerűsítő mítoszt.

## Előnyök és hátrányok röviden

| Szempont | Interpreter | Compiler |
|---|---|---|
| gyors kipróbálás | gyakran előny | változó |
| fordítás időpontja | értelmezéssel végrehajt | futtatás előtt (AOT) vagy közben (JIT) |
| futási teljesítmény | változó | gyakran kedvező |
| hibák észlelése | sokszor futás közben is | sok hiba már fordításkor kijöhet |

## Compiler, interpreter, assembler: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| compiler | magas szintű nyelvet fordít |
| interpreter | közvetlenebbül értelmez és hajt végre |
| assembler | assembly nyelvet alakít gépközeli formára |

## A fordítás és a végrehajtás külön lépés

| Példa | Jellemző feldolgozás |
|---|---|
| C natív program | előfeldolgozás, fordítás, assembly, objektumfájl, linkelés |
| Java | forrásból bájtkód, majd a JVM végrehajtja; JIT is használható |
| JavaScript V8-ban | elemzés, bájtkód, interpreter és futás közbeni fordítási fokozatok |

A **linker** összeállítja az objektumfájlokat és feloldja a köztük lévő
hivatkozásokat. Egy elkészült programnak ettől még lehet szüksége futtatókörnyezetre
vagy dinamikus könyvtárra. A **JIT compiler** valódi fordító, csak futás közben
dolgozik; ezért a „compiler mindig előre fordít” megfogalmazás túl szűk.

A fordítás sikere a nyelvi ellenőrzésekről ad információt, nem bizonyítja az
üzleti szabály helyességét. Egy helyesen forduló program is számolhat téves
szállítási díjat. A szintaxis ellenőrzése, a futásidejű ellenőrzés és az elvárt
eredmény tesztelése egymást kiegészítő lépések.

## Vizsgán jól használható megfogalmazás

> A compiler a kódot másik reprezentációra fordítja, például gépi kódra vagy bájtkódra; ez történhet a futtatás előtt vagy közben.  
> Az interpreter ezzel szemben a kód végrehajtását közvetlenebb módon, az értelmezéssel együtt végzi.  
> A modern rendszerekben a két megközelítés gyakran keveredik, de az alapvető különbség továbbra is a kód más reprezentációra alakítása és
> a közvetlen végrehajtás között van.

## Gyors önellenőrzés

1. Mi a compiler fő feladata?
2. Mi az interpreter fő jellemzője?
3. Miért nem teljesen fekete-fehér ma a kép?
4. Mi a különbség compiler és assembler között?
5. Milyen hibák jelenhetnek meg már fordításkor?

## Rövid válaszok az önellenőrzéshez

1. A forráskód lefordítása
2. Közvetlenebb értelmezés és végrehajtás
3. Mert vannak hibrid és JIT rendszerek
4. A compiler magas szintű nyelvvel, az assembler assemblyvel dolgozik
5. Szintaktikai és bizonyos szerkezeti hibák

## Források

Ellenőrizve: `2026-10-14`.

- [V8: Ignition](https://v8.dev/docs/ignition): interpreter a modern JavaScript-motorban.
- [V8: Sparkplug](https://v8.dev/blog/sparkplug): futás közbeni fordítási fokozat.


1. Python Docs - Using the Python Interpreter  
   https://docs.python.org/3/tutorial/interpreter.html  
   Használat: hivatalos forrás az interpreter-alapú futtatás működéséhez.

2. GCC - Overall Options  
   https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html  
   Használat: hivatalos háttér a fordítási folyamat lépéseihez és a compiler működéséhez.

Megnyitva: `2026-04-09`
