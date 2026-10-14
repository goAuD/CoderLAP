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

## Ugyanaz a szállításidíj-szabály két nézőpontból

A követelmény: a nemnegatív, egész centben megadott rendelési összegnél 50 EUR-tól ingyenes a szállítás, alatta 5 EUR. Érvénytelen összegre hiba jár. Black-box tervezésnél a szabályból választunk: 0, 4 999, 5 000 és 5 001 cent, valamint negatív és törtszám. A határ közvetlen környezetének vizsgálata határérték-elemzés.

<!-- example:run -->
```javascript
function deliveryFee(totalCents) {
  if (!Number.isInteger(totalCents) || totalCents < 0) {
    throw new RangeError("invalid total");
  }
  return totalCents >= 5000 ? 0 : 500;
}

for (const total of [0, 4999, 5000, 5001]) {
  console.log(total, deliveryFee(total));
}
for (const total of [-1, 1.5]) {
  try {
    deliveryFee(total);
  } catch (error) {
    console.log(total, error.name);
  }
}
```

```text
0 500
4999 500
5000 0
5001 0
-1 RangeError
1.5 RangeError
```

White-box nézőpontból a kód elágazásait is követjük: a bemeneti ellenőrzés elfogadó és elutasító eredményét, majd a díjválasztás két ágát. Áglefedettség és feltétellefedettség külön mérték; egy összetett feltétel minden részének vizsgálatához további esetek is szükségesek lehetnek.

A 100%-os lefedettség a választott szerkezeti mérőszámról szól, nem a teljes helyesség bizonyítása. A követelmények ellenőrzése mutatja meg például, hogy valóban 50 EUR volt-e a kívánt határ.

## Vizsgán jól használható megfogalmazás

> A black-box tesztelés során a rendszer külső viselkedését vizsgáljuk
> a bemenetek és kimenetek alapján,
> anélkül hogy a belső megvalósítást részletesen figyelembe vennénk.  
> A white-box tesztelés ezzel szemben a belső szerkezetre, például elágazásokra, feltételekre és kódutakra is épít.  
> A két megközelítés nem egymás helyett, hanem egymást kiegészítve használható.

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

- [ISTQB: CTFL Syllabus v4.0.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)  
  Statikus és dinamikus tesztelés, teszttervezési technikák és lefedettség.

A bővítés forrásai ellenőrizve: `2026-10-14`.

1. ISTQB CTFL Syllabus v4.0.1  
   https://www.istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf  
   Használat: hivatalos, korszerű alapforrás a black-box és white-box tesztelés fogalmaihoz.

2. ISTQB Standard Glossary of Terms Used in Software Testing  
   https://api.glossary.istqb.org/storage/help/DavkaLpvYMRH8Qu6LWaJxSPu7qKDHf9LpUgHTP1F.pdf  
   Használat: hivatalos fogalmi háttér a teszttípusok meghatározásához.

Megnyitva: `2026-04-08`
