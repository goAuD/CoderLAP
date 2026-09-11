# Schleifen

## Gyors vizuális kép

| Ciklustípus | Mikor jó? |
|---|---|
| `for` | ha tudjuk, hány ismétlés kell |
| `while` | ha feltétel alapján ismétlünk |
| `do...while` | ha legalább egyszer mindenképp fusson |
| `for...of` JavaScriptben | egy bejárható adatsor értékeinek feldolgozására |

## Mi az a ciklus?

A ciklus lényege, hogy:

- nem kell ugyanazt a kódot többször leírni
- a program ismétli a műveletet
- amíg teljesül egy feltétel
- vagy amíg be nem járja az elemeket

## Miért fontos?

- rövidebb és tisztább kódot ad
- könnyebb karbantartani
- hatékonyabb megoldást tesz lehetővé ismétlődő műveleteknél

## Kidolgozott példák JavaScriptben

Minden kódblokk önállóan futtatható: mentsd például `pelda.js` néven,
majd indítsd a `node pelda.js` paranccsal egy telepített Node.js környezetben.
A `console.log` a kimenetre ír. Először jósoljuk meg az eredményt, majd futtassuk le.

### Számlálás `for` ciklussal

Feladat: írjuk ki az 1, 2 és 3 számot, külön sorba.

```javascript
for (let number = 1; number <= 3; number++) {
  console.log(number);
}
```

Kimenet:

```text
1
2
3
```

A fejléc három része: kezdőérték (`let number = 1`), folytatási feltétel
(`number <= 3`) és léptetés (`number++`). A kezdőérték egyszer áll be;
a feltételt minden végrehajtás előtt, a léptetést minden ciklusmag után végezzük.

| Feltételvizsgálatkor `number` | `number <= 3` | Mi történik? |
|---|---|---|
| 1 | igaz | kiírjuk az 1-et, majd 2-re növelünk |
| 2 | igaz | kiírjuk a 2-t, majd 3-ra növelünk |
| 3 | igaz | kiírjuk a 3-at, majd 4-re növelünk |
| 4 | hamis | a végrehajtás a ciklus után folytatódik |

### Állapot követése `while` ciklussal

Feladat: induljunk három hátralévő körből, és minden kör után csökkentsük a számukat.

```javascript
let remaining = 3;
while (remaining > 0) {
  console.log(remaining);
  remaining--;
}
```

Kimenet:

```text
3
2
1
```

A `remaining` értéke a ciklusmagban változik. Amikor 0 lesz, a feltétel hamis,
és a ciklus véget ér. A `while` akkor is használható, ha a kezdőállapot például
egy függvény paraméteréből érkezik: a folytatásról mindig az aktuális állapot dönt.

### A feltételvizsgálat helye: `while` és `do...while`

Feladat: figyeljük meg, hányszor hajtódik végre a két ciklusmag, ha a feltétel
már kezdetben hamis. A `runs++` egy végrehajtást számol.

```javascript
let runs = 0;
while (runs < 0) {
  runs++;
}
console.log(runs);

runs = 0;
do {
  runs++;
} while (runs < 0);
console.log(runs);
```

Kimenet:

```text
0
1
```

A `while` először ellenőriz, ezért itt 0 végrehajtás történik. A `do...while`
először végrehajtja a ciklusmagot, utána ellenőriz: itt 1 végrehajtás történik.
A példa szándékosan ezt a két ellenőrzési időpontot teszi láthatóvá.

### Értékek bejárása `for...of` ciklussal

Feladat: adjuk össze egy háromelemű tömb pontszámait.

```javascript
const scores = [3, 5, 7];
let total = 0;
for (const score of scores) {
  total += score;
}
console.log(total);
```

Kimenet:

```text
15
```

A `score` sorban a 3, 5 és 7 értéket kapja. Az összeg 0 → 3 → 8 → 15 szerint
változik. Üres tömbnél a ciklusmag 0 alkalommal fut, az összeg 0 marad.

## Ciklus és rekurzió összehasonlítása

| Fogalom | Lényeg |
|---|---|
| ciklus | ismétlés vezérlési szerkezettel |
| rekurzió | ismétlés önhívó függvénnyel |

## Vizsgán jól használható megfogalmazás

> A ciklus olyan vezérlési szerkezet, amely egy utasítást vagy utasításblokkot többször végrehajt.  
> A futást általában feltétel, számláló vagy bejárandó elemsor vezérli.  
> A ciklusok célja a kódismétlés csökkentése és az ismétlődő feladatok hatékony kezelése.

## Gyors önellenőrzés

1. Hányszor fut le az első példában a ciklusmag, és hányszor vizsgáljuk a feltételt?
2. Mi a `remaining` értéke a `while` példa végén?
3. Mitől lehet a `do...while` hasznos olyan műveletnél, amelyet egyszer biztosan végrehajtunk?
4. Mit ír ki az összegző példa, ha a `scores` értéke `[]`?
5. Melyik művelet ismétli a munkát rekurzió esetén?

## Rövid válaszok az önellenőrzéshez

1. A ciklusmag 3-szor fut; a feltételt 4-szer vizsgáljuk, utoljára a 4-es értéknél.
2. 0; ekkor a `remaining > 0` feltétel hamis.
3. A ciklusmag megelőzi az első feltételvizsgálatot, ezért legalább egyszer lefut.
4. 0-t, mert az összeg kezdőértéke 0, és nincs feldolgozandó elem.
5. A függvény önhívása; ciklusnál a vezérlési szerkezet ismétli a ciklusmagot.

## Források

1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Használat: hivatalos, modern forrás a ciklusok működéséhez és típusaihoz.

2. MDN - Control flow  
   https://developer.mozilla.org/en-US/docs/Glossary/Control_flow  
   Használat: háttérforrás a vezérlési szerkezetek nagyobb kontextusához.

Megnyitva: `2026-09-11`
