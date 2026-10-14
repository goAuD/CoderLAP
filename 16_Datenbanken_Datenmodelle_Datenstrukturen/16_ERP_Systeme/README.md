# ERP-Systeme

## Gyors vizuális kép

| ERP modul | Példa |
|---|---|
| pénzügy | könyvelés, költségek |
| beszerzés | rendelés, szállító |
| raktár / logisztika | készletkezelés |
| HR | dolgozói adatok |
| termelés / projekt | ütemezés, erőforrások |

## Mi az ERP lényege?

Az `ERP` fő célja, hogy a vállalat különböző területei:

- ne elszigetelten működjenek
- ugyanazokra vagy összehangolt adatokra támaszkodjanak
- átláthatóbb folyamatok mentén dolgozzanak

## Miért fontos adatbázis-szempontból?

Az `ERP` rendszerek:

- sokféle üzleti adatot kezelnek
- integrált adatmodellt igényelnek
- erős konzisztencia- és jogosultságkezelést használnak
- tipikusan tranzakciós adatbázisokra támaszkodnak

## Fő előnyök

- egységesebb adatkezelés
- kevesebb duplikált adat
- jobb folyamatintegráció
- jobb riportolhatóság és átláthatóság

## Lehetséges hátrányok vagy kihívások

- bevezetése összetett lehet
- drága és hosszú projekt lehet
- erős szervezeti változást igényelhet
- testreszabás és migráció bonyolult lehet

## ERP és `BIS`: ne keverd össze

| Fogalom | Jelentés |
|---|---|
| `BIS` | tágabb vállalati információs rendszer fogalom |
| `ERP` | integrált vállalatirányítási rendszer |

Az `ERP` gyakran a `BIS` egyik legfontosabb része.

## Kidolgozott ERP-folyamat: beszerzéstől készletig

Egy vállalkozás tíz hálózati adaptert rendel. A beszerzés rendelést hoz létre a közös szállítói és cikktörzsből. A raktár nyolc beérkezett darabot rögzít, tehát két darab még nyitott mennyiség. A beérkező számla tíz darabról szól. A rendelés, áruátvétel és számla összevetése eltérést jelez; a folyamatnak ezt kezelnie kell, nem egyszerűen minden modult ugyanarra az értékre állítani.

A közös cikkazonosító összeköti a beszerzést, készletet és könyvelési folyamatot. A szerepkörök ettől még eltérnek: nem minden raktári dolgozó módosíthat szállítói bankszámlát vagy hagyhat jóvá kifizetést.

Bevezetéskor tisztítani kell a duplikált törzsadatokat, megtervezni az importot, az interfészeket és az oktatást. Egy jó elfogadási próba normál rendelést, részszállítást, visszárut és hibás adat javítását is tartalmaz. Migrációnál darabszámokat és egyeztethető egyenlegeket is ellenőrizz.

Az integrált ERP nem feltétlenül egyetlen fizikai adatbázis. A lényeg a következetes üzleti azonosítók és összehangolt folyamatok használata. A több rendszer közti hibákhoz egyértelmű státuszok, újrapróbálás és egyeztetés szükséges.

## Vizsgán jól használható megfogalmazás

> Az `ERP` rendszer egy integrált vállalatirányítási rendszer, amely több üzleti terület, például a pénzügy,  
> beszerzés, raktározás vagy HR folyamatait közös rendszerben kezeli.  
> Az `ERP` célja az egységes adatkezelés, a folyamatok összehangolása és a jobb átláthatóság.  
> Adatbázis-szempontból az `ERP` rendszerek nagy, integrált és konzisztensen kezelt adatkörnyezetre épülnek.

## Gyors önellenőrzés

1. Mi az `ERP` fő célja?
2. Milyen területeket foghat össze?
3. Miért fontos hozzá az integrált adatkezelés?
4. Mi az egyik előnye?
5. Mi az egyik tipikus bevezetési kihívása?

## Rövid válaszok az önellenőrzéshez

1. A vállalati folyamatok integrálása
2. Pénzügy, beszerzés, raktár, HR stb.
3. Mert ugyanazokkal az adatokkal dolgoznak a területek
4. Egységesebb működés
5. Összetett bevezetés és testreszabás

## Források

1. Oracle - Enterprise Resource Planning (ERP)  
   https://www.oracle.com/erp/  
   Használat: hivatalos, modern forrás az ERP rendszer céljához és tipikus moduljaihoz.

2. SAP - What is SAP Cloud ERP?  
   https://www.sap.com/products/erp.html  
   Használat: hivatalos forrás az ERP integrált vállalati szerepének gyakorlati bemutatásához.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [SAP: What is ERP?](https://www.sap.com/resources/what-is-erp): integrált üzleti területek és bevezetési szempontok
- [Oracle: Matching Invoice Lines](https://docs.oracle.com/en/cloud/saas/financials/25d/fappp/matching-invoice-lines.html): rendelés, áruátvétel és számla egyeztetése

Ellenőrizve: `2026-10-14`.
