# Kopf- und fussgesteuerte Schleifen

## Gyors vizuális kép

| Típus | Feltétel helye | Minimum futás |
|---|---|---|
| fejvezérelt | a ciklus elején | `0` |
| lábvezérelt | a ciklus végén | `1` |

## Mi az a fejvezérelt ciklus?

Ilyenkor a program:

- előbb ellenőrzi a feltételt
- és csak utána hajtja végre a ciklusmagot

Tipikus példa:

- `while`

## Mi az a lábvezérelt ciklus?

Ilyenkor a program:

- előbb végrehajtja a ciklusmagot
- csak utána ellenőrzi a feltételt

Tipikus példa:

- `do...while`

## Miért fontos ez a különbség?

Mert nem ugyanaz történik akkor, ha a feltétel rögtön hamis.

### Fejvezérelt ciklusnál

- akár egyszer sem fut

### Lábvezérelt ciklusnál

- a ciklusmag legalább egyszer biztosan lefut

## Egyszerű példa

Feladat: kérjünk be adatot, amíg nem jó.

Ha legalább egy bekérés biztosan kell, sokszor a lábvezérelt logika természetesebb.

## Ellenőrzés az első feldolgozás után

Az adatbekérést itt előre megadott, **nem üres**, véges egész számokat tartalmazó
tömb helyettesíti. Addig olvasunk, amíg legalább 1-et kapunk vagy elfogy a lista.
Így nincs interaktív várakozás; a példa Node.js-ben ismételhetően fut.

<!-- example:run -->

```javascript
function readAtLeastOnce(inputs) {
  let position = 0;
  let value;
  do {
    value = inputs[position];
    position += 1;
  } while (value < 1 && position < inputs.length);
  return { value, attempts: position };
}
console.log(JSON.stringify(readAtLeastOnce([0, -2, 4])));
console.log(JSON.stringify(readAtLeastOnce([7])));
```

```text
{"value":4,"attempts":3}
{"value":7,"attempts":1}
```

Az első sorban a `0` és `-2` után még van adat, a `4` elfogadható, ezért három
olvasás történik. A `[7]` esetén egy. Ha minden érték 1 alatti, az utolsó érték
után a lista végét jelző feltétel állítja le a ciklust; a hívó ekkor továbbra is
ellenőrzi, hogy az eredmény elfogadható-e. Üres lista feldolgozásához előbb külön
ürességvizsgálat vagy fejvezérelt bejárás szükséges.

A `do...while` feltétele **folytatási feltétel**: igaz esetén ismétlünk.
Egyes pseudocode-jelölések `repeat ... until` alakja ezzel szemben igaz esetén
áll le. Fordításkor ezért a feltétel jelentését, nem csak a ciklus helyét követjük.

## Vizsgán jól használható megfogalmazás

> A fejvezérelt ciklus a feltételt a ciklusmag végrehajtása előtt ellenőrzi, ezért előfordulhat, hogy a ciklus egyszer  
> sem fut le.  
> A lábvezérelt ciklus ezzel szemben a feltételt a ciklusmag után vizsgálja, így legalább egyszer biztosan  
> végrehajtódik.  
> A két típus közötti különbség főként a minimális futásszámban és a feltétel ellenőrzésének helyében van.

## Gyors önellenőrzés

1. Mi az a fejvezérelt ciklus?
2. Mi az a lábvezérelt ciklus?
3. Melyik futhat le nullaszor?
4. Melyik fut le legalább egyszer?
5. Miért fontos ez a különbség?

## Rövid válaszok az önellenőrzéshez

1. Amelyik a feltételt elöl ellenőrzi
2. Amelyik a feltételt hátul ellenőrzi
3. A fejvezérelt
4. A lábvezérelt
5. Mert más viselkedést ad a kezdő feltételtől függően

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: do...while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while): folytatási feltétel és első végrehajtás.


1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Használat: hivatalos forrás a `while` és `do...while` működéséhez.

2. MDN - Control flow and error handling  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling  
   Használat: kiegészítő háttér a vezérlési szerkezetek közti különbségek megértéséhez.

Megnyitva: `2026-04-09`
