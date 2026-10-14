# V-Modell Aufbau

## Gyors vizuális kép

```text
Követelmények        ->        Átvételi teszt
Rendszerterv         ->        Rendszerteszt
Architektúra / design ->       Integrációs teszt
Modulterv            ->        Modulteszt
            Implementáció
```

## Mi a V-modell lényege?

A V alak azt mutatja, hogy:

- a fejlesztés lefelé haladva egyre részletesebb lesz
- az implementáció után a jobb oldalon ellenőrzés történik
- minden tervezési szinthez hozzárendelhető egy tesztelési szint

Ez a klasszikus, vizsgán gyakran elvárt alaplogika.  
A hivatalos `V-Modell XT` ezt kibővíti projektirányítási, minőségbiztosítási és változáskezelési elemekkel is.

## Tipikus felépítés

### Bal oldal

- követelmények meghatározása
- rendszertervezés
- részletes tervezés

### Alul

- implementáció / kódolás

### Jobb oldal

- modulteszt
- integrációs teszt
- rendszerteszt
- átvételi teszt

## Miért fontos ez a felépítés?

- már korán gondolni kell a tesztelésre
- jobban követhető, miből mi következik
- szabályozott környezetben jól használható

## V-modell és vízesésmodell: ne keverd össze

| Fogalom | Jelleg |
|---|---|
| vízesésmodell | lineáris fázisok egymás után |
| V-modell | lineáris jelleg + fejlesztés és tesztelés összerendelése |

## Ugyanaz a funkció négy ellenőrzési szinten

Egy eszközkölcsönző rendszerben egy eszközt egyszerre csak egy személy kölcsönözhet:

| Tervezési alap | Kapcsolódó ellenőrzés |
|---|---|
| felhasználói igény | a tanár végigpróbálja a kölcsönzés és visszaadás feladatát |
| rendszerkövetelmény | két egyidejű foglalási kérésből pontosan egy sikerül |
| komponensek kapcsolata | az alkalmazás és az adatbázis együtt érvényesíti a foglalást |
| részletes modulműködés | az elérhetőség-számítás külön egységtesztje |

A teszteket már a megfelelő leírás elkészítésekor tervezzük. A dokumentumok review-ja kódfuttatás nélkül is megtörténhet, a dinamikus teszt a működő részt igényli. Az általános V-ábra a megfeleltetést tanítja, nem azt, hogy minden ellenőrzés csak a kódolás után kezdődik.

A V-Modell XT ennél részletesebb, testreszabható folyamatkeret. Az egyszerű oktatási V és a teljes XT módszertan ezért nem azonos fogalom.

## Vizsgán jól használható megfogalmazás

> A V-modell egy folyamatmodell, amelyben a fejlesztési és a tesztelési tevékenységek egymáshoz vannak rendelve.  
> A bal oldalon a követelmények és a tervezés található,
> alul az implementáció,
> a jobb oldalon pedig a hozzájuk tartozó tesztelési szintek.  
> A modell fő előnye, hogy a tesztelés már a tervezés korai szakaszában hangsúlyt kap.

## Gyors önellenőrzés

1. Mi a V-modell lényege?
2. Mi van a bal oldalon?
3. Mi van a jobb oldalon?
4. Miért fontos a tesztelés hozzárendelése?
5. Miben több a V-modell a vízesésmodellnél?

## Rövid válaszok az önellenőrzéshez

1. A fejlesztési és tesztelési lépések összerendelése
2. Követelmények és tervezés
3. A megfelelő tesztelési szintek
4. Mert tervezhetőbbé teszi az ellenőrzést
5. Külön hangsúlyozza a tesztelési megfeleltetést

## Források

- [V-Modell XT Bund: Einstieg](https://download.gsb.bund.de/BundesCIO/V-Modell_XT_Bund/V-Modell%20XT%20Bund-2.0-HTML/1431a155da001978.html)  
  A hivatalos XT módszertan a szemléltető V-ábrán túlmutató keret.

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Tesztelési szintek és korai ellenőrzések.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. V-Modell XT Bund 2.0 - Gesamt PDF  
   https://download.gsb.bund.de/BundesCIO/V-Modell_XT_Bund/V-Modell-XT-Bund-2.0-Gesamt.pdf  
   Használat: hivatalos, elsődleges forrás a V-modell felépítéséhez és fogalmaihoz.

2. Einstieg in das V-Modell XT Bund  
   https://download.gsb.bund.de/BundesCIO/V-Modell_XT_Bund/V-Modell%20XT%20Bund-2.0-HTML/1431a155da001978.html  
   Használat: rövidebb, áttekintő hivatalos bevezető a modell logikájához.

Megnyitva: `2026-04-08`
