# Begriff Firmware

## Gyors vizuális kép

| Fogalom            | Mi ez?                                  | Példa                |
| ------------------ | --------------------------------------- | -------------------- |
| hardver            | fizikai alkatrész                       | alaplap, SSD, router |
| firmware           | az eszközbe írt vezérlőszoftver         | UEFI, SSD firmware   |
| operációs rendszer | a teljes gépet kezelő rendszer-szoftver | Windows, Linux       |
| alkalmazás         | felhasználói program                    | Chrome, Word         |

## Mi a firmware?

A firmware olyan programkód és adat, amely jellemzően a hardverhez kötötten van tárolva, gyakran nem hagyományos fájlként, hanem az eszköz saját memóriájában.

Feladata lehet például:

- a hardver indulásának vezérlése
- alapfunkciók biztosítása
- kommunikáció más hardverelemekkel
- az eszköz működési logikájának biztosítása

## Hol helyezkedik el a firmware?

Általában:

- ROM-ban
- flash memóriában
- más nem felejtő tárolóban

Ezért a firmware „közelebb van a hardverhez”, mint egy normál alkalmazás.

## Tipikus példák

### 1. BIOS / UEFI

Az egyik legismertebb firmware-típus.

Feladata:

- a gép alapindítása
- hardverellenőrzés
- boot folyamat előkészítése
- az operációs rendszer indításának lehetővé tétele

### 2. Router firmware

Feladata:

- hálózati működés irányítása
- admin felület biztosítása
- biztonsági és kapcsolatkezelési funkciók

### 3. SSD vagy HDD firmware

Feladata:

- adattárolási műveletek vezérlése
- hibakezelés
- teljesítményoptimalizálás bizonyos szinten

### 4. Perifériák firmware-e

Például:

- nyomtató
- monitor
- billentyűzet
- egér
- kamera

## Firmware vs szoftver: ne keverd össze

| Firmware                                | „Normál” szoftver                         |
| --------------------------------------- | ----------------------------------------- |
| közvetlenül eszközhöz kötődik           | általános rendszerben fut                 |
| alapműködést vezérel                    | felhasználói vagy rendszerfeladatot végez |
| gyakran flash / ROM jellegű tárolón van | háttértáron települ                       |
| eszközspecifikus                        | gyakran hordozhatóbb                      |

## Firmware vs driver

| Firmware                          | Driver                              |
| --------------------------------- | ----------------------------------- |
| az eszközön van                   | jellemzően az operációs rendszerben |
| az eszköz belső működését vezérli | az OS és az eszköz között közvetít  |
| hardverhez szorosan kötődik       | rendszeroldali illesztőprogram      |

Egyszerűen:

- firmware = eszköz belső vezérlése
- driver = operációs rendszer oldali kapcsolat

## Miért fontos a firmware frissítése?

Mert firmware update javíthat:

- hibákat
- stabilitást
- kompatibilitást
- biztonsági problémákat

De kockázata is van:

- hibás frissítés esetén az eszköz működésképtelenné válhat

Ezért firmware-t csak:

- megbízható forrásból
- pontos modellhez
- körültekintően

szabad frissíteni.

## Vizsgán jól használható megfogalmazás

> A firmware a hardverhez kötött, beágyazott vezérlőszoftver.  
> Általában az eszköz saját nem felejtő memóriájában található, és az alapműködését irányítja.  
> Tipikus példája a BIOS vagy UEFI, de routerekben, SSD-kben és perifériákban is van firmware.  
> A firmware nem ugyanaz, mint az operációs rendszer vagy egy alkalmazás.

## Gyakori vizsgahibák

- A firmware-t összekeverni a driverrel.
- A firmware-t alkalmazásnak nevezni.
- Azt mondani, hogy firmware csak PC-ben létezik.
- Elfelejteni, hogy routerben, SSD-ben, nyomtatóban is van firmware.
- Nem tudni példát mondani BIOS / UEFI-re.

## Gyors önellenőrzés

1. Mi a firmware?
2. Miben különbözik az alkalmazástól?
3. Miben különbözik a drivertől?
4. Mondj két példát firmware-re.
5. Miért lehet szükség firmware-frissítésre?

## Rövid válaszok az önellenőrzéshez

1. Hardverhez kötött beágyazott vezérlőszoftver
2. Az alkalmazás felhasználói program, a firmware az eszköz alapműködését irányítja
3. A firmware az eszközön van, a driver az OS oldalán közvetít
4. BIOS / UEFI, router firmware, SSD firmware
5. Hibajavítás, kompatibilitás, stabilitás, biztonság miatt

## Források

1. NIST CSRC Glossary - firmware  
   https://csrc.nist.gov/glossary/term/firmware  
   Használat: szakmai definíció a firmware fogalmához.

2. Microsoft Support - How to use Surface UEFI  
   https://support.microsoft.com/en-us/surface/how-to-use-surface-uefi-df2c8942-dfa0-859d-4394-95f45eb1c3f9  
   Használat: UEFI mint ma is releváns firmware-példa.

3. Ubuntu Desktop  
   https://ubuntu.com/download/desktop  
   Használat: modern desktop környezetben is előforduló firmware-frissítési gyakorlat kontextusa.

Megnyitva: `2026-04-08`
