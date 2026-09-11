# Suchalgorithmen: sequentiell / binaer

## Gyors vizuális kép

| Algoritmus | Feltétel | Jellemző időigény |
|---|---|---|
| szekvenciális / lineáris | nem kell rendezett lista | `O(n)` |
| bináris | rendezett lista kell | `O(log n)` |

## Mi az a szekvenciális keresés?

A szekvenciális keresés:

- az elemeket sorban vizsgálja
- addig halad, amíg meg nem találja a keresett értéket
- vagy el nem fogy a lista

Előnye:

- nagyon egyszerű
- nem kell rendezett adathalmaz

Hátránya:

- nagy listáknál lassú lehet

## Mi az a bináris keresés?

A bináris keresés csak **rendezett** adatoknál használható.

Lépései:

1. megnézi a középső elemet
2. összehasonlítja a keresett értékkel
3. eldönti, hogy balra vagy jobbra kell tovább keresni
4. megint megfelezi a maradék részt

Ezért sokkal gyorsabb lehet.

## Kidolgozott példák JavaScriptben

Feladat: keressük meg a 42-t az `[5, 11, 19, 42, 70]` számtömbben.
A függvények a megtalált elem **indexét** adják vissza. Az indexelés 0-tól indul,
ezért a 42 indexe 3. Ha a keresés találat nélkül fejeződik be, az eredmény `-1`.
A példák véges számokkal dolgoznak, a tömböt változatlanul hagyják.
Mindkét JavaScript-blokk önállóan futtatható, például `node pelda.js` paranccsal
egy telepített Node.js környezetben.

### Lineáris keresés: elemenként haladunk

```javascript
function linearSearch(values, target) {
  for (let index = 0; index < values.length; index++) {
    if (values[index] === target) {
      return index;
    }
  }
  return -1;
}

console.log(linearSearch([5, 11, 19, 42, 70], 42));
console.log(linearSearch([5, 11, 19, 42, 70], 8));
```

Kimenet:

```text
3
-1
```

A keresés először az 5-öt, majd a 11-et, a 19-et és a 42-t vizsgálja meg.
A `return index` a találatnál az egész függvényt befejezi. A 8 keresésekor mind
az öt elem sorra kerül, majd a ciklus utáni `return -1` fut le.
Több azonos értéknél ez a változat az első előfordulás indexét adja vissza.

### Bináris keresés: a vizsgált tartomány felezése

Előfeltétel: a `values` tömb **növekvően rendezett**, azonos értékek is lehetnek
benne. A függvény ezt a rendezettséget adottnak veszi. A `left` és `right`
a még vizsgált tartomány első és utolsó indexe, mindkét határ beleértendő.

```javascript
function binarySearch(values, target) {
  let left = 0;
  let right = values.length - 1;
  while (left <= right) {
    const middle = left + Math.floor((right - left) / 2);
    if (values[middle] === target) {
      return middle;
    }
    if (values[middle] < target) {
      left = middle + 1;
    } else {
      right = middle - 1;
    }
  }
  return -1;
}

console.log(binarySearch([5, 11, 19, 42, 70], 42));
console.log(binarySearch([5, 11, 19, 42, 70], 8));
```

Kimenet:

```text
3
-1
```

| Lépés a 42 keresésekor | `left` | `right` | `middle` | Döntés |
|---|---|---|---|---|
| 1. | 0 | 4 | 2 | a 19 kisebb a 42-nél, ezért `left = 3` |
| 2. | 3 | 4 | 3 | a középső érték 42, visszatérünk a 3-as indexszel |

A `Math.floor` lefelé kerekít, így egész indexet kapunk. Az összehasonlított
középső elemet a következő körből kizárjuk a `+ 1` vagy `- 1` lépéssel, ezért
a tartomány folyamatosan szűkül. Amikor `left > right`, a tartomány üres:
a keresés eredménye `-1`. Üres bemenetnél ez már az első feltételvizsgálatkor igaz.
Ismétlődő értéknél ez a változat egy egyező elem indexét adja vissza; az első
előfordulás megkeresése külön keresési változat feladata.

## Mikor melyiket?

### Szekvenciális keresés

- kicsi adatmennyiségnél
- rendezetlen adatoknál
- gyorsan implementálható megoldásként

### Bináris keresés

- nagyobb adathalmaznál
- ha az adatok rendezettek
- ha sok keresést kell végezni

## A rendezettség és a teljes munkaigény

A bináris keresés előnye a már rendezett, indexelhető tömbön érvényesül.
Ha előbb rendezni kell az adatokat, annak költsége is a teljes feladathoz tartozik.
Egyetlen kereséshez a lineáris bejárás gyakran egyszerűbb; sok keresésnél
a rendezettség fenntartása megtérülhet. A bináris keresés itt indexhatárokat mozgat
egy tömbön; a bináris fa önálló, csomópontokból álló adatszerkezet.

## Vizsgán jól használható megfogalmazás

> A szekvenciális keresés az elemeket sorban vizsgálja meg, amíg meg nem találja a keresett értéket vagy a lista  
> végére nem ér.  
> A bináris keresés ezzel szemben mindig megfelezi a keresési tartományt, ezért gyorsabb, de csak rendezett adatok  
> esetén használható.  
> A két algoritmus közti legfontosabb különbség a működési elv és a rendezettségi feltétel.

## Gyors önellenőrzés

1. Mit jelent a példákban a 3-as visszatérési érték?
2. Melyik elemet vizsgálja először a bináris keresés a megadott ötelemű tömbben?
3. Miért lesz `left = middle + 1`, ha a középső érték kisebb a keresettnél?
4. Mit adnak vissza a függvények üres tömbre?
5. Miért érdemes az előzetes rendezés költségét is mérlegelni?

## Rövid válaszok az önellenőrzéshez

1. Az elem indexét: a 42 a negyedik helyen, a 3-as indexen található.
2. A 2-es indexű 19-et.
3. A rendezett tömbben a közép és a tőle balra lévő értékek túl kicsik; a következő jelölt a közép utáni elem.
4. `-1`-et, mert nincs vizsgálható elem.
5. A teljes munka a rendezést és a kereséseket együtt tartalmazza; egy kereséshez a lineáris bejárás kedvezőbb is lehet.

## Források

1. NIST DADS - linear search  
   https://xlinux.nist.gov/dads/HTML/linearSearch.html  
   Használat: hivatalos definíció és komplexitási háttér a szekvenciális kereséshez.

2. NIST DADS - binary search  
   https://xlinux.nist.gov/dads/HTML/binarySearch.html  
   Használat: hivatalos definíció és működési háttér a bináris kereséshez.

Megnyitva: `2026-09-11`
