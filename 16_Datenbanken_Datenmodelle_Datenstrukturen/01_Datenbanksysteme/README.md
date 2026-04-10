# Datenbanksysteme

## Gyors vizuális kép

| Elem | Szerep |
|---|---|
| adatbázis | az adatok tárolása |
| `DBMS` | kezelés, lekérdezés, hozzáférés, védelem |
| alkalmazások | üzleti vagy technikai használat |
| felhasználók | adatbevitel, lekérdezés, adminisztráció |

## Mi az adatbázisrendszer?

Az adatbázisrendszer általában ezekből áll:

- maga az adatbázis
- az adatbáziskezelő rendszer (`DBMS`)
- a kapcsolódó alkalmazások
- a felhasználók és adminisztrátorok
- a hardver és futási környezet

Ezért fontos, hogy az adatbázisrendszer **több**, mint egy egyszerű adattároló fájl.

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
| adatbázisrendszer | adatbázis + `DBMS` + alkalmazások + környezet |

## Hol találkozunk vele?

Tipikus példák:

- webshop háttérrendszere
- vállalati ügyfélkezelés
- raktárkezelés
- tanulói vagy dolgozói nyilvántartás
- tartalomkezelő rendszerek

## Vizsgán jól használható megfogalmazás

> Az adatbázisrendszer a tárolt adatokból, az adatbáziskezelő rendszerből és a hozzájuk kapcsolódó alkalmazásokból álló teljes rendszer.  
> Célja az adatok strukturált tárolása, lekérdezése, módosítása és biztonságos kezelése.  
> Az adatbázisrendszer tehát nemcsak maga az adat, hanem annak teljes működési környezete is.

## Gyakori vizsgahibák

- Az adatbázisrendszert az adatbázissal azonosítani.
- A `DBMS` fogalmát kihagyni.
- Nem megemlíteni a többfelhasználós és adminisztrációs szerepet.
- Úgy kezelni, mintha csak egyetlen fájl lenne az egész rendszer.

## Gyors önellenőrzés

1. Mi az adatbázisrendszer?
2. Miből áll tipikusan?
3. Mi a különbség adatbázis és `DBMS` között?
4. Miért fontos a központi adatkezelés?
5. Mondj két gyakorlati példát adatbázisrendszerre.

## Rövid válaszok az önellenőrzéshez

1. A teljes adatkezelő környezet
2. Adatbázis, `DBMS`, alkalmazások, felhasználók
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
