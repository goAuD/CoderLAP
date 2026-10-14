# Eingabe-Formular mit Framework

## Gyors vizuális kép

| Kötelező mező | Miért kell? |
|---|---|
| Vorname | Stammdaten |
| Nachname | Stammdaten |
| SV-NR | validálás és QR-eredmény |

## Miért jó itt a `Bootstrap`?

- gyorsan kapsz rendezett űrlapot
- könnyebb responsive layoutot készíteni
- kevesebb saját CSS kell

## Minimális űrlapkövetelmény

- jól olvasható mezőfeliratok
- `Senden` vagy `Prüfen` gomb
- kötelező mezők jelzése
- hibajelzés, ha valamelyik mező hiányzik

## Mire kell figyelni?

- ne legyen túlzsúfolt
- mobilon ne csússzanak szét a mezők
- a hibajelzés legyen egyértelmű

## Részlet: felirat és megfelelő mezőtípus

Ez az űrlap egy mezőjének böngészős HTML-részlete:

```html
<label for="svnummer">SV-NR</label>
<input id="svnummer" name="svnummer" type="text"
       inputmode="numeric" required aria-describedby="sv-help">
<p id="sv-help">10 Ziffern, zum Beispiel 4422 180599.</p>
```

Az `id` és a `for` kapcsolja a feliratot a mezőhöz. A `required` jelzi a kötelezőséget.
Az `inputmode` mobilos billentyűzethez ad javaslatot, de **nem validál**.
Az SV-szám azonosító, ezért szövegként kezeljük, nem számolásra szolgáló `number` mezőként.

A mintamegoldás `novalidate` űrlapot használ, így saját JavaScriptje adja a visszajelzést.
A `trim()` miatt a csupa szóközből álló név is üresnek számít.
A névnél nem írunk olyan betűmintát, amely kizárná az ékezetet, kötőjelet vagy aposztrófot.
Hiányzó mező esetén megállunk; kitöltött, de hibás SV-szám esetén `Falsch` a QR-tartalom.

Bootstrapban a `col-12 col-md-6` a névmezőket kis nézeten egymás alá,
a `md` törésponttól két oszlopba helyezi. A használhatóságot valódi bevitellel és
Tab-billentyűvel is ellenőrizzük.

Forrás: [MDN: required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required),
[MDN: inputmode](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/inputmode),
[Bootstrap-rács](https://getbootstrap.com/docs/5.3/layout/grid/).

## Vizsgán jól használható megfogalmazás

> A gyakorlati feladat első része egy egyszerű, responsive HTML-űrlap készítése `Vorname`, `Nachname` és `SV-NR`  
> mezőkkel.  
> A `Bootstrap` használata azért előnyös, mert gyorsan biztosít rendezett és mobilbarát megjelenést.  
> Fontos, hogy a releváns mezők kitöltése ellenőrizve legyen a gomb megnyomásakor.

## Gyors önellenőrzés

1. Mit csinál az inputmode?
2. Miért használunk trim()-et a névmezőn?
3. Mi az eltérés a hiányzó mező és a kitöltött, hibás SV-szám kezelésében?

## Rövid válaszok az önellenőrzéshez

1. Billentyűzettípust javasol, nem ellenőrzi a formátumot.
2. A csak szóközös név is üresnek számítson.
3. Hiánynál nincs QR; teljes bevitel és hibás SV-szám mellett Falsch készül.

## Források

1. Themenkatalog für die Vorbereitung auf die Lehrabschlussprüfung Applikationsentwicklung-Coding v2-2024  
   https://github.com/goAuD/CoderLAP/blob/main/themenkatalog-applikationsentwicklung-coding-v2-2024.pdf  
   Használat: az űrlap minimális kötelező elemeihez.

2. Bootstrap Forms  
   https://getbootstrap.com/docs/5.3/forms/overview/  
   Használat: hivatalos forrás gyors és responsive űrlapok kialakításához.

3. Bootstrap Layout  
   https://getbootstrap.com/docs/5.3/layout/grid/  
   Használat: hivatalos forrás a responsive rácsszerkezethez.

Megnyitva: `2026-04-09`
