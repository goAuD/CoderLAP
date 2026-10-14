# Algorithmus

## Gyors vizuális kép

```text
Bemenet
    -> feldolgozási lépések
    -> eredmény
```

## Mi az algoritmus?

Egy algoritmus:

- véges számú lépésből áll
- jól meghatározott
- végrehajtható
- valamilyen eredményre vezet

Programozásban az algoritmus a megoldás logikája.  
A program ennek konkrét, nyelvi megvalósítása.

## Az algoritmus tipikus jellemzői

| Jellemző | Jelentés |
|---|---|
| egyértelműség | minden lépés világos |
| végesség | nem tart örökké |
| bemenet | lehet adat, amivel dolgozik |
| kimenet | eredményt ad |
| ismételhetőség | újra végrehajtható |

## Miért fontos?

- segít a probléma strukturálásában
- programozási nyelvtől függetlenül leírható
- összehasonlíthatók vele különböző megoldások
- alapja a hatékony programnak

## Algoritmus és program: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| algoritmus | a megoldás logikai leírása |
| program | az algoritmus konkrét kódja egy nyelven |

Ugyanaz az algoritmus több nyelven is megírható.

## Egyszerű példa

Feladat: számok összegzése `1`-től `n`-ig.

Algoritmus:

1. indulj `0` összeggel
2. menj végig `1`-től `n`-ig
3. mindig add hozzá az aktuális számot az összeghez
4. a végén add vissza az összeget

## Hatékonyság röviden

Nemcsak az számít, hogy működik-e, hanem az is, hogy:

- milyen gyors
- mennyi memóriát használ
- nagy adatmennyiségnél hogyan viselkedik

Ezért beszélünk algoritmusok összehasonlításáról is.

## Bemeneti feltétel, nyomkövetés és eredmény

Az előbbi összegzést most JavaScriptben valósítjuk meg. A feladat szerződése:
`n` egész, `0..1000` közötti szám; az eredmény az `1..n` számok összege. A korlát
ebben a tanulópéldában egyszerű futásidőt és pontos egész eredményt biztosít.

<!-- example:run -->

```javascript
function sumTo(n) {
  if (!Number.isInteger(n) || n < 0 || n > 1000) {
    throw new RangeError("n must be an integer from 0 to 1000");
  }
  let sum = 0;
  for (let i = 1; i <= n; i++) sum += i;
  return sum;
}
console.log(sumTo(4));
console.log(sumTo(0));
```

```text
10
0
```

`n = 4` esetén az összeg rendre `1`, `3`, `6`, `10`. A ciklus előtt nulla,
minden kör után pedig az addig feldolgozott számok összege. Ez az állítás segít
indokolni a helyességet. `n = 0` esetén nincs cikluskör, az eredmény a helyesen
definiált üres összeg, nulla. A ciklusváltozó növekszik és a felső korlát véges,
ezért az érvényes bemeneteknél a végrehajtás befejeződik.

A ciklus `n` összeadást végez, időigénye `O(n)`, segédmemóriája `O(1)`. Ugyanitt
az `n * (n + 1) / 2` képlet rögzített számú művelettel számolható. Ez a konkrét
összegre használható matematikai tulajdonság, nem minden ciklus helyettesíthető
hasonló képlettel.

## Vizsgán jól használható megfogalmazás

> Az algoritmus egy egyértelmű, véges lépéssorozat, amely egy adott probléma megoldására szolgál.  
> Bemeneteket feldolgoz, és eredményt ad vissza.  
> A programozásban az algoritmus a megoldás logikája, amelyet később egy konkrét programozási nyelven valósítunk meg.

## Gyors önellenőrzés

1. Mi az algoritmus lényege?
2. Miben különbözik a programtól?
3. Miért fontos az egyértelműség?
4. Mit jelent az, hogy véges?
5. Miért hasznos ugyanazt a feladatot több algoritmussal is megnézni?

## Rövid válaszok az önellenőrzéshez

1. Egyértelmű megoldási lépéssor
2. Az algoritmus logika, a program konkrét kód
3. Hogy ugyanúgy végrehajtható legyen
4. Hogy a lépéssor véget ér
5. Mert eltérhet a hatékonyságuk

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Algorithm](https://developer.mozilla.org/en-US/docs/Glossary/Algorithm): algoritmus fogalma; saját összegzési példa.


1. MDN - Algorithm  
   https://developer.mozilla.org/en-US/docs/Glossary/Algorithm  
   Használat: modern, tömör fogalmi meghatározás algoritmushoz.

2. NIST CSRC Glossary - Algorithm  
   https://csrc.nist.gov/glossary/term/algorithm  
   Használat: hivatalos definíciós háttér az algoritmus fogalmához.

Megnyitva: `2026-04-09`
