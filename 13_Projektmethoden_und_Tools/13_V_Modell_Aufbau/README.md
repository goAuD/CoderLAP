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

## Vizsgán jól használható megfogalmazás

> A V-modell egy folyamatmodell, amelyben a fejlesztési és a tesztelési tevékenységek egymáshoz vannak rendelve.  
> A bal oldalon a követelmények és a tervezés található,
> alul az implementáció,
> a jobb oldalon pedig a hozzájuk tartozó tesztelési szintek.  
> A modell fő előnye, hogy a tesztelés már a tervezés korai szakaszában hangsúlyt kap.

## Gyakori vizsgahibák

- A V-modellt teljesen azonosnak tekinteni a vízesésmodellel.
- Nem megemlíteni a tesztszintek hozzárendelését.
- Csak a V alakot leírni, de a jelentését nem.
- Kihagyni az implementáció központi szerepét.

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

1. V-Modell XT Bund 2.0 - Gesamt PDF  
   https://download.gsb.bund.de/BundesCIO/V-Modell_XT_Bund/V-Modell-XT-Bund-2.0-Gesamt.pdf  
   Használat: hivatalos, elsődleges forrás a V-modell felépítéséhez és fogalmaihoz.

2. Einstieg in das V-Modell XT Bund  
   https://download.gsb.bund.de/BundesCIO/V-Modell_XT_Bund/V-Modell%20XT%20Bund-2.0-HTML/1431a155da001978.html  
   Használat: rövidebb, áttekintő hivatalos bevezető a modell logikájához.

Megnyitva: `2026-04-08`
