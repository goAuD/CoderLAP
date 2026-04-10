# Einheiten Bit und Byte

## Gyors vizuális kép

| Egység | Jelölés | Mit jelent? | Lehetséges értékek |
|---|---|---|---|
| **bit** | `b` | 1 bináris számjegy | `0` vagy `1` |
| **byte** | `B` | 8 bit együtt | `0-255` |

### Kapcsolatuk

| Kifejezés | Jelentés |
|---|---|
| `1 bit` | egyetlen bináris érték |
| `4 bit` | fél byte, gyakran 1 hexadecimális számjegynek felel meg |
| `8 bit` | `1 byte` |
| `2^8` | `256`, vagyis ennyi különböző értéket tud egy byte tárolni |

## Mi a bit?

A **bit** a `binary digit` rövidítése.  
Ez a számítógépes adatok legalapvetőbb építőeleme.

Egy bit csak két állapotot tud kifejezni:

- `0`
- `1`

Ez használható például:

- igen / nem
- be / ki
- igaz / hamis
- van / nincs

Egyszerű példa:

- egy lámpa **lekapcsolva** = `0`
- egy lámpa **felkapcsolva** = `1`

## Mi a byte?

A **byte** 8 bitből álló egység.

Mivel minden bit kétféle értékű lehet, 8 bit együtt:

`2 × 2 × 2 × 2 × 2 × 2 × 2 × 2 = 2^8 = 256`

Ezért egy byte **256 különböző mintát** tud ábrázolni.

Példák byte-értékekre:

- `00000000` = `0`
- `00000001` = `1`
- `11111111` = `255`

Hexadecimálisan egy byte gyakran így jelenik meg:

- `00`
- `2D`
- `7F`
- `FF`

Egy byte tehát:

- tárolhat egy kis számot
- tárolhat egy karakterkódot
- lehet egy nagyobb adat része

## Miért fontos a bit és a byte?

Mert a digitális világban szinte minden adat ezekből épül fel:

- szöveg
- képek
- hang
- videó
- programkód
- adatbázisok

Ha valaki érti a bit és byte közti különbséget, könnyebben megérti:

- a fájlméreteket
- a memóriahasználatot
- a hálózati sebességet
- a karakterkódolást
- a bináris és hexadecimális ábrázolást

## Hol találkozol velük a gyakorlatban?

### 1. Fájlméret és tárhely

Ezeket általában **byte-ban** mérjük:

- `25 B`
- `4 KB`
- `12 MB`
- `256 GB`

Például:

- egy rövid szövegfájl lehet néhány száz byte
- egy kép lehet több megabyte
- egy SSD lehet több száz gigabyte

### 2. Adatátviteli sebesség

Ezt gyakran **bit per másodpercben** adják meg:

- `Mbps` = megabit per second
- `Gbps` = gigabit per second

Példa:

- `100 Mbps` internetsebesség nem ugyanaz, mint `100 MB/s`

Mivel:

- `1 B = 8 b`

ezért:

- `100 MB/s = 800 Mb/s`

Ez az egyik legfontosabb gyakorlati különbség.

### 3. Karakterek és szöveg

Régebben gyakran igaz volt, hogy egy karakter egy byte körül mozgott, de ma ez **nem mindig igaz**.

Modern kódolásoknál, például `UTF-8` esetén:

- egyes karakterek `1 byte`
- más karakterek `2-4 byte`

Ezért hibás az az állítás, hogy:

> 1 karakter mindig 1 byte.

## `b` és `B`: ne keverd össze

| Jelölés | Jelentés |
|---|---|
| `b` | bit |
| `B` | byte |

Ez nem csak helyesírási részlet, hanem **nyolcszoros különbséget** jelenthet.

Példa:

- `8 b = 1 B`
- `10 MB` = `80 Mb`

Vizsgán ezt nagyon gyakran keverik.

## Gyors példák

