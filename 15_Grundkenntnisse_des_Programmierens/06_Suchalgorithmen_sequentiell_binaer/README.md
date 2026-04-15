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

## Egyszerű példa

Keresett érték: `42`

### Szekvenciális keresés a gyakorlatban

```text
5 -> 11 -> 19 -> 42
```

Végig kell menni az elemeken sorban.

### Bináris keresés a gyakorlatban

```text
rendezett lista
-> középső elem
-> bal vagy jobb fél
-> új közép
```

## Mikor melyiket?

### Szekvenciális keresés

- kicsi adatmennyiségnél
- rendezetlen adatoknál
- gyorsan implementálható megoldásként

### Bináris keresés

- nagyobb adathalmaznál
- ha az adatok rendezettek
- ha sok keresést kell végezni

## Bináris keresés: fontos feltétel

Ez vizsgán kulcspont:

- ha az adatok nincsenek rendezve, a bináris keresés nem alkalmazható közvetlenül

## Vizsgán jól használható megfogalmazás

> A szekvenciális keresés az elemeket sorban vizsgálja meg, amíg meg nem találja a keresett értéket vagy a lista  
> végére nem ér.  
> A bináris keresés ezzel szemben mindig megfelezi a keresési tartományt, ezért gyorsabb, de csak rendezett adatok  
> esetén használható.  
> A két algoritmus közti legfontosabb különbség a működési elv és a rendezettségi feltétel.

## Gyakori vizsgahibák

- Elfelejteni, hogy a bináris kereséshez rendezett lista kell.
- Azt állítani, hogy a bináris keresés mindig jobb.
- Nem megemlíteni a lineáris keresés egyszerűségét.
- Összekeverni a bináris keresést a bináris fával.

## Gyors önellenőrzés

1. Hogyan működik a szekvenciális keresés?
2. Mi a bináris keresés alapötlete?
3. Mi a bináris keresés feltétele?
4. Melyik egyszerűbb?
5. Melyik gyorsabb nagy rendezett listán?

## Rövid válaszok az önellenőrzéshez

1. Sorban végigvizsgálja az elemeket
2. Mindig megfelezi a keresési tartományt
3. Rendezett adatok
4. A szekvenciális keresés
5. A bináris keresés

## Források

1. NIST DADS - linear search  
   https://xlinux.nist.gov/dads/HTML/linearSearch.html  
   Használat: hivatalos definíció és komplexitási háttér a szekvenciális kereséshez.

2. NIST DADS - binary search  
   https://xlinux.nist.gov/dads/HTML/binarySearch.html  
   Használat: hivatalos definíció és működési háttér a bináris kereséshez.

Megnyitva: `2026-04-09`
