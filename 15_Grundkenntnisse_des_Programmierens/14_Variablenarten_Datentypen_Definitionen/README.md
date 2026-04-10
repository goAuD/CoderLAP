# Variablenarten, Datentypen, Definitionen

## Gyors vizuális kép

| Fogalom | Jelentés |
|---|---|
| változó | névvel elérhető adat |
| adattípus | szám, szöveg, logikai érték stb. |
| deklaráció | megmondjuk, hogy létezik |
| inicializálás | kezdőértéket adunk |

## Mi az a változó?

A változó olyan programozási elem, amely:

- egy értékre utal
- neve van
- a program futása során felhasználható

Nyelvtől függően a változó:

- közvetlenül értéket tárolhat
- vagy hivatkozhat egy objektumra / memóriaterületre

## Mi az adattípus?

Az adattípus meghatározza:

- milyen jellegű adatot tárolunk
- milyen műveletek végezhetők rajta
- mennyire kell rá vigyázni formailag

## Tipikus adattípusok

| Típus | Példa |
|---|---|
| egész szám | `42` |
| lebegőpontos szám | `3.14` |
| logikai | `true`, `false` |
| karakter / szöveg | `'A'`, `"hello"` |
| összetett típus | lista, tömb, objektum |

## Változótípusok röviden

Ezt többféleképp értelmezhetjük:

- egyszerű és összetett adattípusok
- lokális és globális változók
- módosítható és nem módosítható kötések

Mivel a konkrét részletek nyelvenként eltérnek, vizsgán a fogalmi magot érdemes biztosan tudni.

## Deklaráció, definíció, inicializálás

Ez fontos vizsgás különbségtétel.

| Fogalom | Egyszerű jelentés |
|---|---|
| deklaráció | megadjuk a változó nevét / létét |
| definíció | tényleges létrehozás vagy hozzárendelés |
| inicializálás | kezdőérték adása |

Megjegyzés:

- ezek pontos nyelvi jelentése eltérhet `C`, `JavaScript`, `Python` vagy más nyelvek között
- vizsgán az alapgondolat a fontos

## Miért fontos az adattípus?

- segít elkerülni hibákat
- meghatározza a műveleteket
- befolyásolhatja a memóriahasználatot és a működést

## Vizsgán jól használható megfogalmazás

> A változó egy névvel ellátott programozási elem, amely egy értéket vagy arra mutató hivatkozást jelöl.  
> Az adattípus meghatározza, hogy milyen jellegű adatot kezelünk, és milyen műveletek végezhetők rajta.  
> A programozásban fontos megkülönböztetni a deklarációt, a definíciót és az inicializálást, még akkor is, ha ezek pontos jelentése nyelvenként eltérhet.

## Gyakori vizsgahibák

- A változót az adattípussal összekeverni.
- Azt állítani, hogy minden nyelvben ugyanaz a deklaráció jelentése.
- Nem tudni példát mondani alap adattípusokra.
- Az inicializálást kihagyni.

## Gyors önellenőrzés

1. Mi a változó?
2. Mi az adattípus?
3. Mondj négy alap adattípust.
4. Mi az inicializálás?
5. Miért térhet el a pontos terminológia nyelvenként?

## Rövid válaszok az önellenőrzéshez

1. Névvel elérhető adat vagy hivatkozás
2. Az adat fajtájának leírása
3. Egész, lebegőpontos, logikai, szöveg
4. Kezdőérték adása
5. Mert a nyelvek eltérően definiálják

## Források

1. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Használat: hivatalos, modern forrás adattípusokhoz és változóalapokhoz.

2. MDN - Statements and declarations  
   https://developer.mozilla.org/docs/Web/JavaScript/Reference/Statements  
   Használat: jól használható háttér a deklaráció és nyelvi szerkezetek megértéséhez.

Megnyitva: `2026-04-09`
