# Begriff Betriebssystem

## Gyors vizuális kép

| Réteg              | Szerep                                        |
| ------------------ | --------------------------------------------- |
| felhasználó        | használja a gépet                             |
| alkalmazások       | konkrét feladatokat végeznek                  |
| operációs rendszer | közvetít, kezel, irányít                      |
| hardver            | CPU, RAM, SSD, kijelző, billentyűzet, hálózat |

### Egyszerű modell

```text
Felhasználó
   ↓
Alkalmazás
   ↓
Operációs rendszer
   ↓
Hardver
```

## Mi az operációs rendszer?

Az operációs rendszer, röviden **OS** (`Operating System`), a számítógép központi rendszer-szoftvere.

Feladata, hogy:

- elindítsa és kezelje a folyamatokat
- ossza a processzoridőt
- kezelje a memóriát
- kezelje a fájlokat és mappákat
- kommunikáljon a hardvereszközökkel
- felhasználói felületet adjon
- biztosítsa, hogy más programok szabályosan futhassanak

## Milyen fő feladatai vannak?

### 1. Folyamatkezelés

Az operációs rendszer indítja, ütemezi és leállítja a programokat.

Például:

- böngésző fut
- zenelejátszó fut
- háttérben frissítés fut

Ezeket az OS szervezi.

### 2. Memóriakezelés

Az operációs rendszer dönti el:

- melyik program mennyi memóriát kap
- hogyan lehet elkerülni, hogy a programok egymást felülírják

### 3. Fájlkezelés

Az OS biztosítja a fájlok és mappák kezelését:

- név
- hely
- hozzáférés
- megnyitás
- mentés
- törlés

### 4. Eszközkezelés

Az operációs rendszer kezeli a hardverhez kapcsolódó működést:

- billentyűzet
- egér
- nyomtató
- monitor
- hálózati kártya
- háttértár

### 5. Felhasználói felület

Az OS biztosíthat:

- **grafikus felületet** (`GUI`)
- **parancssoros felületet** (`CLI`)

Példák:

- Windows asztali felület
- Linux terminál
- macOS Finder és menüsor

## Miből áll egy operációs rendszer?

Egyszerű, vizsgán is használható bontás:

- **kernel**: a rendszer magja
- **illesztőprogramok** (`driverek`): hardverkommunikáció
- **fájlrendszer-kezelés**
- **felhasználói felület**
- **rendszerszolgáltatások**

## Miért nélkülözhetetlen?

Operációs rendszer nélkül a felhasználó nem tudna kényelmesen:

- programot indítani
- fájlokat kezelni
- internetet használni
- nyomtatni
- több feladatot futtatni

Az OS teszi használhatóvá a számítógépet.

## Egyszerű példák

| Helyzet                  | Mit csinál az operációs rendszer?                           |
| ------------------------ | ----------------------------------------------------------- |
| megnyitsz egy fájlt      | megkeresi, jogosultságot ellenőriz, átadja az alkalmazásnak |
| elindítasz egy programot | betölti memóriába, elindítja a folyamatot                   |
| csatlakozol Wi-Fi-re     | kezeli a hálózati eszközt és a kapcsolatot                  |
| nyomtatsz                | továbbítja az adatot a megfelelő eszköznek                  |

## Operációs rendszer vs alkalmazás

| Operációs rendszer             | Alkalmazás                      |
| ------------------------------ | ------------------------------- |
| a gép alapműködését biztosítja | konkrét feladatot old meg       |
| kezeli a hardvert              | az OS szolgáltatásait használja |
| például Windows, macOS, Linux  | például Word, Chrome, VLC       |

## Vizsgán jól használható megfogalmazás

> Az operációs rendszer a számítógép alapvető rendszer-szoftvere,
> amely kezeli a hardvererőforrásokat és futtatási környezetet biztosít
> az alkalmazások számára.  
> Kapcsolatot teremt a felhasználó, a programok és a hardver között.  
> Feladata többek között a folyamatkezelés, a memóriakezelés,
> a fájlkezelés, az eszközkezelés
> és a felhasználói felület biztosítása.

## Gyakori vizsgahibák

- Az operációs rendszert összekeverni az alkalmazásokkal.
- Azt mondani, hogy az OS csak „ablakokat jelenít meg”.
- Kihagyni a memória- és folyamatkezelés szerepét.
- Nem tudni példát mondani GUI-ra és CLI-re.
- A kernelt és az egész operációs rendszert teljesen azonosnak venni.

## Gyors önellenőrzés

1. Mi az operációs rendszer fő feladata?
2. Mi a különbség az operációs rendszer és egy alkalmazás között?
3. Milyen erőforrásokat kezel az OS?
4. Miért fontos a folyamatkezelés?
5. Milyen felhasználói felülete lehet egy operációs rendszernek?

## Rövid válaszok az önellenőrzéshez

1. Kezeli a hardvert és környezetet biztosít az alkalmazásoknak
2. Az OS alapot ad, az alkalmazás konkrét feladatot végez
3. CPU, memória, fájlok, eszközök, hálózat
4. Mert egyszerre több program futását kell szervezni
5. Grafikus (`GUI`) és parancssoros (`CLI`)

## Források

1. NIST CSRC Glossary - Operating system  
   https://csrc.nist.gov/glossary/term/operating_system_  
   Használat: szakmai definíciós háttér az operációs rendszer fogalmához.

2. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Használat: az operációs rendszer fő funkciói, például processz-, memória- és fájlkezelés.

3. Microsoft - Windows help and learning  
   https://support.microsoft.com/en-us/windows  
   Használat: közérthető, modern áttekintés a Windows operációs rendszer funkcióiról.

Megnyitva: `2026-04-08`
