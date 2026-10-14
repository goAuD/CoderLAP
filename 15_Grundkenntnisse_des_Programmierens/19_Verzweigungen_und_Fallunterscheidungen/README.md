# Verzweigungen und Fallunterscheidungen

## Gyors vizuális kép

```text
feltétel?
    igen -> egyik ág
    nem  -> másik ág
```

## Mi az a vezérlési elágazás?

Az elágazás lényege:

- a program nem mindig ugyanazt csinálja
- egy feltétel alapján választ
- különböző utasítások hajtódhatnak végre

## Tipikus formák

### `if`

Egy feltétel esetén fut valami.

### `if / else`

Két lehetséges ág van.

### `else if` lánc

Több feltétel egymás után ellenőrizhető.

### `switch / case`

Több konkrét eset közül választunk.

## Mikor jó a `switch`?

- ha ugyanazt az értéket több lehetséges esettel hasonlítjuk össze
- ha az elágazásokat átláthatóbban akarjuk látni

## Mire kell figyelni?

- a feltételek legyenek egyértelműek
- a sorrend számíthat
- legyen kezelve az alapértelmezett vagy “egyik sem” eset is

## Elágazás és ciklus: ne keverd össze

| Fogalom | Mire való? |
|---|---|
| elágazás | döntés |
| ciklus | ismétlés |

## Tartományok és konkrét állapotok

Egy saját gyakorlófeladatban 50 ponttól teljesített, 80-tól erős eredményt
jelzünk. Ez szemléltető pontozás, nem hivatalos LAP-osztályozás. A második
függvény konkrét szöveges állapotból választ műveletet. Mindkettő Node.js-ben fut.

<!-- example:run -->

```javascript
function result(points) {
  if (!Number.isInteger(points) || points < 0 || points > 100) return "invalid";
  if (points >= 80) return "strong";
  if (points >= 50) return "passed";
  return "practice";
}
for (const points of [49, 50, 79, 80, 101]) {
  console.log(points, result(points));
}
function action(status) {
  switch (status) {
    case "draft": return "edit";
    case "ready": return "start";
    default: return "review";
  }
}
console.log(action("ready"), action("unknown"));
```

```text
49 practice
50 passed
79 passed
80 strong
101 invalid
start review
```

Az `if`-ek sorrendje szándékos: előbb a megengedett tartományt, majd a magasabb
küszöböt ellenőrizzük. A `return` után a későbbi feltételek már nem futnak.
Az 50 és 80 körüli esetek megmutatják a határok befoglalását.

A JavaScript `switch` szigorú egyenlőséggel keresi az esetet. Itt minden ág
visszatér, ezért nem kell `break`. Ha az ág tovább futna, `break`-kel zárnánk le,
különben a következő ág utasításai is végrehajtódhatnának. A `default` a fel nem
sorolt állapotokhoz ad meghatározott választ.

## Vizsgán jól használható megfogalmazás

> Az elágazások és esetválasztások segítségével a program különböző végrehajtási ágak közül választhat feltételek  
> alapján.  
> A leggyakoribb megoldás az `if / else`, több konkrét eset kezelésére pedig gyakran használunk `switch / case`  
> szerkezetet.  
> Ezek a vezérlési szerkezetek a döntési logika megvalósítására szolgálnak.

## Gyors önellenőrzés

1. Mire való az elágazás?
2. Mikor használunk `if / else` szerkezetet?
3. Mikor lehet átláthatóbb a `switch / case`?
4. Miért fontos az alapértelmezett ág?
5. Mi a különbség elágazás és ciklus között?

## Rövid válaszok az önellenőrzéshez

1. Döntési helyzetek kezelésére
2. Ha feltétel alapján két vagy több út közül választunk
3. Ha több konkrét esetet vizsgálunk
4. Mert kezelni kell a nem várt eseteket is
5. Az egyik dönt, a másik ismétel

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch): szigorú egyenlőség, visszatérés és fall-through.


1. MDN - Control flow and error handling  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling  
   Használat: hivatalos, részletes forrás az `if`, `else`, `switch` és egyéb elágazások működéséhez.

2. MDN - Control flow  
   https://developer.mozilla.org/en-US/docs/Glossary/Control_flow  
   Használat: kiegészítő forrás a döntési szerkezetek általános szerepéhez.

Megnyitva: `2026-04-09`
