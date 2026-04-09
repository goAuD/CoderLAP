# Standardbibliothek

## Lényeg 30 másodpercben

A **standard library** olyan előre elkészített, a nyelvhez vagy platformhoz tartozó függvények, osztályok és modulok gyűjteménye, amelyeket a fejlesztő újra felhasználhat.

Röviden:

- nem kell mindent nulláról megírni
- közös, megbízható alapot ad
- gyorsabbá teszi a fejlesztést

## Gyors vizuális kép

| Standard library rész | Példa |
|---|---|
| szövegkezelés | string műveletek |
| fájlkezelés | beolvasás, írás |
| dátum és idő | időkezelés |
| adatszerkezetek | listák, szótárak, gyűjtemények |
| matematikai műveletek | számítások |

## Mi az a standard library?

Minden komolyabb programozási nyelvhez tartozik egy alapkönyvtár vagy szabványos könyvtárkészlet.

Ez tipikusan biztosít:

- alapműveleteket
- gyakran használt eszközöket
- jól dokumentált, közös megoldásokat

## Miért fontos?

- gyorsítja a fejlesztést
- csökkenti a fölösleges saját megoldások számát
- sokszor jobban tesztelt és stabilabb, mint a házilag írt alternatíva
- egységesebb kódot eredményezhet

## Mire jó a gyakorlatban?

Például:

- fájlokat kezelni
- dátumokat számolni
- hálózati műveleteket végezni
- adatokat átalakítani
- gyűjteményekkel dolgozni

## Standard library és külső csomag: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| standard library | a nyelv alap része vagy hivatalos csomagja |
| külső könyvtár | külön telepített, külső csomag |

## Miért nem jó mindent saját kézzel megírni?

- lassabb
- hibásabb lehet
- nehezebb karbantartani
- fölöslegesen duplikáljuk azt, ami már készen és jól megoldva létezik

## Vizsgán jól használható megfogalmazás

> A standard library a programozási nyelvhez tartozó szabványos függvények, modulok és osztályok gyűjteménye.  
> Célja, hogy a fejlesztő gyakori feladatokat kész megoldásokkal tudjon megvalósítani, például fájlkezelést, adatkezelést, szövegfeldolgozást vagy matematikai műveleteket.  
> A standard library használata gyorsabb, egységesebb és megbízhatóbb fejlesztést tesz lehetővé.

## Gyakori vizsgahibák

- A standard library-t bármilyen külső csomagnak nevezni.
- Azt hinni, hogy csak “kényelmi extra”.
- Nem megemlíteni a fejlesztési idő csökkenését.
- A nyelv és a platform alapkönyvtárát összekeverni a projekt-specifikus kóddal.

## Gyors önellenőrzés

1. Mi az a standard library?
2. Miért hasznos?
3. Mondj három tipikus területet, amit lefedhet.
4. Mi a különbség standard library és külső csomag között?
5. Miért nem érdemes mindent saját kézzel újraírni?

## Rövid válaszok az önellenőrzéshez

1. A nyelvhez tartozó hivatalos alapkönyvtár
2. Mert gyorsabb és megbízhatóbb fejlesztést ad
3. Fájlkezelés, dátum, adatszerkezetek
4. Az egyik alapból adott, a másik külön telepített
5. Mert lassabb és hibásabb lehet

## Források

1. Python Docs - The Python Standard Library  
   https://docs.python.org/3/library/index.html  
   Használat: hivatalos elsődleges forrás a standard library fogalmához.

2. MDN - Standard built-in objects  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects  
   Használat: hivatalos, modern példa arra, hogyan jelenik meg egy nyelv beépített alapkönyvtára a gyakorlatban.

Megnyitva: `2026-04-09`
