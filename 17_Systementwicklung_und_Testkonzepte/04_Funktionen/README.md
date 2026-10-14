# Funktionen

## Gyors vizuális kép

```text
bemenet
    -> függvény feldolgoz
    -> visszatérési érték
```

## Mi az a függvény?

A függvény:

- egy konkrét feladatot lát el
- többször meghívható
- csökkenti a kódismétlést
- könnyebbé teszi a tesztelést és karbantartást

## A függvény fő elemei

| Elem | Jelentés |
|---|---|
| név | azonosítja a függvényt |
| paraméterek | bemeneti adatok |
| törzs | a végrehajtandó logika |
| visszatérési érték | az eredmény |

## Miért fontosak a függvények?

- jobban strukturálják a programot
- elkülönítik a felelősségeket
- újrafelhasználhatóvá teszik a logikát
- könnyebbé teszik a hibakeresést

## Eljárás és függvény: ne keverd össze

Vizsgán gyakran előjön ez a különbség:

| Fogalom | Egyszerű értelmezés |
|---|---|
| függvény | általában visszaad valamilyen értéket |
| eljárás | inkább műveletet végez, visszatérési érték nélkül vagy nem hangsúlyosan |

A modern nyelvekben ez a különbség néha kevésbé éles, de az alapötlet még hasznos.

## Jó függvény jellemzői

- legyen világos a célja
- ne csináljon túl sok mindent egyszerre
- kapjon egyértelmű paramétereket
- adjon jól értelmezhető eredményt

## Paraméter, argumentum és visszatérés

Egy rendelési tétel árát számoljuk egész centben. A teljes Node.js-példa
egész, nemnegatív bemenetet és biztonságosan ábrázolható egész eredményt követel.

<!-- example:run -->

```javascript
function totalCents(unitCents, quantity = 1) {
  if (!Number.isSafeInteger(unitCents) || unitCents < 0 ||
      !Number.isSafeInteger(quantity) || quantity < 0) {
    throw new RangeError("Nonnegative integer inputs required");
  }
  const total = unitCents * quantity;
  if (!Number.isSafeInteger(total)) throw new RangeError("Total is too large");
  return total;
}
console.log(totalCents(250, 3));
console.log(totalCents(250));
console.log(totalCents(250, 0));
```

```text
750
250
0
```

A deklarációban `unitCents` és `quantity` **paraméterek**. A `totalCents(250, 3)`
hívásban `250` és `3` **argumentumok**, vagyis az átadott konkrét értékek.
Ha a második argumentum hiányzik, az alapérték 1; a kifejezetten átadott 0 viszont
0 marad. A `return` eredményt ad vissza és lezárja a hívást, a `console.log`
pedig csak megjeleníti a hívó által megkapott értéket.

A számítás nem módosít külső állapotot. Az ilyen függvény könnyen ellenőrizhető
ugyanazzal a bemenettel. Léteznek névtelen függvények is, például callbackként.
JavaScriptben explicit `return` nélkül egy hagyományos függvény `undefined`-ot
ad vissza; ez is meghatározott nyelvi viselkedés.

## Vizsgán jól használható megfogalmazás

> A függvény egy meghívható, újra felhasználható programrész, amely meghatározott feladatot lát el; lehet neve, de névtelen is lehet.  
> Paramétereket kaphat, ezeket feldolgozza, és gyakran visszatérési értéket ad vissza.  
> A függvények használata javítja a program szerkezetét, csökkenti a kódismétlést és megkönnyíti a karbantartást.

## Gyors önellenőrzés

1. Mi a függvény lényege?
2. Milyen fő részei vannak?
3. Miért hasznos a programban?
4. Mi a különbség függvény és eljárás között?
5. Milyen egy jó függvény?

## Rövid válaszok az önellenőrzéshez

1. Újra felhasználható logikai egység
2. Név, paraméterek, törzs, visszatérési érték
3. Mert strukturál és csökkenti az ismétlést
4. A függvény jellemzően ad vissza eredményt
5. Világos, célzott és jól paraméterezett

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions): paraméter, argumentum és visszatérés.


1. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Használat: hivatalos, modern forrás a függvények alapfogalmához.

2. Python Docs - Defining Functions  
   https://docs.python.org/3/tutorial/controlflow.html#defining-functions  
   Használat: hivatalos, jól olvasható kiegészítő forrás a paraméterek és visszatérés fogalmához.

Megnyitva: `2026-04-09`
