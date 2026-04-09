# Datenmodell

## Lényeg 30 másodpercben

Az **adatmodell** azt írja le, hogy milyen adatokat tárolunk, ezek hogyan kapcsolódnak egymáshoz, és milyen szabályok vonatkoznak rájuk.

Röviden:

- strukturálja az adatokat
- kapcsolatokat mutat meg
- alapja az adatbázis megvalósításának

## Gyors vizuális kép

| Modell elem | Jelentés |
|---|---|
| entitás | valamilyen tárolt dolog, pl. ügyfél |
| attribútum | az entitás tulajdonsága |
| kapcsolat | az entitások közti viszony |
| kulcs | azonosítás és összekapcsolás |

## Mi az adatmodell célja?

Az adatmodell segít:

- megérteni az adatok szerkezetét
- elkerülni a káoszt az adatkezelésben
- jól tervezhetővé tenni az adatbázist
- egyértelműsíteni az üzleti szabályokat

## Mit tartalmaz egy adatmodell?

Tipikusan:

- entitásokat
- attribútumokat
- kapcsolatokat
- kulcsokat
- megszorításokat vagy üzleti szabályokat

## Milyen szintek vannak?

| Szint | Fókusz |
|---|---|
| fogalmi modell | üzleti szemlélet |
| logikai modell | táblákhoz közeli struktúra |
| fizikai modell | konkrét `DBMS`-re szabott megvalósítás |

## Példa

Egy webshopnál lehetnek ilyen entitások:

- `Customer`
- `Order`
- `Product`

Kapcsolat:

- egy ügyfélnek több rendelése lehet
- egy rendelés több terméket tartalmazhat

## Adatmodell és adatbázis: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| adatmodell | elvi szerkezeti leírás |
| adatbázis | a ténylegesen megvalósított tárolás |

## Miért fontos a rendszerfejlesztésben?

- jó alapot ad a fejlesztőknek
- segíti az adatok következetes kezelését
- támogatja a tesztelést és továbbfejlesztést

## Vizsgán jól használható megfogalmazás

> Az adatmodell az adatok szerkezetének és kapcsolatainak leírása.  
> Meghatározza, hogy milyen entitásokat, attribútumokat és relációkat kell kezelni, valamint milyen szabályok és kulcsok érvényesek rájuk.  
> Az adatmodell a jól felépített adatbázis és adatkezelő rendszer egyik legfontosabb tervezési alapja.

## Gyakori vizsgahibák

- Az adatmodellt az adatbázissal azonosítani.
- Nem megemlíteni a kapcsolatokat.
- Kihagyni a kulcsok szerepét.
- Úgy kezelni, mintha csak rajz lenne, szabályok nélkül.

## Gyors önellenőrzés

1. Mi az adatmodell?
2. Milyen elemei vannak?
3. Mi a különbség adatmodell és adatbázis között?
4. Miért fontos a kapcsolatok leírása?
5. Milyen szintjei lehetnek a modellezésnek?

## Rövid válaszok az önellenőrzéshez

1. Az adatok szerkezeti leírása
2. Entitások, attribútumok, kapcsolatok, kulcsok
3. Az egyik terv, a másik megvalósítás
4. Mert az adatok nem elszigeteltek
5. Fogalmi, logikai, fizikai

## Források

1. Oracle SQL Developer Data Modeler  
   https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/  
   Használat: hivatalos forrás az adatmodellezés szintjeihez és céljához.

2. Oracle Database Concepts  
   https://docs.oracle.com/cd/F39414_01/cncpt/database-concepts.pdf  
   Használat: hivatalos háttér a relációs adatszervezés és modellezés alapjaihoz.

Megnyitva: `2026-04-09`
