# Mobile First

## Gyors vizuális kép

| Sorrend | Mit jelent? |
|---|---|
| 1. mobil | tartalmi lényeg, egyszerű layout |
| 2. tablet | több hely, bővítés |
| 3. desktop | több helyet kihasználó elrendezés, ugyanazok az alapfeladatok |

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

## Feladatból induló tervezés: egy téma megkeresése

Egy tanuló telefonon is témát keres, megnyitja a magyarázatot, majd visszatér
a találatokhoz. Ez az alapfeladat desktopon is ugyanaz. Először ezt tesszük
kényelmesen használhatóvá: látható kereső, érthető címek, működő visszalépés és
olvasható tartalom. Több helyen később mellé kerülhet egy állandó oldalsáv.
A mobilváltozatból ezért nem vesszük ki az alapvető funkciókat.

**Böngészős CSS-részlet:** a `.navigation` elemen belül normál HTML-linkek
vannak. A dokumentum szabványos viewport metatagot használ.

```css
.navigation {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

@media (min-width: 48rem) {
  .navigation { flex-direction: row; flex-wrap: wrap; }
}
```

Alapból a linkek egymás alatt állnak. `48rem` széles viewporttól egymás mellé
kerülnek, és szükség esetén új sorba törnek. A `48rem` ebben a tervben választott
töréspont, nem minden tabletre érvényes határ. A CSS pixel és a készülék fizikai
képpontja sem ugyanaz; nagyításkor a rendelkezésre álló CSS-szélesség változhat.

**Fokozatos fejlesztés:** az alap HTML-link JavaScript nélkül is navigálhat,
majd JavaScript hozzáadhat gyors szűrést vagy animációt. Ettől külön döntés,
hogy az oldal elrendezése mobilról indul. A mobile first önmagában nem bizonyít
jó teljesítményt: a hálózaton átvitt képek és kód mennyiségét is mérjük. Próbáld
ki a feladatot billentyűzettel, 200%-os nagyítással és lassú hálózattal is.

## Vizsgán jól használható megfogalmazás

> A mobile first olyan webtervezési stratégia,
> amely a fejlesztést a legkisebb kijelzőre optimalizált nézettel kezdi,
> majd onnan bővíti a felületet nagyobb eszközökre.  
> Előnye,
> hogy a tartalom és funkcionalitás prioritása tisztábban látszik,
> és a felület általában egyszerűbb,
> gyorsabb és használhatóbb lesz mobilon is.

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

Ellenőrizve: `2026-10-14`.

- [MDN: Responsive web design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design): mobile-first media query, viewport és nagyítható felület.


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
