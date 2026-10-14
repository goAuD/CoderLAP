# Zweck von Code Reviews

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

## Statikus review és dinamikus teszt

| Fogalom | Fókusz |
|---|---|
| code review | ember nézi át a kódot |
| dinamikus tesztelés | futás közben ellenőrizzük a viselkedést |

A kettő kiegészíti egymást, nem helyettesíti.

## Review egy hozzáférés-kezelési változtatásnál

A változtatás azt ígéri, hogy a felhasználó csak a saját jegyzetét módosíthatja. Az átnézés során végigkövetjük a kérést a gombtól a szerveroldali műveletig: honnan származik a felhasználóazonosító, hol történik a tulajdonos ellenőrzése, és van-e teszt más személy jegyzetére? A felületi gomb elrejtése hasznos megjelenítési döntés, az engedélyt azonban a szervernek kell ellenőriznie.

Egy konkrét megjegyzés például: „A kért jegyzet azonosítója a kliensből jön. Kérlek, kapcsoljuk az adatlekérdezést a hitelesített felhasználóhoz, és ellenőrizzük másik tulajdonos esetét is.” Ez megmutatja a kockázatot és az elvárt eredményt.

A review a **statikus tesztelés** egyik formája: nem szükséges hozzá a vizsgált program futtatása. A futtatásos, dinamikus teszt más bizonyítékot ad. A kis, célzott módosítás, az érthető leírás és a kész teszteredmény mind segíti az átnézőt.

## Vizsgán jól használható megfogalmazás

> A code review célja,
> hogy a forráskódot egy másik fejlesztő is átnézze
> még az éles használat vagy a beolvasztás előtt.  
> Ennek során korán felismerhetők a hibák, javítható a kód minősége, és erősödik a tudásmegosztás a csapaton belül.  
> A code review tehát nemcsak hibakeresés, hanem minőségbiztosítási és együttműködési eszköz is.

## Gyors önellenőrzés

1. Mi a code review fő célja?
2. Miért jó még a merge előtt elvégezni?
3. Miben segíti a csapatot?
4. Hogyan viszonyul a review a dinamikus teszthez?
5. Milyen típusú problémák derülhetnek ki közben?

## Rövid válaszok az önellenőrzéshez

1. Hibák korai felismerése és minőségjavítás
2. Mert olcsóbb korán javítani
3. Tudásmegosztással és közös minőségi szinttel
4. A review statikus tesztelés, a dinamikus teszt a program futtatásával vizsgálja a viselkedést.
5. Logikai, stílusbeli, biztonsági vagy karbantarthatósági gondok

## Források

- [Google: What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)  
  Működés, tesztek, olvashatóság és a módosítás teljes összefüggése.

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Statikus és dinamikus tesztelés, teszttervezési technikák és lefedettség.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. GitHub - Code review  
   https://github.com/features/code-review  
   Használat: hivatalos, modern forrás a code review szerepéhez a fejlesztési folyamatban.

2. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos háttér a statikus tesztelés és review-k minőségbiztosítási szerepéhez.

Megnyitva: `2026-04-08`
