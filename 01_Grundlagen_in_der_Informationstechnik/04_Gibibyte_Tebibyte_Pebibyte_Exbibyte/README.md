# Gibibyte, Tebibyte, Pebibyte, Exbibyte

## Gyors vizuális kép

| Egység | Jelölés | Szorzó | Byte-ban |
|---|---|---:|---:|
| gibibyte | `GiB` | `2^30` | `1 073 741 824 B` |
| tebibyte | `TiB` | `2^40` | `1 099 511 627 776 B` |
| pebibyte | `PiB` | `2^50` | `1 125 899 906 842 624 B` |
| exbibyte | `EiB` | `2^60` | `1 152 921 504 606 846 976 B` |

### Emlékeztető

A bináris egységek a `2^10 = 1024` lépésre épülnek:

- `1 TiB = 1024 GiB`
- `1 PiB = 1024 TiB`
- `1 EiB = 1024 PiB`

## Miért jöttek létre ezek az egységek?

A digitális rendszerek természetesen **kettes alapúak**, ezért a memória és sok belső technikai számítás valójában `2` hatványaira épül.

Sokáig a gyakorlatban a `KB`, `MB`, `GB` jelöléseket használták olyan értékekre is, amelyek valójában:

- `1024`
- `1024^2`
- `1024^3`

alapúak voltak.

Ez félreértésekhez vezetett, ezért vezették be a pontosabb bináris neveket:

- `KiB`
- `MiB`
- `GiB`
- `TiB`
- `PiB`
- `EiB`

## Mit jelent a név?

A bináris prefixek úgy jöttek létre, hogy a megfelelő SI-prefix első része mellé hozzáadták a `bi` részt, ami a `binary` szóra utal.

Példák:

- `giga` → `gibi`
- `tera` → `tebi`
- `peta` → `pebi`
- `exa` → `exbi`

A jelölésben ezért jelenik meg az extra `i`:

- `GB` vs `GiB`
- `TB` vs `TiB`

## GiB és GB: a legfontosabb különbség

| Egység | Típus | Érték |
|---|---|---|
| `GB` | decimális | `10^9 byte` |
| `GiB` | bináris | `2^30 byte` |

Ez számokban:

- `1 GB = 1 000 000 000 byte`
- `1 GiB = 1 073 741 824 byte`

Tehát a `GiB` nagyobb, mint a `GB`.

Ugyanez igaz nagyobb egységeknél is:

- `TiB > TB`
- `PiB > PB`
- `EiB > EB`

## Hol találkozol velük a gyakorlatban?

### 1. Operációs rendszerek és memória

A RAM, cache és sok belső memóriafogalom természetesen bináris világban értelmezhető, ezért itt a bináris egységek logikusabbak.

### 2. Rendszereszközök és technikai dokumentáció

Szakmai dokumentációkban egyre fontosabb a pontos jelölés:

- `GB` ha decimális
- `GiB` ha bináris

### 3. Tárhelykijelzésnél tapasztalt eltérések

Egy gyártó megadhat egy háttértárat `1 TB`-ként, miközben az operációs rendszer bináris logika szerint jelenít meg méretet. Ettől a felhasználó kisebbnek érezheti a kapacitást, pedig valójában csak más egységet lát.

## Gyors példák

### Példa 1

`1 GiB` =

- `2^30 byte`
- `1 073 741 824 byte`

### Példa 2

`2 TiB` =

- `2 × 2^40 byte`
- `2 199 023 255 552 byte`

### Példa 3

`1 PiB` =

- `2^50 byte`
- `1 125 899 906 842 624 byte`

## Kapcsolat a kisebb bináris egységekkel

Teljesebb lánc:

- `1 KiB = 2^10 B`
- `1 MiB = 2^20 B`
- `1 GiB = 2^30 B`
- `1 TiB = 2^40 B`
- `1 PiB = 2^50 B`
- `1 EiB = 2^60 B`

## Vizsgán jól használható megfogalmazás

> A gibibyte, tebibyte, pebibyte és exbibyte bináris adatméret-egységek.  
> Ezek 2 hatványaira épülnek, ezért például 1 GiB = 2^30 byte, 1 TiB = 2^40 byte.  
> A GiB, TiB, PiB és EiB nem azonos a GB, TB, PB és EB decimális egységekkel.  
> A bináris prefixeket azért vezették be, hogy egyértelmű legyen a 1000-es és 1024-es alapú számítás közti különbség.

## Gyakori vizsgahibák

- A `GiB` és `GB` felcserélése.
- Azt mondani, hogy `1 GiB = 1 000 000 000 byte`.
- Elfelejteni, hogy a bináris lépés `1024`, nem `1000`.
- Nem tudni, miért van `i` a jelölésben.
- Azt hinni, hogy a bináris prefixek SI-prefixek.

## Gyors önellenőrzés

1. Mennyi `1 GiB` byte-ban?
2. Mennyi `1 TiB` byte-ban?
3. Melyik nagyobb: `1 GB` vagy `1 GiB`?
4. Miért vezették be a `GiB` jelölést?
5. Mennyi `1 EiB` byte-ban?

## Rövid válaszok az önellenőrzéshez

1. `1 073 741 824 byte`
2. `1 099 511 627 776 byte`
3. `1 GiB` nagyobb
4. Azért, hogy egyértelmű legyen a bináris és decimális egységek különbsége
5. `1 152 921 504 606 846 976 byte`

## Források

1. NIST - Definitions of the SI units: The binary prefixes  
   https://physics.nist.gov/cgi-bin/cuu/Info/Units/binary.html  
   Használat: a bináris prefixek hivatalos definíciója és összehasonlítása az SI-prefixekkel.

2. NIST CSRC Glossary - gibibyte  
   https://csrc.nist.gov/glossary/term/gibibyte  
   Használat: `GiB = 2^30 byte`.

3. NIST CSRC Glossary - tebibyte  
   https://csrc.nist.gov/glossary/term/tebibyte  
   Használat: `TiB = 2^40 byte`.

4. NIST CSRC Glossary - pebibyte  
   https://csrc.nist.gov/glossary/term/pebibyte  
   Használat: `PiB = 2^50 byte`.

5. NIST CSRC Glossary - exbibyte  
   https://csrc.nist.gov/glossary/term/eib  
   Használat: `EiB = 2^60 byte`.

6. NIST SP 811  
   https://physics.nist.gov/cuu/pdf/sp811.pdf  
   Használat: a bináris prefixek NIST-féle szabványos háttere.

Megnyitva: `2026-04-08`
