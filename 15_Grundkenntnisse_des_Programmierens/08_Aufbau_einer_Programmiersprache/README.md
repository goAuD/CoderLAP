# Aufbau einer Programmiersprache

## Gyors vizuális kép

| Elem | Kérdés |
|---|---|
| szintaxis | hogyan írjuk le helyesen? |
| szemantika | mit jelent a leírt utasítás? |
| típusok | milyen adatokat kezelünk? |
| operátorok | milyen műveleteket végzünk? |
| vezérlési szerkezetek | milyen sorrendben fut a program? |

## Miből áll egy programozási nyelv?

Egy programnyelv tipikusan tartalmaz:

- **kulcsszavakat**
- **azonosítókat**
- **literálokat**
- **adattípusokat**
- **operátorokat**
- **utasításokat**
- **vezérlési szerkezeteket**
- gyakran **függvényeket**, **modulokat**, vagy **osztályokat**

## Szintaxis és szemantika

Ez az egyik legfontosabb különbség.

| Fogalom | Jelentés |
|---|---|
| szintaxis | a helyes forma és írásmód |
| szemantika | az utasítás jelentése és működése |

Példa:

- szintaktikailag lehet helyes valami
- de logikailag vagy szemantikailag lehet rossz

## Tipikus nyelvi elemek

### Kulcsszavak

Például:

- `if`
- `while`
- `return`
- `class`

### Azonosítók

Ezek a nevek:

- változónevek
- függvénynevek
- osztálynevek

### Literálok

Közvetlen értékek, például:

- `42`
- `"hello"`
- `true`

### Operátorok

Például:

- összeadás
- összehasonlítás
- logikai műveletek
- értékadás

## Mire kell még gondolni?

Egy nyelvhez gyakran tartozik:

- szabvány vagy nyelvi referencia
- fordító vagy interpreter
- standard library
- futási környezet

## Egy kifejezés részekre bontása

Feladat: 250 cent egységárból és a szövegként kapott `"3"` darabszámból
kiszámítjuk a teljes árat. Ez rögzített, érvényes bemenetű Node.js-példa;
felhasználói adatnál a konverzió után tartományt és egész számot is ellenőrzünk.

<!-- example:run -->

```javascript
const unitCents = 250;
const quantity = Number("3");
const totalCents = unitCents * quantity;
console.log(totalCents);
console.log(typeof quantity, quantity === 3);
```

```text
750
number true
```

| Kódrész | Nyelvi szerep |
|---|---|
| `const` | deklarációs kulcsszó |
| `unitCents` | általunk választott azonosító |
| `250`, `"3"` | szám-, illetve szövegliterál |
| `unitCents * quantity` | értéket előállító kifejezés |
| `===` | szigorú egyenlőségvizsgálat |

A szintaxis megmondja, hogyan épülhet fel a deklaráció. A szemantika mondja meg,
hogy a `*` milyen műveletet végez és milyen értéket kapunk. A `Number` nyelvi
beépített objektum; a `console` a futtatókörnyezet szolgáltatása. A böngésző
`document` objektuma például nem jár automatikusan a Node.js környezethez.

## Vizsgán jól használható megfogalmazás

> Egy programozási nyelv felépítését a szintaxis, a szemantika és a nyelvi elemek összessége adja.  
> Ide tartoznak például a kulcsszavak, azonosítók, literálok, adattípusok, operátorok és vezérlési szerkezetek.  
> A szintaxis azt határozza meg, hogyan kell helyesen leírni a kódot, a szemantika pedig azt, hogy az mit jelent és
> hogyan viselkedik végrehajtáskor.

## Gyors önellenőrzés

1. Mi a szintaxis?
2. Mi a szemantika?
3. Milyen nyelvi elemeket ismersz?
4. Mi a különbség kulcsszó és azonosító között?
5. Miért nem elég csak “helyesen leírni” a kódot?

## Rövid válaszok az önellenőrzéshez

1. A helyes forma és szabályrendszer
2. A jelentés és működés
3. Kulcsszó, azonosító, literál, típus, operátor, utasítás
4. A kulcsszó foglalt nyelvi elem, az azonosító általunk adott név
5. Mert logikailag még lehet hibás

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Grammar and types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types): literálok, deklarációk és típuskonverzió.


1. MDN - Syntax  
   https://developer.mozilla.org/en-US/docs/Glossary/Syntax  
   Használat: hivatalos, jól érthető alapforrás a szintaxis fogalmához.

2. MDN - Grammar and types  
   https://developer.mozilla.org/docs/Web/JavaScript/Guide/Grammar_and_types  
   Használat: korszerű, strukturált áttekintés egy programnyelv tipikus építőelemeihez.

Megnyitva: `2026-04-09`
