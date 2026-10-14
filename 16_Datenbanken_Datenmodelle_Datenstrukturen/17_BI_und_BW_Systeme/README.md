# BI- und BW-Systeme

## Gyors vizuális kép

| Fogalom | Fő szerep |
|---|---|
| `BI` | adatokból információ és üzleti insight |
| `BW` / data warehouse | adatok összegyűjtése, tisztítása, történeti tárolása |

## Mi az a `BI`?

A `BI` olyan módszerek és eszközök összessége, amelyek segítenek:

- riportok készítésében
- adatelemzésben
- trendek felismerésében
- döntéstámogatásban

## Mi az a `BW`?

A `BW` vagy adattárház:

- több forrásból gyűjt adatot
- egységesíti és előkészíti azokat
- elemzésre optimalizált formában tárolja

Gyakran tartalmaz:

- történeti adatokat
- összesített adatokat
- üzleti szempontból strukturált modelleket

## Miért fontos a különbség?

Mert:

- a `BI` inkább a felhasználás és elemzés oldala
- a `BW` inkább az adat-alap és infrastruktúra oldala

## Tipikus kapcsolat

```text
Operatív rendszerek
    -> adatkinyerés / átalakítás
    -> BW / adattárház
    -> BI riportok, dashboardok, elemzés
```

## Mire jók a vállalatban?

- vezetői riportolás
- trendek elemzése
- teljesítménymérés
- stratégiai döntéstámogatás

## `BI`, `BW`, `ERP`: ne keverd össze

| Fogalom | Fókusz |
|---|---|
| `ERP` | operatív vállalati működés |
| `BW` | elemzésre előkészített központi adattárolás |
| `BI` | riportolás és elemzés |

## Kidolgozott riport és az adatok szemcsézettsége

A **BI** üzleti intelligencia és elemzési eszközök összessége. A **BW** gyakran a SAP Business Warehouse termékcsalád nevében szerepel; az általános adattárház megnevezés a data warehouse vagy DWH. Nem minden BI-megoldásnak szükséges külön adattárház, de az egységesített történeti adatok sok elemzést segítenek.

Az operatív, tranzakciós feldolgozás (**OLTP**) egy-egy rendelést rögzít. Az elemző feldolgozás (**OLAP**) sok rendelés összesítését hasonlítja össze. ETL esetén a kinyerés után az átalakítás, majd a betöltés következik; ELT-nél az átalakítás a betöltés után történik.

**MySQL 8.0 / InnoDB, üres gyakorló adatbázis:** itt egy sor egy eladási tétel. Az összeg a mennyiség és egységár szorzatából adódik.

<!-- example:mysql -->
```sql
CREATE TABLE sales (
  id INT PRIMARY KEY,
  category VARCHAR(20) NOT NULL,
  quantity INT NOT NULL,
  unit_price DECIMAL(8,2) NOT NULL
) ENGINE=InnoDB;
INSERT INTO sales VALUES
  (1, 'book', 2, 10.00), (2, 'book', 1, 20.00), (3, 'tool', 3, 5.00);
SELECT category, SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY category
ORDER BY category;
```

```text
book 40.00
tool 15.00
```

Az adattárházi ténytábla mért adatokat, a dimenziók például terméket, dátumot és kategóriát írnak le. Először a sor jelentését, a **szemcsézettséget** kell rögzíteni. Ha tételszintű adathoz a teljes rendelési összeget is minden sorba másoljuk, egy egyszerű összegzés többször számolhatja ugyanazt a bevételt.

A riport mellett legyen világos az időszak, pénznem, nettó/bruttó értelmezés és az utolsó frissítés ideje. Az aggregált szám önmagában nem mondja meg az eltérés okát; ahhoz ellenőrizhető üzleti értelmezés is kell.

## Vizsgán jól használható megfogalmazás

> A `BI` rendszerek az üzleti adatok elemzését, vizualizálását és döntéstámogatását szolgálják.  
> A `BW` vagy adattárház-rendszerek ezzel szemben az adatokat különböző forrásokból összegyűjtik, egységesítik és  
> elemzésre alkalmas formában tárolják.  
> Egyszerűen fogalmazva: a `BW` biztosítja az adatalapot, a `BI` pedig értelmezhető információt és üzleti insightot
> készít belőle.

## Gyors önellenőrzés

1. Mi a `BI` fő célja?
2. Mi a `BW` fő célja?
3. Mi a különbség köztük?
4. Hogyan kapcsolódik az `ERP`-hez?
5. Miért fontos a történeti adattárolás?

## Rövid válaszok az önellenőrzéshez

1. Elemzés és döntéstámogatás
2. Központi adattárolás elemzéshez
3. A `BI` használja, a `BW` előkészíti az adatot
4. Az `ERP` lehet egyik fő adatforrás
5. Mert így trendek is vizsgálhatók

## Források

1. IBM - What is business intelligence (BI)?  
   https://www.ibm.com/topics/business-intelligence  
   Használat: hivatalos, modern forrás a `BI` fogalmához és céljához.

2. SAP - What is a data warehouse?  
   https://www.sap.com/sea/products/data-cloud/datasphere/what-is-a-data-warehouse.html  
   Használat: hivatalos forrás az adattárház szerepéhez.

3. SAP - Business Warehouse in Business Data Cloud  
   https://www.sap.com/products/data-cloud/business-warehouse.html  
   Használat: korszerű, hivatalos forrás a `BW` fogalom vállalati kontextusához.

Megnyitva: `2026-04-09`

### A bővítés ellenőrzött forrásai

- [Microsoft: Star schema](https://learn.microsoft.com/en-us/power-bi/guidance/star-schema): tények, dimenziók és szemcsézettség
- [IBM: Business Intelligence](https://www.ibm.com/think/topics/business-intelligence): elemzés és üzleti értelmezés
- [SAP: Business Warehouse](https://www.sap.com/products/data-cloud/business-warehouse.html): BW mint SAP terméknév

Ellenőrizve: `2026-10-14`.
