# Primaerschluessel, Fremdschluessel, Relationen

## Gyors vizuális kép

| Fogalom | Szerep |
|---|---|
| elsődleges kulcs | egyedi rekordazonosító |
| idegen kulcs | hivatkozás ugyanannak vagy másik táblának a kulcsára |
| reláció | a relációs modellben sorok (tuple-ök) halmaza, táblázatosan ábrázolva |

## Mi az elsődleges kulcs?

Az elsődleges kulcs:

- egyedileg azonosít egy sort
- nem lehet `NULL`
- nem ismétlődhet

Példa:

- `CustomerID`
- `OrderID`

## Mi az idegen kulcs?

Az idegen kulcs:

- egy hivatkozott kulcsra mutat, akár ugyanabban a táblában
- kapcsolatot hoz létre
- segíti a referenciális integritást

Példa:

ha az `Orders` táblában van `CustomerID`, ami a `Customers` táblára mutat, akkor ez tipikus idegen kulcs.

## Mi az a reláció?

A relációs modellben a reláció sorok, vagyis tuple-ök halmaza, amelyet táblaként ábrázolunk. A táblák közti kapcsolatot pontosabban kapcsolatnak vagy relationshipnek nevezzük. A két fogalom összefügg, de nem azonos.

Tipikus kapcsolatok:

- egy-egyhez (`1:1`)
- egy-többhöz (`1:n`)
- több-többhöz (`n:m`)

Az `n:m` kapcsolatot általában kapcsolótáblával oldjuk meg.

## Miért fontosak?

- rendezett adatstruktúrát adnak
- összekapcsolják a táblákat
- támogatják a lekérdezéseket és integritást

## Elsődleges kulcs és idegen kulcs: ne keverd össze

| Szempont | Elsődleges kulcs | Idegen kulcs |
|---|---|---|
| szerep | saját tábla rekordjának azonosítása | hivatkozott kulcsot kapcsol egy sorhoz |
| egyediség | kötelező | nem feltétlenül egyedi |
| `NULL` | nem lehet | szabálytól függően lehet vagy nem |

## Kidolgozott kapcsolatok és kötelezőség

| Követelmény | Megvalósítás |
|---|---|
| egy ügyfélnek több rendelése lehet | `orders.customer_id` idegen kulcs, nem egyedi |
| egy személynek legfeljebb egy profilja lehet | `profiles.person_id` idegen kulcs és UNIQUE |
| egy tanuló több kurzusra járhat, és fordítva | `enrollments` kapcsolótábla két idegen kulccsal |
| egy dolgozónak lehet felettese | nullable `employees.manager_id`, amely `employees.id`-re hivatkozik |

A `NOT NULL` a hivatkozást kötelezővé teszi. A `UNIQUE` legfeljebb egy kapcsolódó sort enged, de önmagában nem biztosítja, hogy minden személyhez létre is jöjjön profil. Az idegen kulcs logikai megszorítás: a `customer_id` oszlopnév önmagában még nem hozza létre.

Törlésnél külön döntés szükséges. A `RESTRICT` megakadályozhatja egy hivatkozott szülő törlését, a `CASCADE` a gyermekekre is továbbviszi a törlést, a `SET NULL` pedig csak nullable hivatkozásnál használható. Válassz a megőrzendő üzleti történet szerint. Egy ügyfélhez tartozó számlákat például nem célszerű pusztán kényelmi okból automatikusan eltüntetni.

## Vizsgán jól használható megfogalmazás

> Az elsődleges kulcs egy sor egyedi, nem NULL azonosítója; több oszlopból is állhat. Az idegen kulcs egy hivatkozott kulccsal biztosít referenciális kapcsolatot. Az n:m kapcsolatot kapcsolótáblával ábrázoljuk. A reláció a relációs modell sorhalmaza, nem egyszerűen a táblák közti kapcsolat másik neve.

## Gyors önellenőrzés

1. Mi az elsődleges kulcs?
2. Mi az idegen kulcs?
3. Mi a reláció és a táblák közti kapcsolat különbsége?
4. Mi az `1:n` kapcsolat?
5. Hogyan oldjuk meg az `n:m` kapcsolatot?

## Rövid válaszok az önellenőrzéshez

1. Egyedi rekordazonosító
2. Hivatkozott kulcsra mutató oszlop vagy oszlopcsoport, akár ugyanazon táblában
3. A reláció tuple-ök halmaza; a kapcsolat a tárolt entitások összefüggése
4. Egy rekordhoz több kapcsolódó rekord tartozhat
5. Kapcsolótáblával

## Források

1. Microsoft Support - Database design basics  
   https://support.microsoft.com/en-us/office/database-design-basics-eb2159cf-1e30-401a-8084-bd4f9c9ca1f5  
   Használat: hivatalos, jól szemléltető forrás a kulcsokhoz és kapcsolatokhoz.

2. Microsoft Support - Guide to table relationships  
   https://support.microsoft.com/en-us/office/guide-to-table-relationships-30446197-4fbe-457b-b992-2f6fb812b58f  
   Használat: hivatalos forrás a relációk és elsődleges / idegen kulcsok gyakorlati értelmezéséhez.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [PostgreSQL: Glossary, Relation](https://www.postgresql.org/docs/current/glossary.html#GLOSSARY-RELATION): a reláció mint tuple-halmaz definíciója
- [MySQL: FOREIGN KEY constraints](https://dev.mysql.com/doc/refman/8.0/en/create-table-foreign-keys.html): hivatkozások és törlési szabályok

Ellenőrizve: `2026-10-14`.
