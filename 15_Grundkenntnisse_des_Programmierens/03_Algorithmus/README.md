# Algorithmus

## Lényeg 30 másodpercben

Az **algoritmus** egy egyértelmű, lépésekre bontott megoldási eljárás.

Röviden:

- megmondja, hogyan oldunk meg egy problémát
- ismételhető
- nem csak számítógép, hanem ember is követheti

## Gyors vizuális kép

```text
Bemenet
    -> feldolgozási lépések
    -> eredmény
```

## Mi az algoritmus?

Egy algoritmus:

- véges számú lépésből áll
- jól meghatározott
- végrehajtható
- valamilyen eredményre vezet

Programozásban az algoritmus a megoldás logikája.  
A program ennek konkrét, nyelvi megvalósítása.

## Az algoritmus tipikus jellemzői

| Jellemző | Jelentés |
|---|---|
| egyértelműség | minden lépés világos |
| végesség | nem tart örökké |
| bemenet | lehet adat, amivel dolgozik |
| kimenet | eredményt ad |
| ismételhetőség | újra végrehajtható |

## Miért fontos?

- segít a probléma strukturálásában
- programozási nyelvtől függetlenül leírható
- összehasonlíthatók vele különböző megoldások
- alapja a hatékony programnak

## Algoritmus és program: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| algoritmus | a megoldás logikai leírása |
| program | az algoritmus konkrét kódja egy nyelven |

Ugyanaz az algoritmus több nyelven is megírható.

## Egyszerű példa

Feladat: számok összegzése `1`-től `n`-ig.

Algoritmus:

1. indulj `0` összeggel
2. menj végig `1`-től `n`-ig
3. mindig add hozzá az aktuális számot az összeghez
4. a végén add vissza az összeget

## Hatékonyság röviden

Nemcsak az számít, hogy működik-e, hanem az is, hogy:

- milyen gyors
- mennyi memóriát használ
- nagy adatmennyiségnél hogyan viselkedik

Ezért beszélünk algoritmusok összehasonlításáról is.

## Vizsgán jól használható megfogalmazás

> Az algoritmus egy egyértelmű, véges lépéssorozat, amely egy adott probléma megoldására szolgál.  
> Bemeneteket feldolgoz, és eredményt ad vissza.  
> A programozásban az algoritmus a megoldás logikája, amelyet később egy konkrét programozási nyelven valósítunk meg.

## Gyakori vizsgahibák

- Az algoritmust azonnal kóddal azonosítani.
- Nem megemlíteni a végességet.
- Túl homályosan fogalmazni a lépéseket.
- Kihagyni a bemenet és kimenet szerepét.

## Gyors önellenőrzés

1. Mi az algoritmus lényege?
2. Miben különbözik a programtól?
3. Miért fontos az egyértelműség?
4. Mit jelent az, hogy véges?
5. Miért hasznos ugyanazt a feladatot több algoritmussal is megnézni?

## Rövid válaszok az önellenőrzéshez

1. Egyértelmű megoldási lépéssor
2. Az algoritmus logika, a program konkrét kód
3. Hogy ugyanúgy végrehajtható legyen
4. Hogy a lépéssor véget ér
5. Mert eltérhet a hatékonyságuk

## Források

1. MDN - Algorithm  
   https://developer.mozilla.org/en-US/docs/Glossary/Algorithm  
   Használat: modern, tömör fogalmi meghatározás algoritmushoz.

2. NIST CSRC Glossary - Algorithm  
   https://csrc.nist.gov/glossary/term/algorithm  
   Használat: hivatalos definíciós háttér az algoritmus fogalmához.

Megnyitva: `2026-04-09`
