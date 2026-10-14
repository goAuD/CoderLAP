# Einsatzgebiet jQuery

## Gyors vizuális kép

| Régebbi tipikus használat | Példa |
|---|---|
| DOM-manipuláció | elemek kiválasztása és módosítása |
| eseménykezelés | kattintás, űrlap-esemény |
| Ajax | szerverhívás oldalfrissítés nélkül |
| animáció | egyszerű effektek |

## Mire használták a jQueryt?

Leggyakrabban:

- HTML-elemek kiválasztására
- DOM módosítására
- eseménykezelésre
- Ajax hívásokra
- egyszerű UI-effektekre

Azért lett népszerű, mert sok korai böngészőközi problémát leegyszerűsített.

## Miért volt nagy dolog?

Mert a natív JavaScript régebben:

- nehézkesebb volt
- több böngészőn eltérően működött
- több kóddal ért el ugyanazt

A jQuery ezt sokáig sokkal egyszerűbbé tette.

## Mi a helyzete ma?

`2026. október 14.` állapot szerint:

- a modern böngészők sok korábbi jQuery-feladatot saját API-val is megoldanak
- a jQuery továbbra is karbantartott library, és meglévő oldalakban, CMS-ekben használatos

## Mikor találkozol még vele?

- legacy weboldalakban
- régi adminfelületekben
- CMS-sablonokban
- kisebb, gyorsan összerakott frontend feladatoknál

## jQuery és JavaScript: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| JavaScript | programozási nyelv |
| jQuery | JavaScript library |

## Ugyanaz a feladat jQueryvel és natív DOM API-val

**Böngészős környezet:** a következő HTML már szerepel az oldalon, a JavaScript
pedig utána fut. Az első megoldás betöltött jQueryt igényel:

```html
<button id="ready" type="button">Bereit</button>
<p id="status" role="status"></p>
```

```javascript
$("#ready").on("click", () => {
  $("#status").text("Die Übung kann beginnen.");
});
```

A gomb aktiválása után a bekezdés szövege `Die Übung kann beginnen.` lesz.
A `$` elemet választ, az `on` eseményt kapcsol hozzá, a `text` szöveget állít be.
Ugyanennek a feladatnak a külön, jQuery nélküli alternatívája:

```javascript
document.querySelector("#ready").addEventListener("click", () => {
  document.querySelector("#status").textContent = "Die Übung kann beginnen.";
});
```

A két JavaScript-változat közül egyet használunk. Szöveges adatot `text` vagy
`textContent` segítségével jelenítünk meg, mert ezek nem értelmezik HTML-ként.
Ha egy projekt már jQueryre és tesztelt pluginokra épül, a karbantartásuk
értelmes döntés lehet. Egyetlen ilyen gombhoz viszont a böngésző saját API-ja is
elegendő, új függőség nélkül.

**Állapot 2026-10-14:** a jQuery nem megszűnt projekt. A hivatalos 4.0.0 kiadás
2026. január 17-én jelent meg. Főverzióváltásnál kompatibilitást és pluginokat
ellenőrzünk; a csomag meglétéből nem következik, hogy bármely régi verziója
biztonságos vagy minden modern böngészőhöz szükséges.

## Vizsgán jól használható megfogalmazás

> A jQuery egy JavaScript library,
> amely leegyszerűsíti a DOM-manipulációt,
> az eseménykezelést és az Ajax-alapú kommunikációt.  
> Történetileg nagyon fontos szerepe volt a webfejlesztésben,
> különösen a böngészőközi kompatibilitási problémák kezelésében.  
> Ma már kisebb a szerepe, de régi rendszerekben és egyszerűbb webes feladatoknál még mindig előfordul.

## Gyors önellenőrzés

1. Mi a jQuery?
2. Mire használták leggyakrabban?
3. Miért lett népszerű?
4. Mi a helyzete ma?
5. Miben különbözik a JavaScript-től?

## Rövid válaszok az önellenőrzéshez

1. Egy JavaScript library
2. DOM, események, Ajax kezelésére
3. Mert leegyszerűsítette a böngészőközi webfejlesztést
4. Karbantartott library; szükségességét a projekt és a natív API-k alapján mérlegeljük
5. A JavaScript nyelv, a jQuery arra épülő library

## Források

Ellenőrizve: `2026-10-14`.

- [jQuery: 4.0.0 release](https://blog.jquery.com/2026/01/17/jquery-4-0-0/): karbantartási státusz és főverzióváltás.
- [jQuery: text()](https://api.jquery.com/text/): szöveges DOM-módosítás.


1. jQuery official site  
   https://jquery.com/  
   Használat: hivatalos leírás arról, mire való a jQuery.

2. jQuery API Documentation  
   https://api.jquery.com/  
   Használat: a jQuery fő funkcióinak hivatalos referenciája.

3. Stack Overflow Developer Survey 2025 - Web frameworks and technologies  
   https://survey.stackoverflow.co/2025/technology/  
   Használat: történeti, 2025-ös használati felmérés; a mai támogatási státuszt a gyártói kiadási közleményből ellenőrizzük.

Megnyitva: `2026-04-08`
