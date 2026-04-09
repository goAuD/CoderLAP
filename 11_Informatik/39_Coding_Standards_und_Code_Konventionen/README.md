# Coding Standards und Code Konventionen

## Lényeg 30 másodpercben

A **coding standard** és a **code convention** olyan szabályrendszer, amely egységesebbé teszi a kódot.

Röviden:

- hogyan nevezzünk el dolgokat
- hogyan tördeljünk és formázzunk
- milyen szerkezetet kövessünk
- hogyan legyen olvasható és karbantartható a kód

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

## Vizsgán jól használható megfogalmazás

> A coding standardok és code konvenciók olyan közös szabályok, amelyek egységesebbé és jobban olvashatóvá teszik a forráskódot.  
> Ide tartozik például a névadás, a formázás, a szerkezet, a kommentelés és a kódminőségi szabályok használata.  
> Ezek különösen csapatmunkában fontosak, mert megkönnyítik a review-t, a karbantartást és az együttműködést.

## Gyakori vizsgahibák

- Azt állítani, hogy ez csak esztétikai kérdés.
- Nem megemlíteni a csapatmunka szerepét.
- A standardot és a lintert ugyanannak nevezni.
- Nem hozni rá konkrét példát.

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
