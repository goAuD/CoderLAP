# Mobile Webseiten

## Gyors vizuális kép

| Fontos szempont | Példa |
|---|---|
| kis kijelző | egyszerűbb layout |
| érintés | nagyobb gombok |
| mobilnet | gyorsabb betöltés |
| olvashatóság | megfelelő betűméret |

## Mi számít mobil weboldalnak?

Olyan oldal, amely:

- mobilon is olvasható
- alapméreten is jól olvasható, és szükség esetén nagyítható
- a navigáció könnyen kezelhető ujjal
- a teljesítmény elfogadható

## Régi és modern megközelítés

| Megközelítés | Jelentés |
|---|---|
| külön mobil oldal | pl. `m.pelda.hu` |
| reszponzív oldal | ugyanaz az oldal alkalmazkodik |

Ma a gyakorlatban általában a **reszponzív** megoldás az ajánlott.

## Mire kell figyelni mobil oldalaknál?

- kis képernyő
- érintéses használat
- változó hálózati minőség
- kisebb figyelmi idő
- gyors betöltés

## Tipikus jó megoldások

- nagyobb kattintható felületek
- egyszerűbb navigáció
- jól tördelődő tartalom
- optimalizált képek
- rövidebb, lényegre törő felület

## Mobile website és natív app: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| mobil weboldal | böngészőben fut |
| natív mobilapp | operációs rendszerre telepített alkalmazás |

## Mobilon valós feladatot próbálunk végig

Egy bejelentkezési űrlapot nem csak keskeny ablakkal ellenőrzünk. A képernyőn
megjelenő billentyűzet mellett is elérhetőnek kell maradnia a mezőnek, a
hibaüzenetnek és a küldésnek. Álló és fekvő nézetben, nagyított szöveggel is
végigpróbáljuk a feladatot. A kézi nagyítást nem tiltjuk le a viewportban.

A WCAG 2.2 AA célméret-követelménye főszabályként `24 × 24` CSS-pixeles
érintési célból indul ki, meghatározott távolsági és egyéb kivételekkel.
Kényelmes mobilkezeléshez gyakran nagyobb, például `44 × 44` CSS-pixeles gombot
választunk. Ez tervezési döntés, nem minden eszközön azonos fizikai méret.
Hoverre épített súgóhoz érintéssel és billentyűzettel használható út is kell.

A kijelző kivágását és az alsó rendszerterületet CSS-ben is figyelembe vehetjük:

```css
.site-footer {
  padding-block-end: max(1rem, env(safe-area-inset-bottom, 0px));
}
```

Ez böngészős CSS-részlet: legalább `1rem` térközt hagy, nagyobb alsó safe area
esetén ahhoz igazodik. A tényleges érték eszköz- és viewportbeállítás-függő.
Egy lebegő gomb elhelyezését külön is ellenőrizzük, hogy ne fedjen tartalmat.

Lassabb hálózatnál kisebb megfelelő kép, előre lefoglalt képhely és érthető
betöltési állapot segít. A telepíthetőség önmagában nem jelent natív appot:
PWA is telepíthető, miközben webes technológiákra épül.

## Vizsgán jól használható megfogalmazás

> A mobil weboldal olyan webes felület,
> amelyet kifejezetten telefonon
> és más kisebb kijelzőn is jól használhatóra terveznek.  
> Fontos szempont a jó olvashatóság, az érintésbarát kezelés,
> a gyors betöltés és a kis képernyőhöz alkalmazkodó elrendezés.  
> A modern gyakorlatban ezt leginkább reszponzív webdesignnal valósítják meg.

## Gyors önellenőrzés

1. Mi a mobil weboldal fő célja?
2. Miért fontos a gyors betöltés?
3. Miért kell nagyobb érintési felület?
4. Mi a különbség a mobil weboldal és a natív app között?
5. Mi a mai tipikus megvalósítási mód?

## Rövid válaszok az önellenőrzéshez

1. Jó használhatóság mobil böngészőben
2. Mert mobilhálózaton és mobilon különösen számít
3. Mert ujjal kell kezelni
4. A mobil weboldal webes környezetben fut; a natív app az adott platform alkalmazásmodelljére épül. Webes PWA is telepíthető.
5. Reszponzív webdesign

## Források

Ellenőrizve: `2026-10-14`.

- [W3C: Target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): 24 CSS-pixel és a követelmény kivételei.
- [MDN: env()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env): safe area környezeti változók.


1. MDN - Responsive design  
   https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design  
   Használat: a mobilbarát webes kialakítás alapjai.

2. web.dev - Learn Design  
   https://web.dev/learn/design/  
   Használat: modern, Google által gondozott útmutató mobil és többeszközös webes tervezéshez.

3. MDN - Responsive Web Design (RWD)  
   https://developer.mozilla.org/en-US/docs/Glossary/Responsive_web_design  
   Használat: a reszponzív szemlélet rövid, pontos definíciója.

Megnyitva: `2026-04-08`
