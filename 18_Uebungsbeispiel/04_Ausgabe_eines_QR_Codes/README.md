# Ausgabe eines QR-Codes

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

## A döntés és a QR-kép külön lépés

A következő böngészős részlet a helyi `vendor/qrcode.js` betöltése után használható.
A `validation` a teljes SV-ellenőrzés eredménye, a `qrCodeBox` a kimeneti HTML-elem:

```javascript
const payload = validation.isValid ? "Richtig" : "Falsch";
const qr = qrcode(0, "M");
qr.addData(payload);
qr.make();
qrCodeBox.innerHTML = qr.createSvgTag(6);
```

A `0` automatikus QR-méretválasztást, az `M` hibajavítási szintet jelent.
A `make()` építi meg a kódot. A megjelenítő megtartja a könyvtár alapértelmezett,
négy modul széles üres szegélyét; ez segíti a mintázat elkülönítését a környezettől.
A részlet feltételezi az előzetes kötelezőmező-ellenőrzést.

A QR-payload pontosan egy szó. A név és az SV-szám nem kerül bele,
és a QR-generálásnak nincs szüksége külső hálózati kérésre.
A hibajavítás a QR olvashatóságát segíti, a benne tárolt állítás valódiságát nem igazolja.
Szerkesztéskor a régi eredményt elrejtjük, hogy az új bevitel mellett ne maradjon régi QR.

Forrás: [qrcode-generator API](https://kazuhikoarase.github.io/qrcode-generator/js/).

## Vizsgán jól használható megfogalmazás

> A feladat szerint a generált QR-kód tartalma kizárólag `Richtig` vagy `Falsch` lehet.  
> Ez azt jelenti, hogy a programnak először el kell döntenie az `SV-Nr` helyességét, majd ennek megfelelően kell  
> létrehoznia a QR-kódot.  
> A legegyszerűbb megoldás egy böngészőben futó JavaScript-alapú QR-generálás.

## Gyors önellenőrzés

1. Miért kell előbb eldönteni az eredményt?
2. Mit szolgál az üres QR-szegély?
3. Hová kerülnek a névmezők adatai a QR-ban?

## Rövid válaszok az önellenőrzéshez

1. A döntés választja ki a pontos payloadot: Richtig vagy Falsch.
2. Segíti a kód elkülönítését és beolvasását.
3. Sehová, csak az eredményszó kerül a QR-ba.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Használat: a QR-payload pontos elvárásához.

2. qrcode-generator package  
   https://www.npmjs.com/package/qrcode-generator  
   Használat: a helyi, egyszerű böngészős QR-generálás technikai alapjához.

Megnyitva: `2026-04-09`
