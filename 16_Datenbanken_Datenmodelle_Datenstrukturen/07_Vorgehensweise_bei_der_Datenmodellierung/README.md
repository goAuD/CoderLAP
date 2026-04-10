# Vorgehensweise bei der Datenmodellierung

## Gyors vizuális kép

```text
Követelmények megértése
    -> entitások és attribútumok azonosítása
    -> kapcsolatok meghatározása
    -> kulcsok kijelölése
    -> normalizálás
    -> logikai / fizikai modell
```

## Mi az adatmodellezés célja?

Az, hogy:

- világos legyen, milyen adatokat kell tárolni
- ezek hogyan kapcsolódnak egymáshoz
- milyen szabályok érvényesek rájuk

## Tipikus lépések

### 1. Követelmények összegyűjtése

Meg kell érteni:

- milyen adatokat kell tárolni
- milyen kérdésekre kell válaszolni
- milyen műveleteket kell támogatni

### 2. Entitások azonosítása

Például:

- ügyfél
- rendelés
- termék
- dolgozó

### 3. Attribútumok meghatározása

Például egy ügyfélnél:

- név
- cím
- e-mail
- azonosító

### 4. Kapcsolatok megadása

Például:

- egy ügyfélnek több rendelése lehet
- egy rendelés több terméket tartalmazhat

### 5. Kulcsok és szabályok meghatározása

Itt döntjük el:

- mi legyen az elsődleges kulcs
- hol kell idegen kulcs
- milyen integritási szabályok szükségesek

### 6. Normalizálás

Cél:

- kevesebb redundancia
- jobb adatkonzisztencia

### 7. Logikai és fizikai megvalósítás

Itt lesz az elméleti modellből konkrét adatbázis-séma.

## Fogalmi, logikai, fizikai modell

| Szint | Jelentés |
|---|---|
| fogalmi modell | üzleti szintű leírás |
| logikai modell | táblák, kulcsok, kapcsolatok |
| fizikai modell | konkrét `DBMS`-hez igazított megvalósítás |

## Vizsgán jól használható megfogalmazás

> Az adatmodellezés során a valós vagy üzleti folyamatok adatait strukturált modellé alakítjuk.  
> Ennek tipikus lépése a követelmények felmérése, az entitások és attribútumok meghatározása, a kapcsolatok és kulcsok kijelölése, majd a normalizálás és a konkrét adatbázis-séma kialakítása.  
> A cél egy átlátható, bővíthető és konzisztens adatstruktúra létrehozása.

## Gyakori vizsgahibák

- Rögtön táblákkal kezdeni az üzleti fogalmak megértése nélkül.
- A modellezést csak rajzolásnak tekinteni.
- Nem megemlíteni a kulcsokat és kapcsolatokat.
- A fogalmi és fizikai modellt összekeverni.

## Gyors önellenőrzés

1. Mi az adatmodellezés célja?
2. Melyek a tipikus fő lépések?
3. Mi az entitás?
4. Mi a különbség logikai és fizikai modell között?
5. Miért fontos a normalizálás a modellezés során?

## Rövid válaszok az önellenőrzéshez

1. Strukturált adatmodell létrehozása
2. Igényfelmérés, entitások, attribútumok, kapcsolatok, kulcsok, normalizálás
3. Olyan dolog vagy objektum, amiről adatot tárolunk
4. Az egyik általánosabb, a másik konkrét `DBMS`-re szabott
5. Mert csökkenti a redundanciát és növeli a konzisztenciát

## Források

1. Oracle SQL Developer Data Modeler  
   https://www.oracle.com/database/sqldeveloper/technologies/sql-data-modeler/  
   Használat: hivatalos, modern forrás a logikai, relációs és fizikai modellezési szintekhez.

2. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Használat: gyakorlati, hivatalos forrás a relációs tervezési folyamat alaplépéseihez.

Megnyitva: `2026-04-09`
