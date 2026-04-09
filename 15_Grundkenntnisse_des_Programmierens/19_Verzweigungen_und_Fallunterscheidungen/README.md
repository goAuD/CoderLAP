# Verzweigungen und Fallunterscheidungen

## Lényeg 30 másodpercben

Az elágazások segítségével a program különböző utakon haladhat tovább attól függően, hogy milyen feltételek teljesülnek.

Röviden:

- döntési pontokat valósítanak meg
- tipikus eszköz az `if / else`
- több lehetőség esetén gyakori a `switch / case`

## Gyors vizuális kép

```text
feltétel?
    igen -> egyik ág
    nem  -> másik ág
```

## Mi az a vezérlési elágazás?

Az elágazás lényege:

- a program nem mindig ugyanazt csinálja
- egy feltétel alapján választ
- különböző utasítások hajtódhatnak végre

## Tipikus formák

### `if`

Egy feltétel esetén fut valami.

### `if / else`

Két lehetséges ág van.

### `else if` lánc

Több feltétel egymás után ellenőrizhető.

### `switch / case`

Több konkrét eset közül választunk.

## Mikor jó a `switch`?

- ha ugyanazt az értéket több lehetséges esettel hasonlítjuk össze
- ha az elágazásokat átláthatóbban akarjuk látni

## Mire kell figyelni?

- a feltételek legyenek egyértelműek
- a sorrend számíthat
- legyen kezelve az alapértelmezett vagy “egyik sem” eset is

## Elágazás és ciklus: ne keverd össze

| Fogalom | Mire való? |
|---|---|
| elágazás | döntés |
| ciklus | ismétlés |

## Vizsgán jól használható megfogalmazás

> Az elágazások és fallunterscheidungok segítségével a program különböző végrehajtási ágak közül választhat feltételek alapján.  
> A leggyakoribb megoldás az `if / else`, több konkrét eset kezelésére pedig gyakran használunk `switch / case` szerkezetet.  
> Ezek a vezérlési szerkezetek a döntési logika megvalósítására szolgálnak.

## Gyakori vizsgahibák

- Az elágazást ciklusnak nevezni.
- A `switch`-et mindenre alkalmasnak beállítani.
- Nem megemlíteni az alapértelmezett esetet.
- A feltételek sorrendjének jelentőségét elfelejteni.

## Gyors önellenőrzés

1. Mire való az elágazás?
2. Mikor használunk `if / else` szerkezetet?
3. Mikor lehet átláthatóbb a `switch / case`?
4. Miért fontos az alapértelmezett ág?
5. Mi a különbség elágazás és ciklus között?

## Rövid válaszok az önellenőrzéshez

1. Döntési helyzetek kezelésére
2. Ha feltétel alapján két vagy több út közül választunk
3. Ha több konkrét esetet vizsgálunk
4. Mert kezelni kell a nem várt eseteket is
5. Az egyik dönt, a másik ismétel

## Források

1. MDN - Control flow and error handling  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling  
   Használat: hivatalos, részletes forrás az `if`, `else`, `switch` és egyéb elágazások működéséhez.

2. MDN - Control flow  
   https://developer.mozilla.org/en-US/docs/Glossary/Control_flow  
   Használat: kiegészítő forrás a döntési szerkezetek általános szerepéhez.

Megnyitva: `2026-04-09`