| Példa | Jelentés |
|---|---|
| `1 bit` | `0` vagy `1` |
| `1 byte` | 8 bit |
| `1 byte` | 256 lehetséges érték |
| `64-bit` processzor | 64 bites adatokkal dolgozó architektúra |
| `100 Mbps` | hálózati sebesség bitben megadva |
| `20 MB` fájl | fájlméret byte-alapú mértékben |

## Amire figyelni kell

- A **bit** és a **byte** nem ugyanaz.
- A `b` és a `B` felcserélése súlyos hibához vezethet.
- A **byte ma gyakorlatban 8 bit**, de történetileg léteztek eltérő megoldások is.
- Nem minden karakter fér el 1 byte-ban.
- A nagyobb egységek (`KB`, `MB`, `GB`, illetve `KiB`, `MiB`, `GiB`) külön témakörhöz tartoznak.

## Vizsgán jól használható megfogalmazás

> A bit a digitális információ legkisebb egysége, értéke 0 vagy 1 lehet.  
> A byte 8 bitből álló egység, ezért 256 különböző értéket tud ábrázolni.  
> A byte-ot főleg tárhely és fájlméret mérésére használjuk, míg a bit gyakran adatátviteli sebességnél jelenik meg.  
> Fontos különbség, hogy a `b` bitet, a `B` pedig byte-ot jelent.

## Gyakori vizsgahibák

- Azt mondani, hogy a bit és a byte ugyanaz.
- Elfelejteni, hogy `1 byte = 8 bit`.
- Összekeverni a `b` és `B` jelölést.
- Azt állítani, hogy minden karakter mindig 1 byte.
- Összemosni ezt a témát a `KB / MB / GB` és `KiB / MiB / GiB` témákkal.

## Gyors önellenőrzés

1. Mi a bit?
2. Hány bitből áll egy byte?
3. Hány különböző értéket tud felvenni egy byte?
4. Melyiket használjuk gyakrabban fájlmérethez: bit vagy byte?
5. Mit jelent a `b`, és mit jelent a `B`?
6. Miért nem ugyanaz a `100 Mbps` és a `100 MB/s`?

## Rövid válaszok az önellenőrzéshez

1. A bit egy bináris számjegy, amely `0` vagy `1`
2. `8` bitből
3. `256` különböző értéket
4. Általában a **byte**-ot
5. `b` = bit, `B` = byte
6. Mert `1 byte = 8 bit`, ezért a két érték más nagyságrendet jelent

## Források

Az összefoglalóhoz modern, hivatalos vagy technikailag erős elsődleges forrásokat használtam.

1. NIST CSRC Glossary - bit  
   https://csrc.nist.gov/glossary/term/bit  
   Használat: a bit alapdefiníciója mint bináris számjegy (`0` vagy `1`).

2. NIST CSRC Glossary - Byte  
   https://csrc.nist.gov/glossary/term/Byte  
   Használat: a byte alapdefiníciója mint 8 bites egység.

3. NIST IR 8289 - Quantities and Units for Software Product Measurements  
   https://doi.org/10.6028/NIST.IR.8289  
   Használat: `Byte B = 8 bit`, a byte gyakorlati szerepe, valamint a `B` jelölés.

4. NIST IR 8101 - A Rational Foundation for Software Metrology  
   https://nvlpubs.nist.gov/nistpubs/ir/2016/NIST.IR.8101.pdf  
   Használat: a `bit` mint információs egység, `1 B = 8 b`, valamint az adatátviteli sebesség bit/s alapú gyakorlata.

5. MDN Web Docs - Endianness  
   https://developer.mozilla.org/en-US/docs/Glossary/Endianness  
   Használat: egy byte 8 bites értékként való gyakorlati értelmezése (`0x00`-`0xFF`).

6. MDN Web Docs - UTF-8  
   https://developer.mozilla.org/en-US/docs/Glossary/UTF-8  
   Használat: annak tisztázása, hogy modern kódolásokban egy karakter nem feltétlenül 1 byte.

7. BIPM - SI Brochure  
   https://www.bipm.org/en/publications/si-brochure  
   Használat: az SI-jelölések és prefixek modern, hivatalos háttérkörnyezete.

Megnyitva: `2026-04-08`
