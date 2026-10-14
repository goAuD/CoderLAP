# Testkonzepte

## Gyors vizuális kép

| Tesztkoncepció eleme | Kérdés |
|---|---|
| tesztcél | mit akarunk igazolni? |
| tesztszint | hol tesztelünk? |
| teszttípus | mit vizsgálunk? |
| tesztadat | mivel próbáljuk ki? |
| eredménykritérium | honnan tudjuk, hogy jó? |

## Mi az a tesztkoncepció?

Ez egy terv vagy megközelítés arra, hogy a szoftver minőségét hogyan ellenőrizzük.

Tartalmazhatja:

- a tesztelés célját
- a tesztelési stratégiát
- a tesztszinteket
- a teszttípusokat
- az eszközöket
- a felelősségeket

## Fontos tesztszintek

| Szint | Mire fókuszál? |
|---|---|
| unit test | egy kis egységre |
| integration test | egységek együttműködésére |
| system test | teljes rendszerre |
| acceptance test | üzleti / felhasználói elfogadásra |

## Fontos teszttípusok

Például:

- funkcionális teszt
- nem funkcionális teszt
- regressziós teszt
- biztonsági teszt
- használhatósági teszt

## Miért fontos a tesztkoncepció?

- rendszerezi a tesztelést
- csökkenti a kihagyott területek esélyét
- segíti az erőforrás-tervezést
- javítja az átláthatóságot

## Tesztkoncepció és teszteset: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| tesztkoncepció | magasabb szintű megközelítés |
| teszteset | konkrét kipróbálási leírás |

## A kockázatból tesztesetet készítünk

Egy foglalási rendszerben a dupla foglalás és az utolsó hely túlfoglalása fontos
kockázat. Ezekhez különböző szinteken készül bizonyíték:

| Szint | Konkrét ellenőrzés |
|---|---|
| Unit | a férőhely-szabály elfogadja az érvényes darabszámot |
| Integráció | az alkalmazás és az adatbázis együtt őrzi az egyediséget |
| Rendszer | két párhuzamos kérés közül csak egy kapja az utolsó helyet |
| Elfogadás | a felhasználó érti a visszaigazolást és a betelt állapotot |

Ha a megengedett darabszám egész `1..30`, egy érvényes osztály képviselője
például 12. A határokhoz `0, 1, 2, 29, 30, 31` értékeket választunk.
Tört szám, szöveg és hiányzó érték további bemeneti csoportok. Ezzel konkrét
feltevéseket ellenőrzünk, nem minden lehetséges bemenetet próbálunk ki.

A **black-box** nézőpont a szerződésből vezet le eseteket. A **white-box** a belső
szerkezetet is használja, például mindkét elágazási kimenetet bejárja. A lefedettség
segít a hiányok keresésében, de még 100% kódlefedettség sem bizonyítja, hogy a
követelmény helyes vagy minden fontos állapotkombinációt kipróbáltunk.

## Vizsgán jól használható megfogalmazás

> A tesztkoncepció azt határozza meg, hogyan kívánjuk a szoftver minőségét ellenőrizni.  
> Leírja a tesztelés célját, a tesztszinteket, a teszttípusokat, a használt módszereket és az eredményértékelés  
> alapját.  
> A jó tesztkoncepció biztosítja, hogy a tesztelés ne véletlenszerűen, hanem tudatos és tervezett módon történjen.

## Gyors önellenőrzés

1. Mi az a tesztkoncepció?
2. Milyen elemeket tartalmazhat?
3. Mi a különbség tesztkoncepció és teszteset között?
4. Milyen tesztszinteket ismersz?
5. Miért fontos előre megtervezni a tesztelést?

## Rövid válaszok az önellenőrzéshez

1. A tesztelés megközelítésének leírása
2. Célok, szintek, típusok, eszközök, felelősségek
3. Az egyik stratégia, a másik konkrét ellenőrzés
4. Unit, integration, system, acceptance
5. Mert így átláthatóbb és teljesebb lesz

## Források

Ellenőrizve: `2026-10-14`.

- [ISTQB CTFL 4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf): tesztszintek és teszttervezési technikák.


1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos elsődleges forrás a tesztelési alapfogalmakhoz, tesztszintekhez és teszttípusokhoz.

2. OWASP Web Security Testing Guide  
   https://owasp.org/www-project-web-security-testing-guide/  
   Használat: hivatalos, modern példa arra, hogyan jelenik meg a tesztkoncepció egy konkrét tesztelési területen.

Megnyitva: `2026-04-09`
