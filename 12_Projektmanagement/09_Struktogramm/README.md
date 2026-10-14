# Struktogramm

## Gyors vizuális kép

| Elem | Mit mutat? |
|---|---|
| egymás alatti blokkok | lépések sorrendje |
| osztott blokk | elágazás |
| ismétlődő blokk | ciklus |

## Mi a struktogramm?

A struktogramm az algoritmusok szemléletes leírására szolgál.

Segít abban, hogy:

- átlásd a programlogikát
- még kódírás előtt megtervezd a működést
- oktatásban és dokumentációban jól bemutatható legyen a vezérlés

## Miben más, mint a flowchart?

A struktogramm erősebben a **strukturált programozás** logikájára épít.

Ezért:

- kevésbé „nyilas-szétágazós”
- inkább egymásba ágyazott blokkokból áll

## Mikor hasznos?

- algoritmus tanításánál
- egyszerűbb programlogika tervezésénél
- programozási alapfogalmak bemutatásánál

## Struktogramm és flowchart: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| struktogramm | blokkos, strukturált algoritmusábra |
| flowchart | nyilas folyamatábra, lépések és döntések folyása |

## A blokkoktól a futtatható algoritmusig

A Nassi-Shneiderman név Isaac Nassi és Ben Shneiderman szerzőkre utal. A diagram a vezérlést egymásba ágyazott blokkokkal, nem külön összekötő nyilakkal írja le. A szekvencia egymás alatti lépésekből áll; a ciklus kerete tartalmazza az ismételt műveleteket, azon belül az elágazás két alternatívát választ szét.

Példafeladat: egy számlista pozitív elemeit adjuk össze. A struktogramm külső szekvenciája: összeg nullázása, a lista bejárása, eredmény visszaadása. A bejáró ciklusba egy `value > 0` döntés kerül; igaz esetben hozzáadunk, hamis esetben nincs művelet. Ennek kódja:

<!-- example:run -->
```javascript
function sumPositive(values) {
  let sum = 0;
  for (const value of values) {
    if (value > 0) {
      sum += value;
    }
  }
  return sum;
}

console.log(sumPositive([-2, 3, 5]));
console.log(sumPositive([]));
```

```text
8
0
```

A `[-2, 3, 5]` listánál az összeg rendre 0, 3, 8. Az üres lista esetén a ciklus egyszer sem fut, ezért az eredmény 0. A rajznak és a kódnak ezeket az eseteket azonosan kell leírnia.

## Vizsgán jól használható megfogalmazás

> A struktogramm egy algoritmus vagy programlogika blokkszerű, strukturált ábrázolása.  
> Segítségével jól szemléltethető a lépések sorrendje,
> az elágazás és a ciklus, ezért különösen hasznos
> az algoritmusok tervezésében és oktatásában.  
> A flowcharttal szemben inkább egymásba ágyazott szerkezeteket használ, és közelebb áll a strukturált programozás gondolkodásmódjához.

## Gyors önellenőrzés

1. Mi a struktogramm lényege?
2. Mire használjuk?
3. Miért hívják Nassi-Shneiderman diagramnak is?
4. Miben különbözik a flowcharttól?
5. Milyen logikai elemeket tud jól mutatni?

## Rövid válaszok az önellenőrzéshez

1. Strukturált algoritmusábra
2. Algoritmusok tervezésére és bemutatására
3. A szerzők, Isaac Nassi és Ben Shneiderman neve után
4. Blokkosabb és strukturáltabb
5. Szekvencia, elágazás, ciklus

## Források

- [Structorizer: User Guide](https://help.structorizer.fisch.lu/index.php?menu=44&page=)  
  Strukturált vezérlési ábrák és az azokból következő programlogika.

- [Ben Shneiderman: Publications](https://www.cs.umd.edu/~ben/publications.html)  
  Az 1973-as, Nassi és Shneiderman által írt eredeti közlemény bibliográfiája.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Structorizer User Guide  
   https://help.structorizer.fisch.lu/index.php?menu=66&page=  
   Használat: dedikált, hivatalos eszköz és dokumentáció Nassi-Shneiderman diagramokhoz.

2. inf-schule - Bausteine von Algorithmen  
   https://inf-schule.de/algorithmen/grundlagen/algorithmusbegriff/bausteine  
   Használat: megbízható oktatási forrás, amely egymás mellett mutat struktogrammot és flussdiagrammot.

Megnyitva: `2026-04-08`
