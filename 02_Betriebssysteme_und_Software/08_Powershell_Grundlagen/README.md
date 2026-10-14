# Powershell Grundlagen

## Gyors vizuális kép

| Fogalom        | Jelentés                                         |
| -------------- | ------------------------------------------------ |
| shell          | parancsértelmező környezet                       |
| cmdlet         | PowerShell-parancs                               |
| objektum-alapú | nem csak sima szöveget, hanem objektumokat kezel |
| script         | parancsokból álló `.ps1` fájl                    |

## Mi az a PowerShell?

A PowerShell egy modern parancssori környezet és szkriptnyelv.

Használható:

- rendszeradminisztrációra
- fájlkezelésre
- folyamatkezelésre
- információlekérdezésre
- automatizálásra

## Miért különleges?

Sok hagyományos shell főleg szöveggel dolgozik.  
A PowerShell ezzel szemben **objektumokat** kezel.

Ez azért hasznos, mert:

- strukturáltabb az adatkezelés
- könnyebb szűrni, rendezni, feldolgozni

## Cmdlet névadás

A PowerShell-parancsok tipikus formája:

- `Ige-Főnév`

Példák:

- `Get-Help`
- `Get-Command`
- `Get-ChildItem`
- `Set-Location`
- `Copy-Item`

## Fontos alapparancsok

### Segítség és parancskeresés

| Parancs       | Mire jó?                    |
| ------------- | --------------------------- |
| `Get-Help`    | súgó megjelenítése          |
| `Get-Command` | elérhető parancsok keresése |

Példák:

```powershell
Get-Help Get-ChildItem
Get-Command *Item*
```

### Hely és navigáció

| Parancs        | Mire jó?                    |
| -------------- | --------------------------- |
| `Get-Location` | aktuális hely megjelenítése |
| `Set-Location` | mappaváltás                 |

Példák:

```powershell
Get-Location
Set-Location C:\DEV_SCHOOL
```

### Fájlok és mappák listázása

| Parancs         | Mire jó?                   |
| --------------- | -------------------------- |
| `Get-ChildItem` | fájlok és mappák listázása |

Példák:

```powershell
Get-ChildItem
Get-ChildItem -Force
Get-ChildItem -Recurse
```

### Létrehozás, másolás, mozgatás, törlés

| Parancs       | Mire jó?             |
| ------------- | -------------------- |
| `New-Item`    | új elem létrehozása  |
| `Copy-Item`   | másolás              |
| `Move-Item`   | mozgatás / átnevezés |
| `Remove-Item` | törlés               |

Példák:

```powershell
New-Item -ItemType Directory -Path .\Teszt
Copy-Item .\a.txt .\backup\a.txt
Move-Item .\a.txt .\b.txt
Remove-Item .\b.txt
```

### Tartalom megjelenítése

| Parancs       | Mire jó?                 |
| ------------- | ------------------------ |
| `Get-Content` | fájl tartalmának kiírása |

Példa:

```powershell
Get-Content .\jegyzet.txt
```

## Hasznos aliasok

Windows alatt gyakori PowerShell-aliasok; más platformon az elérhetőség eltérhet:

| Alias | Eredeti parancs |
| ----- | --------------- |
| `ls`  | `Get-ChildItem` |
| `dir` | `Get-ChildItem` |
| `cd`  | `Set-Location`  |
| `cat` | `Get-Content`   |

Fontos:

- vizsgán jobb az eredeti cmdlet-neveket ismerni

## Mire használják a gyakorlatban?

- fájlkezelés
- rendszerinformáció lekérdezés
- automatizált adminisztráció
- szkriptek futtatása
- szerver- és kliensgépek kezelése

## Futtatható példa: objektumok szűrése és rendezése

Feladat: egy kitalált tárhelylistából írjuk ki név szerint azokat a köteteket, ahol 10 GiB-nál kevesebb a szabad hely. A példa PowerShell 5.1-ben és 7-ben futtatható, csak memóriában dolgozik.

```powershell
$volumes = @(
    [pscustomobject]@{ Name = 'DATA'; FreeGiB = 18 }
    [pscustomobject]@{ Name = 'CACHE'; FreeGiB = 4 }
    [pscustomobject]@{ Name = 'BACKUP'; FreeGiB = 8 }
)
$volumes |
    Where-Object { $_.FreeGiB -lt 10 } |
    Sort-Object Name |
    ForEach-Object { '{0}: {1} GiB' -f $_.Name, $_.FreeGiB }
```

Várt kimenet:

```text
BACKUP: 8 GiB
CACHE: 4 GiB
```

A `|` objektumokat ad tovább, a `$_` az éppen feldolgozott objektum. A szűrés számértéket hasonlít össze, a rendezés a `Name` tulajdonságot használja. Szöveg csak az utolsó lépésben készül. Külső parancssori programok kimenete viszont gyakran szöveg.

A Windows PowerShell 5.1 és a több platformon elérhető PowerShell 7 külön kiadás. Az alias tényleges feloldását a `Get-Command ls` mutatja meg. Az előző fájlműveleti parancsok szemléltető részletek, meglévő fájlokat és könyvtárakat feltételeznek; módosítás előtt a támogatott parancsokon a `-WhatIf` segít áttekinteni a tervezett műveletet.

## Vizsgán jól használható megfogalmazás

> A PowerShell a Microsoft objektum-alapú parancssori shellje és automatizálási környezete.  
> Cmdleteket használ, amelyek jellemzően ige-főnév formában vannak elnevezve, például `Get-Help` vagy `Get-ChildItem`.  
> Használható fájlkezelésre, információlekérdezésre és adminisztrációs feladatok automatizálására.

## Gyors önellenőrzés

1. Mi a PowerShell?
2. Mit csinál a `Get-Help`?
3. Mit csinál a `Get-Command`?
4. Mit csinál a `Get-ChildItem`?
5. Melyik parancs vált mappát?
6. Mit jelent az, hogy a PowerShell objektum-alapú?

## Rövid válaszok az önellenőrzéshez

1. Microsoft shell és automatizálási környezet
2. Súgót jelenít meg
3. Parancsokat keres / listáz
4. Fájlokat és mappákat listáz
5. `Set-Location`
6. Nem csak sima szöveggel, hanem strukturált objektumokkal dolgozik

## Források

1. Microsoft Learn - PowerShell Documentation  
   https://learn.microsoft.com/en-us/powershell/  
   Használat: hivatalos PowerShell alapdokumentáció.

2. Microsoft Learn - Get-Help  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-help?view=powershell-7.6  
   Használat: a súgórendszer alapja.

3. Microsoft Learn - Get-Command  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.6  
   Használat: parancskeresés és cmdlet-felfedezés.

4. Microsoft Learn - Get-ChildItem  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.6  
   Használat: listázás fájlrendszerben és más providereknél.

5. Microsoft Learn - Set-Location  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-location?view=powershell-7.6  
   Használat: mappaváltás és aktuális hely kezelése.

6. Microsoft Learn - Copy-Item  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.6  
   Használat: egyszerű fájl- és mappamásolás.

7. Microsoft Learn - Remove-Item  
   https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item?view=powershell-7.6  
   Használat: elemek törlése.

Megnyitva: `2026-04-08`

### A bővítés ellenőrzött forrásai

- [Microsoft: about_Pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines): objektumok a pipeline-ban.

Ellenőrizve: `2026-10-14`.
