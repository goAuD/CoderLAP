# Urheberrecht Grundbegriffe

## Gyors vizuális kép

| Fogalom | Rövid jelentés |
|---|---|
| szerző | aki az alkotást létrehozta |
| mű | jogilag védhető alkotás |
| felhasználás | másolás, közzététel, terjesztés, feltöltés stb. |
| licenc | engedély a felhasználásra |
| jogsértés | felhasználás a szükséges engedély vagy törvényi megengedés nélkül |

## Mi a szerzői jog célja?

A szerzői jog célja:

- a szerző alkotásának védelme
- a szerző rendelkezési jogának biztosítása
- annak szabályozása, ki, hogyan és milyen feltételekkel használhat fel egy művet

## Mi számít műnek?

Védelem alá eshet például:

- irodalmi mű
- zenei mű
- fénykép
- grafika
- film
- szoftver

Vizsgán érdemes így gondolkodni:

- ha van egyéni, szellemi alkotásjelleg, akkor lehet szerzői jogi védelem

## Mi nem védett ugyanígy?

Önmagában nem a puszta ötlet védett.

Példa:

- "csináljunk egy webshopot használt könyveknek" mint ötlet önmagában nem szerzői jogi védelem tárgya
- a konkrét megvalósítás, a szöveg, a dizájn, a kód, a grafika viszont lehet védett

## Milyen jogai vannak a szerzőnek?

Egyszerűsítve a szerző dönt arról, hogy a mű:

- másolható-e
- terjeszthető-e
- nyilvánosan hozzáférhetővé tehető-e
- módosítható-e

Ezért fontos a licenc vagy engedély.

## Mi a licenc?

A **licenc** felhasználási engedély.

Ez megmondhatja például:

- mire használható a mű
- meddig használható
- ingyenes-e vagy fizetős
- módosítható-e
- kereskedelmi célra használható-e

Szoftvernél ez különösen fontos.

## Mit jelent ez IT-s környezetben?

Gyakorlati példák:

- nem tölthetek fel csak úgy más képét a weboldalamra
- nem másolhatok be idegen forráskódot engedély nélkül
- zenét videóhoz a megfelelő felhasználási jogok tisztázása után használok
- open source szoftvernél is meg kell nézni a licenc feltételeit

## Ne keverd össze

| Fogalom | Mit jelent? |
|---|---|
| szerzői jog | az alkotás jogi védelme |
| tulajdonjog | a fizikai hordozó vagy tárgy tulajdona |
| licenc | felhasználási engedély |
| ötlet | önmagában nem ugyanúgy védett, mint a kész mű |

## Licencellenőrzés egy szoftver kiadásakor

Egy projekt saját kódot, külső könyvtárat, ikont és betűtípust tartalmaz.
Mindegyikhez külön megkeressük a jogosultat és a tényleges licencet.
Az „ingyen letölthető” az árról szól, nem a másolás, módosítás és továbbadás teljes jogáról.
Egy nyilvános Git-repozitórium sem ad automatikusan tetszőleges felhasználási engedélyt.

**Példa:** Apache-2.0 licencű könyvtárat csomagolunk az alkalmazással.
Továbbadáskor mellékeljük a licencet, megőrizzük az előírt jogi közléseket,
a módosított fájlokon jelöljük a változtatást, és ha a csomag releváns `NOTICE`
közléseket tartalmaz, azokat is megtartjuk a licenc által megengedett módon.
A licenc nem ad általános jogot a szerző védjegyeinek használatára.
Más licenc, például egy copyleft licenc eltérő kötelezettségeket írhat elő;
a konkrét terjesztési módhoz olvassuk el a feltételeket.

A szerzői jog a védhető alkotás létrejöttével keletkezik, nem egy `©` felirat
hozza létre. Engedély mellett törvényben meghatározott szabad felhasználás is létezhet,
de annak feltételeit külön ellenőrizni kell. A forrás megnevezése önmagában
nem pótolja az engedélyt. Szoftvernél külön szabályok vannak: például a szükséges
biztonsági másolat készítését az UrhG 40d. § a jogszerű használóhoz és a szükségességhez köti.

**Átadandó eredmény:** rövid függőség- és licenclista, a szükséges licencfájlokkal.
Ez később a projekt költöztetését és kiadását is ellenőrizhetővé teszi.

Források: [RIS: UrhG 40a](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001848&Paragraf=40a),
[UrhG 40d](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001848&Paragraf=40d),
[Apache License 2.0, 4. és 6. pont](https://www.apache.org/licenses/LICENSE-2.0).
Ellenőrizve: 2026-10-14.

## Vizsgán jól használható megfogalmazás

> A szerzői jog az egyéni szellemi alkotásokat védi, például szövegeket, képeket, zenéket vagy szoftvereket.  
> Nem az ötlet önmagában, hanem a konkrét alkotás áll védelem alatt.  
> A mű felhasználásához általában a szerző engedélye vagy megfelelő licenc szükséges.

## Gyors önellenőrzés

1. Mit véd a szerzői jog?
2. Mi a különbség az ötlet és a mű között?
3. Mi a licenc?
4. Lehet-e a szoftver szerzői jogi védelem alatt?
5. Felhasználható-e bármi csak azért, mert fent van az interneten?

## Rövid válaszok az önellenőrzéshez

1. Az egyéni szellemi alkotásokat
2. Az ötlet önmagában nem, a konkrét alkotás igen lehet védett
3. Felhasználási engedély
4. Igen
5. Nem

## Források

1. RIS - Urheberrechtsgesetz, geltende Fassung  
   https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001848  
   Használat: az osztrák szerzői jog elsődleges jogforrása.

2. RIS - Urheberrechtsgesetz § 1  
   https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001848&Paragraf=1&Uebergangsrecht=  
   Használat: a védett mű fogalmának jogi kiindulópontja.

3. oesterreich.gv.at - Was ist das Urheberrecht?  
   https://www.oesterreich.gv.at/themen/onlinesicherheit_internet_und_neue_medien/internet_und_handy___sicher_durch_die_digitale_welt/7/Seite.1720410.html  
   Használat: közérthető osztrák kormányzati magyarázat internetes és digitális példákkal.

Megnyitva: `2026-04-08`
