# Erste drei Normalformen

## Lényeg 30 másodpercben

Az első három normálforma célja, hogy az adatbázis szerkezete rendezettebb legyen, és csökkenjen a redundancia és az anomáliák esélye.

Röviden:

- `1NF`: egy mezőben egy érték
- `2NF`: a nem kulcsmezők teljesen függjenek a teljes kulcstól
- `3NF`: a nem kulcsmezők ne függjenek más nem kulcsmezőktől

## Gyors vizuális kép

| Normálforma | Lényege |
|---|---|
| `1NF` | nincs ismétlődő csoport, egy cellában egy érték |
| `2NF` | nincs részleges függés összetett kulcs esetén |
| `3NF` | nincs tranzitív függés nem kulcsmezők között |

## Miért van szükség normalizálásra?

Mert segít:

- csökkenteni a redundanciát
- elkerülni az adatinkonzisztenciát
- könnyebbé tenni a karbantartást

## `1NF` - első normálforma

Egy mezőben csak **egyetlen atomi érték** legyen.

Nem jó például:

- egy mezőben több telefonszám vesszővel elválasztva

## `2NF` - második normálforma

A tábla legyen `1NF`-ben, és minden nem kulcsmező a **teljes kulcstól** függjön.

Ez főleg összetett kulcs esetén fontos.

Ha egy mező csak a kulcs egyik részétől függ, azt külön táblába kell tenni.

## `3NF` - harmadik normálforma

A tábla legyen `2NF`-ben, és a nem kulcsmezők **ne függjenek más nem kulcsmezőktől**.

Vagyis:

- a nem kulcsmezők a kulcstól függjenek
- ne egymástól

## Egyszerű példa

Ha egy `Products` táblában van:

- `ProductID`
- `SRP`
- `Discount`

és a `Discount` az `SRP`-től függ, nem közvetlenül a kulcstól, akkor ez `3NF`-sértés lehet.

## Mire kell figyelni vizsgán?

- ne csak definíciót mondd, hanem a célt is
- a `2NF`-nél fontos az összetett kulcs
- a `3NF`-nél a tranzitív függés a kulcsszó

## Vizsgán jól használható megfogalmazás

> Az első három normálforma a relációs adatbázistervezés alapelvei közé tartozik.  
> Az első normálforma szerint egy mezőben csak egy érték szerepelhet, a második normálforma kizárja a részleges függéseket összetett kulcs esetén, a harmadik normálforma pedig megtiltja, hogy nem kulcsmezők más nem kulcsmezőktől függjenek.  
> Ezek a szabályok csökkentik a redundanciát és javítják az adatkonzisztenciát.

## Gyakori vizsgahibák

- A `1NF`-et csak “rendezett táblának” nevezni.
- A `2NF` lényegéből kihagyni az összetett kulcsot.
- A `3NF`-et összekeverni a `2NF`-fel.
- Nem megemlíteni a tranzitív függést.

## Gyors önellenőrzés

1. Mi az `1NF` lényege?
2. Mikor fontos különösen a `2NF`?
3. Mit tilt a `3NF`?
4. Miért jó a normalizálás?
5. Mi az a tranzitív függés röviden?

## Rövid válaszok az önellenőrzéshez

1. Egy mezőben egy érték
2. Összetett kulcs esetén
3. Nem kulcsmezők egymástól való függését
4. Mert csökkenti a redundanciát és hibákat
5. Amikor egy nem kulcsmező más nem kulcsmezőtől függ

## Források

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Használat: hivatalos, jól érthető magyarázat az első három normálformához.

2. Microsoft Learn - Description of the database normalization basics  
   https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/access/database-normalization-description  
   Használat: hivatalos háttér a normalizálás céljához és a `1NF`, `2NF`, `3NF` gyakorlati értelmezéséhez.

Megnyitva: `2026-04-09`
