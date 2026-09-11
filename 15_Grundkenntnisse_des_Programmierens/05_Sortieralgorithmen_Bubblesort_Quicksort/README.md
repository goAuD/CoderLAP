# Sortieralgorithmen: Bubblesort / Quicksort

## Gyors vizuális kép

| Algoritmus | Alapelv | Tipikus teljesítmény |
|---|---|---|
| Bubble Sort | szomszédos elemek cserélgetése | gyenge nagy listáknál |
| Quick Sort | pivot körüli felosztás, majd rekurzív rendezés | általában gyors |

## Mi az a Bubble Sort?

A `Bubble Sort` úgy működik, hogy:

- végigmegy a listán
- összehasonlítja a szomszédos elemeket
- ha rossz sorrendben vannak, felcseréli őket
- ezt addig ismétli, amíg nincs több csere

Ez egyszerű és jól tanítható, de nagy adatmennyiségnél nem hatékony.

## Mi az a Quick Sort?

A `Quick Sort` alapötlete:

- választ egy elemet, ez a `pivot`
- az elemeket a pivothoz viszonyítva csoportosítja
- a kisebb és nagyobb elemek közötti helyre kerülnek a pivottal egyenlők
- ezután rekurzívan rendezi a részeket

Ez tipikusan sokkal gyorsabb megközelítés.

## Kidolgozott példák JavaScriptben

Feladat: rendezzük a `[4, 2, 4, 1]` tömb számait növekvő sorrendbe.
A példák véges számokból álló tömböt várnak, és új rendezett tömböt adnak vissza;
a bemenet változatlan marad. Minden JavaScript-blokk külön fájlba másolva
futtatható, például `node pelda.js` paranccsal egy telepített Node.js környezetben.

### Bubble Sort: szomszédos elemek összehasonlítása

```javascript
function bubbleSort(values) {
  const result = [...values];
  for (let end = result.length - 1; end > 0; end--) {
    let swapped = false;
    for (let index = 0; index < end; index++) {
      if (result[index] > result[index + 1]) {
        const previous = result[index];
        result[index] = result[index + 1];
        result[index + 1] = previous;
        swapped = true;
      }
    }
    if (!swapped) {
      break;
    }
  }
  return result;
}

console.log(JSON.stringify(bubbleSort([4, 2, 4, 1])));
```

Kimenet:

```text
[1,2,4,4]
```

A `[...values]` másolatot készít. A belső ciklus két szomszédos számot vizsgál:
ha a bal oldali nagyobb, a `previous` ideiglenes változó segítségével felcseréli
őket. A `JSON.stringify` a tömböt egységes szöveges alakban jeleníti meg.

| Menet | Kezdőállapot | Állapot a menet végén |
|---|---|---|
| 1., `end = 3` | `[4, 2, 4, 1]` | `[2, 4, 1, 4]` |
| 2., `end = 2` | `[2, 4, 1, 4]` | `[2, 1, 4, 4]` |
| 3., `end = 1` | `[2, 1, 4, 4]` | `[1, 2, 4, 4]` |

Minden menet a még vizsgált rész legnagyobb elemét a rész végére juttatja.
Ezért az `end` határt eggyel csökkentjük. Ha egy teljes menetben nem történt
csere, a tömb már rendezett, és a `break` befejezi a külső ciklust.
Üres és egyelemű tömbnél a másolat közvetlenül visszakerül a hívóhoz.

### Quick Sort: felosztás és rekurzió

Ez a tanulási változat három külön tömbben gyűjti a kisebb, egyenlő és nagyobb
értékeket. Az egyenlő elemek csoportja megőrzi az ismétlődő számokat is.

```javascript
function quickSort(values) {
  if (values.length <= 1) {
    return [...values];
  }
  const pivot = values[0];
  const smaller = [];
  const equal = [];
  const larger = [];
  for (const value of values) {
    if (value < pivot) {
      smaller.push(value);
    } else if (value > pivot) {
      larger.push(value);
    } else {
      equal.push(value);
    }
  }
  return [...quickSort(smaller), ...equal, ...quickSort(larger)];
}

console.log(JSON.stringify(quickSort([4, 2, 4, 1])));
```

