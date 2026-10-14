# Coding Standards und Code Konventionen

## Gyors vizuális kép

| Terület | Példa |
|---|---|
| névadás | `camelCase`, `PascalCase` |
| formázás | behúzás, sortörés |
| szerkezet | fájlfelépítés, függvényméret |
| minőség | linter, formatter, szabályok |

## Miért fontos?

- könnyebb olvasni a kódot
- csapatban egységesebb lesz a munka
- kevesebb félreértés
- egyszerűbb review
- jobb karbantarthatóság

## Standard és konvenció: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| coding standard | formálisabb, elvárt szabályrendszer |
| code convention | bevett közös szokás vagy irányelv |

A gyakorlatban sokszor összemosódnak, de a lényeg ugyanaz: legyen következetes a kód.

## Milyen területeket érint?

- változónevek
- osztálynevek
- fájlszerkezet
- kommentelés
- hibakezelés
- importok rendezése
- whitespace és behúzás

## Hogyan tartatjuk be?

- team agreement
- code review
- linter
- formatter
- `.editorconfig`
- CI ellenőrzések

## Miért nem csak "szépségkérdés"?

Mert a rosszul egységesített kód:

- lassítja a csapatot
- növeli a hibázás esélyét
- nehezíti az onboardingot

## Kis csapat, ellenőrizhető megállapodás

**Példa:** a csapat két szóközzel húzza be a JavaScriptet, UTF-8 fájlokat és LF
sortörést használ. A repository gyökerében lévő `.editorconfig` ezt rögzítheti:

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true

[*.js]
indent_style = space
indent_size = 2
```

Az EditorConfigot támogató szerkesztő a megnyitott fájltól felfelé keresi a
beállításokat; `root = true` megállítja ezt a keresést. Egy `.js` fájlra az
általános rész és a JavaScript-rész is érvényes. A konfiguráció önmagában nem
futtat CI-ellenőrzést, és nem javít üzleti logikát.

| Eszköz vagy szabály | Mit bizonyít? | Konkrét példa |
|---|---|---|
| formatter | a megállapodott formátumot | következetes behúzás és sortörés |
| linter | az engedélyezett szabályok teljesülését | nem használt változó vagy nem definiált név jelzése |
| típusellenőrző | a leírt típusok szerinti kapcsolatokat | számot váró paraméter hibás hívása |
| teszt | adott bemenetnél az elvárt viselkedést | a 0 perces időtartam eredménye 0 másodperc |
| review | emberi értékelést a szándékról és megoldásról | érthető-e az adatkezelés és a változtatás oka? |

Névadáskor a mértékegységet is közöljük: `durationSeconds` vagy `priceCents`
pontosabb, mint az önmagában álló `value`. A komment inkább a nem nyilvánvaló
okot magyarázza, ne csupán ismételje az utasítást. A formázási változásokat
érdemes különválasztani a működés módosításától, hogy a diff átlátható maradjon.
A stílusvitát egyszer rendezzük a közös konfigurációban, utána a review a
feladatra összpontosíthat. A linter zöld eredménye nem általános helyességi bizonyíték.

## Vizsgán jól használható megfogalmazás

> A coding standardok és code konvenciók olyan közös szabályok,
> amelyek egységesebbé és jobban olvashatóvá teszik a forráskódot.  
> Ide tartozik például a névadás, a formázás, a szerkezet, a kommentelés és a kódminőségi szabályok használata.  
> Ezek különösen csapatmunkában fontosak, mert megkönnyítik a review-t, a karbantartást és az együttműködést.

## Gyors önellenőrzés

1. Miért fontosak a kódkonvenciók?
2. Milyen területeket szabályozhatnak?
3. Mi a szerepe a linternek?
4. Mi a szerepe a formatternek?
5. Miért segítik a code review-t?

## Rövid válaszok az önellenőrzéshez

1. Egységesebb és olvashatóbb kódot adnak
2. Névadás, formázás, szerkezet stb.
3. Szabálysértéseket és hibákat jelez
4. Egységesen formázza a kódot
5. Mert kevesebb zaj marad, jobban látszik a lényeg

## Források

Ellenőrizve: `2026-10-14`.

- [EditorConfig](https://editorconfig.org/): fájlszintű konfiguráció és keresési sorrend.
- [ESLint: Core concepts](https://eslint.org/docs/latest/use/core-concepts/): szabályalapú statikus ellenőrzés.
- [Prettier: Prettier vs. Linters](https://prettier.io/docs/comparison): formázás és minőségi szabályok szerepe.


1. EditorConfig  
   https://editorconfig.org/  
   Használat: eszköz a projektszintű formázási konvenciók egységesítésére.

2. PEP 8 - Style Guide for Python Code  
   https://peps.python.org/pep-0008/  
   Használat: ismert hivatalos stílusguide-programnyelvi példa.

3. Microsoft Learn - C# coding conventions  
   https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions  
   Használat: hivatalos példája a kódkonvenciók gyakorlati alkalmazásának.

4. typescript-eslint shared configs  
   https://typescript-eslint.io/users/configs/  
   Használat: modern TypeScript szabályozási és lintelési kontextus.

Megnyitva: `2026-04-08`
