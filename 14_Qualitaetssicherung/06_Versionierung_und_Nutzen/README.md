# Versionierung und Nutzen

## Lényeg 30 másodpercben

A **versionierung** itt nem a verziókezelő rendszert jelenti, hanem azt, hogy a szoftverkiadásoknak értelmes verziószámot adunk.

Röviden:

- látszik, melyik kiadásról van szó
- követhető a változás mértéke
- könnyebb a kompatibilitás és a hibakövetés

## Gyors vizuális kép

| Verzió | Tipikus jelentés |
|---|---|
| `2.0.0` | nagyobb, nem kompatibilis változás |
| `2.1.0` | új funkció, visszafelé jellemzően kompatibilis |
| `2.1.3` | hibajavítás |

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

- nagyobb, törő változás

### Minor

- új funkció, jellemzően kompatibilis bővítés

### Patch

- kisebb javítás, hibafix

## Versionierung és Versionsverwaltung: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| versionierung | kiadások számozása |
| versionsverwaltung | változások követése egy VCS-ben, pl. `Git` |

## Vizsgán jól használható megfogalmazás

> A versionierung a szoftverkiadások tudatos verziószámozását jelenti.  
> Célja, hogy egyértelműen azonosítható legyen egy adott kiadás, és látható legyen a változás mértéke is.  
> A gyakorlatban gyakori a `major.minor.patch` séma, amely segíti a kompatibilitás, a hibakövetés és a frissítések kezelését.

## Gyakori vizsgahibák

- Összekeverni a verziókezeléssel.
- Azt hinni, hogy a verziószám csak dísz.
- Nem megemlíteni a kompatibilitást.
- Nem tudni, mit jelent a `major`, `minor`, `patch`.

## Gyors önellenőrzés

1. Mi a versionierung lényege?
2. Miért hasznos egy verziószám?
3. Mit jelöl gyakran a `major`?
4. Mit jelöl gyakran a `patch`?
5. Mi a különbség a versionierung és a versionsverwaltung között?

## Rövid válaszok az önellenőrzéshez

1. A kiadások tudatos számozása
2. Mert azonosíthatóvá és követhetővé teszi a kiadásokat
3. Nagyobb, törő változást
4. Kisebb hibajavítást
5. Az egyik számoz, a másik változásokat kezel

## Források

1. Semantic Versioning 2.0.0  
   https://semver.org/  
   Használat: elsődleges, hivatalos forrás a `major.minor.patch` logikájához.

2. npm Docs - About semantic versioning  
   https://docs.npmjs.com/about-semantic-versioning  
   Használat: modern, gyakorlati összefoglaló a verziózás hasznáról és alkalmazásáról.

Megnyitva: `2026-04-08`
