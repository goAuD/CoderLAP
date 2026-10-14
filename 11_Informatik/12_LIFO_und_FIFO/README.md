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

## Érkezés és kivétel felváltva

**Feladat:** megérkezik `A`, majd `B`; egy tételt kiveszünk; megérkezik `C`;
végül kiürítjük a tárolót. Ez jobban megmutatja a szabályt, mint egy egyszerű
megfordított lista. Node.js-ben önállóan futtatható:

<!-- example:run -->

```javascript
const lifo = [];
const fifo = [];
for (const task of ["A", "B"]) {
  lifo.push(task);
  fifo.push(task);
}
console.log(lifo.pop(), fifo.shift());
lifo.push("C");
fifo.push("C");
console.log(lifo.pop(), fifo.shift());
console.log(lifo.pop(), fifo.shift());
console.log(lifo.length, fifo.length);
```

```text
B A
C B
A C
0 0
```

Az első kivételnél LIFO szerint `B`, FIFO szerint `A` távozik. Az új `C`
a verem tetejére kerül, ezért rögtön ő következik; a sorban viszont `B`
mögé áll. LIFO sorrendje így `B, C, A`, FIFO sorrendje `A, B, C`.

A sorrend az **elemek kiválasztására** vonatkozik. Több párhuzamos feldolgozó
esetén FIFO-kivétel mellett is végezhet hamarabb egy később kezdett rövid feladat.
Egy prioritásos sor pedig más kiválasztási szabályt használ: nem minden olyan
könyvtári típus szigorúan FIFO, amelynek nevében „Queue” szerepel.

## Vizsgán jól használható megfogalmazás

> A LIFO és FIFO olyan feldolgozási elvek,
> amelyek meghatározzák, milyen sorrendben vesszük ki
> vagy dolgozzuk fel az elemeket.  
> LIFO esetén az utoljára bekerült elem jön ki először, FIFO esetén pedig a legkorábban bekerült elem.  
> A LIFO tipikus megvalósítása a stack, a FIFO-é pedig a queue.

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

Ellenőrizve: `2026-10-14`.

- [MDN: Array.shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift): soreleji kivétel és módosuló tömb.
- [Oracle: Queue](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/Queue.html): FIFO és más sorrendi szabályú queue-k.


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
