# Gueltigkeitsbereiche von Variablen

## Gyors vizuális kép

| Scope típusa | Hol érhető el? |
|---|---|
| globális | a program nagy részében |
| lokális / függvény-szintű | csak egy függvényen belül |
| blokk-szintű | csak egy adott blokkban, például `if` vagy ciklus belsejében |

## Mi az a hatókör?

A hatókör azt jelenti, hogy:

- hol hoztuk létre a változót
- mely kódrészek férhetnek hozzá
- hol használható biztonságosan

## Miért fontos?

- segít elkerülni a névütközéseket
- csökkenti a véletlen felülírás esélyét
- átláthatóbbá teszi a programot
- könnyebbé teszi a hibakeresést

## Tipikus scope-ok

### Globális

- sok helyről elérhető
- kényelmesnek tűnhet
- de növelheti a hibalehetőséget

### Lokális

- csak egy függvényen vagy eljáráson belül él
- jobban kontrollálható

### Blokk-szintű

- csak egy adott `{}` blokkon belül látszik
- modern nyelvekben és modern nyelvi elemeknél gyakori

## Hatókör és élettartam: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| hatókör | hol érhető el a változó |
| élettartam | meddig létezik a változó |

A kettő összefügg, de nem ugyanaz.

## Miért problémás a túl sok globális változó?

- nehezebb követni a program állapotát
- könnyebb véletlenül módosítani
- gyengíti a moduláris felépítést

## Vizsgán jól használható megfogalmazás

> A változók hatóköre azt határozza meg, hogy a program mely részein érhető el egy adott változó.  
> Beszélhetünk például globális, lokális és blokk-szintű scope-ról.  
> A helyes scope-kezelés fontos a hibák megelőzése, az átláthatóság és a karbantarthatóság szempontjából.

## Gyakori vizsgahibák

- A hatókört az élettartammal összekeverni.
- Azt állítani, hogy a globális változó mindig jó, mert “mindenhonnan látszik”.
- Nem megemlíteni a lokális scope előnyeit.
- Scope és adattípus összemosása.

## Gyors önellenőrzés

1. Mit jelent a változó hatóköre?
2. Mi a különbség globális és lokális scope között?
3. Miért veszélyes sok globális változót használni?
4. Mi a blokk-szintű scope?
5. Mi a különbség scope és élettartam között?

## Rövid válaszok az önellenőrzéshez

1. Azt, hogy hol érhető el a változó
2. Az egyik sok helyről, a másik csak helyileg látszik
3. Mert nehezebb követni és könnyebb felülírni
4. Amikor csak egy adott blokkban érhető el
5. Az egyik a láthatóság, a másik a létezés ideje

## Források

1. MDN - Scope  
   https://developer.mozilla.org/en-US/docs/Glossary/Scope  
   Használat: hivatalos, tömör alapforrás a scope fogalmához.

2. MDN - Functions  
   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions  
   Használat: kiegészítő háttér a függvény- és lokális scope gyakorlati értelmezéséhez.

Megnyitva: `2026-04-09`
