# Auswertung eines Softwaretests

## Lényeg 30 másodpercben

A szoftverteszt kiértékelése azt jelenti, hogy összehasonlítjuk a tényleges eredményt a várt eredménnyel, és eldöntjük, hogy a teszt sikeres volt-e.

Röviden:

- elvárt eredmény vs tényleges eredmény
- pass / fail döntés
- eltérés esetén hiba vagy további vizsgálat

## Gyors vizuális kép

| Lépés | Kérdés |
|---|---|
| teszt futtatása | mi történt ténylegesen? |
| összehasonlítás | ezt vártuk? |
| értékelés | megfelelt vagy nem? |
| jelentés | mit kell rögzíteni és továbbadni? |

## Mit jelent a teszt kiértékelése?

A kiértékelés során:

- megnézzük a teszt eredményét
- összevetjük a specifikációval vagy tesztesettel
- rögzítjük az eltéréseket
- eldöntjük a következő lépést

## Milyen eredmény lehet?

### Sikeres teszt

- a tényleges eredmény megfelel a vártnak

### Sikertelen teszt

- eltérés van a várt és a tényleges eredmény között

### Nem egyértelmű eredmény

- lehet környezeti probléma
- lehet rossz tesztadat
- lehet nem reprodukálható hiba

## Mit kell rögzíteni?

Tipikusan:

- teszteset azonosító
- bemenetek
- várt eredmény
- tényleges eredmény
- státusz
- hiba leírása

## Miért fontos a jó kiértékelés?

- segíti a hibajavítást
- nyomon követhetővé teszi a minőséget
- segíti a döntést, kiadható-e a szoftver
- objektívebbé teszi a tesztelést

## Teszt kiértékelése és hibajavítás: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| kiértékelés | eredmény összevetése az elvárással |
| hibajavítás | a hiba okának megszüntetése |

## Vizsgán jól használható megfogalmazás

> A szoftverteszt kiértékelése során a tényleges eredményt összehasonlítjuk a várt eredménnyel.  
> Ha a kettő megegyezik, a teszt sikeres, ha eltérés van, a teszt sikertelen, és a hibát vagy rendellenességet dokumentálni kell.  
> A megfelelő kiértékelés segíti a hibakövetést, a minőség mérését és a további fejlesztési döntéseket.

## Gyakori vizsgahibák

- A teszt futtatását összekeverni a kiértékeléssel.
- Nem megemlíteni a várt eredményt.
- A hibát automatikusan fejlesztői hibának nevezni környezetvizsgálat nélkül.
- Kihagyni a dokumentálás szerepét.

## Gyors önellenőrzés

1. Mi a teszt kiértékelésének alapja?
2. Mikor sikeres egy teszt?
3. Mit kell dokumentálni sikertelen tesztnél?
4. Miért fontos az objektív összehasonlítás?
5. Mi a különbség kiértékelés és hibajavítás között?

## Rövid válaszok az önellenőrzéshez

1. A várt és tényleges eredmény összevetése
2. Ha egyeznek
3. Eltérés, körülmények, státusz, hiba leírása
4. Mert így megbízhatóbb a minőségértékelés
5. Az egyik értékel, a másik javít

## Források

1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos forrás a teszteredmények kiértékeléséhez, hibadokumentáláshoz és tesztfolyamat-alapokhoz.

2. GitHub Docs - About continuous integration with GitHub Actions  
   https://docs.github.com/en/actions/about-github-actions/about-continuous-integration-with-github-actions  
   Használat: modern, hivatalos példa arra, hogyan jelennek meg és értékelhetők a teszteredmények a gyakorlatban.

Megnyitva: `2026-04-09`
