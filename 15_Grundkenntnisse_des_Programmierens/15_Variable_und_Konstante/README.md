# Variable und Konstante

## Gyors vizuális kép

| Fogalom | Jellemző |
|---|---|
| változó | új értéket kaphat |
| konstans | fix kötés vagy fix érték célja |

## Mi az a változó?

A változó:

- értéket tárol vagy jelöl
- neve van
- a program futása közben megváltozhat

Példa:

```text
pontszam = 10
pontszam = pontszam + 5
```

## Mi az a konstans?

A konstans olyan névvel ellátott elem, amelynek értékét vagy kötését nem akarjuk megváltoztatni.

Ez lehet:

- valóban állandó érték
- vagy nyelvtől függően olyan kötés, amely nem rendelhető át

## Miért hasznos konstansokat használni?

- egyértelműbb szándékot mutat
- csökkenti a véletlen átírás esélyét
- olvashatóbbá teszi a kódot
- karbantartáskor könnyebb egy helyen módosítani a fix értékeket

## Fontos modern pontosítás

Sok nyelvben a `const` vagy hasonló megoldás:

- nem feltétlenül teszi teljesen megváltoztathatatlanná az egész objektumot
- inkább a kötést vagy újraértékadást korlátozza

Ez vizsgán plusz pontot érhet, ha jól fogalmazod meg.

## Változó és konstans: ne keverd össze

| Szempont | Változó | Konstans |
|---|---|---|
| újraértékadás | igen | általában nem |
| szerep | futás közben változó adatok | fix értékek vagy rögzített kötés |
| olvashatóság | általános | szándékot tisztáz |

## Kötés és objektumállapot külön követhető

Feladat: egy próbálkozást számolunk, és egy teljesített témát írunk egy profilba.
A Node.js-példában a `let` új értéket enged, a `const` a név kötését rögzíti.

<!-- example:run -->

```javascript
let attempts = 0;
attempts += 1;
const profile = { name: "Ada", completed: 0 };
profile.completed += 1;
console.log(attempts, profile.completed);
const settings = Object.freeze({ maxAttempts: 3 });
console.log(settings.maxAttempts, Object.isFrozen(settings));
```

```text
1 1
3 true
```

A `profile` továbbra is ugyanarra az objektumra mutat, miközben annak
`completed` tulajdonsága változik. A `const` tehát itt nem teszi változtathatatlanná
az objektumot. Új objektum hozzárendelése ugyanahhoz a `profile` kötéshez viszont
nem megengedett. Ha két változó ugyanarra az objektumra hivatkozik, mindkettőből
látható a tulajdonság módosítása.

Az `Object.freeze` a megadott objektum saját tulajdonságait fagyasztja be.
Ez **sekély** művelet: a benne hivatkozott további objektumokat külön kell kezelni.
A forráskódban lévő konstans sem titkos: a böngészőbe kiküldött API-kulcsot
semmilyen `const` deklaráció nem védi meg a látogatótól.

## Vizsgán jól használható megfogalmazás

> A változó olyan programozási elem, amelynek értéke a program futása során megváltozhat.  
> A konstans ezzel szemben olyan elem, amelynek értékét vagy kötését nem kívánjuk módosítani.  
> A konstansok használata növeli a kód olvashatóságát és csökkenti a véletlen hibák kockázatát, bár a pontos viselkedés
> nyelvenként eltérhet.

## Gyors önellenőrzés

1. Mi a változó?
2. Mi a konstans?
3. Miért jó konstansokat használni?
4. Miért kell óvatosan fogalmazni a “nem változik meg” állítással?
5. Milyen esetben használunk jellemzően konstansokat?

## Rövid válaszok az önellenőrzéshez

1. Futás közben változható értékű elem
2. Fixnek szánt érték vagy kötés
3. Mert tisztább és biztonságosabb kódot ad
4. Mert a pontos szabály nyelvenként eltér
5. Fix konfigurációs vagy állandó értékekhez

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze): sekély változtathatatlanság.


1. MDN - const  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const  
   Használat: hivatalos, modern forrás a konstans kötés pontos értelmezéséhez.

2. MDN - Grammar and types  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types  
   Használat: háttérforrás a változók és értékek alapfogalmaihoz.

Megnyitva: `2026-04-09`
