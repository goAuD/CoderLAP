# Multitasking Betriebssystem

## Gyors vizuális kép

| Helyzet | Mit csinál a multitasking OS? |
|---|---|
| böngésző + zene + letöltés | ütemezi a folyamatokat |
| több ablak nyitva | kezeli a CPU-időt és a memóriát |
| háttérfrissítés fut | a háttér- és előtérfeladatokat együtt szervezi |

## Mi az a multitasking?

A multitasking azt jelenti, hogy az operációs rendszer több folyamatot kezel egy időben.

Ez lehet:

- valódi párhuzamosság több CPU-mag esetén
- gyors váltogatás egy magon, ami a felhasználónak egyidejű futásnak látszik

## Mit csinál ilyenkor az operációs rendszer?

Az OS:

- ütemezi a feladatokat
- CPU-időt oszt
- memóriát kezel
- eldönti, melyik folyamat mikor fusson
- biztosítja, hogy a folyamatok ne zavarják egymást

## Példa a gyakorlatból

Egy laptopon fut egyszerre:

- böngésző
- Teams vagy chat
- vírusvédelem
- fájlszinkronizálás
- zenelejátszó

Ha az OS nem tudna multitaskingot:

- csak egy feladatot lehetne egyszerre normálisan végezni

## Miért hasznos?

- javítja a felhasználói élményt
- növeli a hatékonyságot
- lehetővé teszi a háttérfeladatokat
- segíti a modern alkalmazások együttélését

## Előtér- és háttérfeladatok

Egy multitasking rendszer tud kezelni:

- **előtérben futó** feladatokat
- **háttérben futó** feladatokat

Példák:

- előtér: dokumentumszerkesztés
- háttér: frissítés, szinkronizálás, antivírus

## Kapcsolódó fogalmak

### Folyamat (`process`)

Egy futó program példánya.

### Szál (`thread`)

Egy folyamaton belüli végrehajtási egység.

### Ütemezés (`scheduling`)

Az a mechanizmus, amellyel az OS eldönti, melyik feladat mikor fusson.

## Multitasking vs multiprocessing

| Fogalom | Jelentés |
|---|---|
| multitasking | több feladat kezelése egy operációs rendszerben |
| multiprocessing | több processzor / több mag használata |

A kettő kapcsolódik, de nem ugyanaz.

## Multitasking vs multithreading

| Fogalom | Jelentés |
|---|---|
| multitasking | több folyamat / feladat kezelése rendszer-szinten |
| multithreading | egy programon belüli több szál használata |

## Vizsgán jól használható megfogalmazás

> A multitasking operációs rendszer képes több folyamat vagy feladat kezelésére úgy, hogy azok a felhasználó számára egyidejűnek tűnjenek.  
> Ehhez a rendszer ütemezi a folyamatokat, CPU-időt oszt, memóriát kezel és koordinálja a háttér- és előtérfeladatokat.  
> A modern desktop operációs rendszerek általában multitasking rendszerek.

## Gyakori vizsgahibák

- A multitaskingot összekeverni a többmagos processzorral.
- Azt mondani, hogy multitasking csak valódi párhuzamosság lehet.
- Nem tudni példát mondani háttérfolyamatra.
- A folyamat és a program fogalmát teljesen azonosnak venni.
- A multitaskingot összekeverni a multithreadinggel.

## Gyors önellenőrzés

1. Mit jelent a multitasking?
2. Mi a multitasking operációs rendszer feladata?
3. Mondj egy előtér- és egy háttérfeladat példát.
4. Ugyanaz-e a multitasking és a multiprocessing?
5. Miért fontos az ütemezés?

## Rövid válaszok az önellenőrzéshez

1. Több feladat kezelése egy időben
2. CPU-idő, memória és folyamatok kezelése
3. Előtér: böngésző, háttér: frissítés vagy szinkronizálás
4. Nem, a multiprocessing a több processzormag használatára utal
5. Mert el kell dönteni, melyik feladat mikor kap erőforrást

## Források

1. IBM - What is an Operating System?  
   https://www.ibm.com/think/topics/operating-systems  
   Használat: process management, resource allocation és a több folyamat kezelésének leírása.

2. Oracle Linux Blog - CFS Group Scheduling  
   https://blogs.oracle.com/linux/post/cfs-group-scheduling  
   Használat: modern Linux kernel ütemezési háttér és „ideal multitasking CPU” kontextus.

3. Microsoft - Windows help and learning  
   https://support.microsoft.com/en-us/windows  
   Használat: általános OS-feladatok modern, közérthető összefoglalása.

Megnyitva: `2026-04-08`
