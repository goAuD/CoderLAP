# LIFO und FIFO

## Gyors vizuális kép

| Elv | Jelentés | Tipikus adatszerkezet | Hétköznapi példa |
|---|---|---|---|
| LIFO | utolsó be, első ki | stack | tányérok egymáson |
| FIFO | első be, első ki | queue | sorban állás |

## Mi az a LIFO?

A LIFO elv szerint az a tétel kerül először feldolgozásra vagy kivételre, amelyik **legutóbb** került be.

Példa:

1. beteszed `A`
2. beteszed `B`
3. beteszed `C`
4. kivételkor először `C` jön

Ez tipikusan **stack** viselkedés.

## Mi az a FIFO?

A FIFO elv szerint az a tétel kerül először feldolgozásra, amelyik **legkorábban** került be.

Példa:

1. beteszed `A`
2. beteszed `B`
3. beteszed `C`
4. kivételkor először `A` jön

Ez tipikusan **queue** viselkedés.

## Hol jelenik meg az informatikában?

### LIFO

- függvényhívási verem
- visszalépési mechanizmusok
- undo jellegű megoldások

### FIFO

- nyomtatási sor
- üzenetsor
- feladatok feldolgozása érkezési sorrendben
- várakozási sorok

## Miért fontos ez?

Mert a feldolgozási sorrend:

- meghatározza a program működését
- hatással van a helyességre
- befolyásolja a teljesítményt és a felhasználói élményt

Ha rossz elvet választunk, a rendszer logikailag hibás lehet.

## LIFO és FIFO: ne keverd össze

| Kérdés | LIFO | FIFO |
|---|---|---|
| melyik elem jön először? | a legutóbbi | a legrégebbi |
| tipikus szerkezet | stack | queue |
| fő kép | verem | sor |

## Mire kell figyelni?

- A LIFO és FIFO nem konkrét programnyelv, hanem működési elv.
- Ugyanaz az adatszerkezet bizonyos esetekben többféleképpen is használható.
- A vizsgán gyakran példát is kérnek, nem csak feloldást.

## Vizsgán jól használható megfogalmazás

> A LIFO és FIFO olyan feldolgozási elvek,
> amelyek meghatározzák, milyen sorrendben vesszük ki
> vagy dolgozzuk fel az elemeket.  
> LIFO esetén az utoljára bekerült elem jön ki először, FIFO esetén pedig a legkorábban bekerült elem.  
> A LIFO tipikus megvalósítása a stack, a FIFO-é pedig a queue.

## Gyakori vizsgahibák

- A két rövidítést felcserélni.
- Csak angolul feloldani, de nem elmagyarázni.
- Nem mondani rá informatikai példát.
- Azt hinni, hogy mindkettő ugyanarra a célra való.

## Gyors önellenőrzés

1. Mit jelent a LIFO?
2. Mit jelent a FIFO?
3. Melyikhez kapcsolódik inkább a stack?
4. Melyikhez kapcsolódik inkább a queue?
5. Mondj egy-egy példát mindkettőre.

## Rövid válaszok az önellenőrzéshez

1. Last In, First Out
2. First In, First Out
3. LIFO
4. FIFO
5. LIFO: hívási verem. FIFO: nyomtatási sor

## Források

1. Oracle Java SE - `Deque` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Deque.html  
   Használat: hivatalos forrás arra, hogy egy deque használható LIFO stackként és FIFO queue-ként is.

2. Oracle Java SE - `Queue` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Queue.html  
   Használat: hivatalos forrás a queue általános működési elvéhez.

3. MDN - Call stack  
   https://developer.mozilla.org/en-US/docs/Glossary/Call_stack  
   Használat: gyakorlati, webes példa a LIFO működésre a programfutás során.

Megnyitva: `2026-04-08`
