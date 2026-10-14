# Backup Prinzipien

## Gyors vizuális kép

| Típus | Mit ment? | Előny | Hátrány |
|---|---|---|---|
| full | mindent | egyszerű restore | idő- és tárhelyigényes |
| incremental | utolsó mentés óta változott adatokat | gyorsabb, kisebb | restore bonyolultabb |
| differential | utolsó teljes mentés óta változott adatokat | restore egyszerűbb, mint incremental | nőhet a mérete |

## Melyek a fő backup alapelvek?

### 1. Rendszeresség

A backup csak akkor ér valamit, ha:

- rendszeresen készül

### 2. Több példány

Jó gyakorlat:

- ne csak egyetlen másolat legyen

Erre ismert elv:

- `3-2-1`

vagyis:

- legalább 3 példány összesen, az éles adatot is beleszámítva
- 2 különböző adathordozó
- 1 külön / offsite másolat

### 3. Restore teszt

Nem elég, hogy "lefutott" a mentés.

Meg kell nézni:

- tényleg visszaállítható-e

### 4. Elkülönített tárolás

A mentés ne legyen mindig ugyanazon a rendszeren vagy ugyanabban a helyiségben.

### 5. Megfelelő mentési típus

Nem mindenhez ugyanaz a legjobb.

## Mi a full backup?

A full backup:

- mindent lement

Előny:

- egyszerű visszaállítás

Hátrány:

- több idő és tárhely

## Mi az incremental backup?

Az incremental backup:

- csak a legutóbbi mentés óta változott adatokat menti

Előny:

- gyorsabb
- kevesebb tárhely kell

Hátrány:

- restore-nál több lépés kellhet

## Mi a differential backup?

A differential backup:

- mindig az utolsó teljes mentés óta történt változásokat menti

Előny:

- restore egyszerűbb lehet, mint incrementalnál

Hátrány:

- idővel általában nő a mérete; ez a változásoktól és a mentőprogramtól is függ

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| backup | helyreállítási célú mentés |
| sync | két hely tartalmának összehangolása, nem mindig valódi backup |
| archive | hosszabb távú megőrzés, nem feltétlen gyors restore-ra |

## Kidolgozott mentési lánc

Vasárnap teljes mentés készül. Hétfőn az `A`, kedden a `B`, szerdán a `C` fájl változik. Az egyszerű példában nincs törlés, tömörítés vagy deduplikáció.

| Nap | Napi inkrementális mentés | Napi differenciális mentés |
|---|---|---|
| hétfő | A változása | A változása |
| kedd | B változása | A és B változása |
| szerda | C változása | A, B és C változása |

A szerdai állapothoz a hagyományos inkrementális láncnál **vasárnap + hétfő + kedd + szerda** szükséges. Differenciálisnál **vasárnap + szerda** elegendő. Ezért egy hiányzó keddi inkrementális tag a későbbi állapot visszaállítását is akadályozhatja. Egyes termékek szintetikus teljes mentést készítenek; ott a tényleges függőségeket a termék szerint kell ellenőrizni.

A RAID egyes lemezhibák mellett fenntarthatja a rendelkezésre állást, de a törlést vagy a titkosított adatot is továbbviheti. A szinkronizálás ugyanezt több helyen is megismételheti. A backup értékét a korábbi, konzisztens állapot tényleges visszaállíthatósága adja. A 3-2-1 elv mellett ezért az elkülönített jogosultság, az offline vagy megfelelően védett változtathatatlan példány és a rendszeres restore-próba is számít.

## Vizsgán jól használható megfogalmazás

> A backup alapelvei közé tartozik a rendszeres mentés,
> a több példányos és elkülönített tárolás,
> valamint a visszaállítás rendszeres tesztelése.  
> A full backup minden adatot ment,
> az incremental csak a legutóbbi mentés óta változott adatokat,
> a differential pedig az utolsó teljes mentés óta történt változásokat.  
> A megfelelő mentési elvet a visszaállítási igény, az idő és a tárhely alapján kell megválasztani.

## Gyors önellenőrzés

1. Mi a full backup?
2. Mi az incremental backup?
3. Mi a differential backup?
4. Mi a 3-2-1 elv lényege?
5. Ugyanaz-e a sync és a backup?

## Rövid válaszok az önellenőrzéshez

1. Minden adat teljes mentése
2. Csak a legutóbbi mentés óta változott adatok mentése
3. Az utolsó teljes mentés óta változott adatok mentése
4. Több példány, több médium, egy elkülönített másolat
5. Nem

## Források

1. BSI - Datensicherung – wie geht das?  
   https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Cyber-Sicherheitsempfehlungen/Daten-sichern-verschluesseln-und-loeschen/Datensicherung-und-Datenverlust/Datensicherung-wie-geht-das/datensicherung-wie-geht-das.html  
   Használat: közérthető, hivatalos magyarázat full és incremental backuphoz.

2. BSI - CON.3 Datensicherungskonzept (Edition 2023)  
   https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Grundschutz/IT-GS-Kompendium_Einzel_PDFs_2023/03_CON_Konzepte_und_Vorgehensweisen/CON_3_Datensicherungskonzept_Edition_2023.pdf?__blob=publicationFile&v=3  
   Használat: elsődleges forrás a backup alapelvekhez, restore teszthez és biztonságos mentési folyamathoz.

3. CISA - Back Up Business Data  
   https://www.cisa.gov/audiences/small-and-medium-businesses/secure-your-business/back-up-business-data  
   Használat: modern, hivatalos összefoglaló a 3-2-1 szabályról és a tesztelés fontosságáról.

4. CISA - Back Up Government Data  
   https://www.cisa.gov/audiences/state-local-tribal-and-territorial-government/secure-us-sltt/back-government-data  
   Használat: további hivatalos gyakorlati példa restore- és rollback-szempontokkal.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [CISA: StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide): elkülönített, titkosított mentések és ellenőrzött helyreállítás

Ellenőrizve: `2026-10-14`.
