# Ausgabe eines QR-Codes

## Lényeg 30 másodpercben

A `QR`-kód tartalma a PDF szerint **nem a teljes űrlapadat**, hanem kizárólag:

- `Richtig`
- vagy `Falsch`

Röviden:

- helyes `SV-Nr` esetén `Richtig`
- hibás `SV-Nr` esetén `Falsch`

## Gyors vizuális kép

| Eredmény | QR-kód tartalma |
|---|---|
| érvényes SV-Nr | `Richtig` |
| érvénytelen SV-Nr | `Falsch` |

## Mi a jó megoldás itt?

Egyszerű vizsgamegoldásnál:

- a gombnyomás után eldöntjük a helyességet
- az eredményből generálunk QR-kódot
- a QR-t közvetlenül a böngészőben jelenítjük meg

## Mire kell figyelni?

- ne teljes adatblokkot kódoljunk bele
- ne próbáljunk extra exportot vagy letöltést építeni, ha nem kérik
- a QR generálása csak az ellenőrzés után történjen

## Vizsgán jól használható megfogalmazás

> A feladat szerint a generált QR-kód tartalma kizárólag `Richtig` vagy `Falsch` lehet.  
> Ez azt jelenti, hogy a programnak először el kell döntenie az `SV-Nr` helyességét, majd ennek megfelelően kell létrehoznia a QR-kódot.  
> A legegyszerűbb megoldás egy böngészőben futó JavaScript-alapú QR-generálás.

## Gyakori vizsgahibák

- A teljes nevet és SV-számot beleírni a QR-ba.
- A QR generálást külön logika nélkül csinálni.
- Külső online QR-generátorra támaszkodni helyi library helyett.
- Nem ellenőrizni, hogy a QR valóban a várt szót tartalmazza.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   `../../themenkatalog-applikationsentwicklung-coding-v2-2024.pdf`  
   Használat: a QR-payload pontos elvárásához.

2. qrcode-generator package  
   https://www.npmjs.com/package/qrcode-generator  
   Használat: a helyi, egyszerű böngészős QR-generálás technikai alapjához.

Megnyitva: `2026-04-09`
