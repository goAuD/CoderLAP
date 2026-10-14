# Call By Value und Call By Reference

## Gyors vizuális kép

| Mód | Mi történik? |
|---|---|
| `call by value` | a paraméter az átadott érték másolatát kapja, ez objektumhivatkozás is lehet |
| `call by reference` | a paraméter a hívó változóját jelöli |

## Mi az a `call by value`?

Ilyenkor a függvény:

- a paraméter értékének másolatát kapja meg
- a paraméter újraértékadása nem írja át a hívó változóját; közösen elért objektum módosítása külön kérdés

Előnye:

- a helyi paraméterkötés változtatása elkülönül a hívó változójától

## Mi az a `call by reference`?

Ilyenkor a függvény:

- nem egyszerű másolattal dolgozik
- hanem úgy kap hozzáférést, hogy az eredeti adat is módosulhat

Előnye:

- bizonyos helyzetekben hatékonyabb lehet
- közvetlenebb módosítást tesz lehetővé

## Miért kell óvatosan fogalmazni?

Mert a modern nyelvek nem mindig tisztán csak ezt vagy azt valósítják meg.

Például:

- egyes nyelvek csak érték szerinti átadást használnak, de referenciatípusokkal
- mások támogatnak valódi referencia szerinti átadást is

Vizsgán ezért az alapelvet kell jól érteni:

- másolat vagy közvetlenebb hozzáférés az eredetihez

## Mikor fontos ez?

- függvények tervezésénél
- mellékhatások megértésénél
- hibakeresésnél
- teljesítmény és memória szempontjából

## Mellékhatás: kulcsfogalom

Ha egy függvény megváltoztatja a kívülről kapott adatot, az mellékhatás lehet.

Ezért jó vizsgás mondat:

- a `call by reference`-szerű viselkedés erősebb mellékhatást eredményezhet

## JavaScript: az átadott érték lehet objektumhivatkozás

A JavaScript paraméterei érték szerint kapják az argumentumokat. Objektumnál
a hivatkozás értéke másolódik, ezért a hívó és a függvény ugyanazt az objektumot
érheti el. Ez nem a hívó változójának referencia szerinti átadása.

<!-- example:run -->

```javascript
function change(number, record) {
  number = 99;
  record.count = 2;
  record = { count: 99 };
  console.log(number, record.count);
}
let number = 1;
const record = { count: 1 };
change(number, record);
console.log(number, record.count);
```

```text
99 99
1 2
```

A Node.js-példában a helyi `number = 99` nem írja át a külső `number` változót.
A `record.count = 2` viszont a közösen elért objektumot módosítja, ezért a hívó
is 2-t lát. A `record = { count: 99 }` már csak a helyi paramétert köti másik
objektumhoz; a hívó továbbra is az eredetire hivatkozik.

Valódi referencia szerinti átadásnál a paraméter a hívó változóját is jelölheti:
például C#-ban a `ref` ezt kifejezetten jelzi. Ettől külön kérdés, hogy egy
objektum tulajdonságai módosíthatók-e. A függvény szerződésében ezért írjuk le,
hogy módosítja-e a kapott objektumot vagy új eredményt készít.

## Vizsgán jól használható megfogalmazás

> `Call by value` esetén az átadott érték másolódik; a paraméter újraértékadása nem változtatja meg a hívó változóját.  
> `Call by reference` esetén a függvény hivatkozáson keresztül éri el az adatot, ezért az eredeti érték is módosulhat.  
> A pontos megvalósítás programozási nyelvenként eltérhet, de az alapvető különbség a másolat és a közvetlenebb
> hozzáférés között van.

## Gyors önellenőrzés

1. Mi a `call by value` lényege?
2. Mi a `call by reference` lényege?
3. Miért fontos ez a függvényeknél?
4. Mi az egyik kockázata a referencia-alapú módosításnak?
5. Miért kell óvatosan általánosítani a nyelvek között?

## Rövid válaszok az önellenőrzéshez

1. Az átadott érték másolatát kapja a paraméter, objektumhivatkozás esetén is
2. A paraméter a hívó változóját jelöli
3. Mert hat a módosíthatóságra és hibákra
4. Váratlan mellékhatás
5. Mert a pontos megvalósítás eltérhet

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions): JavaScript érték szerinti átadás és objektummódosítás.
- [Microsoft: Method parameters](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters): valódi ref paraméter.


1. Microsoft Learn - Method Parameters (C#) – Pass by value and pass by reference  
   https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters  
   Használat: hivatalos, jól érthető forrás a két paraméterátadási mód alapkülönbségéhez.

2. Oracle - Pass-By-Value Example  
   https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html  
   Használat: hivatalos forrás arra, hogy a nyelvi megvalósítás és az általános fogalmi különbség nem mindig ugyanaz.

Megnyitva: `2026-04-09`
