# Single-User-System und Multi-User-System

## Gyors vizuális kép

| Típus | Jellemző |
|---|---|
| single-user | jellemzően egy fő használja egyszerre |
| multi-user | több felhasználó, fiókok, jogosultságok, elkülönítés |

## Mi az a single-user rendszer?

Olyan rendszer, amelyet tipikusan egyetlen felhasználó használ közvetlenül.

Példák:

- otthoni PC egyetlen aktív felhasználóval
- egyéni laptophasználat
- egyszerű beágyazott rendszerek bizonyos esetei

Fontos:

- attól még lehet több felhasználói fiók
- a lényeg inkább az, hogy a használat modellje egy felhasználóra épül

## Mi az a multi-user rendszer?

Olyan rendszer, amely több felhasználó számára biztosít hozzáférést, elkülönített jogosultságokat és erőforráskezelést.

Tipikusan támogat:

- külön felhasználói fiókokat
- jogosultsági szinteket
- párhuzamos hozzáférést
- erőforrásmegosztást
- adminisztrációt

Példák:

- Linux szerver
- Windows Server
- vállalati terminál- vagy szerverkörnyezet

## A legfontosabb különbség

| Szempont | Single-user | Multi-user |
|---|---|---|
| elsődleges használat | egy felhasználó | több felhasználó |
| jogosultsági rendszer | egyszerűbb is lehet | általában részletesebb |
| párhuzamos hozzáférés | nem ez a fő cél | igen, tipikus cél |
| adminisztráció | egyszerűbb | összetettebb |

## Mit kell tudni vizsgán?

Nem az a fő kérdés, hogy hány ember „ül a gép előtt”, hanem hogy a rendszer:

- támogat-e több felhasználói identitást
- tud-e jogosultságokat kezelni
- tud-e erőforrásokat több user között szabályozni

## Példák

### Single-user példák

- otthoni Windows PC
- személyes MacBook
- saját fejlesztői laptop

### Multi-user példák

- Linux szerver több user accounttal
- egyetemi vagy céges szerver
- terminálszerver
- több adminnal és felhasználóval működő rendszerek

## Fontos pontosítás

Egy modern operációs rendszer lehet:

- **multitasking**
- és közben **single-user használatú**

vagy:

- **multi-user**
- és közben szintén **multitasking**

Tehát:

- a single-user / multi-user és a multitasking **nem ugyanaz a kérdés**

## Biztonsági jelentőség

A multi-user rendszerekben különösen fontos:

- hitelesítés
- jogosultságkezelés
- elkülönítés
- naplózás

Mert több user osztozik ugyanazon a rendszeren vagy infrastruktúrán.

## Vizsgán jól használható megfogalmazás

> A single-user rendszer elsősorban egy felhasználó közvetlen használatára készült.  
> A multi-user rendszer ezzel szemben több felhasználó számára is képes hozzáférést, külön jogosultságokat és elkülönített munkakörnyezetet biztosítani.  
> A multi-user rendszerek tipikusan szerveres vagy vállalati környezetben fontosak.

## Gyakori vizsgahibák

- Összekeverni a multi-user és a multitasking fogalmát.
- Azt hinni, hogy ha több user account van, akkor az automatikusan teljes értékű multi-user működés.
- Azt mondani, hogy minden desktop gép csak single-user lehet.
- Nem említeni a jogosultságkezelést.
- Nem tudni szerverpéldát mondani.

## Gyors önellenőrzés

1. Mi a single-user rendszer lényege?
2. Mi a multi-user rendszer lényege?
3. Mondj egy multi-user példát.
4. Ugyanaz-e a multi-user és a multitasking?
5. Miért fontos a jogosultságkezelés a multi-user rendszereknél?

## Rövid válaszok az önellenőrzéshez

1. Egy felhasználó használatára épülő működés
2. Több felhasználó kezelésére és elkülönítésére képes
3. Linux szerver vagy Windows Server
4. Nem
5. Mert több user osztozik a rendszer erőforrásain

## Források

1. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Használat: single-user és enterprise / multi-user kontextus, jogosultságok és erőforráskezelés.

2. IBM - Mainframe Operating Systems  
   https://www.ibm.com/products/z/operating-systems  
   Használat: több felhasználót és nagyvállalati környezetet kiszolgáló OS-ek példái.

3. Microsoft - Windows help and learning  
   https://support.microsoft.com/en-us/windows  
   Használat: modern desktop single-user használati kontextus példája.

Megnyitva: `2026-04-08`
