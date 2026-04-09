# Vererbungsprinzip

## Lényeg 30 másodpercben

Az **öröklés** (`inheritance`) azt jelenti, hogy egy osztály átvehet tulajdonságokat és viselkedést egy másik osztálytól.

Röviden:

- van szülő és leszármazott osztály
- a közös részek újrafelhasználhatók
- de túlhasználva bonyolulttá teheti a rendszert

## Gyors vizuális kép

```text
Vehicle
  -> Car
  -> Bike
```

## Mi az öröklés lényege?

Ha több osztálynak vannak közös tulajdonságai vagy műveletei, akkor ezek egy ősosztályba szervezhetők.

Példa:

- `Vehicle` osztály: `speed`, `move()`
- `Car` osztály: örökli ezeket, és még saját elemei is lehetnek

## Miért hasznos?

- csökkenti a kódismétlést
- segít közös logikát kiemelni
- jobban szervezhetővé teszi a modellt

## Lehetséges veszélyei

- túl mély öröklési hierarchia
- nehezebb átláthatóság
- rossz általánosítások
- merevebb szerkezet

Ezért vizsgán jó, ha kimondod:

- az öröklés hasznos, de nem mindenre ez a legjobb eszköz

## Öröklés és kompozíció: rövid különbség

| Fogalom | Alapötlet |
|---|---|
| öröklés | “egy speciálisabb változata valaminek” |
| kompozíció | “részekből áll össze” |

## Mi öröklődik tipikusan?

- attribútumok
- metódusok
- általános viselkedés

De a leszármazott osztály:

- kibővítheti
- módosíthatja
- felülírhatja egyes elemek működését

## Vizsgán jól használható megfogalmazás

> Az öröklés az objektumorientált programozás egyik alapelve, amely lehetővé teszi, hogy egy osztály tulajdonságokat és műveleteket vegyen át egy másik osztálytól.  
> Ez támogatja az újrafelhasználhatóságot és a közös viselkedés kiemelését.  
> Ugyanakkor a túlzott vagy rosszul megtervezett öröklés bonyolult és nehezen karbantartható rendszert eredményezhet.

## Gyakori vizsgahibák

- Az öröklést minden OOP-megoldás alapjának nevezni.
- Nem megemlíteni az újrafelhasználhatóságot.
- Kihagyni a lehetséges hátrányokat.
- Az öröklést osztálypéldányosítással összekeverni.

## Gyors önellenőrzés

1. Mi az öröklés lényege?
2. Miért hasznos?
3. Mi lehet a hátránya?
4. Mi a különbség szülő és leszármazott osztály között?
5. Mi a különbség öröklés és kompozíció között röviden?

## Rövid válaszok az önellenőrzéshez

1. Közös tulajdonságok és műveletek átvétele
2. Mert csökkenti az ismétlést és szervezettebb modellt ad
3. Túl bonyolult hierarchiát okozhat
4. A leszármazott átvesz és bővít
5. Az egyik “is-a”, a másik inkább “has-a” jellegű

## Források

1. MDN - Inheritance and the prototype chain  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain  
   Használat: hivatalos, modern forrás az öröklés általános alapelvéhez.

2. Python Docs - Inheritance  
   https://docs.python.org/3/tutorial/classes.html#inheritance  
   Használat: hivatalos, tiszta forrás az öröklés gyakorlati működéséhez.

Megnyitva: `2026-04-09`
