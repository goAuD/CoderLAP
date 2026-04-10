# Frame

## Gyors vizuális kép

| Fogalom | Állapot | Mire való? |
|---|---|---|
| `frame` | elavult | régi, több keretes oldalfelosztás |
| `frameset` | elavult | kereteket tartalmazó dokumentum |
| `iframe` | ma is használatos | másik oldal beágyazása az oldalon belül |

## Mi volt a régi frame-rendszer?

A klasszikus `frame`-es HTML-megoldásnál egy oldal több külön részre oszlott, és ezek külön dokumentumokat töltöttek be.

Ez régen hasznosnak tűnt navigációhoz és oldalfelosztáshoz, de sok problémát okozott:

- rossz használhatóság
- nehézkes bookmarkolás
- gyengébb keresőbarátság
- akadálymentességi gondok
- bonyolultabb kezelés

Ezért a modern weben ezt már nem tekintik jó gyakorlatnak.

## Mi az az `iframe`?

Az `iframe` (`inline frame`) egy HTML-elem, amely egy másik dokumentumot ágyaz be az aktuális oldalba.

Tipikus példák:

- videóbeágyazás
- térképbeágyazás
- külső widget
- dokumentumnézet

Példa:

```html
<iframe src="https://example.com" title="Pelda"></iframe>
```

## Miért kell óvatosan használni?

Mert az `iframe` hasznos, de nem ingyenes megoldás.

Kockázatok és szempontok:

- biztonság
- teljesítmény
- eltérő tartalomforrások kezelése
- hozzáférhetőség
- reszponzív megjelenítés

Ezért gyakran fontos a `sandbox` és más korlátozó attribútumok használata.

## Mikor jó választás?

- ha külső szolgáltatást kell beágyazni
- ha elkülönített tartalmat kell megjeleníteni
- ha integrációs célból kész komponens érkezik

## Mikor nem jó választás?

- ha a teljes oldalstruktúrát erre építenénk
- ha egyszerű HTML/CSS-sel is megoldható
- ha a beágyazott tartalom miatt romlik a teljesítmény vagy a használhatóság

## Frame és iframe: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| `frame` | régi, elavult keretes megoldás |
| `frameset` | a régi keretkiosztó elem |
| `iframe` | modern, beágyazó elem |

## Vizsgán jól használható megfogalmazás

> A frame fogalom a régi HTML-ben több keretre osztott oldalakat jelentett, de ez a megoldás ma már elavult.  
> A modern weben helyette az `iframe` használható, amellyel egy másik dokumentumot lehet az aktuális oldalba beágyazni.  
> Az `iframe` hasznos lehet például videók vagy külső szolgáltatások megjelenítésére, de biztonsági és használhatósági szempontból körültekintően kell alkalmazni.

## Gyakori vizsgahibák

- A régi `frame` és a modern `iframe` összekeverése.
- Azt állítani, hogy a frame ma is ajánlott alapoldalszerkezet.
- Nem megemlíteni az elavultságot.
- Nem beszélni a biztonsági szempontokról.

## Gyors önellenőrzés

1. Mi a különbség `frame` és `iframe` között?
2. Miért számít a régi frame-rendszer elavultnak?
3. Mire használható az `iframe`?
4. Miért kell figyelni a biztonságra?
5. Mondj két tipikus beágyazási példát.

## Rövid válaszok az önellenőrzéshez

1. A `frame` régi és elavult, az `iframe` modern beágyazó elem
2. Mert rosszabb használhatóságot és technikai problémákat okoz
3. Másik oldal vagy külső tartalom beágyazására
4. Mert külső tartalom kerül az oldalba
5. Videó és térkép

## Források

1. MDN - `<iframe>`: The Inline Frame element  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe  
   Használat: az `iframe` modern, hivatalos fejlesztői referenciája.

2. WHATWG HTML Standard - The `iframe` element  
   https://html.spec.whatwg.org/multipage/iframe-embed-object.html#the-iframe-element  
   Használat: szabványi háttér az `iframe` működéséhez.

3. MDN - `<frameset>`  
   https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/frameset  
   Használat: a régi frame-rendszer elavult státuszának hivatalos bemutatása.

Megnyitva: `2026-04-08`
