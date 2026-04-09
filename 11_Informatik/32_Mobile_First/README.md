# Mobile First

## Lényeg 30 másodpercben

A **mobile first** olyan tervezési és fejlesztési stratégia, amelynél először a **mobil nézetet** készítjük el, és utána bővítjük nagyobb kijelzőkre.

Röviden:

- először a legkisebb képernyőre tervezünk
- csak a szükséges elemekkel indulunk
- majd fokozatosan bővítjük a felületet

## Gyors vizuális kép

| Sorrend | Mit jelent? |
|---|---|
| 1. mobil | tartalmi lényeg, egyszerű layout |
| 2. tablet | több hely, bővítés |
| 3. desktop | további funkciók és összetettebb elrendezés |

## Miért jó a mobile first?

Mert rákényszerít arra, hogy:

- a lényegre koncentráljunk
- egyszerű, tiszta felületet tervezzünk
- ne zsúfoljuk túl az oldalt

Ez sokszor jobb eredményt ad, mint amikor egy nagy desktop oldalt próbálunk később "összenyomni".

## Hogyan működik technikailag?

Gyakori megközelítés:

- alap CSS a mobil nézethez
- nagyobb nézetekre `min-width` alapú media query-k

Tehát:

- először az alap megoldás készül
- majd fokozatosan hozzáadjuk a bővítéseket

## Mobile first és responsive: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| mobile first | tervezési stratégia |
| responsive | az alkalmazkodó végeredmény |

## Miért fontos ma?

- a mobilhasználat nagyon erős
- sok felhasználó először telefonról érkezik
- a teljesítmény és egyszerűség mobilon különösen kritikus

## Mire kell figyelni?

- A mobile first nem azt jelenti, hogy desktopra már nem is kell jól tervezni.
- A mobil nézetben priorizálni kell a tartalmat.
- A teljesítmény és a navigáció kulcskérdés.
- A fokozatos bővítés logikáját következetesen kell használni.

## Vizsgán jól használható megfogalmazás

> A mobile first olyan webtervezési stratégia, amely a fejlesztést a legkisebb kijelzőre optimalizált nézettel kezdi, majd onnan bővíti a felületet nagyobb eszközökre.  
> Előnye, hogy a tartalom és funkcionalitás prioritása tisztábban látszik, és a felület általában egyszerűbb, gyorsabb és használhatóbb lesz mobilon is.

## Gyakori vizsgahibák

- A mobile firstet összekeverni a responsive webdesignnal.
- Azt hinni, hogy csak mobilra készítünk oldalt.
- Nem megemlíteni a tartalmi priorizálás szerepét.
- Nem beszélni a fokozatos bővítésről.

## Gyors önellenőrzés

1. Mi a mobile first lényege?
2. Miért jobb ez sokszor, mint a desktopról indulás?
3. Mi a kapcsolata a responsive designnal?
4. Mit kell először eldönteni mobile firstnél?
5. Miért fontos a teljesítmény?

## Rövid válaszok az önellenőrzéshez

1. Mobilról indulunk és onnan bővítünk
2. Mert a lényegre kényszerít
3. A mobile first stratégia, a responsive a megvalósuló alkalmazkodás
4. Mi a legfontosabb tartalom és funkció
5. Mert mobilon különösen érzékeny a felhasználó rá

## Források

1. MDN - Mobile First  
   https://developer.mozilla.org/en-US/docs/Glossary/Mobile_First  
   Használat: rövid, pontos fogalmi meghatározás.

2. MDN - Responsive design  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design  
   Használat: technikai háttér a mobile-firstből épített reszponzív megoldásokhoz.

3. web.dev - Learn Design  
   https://web.dev/learn/design/  
   Használat: modern gyakorlati irányelvek mobilközpontú webes tervezéshez.

Megnyitva: `2026-04-08`
