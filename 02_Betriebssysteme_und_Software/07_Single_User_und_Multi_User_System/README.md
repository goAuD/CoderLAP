# Single-User-System und Multi-User-System

## Gyors vizuális kép

| Típus       | Jellemző                                             |
| ----------- | ---------------------------------------------------- |
| single-user | jellemzően egy fő használja egyszerre                |
| multi-user  | több felhasználó, fiókok, jogosultságok, elkülönítés |

## Mi az a single-user rendszer?

A klasszikus single-user rendszer egy felhasználó munkájára készült, több felhasználó elkülönített, egyidejű munkamenetének támogatása nélkül. Történeti példa a személyi gépeken használt MS-DOS.

Külön fogalom a **single-user használat**: egy modern, több fiókot és jogosultságokat kezelő operációs rendszert is használhat éppen egyetlen ember. Ettől az OS felhasználókezelési képessége nem változik meg.

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

| Szempont              | Single-user         | Multi-user             |
| --------------------- | ------------------- | ---------------------- |
| elsődleges használat  | egy felhasználó     | több felhasználó       |
| jogosultsági rendszer | egyszerűbb is lehet | általában részletesebb |
| párhuzamos hozzáférés | nem ez a fő cél     | igen, tipikus cél      |
| adminisztráció        | egyszerűbb          | összetettebb           |

## Mit kell tudni vizsgán?

Nem az a fő kérdés, hogy hány ember „ül a gép előtt”, hanem hogy a rendszer:

- támogat-e több felhasználói identitást
- tud-e jogosultságokat kezelni
- tud-e erőforrásokat több user között szabályozni

## Példák

### Egyfelhasználós használati helyzetek modern OS-en

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

## Kidolgozott eset: közös iskolai számítógép

Anna és Béla külön fiókkal használja ugyanazt a gépet. A saját fájljaikhoz külön hozzáférési szabályok tartoznak, a karbantartáshoz külön adminisztrátori fiók van. A gépnek akkor is van többfelhasználós biztonsági modellje, ha a helyi képernyőn egyszerre csak egyikük dolgozik.

Három kérdést vizsgálunk külön:

1. Vannak-e elkülönített felhasználói identitások és jogosultságok?
2. Maradhat-e több munkamenet bejelentkezve, illetve dolgozhatnak-e egyidejűleg?
3. Milyen kiadás, szolgáltatás és licenc engedi a távoli munkameneteket?

A Windows, a macOS és a Linux modern rendszerei nem írhatók le pusztán azzal, hogy „asztali gép, tehát single-user”. A többfelhasználós képesség és az egyszerre használható interaktív asztalok száma külön tulajdonság. Az egyes Windows kliens- és szerverkiadások munkamenet-korlátai eltérhetnek.

## Vizsgán jól használható megfogalmazás

> A single-user rendszer elsősorban egy felhasználó közvetlen használatára készült.  
> A multi-user rendszer ezzel szemben több felhasználó számára is képes
> hozzáférést, külön jogosultságokat
> és elkülönített munkakörnyezetet biztosítani.  
> A multi-user rendszerek tipikusan szerveres vagy vállalati környezetben fontosak.

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

### A bővítés ellenőrzött forrásai

- [Microsoft: Manage user accounts](https://support.microsoft.com/en-us/windows/security/identity-signin/manage-user-accounts-in-windows): külön fiókok és hozzáférések modern Windows alatt.

Ellenőrizve: `2026-10-14`.
