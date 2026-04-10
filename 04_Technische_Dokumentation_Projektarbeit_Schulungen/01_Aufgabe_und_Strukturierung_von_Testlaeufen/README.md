# Aufgabe und Strukturierung von Testläufen

## Gyors vizuális kép

| Elem | Mit jelent? |
|---|---|
| tesztcél | mit akarunk ellenőrizni |
| tesztkörnyezet | hol fut a teszt |
| tesztadat | mivel végezzük a tesztet |
| tesztlépések | mit kell végrehajtani |
| várt eredmény | mi számít helyes működésnek |
| tényleges eredmény | mi történt valójában |
| státusz | `pass`, `fail`, `blocked` stb. |

## Mi a tesztfutás feladata?

A tesztfutás célja:

- hibák megtalálása
- a követelmények ellenőrzése
- a működés igazolása
- a minőség értékelése
- döntéstámogatás kiadás vagy átadás előtt

Egyszerűen:

- nem elég azt mondani, hogy „működik”
- ezt ellenőrizhető, dokumentált módon kell bizonyítani

## Mit kell előkészíteni egy tesztfutáshoz?

### 1. Tesztcél

Például:

- a bejelentkezés működésének ellenőrzése
- a keresés validálása
- az adatbázis-kapcsolat ellenőrzése

### 2. Tesztkörnyezet

Meg kell adni:

- rendszerverzió
- eszköz vagy platform
- böngésző
- operációs rendszer
- adatbázis
- hálózati feltételek

### 3. Tesztadatok

Például:

- tesztfelhasználó
- mintaadatbázis
- érvényes és érvénytelen adatok

### 4. Tesztesetek és lépések

Pontosan rögzíteni kell:

- mit csinál a tesztelő
- milyen sorrendben
- milyen bemenettel

### 5. Várt eredmény

Ez mondja meg, hogy:

- mit tekintünk helyes működésnek

## Hogyan érdemes strukturálni egy tesztfutást?

## 1. Azonosítás

Legyen egyértelmű:

- tesztfutás neve vagy azonosítója
- dátum
- felelős személy
- tesztelt verzió

## 2. Cél és hatókör

Le kell írni:

- mit tesztelünk
- mit nem tesztelünk
- mi a teszt célja

## 3. Előfeltételek

Példák:

- felhasználó létrehozva
- adatbázis betöltve
- rendszer fut
- hálózat elérhető

## 4. Tesztlépések

Ezek legyenek:

- sorrendben
- egyértelműek
- ismételhetők

## 5. Eredmények és státusz

A teszt végén dokumentálni kell:

- tényleges eredmény
- `pass`
- `fail`
- `blocked`
- megjegyzések
- hibajegy hivatkozás

## Tipikus tesztfutási státuszok

| Státusz | Jelentés |
|---|---|
| `ready to run` | futtatásra kész |
| `pass` | sikeres |
| `fail` | hibás eredmény |
| `blocked` | nem futtatható valamilyen akadály miatt |
| `skipped` | szándékosan kihagyva |

## Mire kell figyelni?

- a várt eredmény legyen egyértelmű
- a tesztlépések legyenek reprodukálhatók
- a környezet legyen dokumentált
- az eredményeket pontosan rögzíteni kell
- hibánál legyen bizonyíték vagy hivatkozás

## Példa egyszerű tesztfutásra

### Tesztcél

Bejelentkezés ellenőrzése helyes adatokkal

### Előfeltétel

Tesztfelhasználó létezik

### Tesztlépések

1. Nyisd meg a login oldalt.
2. Add meg a felhasználónevet.
3. Add meg a jelszót.
4. Kattints a bejelentkezés gombra.

### Várt eredmény

A rendszer belépteti a felhasználót és megjelenik a dashboard.

### Tényleges eredmény

A felhasználó belépett, dashboard megjelent.

### Státusz

`pass`

## Vizsgán jól használható megfogalmazás

> A tesztfutás feladata annak ellenőrzése, hogy egy funkció vagy rendszer a követelményeknek megfelelően működik-e.  
> Egy jól strukturált tesztfutás tartalmazza a tesztcélt, a tesztkörnyezetet, a tesztadatokat, a tesztlépéseket, a várt eredményt, a tényleges eredményt és a teszt státuszát.  
> A tesztfutás dokumentálása fontos a hibák követéséhez, a minőségbiztosításhoz és az átadás előtti döntésekhez.

## Gyakori vizsgahibák

- Nincs egyértelmű várt eredmény.
- A tesztlépések túl homályosak.
- Nincs dokumentálva a környezet.
- Hibát észlelnek, de nem rögzítik pontosan.
- A `blocked` és `fail` státuszt összekeverik.

## Gyors önellenőrzés

1. Mi a tesztfutás célja?
2. Mit kell megadni a várt eredményben?
3. Miért fontos a tesztkörnyezet rögzítése?
4. Mi a különbség a `fail` és a `blocked` között?
5. Milyen adatokat kell minimálisan dokumentálni egy tesztfutásnál?

## Rövid válaszok az önellenőrzéshez

1. A működés ellenőrzése és dokumentálása
2. Hogy mi számít helyes működésnek
3. Mert ettől ismételhető és visszakövethető a teszt
4. `fail` = hibás eredmény, `blocked` = a teszt nem futtatható
5. Cél, környezet, lépések, tesztadatok, várt és tényleges eredmény, státusz

## Források

1. ISTQB CTFL Syllabus v3.1.1  
   https://istqb.org/wp-content/uploads/2024/11/ISTQB-CTFL_Syllabus_2018_v3.1.1.pdf  
   Használat: test execution, logging, expected vs actual result, test execution work products.

2. Azure DevOps Test Plans - Manage test runs  
   https://learn.microsoft.com/en-us/azure/devops/test/test-runs  
   Használat: modern, hivatalos példa a test run fogalmára, metaadatokra és státuszokra.

3. Azure DevOps - Publish Test Results task  
   https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/test/publish-test-results  
   Használat: teszteredmények dokumentálása és riportolása modern folyamatokban.

Megnyitva: `2026-04-08`
