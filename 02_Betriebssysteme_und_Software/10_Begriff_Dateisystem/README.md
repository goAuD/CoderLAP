# Begriff Dateisystem

## Gyors vizuális kép

| Fogalom          | Mit jelent?                          |
| ---------------- | ------------------------------------ |
| fájl             | logikailag összetartozó adat         |
| mappa / könyvtár | fájlok rendezése                     |
| fájlrendszer     | a tárolás és elérés szabályrendszere |
| háttértár        | fizikai vagy logikai tároló          |

## Mi az a fájlrendszer?

A fájlrendszer szabályozza:

- a fájlneveket
- a könyvtárstruktúrát
- a tárolási helyeket
- a hozzáférést
- az olvasási és írási műveleteket

Nélküle a rendszer nem tudna normálisan:

- menteni
- megnyitni
- törölni
- rendezni

adatokat.

## Milyen feladatai vannak?

### 1. Névkezelés

Megadja, hogyan lehet fájlokat és mappákat elnevezni.

### 2. Szervezés

Lehetővé teszi a mappákba rendezést.

### 3. Tárolás

Nyilvántartja, hogy az adat fizikailag vagy logikailag hol található.

### 4. Hozzáférés

Biztosítja, hogy a rendszer meg tudja nyitni és kezelni a fájlokat.

### 5. Jogosultságok és attribútumok

Sok fájlrendszer tárol:

- jogosultságokat
- időbélyegeket
- méretet
- egyéb metaadatokat

## Hol találkozol vele?

Minden olyan helyen, ahol fájlokat használsz:

- SSD
- HDD
- USB pendrive
- memória-kártya
- külső lemez
- hálózati megosztás

## Gyakori fájlrendszerek

| Fájlrendszer | Tipikus környezet                             |
| ------------ | --------------------------------------------- |
| `NTFS`       | Windows                                       |
| `ReFS`       | Windows Server környezetekben bizonyos esetek |
| `exFAT`      | cserélhető adathordozók                       |
| `ext4`       | Linux                                         |
| `APFS`       | Apple rendszerek                              |

## Fájlrendszer vs háttértár

| Háttértár                   | Fájlrendszer               |
| --------------------------- | -------------------------- |
| fizikai vagy logikai tároló | a tárolás szabályrendszere |
| például SSD vagy HDD        | például NTFS vagy ext4     |

Példa:

- egy SSD lehet hardver
- ezen lehet `NTFS` vagy más fájlrendszer

## Fájlrendszer vs fájl

| Fájl                  | Fájlrendszer                         |
| --------------------- | ------------------------------------ |
| egyetlen adatobjektum | az összes fájl kezelésének rendszere |

## Fájlrendszer vs mappa

| Mappa                   | Fájlrendszer                                 |
| ----------------------- | -------------------------------------------- |
| a szervezés egyik eleme | a teljes tárolási struktúra szabályrendszere |

## Miért fontos?

Mert a fájlrendszer hatással lehet:

- kompatibilitásra
- sebességre
- maximális fájlméretre
- megbízhatóságra
- jogosultságkezelésre

## Egyszerű gyakorlati példa

Ha egy pendrive `exFAT`-ra van formázva:

- több rendszer is könnyebben kezelheti

Ha egy Windows rendszerlemez `NTFS`:

- támogatott a Windows általános használatára

Ha Linux rendszerpartícióról van szó:

- gyakori az `ext4`

## Kidolgozott eset: egy 6 GiB-os videó másolása

A pendrive-on 20 GiB szabad hely van, de FAT32 fájlrendszerrel egy 6 GiB-os fájl mégsem tárolható rajta. A FAT32 fájlméretének felső határa `2^32 - 1` bájt, vagyis 4 GiB mínusz 1 bájt. A szabad összkapacitás és az egyetlen fájlra vonatkozó korlát külön tulajdonság.

Ha mindkét célrendszer támogatja, exFAT alkalmas lehet a nagy fájl átvitelére. Ha Windows-jogosultságok is szükségesek, NTFS lehet megfelelőbb. Újraformázás előtt a meglévő adatokat mentjük, mert a formázás adatvesztést okozhat.

Egy fizikai lemezen több **partíció** is lehet; a fájlrendszer tipikusan egy köteten szervezi a fájlokat, azon belül a **könyvtár** a rendszerezést szolgálja. A naplózás (`journaling`) az összeomlás utáni konzisztencia helyreállítását segíti. A véletlen törlés vagy az eszköz elvesztése ellen külön biztonsági mentés kell.

## Vizsgán jól használható megfogalmazás

> A fájlrendszer olyan szoftveres mechanizmus vagy szabályrendszer,
> amely meghatározza, hogyan nevezzük el, tároljuk, rendezzük
> és érjük el a fájlokat a háttértáron.  
> A fájlrendszer kezeli a könyvtárstruktúrát, a hozzáférést és gyakran a metaadatokat is.  
> Tipikus példák az NTFS, exFAT, ext4 vagy APFS.

## Gyors önellenőrzés

1. Mi a fájlrendszer feladata?
2. Mi a különbség a háttértár és a fájlrendszer között?
3. Mondj két fájlrendszer-példát.
4. Miért fontos a fájlrendszer a fájlok eléréséhez?
5. Hol találkozunk fájlrendszerekkel?

## Rövid válaszok az önellenőrzéshez

1. A fájlok elnevezését, tárolását, szervezését és elérését szabályozza
2. A háttértár a tároló, a fájlrendszer a használat szabályrendszere
3. NTFS, exFAT, ext4, APFS
4. Mert ez mondja meg, hol van a fájl és hogyan férünk hozzá
5. SSD-n, HDD-n, pendrive-on, hálózati tárhelyen is

## Források

1. NIST CSRC Glossary - File System  
   https://csrc.nist.gov/glossary/term/file_system  
   Használat: a fájlrendszer fogalmának technikai definíciója.

2. Microsoft Learn - ReFS overview  
   https://learn.microsoft.com/en-us/windows-server/storage/refs/refs-overview  
   Használat: modern Windows fájlrendszer-példa és fájlrendszer-jellemzők.

3. Red Hat Enterprise Linux - Managing file systems  
   https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_file_systems/  
   Használat: Linuxos fájlrendszer-kezelési háttér és rendszeres fogalmak.

4. Apple Developer Documentation - Files and directories  
   https://developer.apple.com/documentation/technologyoverviews/files-and-directories  
   Használat: modern Apple fájlrendszer-környezet és APFS-kontextus.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [Microsoft: File System Functionality Comparison](https://learn.microsoft.com/en-us/windows/win32/fileio/filesystem-functionality-comparison): méretkorlát, jogosultságok, naplózás.

Ellenőrizve: `2026-10-14`.
