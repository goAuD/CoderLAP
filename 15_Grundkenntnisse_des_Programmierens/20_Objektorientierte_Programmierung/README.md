# Objektorientierte Programmierung

## Lényeg 30 másodpercben

Az objektumorientált programozás (`OOP`) olyan szemlélet, amelyben a rendszert objektumokkal modellezzük, amelyek állapotot és viselkedést is tartalmaznak.

Röviden:

- osztályok és objektumok köré épül
- az adat és a művelet összetartozik
- célja a jobb modellezhetőség és karbantarthatóság

## Gyors vizuális kép

| Fogalom | Jelentés |
|---|---|
| osztály | sablon vagy terv |
| objektum | az osztály konkrét példánya |
| attribútum | az objektum adata |
| metódus | az objektum művelete |

## Mi az OOP alapötlete?

A programot nem pusztán lépéssorként, hanem együttműködő objektumok rendszerként nézzük.

Egy objektum:

- rendelkezik adatokkal
- képes műveleteket végrehajtani
- kapcsolatban állhat más objektumokkal

## Az OOP fő fogalmai

### Osztály és objektum

- az osztály egy minta vagy terv
- az objektum ennek konkrét példánya

### Encapsulation

Az adatok és a hozzájuk tartozó műveletek összezárása.  
Segít abban, hogy ne lehessen mindent bárhonnan összevissza módosítani.

### Inheritance

Egy osztály tulajdonságokat és működést örökölhet egy másikból.

### Polymorphism

Ugyanaz a művelet különböző objektumoknál eltérően valósulhat meg.

### Abstraction

A lényeges dolgokat kiemeljük, a felesleges részleteket elrejtjük.

## Miért hasznos?

- jobban modellezhetők valós vagy üzleti entitások
- könnyebb lehet a bővítés
- javíthatja az újrafelhasználhatóságot
- nagyobb rendszereknél átláthatóbb szerkezetet adhat

## De nem csodaszer

Az OOP sem mindenre tökéletes.

Gond lehet, ha:

- túltervezzük
- feleslegesen bonyolítjuk az osztályhierarchiát
- rosszul választjuk meg a felelősségeket

## OOP és procedurális megközelítés

| Szempont | Procedurális | OOP |
|---|---|---|
| fő fókusz | lépések | objektumok |
| szervezés | függvények / eljárások | osztályok / objektumok |
| adatok és műveletek | gyakran külön | együtt kezelve |

## Vizsgán jól használható megfogalmazás

> Az objektumorientált programozás olyan programozási paradigma, amelyben a rendszert objektumokkal modellezzük.  
> Az objektumok állapotot és viselkedést tartalmaznak, és általában osztályok alapján jönnek létre.  
> Az OOP fontos fogalmai az osztály, objektum, encapsulation, inheritance, polymorphism és abstraction.  
> Fő előnye a jobb modellezhetőség és karbantarthatóság, különösen összetettebb rendszereknél.

## Gyakori vizsgahibák

- Az OOP-t csak öröklésként leírni.
- Az objektumot az osztállyal összekeverni.
- Azt állítani, hogy minden jó program csak OOP lehet.
- Kihagyni az encapsulation szerepét.

## Gyors önellenőrzés

1. Mi az osztály?
2. Mi az objektum?
3. Mit jelent az encapsulation?
4. Mit jelent a polymorphism?
5. Milyen előnye lehet az OOP-nak?

## Rövid válaszok az önellenőrzéshez

1. Terv vagy sablon
2. Az osztály példánya
3. Adatok és műveletek összezárása
4. Ugyanaz a művelet többféleképp valósulhat meg
5. Jobb modellezhetőség és karbantarthatóság

## Források

1. Oracle Java Tutorials - Object-Oriented Programming Concepts  
   https://docs.oracle.com/javase/tutorial/java/concepts  
   Használat: hivatalos, elsődleges forrás az OOP alapfogalmaihoz.

2. MDN - Working with objects  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_objects  
   Használat: modern, jól olvasható forrás objektumok, tulajdonságok és metódusok gyakorlati értelmezéséhez.

Megnyitva: `2026-04-09`
