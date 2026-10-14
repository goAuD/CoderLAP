# Klassen

## Gyors vizuális kép

| Fogalom | Jelentés |
|---|---|
| osztály | minta / terv |
| objektum | az osztály konkrét példánya |
| attribútum | adat vagy tulajdonság |
| metódus | az osztályhoz tartozó művelet |

## Mi az a class?

Az osztály leírja:

- milyen tulajdonságai vannak egy objektumnak
- milyen műveleteket tud végrehajtani

Példa:

```text
Osztály: Car
  attribútumok: color, speed
  metódusok: start(), brake()
```

## Miért fontos?

- rendezi a program szerkezetét
- segít valós vagy üzleti fogalmak modellezésében
- támogatja az újrafelhasználhatóságot
- jobban szétválasztja a felelősségeket

## Osztály és objektum: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| osztály | sablon |
| objektum | a sablon alapján létrejövő konkrét elem |

## Tipikus elemek

- attribútumok
- metódusok
- konstruktor
- láthatósági szabályok, például `public`, `private`

## Miért kapcsolódik a rendszerfejlesztéshez?

Mert osztályokkal:

- jobban tervezhetők a komponensek
- tisztább felelősségi körök adhatók
- bővíthetőbb szerkezet készíthető

## Konstruktor, példánytag és statikus tag

Két témát hozunk létre, de csak az elsőt jelöljük késznek. A teljes példa Node.js-ben fut.

<!-- example:run -->

```javascript
class Topic {
  static created = 0;
  constructor(title) {
    if (typeof title !== "string" || title.trim() === "") {
      throw new TypeError("Nonempty title required");
    }
    this.title = title;
    this.completed = false;
    Topic.created += 1;
  }
  complete() { this.completed = true; }
}
const first = new Topic("Loops");
const second = new Topic("Functions");
first.complete();
console.log(first.completed, second.completed, Topic.created);
```

```text
true false 2
```

A `new Topic(...)` létrehoz egy példányt és meghívja a konstruktort. A konstruktor
ellenőrzi a címet és beállítja a kezdőállapotot. A `this` az aktuális példányt
jelöli. A `title` és `completed` példányonként külön adat; a `static created`
viszont az osztályhoz tartozik, ezért `Topic.created` alakban kérjük le.

A számláló a létrehozások száma ebben a folyamatban, nem az adatbázisban tárolt
témák száma és nem a még élő objektumok száma. A nyilvános mezők itt a tanulhatóságot
szolgálják. Érvényességi szabályok védelméhez privát mező és ellenőrző metódus
használható; JavaScriptben ezt `#` jelöli, nem `private` kulcsszó.

## Vizsgán jól használható megfogalmazás

> Az osztály az objektumorientált programozás egyik alapfogalma, amely egy objektumtípus tulajdonságait és műveleteit  
> írja le.  
> Az osztály egy terv vagy sablon, amelyből konkrét objektumok példányosíthatók.  
> Segítségével a program jobban strukturálható, és a valós világ elemei vagy üzleti fogalmai jól modellezhetők.

## Gyors önellenőrzés

1. Mi az osztály?
2. Mi az objektum?
3. Milyen elemei lehetnek egy osztálynak?
4. Miért hasznosak az osztályok?
5. Miben különbözik az osztály és az objektum?

## Rövid válaszok az önellenőrzéshez

1. Sablon vagy terv
2. Az osztály példánya
3. Attribútumok, metódusok, konstruktor
4. Mert strukturálják a rendszert
5. Az egyik minta, a másik konkrét példány

## Források

Ellenőrizve: `2026-10-14`.

- [MDN: Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes): konstruktor, static és példánytagok.


1. MDN - Using classes  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_classes  
   Használat: modern, hivatalos forrás az osztály fogalmához és elemeihez.

2. Python Docs - Classes  
   https://docs.python.org/3/tutorial/classes.html  
   Használat: hivatalos, jól követhető forrás az osztályok és példányok szerepéhez.

Megnyitva: `2026-04-09`
