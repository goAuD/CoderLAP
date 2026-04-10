# Primaerschluessel, Fremdschluessel, Relationen

## Gyors vizuális kép

| Fogalom | Szerep |
|---|---|
| elsődleges kulcs | egyedi rekordazonosító |
| idegen kulcs | hivatkozás másik táblára |
| reláció | kapcsolat két tábla között |

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

- egy másik tábla kulcsára hivatkozik
- kapcsolatot hoz létre
- segíti a referenciális integritást

Példa:

ha az `Orders` táblában van `CustomerID`, ami a `Customers` táblára mutat, akkor ez tipikus idegen kulcs.

## Mi az a reláció?

Reláció alatt ebben a témában jellemzően a táblák közti kapcsolatot értjük.

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
| szerep | saját tábla rekordjának azonosítása | másik tábla rekordjára mutat |
| egyediség | kötelező | nem feltétlenül egyedi |
| `NULL` | nem lehet | szabálytól függően lehet vagy nem |

## Vizsgán jól használható megfogalmazás

> Az elsődleges kulcs egy rekord egyedi azonosítására szolgál egy táblán belül.  
> Az idegen kulcs ezzel szemben egy másik tábla kulcsára hivatkozik, és így kapcsolatot hoz létre a táblák között.  
> A relációk segítségével a külön tárolt adatok összekapcsolhatók, ami a relációs adatbázis-modell alapja.

## Gyakori vizsgahibák

- Az elsődleges kulcsot idegen kulcsnak nevezni.
- A reláció fogalmát pusztán “táblának” fordítani.
- Nem megemlíteni az egyediséget.
- Az `n:m` kapcsolatnál elfelejteni a kapcsolótáblát.

## Gyors önellenőrzés

1. Mi az elsődleges kulcs?
2. Mi az idegen kulcs?
3. Mire jó a reláció?
4. Mi az `1:n` kapcsolat?
5. Hogyan oldjuk meg az `n:m` kapcsolatot?

## Rövid válaszok az önellenőrzéshez

1. Egyedi rekordazonosító
2. Másik tábla kulcsára mutató mező
3. Táblák összekapcsolására
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
