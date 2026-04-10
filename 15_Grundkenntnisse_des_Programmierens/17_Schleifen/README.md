# Schleifen

## Gyors vizuális kép

| Ciklustípus | Mikor jó? |
|---|---|
| `for` | ha tudjuk, hány ismétlés kell |
| `while` | ha feltétel alapján ismétlünk |
| `do...while` | ha legalább egyszer mindenképp fusson |
| `for...each` jelleg | elemek bejárására |

## Mi az a ciklus?

A ciklus lényege, hogy:

- nem kell ugyanazt a kódot többször leírni
- a program ismétli a műveletet
- amíg teljesül egy feltétel
- vagy amíg be nem járja az elemeket

## Miért fontos?

- rövidebb és tisztább kódot ad
- könnyebb karbantartani
- hatékonyabb megoldást tesz lehetővé ismétlődő műveleteknél

## Tipikus ciklusok

### `for`

Jó akkor, ha:

- számlálunk
- ismert tartományban dolgozunk
- index alapján haladunk

### `while`

Jó akkor, ha:

- előre nem tudjuk, hány ismétlés kell
- amíg egy feltétel igaz

### `do...while`

Jó akkor, ha:

- a ciklusmag legalább egyszer biztosan fusson

## Mire kell figyelni?

- a kilépési feltétel legyen helyes
- a ciklus ne fusson végtelenül
- a számlálót vagy állapotot megfelelően módosítani kell

## Ciklus és rekurzió: ne keverd össze

| Fogalom | Lényeg |
|---|---|
| ciklus | ismétlés vezérlési szerkezettel |
| rekurzió | ismétlés önhívó függvénnyel |

## Vizsgán jól használható megfogalmazás

> A ciklus olyan vezérlési szerkezet, amely egy utasítást vagy utasításblokkot többször végrehajt.  
> A futást általában feltétel, számláló vagy bejárandó elemsor vezérli.  
> A ciklusok célja a kódismétlés csökkentése és az ismétlődő feladatok hatékony kezelése.

## Gyakori vizsgahibák

- Nem megemlíteni a kilépési feltételt.
- A `while` és `do...while` különbségét kihagyni.
- Azt hinni, hogy a ciklus mindig ismert számú ismétlésből áll.
- Végtelen ciklus veszélyét nem említeni.

## Gyors önellenőrzés

1. Mi a ciklus lényege?
2. Mire jó a `for` ciklus?
3. Mikor jobb a `while`?
4. Miért veszélyes a hibás kilépési feltétel?
5. Mi a különbség ciklus és rekurzió között?

## Rövid válaszok az önellenőrzéshez

1. Ismételt végrehajtás
2. Ismert ismétlésszám vagy számlálás esetén
3. Ha feltétel alapú az ismétlés
4. Mert végtelen ciklushoz vezethet
5. A ciklus vezérlési szerkezet, a rekurzió önhívás

## Források

1. MDN - Loops and iteration  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Loops_and_iteration  
   Használat: hivatalos, modern forrás a ciklusok működéséhez és típusaihoz.

2. MDN - Control flow  
   https://developer.mozilla.org/en-US/docs/Glossary/Control_flow  
   Használat: háttérforrás a vezérlési szerkezetek nagyobb kontextusához.

Megnyitva: `2026-04-09`
