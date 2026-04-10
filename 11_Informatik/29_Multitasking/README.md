# Multitasking

## Gyors vizuális kép

| Helyzet | Mit lát a felhasználó? |
|---|---|
| zene szól, közben böngészel | több feladat egyszerre fut |
| fájl másolása és dokumentumszerkesztés | rendszer több munkát kezel |

## Mi a multitasking lényege?

Az operációs rendszer a processzoridőt és más erőforrásokat több feladat között osztja el.

Ez történhet:

- gyors időosztással
- több mag használatával
- folyamatok és szálak kezelésével

## Miért fontos?

- a rendszer használhatóbb lesz
- több alkalmazás dolgozhat egy időben
- jobb felhasználói élményt ad
- háttérfeladatok futtathatók munka közben

## Multitasking és párhuzamosság

| Fogalom | Jelentés |
|---|---|
| multitasking | több feladat kezelése egy rendszerben |
| valódi párhuzamosság | több magon ténylegesen egy időben futó végrehajtás |
| időosztás | nagyon gyors váltás a feladatok között |

## Hol jelenik meg?

- operációs rendszerekben
- mobil rendszerekben
- szervereken
- böngészős környezetben is részben, például worker modelleknél

## Mire kell figyelni?

- A multitasking nem jelenti azt, hogy minden mindig valóban egyszerre fut.
- Több feladat több erőforrást igényelhet.
- Rossz terhelésnél a rendszer lassulhat.
- Fejlesztésnél figyelni kell a szálbiztonságra és a megosztott erőforrásokra.

## Vizsgán jól használható megfogalmazás

> A multitasking azt jelenti, hogy egy operációs rendszer több feladatot vagy folyamatot kezel úgy, hogy azok a felhasználó számára egyidejűnek tűnnek.  
> Ez megvalósulhat gyors időosztással vagy több processzormag használatával.  
> Célja, hogy a rendszer több alkalmazást és háttérműveletet is hatékonyan tudjon kezelni.

## Gyakori vizsgahibák

- A multitaskingot valódi párhuzamossággal teljesen azonosnak venni.
- Nem megemlíteni az operációs rendszer szerepét.
- Azt hinni, hogy egyetlen processzormagon nincs multitasking.
- Nem beszélni az erőforrásmegosztásról.

## Gyors önellenőrzés

1. Mi a multitasking lényege?
2. Mi a különbség multitasking és valódi párhuzamosság között?
3. Miért fontos a felhasználó számára?
4. Ki kezeli ezt tipikusan?
5. Mi lehet a technikai nehézsége?

## Rövid válaszok az önellenőrzéshez

1. Több feladat kezelése egy rendszerben
2. A multitasking lehet gyors váltogatás is, nem csak valódi egyidejű futás
3. Mert egyszerre több dolgot lehet használni
4. Az operációs rendszer
5. Erőforrás-kezelés és szálbiztonság

## Források

1. Microsoft Support - How to multitask in Windows  
   https://support.microsoft.com/en-us/windows/how-to-multitask-in-windows-b4fa0333-98f8-ef43-e25c-06d4fb1d6960  
   Használat: gyakorlati, hivatalos példa a multitasking felhasználói oldalára.

2. MDN - Thread  
   https://developer.mozilla.org/en-US/docs/Glossary/Thread  
   Használat: alapfogalmi háttér a szálak és végrehajtási egységek megértéséhez.

3. MDN - Web Workers API  
   https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API  
   Használat: böngészős környezetben a párhuzamosabb feladatkezelés egyik hivatalos példája.

Megnyitva: `2026-04-08`
