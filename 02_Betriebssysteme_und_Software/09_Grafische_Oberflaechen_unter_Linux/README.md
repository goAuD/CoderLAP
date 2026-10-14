# Grafische Oberflaechen unter Linux

## Gyors vizuális kép

| Felület    | Jellemző                      |
| ---------- | ----------------------------- |
| GNOME      | letisztult, modern            |
| KDE Plasma | nagyon testreszabható         |
| Xfce       | könnyű, gyors, takarékos      |
| Cinnamon   | hagyományosabb desktop élmény |

## Mi az a grafikus felület Linux alatt?

A grafikus felület az a réteg, amely lehetővé teszi az egérrel, ablakokkal, ikonokkal, menükkel történő munkát.

A felhasználó számára ez látszik például:

- bejelentkezési képernyő
- asztal
- panel vagy tálca
- alkalmazásmenü
- fájlkezelő
- rendszerbeállítások

## Mi az a desktop environment?

Nem csak egy „szép kinézet”, hanem általában egy komplett csomag:

- ablakkezelő
- panel vagy dock
- fájlkezelő
- beállításkezelő
- rendszeralkalmazások
- widgetek vagy kiegészítők

## 1. GNOME

Jellemzői:

- modern, letisztult megközelítés
- áttekinthető felület
- sok disztribúció alapértelmezett vagy gyakori választása

## 2. KDE Plasma

Jellemzői:

- rendkívül testreszabható
- sok beállítási lehetőség
- modern és funkciógazdag

## 3. Xfce

Jellemzői:

- könnyű és gyors
- alacsonyabb erőforrásigény
- hagyományosabb desktop élmény

## 4. Cinnamon

Jellemzői:

- klasszikusabb desktop elrendezés
- felhasználóbarát megközelítés
- sokaknak ismerős Windows-szerű logika

## Miért fontos, hogy Linux alatt többféle felület van?

Mert a Linux világban gyakori a választási szabadság.

Ez azt jelenti, hogy:

- ugyanaz a rendszer más felülettel is használható
- a felhasználó igényhez igazíthatja a környezetet

Például:

- teljesítmény
- egyszerűség
- kinézet
- testreszabhatóság

## Kapcsolódó fogalmak

### Megjelenítési protokoll és kiszolgáló

Az `X11` és a `Wayland` protokollokat ír le a grafikus kliensek és a megjelenítési rendszer közötti kommunikációhoz. Egy Wayland-kiszolgálót **kompozitornak** nevezünk: összerakja a megjelenő képet és kezeli a bemenet továbbítását. A protokoll és a konkrét implementáció külön fogalom.

### Ablakkezelő és bejelentkezéskezelő

Az **ablakkezelő** az ablakok elhelyezésével és viselkedésével foglalkozik. A **display manager** a grafikus bejelentkezést és a munkamenet indítását kezeli. A teljes desktop environment ezeknél több, például panelt, fájlkezelőt és beállításokat is tartalmaz.

## Linux GUI vs Windows / macOS

| Linux                        | Windows / macOS                        |
| ---------------------------- | -------------------------------------- |
| többféle desktop environment | jellemzően egységesebb gyári felület   |
| erős testreszabhatóság       | általában kötöttebb alapélmény         |
| disztribúciótól is függ      | gyártó által szorosabban meghatározott |

## Kidolgozott választás: régebbi tanulói laptop

A feladat böngésző, szövegszerkesztő és terminál használata. Ugyanazon disztribúción kipróbálunk egy könnyebb és egy teljesebb asztali környezetet. Megmérjük a belépés utáni memóriaigényt, majd megnyitjuk ugyanazokat az alkalmazásokat. A böngésző lapjai több erőforrást is igényelhetnek, mint a felületek közötti különbség.

A döntéshez a képernyőméretezést, billentyűzetkiosztást, akadálymentességet és a szükséges képernyőmegosztó működését is kipróbáljuk. Az, hogy egy környezet „könnyű”, relatív tulajdonság, nem garancia az összes feladat sebességére. A disztribúció, desktop environment és Wayland/X11-munkamenet nevét külön rögzítjük a tesztjegyzetben.

## Vizsgán jól használható megfogalmazás

> Linux alatt többféle grafikus felület, más néven desktop environment használható.  
> Ilyen például a GNOME, a KDE Plasma, az Xfce vagy a Cinnamon.  
> Ezek biztosítják az ablakkezelést, a paneleket, a fájlkezelőt és a grafikus beállítási lehetőségeket.  
> A Linux egyik előnye, hogy a felhasználó többféle grafikus környezet közül választhat.

## Gyors önellenőrzés

1. Mi az a desktop environment?
2. Mondj három Linuxos grafikus felületet.
3. Melyik ismert könnyű, erőforrás-takarékos felület?
4. Melyik híres a sok testreszabási lehetőségről?
5. Mit jelent az, hogy Linux alatt többféle grafikus felület használható?

## Rövid válaszok az önellenőrzéshez

1. Komplett grafikus asztali környezet
2. GNOME, KDE Plasma, Xfce, Cinnamon
3. Az **Xfce**
4. A **KDE Plasma**
5. Hogy ugyanaz a Linux-rendszer többféle GUI-val is használható

## Források

1. GNOME Help - Visual overview of GNOME
   https://help.gnome.org/gnome-help/shell-introduction.html
   Használat: GNOME mint grafikus Linux desktop környezet.

2. KDE - Plasma is a Desktop  
   https://kde.org/plasma-desktop/  
   Használat: KDE Plasma hivatalos desktop leírása.

3. Xfce - About  
   https://www.xfce.org/about  
   Használat: Xfce mint könnyű desktop environment.

4. Fedora KDE  
   https://fedoraproject.org/kde/  
   Használat: KDE Plasma Linux desktop környezet modern disztribúciós példája.

5. Linux Mint - Cinnamon
   https://github.com/linuxmint/cinnamon
   Használat: Cinnamon mint fontos Linux desktop felület.

Felülvizsgálva: `2026-10-14`

### A bővítés ellenőrzött forrásai

- [Wayland project](https://wayland.freedesktop.org/): protokoll, kliens és kompozitor.

Ellenőrizve: `2026-10-14`.
