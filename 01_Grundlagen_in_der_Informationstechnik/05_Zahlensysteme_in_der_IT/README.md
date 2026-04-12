# Zahlensysteme in der IT

## Gyors vizuális kép

| Számrendszer  | Alap | Használt számjegyek | Példa ugyanarra az értékre |
| ------------- | ---: | ------------------- | -------------------------- |
| bináris       |  `2` | `0, 1`              | `101010₂`                  |
| oktális       |  `8` | `0-7`               | `52₈`                      |
| decimális     | `10` | `0-9`               | `42₁₀`                     |
| hexadecimális | `16` | `0-9, A-F`          | `2A₁₆`                     |

Mind a négy szám ugyanazt az értéket jelentheti:

- `42`

## Mi az a számrendszer?

A számrendszer egy szabályrendszer arra, hogyan írunk le mennyiségeket számjegyekkel.

A helyiértékes rendszer lényege:

- minden pozíció súlya más
- ez a súly az alap hatványaiból adódik

Példa decimális rendszerben:

`542` =

- `5 × 10^2`
- `4 × 10^1`
- `2 × 10^0`

## 1. Decimális számrendszer

Ez a hétköznapi, ember által leggyakrabban használt rendszer.

Alapja:

- `10`

Számjegyei:

- `0-9`

Példa:

`347` =

- `3 × 10^2`
- `4 × 10^1`
- `7 × 10^0`

## 2. Bináris számrendszer

Az informatika alapja a bináris rendszer, mert a digitális áramkörök természetesen két állapottal dolgoznak:

- `0`
- `1`

Alapja:

- `2`

Példa:

`1011₂` =

- `1 × 2^3`
- `0 × 2^2`
- `1 × 2^1`
- `1 × 2^0`

Ez decimálisan:

- `8 + 0 + 2 + 1 = 11`

## 3. Oktális számrendszer

Az oktális rendszer alapja:

- `8`

Számjegyei:

- `0-7`

Ma ritkábban használjuk, de még találkozhatunk vele például:

- régebbi rendszerekben
- jogosultsági jelölésekben
- alacsony szintű technikai környezetekben

Példa:

`17₈` =

- `1 × 8^1 + 7 × 8^0 = 15₁₀`

## 4. Hexadecimális számrendszer

Alapja:

- `16`

Számjegyei:

- `0-9`
- `A, B, C, D, E, F`

ahol:

- `A = 10`
- `B = 11`
- `C = 12`
- `D = 13`
- `E = 14`
- `F = 15`

Példa:

`2A₁₆` =

- `2 × 16^1 + 10 × 16^0`
- `32 + 10 = 42`

## Miért fontos a hexadecimális rendszer?

Mert nagyon jól illeszkedik a bináris világhoz:

- `1 hexadecimális számjegy = 4 bit`

Ezért a hosszú bináris sorozatok sokkal rövidebben írhatók hexában.

Példa:

- binárisan: `11111111`
- hexában: `FF`

## Hol használják ezeket az informatikában?

### Decimális

- hétköznapi számolás
- felhasználói felületek
- üzleti adatok

### Bináris

- bitek
- processzorok
- memória
- alacsony szintű működés

### Oktális

- néhány rendszer- és jogosultsági jelölés
- speciális technikai környezetek

### Hexadecimális

- memóriacímek
- hibakódok
- színkódok, például CSS-ben
- bájtok rövid jelölése
- bináris adatok áttekinthető ábrázolása

## Gyakori jelölések programozásban

Sok nyelv és eszköz használ prefixeket:

- `0b1010` = bináris
- `0o52` = oktális
- `42` = decimális
- `0x2A` = hexadecimális

Ez nyelvenként változhat, de az alapötlet ugyanaz.

## Vizsgán jól használható megfogalmazás

> Az informatikában leggyakrabban a bináris, oktális, decimális és hexadecimális számrendszert használjuk.  
> A bináris rendszer alapja 2, ezért csak 0 és 1 számjegyeket használ.  
> A decimális rendszer alapja 10, ez a hétköznapi számrendszer.  
> A hexadecimális rendszer alapja 16, és azért fontos,
> mert jól tömöríti a bináris adatokat:
> egy hexaszámjegy 4 bitnek felel meg.

## Gyakori vizsgahibák

- Elfelejteni, hogy hexában az `A-F` is számjegy.
- Azt mondani, hogy az oktális alapja `16`.
- Nem tudni, hogy a bináris rendszer csak `0`-t és `1`-et használ.
- Nem felismerni, hogy ugyanaz a szám több számrendszerben máshogy néz ki.
- Nem tudni, miért praktikus a hexadecimális jelölés.

## Gyors önellenőrzés

1. Melyik számrendszer alapja `2`?
2. Melyik számrendszer használ `0-9` és `A-F` jeleket?
3. Mennyi a `2A₁₆` decimálisan?
4. Melyik számrendszert használjuk leginkább a digitális hardver logikájához?
5. Miért hasznos a hexadecimális rendszer?

## Rövid válaszok az önellenőrzéshez

1. A **bináris**
2. A **hexadecimális**
3. `42`
4. A **bináris**
5. Mert kompaktan írja le a bináris adatokat, és `1 hexaszámjegy = 4 bit`

## Források

1. Microsoft Learn - Literals in Q#  
   https://learn.microsoft.com/en-us/azure/quantum/user-guide/language/expressions/valueliterals  
   Használat: bináris, oktális, decimális és hexadecimális jelölések modern, hivatalos példái.

2. Oracle - Binary Literals (Java SE 7+)  
   https://docs.oracle.com/javase/8/docs/technotes/guides/language/binary-literals.html  
   Használat: bináris és hexadecimális reprezentáció gyakorlati használata programozásban.

3. MDN - parseInt()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt  
   Használat: a `radix` fogalma, számrendszerek és érvényes számjegyek.

4. MDN - Number.prototype.toString()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString  
   Használat: különböző alapú számábrázolás és konverzió programozásban.

5. IBM Docs - ASCII and Hex Equivalents  
   https://www.ibm.com/docs/en/iis/11.7.0?topic=reference-ascii-hex-equivalents  
   Használat: bináris, oktális, decimális és hexadecimális megfelelések áttekintése.

Megnyitva: `2026-04-08`
