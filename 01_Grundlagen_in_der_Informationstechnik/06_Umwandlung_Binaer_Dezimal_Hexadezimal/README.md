# Umwandlung zwischen Binär-, Dezimal- und Hexadezimalzahlen

## Gyors vizuális kép

| Számrendszer  | Alap | Jellegzetes jelek |
| ------------- | ---: | ----------------- |
| bináris       |  `2` | `0, 1`            |
| decimális     | `10` | `0-9`             |
| hexadecimális | `16` | `0-9, A-F`        |

### Kulcskapcsolat

| Hexa | Bináris |
| ---- | ------- |
| `0`  | `0000`  |
| `1`  | `0001`  |
| `2`  | `0010`  |
| `3`  | `0011`  |
| `4`  | `0100`  |
| `5`  | `0101`  |
| `6`  | `0110`  |
| `7`  | `0111`  |
| `8`  | `1000`  |
| `9`  | `1001`  |
| `A`  | `1010`  |
| `B`  | `1011`  |
| `C`  | `1100`  |
| `D`  | `1101`  |
| `E`  | `1110`  |
| `F`  | `1111`  |

Ez az egyik leghasznosabb vizsgatáblázat.

## 1. Bináris → Decimális

Módszer:

- minden helyiértéket megszorzunk a megfelelő `2` hatvánnyal
- az eredményeket összeadjuk

### Példa

`101101₂`

Szétszedve:

- `1 × 2^5 = 32`
- `0 × 2^4 = 0`
- `1 × 2^3 = 8`
- `1 × 2^2 = 4`
- `0 × 2^1 = 0`
- `1 × 2^0 = 1`

Összesen:

- `32 + 8 + 4 + 1 = 45`

Tehát:

- `101101₂ = 45₁₀`

## 2. Decimális → Bináris

Módszer:

- osztunk `2`-vel
- feljegyezzük a maradékokat
- a maradékokat alulról felfelé olvassuk

### Példa

`45₁₀`

| Osztás   | Hányados | Maradék |
| -------- | -------: | ------: |
| `45 / 2` |     `22` |     `1` |
| `22 / 2` |     `11` |     `0` |
| `11 / 2` |      `5` |     `1` |
| `5 / 2`  |      `2` |     `1` |
| `2 / 2`  |      `1` |     `0` |
| `1 / 2`  |      `0` |     `1` |

Alulról felfelé:

- `101101`

Tehát:

- `45₁₀ = 101101₂`

## 3. Bináris → Hexadecimális

Módszer:

- jobbról indulva `4 bites` csoportokra bontjuk a bináris számot
- ha kell, bal oldalon nullákkal kiegészítjük
- minden `4 bites` csoportot egy hexaszámjegyre cserélünk

### Példa

`1101111010₂`

Négyes csoportokban:

- `0011 0111 1010`

Átváltva:

- `0011 = 3`
- `0111 = 7`
- `1010 = A`

Tehát:

- `1101111010₂ = 37A₁₆`

## 4. Hexadecimális → Bináris

Módszer:

- minden hexaszámjegyet lecserélünk a megfelelő `4 bites` bináris alakra

### Példa

`7B₁₆`

Átváltás:

- `7 = 0111`
- `B = 1011`

Tehát:

- `7B₁₆ = 01111011₂`

## 5. Decimális → Hexadecimális

Módszer:

- osztás `16`-tal
- maradékok feljegyzése
- a maradékokat alulról felfelé olvassuk

### Példa

`123₁₀`

| Osztás     | Hányados | Maradék |
| ---------- | -------: | ------: |
| `123 / 16` |      `7` |    `11` |
| `7 / 16`   |      `0` |     `7` |

A `11` hexában:

- `B`

Alulról felfelé:

- `7B`

Tehát:

- `123₁₀ = 7B₁₆`

## 6. Hexadecimális → Decimális

Módszer:

- megszorozzuk a számjegyeket a megfelelő `16` hatványokkal
- összeadjuk az eredményt

### Példa

`2F₁₆`

ahol:

- `2 = 2`
- `F = 15`

Számolás:

- `2 × 16^1 = 32`
- `15 × 16^0 = 15`

Összesen:

- `32 + 15 = 47`

Tehát:

- `2F₁₆ = 47₁₀`

## Miért fontos a bináris ↔ hexadecimális átváltás?

Mert ez a leggyorsabb gyakorlati kapcsolat:

- `1 hexaszámjegy = 4 bit`

Ezért:

- memóriacímek
- hibakódok
- színek
- bájtértékek

esetén a hexadecimális alak nagyon praktikus.

## Vizsgán jól használható megfogalmazás

> A bináris, decimális és hexadecimális számok közti átváltás alapja a helyiértékes rendszer.  
> Binárisból decimálisba 2 hatványok alapján számolunk, decimálisból binárisba pedig 2-vel osztunk és a maradékokat olvassuk visszafelé.  
> Hexadecimális és bináris között különösen könnyű az átváltás, mert egy hexaszámjegy pontosan 4 bitnek felel meg.

## Gyakori vizsgahibák

- Rossz irányban olvasni a maradékokat osztásos módszernél.
- Elfelejteni, hogy `A-F` értéke `10-15`.
- Bináris számot nem balról jobbra, hanem rossz helyiértékekkel értelmezni.
- Nem `4` bites blokkokra bontani a bináris számot hexa előtt.
- A `0` helyiértékeit kihagyni a számolásból.

## Gyors önellenőrzés

1. Mennyi `1010₂` decimálisan?
2. Mennyi `13₁₀` binárisan?
3. Mennyi `1111₂` hexadecimálisan?
4. Mennyi `A₁₆` binárisan?
5. Mennyi `FF₁₆` decimálisan?

## Rövid válaszok az önellenőrzéshez

1. `10`
2. `1101`
3. `F`
4. `1010`
5. `255`

## Források

1. MDN - parseInt()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt  
   Használat: számrendszer-alap (`radix`) és különböző alapú számok értelmezése.

2. MDN - Number.prototype.toString()  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toString  
   Használat: számok különböző alapú reprezentációja és konverziós példák.

3. Microsoft Learn - Literals in Q#  
   https://learn.microsoft.com/en-us/azure/quantum/user-guide/language/expressions/valueliterals  
   Használat: bináris, oktális, decimális és hexadecimális jelölések hivatalos példái.

4. Oracle - Binary Literals  
   https://docs.oracle.com/javase/8/docs/technotes/guides/language/binary-literals.html  
   Használat: bináris és hexadecimális számábrázolás gyakorlati programozási példákban.

5. IBM Docs - ASCII and Hex Equivalents  
   https://www.ibm.com/docs/en/iis/11.7.0?topic=reference-ascii-hex-equivalents  
   Használat: konkrét megfeleléstábla bináris, oktális, decimális és hexadecimális értékekhez.

Megnyitva: `2026-04-08`
