# Variablenarten, Datentypen, Definitionen

## Gyors vizuális kép

| Fogalom | Jelentés |
|---|---|
| változó | névvel elérhető adat |
| adattípus | szám, szöveg, logikai érték stb. |
| deklaráció | megmondjuk, hogy létezik |
| inicializálás | kezdőértéket adunk |

## Mi az a változó?

A változó olyan programozási elem, amely:

- egy értékre utal
- neve van
- a program futása során felhasználható

Nyelvtől függően a változó:

- közvetlenül értéket tárolhat
- vagy hivatkozhat egy objektumra / memóriaterületre

## Mi az adattípus?

Az adattípus meghatározza:

- milyen jellegű adatot tárolunk
- milyen műveletek végezhetők rajta
- mennyire kell rá vigyázni formailag

## Tipikus adattípusok

| Típus | Példa |
|---|---|
| egész szám | `42` |
| lebegőpontos szám | `3.14` |
| logikai | `true`, `false` |
| karakter / szöveg | `'A'`, `"hello"` |
| összetett típus | lista, tömb, objektum |

## Változótípusok röviden

Ezt többféleképp értelmezhetjük:

- egyszerű és összetett adattípusok
- lokális és globális változók
- módosítható és nem módosítható kötések

Mivel a konkrét részletek nyelvenként eltérnek, vizsgán a fogalmi magot érdemes biztosan tudni.

## Deklaráció, definíció, inicializálás

Ez fontos vizsgás különbségtétel.

| Fogalom | Egyszerű jelentés |
|---|---|
| deklaráció | megadjuk a változó nevét / létét |
| definíció | az entitás tényleges meghatározása; pontos jelentése nyelvfüggő |
| inicializálás | kezdőérték adása |

Megjegyzés:

- ezek pontos nyelvi jelentése eltérhet `C`, `JavaScript`, `Python` vagy más nyelvek között
- vizsgán az alapgondolat a fontos

## Miért fontos az adattípus?

- segít elkerülni hibákat
- meghatározza a műveleteket
- befolyásolhatja a memóriahasználatot és a működést

## Pontosítás JavaScript-példán

A `let count;` létrehozza a kötést; a deklaráció végrehajtása után az értéke
`undefined`. Az utána következő `count = 3` értékadás. A `const enabled = true`
deklaráció és inicializálás együtt. A „definíció” részleteit mindig a konkrét
nyelvhez kötjük, nem használjuk az értékadás általános szinonimájaként.

<!-- example:run -->

```javascript
let count;
console.log(typeof count);
count = 3;
const enabled = true;
const label = "3";
console.log(typeof count, typeof enabled, typeof label);
console.log(count === Number(label));
console.log(Number.isFinite(Number("unknown")));
```

```text
undefined
number boolean string
true
false
```

A példa Node.js-ben fut. JavaScriptben a `3` és `3.14` egyaránt `number`;
nincs külön általános `int` típusa. A `bigint` külön egész típus, például `3n`,
és a `number` értékekkel végzett közös számoláshoz tudatos konverzió kell.
Szöveget `string`, igaz/hamis értéket `boolean` tárol. A `null` tudatosan választott
üres értéket jelenthet, az `undefined` pedig például hiányzó értéket.

Dinamikus típusosságnál a változó más típusú értéket is kaphat; az értékeknek
ettől még van típusuk. A `Number("unknown")` eredménye `NaN`; ezért a konverziót
ellenőrzés követi. A `Number.isFinite` nem fogadja el a végtelent és a `NaN`-t.
Pénzösszegnél egész cent vagy erre tervezett decimális megoldás alkalmasabb, mint
a kerekítési szabály nélkül végzett bináris lebegőpontos számolás.

## Vizsgán jól használható megfogalmazás

> A változó egy névvel ellátott programozási elem, amely egy értéket vagy arra mutató hivatkozást jelöl.  
> Az adattípus meghatározza, hogy milyen jellegű adatot kezelünk, és milyen műveletek végezhetők rajta.  
> A programozásban fontos megkülönböztetni a deklarációt, a definíciót és az inicializálást, még akkor is, ha ezek
> pontos jelentése nyelvenként eltérhet.

## Gyors önellenőrzés

1. Mi a változó?
2. Mi az adattípus?
3. Mondj négy alap adattípust.
4. Mi az inicializálás?
5. Miért térhet el a pontos terminológia nyelvenként?

## Rövid válaszok az önellenőrzéshez

1. Névvel elérhető adat vagy hivatkozás
2. Az adat fajtájának leírása
3. Egész, lebegőpontos, logikai, szöveg
4. Kezdőérték adása
5. Mert a nyelvek eltérően definiálják

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: JavaScript data types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Data_structures): nyelvspecifikus típusok és konverzió.


1. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Használat: hivatalos, modern forrás adattípusokhoz és változóalapokhoz.

2. MDN - Statements and declarations  
   https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements  
   Használat: jól használható háttér a deklaráció és nyelvi szerkezetek megértéséhez.

Megnyitva: `2026-04-09`
