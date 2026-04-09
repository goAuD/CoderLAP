# Probleme des Wasserfallmodells

## Lényeg 30 másodpercben

A vízesésmodell fő problémája, hogy **merev és nehezen reagál a változásokra**.

Röviden:

- a fázisok egymás után következnek
- a visszalépés nehézkes
- a hibák és félreértések sokszor későn derülnek ki

## Gyors vizuális kép

| Tipikus probléma | Miért gond? |
|---|---|
| kevés rugalmasság | a változó igényeket nehéz kezelni |
| késői tesztelés | a hibák későn látszanak |
| kevés korai visszajelzés | rossz irányba mehet a fejlesztés |
| nagy dokumentációs teher | lassíthatja a munkát |

## Miért lehet problémás a vízesésmodell?

A modell lineáris:

- előbb követelmények
- aztán tervezés
- majd fejlesztés
- utána teszt

Ez stabil környezetben működhet, de ha a projekt közben változnak az igények, akkor a modell nehézkessé válhat.

## Tipikus problémák

### 1. A változás drága

Ha későn derül ki, hogy valamit máshogy kellene, akkor több korábbi fázishoz is vissza kell nyúlni.

### 2. A felhasználó későn lát eredményt

Sokáig csak dokumentumok és tervek vannak, működő eredmény kevés.

### 3. A hibák későn látszanak

Ha a tesztelés a folyamat vége felé történik, a problémák kijavítása költségesebb lehet.

### 4. Rosszul kezeli a bizonytalanságot

Új vagy gyorsan változó projektekhez sokszor túl merev.

## Mikor lehet mégis jó?

- ha a követelmények stabilak
- ha erősen szabályozott a környezet
- ha a dokumentáció kiemelten fontos

Tehát nem rossz modell, csak nem minden helyzetben ideális.

## Vizsgán jól használható megfogalmazás

> A vízesésmodell egyik fő problémája a merev, lineáris felépítés.  
> A változó követelményeket nehezen kezeli, és a hibák vagy félreértések gyakran csak későn derülnek ki, amikor a javítás már drágább.  
> Emiatt bizonytalan vagy gyorsan változó projektekben sokszor kevésbé előnyös, mint az iteratív vagy agilis megközelítések.

## Gyakori vizsgahibák

- Azt állítani, hogy a vízesésmodell mindig rossz.
- Nem megemlíteni a változáskezelés nehézségét.
- Kihagyni a késői visszajelzés problémáját.
- Nem tenni különbséget stabil és változó projektek között.

## Gyors önellenőrzés

1. Mi a vízesésmodell fő gyenge pontja?
2. Miért gond a késői tesztelés?
3. Miért nehéz benne a változáskezelés?
4. Milyen projektnél lehet mégis jó?
5. Miért látja későn a felhasználó az eredményt?

## Rövid válaszok az önellenőrzéshez

1. A merevség és a nehéz változáskezelés
2. Mert a hibák későn derülnek ki
3. Mert a fázisok egymásra épülnek
4. Stabil, jól definiált projektnél
5. Mert a működő eredmény később jelenik meg

## Források

1. Atlassian - Waterfall methodology  
   https://www.atlassian.com/agile/project-management/waterfall-methodology  
   Használat: modern, gyakorlati forrás a vízesésmodell előnyeihez és korlátaihoz.

2. IBM - What is the Software Development Lifecycle (SDLC)?  
   https://www.ibm.com/think/topics/sdlc  
   Használat: áttekintés a lineáris és iteratív fejlesztési modellek közti különbségekről.

Megnyitva: `2026-04-08`
