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

## Beágyazás minimális jogosultsággal

Ez a HTML-részlet helyben is megnyitható, és nem tölt be külső szolgáltatást:

```html
<iframe
  title="Isolierte Textvorschau"
  sandbox
  srcdoc="<p>Nur lesen</p>">
</iframe>
```

A keretben a `Nur lesen` szöveg jelenik meg. A `title` a keret célját nevezi meg
segítő technológiák számára. A `srcdoc` itt rögzített mintatartalom; felhasználói
HTML beszúrásához külön biztonságos tartalomkezelés szükséges. Az üres `sandbox`
a korlátozásokat bekapcsolja: például nincs szkriptfuttatás és űrlapküldés.
Csak a valóban szükséges képességet engedjük vissza.

Az `allow-scripts` és `allow-same-origin` együttes engedélyezése azonos eredetű
tartalomnál alááshatja az elkülönítést. A beágyazott oldal saját szervere
`Content-Security-Policy: frame-ancestors` fejléccel korlátozhatja, ki ágyazhatja
be; ezt az oldal használója nem írhatja felül egy HTML-attribútummal.

A régi teljes oldalas `frameset` elrendezést CSS Grid/Flexbox és normál
navigáció váltja ki. Az `iframe` külön dokumentum beágyazására való, nem az
elavult frame-es oldalfelosztás általános utódja. Külső beágyazásnál a hálózati
adatküldést és a betöltési költséget is megvizsgáljuk.

## Vizsgán jól használható megfogalmazás

> A frame fogalom a régi HTML-ben több keretre osztott oldalakat jelentett, de ez a megoldás ma már elavult.  
> Másik dokumentum beágyazására a modern weben az `iframe` használható,
> amellyel egy másik dokumentumot lehet az aktuális oldalba beágyazni.  
> Az `iframe` hasznos lehet például videók
> vagy külső szolgáltatások megjelenítésére,
> de biztonsági és használhatósági szempontból körültekintően kell alkalmazni.

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

Ellenőrizve: `2026-10-14`.

- [MDN: iframe](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe): sandbox, srcdoc, címke és eredet.
- [MDN: frame-ancestors](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/frame-ancestors): a beágyazást a tartalom szervere is korlátozhatja.


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
