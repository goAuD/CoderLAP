# Sortieralgorithmen: Bubblesort / Quicksort

## Lényeg 30 másodpercben

A `Bubble Sort` és a `Quick Sort` is rendezési algoritmus, de nagyon eltérő hatékonyságúak.

Röviden:

- `Bubble Sort`: egyszerű, de lassú
- `Quick Sort`: általában sokkal gyorsabb
- vizsgán fontos a működési elv és az alapvető összehasonlítás

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
- a többi elemet két részre osztja
- egyik oldalra kerülnek a kisebbek, másikra a nagyobbak
- ezután rekurzívan rendezi a részeket

Ez tipikusan sokkal gyorsabb megközelítés.

## Egyszerű működési különbség

### Bubble Sort

```text
szomszédos elemek összehasonlítása
-> csere
-> újabb végigmenet
```

### Quick Sort

```text
pivot kiválasztása
-> felosztás kisebb / nagyobb részre
-> rekurzív rendezés
```

## Hatékonyság röviden

| Algoritmus | Jellemző időigény |
|---|---|
| Bubble Sort | tipikusan `O(n^2)` |
| Quick Sort | tipikusan `O(n log n)` |

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

> A Bubble Sort egy egyszerű rendezési algoritmus, amely a szomszédos elemek ismételt összehasonlításával és cseréjével rendezi a listát.  
> A Quick Sort ezzel szemben egy pivot elem köré osztja fel az adatokat, majd a részeket rekurzívan rendezi.  
> A Quick Sort a gyakorlatban általában jóval hatékonyabb, míg a Bubble Sort inkább tanulási célra hasznos.

## Gyakori vizsgahibák

- Azt állítani, hogy a Bubble Sort gyors.
- Nem megemlíteni a pivot szerepét a Quick Sortnál.
- Elfelejteni, hogy a Quick Sort gyakran rekurzív.
- A működési elvet összekeverni a pontos kódmegvalósítással.

## Gyors önellenőrzés

1. Hogyan működik a Bubble Sort?
2. Mi a pivot a Quick Sortban?
3. Melyik szokott gyorsabb lenni?
4. Miért tanítják mégis a Bubble Sortot?
5. Milyen gondolkodást igényel a Quick Sort?

## Rövid válaszok az önellenőrzéshez

1. Szomszédos elemek cserélgetésével rendez
2. Egy kiválasztott elem, ami köré felosztjuk a listát
3. Általában a Quick Sort
4. Mert egyszerű és szemléletes
5. Felosztásos és rekurzív gondolkodást

## Források

1. NIST DADS - bubble sort  
   https://xlinux.nist.gov/dads/HTML/bubblesort.html  
   Használat: hivatalos definíció és komplexitási háttér a `Bubble Sort`-hoz.

2. NIST DADS - quicksort  
   https://xlinux.nist.gov/dads/HTML/quicksort.html  
   Használat: hivatalos definíció és teljesítménybeli háttér a `Quick Sort`-hoz.

Megnyitva: `2026-04-09`
