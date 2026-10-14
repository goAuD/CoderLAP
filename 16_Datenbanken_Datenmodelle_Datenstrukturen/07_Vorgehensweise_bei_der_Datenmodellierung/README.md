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

## Kidolgozott modell: tanulók és kurzusok

Először a szabályokat rögzítjük: egy tanuló több kurzusra jelentkezhet; egy kurzusra több tanuló járhat; ugyanaz a tanuló ugyanarra a meghirdetett kurzusra egyszer jelentkezhet. A jelentkezés dátuma nem a tanulóhoz önmagában, hanem ehhez a kapcsolathoz tartozik.

| Tábla | Kulcs és lényeges adatok |
|---|---|
| students | `id` elsődleges kulcs, név |
| courses | `id` elsődleges kulcs, cím |
| enrollments | összetett kulcs: `student_id, course_id`; jelentkezési dátum |

A két idegen kulcs az `enrollments` táblában oldja fel az n:m kapcsolatot. A `0..n` azt is megengedi, hogy egy új kurzusnak még nincs résztvevője. A jelentkezés mindkét hivatkozása kötelező. A kurzuscím nem jó azonosító, mert változhat és ismétlődhet.

Ellenőrizd a modellt konkrét történettel: felvehető-e egy üres kurzus, szerepelhet-e két azonos nevű tanuló, tiltott-e a kettős jelentkezés, és mi történjen kurzustörléskor? Ha egy kurzus évente újra indul, külön kurzusalkalom szükséges; ezt az igényt a követelmény határozza meg. A törlési szabály és a megőrzendő történet is a modellezés része.

## Vizsgán jól használható megfogalmazás

> Az adatmodellezés során a valós vagy üzleti folyamatok adatait strukturált modellé alakítjuk.  
> Ennek tipikus lépése a követelmények felmérése, az entitások és attribútumok meghatározása, a kapcsolatok és kulcsok  
> kijelölése, majd a normalizálás és a konkrét adatbázis-séma kialakítása.  
> A cél egy átlátható, bővíthető és konzisztens adatstruktúra létrehozása.

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

### A bővítés ellenőrzött forrásai

- [Microsoft: Database design basics](https://support.microsoft.com/en-us/access/database-design-basics): követelmények, táblák, kapcsolatok és normalizálás

Ellenőrizve: `2026-10-14`.
