# Zeichencodierung

## Gyors vizuális kép

| Szint | Mit jelent? |
|---|---|
| karakter | ember által olvasott jel, pl. `A`, `é`, `€` |
| kódpont | absztrakt azonosító, pl. Unicode `U+00E9` |
| kódolás | hogyan tároljuk bájtokban, pl. `UTF-8` |

## Mi az a karakterkódolás?

A karakterkódolás egy megfeleltetés a **szöveg** és a **bájtok** között.

Ha ugyanazt a bájtsorozatot más kódolással olvassuk, a szöveg hibás lehet.

Ezért fontos, hogy:

- a fájl valóban abban a kódolásban legyen mentve
- a rendszer ezt helyesen ismerje fel
- a weboldal ezt egyértelműen jelezze

## Miért fontos a weben?

Mert a hibás kódolás eredménye:

- olvashatatlan karakterek
- "krikszkraksz"
- hibás adatfeldolgozás
- keresési, megjelenítési vagy exportálási probléma

HTML-ben gyakori megadás:

```html
<meta charset="utf-8" />
```

## Mit jelent a `UTF-8`?

A `UTF-8` a Unicode egyik karakterkódolási formája.

Előnyei:

- a világ legtöbb írásrendszere kezelhető vele
- weben szabványos és ajánlott
- kompatibilis az ASCII első 128 karakterével

## Mit kell megkülönböztetni?

| Fogalom | Jelentés |
|---|---|
| karakterkészlet | milyen karakterek léteznek |
| kódpont | a karakter absztrakt azonosítója |
| karakterkódolás | hogyan tároljuk a karaktert bájtokban |

Példa:

- a `é` karakter egy jel
- Unicode-ban van hozzá kódpont
- `UTF-8` megmondja, milyen bájtsorozat reprezentálja

## Miért nem elég "csak szöveget menteni"?

Mert a számítógépnek tudnia kell:

- milyen kódolás szerint mentetted
- hogyan kell visszaolvasni

Ha a mentés és a beolvasás nem ugyanazzal a kódolással történik, hibás eredmény lesz.

## Ne keverd össze

| Fogalom | Mit nem jelent? |
|---|---|
| Unicode | nem ugyanaz, mint a konkrét bájtkódolás |
| UTF-8 | nem minden szövegkódolás neve |
| ASCII | nem alkalmas minden nyelvre |

## Mire kell figyelni?

- Új webes projektnél `UTF-8` az alapértelmezett jó választás.
- A fájlt és a deklarációt ugyanarra a kódolásra kell beállítani.
- Régi rendszereknél keveredhetnek a legacy kódolások.
- Adatcsere és import/export során különösen fontos a helyes kódolás.

## Karakter, kódegység és bájt: háromféle hossz

**Feladat:** kódoljuk az `Aő🙂` szöveget UTF-8 bájtokra, majd olvassuk vissza.
A példa mai Node.js-ben és böngészőkonzolban is fut:

<!-- example:run -->

```javascript
const text = "Aő🙂";
const bytes = new TextEncoder().encode(text);
console.log(text.length, [...text].length, bytes.length);
console.log([...bytes].map((byte) => byte.toString(16).padStart(2, "0")).join(" "));
console.log(new TextDecoder("utf-8", { fatal: true }).decode(bytes));
console.log("é" === "é");
console.log("é" === "é".normalize("NFC"));
```

```text
4 3 7
41 c5 91 f0 9f 99 82
Aő🙂
false
true
```

A szöveg három Unicode-kódpontból áll. A JavaScript `length` viszont UTF-16
kódegységeket számol: az emoji kettőt használ, ezért az eredmény `4`.
UTF-8-ban `A` egy bájt, `ő` kettő, az emoji négy, összesen `7`.
A `TextEncoder` UTF-8-at készít, a dekóder ebből visszaállítja a szöveget.
A `fatal: true` hibás bemeneti bájtok esetén kivételt kér helyettesítő jel helyett.

Az `é` egyetlen kódpontként és `e` plusz kombináló ékezettel is leírható.
Az utolsó két sor azt mutatja, hogy a nyers sztringek különbözhetnek, miközben
NFC-normalizálás után egyeznek. A felhasználó által látott jelek száma még
a kódpontok számától is eltérhet, például összetett emojinál.

A font ettől külön kérdés: helyes bájtok mellett is megjelenhet hiányzó jel,
ha a betűkészlet nem tartalmazza. Ilyenkor nem karakterkódolás-cserével javítunk.

## Vizsgán jól használható megfogalmazás

> A karakterkódolás azt határozza meg, hogyan reprezentáljuk a szöveg karaktereit bájtok formájában.  
> A weben a modern és ajánlott megoldás a UTF-8,
> mert sok nyelv karaktereit képes egységesen kezelni,
> és elkerülhető vele a hibás karaktermegjelenítés.  
> A hibás kódolás tipikus következménye a torz vagy olvashatatlan szöveg.

## Gyors önellenőrzés

1. Mi a karakterkódolás lényege?
2. Miért fontos a `UTF-8`?
3. Mi történik hibás kódolás esetén?
4. Mi a különbség a Unicode és a UTF-8 között?
5. Hogyan adjuk meg HTML-ben a javasolt kódolást?

## Rövid válaszok az önellenőrzéshez

1. A szöveg és bájtok közötti megfeleltetés
2. Mert modern, egységes és soknyelvű
3. Hibás karaktermegjelenítés
4. A Unicode absztrakt rendszer, a UTF-8 konkrét kódolás
5. `<meta charset="utf-8" />`

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: TextEncoder](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder): UTF-8 bájtok előállítása.
- [WHATWG: Encoding](https://encoding.spec.whatwg.org/): dekódolás és hibakezelés.
- [MDN: String.normalize](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize): Unicode-normalizálás.


1. MDN - Character encoding  
   https://developer.mozilla.org/en-US/docs/Glossary/Character_encoding  
   Használat: rövid, pontos definíció a karakterkódolás fogalmára.

2. WHATWG - Encoding Standard  
   https://encoding.spec.whatwg.org/  
   Használat: a webes karakterkódolások hivatalos, aktuális szabványa.

3. W3C International - Choosing & applying a character encoding  
   https://www.w3.org/International/questions/qa-choosing-encodings.en  
   Használat: gyakorlati, hivatalos útmutató a helyes kódolásválasztáshoz, különösen `UTF-8` esetén.

Megnyitva: `2026-04-08`
