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

## Vizsgán jól használható megfogalmazás

> A fejvezérelt ciklus a feltételt a ciklusmag végrehajtása előtt ellenőrzi, ezért előfordulhat, hogy a ciklus egyszer  
> sem fut le.  
> A lábvezérelt ciklus ezzel szemben a feltételt a ciklusmag után vizsgálja, így legalább egyszer biztosan  
> végrehajtódik.  
> A két típus közötti különbség főként a minimális futásszámban és a feltétel ellenőrzésének helyében van.

## Gyakori vizsgahibák

- A `while` és `do...while` különbségét nem tudni.
- Azt állítani, hogy mindkettő ugyanúgy működik.
- Nem megemlíteni az egyszeri garantált futást.
- Fejvezérelt és lábvezérelt fogalmát felcserélni.

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

1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Használat: hivatalos forrás a `while` és `do...while` működéséhez.

2. MDN - Control flow and error handling  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling  
   Használat: kiegészítő háttér a vezérlési szerkezetek közti különbségek megértéséhez.

Megnyitva: `2026-04-09`
