# Big Data

## Gyors vizuális kép

| Jellemző | Jelentés |
|---|---|
| Volume | nagyon sok adat |
| Velocity | gyors adatáramlás |
| Variety | sokféle formátum és forrás |
| Value | üzleti vagy társadalmi haszon |

## Mi a Big Data?

A Big Data nem egyszerűen "sok adat".

Inkább azt jelenti, hogy az adatok:

- túl nagyok
- túl gyorsan jönnek
- túl sokfélék

ahhoz, hogy hagyományos megoldásokkal mindig könnyen kezelhetők legyenek.

## Honnan jöhet sok adat?

Példák:

- közösségi média
- vásárlási tranzakciók
- szenzorok
- GPS-jelek
- képek, videók
- gépi naplók

## Miért fontos?

Mert a jó adatelemzés segíthet:

- jobb döntéseket hozni
- folyamatot optimalizálni
- mintázatokat felismerni
- hibát vagy csalást észlelni
- személyre szabott szolgáltatásokat nyújtani

## Milyen kockázatai vannak?

- adatvédelmi kockázat
- hibás vagy torz adatok
- túlzott megfigyelés
- diszkriminatív döntések
- nehéz adatminőség-ellenőrzés

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| Big Data | nagy, gyors, sokféle adat kezelése |
| adatbázis | adatok strukturált tárolási rendszere |
| AI / Machine Learning | módszer az adatok elemzésére, nem ugyanaz mint maga a Big Data |

## Kidolgozott példa: adatmennyiségből döntés

Egy kitalált üzemben 1000 érzékelő másodpercenként egy 100 bájtos rekordot küld. A nyers adatforgalom `1000 × 100 = 100 000 B/s`, naponta pedig `8 640 000 000 B`, vagyis `8,64 GB`. Ebben még nincs benne az indexek, másolatok és hálózati fejlécek mérete. A szám önmagában nem teszi a feladatot Big Datává: a sebesség, a feldolgozási határidő és a különböző formátumok is számítanak.

Az elemzés előtt ellenőrizzük az időbélyegeket, a mértékegységeket és a hiányzó méréseket. A hibás szenzor több millió hibás adata nem lesz megbízható attól, hogy sok van belőle. Ezt a megbízhatósági szempontot gyakran `Veracity` néven is említik. A `3V`, `4V` és `5V` különböző magyarázó modellek, nem egyetlen kötelező felsorolás.

Az üzem döntése lehet például egy csapágy ellenőrzése növekvő rezgés alapján. A mintázat figyelmeztetés, az okot szakmai vizsgálattal is igazolni kell.

## Vizsgán jól használható megfogalmazás

> A Big Data nagy mennyiségű, gyorsan keletkező
> és sokféle forrásból származó adatok feldolgozását és elemzését jelenti.  
> A fogalmat gyakran a `Volume`, `Velocity` és `Variety` jellemzőkkel írják le.  
> Előnye, hogy értékes információ nyerhető ki belőle, ugyanakkor adatvédelmi, minőségi és etikai kockázatokat is hordoz.

## Gyors önellenőrzés

1. Mit jelent a `Volume`?
2. Mit jelent a `Velocity`?
3. Mit jelent a `Variety`?
4. Mondj két Big Data adatforrást.
5. Mondj egy előnyt és egy kockázatot.

## Rövid válaszok az önellenőrzéshez

1. Nagy adatmennyiség
2. Gyors adatkeletkezés / adatáramlás
3. Sokféle adat és forrás
4. Például szenzorok és tranzakciók
5. Előny: jobb döntéstámogatás; kockázat: adatvédelmi probléma

## Források

- [NIST: Big data](https://csrc.nist.gov/topics/technologies/big-data)  
  Méretezhető architektúra és a Big Data jellemzői.

- [NIST: The real challenge of Big Data](https://www.nist.gov/baldrige/real-challenge-big-data)  
  Veracity és adatminőség; nincs állandó bájtküszöb.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. NIST - Big Data Interoperability Framework: Volume 1, Definitions  
   https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2  
   Használat: hivatalos NIST-definíció és a Big Data alapfogalmainak elsődleges forrása.

2. European Commission - Big data  
   https://digital-strategy.ec.europa.eu/en/policies/big-data  
   Használat: EU-s összefoglaló a Big Data gazdasági és társadalmi szerepéről.

Megnyitva: `2026-04-08`
