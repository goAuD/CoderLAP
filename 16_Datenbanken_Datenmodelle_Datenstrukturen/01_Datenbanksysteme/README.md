# Datenbanksysteme

## Gyors vizuális kép

| Elem | Szerep |
|---|---|
| adatbázis | az adatok tárolása |
| `DBMS` | kezelés, lekérdezés, hozzáférés, védelem |
| alkalmazások | üzleti vagy technikai használat |
| felhasználók | adatbevitel, lekérdezés, adminisztráció |

## Mi az adatbázisrendszer?

Szűk szakmai értelemben az adatbázisrendszer az **adatbázis és az azt kezelő DBMS együttese**. Tágabb működési környezetében szerepelnek az alkalmazások, a felhasználók, az üzemeltetők és a hardver is. Érdemes jelezni, melyik értelemben használod a fogalmat.

A DBMS lehet külön kiszolgáló, például MySQL, vagy az alkalmazásba beépített könyvtár, például SQLite. Attól, hogy egy adatbázis egy fájlban tárolható, még lehet teljes értékű lekérdezés- és tranzakciókezelése.

## Miért fontos?

- központi adatkezelést tesz lehetővé
- több felhasználó dolgozhat ugyanazzal az adatbázissal
- szabályozható a hozzáférés
- támogatja a biztonságot, mentést, integritást és teljesítményt

## Tipikus adatbázisrendszer-feladatok

- adatok tárolása
- lekérdezés
- módosítás
- jogosultságkezelés
- mentés és visszaállítás
- többfelhasználós működés kezelése

## Adatbázis, `DBMS`, adatbázisrendszer: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| adatbázis | strukturáltan tárolt adatok |
| `DBMS` | szoftver, amely kezeli az adatokat |
| adatbázisrendszer | szűken: adatbázis + `DBMS`; tágabban: a működési környezet is |

## Hol találkozunk vele?

Tipikus példák:

- webshop háttérrendszere
- vállalati ügyfélkezelés
- raktárkezelés
- tanulói vagy dolgozói nyilvántartás
- tartalomkezelő rendszerek

## Kidolgozott eset: könyvkölcsönzés

Egy könyvtári alkalmazásban a `books` és `loans` táblák az adatbázis részei. A MySQL DBMS feldolgozza a lekérdezést, ellenőrzi a kulcsokat és összehangolja a párhuzamos módosításokat. Az alkalmazás mutatja az űrlapot, ellenőrzi a bejelentkezett személy üzleti jogosultságát, és elküldi a szükséges utasítást.

Ha két pult egyszerre adná ki ugyanazt a példányt, a közös fájlba írás önmagában kevés. Egy jól megtervezett tranzakció és adatbázisszabály teszi ellenőrizhetővé, hogy egyetlen aktív kölcsönzés szülessen. A DBMS nem találja ki helyettünk ezt az üzleti szabályt.

A relációs modell táblákkal, kulcsokkal és kapcsolatokkal dolgozik. Dokumentum-, kulcs-érték- és gráfadatbázisok más szerkezetet kínálnak. A választásnál a lekérdezések, az adatok kapcsolatai és a konzisztenciaigény fontosabb, mint önmagában az SQL vagy NoSQL címke.

## Vizsgán jól használható megfogalmazás

> Az adatbázis strukturált adatokat tárol, a DBMS pedig kezeli a hozzáférést, a lekérdezéseket és a módosításokat. Együtt alkotják az adatbázisrendszer magját. Az alkalmazások és az üzemeltetési környezet erre épülnek.

## Gyors önellenőrzés

1. Mi az adatbázisrendszer?
2. Miből áll tipikusan?
3. Mi a különbség adatbázis és `DBMS` között?
4. Miért fontos a központi adatkezelés?
5. Mondj két gyakorlati példát adatbázisrendszerre.

## Rövid válaszok az önellenőrzéshez

1. Szűken adatbázis és DBMS; tágabban a kapcsolódó működési környezet is
2. A magja adatbázis és DBMS, körülötte alkalmazások és üzemeltetési környezet
3. Az egyik adat, a másik kezelő szoftver
4. Mert egységes és biztonságos hozzáférést ad
5. Webshop, ügyfélnyilvántartó rendszer

## Források

1. Oracle - What Is a Database?  
   https://www.oracle.com/database/what-is-database/  
   Használat: hivatalos, modern forrás az adatbázis, `DBMS` és adatbázisrendszer kapcsolatának megértéséhez.

2. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Használat: hivatalos alapforrás a relációs adatbázisok és a `DBMS` szerepének pontosabb meghatározásához.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [SQLite: Appropriate Uses](https://www.sqlite.org/whentouse.html): beágyazott és kliens-szerver adatkezelés megkülönböztetése
- [MySQL: Introduction to InnoDB](https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html): tranzakciók és az InnoDB tárolómotor szerepe

Ellenőrizve: `2026-10-14`.
