# Logikschaltungen und Wahrheitstabellen

## Gyors vizuális kép

### NOT

| A   | NOT A |
| --- | ----- |
| 0   | 1     |
| 1   | 0     |

### AND röviden

| A   | B   | A AND B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 0       |
| 1   | 0   | 0       |
| 1   | 1   | 1       |

### OR röviden

| A   | B   | A OR B |
| --- | --- | ------ |
| 0   | 0   | 0      |
| 0   | 1   | 1      |
| 1   | 0   | 1      |
| 1   | 1   | 1      |

### XOR röviden

| A   | B   | A XOR B |
| --- | --- | ------- |
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 0       |

## Mi az a logikai kapcsolás?

Olyan digitális áramköri elem vagy logikai művelet, amely bináris bemenetekből bináris kimenetet állít elő.

Egyszerűen:

- bemenet: `0` vagy `1`
- szabály: logikai művelet
- kimenet: `0` vagy `1`

## Mi az az igazságtábla?

Az igazságtábla felsorolja az összes lehetséges bemeneti kombinációt, és minden sorhoz megadja a kimenetet.

Két bemenet esetén összesen:

- `4` kombináció van

mert:

- `00`
- `01`
- `10`
- `11`

Egy bemenet esetén:

- `2` kombináció van

## 1. NOT

A **NOT** egy bemenetű logikai művelet.

Feladata:

- megfordítani a bemenetet

Szabály:

- `0` → `1`
- `1` → `0`

Jelentése:

- tagadás
- invertálás

Egyszerű példa:

- rendszer engedélyezve = `1`
- NOT után tiltva = `0`

## 2. AND

Az **AND** azt jelenti:

- csak akkor lesz `1`, ha **mindkét** bemenet `1`

Kulcsszó:

- **és**

Gyakorlati gondolat:

- két feltételnek egyszerre kell teljesülnie

Példa:

- felhasználó be van jelentkezve = `1`
- van jogosultsága = `1`
- hozzáférés = `1`

Ha bármelyik hiányzik:

- a kimenet `0`

## 3. OR

Az **OR** azt jelenti:

- akkor lesz `1`, ha **legalább az egyik** bemenet `1`

Kulcsszó:

- **vagy**

Példa:

- riasztás indul, ha az ajtó nyitva van **vagy** az ablak nyitva van

Csak akkor `0`, ha mindkét bemenet `0`.

## 4. XOR

Az **XOR** jelentése:

- kizáró vagy

Szabály:

- akkor `1`, ha a két bemenet **különbözik**
- akkor `0`, ha a két bemenet **azonos**

Tehát:

- `0, 1` → `1`
- `1, 0` → `1`
- `0, 0` → `0`
- `1, 1` → `0`

Az XOR nagyon fontos például:

- paritásvizsgálatnál
- egyszerű összeadó áramköröknél
- bizonyos titkosítási műveleteknél

## Hogyan lehet gyorsan megjegyezni?

### AND

- mindkettő igaz kell

### OR

- legalább egy igaz kell

### XOR

- pontosan az egyik igaz
- vagy úgy is: a két bemenet különbözik

### NOT röviden

- megfordítja az értéket

## Jelölések

Néha a következő alakokkal is találkozhatsz:

| Művelet | Szavas alak | Gyakoribb rövid alak |
| ------- | ----------- | -------------------- |
| NOT     | tagadás     | `NOT A`              |
| AND     | és          | `A AND B`            |
| OR      | vagy        | `A OR B`             |
| XOR     | kizáró vagy | `A XOR B`            |

Matematikai vagy programozási környezetben lehetnek más jelek is, de vizsgán a szöveges értelmezés a legfontosabb.

## Mire használják ezeket?

- digitális áramkörökben
- vezérlési feltételekben
- programozásban logikai döntéseknél
- bitműveleteknél
- hibavizsgálatban

## Összetett feltétel levezetése

Egy művelet akkor engedélyezett, ha a felhasználó bejelentkezett (`A`),
van szerkesztési joga (`B`), és a dokumentum nincs zárolva (`C` jelenti a zárolást).
A szabály: `A AND B AND NOT C`. Három független logikai bemenethez `2³ = 8` sor kell.

| A | B | C | A AND B AND NOT C |
| - | - | - | ---------------- |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

Az önálló JavaScriptben valódi logikai értékeket használunk:

<!-- example:run -->
```javascript
const signedIn = true;
const canEdit = true;
const locked = false;
console.log(signedIn && canEdit && !locked);
console.log(!(signedIn && canEdit) === (!signedIn || !canEdit));
console.log(true !== false);
```

Várt kimenet:

```text
true
true
true
```

A második sor De Morgan azonosságát szemlélteti: `NOT (A AND B)` ugyanaz,
mint `(NOT A) OR (NOT B)`. A harmadik sor két boolean eltérésével fejez ki XOR-t.
JavaScriptben a `^` bitenkénti művelet, ezért logikai feltételekhez itt nem azt használjuk.
Az `&&` és `||` rövidzáras: a jobb oldalt csak akkor értékelik ki, ha az eredményhez kell.
Egy kapcsolási rajz bemenetei ezzel szemben nem programutasítások végrehajtási sorrendjét jelentik.

A kliensoldali feltétel csak a felület viselkedését szemlélteti. Valós rendszerben
a szervernek a jogosultságot a művelet végrehajtásakor is ellenőriznie kell.

Forrás: [MDN: kifejezések és operátorok](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators).

## Vizsgán jól használható megfogalmazás

> A logikai kapcsolások bináris bemenetekkel dolgoznak, tehát a jelek 0 vagy 1 értékűek.  
> Az igazságtábla megmutatja, hogy az összes lehetséges bemeneti kombinációhoz milyen kimenet tartozik.  
> Az AND csak akkor ad 1-et, ha mindkét bemenet 1.  
> Az OR akkor ad 1-et, ha legalább az egyik bemenet 1.  
> Az XOR akkor ad 1-et, ha a két bemenet különbözik.  
> A NOT egy bemenetet invertál.

## Gyors önellenőrzés

1. Mikor ad az AND `1` kimenetet?
2. Mikor ad az OR `0` kimenetet?
3. Mikor ad az XOR `1` kimenetet?
4. Mit csinál a NOT?
5. Hány soros egy kétbemenetű igazságtábla?

## Rövid válaszok az önellenőrzéshez

1. Csak akkor, ha mindkét bemenet `1`
2. Csak akkor, ha mindkét bemenet `0`
3. Akkor, ha a két bemenet különbözik
4. Megfordítja a bemenetet
5. `4` soros

## Források

1. Analog Devices - Logic Gate  
   https://www.analog.com/en/resources/glossary/logic-gate.html  
   Használat: logikai kapuk definíciói és az AND, OR, XOR, NOT igazságtáblái.

2. Analog Devices - XOR Gate  
   https://www.analog.com/en/resources/glossary/xor-gate.html  
   Használat: az XOR pontos működése és tipikus gyakorlati felhasználása.

3. Texas Instruments Education - Using Boolean Logic on the TI-83 Plus and TI-84 Plus Family  
   https://education.ti.com/en/customer-support/knowledge-base/ti-83-84-plus-family/product-usage/34774  
   Használat: Boolean műveletek (`and`, `or`, `xor`, `not`) gyakorlati, ellenőrizhető leírása.

Megnyitva: `2026-04-08`
