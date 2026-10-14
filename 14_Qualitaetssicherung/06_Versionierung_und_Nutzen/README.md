# Versionierung und Nutzen

## Gyors vizuális kép

| Verzió | Tipikus jelentés |
|---|---|
| `2.0.0` | a publikus API-val nem kompatibilis változás |
| `2.1.0` | új funkció, visszafelé kompatibilis |
| `2.1.3` | visszafelé kompatibilis hibajavítás |

## Mi az a versionierung?

A szoftververziózás azt jelenti, hogy a kiadásoknak tudatos verzióazonosítót adunk.

Gyakori séma:

```text
MAJOR.MINOR.PATCH
```

Ez a szemantikus verziózás (`Semantic Versioning`, `SemVer`) legismertebb formája.

## Miért hasznos?

- egyértelműen azonosítható a kiadás
- követhető, milyen mértékű változás történt
- segíti a hibajegyek és kiadások összekapcsolását
- támogatja a frissítések tervezését
- fontos függőségek és kompatibilitás kezelésekor

## Tipikus jelentések

### Major

- a publikus API kompatibilitását törő változás

### Minor

- új, visszafelé kompatibilis funkció

### Patch

- visszafelé kompatibilis hibajavítás

## Versionierung és Versionsverwaltung: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| versionierung | kiadások számozása |
| versionsverwaltung | változások követése egy VCS-ben, pl. `Git` |

## A változás méretétől a kompatibilitásig

A SemVer a közzétett API szerződéséhez viszonyít. Egy könyvtár `sum(numbers)` függvényénél három példa:

| Kiindulás: 2.3.4 | Változás | Új verzió |
|---|---|---|
| dokumentált működés javítása | az üres lista a leírás szerinti 0-t adja | 2.3.5 |
| kompatibilis bővítés | új `average(numbers)` függvény | 2.4.0 |
| kompatibilitást törő módosítás | `sum` szám helyett objektumot ad vissza | 3.0.0 |

Egy egysoros törő módosítás is lehet major. A minor és patch nem „többnyire” kompatibilis: SemVer követésekor ez követelmény. Egy másféle számozási rendet használó alkalmazásnál viszont a saját dokumentált szabály érvényes.

A `0.x.y` kezdeti fejlesztést jelez, stabil publikus API ígérete nélkül. A `2.4.0-rc.1` előzetes kiadás, nem azonos a végleges `2.4.0` verzióval. A már kiadott csomag tartalmát új verzióazonosító nélkül nem cseréljük le; így a hibajegyben szereplő verzió valóban visszakereshető.

## Vizsgán jól használható megfogalmazás

> A versionierung a szoftverkiadások tudatos verziószámozását jelenti.  
> Célja, hogy egyértelműen azonosítható legyen egy adott kiadás, és látható legyen a változás mértéke is.  
> A gyakorlatban gyakori a `major.minor.patch` séma, amely segíti a kompatibilitás, a hibakövetés és a frissítések kezelését.

## Gyors önellenőrzés

1. Mi a versionierung lényege?
2. Miért hasznos egy verziószám?
3. Mit jelöl gyakran a `major`?
4. Mit jelöl gyakran a `patch`?
5. Mi a különbség a versionierung és a versionsverwaltung között?

## Rövid válaszok az önellenőrzéshez

1. A kiadások tudatos számozása
2. Mert azonosíthatóvá és követhetővé teszi a kiadásokat
3. SemVer esetén a publikus API kompatibilitását törő változást, a kódmódosítás méretétől függetlenül.
4. SemVer esetén visszafelé kompatibilis hibajavítást.
5. Az egyik számoz, a másik változásokat kezel

## Források

- [Semantic Versioning 2.0.0](https://semver.org/)  
  Publikus API, kompatibilitás, előzetes kiadás és megváltoztathatatlan kiadott csomag.

- [npm: About semantic versioning](https://docs.npmjs.com/about-semantic-versioning/)  
  Patch, minor és major gyakorlati példák.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. Semantic Versioning 2.0.0  
   https://semver.org/  
   Használat: elsődleges, hivatalos forrás a `major.minor.patch` logikájához.

2. npm Docs - About semantic versioning  
   https://docs.npmjs.com/about-semantic-versioning  
   Használat: modern, gyakorlati összefoglaló a verziózás hasznáról és alkalmazásáról.

Megnyitva: `2026-04-08`
