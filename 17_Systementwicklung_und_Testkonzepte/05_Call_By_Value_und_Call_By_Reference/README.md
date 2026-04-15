# Call By Value und Call By Reference

## Gyors vizuális kép

| Mód | Mi történik? |
|---|---|
| `call by value` | a függvény egy másolattal dolgozik |
| `call by reference` | a függvény az eredeti adathoz kapcsolódik |

## Mi az a `call by value`?

Ilyenkor a függvény:

- a paraméter értékének másolatát kapja meg
- a módosítás jellemzően nem írja át közvetlenül az eredeti változót

Előnye:

- biztonságosabb, mert kevésbé okoz váratlan mellékhatást

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

## Vizsgán jól használható megfogalmazás

> `Call by value` esetén a függvény a paraméter értékének másolatával dolgozik, ezért a módosítás jellemzően nem  
> érinti közvetlenül az eredeti változót.  
> `Call by reference` esetén a függvény hivatkozáson keresztül éri el az adatot, ezért az eredeti érték is módosulhat.  
> A pontos megvalósítás programozási nyelvenként eltérhet, de az alapvető különbség a másolat és a közvetlenebb
> hozzáférés között van.

## Gyakori vizsgahibák

- Azt állítani, hogy minden nyelv tisztán ugyanúgy működik.
- Nem megemlíteni a mellékhatások lehetőségét.
- A referenciát pointerrel teljesen azonosítani.
- Úgy tenni, mintha a paraméterátadás csak technikai részlet lenne.

## Gyors önellenőrzés

1. Mi a `call by value` lényege?
2. Mi a `call by reference` lényege?
3. Miért fontos ez a függvényeknél?
4. Mi az egyik kockázata a referencia-alapú módosításnak?
5. Miért kell óvatosan általánosítani a nyelvek között?

## Rövid válaszok az önellenőrzéshez

1. Másolatot kap a függvény
2. Az eredetihez kapcsolódva dolgozik
3. Mert hat a módosíthatóságra és hibákra
4. Váratlan mellékhatás
5. Mert a pontos megvalósítás eltérhet

## Források

1. Microsoft Learn - Method Parameters (C#) – Pass by value and pass by reference  
   https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/method-parameters  
   Használat: hivatalos, jól érthető forrás a két paraméterátadási mód alapkülönbségéhez.

2. Oracle - Pass-By-Value Example  
   https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html  
   Használat: hivatalos forrás arra, hogy a nyelvi megvalósítás és az általános fogalmi különbség nem mindig ugyanaz.

Megnyitva: `2026-04-09`
