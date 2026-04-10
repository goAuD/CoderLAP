# ASCII-Tabellen

## Gyors vizuális kép

| Karakter | Decimális kód | Hexa |
|---|---|---|
| `A` | `65` | `41` |
| `a` | `97` | `61` |
| `0` | `48` | `30` |
| szóköz | `32` | `20` |

## Mi az ASCII-tábla szerepe?

Az ASCII-tábla segít megérteni:

- hogyan lesz a karakterből szám
- hogyan tárolja a gép a szöveget
- hogyan működnek bizonyos alacsonyabb szintű átalakítások

Programozásban hasznos lehet például:

- karakterkódok vizsgálatánál
- egyszerű szövegfeldolgozásnál
- protokollok és fájlformátumok értelmezésénél

## Milyen karakterek vannak benne?

### Vezérlőkarakterek

Például:

- soremelés
- tab
- kocsivissza

### Nyomtatható karakterek

Például:

- betűk
- számjegyek
- írásjelek

## ASCII és Unicode: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| ASCII | 7 bites, 128 karakter |
| Unicode | sokkal nagyobb karakterkészlet |

A modern rendszerek többsége ma már Unicode-ot használ, de az ASCII alapjai továbbra is fontosak.

## Miért hasznos még ma is?

- sok technikai dokumentáció erre épít
- a karakterkódok alaplogikáját jól mutatja
- programozásnál gyakran találkozunk ASCII-kompatibilis fogalmakkal

## Vizsgán jól használható megfogalmazás

> Az ASCII-tábla az ASCII karakterkészlet karaktereihez tartozó numerikus kódokat mutatja meg.  
> Az ASCII egy 7 bites karakterkódolás, amely 128 karaktert tartalmaz, köztük vezérlőkaraktereket és nyomtatható jeleket.  
> Bár ma már jellemzően Unicode-alapú rendszereket használunk, az ASCII továbbra is alapvető jelentőségű a karakterkódolás megértésében.

## Gyakori vizsgahibák

- Az ASCII-t Unicode-nak nevezni.
- Azt állítani, hogy minden modern szöveg ASCII.
- Nem megemlíteni a vezérlőkaraktereket.
- A 7 bites alapot elfelejteni.

## Gyors önellenőrzés

1. Hány karaktert fed le az ASCII?
2. Miért hasznos egy ASCII-tábla?
3. Mondj két példát ASCII-kódra.
4. Mi a különbség ASCII és Unicode között?
5. Miért maradt fontos az ASCII ma is?

## Rövid válaszok az önellenőrzéshez

1. `128`-at
2. Mert megmutatja a karakter-kód megfeleltetést
3. `A = 65`, `0 = 48`
4. A Unicode sokkal nagyobb karakterkészlet
5. Mert sok alapfogalom erre épül

## Források

1. MDN - ASCII  
   https://developer.mozilla.org/en-US/docs/Glossary/ASCII  
   Használat: modern, hivatalos összefoglaló az ASCII fogalmához.

2. IETF RFC 20  
   https://www.ietf.org/rfc/rfc20.txt  
   Használat: történeti, elsődleges szabványforrás az ASCII karakterkészlethez.

Megnyitva: `2026-04-09`
