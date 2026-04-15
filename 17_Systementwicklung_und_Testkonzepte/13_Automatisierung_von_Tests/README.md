# Automatisierung von Tests

## Gyors vizuális kép

| Előny | Korlát |
|---|---|
| gyors ismétlés | kezdeti bevezetési költség |
| gyakori regresszióteszt | karbantartani kell |
| CI-be illeszthető | rosszul tervezve instabil lehet |

## Mi az a tesztautomatizálás?

A tesztautomatizálás során:

- szkriptek
- tesztframeworkök
- CI-rendszerek

végzik el a tesztek futtatását és gyakran az eredmények kiértékelését is.

## Miért hasznos?

- gyorsan újrafuttatható ugyanaz a teszt
- regressziótesztekhez nagyon jó
- csökkenti a kézi, ismétlődő munkát
- könnyen beilleszthető `CI` folyamatba

## Mit érdemes automatizálni?

Tipikusan:

- gyakran ismételt tesztek
- stabil funkciók
- regressziós ellenőrzések
- build utáni alapellenőrzések

## Mit nem biztos, hogy érdemes?

- nagyon gyorsan változó UI-t kezdetben
- egyszeri vagy ritka ellenőrzéseket
- erősen emberi megítélést igénylő teszteket

## Kockázatok

- a tesztek is lehetnek hibásak
- karbantartási költségük van
- rossz izoláció esetén flaky tesztek jöhetnek létre
- hamis biztonságérzetet adhatnak, ha nincs jó tesztstratégia

## Tesztautomatizálás és teljes minőségbiztosítás: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| tesztautomatizálás | bizonyos tesztek gépesített futtatása |
| minőségbiztosítás | szélesebb folyamat, több elemmel |

## Tipikus eszközök és környezetek

- unit test frameworkök
- browseres tesztautomatizálás
- `CI` rendszerek
- riportáló eszközök

## Vizsgán jól használható megfogalmazás

> A tesztautomatizálás során bizonyos teszteket eszközök és szkriptek futtatnak le automatikusan.  
> Ez különösen hasznos ismétlődő, regressziós vagy `CI`-be illeszthető tesztek esetén, mert gyorsabb és gyakrabban  
> végrehajtható ellenőrzést tesz lehetővé.  
> Ugyanakkor nem minden teszt automatizálható ésszerűen, és az automatizált tesztek karbantartása is erőforrást igényel.

## Gyakori vizsgahibák

- Azt állítani, hogy minden tesztet automatizálni kell.
- Nem megemlíteni a karbantartási költséget.
- A tesztautomatizálást a teljes QA-val azonosítani.
- Kihagyni a `CI` kapcsolatát.

## Gyors önellenőrzés

1. Mi a tesztautomatizálás lényege?
2. Milyen tesztek alkalmasak rá különösen?
3. Mi az egyik fő előnye?
4. Mi az egyik fő hátránya?
5. Miért fontos a `CI` kapcsolata?

## Rövid válaszok az önellenőrzéshez

1. Tesztek automatikus futtatása eszközökkel
2. Gyakran ismételt és regressziós tesztek
3. Gyors újrafuttatás
4. Karbantartási költség
5. Mert így minden változásnál automatikusan ellenőrizhető a kód

## Források

1. Selenium - Overview of Test Automation  
   https://www.selenium.dev/documentation/test_practices/overview/  
   Használat: hivatalos, modern forrás a tesztautomatizálás céljához, előnyeihez és korlátaihoz.

2. GitHub Docs - About continuous integration with GitHub Actions  
   https://docs.github.com/en/actions/about-github-actions/about-continuous-integration-with-github-actions  
   Használat: hivatalos forrás arra, hogyan illeszkedik a tesztautomatizálás a `CI` folyamatba.

3. ISTQB CTFL Overview  
   https://test.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/  
   Használat: hivatalos háttér a tesztautomatizálás előnyeihez és kockázataihoz tesztelési nézőpontból.

Megnyitva: `2026-04-09`
