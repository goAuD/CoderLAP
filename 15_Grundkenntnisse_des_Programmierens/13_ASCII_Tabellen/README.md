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

## Karakterkód és számérték a gyakorlatban

Node.js-ben futtatható példa: a `"7"` egy számjegyből álló szöveg. Megnézzük a
kódját, majd az ASCII-számjegyek folytonos tartományát használva a számértékét.

<!-- example:run -->

```javascript
const digit = "7";
const code = digit.codePointAt(0);
console.log(code);
console.log(code - "0".codePointAt(0));
console.log(String.fromCodePoint(65));
console.log("\n".codePointAt(0));
```

```text
55
7
A
10
```

Az `55` a `7` karakter kódja, a `7` pedig annak számértéke. A kivonás csak
előzőleg ellenőrzött `"0".."9"` karakterre ad értelmes számjegyeredményt.
Általános szövegkonverzióra inkább a nyelv megfelelő átalakító függvényét és
bemenetellenőrzést használjuk.

Az LF (`10`, `0A` hex) és CR (`13`, `0D` hex) külön vezérlőkarakter. A Windows
szövegfájloknál gyakori CRLF két karakterből áll. A `codePointAt` Unicode-kódpontot
ad; a `0..127` tartományban ez megegyezik az ASCII-val. Az `ő` és az emoji már
nem ASCII. Szövegfájl bájtjainak értelmezéséhez az alkalmazott kódolást is tudnunk kell.

## Vizsgán jól használható megfogalmazás

> Az ASCII-tábla az ASCII karakterkészlet karaktereihez tartozó numerikus kódokat mutatja meg.  
> Az ASCII egy 7 bites karakterkódolás, amely 128 karaktert tartalmaz, köztük vezérlőkaraktereket és nyomtatható  
> jeleket.  
> Bár ma már jellemzően Unicode-alapú rendszereket használunk, az ASCII továbbra is alapvető jelentőségű a
> karakterkódolás megértésében.

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

Ellenőrizve: `2026-10-14`.

- [MDN: String.codePointAt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/codePointAt): Unicode-kódpont lekérése.
- [IETF RFC 20](https://www.ietf.org/rfc/rfc20.txt): ASCII kódértékek, LF és CR.


1. MDN - ASCII  
   https://developer.mozilla.org/en-US/docs/Glossary/ASCII  
   Használat: modern, hivatalos összefoglaló az ASCII fogalmához.

2. IETF RFC 20  
   https://www.ietf.org/rfc/rfc20.txt  
   Használat: történeti, elsődleges szabványforrás az ASCII karakterkészlethez.

Megnyitva: `2026-04-09`
