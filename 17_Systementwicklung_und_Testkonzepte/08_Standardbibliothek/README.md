# Standardbibliothek

## Gyors vizuális kép

| Standard library rész | Példa |
|---|---|
| szövegkezelés | string műveletek |
| fájlkezelés | beolvasás, írás |
| dátum és idő | időkezelés |
| adatszerkezetek | listák, szótárak, gyűjtemények |
| matematikai műveletek | számítások |

## Mi az a standard library?

A legtöbb általános célú nyelv és futtatókörnyezet kínál alapkönyvtárat; ennek terjedelme platformonként eltér.

Ez tipikusan biztosít:

- alapműveleteket
- gyakran használt eszközöket
- jól dokumentált, közös megoldásokat

## Miért fontos?

- gyorsítja a fejlesztést
- csökkenti a fölösleges saját megoldások számát
- sokszor jobban tesztelt és stabilabb, mint a házilag írt alternatíva
- egységesebb kódot eredményezhet

## Mire jó a gyakorlatban?

Például:

- fájlokat kezelni
- dátumokat számolni
- hálózati műveleteket végezni
- adatokat átalakítani
- gyűjteményekkel dolgozni

## Standard library és külső csomag: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| standard library | a nyelv alap része vagy hivatalos csomagja |
| külső könyvtár | külön telepített, külső csomag |

## Miért nem jó mindent saját kézzel megírni?

- lassabb
- hibásabb lehet
- nehezebb karbantartani
- fölöslegesen duplikáljuk azt, ami már készen és jól megoldva létezik

## Egy beépített művelet szerződését is elolvassuk

Feladat: számokat növekvően rendezünk, megőrizve a bemenetet, majd megduplázzuk
a rendezett értékeket. A példa Node.js-ben és modern böngészőkonzolban fut.

<!-- example:run -->

```javascript
const values = [20, 3, 100];
const sorted = [...values].sort((a, b) => a - b);
console.log(JSON.stringify(sorted));
console.log(JSON.stringify(values));
console.log(JSON.stringify(sorted.map(value => value * 2)));
```

```text
[3,20,100]
[20,3,100]
[6,40,200]
```

A `sort` az adott tömböt módosítja, ezért előbb másolunk. Az `(a, b) => a - b`
numerikus összehasonlítást ad; negatív eredmény esetén `a` kerül előrébb.
A `map` új tömböt készít a callback visszaadott értékeiből. A dokumentációból
tehát a bemenet mellett a visszatérést, mellékhatást és előfeltételeket is ellenőrizzük.

JavaScriptnél az `Array`, `Math` és `JSON` a nyelv része. A DOM és a böngésző
fájlválasztója platformszolgáltatás, a Node.js `node:fs` modulja pedig a Node
alapkönyvtárához tartozik. Nem minden környezetben ugyanazok az API-k érhetők el.
Külső csomag akkor indokolt, ha valódi hiányt pótol; előbb megnézzük a meglévő
eszközöket, a kompatibilitást és a karbantartási költséget.

## Vizsgán jól használható megfogalmazás

> A standard library a programozási nyelvhez tartozó szabványos függvények, modulok és osztályok gyűjteménye.  
> Célja, hogy a fejlesztő gyakori feladatokat kész megoldásokkal tudjon megvalósítani, például fájlkezelést,  
> adatkezelést, szövegfeldolgozást vagy matematikai műveleteket.  
> A standard library használata gyorsabb, egységesebb és megbízhatóbb fejlesztést tesz lehetővé.

## Gyors önellenőrzés

1. Mi az a standard library?
2. Miért hasznos?
3. Mondj három tipikus területet, amit lefedhet.
4. Mi a különbség standard library és külső csomag között?
5. Miért nem érdemes mindent saját kézzel újraírni?

## Rövid válaszok az önellenőrzéshez

1. A nyelvhez tartozó hivatalos alapkönyvtár
2. Mert gyorsabb és megbízhatóbb fejlesztést ad
3. Fájlkezelés, dátum, adatszerkezetek
4. Az egyik alapból adott, a másik külön telepített
5. Mert lassabb és hibásabb lehet

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Array.sort](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort): numerikus rendezés és bemenetmódosítás.


1. Python Docs - The Python Standard Library  
   https://docs.python.org/3/library/index.html  
   Használat: hivatalos elsődleges forrás a standard library fogalmához.

2. MDN - Standard built-in objects  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects  
   Használat: hivatalos, modern példa arra, hogyan jelenik meg egy nyelv beépített alapkönyvtára a gyakorlatban.

Megnyitva: `2026-04-09`
