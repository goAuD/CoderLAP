# Aktuelle Programmiersprachen

## Gyors vizuális kép

| Nyelv | Tipikus erősség |
|---|---|
| JavaScript / TypeScript | web frontend és sok backend |
| Python | automatizálás, backend, adat, AI |
| Java | enterprise, backend |
| C# | .NET, web, vállalati fejlesztés |
| PHP | klasszikus és modern web backend |
| Kotlin | Android és backend |
| Swift | Apple platformok |
| Dart | Flutter |

## Mit jelent az, hogy "aktuális"?

Nem azt, hogy "új", hanem azt, hogy:

- ma is széles körben használják
- aktív ökoszisztémája van
- van hozzá friss dokumentáció, tooling és közösség
- új projektekben is reális választás

## Mi alapján számít egy nyelv ma fontosnak?

- mennyire használják a gyakorlatban
- mennyi fejlesztési területen jelenik meg
- mennyire aktív az ökoszisztémája
- vannak-e modern frameworkök és eszközök körülötte
- mennyire könnyű vele munkaerőt találni és csapatban dolgozni

## 2026-ban tipikus fő csoportok

### Web és internet

- `JavaScript`
- `TypeScript`
- `PHP`
- `Java`
- `C#`
- `Python`

### Mobil

- `Kotlin`
- `Swift`
- `Dart`
- `JavaScript` / `TypeScript` cross-platform környezetekben

### Általános és backend

- `Python`
- `Java`
- `C#`
- `Go`
- `PHP`

## Miért nincs egyetlen "legjobb" nyelv?

Mert a választás attól függ:

- milyen platformra fejlesztesz
- milyen csapat dolgozik rajta
- milyen teljesítmény kell
- milyen ökoszisztéma előnyös
- milyen meglévő rendszerhez kell illeszkedni

## Mire kell figyelni vizsgán?

Ha a kérdés "aktuális nyelvek", akkor érdemes:

- nem csak egyet mondani
- területhez kötni őket
- megmutatni, hogy ma több fő irány van egyszerre jelen

## Nyelv, futtatókörnyezet és framework külön szerepe

| Elem | Mi ez? | Példa a kapcsolatukra |
|---|---|---|
| JavaScript | programozási nyelv, alapját az ECMAScript szabvány adja | Node.js-ben vagy böngészőben futhat |
| Node.js | JavaScript-futtatókörnyezet | például szerveroldali kódhoz |
| TypeScript | JavaScriptre építő nyelv statikus típusellenőrzéssel | típusaiból általában nem marad futó JavaScript-kód |
| React / Angular | UI-library / webes framework | JavaScript vagy TypeScript projektek eszközei |

**Szemléltető TypeScript-forrás**, amelyet például a TypeScript Playgroundban
lehet fordítani:

```typescript
function greet(name: string): string {
  return `Hallo ${name}`;
}
console.log(greet("Ada"));
```

A típusjelölések nélküli JavaScript-változat Node.js-ben önállóan futtatható:

<!-- example:run -->

```javascript
function greet(name) {
  return `Hallo ${name}`;
}
console.log(greet("Ada"));
```

```text
Hallo Ada
```

A `name: string` fejlesztéskor segít ellenőrizni a hívásokat. A hálózatról
beérkező JSON-t azonban futáskor is ellenőrizni kell, mert a TypeScript-típus
nem alakítja át és nem hitelesíti a külső adatot. A típusellenőrzés, a teszt
és a bemeneti validálás más-más kérdésre ad választ.

**Indokolt választás:** egy kis meglévő PHP-webhely űrlapjának bővítésénél a
karbantartott PHP-környezet megtartása egyszerű lehet; Android-specifikus
eszközfunkcióknál Kotlin és a platform API-ja lehet jó alap. A támogatott
verzió, csapattudás, telepítési környezet és feladat többet mond, mint egyetlen
népszerűségi rangsor. Az itt szereplő felsorolás nem teljes lista és nem rangsor.

## Vizsgán jól használható megfogalmazás

> `2026. október 14.` állapot szerint az aktuális programozási nyelvek közé azok sorolhatók,
> amelyek ma is széles körben használtak és aktívan támogatottak.  
> A webes, mobilos és vállalati fejlesztésben
> különösen fontos például a JavaScript, TypeScript, Python, Java,
> C#, PHP, Kotlin és Swift.  
> Nem egyetlen “legjobb” nyelv létezik, hanem a választás mindig a feladat, a platform és az ökoszisztéma függvénye.

## Gyors önellenőrzés

1. Mit jelent itt az, hogy aktuális?
2. Mondj legalább öt ma releváns nyelvet.
3. Melyek fontosak mobilfejlesztésben?
4. Miért nincs egyetlen legjobb nyelv?
5. Milyen szerepe van az ökoszisztémának?

## Rövid válaszok az önellenőrzéshez

1. Ma is széles körben használt és támogatott
2. Például JavaScript, TypeScript, Python, Java, C#
3. Kotlin, Swift, Dart
4. Mert a feladattól függ
5. Meghatározza a használhatóságot és a fejlesztési környezetet

## Források

Ellenőrizve: `2026-10-14`.

- [TypeScript Handbook: The Basics](https://www.typescriptlang.org/docs/handbook/2/basic-types.html): típusellenőrzés és típusok törlése a fordításkor.
- [Android Developers: Kotlin-first](https://developer.android.com/kotlin/first): feladat- és platformfüggő nyelvválasztás példája.


1. Stack Overflow Developer Survey 2025 - Technology  
   https://survey.stackoverflow.co/2025/technology/  
   Használat: a 2025-ös válaszadók használati szokásainak történeti pillanatképe, nem teljes piaci rangsor vagy mai támogatási igazolás.

2. TypeScript  
   https://www.typescriptlang.org/  
   Használat: a modern webfejlesztésben fontos TypeScript hivatalos forrása.

3. Python Documentation  
   https://docs.python.org/3/  
   Használat: a Python aktuális, aktívan támogatott ökoszisztémájának hivatalos forrása.

4. Oracle Java  
   https://www.oracle.com/java/  
   Használat: a Java hivatalos ökoszisztéma-belépési pontja.

5. .NET Languages  
   https://dotnet.microsoft.com/en-us/languages  
   Használat: a modern .NET és C# nyelvi ökoszisztéma hivatalos forrása.

Megnyitva: `2026-04-08`
