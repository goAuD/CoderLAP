# Gigabyte, Terabyte, Petabyte, Exabyte

## Lényeg 30 másodpercben

A **gigabyte**, **terabyte**, **petabyte** és **exabyte** a **byte** nagyobb, **tízes alapú** mértékegységei.

Ebben a témában:

- `1 GB = 10^9 B = 1 000 000 000 byte`
- `1 TB = 10^12 B = 1 000 000 000 000 byte`
- `1 PB = 10^15 B = 1 000 000 000 000 000 byte`
- `1 EB = 10^18 B = 1 000 000 000 000 000 000 byte`

Ezek **SI-prefixekre** épülnek, tehát **decimális** egységek.  
Nem ugyanazok, mint a **GiB**, **TiB**, **PiB**, **EiB** bináris egységek.

## Gyors vizuális kép

| Egység | Jelölés | Szorzó | Byte-ban |
|---|---|---:|---:|
| gigabyte | `GB` | `10^9` | `1 000 000 000 B` |
| terabyte | `TB` | `10^12` | `1 000 000 000 000 B` |
| petabyte | `PB` | `10^15` | `1 000 000 000 000 000 B` |
| exabyte | `EB` | `10^18` | `1 000 000 000 000 000 000 B` |

### Egyszerű emlékeztető

Minden újabb lépés:

- `× 1000`

Vagyis:

- `1 TB = 1000 GB`
- `1 PB = 1000 TB`
- `1 EB = 1000 PB`

## Mit jelentenek ezek az egységek?

Ezek a mértékegységek arra valók, hogy nagyon nagy adatméreteket rövidebben és áttekinthetőbben írjunk le.

Például:

- egy kisebb dokumentum néhány `KB`
- egy kép néhány `MB`
- egy film vagy játék több `GB`
- egy nagyobb háttértár több `TB`
- vállalati vagy felhős adatmennyiség eljuthat `PB` vagy `EB` tartományba

## Miért tízes alapúak?

A `giga`, `tera`, `peta`, `exa` nevek az **SI-prefixekből** származnak.

Ez azt jelenti, hogy:

- `giga = 10^9`
- `tera = 10^12`
- `peta = 10^15`
- `exa = 10^18`

Ezért a `GB`, `TB`, `PB`, `EB` egységek **nem 1024-es**, hanem **1000-es** lépésekben nőnek.

## Hol használják ezeket a gyakorlatban?

### 1. Tárhelyek marketing- és gyártói megadása

A háttértár-gyártók gyakran decimális egységet használnak.

Példa:

- `1 TB` SSD = `1 000 000 000 000 byte`

Ez technikailag helyes, csak sokan összekeverik a bináris egységekkel.

### 2. Felhőszolgáltatások és adatközpontok

Nagy adatmennyiségek esetén gyakori:

- `TB`
- `PB`
- `EB`

Például:

- backup-rendszerek
- logtárolás
- videóplatformok
- mesterséges intelligencia adatkészletek

### 3. Hálózati és üzleti kommunikáció

Riportokban, szerződésekben, szolgáltatási leírásokban is gyakran decimális egységeket használnak.

## GB és GiB: ne keverd össze

| Egység | Jelentés | Érték byte-ban |
|---|---|---:|
| `GB` | gigabyte, decimális | `10^9 = 1 000 000 000 B` |
| `GiB` | gibibyte, bináris | `2^30 = 1 073 741 824 B` |

Ugyanez nagyobb egységeknél is igaz:

| Decimális | Bináris |
|---|---|
| `TB` | `TiB` |
| `PB` | `PiB` |
| `EB` | `EiB` |

Ez a különbség azért fontos, mert ugyanannak a háttértárnak a mérete másként jelenhet meg attól függően, hogy a rendszer decimális vagy bináris egységet használ.

## Gyors példák

### Példa 1

`2 TB` =

- `2 × 10^12 B`
- `2 000 000 000 000 byte`

### Példa 2

`3 PB` =

- `3 × 10^15 B`
- `3 000 000 000 000 000 byte`

### Példa 3

`1 EB` =

- `10^18 B`
- `1 000 000 000 000 000 000 byte`

## Miért fontos vizsgán?

Mert itt szokott előjönni:

- mértékegységek helyes jelentése
- a `B` mint byte
- a tízes és bináris prefixek közti különbség
- a tárhelyek látszólagos eltérése

## Vizsgán jól használható megfogalmazás

> A gigabyte, terabyte, petabyte és exabyte nagy adatméretek jelölésére szolgáló, decimális byte-egységek.  
> Ezek SI-prefixekre épülnek, ezért 1000-es lépésekben növekednek.  
> Például 1 GB = 10^9 byte, 1 TB = 10^12 byte, 1 PB = 10^15 byte, 1 EB = 10^18 byte.  
> Fontos, hogy ezek nem azonosak a bináris GiB, TiB, PiB és EiB egységekkel.

## Gyakori vizsgahibák

- Azt mondani, hogy `1 GB = 1024 MB`.
- Összekeverni a `GB` és `GiB` jelentését.
- Elfelejteni, hogy itt a `B` byte-ot jelent.
- Azt hinni, hogy minden operációs rendszer ugyanúgy írja ki a tárhelyet.
- Nem tudni, hogy a `giga`, `tera`, `peta`, `exa` SI-prefixek.

## Gyors önellenőrzés

1. Mennyi `1 GB` byte-ban?
2. Mennyi `1 TB` byte-ban?
3. Milyen alapú a `GB`: tízes vagy kettes?
4. Mi a különbség a `GB` és a `GiB` között?
5. Mennyi `1 EB` byte-ban?

## Rövid válaszok az önellenőrzéshez

1. `1 000 000 000 byte`
2. `1 000 000 000 000 byte`
3. **Tízes alapú**
4. A `GB` decimális (`10^9`), a `GiB` bináris (`2^30`)
5. `1 000 000 000 000 000 000 byte`

## Források

1. BIPM - SI prefixes  
   https://www.bipm.org/en/measurement-units/si-prefixes  
   Használat: a `giga`, `tera`, `peta`, `exa` SI-prefixek hivatalos értékei.

2. SI Brochure - BIPM  
   https://www.bipm.org/en/publications/si-brochure/  
   Használat: az SI-prefixek hivatalos háttérszabályai.

3. NIST IR 8289 - Quantities and Units for Software Product Measurements  
   https://doi.org/10.6028/NIST.IR.8289  
   Használat: a `byte` és `B` jelölés technikai használata.

4. NIST - Definitions of the SI units: The binary prefixes  
   https://physics.nist.gov/cgi-bin/cuu/Info/Units/binary.html  
   Használat: a decimális és bináris adatméretek tiszta szétválasztása.

Megnyitva: `2026-04-08`
