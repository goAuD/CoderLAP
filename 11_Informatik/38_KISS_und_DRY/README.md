# KISS und DRY

## Gyors vizuális kép

| Elv | Lényege |
|---|---|
| KISS | a legegyszerűbb, érthető megoldást keresd |
| DRY | a duplikációt csökkentsd, a közös logikát vond össze |

## Mi a KISS?

A KISS elv azt mondja, hogy a megoldás legyen:

- egyszerű
- jól érthető
- felesleges bonyolultságtól mentes

Ez nem azt jelenti, hogy primitív legyen, hanem azt, hogy:

- ne tervezz túl
- ne vezess be indokolatlan absztrakciókat
- ne oldj meg előre olyan problémát, ami még nincs

## Mi a DRY?

A DRY elv szerint a logikát nem szabad feleslegesen több helyen megismételni.

Ha ugyanaz a szabály több helyen szerepel, abból könnyen lesz:

- hibalehetőség
- nehézkes karbantartás
- inkonzisztens működés

## Miért fontosak együtt?

Mert a jó kód egyszerre:

- egyszerű
- nem fölöslegesen ismétlődő

De figyelem:

- a DRY túlzásba vitele néha túlbonyolított absztrakcióhoz vezethet

Ezért egyensúly kell.

## Gyakorlati példák

### KISS példa

Egy egyszerű `if`-ágas megoldás jobb lehet, mint egy túltervezett mintarendszer, ha a probléma kicsi.

### DRY példa

Ha ugyanaz a számítás vagy validáció három helyen szerepel, érdemes közös függvénybe tenni.

## KISS és DRY: ne keverd össze

| Elv | Mire figyel? |
|---|---|
| KISS | komplexitás csökkentése |
| DRY | ismétlés csökkentése |

## Mire kell figyelni?

- A túl sok absztrakció sértheti a KISS elvet.
- A másolás-beillesztés tipikusan sérti a DRY elvet.
- Nem minden hasonlóság valódi duplikáció.
- Néha egy kicsi ismétlés érthetőbb, mint egy rossz absztrakció.

## Vizsgán jól használható megfogalmazás

> A KISS elv szerint a megoldás legyen egyszerű és jól érthető, kerülve a felesleges bonyolultságot.  
> A DRY elv szerint ugyanazt a logikát
> nem szabad fölöslegesen több helyen ismételni,
> hanem célszerű közös absztrakcióba
> vagy függvénybe szervezni.  
> A jó fejlesztésben a két elvet együtt, egyensúlyban érdemes alkalmazni.

## Gyakori vizsgahibák

- A KISS-t "minimalista dizájnnal" összekeverni.
- A DRY-t minden apró hasonlóság erőltetett összevonásaként értelmezni.
- Nem beszélni az egyensúlyról.
- A másolást karbantartható megoldásnak nevezni.

## Gyors önellenőrzés

1. Mit jelent a KISS?
2. Mit jelent a DRY?
3. Miért veszélyes a duplikáció?
4. Miért lehet gond a túlzott absztrakció?
5. Hogyan függ össze a két elv?

## Rövid válaszok az önellenőrzéshez

1. Tartsd egyszerűen a megoldást
2. Ne ismételd a logikát feleslegesen
3. Mert hibát és nehéz karbantartást okoz
4. Mert rontja az érthetőséget
5. Együtt segítik a tisztább kódot

## Források

1. DevIQ - Keep It Simple  
   https://deviq.com/principles/keep-it-simple/  
   Használat: a KISS elv rövid, szakmai magyarázata.

2. DevIQ - Don't Repeat Yourself  
   https://deviq.com/principles/dont-repeat-yourself/  
   Használat: a DRY elv hivatalos jellegű, szakmai leírása.

3. DevIQ - Once and Only Once  
   https://deviq.com/principles/once-and-only-once/  
   Használat: a DRY elvhez kapcsolódó kiegészítő magyarázat.

Megnyitva: `2026-04-08`