Kimenet:

```text
[1,2,4,4]
```

Az első pivot 4: `smaller = [2, 1]`, `equal = [4, 4]`, `larger = []`.
A `[2, 1]` részben a pivot 2, így `[1]`, `[2]` és `[]` keletkezik.
Az üres és egyelemű részek már rendezettek: ez a rekurzió **alapesete**.
A visszatérő eredmények összefűzése előbb `[1, 2]`, majd `[1, 2, 4, 4]`.

A pivot és az azzal egyenlő elemek kikerülnek a további rekurzív hívásokból,
ezért a feldolgozott rész mérete csökken. Ez a megoldás külön tömböket foglal
a szemléletes működésért; léteznek helyben rendező Quick Sort változatok is.
Itt az első elem a pivot: már rendezett, különböző értékeknél ez egyenlőtlen
felosztásokhoz és `O(n^2)` időigényhez vezethet. Nagy bemenetnél a rekurzió
mélységét a futtatókörnyezet hívási veremének mérete is korlátozza.

## Hatékonyság röviden

| Algoritmus | Jellemző időigény |
|---|---|
| Bubble Sort | általános és legrosszabb esetben `O(n^2)`; a fenti változat rendezett bemeneten `O(n)` |
| Quick Sort | átlagosan `O(n log n)` megfelelő bemeneteloszlás vagy pivotválasztás mellett; legrosszabb esetben `O(n^2)` |

Megjegyzés:

- a `Quick Sort` legrosszabb esete lehet `O(n^2)`
- de a gyakorlatban általában mégis sokkal jobb, mint a `Bubble Sort`

## Mikor mit érdemes tudni?

### Bubble Sort

- jó tanuláshoz
- könnyű megérteni
- valós projekthez ritkán ideális nagyobb adatoknál

### Quick Sort

- fontos klasszikus algoritmus
- gyors
- rekurziót és felosztásos gondolkodást igényel

## Vizsgán jól használható megfogalmazás

> A Bubble Sort egy egyszerű rendezési algoritmus, amely a szomszédos elemek ismételt összehasonlításával és  
> cseréjével rendezi a listát.  
> A Quick Sort ezzel szemben egy pivot elem köré osztja fel az adatokat, majd a részeket rekurzívan rendezi.  
> A Quick Sort a gyakorlatban általában jóval hatékonyabb, míg a Bubble Sort inkább tanulási célra hasznos.

## Gyors önellenőrzés

1. Miért csökkenhet az `end` minden Bubble Sort menet után?
2. Mit eredményez a `swapped = false` egy teljes menet végén?
3. Melyik csoportba kerül a két 4-es a Quick Sort példában?
4. Mi a rekurzió alapesete, és mi biztosítja, hogy elérjük?
5. Milyen eredményt ad mindkét függvény `[]` és `[7]` bemenetre?

## Rövid válaszok az önellenőrzéshez

1. A vizsgált rész legnagyobb eleme a menet végére a végleges helyére kerül.
2. A `break` befejezi a rendezést, mert minden vizsgált szomszédpár sorrendje megfelelő.
3. Az `equal` tömbbe; mindkét előfordulás megmarad.
4. A legfeljebb egyelemű tömb. A kisebb és nagyobb csoport egyaránt rövidebb az eredeti résznél.
5. Új `[]`, illetve `[7]` tömböt; a bemenet változatlan marad.

## Források

1. NIST DADS - bubble sort  
   https://xlinux.nist.gov/dads/HTML/bubblesort.html  
   Használat: hivatalos definíció és komplexitási háttér a `Bubble Sort`-hoz.

2. NIST DADS - quicksort  
   https://xlinux.nist.gov/dads/HTML/quicksort.html  
   Használat: hivatalos definíció és teljesítménybeli háttér a `Quick Sort`-hoz.

Megnyitva: `2026-09-11`
