# Sicherungsmethoden

## Gyors vizuális kép

| Mentéstípus | Jellemző |
|---|---|
| teljes mentés | minden adat mentése |
| inkrementális | csak a változások mentése |
| logikai mentés | például `dump`, sémák és adatok exportja |
| fizikai mentés | adatfájlok, WAL / naplók, teljes állapot |

## Miért fontos a mentés?

- hardverhiba esetén
- emberi hiba esetén
- szoftverhiba esetén
- támadás vagy adatvesztés után

## Tipikus módszerek

### Teljes mentés

Az egész adatbázis mentése.

Előny:

- egyszerűbb visszaállítás

Hátrány:

- idő- és tárhelyigényesebb

### Inkrementális mentés

Csak az utolsó mentés óta történt változásokat menti.

Előny:

- kisebb tárhely

Hátrány:

- a visszaállítás összetettebb lehet

### Logikai mentés

Például:

- `SQL dump`
- séma + adatok exportja

### Fizikai mentés

A tényleges adatfájlok vagy adatbázis-szintű állapot mentése.

## Backup és recovery együtt fontos

Vizsgán jó, ha kimondod:

- nem elég menteni
- vissza is kell tudni állítani
- a helyreállítási idő és adatvesztési elfogadható mérték is számít

## Mentés és replikáció: ne keverd össze

| Fogalom | Mire jó? |
|---|---|
| backup | korábban mentett, használható adatállapot visszaállításának alapja |
| replikáció | másolat fenntartása működés vagy rendelkezésre állás miatt |

## Kidolgozott MySQL-mentési helyzet

A **teljes/inkrementális** az adatmennyiség és a mentési lánc felosztása, a **logikai/fizikai** pedig a mentés megvalósításának másik szempontja. Egy teljes mentés tehát lehet logikai dump is.

MySQL/InnoDB esetén a `mysqldump --single-transaction` konzisztens logikai pillanatképet tud készíteni a tranzakciós táblákról. Közben nem szabad a dumpot érintő táblaszerkezetet változtatni. A kapcsoló nem teszi ugyanígy konzisztenssé a közben változó MyISAM táblákat. A futó szerver adatkönyvtárának egyszerű másolása szintén nem általános mentési eljárás; fizikai backuphoz támogatott, konzisztenciát biztosító módszer kell.

Példa: 02:00-kor készült egy teljes mentés, 10:15-kor véletlen törlés történt. Ha a megfelelő bináris naplók és kezdőpozíció rendelkezésre állnak, a mentés után a napló a törlés előtti pontig visszajátszható (**point-in-time recovery**). A törlést tartalmazó eseményt már nem kell visszajátszani. A mentés önmagában nem tartalmazza a 02:00 utáni adatokat.

A próbavisszaállítás külön adatbázisba történjen. Ellenőrizd a sémát, darabszámokat, kulcsokat és legalább egy üzleti lekérdezést. Rutinok, események, jogosultságok, konfiguráció és kulcsok külön figyelmet igényelhetnek. A replikáció a véletlen törlést is továbbíthatja, ezért nem helyettesíti a korábbi állapotból történő helyreállítást.

## Vizsgán jól használható megfogalmazás

> A mentési módszerek célja, hogy az adatbázis hiba, adatvesztés vagy támadás után helyreállítható legyen.  
> Gyakori megoldás a teljes mentés, az inkrementális mentés, valamint a logikai és fizikai mentés.  
> A hatékony adatvédelemhez nemcsak backup, hanem megtervezett visszaállítási eljárás is szükséges.

## Gyors önellenőrzés

1. Mi a mentés célja?
2. Mi a különbség teljes és inkrementális mentés között?
3. Mi a logikai mentés?
4. Miért kell recovery terv is?
5. Mi a különbség backup és replikáció között?

## Rövid válaszok az önellenőrzéshez

1. Helyreállíthatóság biztosítása
2. Az egyik mindent, a másik csak a változásokat menti
3. Például SQL-dump alapú mentés
4. Mert a mentést használni is tudni kell
5. A backup visszaállításra, a replikáció rendelkezésre állásra is szolgál

## Források

1. PostgreSQL - Backup and Restore  
   https://www.postgresql.org/docs/current/backup.html  
   Használat: hivatalos forrás a backup alapfogalmaihoz.

2. PostgreSQL - SQL Dump  
   https://www.postgresql.org/docs/current/backup-dump.html  
   Használat: hivatalos háttér a logikai mentéshez.

3. PostgreSQL - Continuous Archiving and Point-in-Time Recovery (PITR)  
   https://www.postgresql.org/docs/current/continuous-archiving.html  
   Használat: hivatalos háttér a fejlettebb helyreállítási lehetőségekhez.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [MySQL: mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html): single-transaction feltételei és dump-tartalom
- [MySQL: Point-in-Time Recovery](https://dev.mysql.com/doc/refman/8.0/en/point-in-time-recovery.html): alapmentés és bináris napló visszajátszása

Ellenőrizve: `2026-10-14`.
