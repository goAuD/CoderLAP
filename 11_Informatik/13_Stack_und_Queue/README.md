# Stack und Queue

## Lényeg 30 másodpercben

A **stack** és a **queue** két alapvető adatszerkezeti modell.

- `stack` = verem
- `queue` = sor

Röviden:

- a stack jellemzően `LIFO`
- a queue jellemzően `FIFO`

## Gyors vizuális kép

| Adatszerkezet | Működés | Alapműveletek |
|---|---|---|
| stack | LIFO | `push`, `pop`, `peek` |
| queue | FIFO | `enqueue`, `dequeue`, `peek` |

## Mi az a stack?

A stack olyan adatszerkezet, ahol az elemeket egymás "tetejére" tesszük.

Tipikus műveletek:

- `push` = elem betétele
- `pop` = legfelső elem kivétele
- `peek` = legfelső elem megnézése

Ezért a stack **LIFO** elven működik.

## Mi az a queue?

A queue olyan adatszerkezet, ahol az elemek sorban várnak feldolgozásra.

Tipikus műveletek:

- `enqueue` = elem beállítása a sor végére
- `dequeue` = elem kivétele a sor elejéről
- `peek` = sor elejének megtekintése

Ezért a queue **FIFO** elven működik.

## Hol használjuk őket?

### Stack

- függvényhívások kezelése
- visszalépés vagy undo
- zárójelek ellenőrzése
- mélységi bejárások

### Queue

- feladatsorok
- nyomtatási sor
- üzenetkezelés
- szélességi bejárások

## Mi a különbség az elv és a szerkezet között?

| Fogalom | Mit jelent? |
|---|---|
| LIFO / FIFO | működési sorrendi elv |
| stack / queue | konkrét adatszerkezeti modell |

Tehát:

- a LIFO/FIFO inkább szabály
- a stack/queue inkább szerkezet és műveletkészlet

## Stack és queue: ne keverd össze

| Kérdés | Stack | Queue |
|---|---|---|
| melyik elem jön ki? | legutóbbi | legrégebbi |
| sorrendi elv | LIFO | FIFO |
| tipikus kép | verem | sor |
| tipikus művelet | `push/pop` | `enqueue/dequeue` |

## Mire kell figyelni?

- A stack nem azonos a call stackkal, csak az annak egy konkrét alkalmazása.
- A queue nem csak várakozási sor, hanem sok feldolgozási modell alapja.
- Vizsgán gyakran kérik a műveletek nevét vagy legalább a működésüket.

## Vizsgán jól használható megfogalmazás

> A stack és a queue alapvető adatszerkezeti modellek.  
> A stack veremelven működik, ezért az utoljára betett elem kerül ki először, vagyis LIFO.  
> A queue ezzel szemben sorelven működik, ezért a legrégebben betett elem kerül feldolgozásra először, vagyis FIFO.

## Gyakori vizsgahibák

- A stacket és queue-t csak hétköznapi példával elmagyarázni, műveletek nélkül.
- A LIFO/FIFO-t nem kötni hozzájuk.
- A `push/pop` és `enqueue/dequeue` fogalmak összekeverése.
- Azt mondani, hogy a stack mindig gyorsabb vagy jobb.

## Gyors önellenőrzés

1. Mi a stack lényege?
2. Mi a queue lényege?
3. Milyen műveletek jellemzőek stackre?
4. Milyen műveletek jellemzőek queue-ra?
5. Mi a kapcsolat a stack és a LIFO között?

## Rövid válaszok az önellenőrzéshez

1. Veremszerű tárolás, LIFO működés
2. Sorjellegű tárolás, FIFO működés
3. `push`, `pop`, `peek`
4. `enqueue`, `dequeue`, `peek`
5. A stack tipikusan LIFO szerint működik

## Források

1. Oracle Java SE - `Deque` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Deque.html  
   Használat: hivatalos forrás a stack és queue jellegű használathoz ugyanazon absztrakción belül.

2. Oracle Java SE - `Queue` Interface  
   https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Queue.html  
   Használat: a queue fogalma és alapműveletei.

3. MDN - Call stack  
   https://developer.mozilla.org/en-US/docs/Glossary/Call_stack  
   Használat: gyakorlati példa a stack működésére programfutás közben.

Megnyitva: `2026-04-08`
