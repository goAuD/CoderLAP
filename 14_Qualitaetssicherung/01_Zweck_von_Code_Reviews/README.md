# Zweck von Code Reviews

## Lényeg 30 másodpercben

A **code review** célja, hogy a kódot még beolvasztás vagy kiadás előtt egy másik ember is átnézze.

Röviden:

- hibákat lehet korán észrevenni
- javítja a kód minőségét
- segíti a tudásmegosztást a csapatban
- csökkenti a rossz döntések vagy rejtett hibák esélyét

## Gyors vizuális kép

| Cél | Mit ad? |
|---|---|
| hibák korai észlelése | kevesebb késői javítás |
| minőségjavítás | olvashatóbb, egységesebb kód |
| tudásmegosztás | több ember érti a rendszert |
| kockázatcsökkentés | kevesebb egyemberes tudás |

## Mi az a code review?

A code review során valaki más is megnézi a módosított kódot.

Tipikusan ellenőrizheti:

- helyes-e a megoldás
- érthető-e a kód
- követi-e a csapat szabályait
- vannak-e kockázatok vagy mellékhatások
- hiányzik-e teszt vagy dokumentáció

## Mi a fő célja?

A code review nem csak hibakeresés.

Fő céljai:

- technikai hibák korai felismerése
- kódminőség javítása
- egységes stílus és szabályok betartása
- csapatszintű tanulás
- biztonságosabb beolvasztás

## Mire nem való?

- nem személyes kritika
- nem hatalmi eszköz
- nem csak formai hibák keresése
- nem szabad végtelen vitává váljon

## Code review és tesztelés: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| code review | ember nézi át a kódot |
| tesztelés | futás közben ellenőrizzük a viselkedést |

A kettő kiegészíti egymást, nem helyettesíti.

## Vizsgán jól használható megfogalmazás

> A code review célja, hogy a forráskódot egy másik fejlesztő is átnézze még az éles használat vagy a beolvasztás előtt.  
> Ennek során korán felismerhetők a hibák, javítható a kód minősége, és erősödik a tudásmegosztás a csapaton belül.  
> A code review tehát nemcsak hibakeresés, hanem minőségbiztosítási és együttműködési eszköz is.

## Gyakori vizsgahibák

- A code review-t pusztán helyesírás-ellenőrzésnek tekinteni.
- Nem megemlíteni a tudásmegosztást.
- Azt állítani, hogy a code review helyettesíti a tesztelést.
- Személyes kritikával összekeverni a szakmai ellenőrzést.

## Gyors önellenőrzés

1. Mi a code review fő célja?
2. Miért jó még a merge előtt elvégezni?
3. Miben segíti a csapatot?
4. Miért nem ugyanaz, mint a tesztelés?
5. Milyen típusú problémák derülhetnek ki közben?

## Rövid válaszok az önellenőrzéshez

1. Hibák korai felismerése és minőségjavítás
2. Mert olcsóbb korán javítani
3. Tudásmegosztással és közös minőségi szinttel
4. Mert emberi átnézés, nem futás közbeni ellenőrzés
5. Logikai, stílusbeli, biztonsági vagy karbantarthatósági gondok

## Források

1. GitHub - Code review  
   https://github.com/features/code-review  
   Használat: hivatalos, modern forrás a code review szerepéhez a fejlesztési folyamatban.

2. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos háttér a statikus tesztelés és review-k minőségbiztosítási szerepéhez.

Megnyitva: `2026-04-08`
