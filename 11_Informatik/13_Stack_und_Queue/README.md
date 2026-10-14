# Stack und Queue

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

## Mire jó a műveletkészlet? Zárójelpárok ellenőrzése

**Feladat:** egy szöveg kerek zárójelei legyenek kiegyensúlyozottak. Minden
nyitás betesz egy elemet, minden zárás kivesz egyet. A többi karaktert ez az
egyszerű ellenőrző figyelmen kívül hagyja. Nem teljes JavaScript-elemző,
idézőjeleket és megjegyzéseket sem értelmez. Futtatás: Node.js.

<!-- example:run -->

```javascript
function balancedParentheses(text) {
  const stack = [];
  for (const character of text) {
    if (character === "(") stack.push(character);
    if (character === ")") {
      if (stack.length === 0) return false;
      stack.pop();
    }
  }
  return stack.length === 0;
}
console.log(balancedParentheses("(a + (b))"));
console.log(balancedParentheses(")("));
console.log(balancedParentheses("((a)"));
console.log(balancedParentheses(""));
```

```text
true
false
false
true
```

Az első példánál a verem mélysége a zárójeleknél `1, 2, 1, 0`. A `)(` azonnal
elutasításra kerül, mert üres veremből kellene kivenni. A `((a)` végén marad
egy nyitás. Az üres szövegben nincs párosítatlan zárójel, ezért az eredmény igaz.
A bejárás ideje a szöveg hosszával arányos, a verem legfeljebb annyi elemet tárol,
ahány egymásba ágyazott nyitó zárójel van.

A queue-nál más szerződés kell: a `peek` nem vesz ki elemet, a `dequeue` igen.
Üres tárolónál dokumentáljuk a visszatérési értéket vagy a kivételt. A JavaScript
`shift()` üres tömbre `undefined` értéket ad. Tömb elejéről törölve indexeket
kell átrendezni; nagy forgalmú sorhoz körkörös puffer vagy megfelelő könyvtári
queue lehet jobb. A FIFO-elv önmagában nem mondja meg a műveletek költségét.

## Vizsgán jól használható megfogalmazás

> A stack és a queue alapvető adatszerkezeti modellek.  
> A stack veremelven működik, ezért az utoljára betett elem kerül ki először, vagyis LIFO.  
> A queue ezzel szemben sorelven működik, ezért a legrégebben betett elem kerül feldolgozásra először, vagyis FIFO.

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

Ellenőrizve: `2026-10-14`.

- [MDN: Array.shift](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift): üres tömb és átrendezési szemantika.
- [MDN: Call stack](https://developer.mozilla.org/en-US/docs/Glossary/Call_stack): a verem egy konkrét alkalmazása.


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
