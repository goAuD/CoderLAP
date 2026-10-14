# Vererbungsprinzip

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

## Azonos művelet, felülírt megvalósítás

Az alábbi Node.js-példában egy üzenet szöveggé alakítását specializáljuk:

<!-- example:run -->

```javascript
class Message {
  constructor(text) { this.text = text; }
  render() { return this.text; }
}
class UrgentMessage extends Message {
  render() { return `! ${super.render()}`; }
}
for (const message of [new Message("Ready"), new UrgentMessage("Save")]) {
  console.log(message.render());
}
```

```text
Ready
! Save
```

Az `extends` összekapcsolja az osztályokat. Az `UrgentMessage` örökli a konstruktor
viselkedését, és felülírja a `render` metódust. A `super.render()` a szülő
megvalósítását hívja. A ciklus ugyanúgy `render()`-t kér mindkettőtől, mégis eltérő
eredményt kap: ez polimorf viselkedés.

A hívó szerződése mindkét esetben megmarad: a `render` szöveget ad vissza.
Öröklést akkor választunk, ha a leszármazott a szülő helyén értelmesen használható.
Ha egy üzenethez naplózó szolgáltatás tartozik, az „van neki” kapcsolat, ezért
inkább átadott komponenssel modellezzük. A közös kódsorok önmagukban még nem
indokolnak öröklési hierarchiát.

## Vizsgán jól használható megfogalmazás

> Az öröklés az objektumorientált programozás egyik alapelve, amely lehetővé teszi, hogy egy osztály tulajdonságokat  
> és műveleteket vegyen át egy másik osztálytól.  
> Ez támogatja az újrafelhasználhatóságot és a közös viselkedés kiemelését.  
> Ugyanakkor a túlzott vagy rosszul megtervezett öröklés bonyolult és nehezen karbantartható rendszert eredményezhet.

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

Ellenőrizve: `2026-10-14`.

- [MDN: Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes): extends, super és metódusfelülírás.


1. MDN - Inheritance and the prototype chain  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain  
   Használat: hivatalos, modern forrás az öröklés általános alapelvéhez.

2. Python Docs - Inheritance  
   https://docs.python.org/3/tutorial/classes.html#inheritance  
   Használat: hivatalos, tiszta forrás az öröklés gyakorlati működéséhez.

Megnyitva: `2026-04-09`
