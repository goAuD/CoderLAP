# Userinterface

## Gyors vizuális kép

| UI-elem | Feladata |
|---|---|
| gomb | művelet indítása |
| menü | navigáció |
| input mező | adatbevitel |
| ikon | vizuális jelentés |
| visszajelzés | állapot közlése |

## Mi az a user interface?

A felhasználói felület az a fizikai vagy logikai eszközrendszer,
amellyel a felhasználó használni tud egy alkalmazást, eszközt vagy folyamatot.

Webes környezetben ez tipikusan:

- oldalszerkezet
- navigáció
- űrlapok
- gombok
- táblázatok
- állapotjelzések
- hibavisszajelzések

## Miért fontos?

Mert a felhasználó nem a forráskódot látja, hanem a felületet.

Egy jó UI:

- érthető
- következetes
- könnyen kezelhető
- gyorsan megtanulható
- egyértelmű visszajelzést ad

Egy rossz UI:

- zavaró
- lassítja a munkát
- növeli a hibázás esélyét
- csökkenti az elégedettséget

## A jó UI alapelvei

- egyértelműség
- konzisztencia
- átlátható navigáció
- jó olvashatóság
- látható visszajelzés
- hozzáférhetőség

## UI és UX: ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| UI | maga a felület és annak elemei |
| UX | a teljes felhasználói élmény |

A UI a kezelhető felület, beleértve a billentyűzetes és segítő technológiás használatot is. A UX a teljes használati élményt és hatékonyságot vizsgálja.

## Mire kell figyelni fejlesztőként?

- A felület legyen érthető első ránézésre.
- A hibákhoz legyen világos hibaüzenet.
- Az űrlapok legyenek logikusak.
- A mobil és desktop nézet eltéréseit tervezni kell.
- Az akadálymentesség nem opcionális extra, hanem minőségi követelmény.

## Egy kis felület, teljes visszajelzéssel

A következő HTML-részletet egy böngészőben megnyitott dokumentum `body` részébe
tehetjük. Csak megjelenít egy célt, nem menti adatbázisba:

```html
<form id="goal-form">
  <label for="minutes">Lernzeit in Minuten (1 bis 120)</label>
  <input id="minutes" name="minutes" type="number" min="1" max="120" required>
  <button type="submit">Lernziel anzeigen</button>
</form>
<p id="goal-status" role="status"></p>
<script>
  const form = document.querySelector("#goal-form");
  const minutes = document.querySelector("#minutes");
  const status = document.querySelector("#goal-status");
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    status.textContent = `Lernziel: ${minutes.valueAsNumber} Minuten`;
  });
</script>
```

`25` beírása és a gomb aktiválása után `Lernziel: 25 Minuten` jelenik meg.
Üres mezőt, `0` vagy `121` értéket a böngésző normál űrlapküldése visszautasít;
ekkor a `submit` kezelő nem fut le. Szerverhez küldött adatnál ugyanezeket
a feltételeket szerveroldalon is ellenőrizni kell.

A látható `label` a `for` és `id` egyezése révén a mezőhöz tartozik.
A natív gomb billentyűzettel is aktiválható; nincs kattintható `div`-re szükség.
A `role="status"` a frissülő eredményt segítő technológiának is jelzi.
Az ellenőrzéshez csak Tab, Shift+Tab és Enter használatával is végigmegyünk
az űrlapon, és megőrizzük a látható fókuszjelzést.

Ez UI-feladat: címke, beviteli korlát, művelet és visszajelzés együtt működik.
A teljes UX értékeléséhez azt is vizsgáljuk, érthető-e a cél, mennyi munkát
igényel a megadása, és valóban segíti-e a tanulást.

## Vizsgán jól használható megfogalmazás

> A user interface a rendszer azon része,
> amelyen keresztül a felhasználó kapcsolatba lép
> az alkalmazással vagy eszközzel.  
> Ide tartoznak például a gombok, menük,
> űrlapok, ikonok és visszajelző elemek.  
> Egy jó felhasználói felület érthető, következetes, könnyen kezelhető és támogatja a hibamentes használatot.

## Gyors önellenőrzés

1. Mi a UI lényege?
2. Mondj négy tipikus UI-elemet.
3. Miért fontos a konzisztencia?
4. Mi a különbség UI és UX között?
5. Miért fontos a hozzáférhetőség?

## Rövid válaszok az önellenőrzéshez

1. Az ember és a rendszer közötti felület
2. Gomb, menü, input mező, ikon
3. Mert könnyebbé teszi a használatot
4. UI a felület, UX a teljes élmény
5. Mert többféle felhasználó számára használhatóvá teszi a rendszert

## Források

- [W3C: role=status](https://www.w3.org/WAI/WCAG22/Techniques/aria/ARIA22): a dinamikus állapotüzenet szemantikus jelölése. Ellenőrizve: `2026-10-14`.

Ellenőrizve: `2026-10-14`.

- [W3C WAI: Labeling controls](https://www.w3.org/WAI/tutorials/forms/labels/): látható, programozottan összekapcsolt címkék.


1. NIST CSRC Glossary - User interface  
   https://csrc.nist.gov/glossary/term/user_interface  
   Használat: rövid, hivatalos definíció a UI fogalmára.

2. W3C WAI - Introduction to Web Accessibility  
   https://www.w3.org/WAI/fundamentals/accessibility-intro/  
   Használat: hivatalos háttér ahhoz, hogy a jó felület nemcsak szép, hanem hozzáférhető is.

3. MDN - Accessibility  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility  
   Használat: fejlesztői nézőpontból gyakorlati kapcsolódás a jól tervezett felhasználói felülethez.

Megnyitva: `2026-04-08`
