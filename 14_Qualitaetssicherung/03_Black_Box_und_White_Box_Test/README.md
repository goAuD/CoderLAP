# Black Box und White Box Test

## Gyors vizuális kép

| Teszttípus | Mire fókuszál? |
|---|---|
| black-box | bemenet és kimenet |
| white-box | belső logika, ágak, feltételek, kódszerkezet |

## Mi az a black-box teszt?

Itt a tesztelő azt nézi:

- mit kap bemenetként a rendszer
- milyen kimenetet ad
- megfelel-e a követelményeknek

Nem kell ismernie részletesen a belső megvalósítást.

## Mi az a white-box teszt?

Itt a belső működés is fontos.

A tesztelés alapja lehet:

- vezérlési utak
- elágazások
- feltételek
- ciklusok
- lefedettség

Ehhez általában ismerni kell a kód vagy belső szerkezet működését.

## Mikor hasznos melyik?

### Black-box

- követelmények ellenőrzésére
- funkciók tesztelésére
- felhasználói nézőpontból

### White-box

- kódlogika ellenőrzésére
- lefedettség javítására
- belső hibák megtalálására

## Black-box és white-box: ne állítsd szembe túl mereven

A gyakorlatban sok projekt **mindkettőt** használja, mert:

- a black-box a viselkedést ellenőrzi
- a white-box a belső minőséget és lefedettséget javítja

## Vizsgán jól használható megfogalmazás

> A black-box tesztelés során a rendszer külső viselkedését vizsgáljuk a bemenetek és kimenetek alapján, anélkül hogy a belső megvalósítást részletesen figyelembe vennénk.  
> A white-box tesztelés ezzel szemben a belső szerkezetre, például elágazásokra, feltételekre és kódutakra is épít.  
> A két megközelítés nem egymás helyett, hanem egymást kiegészítve használható.

## Gyakori vizsgahibák

- Azt állítani, hogy a black-box teszt nem is tesztelés.
- A white-box tesztet kizárólag unit testtel azonosítani.
- Nem megemlíteni a belső szerkezet ismeretét.
- A két módszert teljesen egymás ellenpontjaként kezelni.

## Gyors önellenőrzés

1. Mi a black-box teszt lényege?
2. Mi a white-box teszt lényege?
3. Melyiknél fontos a belső logika ismerete?
4. Melyik nézi inkább a követelmények szerinti viselkedést?
5. Miért jó együtt használni őket?

## Rövid válaszok az önellenőrzéshez

1. Külső viselkedés vizsgálata
2. Belső logika és szerkezet vizsgálata
3. A white-boxnál
4. A black-boxnál
5. Mert másfajta hibákat tárnak fel

## Források

1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos, korszerű alapforrás a black-box és white-box tesztelés fogalmaihoz.

2. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Használat: hivatalos fogalmi háttér a teszttípusok meghatározásához.

Megnyitva: `2026-04-08`
