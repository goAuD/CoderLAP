# QR-Code Pruefung und Tools

## Gyors vizuális kép

```text
Űrlap kitöltése
    -> QR generálás
    -> scannerrel beolvasás
    -> tartalom ellenőrzése
```

## Mit javasol a PDF?

A PDF külön említi:

- `CodeTwo QR Code Desktop Reader`

Ez arra jó, hogy:

- képernyőn megjelenő QR-kódot is ellenőrizni lehessen
- telefon nélkül is visszaolvasható legyen a generált kód

> **Fontos (2026):** A `CodeTwo QR Code Desktop Reader` a gyártó oldalán **deprecated** státuszú — már nem elérhető
> letöltésre, és nem kap frissítéseket. A PDF még ezt a toolt nevezi meg, ezért vizsgán érdemes ismerni a nevét, de a
> gyakorlatban alternatív QR-olvasóra is szükség lehet, például mobiltelefon kamerája, böngészős online dekóder vagy más
> ingyenes desktop scanner.

## Mit kell ellenőrizni?

- tényleg olvasható-e a QR
- a tartalom pontosan `Richtig` vagy `Falsch`
- a valid és invalid tesztpéldáknál jól vált-e

## Egyszerű ellenőrzési lépések

1. futtasd a mintamegoldást
2. adj meg érvényes `SV-Nr`-t
3. olvasd vissza a QR-t
4. ismételd meg érvénytelen `SV-Nr`-rel
5. ellenőrizd, hogy az eredmény helyes-e

## Vizsgán jól használható megfogalmazás

> A generált QR-kód helyességét külön ellenőrizni kell egy olvasóeszközzel vagy desktop scannerrel.  
> A cél annak igazolása, hogy a kód valóban a kívánt tartalmat, vagyis `Richtig` vagy `Falsch` szöveget tartalmazza.  
> A PDF ehhez példaként a `CodeTwo QR Code Desktop Reader` használatát említi.

## Gyakori vizsgahibák

- A QR-t nem ellenőrizni visszaolvasással.
- Csak a megjelenésre hagyatkozni.
- Érvényes és érvénytelen mintaszámmal nem is kipróbálni.
- A QR olvashatóságát nem ellenőrizni kisebb képernyőméreten.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Használat: a javasolt tool és az ellenőrzési elv miatt.

2. CodeTwo QR Code Desktop Reader  
   https://www.codetwo.com/freeware/qr-code-desktop-reader/  
   Használat: a PDF-ben említett ellenőrző eszköz hivatalos oldala.

Megnyitva: `2026-04-09`
