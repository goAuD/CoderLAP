# Pseudocode

## Gyors vizuális kép

| Tulajdonság | Pseudocode |
|---|---|
| futtatható? | nem |
| olvasható? | igen, ez a cél |
| nyelvfüggő? | nem feltétlenül |
| mire jó? | algoritmus tervezése és bemutatása |

## Mi az a pseudocode?

A pseudocode olyan leírás, amely:

- hasonlít a programkódra
- de nem kötődik szigorúan egy adott nyelv szintaxisához
- inkább a logikát emeli ki

Példa:

```text
BEOLVAS n
osszeg = 0
Ciklus i = 1-től n-ig
  osszeg = osszeg + i
KIÍR osszeg
```

## Miért hasznos?

- könnyű vele algoritmust megtervezni
- egyszerűbb megbeszélni egy megoldást
- nem akadunk el a nyelvi részletekben
- vizsgán jól használható gondolkodási eszköz

## Pseudocode és valódi kód: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| pseudocode | logikai leírás |
| programkód | konkrét, szintaktikailag helyes megvalósítás |

## Jó pseudocode jellemzői

- világos
- rövid
- logikus
- követhető
- nem túl technológiafüggő

## Mire kell figyelni?

- ne legyen túl homályos
- ne keverd össze konkrét nyelvi részletekkel, ha nem szükséges
- a lépések sorrendje legyen egyértelmű

## Pseudocode-ból ellenőrizhető megoldás

Feladat: véges számokat tartalmazó listából a legnagyobbat kérjük. Üres lista
esetén az eredmény „nincs érték”. Először a nyelvfüggetlen leírás:

```text
HA a lista üres: VISSZA nincs érték
legnagyobb = az első elem
MINDEN további elemre:
  HA az elem nagyobb, mint legnagyobb:
    legnagyobb = elem
VISSZA legnagyobb
```

Ugyanez önállóan futtatható JavaScriptben:

<!-- example:run -->

```javascript
function maximum(values) {
  if (values.length === 0) return null;
  let largest = values[0];
  for (let i = 1; i < values.length; i++) {
    if (values[i] > largest) largest = values[i];
  }
  return largest;
}
console.log(maximum([-5, -2, -7]));
console.log(maximum([]));
```

```text
-2
null
```

A kezdőérték `-5`, a második elemnél `-2` lesz, a harmadik nem változtatja meg.
Az első tényleges elemmel való kezdés negatív számok esetén is helyes. A `null`
itt a „nincs eredmény” megállapodás, nem a nulla szám. Az átültetésnél tudatos
döntés az indexelés (`0`-tól), a visszatérés jelölése és az üres eset kezelése.
Pseudocode-hoz nincs egyetlen kötelező szintaxis, ezért a jelöléseinket következetesen
használjuk, és az elágazás végét behúzással vagy záró szóval tesszük egyértelművé.

## Vizsgán jól használható megfogalmazás

> A pseudocode egy kódhoz hasonló, de nem futtatható leírás, amely egy algoritmus vagy programrész logikáját mutatja  
> be.  
> Célja, hogy nyelvfüggetlenül és jól olvashatóan lehessen megtervezni vagy elmagyarázni egy megoldást.  
> A pseudocode különösen hasznos algoritmusok bemutatásánál és vizsgafeladatoknál.

## Gyors önellenőrzés

1. Mi a pseudocode lényege?
2. Miért nyelvfüggetlen?
3. Mire használjuk?
4. Mi a különbség közte és a valódi kód között?
5. Milyen egy jó pseudocode?

## Rövid válaszok az önellenőrzéshez

1. Algoritmus logikai leírása
2. Mert nem egy konkrét nyelv szabályaihoz kötött
3. Tervezésre és magyarázatra
4. A pseudocode nem futtatható
5. Világos és követhető

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Pseudocode](https://developer.mozilla.org/en-US/docs/Glossary/Pseudocode): nyelvfüggetlen leírás és jelölések.


1. MDN - Pseudocode  
   https://developer.mozilla.org/en-US/docs/Glossary/Pseudocode  
   Használat: korszerű, hivatalos fogalmi meghatározás a pseudocode szerepéhez.

2. MDN - Algorithm  
   https://developer.mozilla.org/en-US/docs/Glossary/Algorithm  
   Használat: kiegészítő háttér az algoritmus és a pseudocode kapcsolatának tisztázásához.

Megnyitva: `2026-04-09`
