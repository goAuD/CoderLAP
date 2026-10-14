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

- lehet-e SQL NULL; az üres szöveg megengedettsége külön szabály

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

## A NULL, az üres szöveg és a nulla külön eset

A `NOT NULL` az SQL `NULL` értékét tiltja. A `0`, az üres szöveg (`''`) és a
szóközöket tartalmazó szöveg más értékek; érvényességüket külön szabály dönti el.
Például egy terméknévhez az alkalmazás előírhatja, hogy levágott szélső szóközök
után 1..80 karakter maradjon.

| Bemenet a névhez | Elvárt eredmény e szerződés szerint |
|---|---|
| `"Ada"` | elfogadás |
| `NULL`, `""`, `"   "` | elutasítás |
| 80 karakter | elfogadás |
| 81 karakter | elutasítás, csendes csonkítás nélkül |
| `"Őrség"` | helyes tárolás és változatlan visszaolvasás |

MySQL 8.4-ben például az `price DECIMAL(8,2) NOT NULL CHECK (price >= 0)` egy
**oszlopdefiníció-részlet**, nem önálló SQL-program. A `CHECK` önmagában a `NULL`
miatt ismeretlen eredményű feltételt is elfogadhatja, ezért kell mellé a
kötelezőség. Teszteljük a tényleges adatbázisverziót és SQL-módot, ne csak a
felületet. A karakterhossz és bájthossz eltérhet; az ékezetes szöveg ezért fontos
próbaadat. Az inputellenőrzés mellett külön kell paraméterezett SQL, jogosultság-
ellenőrzés és megjelenítéskor megfelelő kódolás.

## Vizsgán jól használható megfogalmazás

> Az adatbázismezők tesztelése során azt ellenőrizzük, hogy a mezők megfelelnek-e az adattípusra, kötelezőségre,  
> hosszra, tartományra, formátumra és egyediségre vonatkozó elvárásoknak.  
> Fontos nemcsak helyes, hanem hibás, határértékű és váratlan bemenetekkel is tesztelni.  
> A cél az adatminőség, a konzisztencia és a biztonság biztosítása.

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

Ellenőrizve: `2026-10-14`.

- [MySQL: NULL values](https://dev.mysql.com/doc/refman/8.4/en/working-with-null.html): NULL, üres szöveg és nulla különbsége.
- [MySQL: CHECK constraints](https://dev.mysql.com/doc/refman/8.4/en/create-table-check-constraints.html): CHECK és UNKNOWN.
- [OWASP: Input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html): validáció és külön biztonsági rétegek.


1. OWASP Input Validation Cheat Sheet  
   https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html  
   Használat: hivatalos forrás a helyes input-ellenőrzési elvekhez, beleértve a szintaktikai és szemantikai validációt.

2. PostgreSQL - Constraints  
   https://www.postgresql.org/docs/current/ddl-constraints.html  
   Használat: hivatalos háttér a mezőszintű megszorításokhoz, például `NOT NULL`, `UNIQUE`, `CHECK`, `FOREIGN KEY`.

Megnyitva: `2026-04-09`
