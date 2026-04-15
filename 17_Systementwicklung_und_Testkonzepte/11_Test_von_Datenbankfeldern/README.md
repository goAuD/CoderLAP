# Test von Datenbankfeldern

## Gyors vizuális kép

| Mit tesztelünk? | Példa |
|---|---|
| adattípus | számmezőbe ne menjen szöveg |
| hossz | ne lehessen túl hosszú értéket menteni |
| kötelező mező | `NOT NULL` működik-e |
| egyediség | `UNIQUE` mező nem duplikálható |
| tartomány | ár nem lehet negatív |

## Mit jelent egy adatbázismező tesztelése?

Azt ellenőrizzük, hogy a mező:

- a megfelelő típusú adatot fogadja
- elfogadja a helyes értékeket
- elutasítja a hibás vagy veszélyes értékeket
- összhangban van a specifikációval és megszorításokkal

## Tipikus ellenőrzések

### Kötelező mező

- üresen maradhat-e vagy sem

### Hosszellenőrzés

- túl hosszú adatot enged-e

### Formátumellenőrzés

- e-mail, dátum, kód, irányítószám formája helyes-e

### Tartományellenőrzés

- szám vagy dátum egy érvényes határon belül van-e

### Egyediség

- duplikált érték engedett-e vagy tiltott

## Miért fontos?

- védi az adatminőséget
- csökkenti a hibás rekordok számát
- javítja a biztonságot
- megelőzi a későbbi adatfeldolgozási problémákat

## Tesztelni kell helyes és hibás bemenetekkel is

Vizsgán jó pont:

- ne csak “jó” adatokat próbáljunk
- legyenek határértékek és rossz bemenetek is

## Adatbázismező tesztelése és UI-teszt: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| UI-teszt | a felületi viselkedés |
| adatmezőteszt | az adat érvényessége és tárolása |

## Vizsgán jól használható megfogalmazás

> Az adatbázismezők tesztelése során azt ellenőrizzük, hogy a mezők megfelelnek-e az adattípusra, kötelezőségre,  
> hosszra, tartományra, formátumra és egyediségre vonatkozó elvárásoknak.  
> Fontos nemcsak helyes, hanem hibás, határértékű és váratlan bemenetekkel is tesztelni.  
> A cél az adatminőség, a konzisztencia és a biztonság biztosítása.

## Gyakori vizsgahibák

- Csak helyes adatokat tesztelni.
- Nem megemlíteni a határértékeket.
- A mezőtesztet kizárólag felületi ellenőrzésként kezelni.
- Kihagyni az egyediség és formátum vizsgálatát.

## Gyors önellenőrzés

1. Mit kell ellenőrizni egy adatbázismezőnél?
2. Miért fontos a hibás bemenetek tesztelése?
3. Mi az a határértékteszt itt?
4. Mire való az egyediség ellenőrzése?
5. Miért fontos a szerveroldali és adatbázisszintű védelem is?

## Rövid válaszok az önellenőrzéshez

1. Típus, hossz, kötelezőség, tartomány, formátum, egyediség
2. Mert a rendszernek azokat is kezelnie kell
3. A megengedett minimum és maximum környékének tesztelése
4. Duplikációk megelőzésére
5. Mert a kliensoldali ellenőrzés megkerülhető

## Források

1. OWASP Input Validation Cheat Sheet  
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html  
   Használat: hivatalos forrás a helyes input-ellenőrzési elvekhez, beleértve a szintaktikai és szemantikai validációt.

2. PostgreSQL - Constraints  
   https://www.postgresql.org/docs/current/ddl-constraints.html  
   Használat: hivatalos háttér a mezőszintű megszorításokhoz, például `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`.

Megnyitva: `2026-04-09`
