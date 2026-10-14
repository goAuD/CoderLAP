# JSON

## Gyors vizuális kép

| Típus | Példa |
|---|---|
| objektum | `{ "name": "Anna" }` |
| tömb | `[1, 2, 3]` |
| kulcs-érték | `"age": 21` |

## Mi az a JSON?

A JSON egy nyelvfüggetlen adatcsere-formátum,
amely a JavaScript objektumjelöléséből indult,
de ma már sokféle programnyelv használja.

Gyakran alkalmazzák:

- REST API-k válaszaiban
- konfigurációkban
- frontend és backend közötti adatcserében
- fájlalapú adatszerkezetekben

## Alapfelépítés

A JSON két fő szerkezeti eleme:

- objektum
- tömb

Példa:

```json
{
  "id": 42,
  "name": "Anna",
  "active": true,
  "roles": ["user", "editor"]
}
```

## Milyen értéktípusok lehetnek benne?

- string
- number
- object
- array
- boolean
- `null`

## Miért népszerű?

- egyszerű
- jól olvasható
- széles körben támogatott
- könnyen parse-olható
- webes környezetben nagyon praktikus

## JSON és JavaScript objektum: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| JSON | szigorú adatcsere-formátum |
| JavaScript objektum | programnyelvi adatstruktúra |

Fontos különbségek:

- a JSON szöveg
- a kulcsokat idézőjelbe kell tenni
- kommentek nem részei a szabványos JSON-nak

## Mire kell figyelni?

- A szabványos JSON-ban nincs komment.
- A felesleges trailing comma nem megengedett.
- A JSON önmagában csak adat, nem viselkedés.
- Hibás szintaxis esetén a feldolgozás sikertelen lesz.

## JSON és XML: ne keverd össze

| Szempont | JSON | XML |
|---|---|---|
| jelleg | könnyű adatcsere-formátum | jelölőnyelv |
| olvashatóság | gyakran egyszerűbb | sokszor részletesebb |
| tipikus mai webes API | nagyon gyakori | ritkább, de még előfordul |

## Parsing, ellenőrzés és szerializálás

**Feladat:** egy témához `0..5` közötti egész pontszámot olvasunk. A JSON-szintaxis
és az alkalmazás elvárása két külön ellenőrzés. Node.js-ben futtatható:

<!-- example:run -->

```javascript
function parseProgress(text) {
  const value = JSON.parse(text);
  if (value === null || Array.isArray(value) || typeof value !== "object" ||
      typeof value.topic !== "string" || !Number.isInteger(value.score) ||
      value.score < 0 || value.score > 5) {
    throw new Error("Invalid progress");
  }
  return { topic: value.topic, score: value.score };
}
const progress = parseProgress('{"topic":"loops","score":4}');
console.log(progress.topic, progress.score + 1);
console.log(JSON.stringify(progress));
for (const text of ['null', '{"topic":"loops","score":"4"}']) {
  try {
    parseProgress(text);
  } catch (error) {
    console.log(error.message);
  }
}
```

```text
loops 5
{"topic":"loops","score":4}
Invalid progress
Invalid progress
```

A `JSON.parse` szövegből futásidejű értéket készít. A `JSON.stringify` ennek
fordított irányát végzi. A pontszám számként összeadható; a `"4"` viszont sztring,
ezért az itt választott szerződés elutasítja. A `null` teljesen szabályos JSON,
de nem a várt rekord. A feldolgozott adatot használjuk, nem `eval`-lal futtatjuk.

A JSON legfelső értéke nem csak objektum vagy tömb lehet, hanem például szám,
logikai érték vagy `null` is. Az objektumkulcsok és szövegértékek dupla
idézőjelet használnak. `undefined`, függvény és `BigInt` nem JSON-értéktípus;
egy dátum átvitelének formátumáról külön megállapodunk, gyakran ISO-formátumú
sztringet használva.

A számokat a fogadó nyelv saját számábrázolása korlátozhatja. Nagy, pontos
azonosítót ezért gyakran sztringként adunk át. Azonos objektumon belül egyedi
kulcsneveket használjunk, mert az ismétlődő nevek kezelése rendszerenként eltérhet.

## Vizsgán jól használható megfogalmazás

> A JSON egy könnyű, szöveges adatcsere-formátum, amely kulcs-érték párok és tömbök segítségével írja le az adatokat.  
> Gyakran használják webes API-kban, mert egyszerű, jól olvasható és sok programnyelv könnyen feldolgozza.  
> A szabványos JSON-ban például a kulcsokat idézőjelbe kell tenni, és kommentek nem használhatók.

## Gyors önellenőrzés

1. Mire használjuk gyakran a JSON-t?
2. Mi a két alapvető szerkezeti eleme?
3. Mi a különbség JSON és JavaScript objektum között?
4. Lehet-e komment a szabványos JSON-ban?
5. Miért népszerű a weben?

## Rövid válaszok az önellenőrzéshez

1. Adatcserére
2. Objektum és tömb
3. A JSON szövegformátum, az objektum futásidejű adatstruktúra
4. Nem
5. Mert egyszerű és széles körben támogatott

## Források

Ellenőrizve: `2026-10-14`.

- [IETF: JSON RFC8259](https://www.rfc-editor.org/rfc/rfc8259): értéktípusok, egyedi kulcsok és interoperabilitás.
- [MDN: JSON.parse](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse): szövegből futásidejű érték.


1. RFC 8259 - The JavaScript Object Notation (JSON) Data Interchange Format  
   https://www.rfc-editor.org/rfc/rfc8259  
   Használat: a JSON hivatalos, szabványos leírása.

2. MDN - JSON  
   https://developer.mozilla.org/en-US/docs/Glossary/JSON  
   Használat: rövid, fejlesztőbarát definíció és kontextus.

3. ECMA-404 - The JSON Data Interchange Syntax  
   https://ecma-international.org/publications-and-standards/standards/ecma-404/  
   Használat: szabványos háttér a JSON szintaxisához.

Megnyitva: `2026-04-08`
